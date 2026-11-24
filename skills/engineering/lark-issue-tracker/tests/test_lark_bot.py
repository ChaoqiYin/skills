"""Exercise the wrapper through a real fake CLI process on a temporary PATH."""

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


WRAPPER = Path(__file__).resolve().parents[1] / "scripts" / "lark_bot.py"
FAKE_BODY = r'''
import json
import os
from pathlib import Path
import sys

with Path(os.environ["LARK_BOT_TEST_CALLS"]).open("a") as stream:
    stream.write(json.dumps(sys.argv[1:]) + "\n")
response = json.loads(Path(os.environ["LARK_BOT_TEST_RESPONSE"]).read_text())
sys.stdout.write(response.get("stdout", ""))
sys.stderr.write(response.get("stderr", ""))
sys.exit(response.get("exit_code", 0))
'''


class WrapperProcessTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        root = Path(self.directory.name)
        self.calls = root / "calls.jsonl"
        self.response = root / "response.json"
        executable = root / "lark-cli"
        executable.write_text("#!" + sys.executable + "\n" + FAKE_BODY)
        executable.chmod(0o755)
        self.environment = dict(os.environ)
        self.environment.update({
            "PATH": str(root),
            "LARK_BOT_TEST_CALLS": str(self.calls),
            "LARK_BOT_TEST_RESPONSE": str(self.response),
        })

    def run_wrapper(self, arguments, stdout=None, stderr="", exit_code=0):
        if stdout is None:
            stdout = json.dumps({"ok": True, "identity": "bot", "data": {}})
        self.response.write_text(json.dumps({
            "stdout": stdout, "stderr": stderr, "exit_code": exit_code,
        }))
        return subprocess.run(
            [sys.executable, str(WRAPPER), *arguments],
            capture_output=True, text=True, env=self.environment, check=False,
        )

    def recorded_calls(self):
        if not self.calls.exists():
            return []
        return [json.loads(line) for line in self.calls.read_text().splitlines()]

    def assert_local_error(self, result, exit_code):
        self.assertEqual(result.returncode, exit_code)
        self.assertEqual(result.stdout, "")
        envelope = json.loads(result.stderr)
        self.assertIs(envelope["ok"], False)
        self.assertIsNone(envelope["identity"])
        return envelope

    def test_appends_bot_once_and_preserves_payload_exactly(self):
        payload = '{"name": "spaces \\\"quotes\\\"; $(touch /bad) & | >"}'
        arguments = ["base", "+create", "--json", payload]
        result = self.run_wrapper(arguments)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr, "")
        self.assertEqual(json.loads(result.stdout)["identity"], "bot")
        self.assertEqual(self.recorded_calls(), [
            arguments + ["--as", "bot", "--format", "json"],
        ])

    def test_all_supported_domains_and_optional_leading_separator(self):
        for domain in ("base", "drive", "contact"):
            with self.subTest(domain=domain):
                result = self.run_wrapper(["--", domain, "+list"])
                self.assertEqual(result.returncode, 0)
                self.assertEqual(self.recorded_calls()[-1], [
                    domain, "+list", "--as", "bot", "--format", "json",
                ])
        self.assertEqual(len(self.recorded_calls()), 3)

    def test_forbidden_arguments_do_not_start_the_cli(self):
        cases = [
            [], ["base"], ["auth", "login"], ["config", "set"],
            ["profile", "use"], ["api", "request"], ["task", "+list"],
            ["base", "--help"], ["base", "+list", "--"],
            ["--", "--", "base", "+list"],
        ]
        flags = [
            ["--as", "bot"], ["--as", "user"], ["--as=bot"],
            ["--as=user"], ["--as="], ["-q", ".data"], ["-q.data"],
            ["--jq", ".data"], ["--jq=.data"], ["--jq="],
            ["--format", "json"], ["--format=json"], ["--format=text"],
            ["--output", "target"], ["--output=target"],
            ["--output-dir", "target"], ["--output-dir=target"],
            ["--output-file", "target"], ["--output-file=target"],
            ["--output-path", "target"], ["-o", "target"], ["-otarget"],
        ]
        cases.extend(["base", "+list", *flag] for flag in flags)
        for arguments in cases:
            with self.subTest(arguments=arguments):
                self.assert_local_error(self.run_wrapper(arguments), 2)
        self.assertEqual(self.recorded_calls(), [])

    def test_json_payload_values_are_not_interpreted_as_options(self):
        for payload in ('"--as"', '{"--format":"json","--jq":".data"}',
                        '{"argv":["--as","user"],"name":"a b"}'):
            with self.subTest(payload=payload):
                result = self.run_wrapper(["drive", "+create", "--json", payload])
                self.assertEqual(result.returncode, 0)
                self.assertEqual(self.recorded_calls()[-1][3], payload)

    def test_unverified_success_never_reports_success(self):
        cases = [
            '{"ok":true,"identity":"user"}', '{"ok":true}',
            '{"ok":1,"identity":"bot"}', '{"ok":false,"identity":"bot"}',
            '{"code":0,"msg":"ok"}', '[]', 'null', 'broken secret sentinel',
            '{"ok":true,"identity":"bot","data":NaN}',
        ]
        for raw in cases:
            with self.subTest(raw=raw):
                result = self.run_wrapper(["base", "+create"], stdout=raw)
                envelope = self.assert_local_error(result, 1)
                self.assertTrue(envelope["error"]["write_may_have_occurred"])
                self.assertNotIn("sentinel", result.stderr)
        self.assertEqual(len(self.recorded_calls()), len(cases))

    def test_bot_permission_failure_keeps_exit_code_and_never_logs_in(self):
        envelope = {
            "ok": False, "identity": "bot",
            "error": {"type": "authorization", "subtype": "missing_scope",
                      "missing_scopes": ["drive:drive"]},
        }
        arguments = ["drive", "+list"]
        result = self.run_wrapper(arguments, stdout="", stderr=json.dumps(envelope), exit_code=7)
        self.assertEqual(result.returncode, 7)
        self.assertEqual(result.stdout, "")
        self.assertEqual(json.loads(result.stderr), envelope)
        self.assertEqual(self.recorded_calls(), [
            arguments + ["--as", "bot", "--format", "json"],
        ])

    def test_exit_ten_is_not_retried_and_yes_requires_explicit_input(self):
        envelope = {"ok": False, "identity": "bot", "error": {"type": "confirmation"}}
        for explicit_yes in (False, True):
            with self.subTest(explicit_yes=explicit_yes):
                arguments = ["base", "+delete"] + (["--yes"] if explicit_yes else [])
                before = len(self.recorded_calls())
                result = self.run_wrapper(arguments, stdout="", stderr=json.dumps(envelope), exit_code=10)
                self.assertEqual(result.returncode, 10)
                self.assertEqual(json.loads(result.stderr), envelope)
                self.assertEqual(len(self.recorded_calls()), before + 1)
                self.assertEqual(self.recorded_calls()[-1],
                                 arguments + ["--as", "bot", "--format", "json"])

    def test_invalid_failure_keeps_original_nonzero_code_without_raw_output(self):
        cases = [
            "raw sensitive sentinel", '{"ok":false,"identity":"user"}',
            '{"ok":false}', '{"ok":true,"identity":"bot"}', '[]',
        ]
        for exit_code in (1, 7, 10):
            for raw in cases:
                with self.subTest(exit_code=exit_code, raw=raw):
                    result = self.run_wrapper(
                        ["base", "+create"],
                        stdout='{"ok":true,"identity":"bot"}',
                        stderr=raw, exit_code=exit_code,
                    )
                    envelope = self.assert_local_error(result, exit_code)
                    self.assertTrue(envelope["error"]["write_may_have_occurred"])
                    self.assertNotIn("sentinel", result.stderr)

    def test_sensitive_fields_and_bearer_strings_are_redacted(self):
        secret_keys = ["appSecret", "app_secret", "accessToken", "access_token",
                       "refreshToken", "refresh_token", "Authorization", "client_secret"]
        data = {key: "sensitive_sentinel_" + key for key in secret_keys}
        data.update({
            "base_token": "base_resource_token", "file_token": "file_resource_token",
            "nested": [{"appSecret": "nested_sentinel"}],
            "message": "Request Authorization: Bearer bearer_sentinel failed",
            "other": "Authorization Bearer second_sentinel",
            "argv": ["argument_sentinel"], "env": {"X": "environment_sentinel"},
        })
        for failure in (False, True):
            with self.subTest(failure=failure):
                envelope = {"ok": not failure, "identity": "bot", "data": data}
                raw = json.dumps(envelope)
                result = self.run_wrapper(["base", "+list"],
                                          stdout="" if failure else raw,
                                          stderr=raw if failure else "stderr_sentinel",
                                          exit_code=10 if failure else 0)
                self.assertEqual(result.returncode, 10 if failure else 0)
                output = result.stdout + result.stderr
                self.assertNotIn("sentinel", output)
                actual = json.loads(output)["data"]
                for key in secret_keys:
                    self.assertEqual(actual[key], "[REDACTED]")
                self.assertEqual(actual["base_token"], "base_resource_token")
                self.assertEqual(actual["file_token"], "file_resource_token")

    def test_missing_executable_produces_only_a_local_json_error(self):
        (Path(self.directory.name) / "lark-cli").unlink()
        result = self.run_wrapper(["base", "+list"])
        self.assert_local_error(result, 127)
        self.assertEqual(self.recorded_calls(), [])


if __name__ == "__main__":
    unittest.main()
