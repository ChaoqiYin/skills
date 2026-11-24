#!/usr/bin/env python3
"""Run one Lark CLI command using lark-shared's bot JSON output contract."""

import json
import re
import subprocess
import sys


DOMAINS = frozenset({"base", "drive", "contact"})
SECRET_KEYS = frozenset({
    "appsecret", "app_secret", "accesstoken", "access_token",
    "refreshtoken", "refresh_token", "authorization", "client_secret",
})
BEARER_HEADER = re.compile(
    r"\b(Authorization\s*(?::|=)?\s*Bearer\s+)[^\s,;\"'\]\}]+",
    re.IGNORECASE,
)


def sanitize(value):
    """Redact explicit credential fields and authorization header strings."""
    if isinstance(value, dict):
        return {
            key: "[REDACTED]"
            if key.casefold() in SECRET_KEYS or key.casefold() in {"argv", "env"}
            else sanitize(item)
            for key, item in value.items()
        }
    if isinstance(value, list):
        return [sanitize(item) for item in value]
    if isinstance(value, str):
        return BEARER_HEADER.sub(r"\1[REDACTED]", value)
    return value


def emit(envelope, stream):
    print(json.dumps(sanitize(envelope), ensure_ascii=True, allow_nan=False), file=stream)


def reject(error_type, message, exit_code=2, uncertain=False):
    envelope = {
        "ok": False,
        "identity": None,
        "error": {"type": error_type, "message": message},
    }
    if uncertain:
        envelope["error"]["write_may_have_occurred"] = True
        envelope["error"]["hint"] = (
            "Verify the target resource before any further action. "
            "The wrapper did not retry."
        )
    emit(envelope, sys.stderr)
    return exit_code


def forbidden_option(argument):
    name = argument.split("=", 1)[0]
    return (
        name in {"--as", "--jq", "--format", "--output", "--out"}
        or name.startswith("--output-")
        or argument.startswith("-q")
        or (argument.startswith("-o") and not argument.startswith("--"))
    )


def reject_constant(value):
    raise ValueError(value)


def parse_envelope(raw, expected_ok):
    try:
        envelope = json.loads(
            raw,
            parse_constant=reject_constant,
        )
    except (ValueError, RecursionError):
        return None
    if (
        not isinstance(envelope, dict)
        or envelope.get("ok") is not expected_ok
        or envelope.get("identity") != "bot"
    ):
        return None
    return envelope


def main(arguments):
    if arguments[:1] == ["--"]:
        arguments = arguments[1:]
    if (
        len(arguments) < 2
        or arguments[0] not in DOMAINS
        or not arguments[1]
        or arguments[1].startswith("-")
        or "--" in arguments
        or any(forbidden_option(argument) for argument in arguments)
    ):
        return reject(
            "invalid_arguments",
            "Expected base, drive, or contact and a command. Identity, format, "
            "filter, output redirection, and internal separator options are forbidden.",
        )
    try:
        result = subprocess.run(
            ["lark-cli", *arguments, "--as", "bot", "--format", "json"],
            capture_output=True,
            text=True,
            errors="replace",
            check=False,
        )
    except OSError:
        return reject("launch_failed", "Unable to launch lark-cli.", exit_code=127)

    exit_code = result.returncode
    if exit_code < 0:
        exit_code = 128 - exit_code
    envelope = parse_envelope(
        result.stdout if exit_code == 0 else result.stderr,
        expected_ok=exit_code == 0,
    )
    if envelope is None:
        return reject(
            "invalid_upstream_envelope",
            "The CLI result could not be verified as a bot JSON envelope. "
            "A write may already have occurred.",
            exit_code=exit_code or 1,
            uncertain=True,
        )
    emit(envelope, sys.stdout if exit_code == 0 else sys.stderr)
    return exit_code


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
