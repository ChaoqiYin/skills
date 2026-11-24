---
name: why
description: "Use for 'why does X work this way', 'why we picked Y', design rationale, regressions, postmortems, or data-backed thresholds. Returns a cited read on decisions and tradeoffs. Use how for runtime behavior."
disable-model-invocation: true
---

# Why

Answer from the record, not the code: read the commits and PR discussions that introduced the target and each later change, and other sources if the trail is thin. Cite what the authors wrote, mark your own inferences as inferences, and say what the record does not answer.

Use the project's configured issue backend for requirement and decision discussions. For Feishu, resolve lark-issue-tracker and its dependencies, and read the relevant task details, record comments/replies, and per-record history when needed. Keep the investigation read-only. Cite real record links and comment identifiers; do not assume every decision lives in a code-host issue.
