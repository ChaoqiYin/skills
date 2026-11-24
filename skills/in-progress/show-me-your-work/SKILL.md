---
name: show-me-your-work
description: "Keep a reviewable decision trail for long-running or unattended work: a TSV log with one row per decision (what, why, evidence, result). Local by default; commit it when a reviewer needs the trail to trust the result. Use for /show-me-your-work, autonomous or multi-phase runs, or work a human reviews after stepping away."
disable-model-invocation: true
---

# Show me your work

Keep one canonical log.

## The format

A single TSV file, one row per decision. Cells stay single-line. Evidence is a pointer, not prose.

Copy `references/decision-log-template.tsv` (the header row) to start a clean log. Columns:

- **ts.** ISO8601 timestamp.
- **phase.** The phase or workstream.
- **decision.** What was chosen or done, one line.
- **why.** The reason in plain words. If a principle drove it, say it plainly, not as a jargon tag.
- **evidence.** A link or path that proves it: commit SHA, PR number, `file:line`, or an artifact, trace, or screenshot path. Never a paragraph.
- **result.** The outcome or predicate state: `tests green`, `reverted`, `pixel-diff 0`, `INCONCLUSIVE`, `open`.

An example, plain-spoken so a reviewer reads it at a glance.

```
ts	phase	decision	why	evidence	result
2026-05-24T09:02:00Z	frame	counted the work first, about 100 components and roughly 75 hours	wanted to know the size before starting a long run	commit 3a9f1c2	found 5 things to sort out before starting
2026-05-24T09:40:00Z	harness	took screenshots of the old version before changing anything	so we can compare old against new and catch any visual change	scripts/snapshot.sh, baseline/	saved 120 reference screenshots
2026-05-24T11:15:00Z	widget	moved the widget styles over without changing how it looks	keep the change small and the result identical	commit 7c21e0a, pixel-diff 0	looks identical, tests pass
2026-05-24T12:30:00Z	widget	threw out a helper's work because its screenshots were blank	checked the real files instead of trusting its summary	worktree reset	reverted, tightened the instructions for next time
```

## Logging a row

Write each entry the way you'd tell a teammate what you did. Plain words, concrete actions, no AI speak or abstract jargon (the **unslop** skill applies to log text too).

Use the helper `scripts/log.sh <logfile> <phase> <decision> <why> <evidence> <result>`. It stamps `ts`, writes the header on first use, strips stray tabs/newlines, and prefixes any cell starting with `=`, `+`, `-`, or `@` with a single quote. A bare `printf` appending a row works too, but mind those same bytes if cells come from generated or user-supplied text.

Log decision points and checkpoints, not every action: a fork chosen, a unit completed with its verification result, a pivot or revert with its trigger, a blocker surfaced, a gate fixed. For loop runs, one row per iteration. Skip the trivial and self-evident.

A run is one agent conversation, including its later turns and any summary of it. A pickup, a replacement agent, or a new chat starts a new run. When a run adds to a log that already has rows, its first row has phase `start`, and so does its first row after another run's `start` row. So a run that comes back to a log in a later turn first reads the log's last rows to see whether another run wrote since. A `start` row names the `ts` range of the rows before it that this run did not write, and its evidence names this run using the session identifier exposed by the current harness when available, or a clearly labeled local run identifier. Use phase `start` for nothing else.

## Where it lives

By default the log is a working artifact, not committed. Keep it at `decisions.tsv` in the work dir, or `.audit/<task-slug>.tsv` when several efforts run at once, and leave it out of git.

Commit it only when the work is ambitious enough that a reviewer needs the trail to trust the result.

## Rules

- Append-only. A wrong call gets a new row that supersedes it. Never edit or delete history.
- Prefer evidence produced by committed scripts over hand-made one-offs (the **encode-lessons-in-structure** principle skill).

## Audit the log against the transcript

At the end of the run, before handing back, check the log told the truth. Resolve this run in the active workspace through the current harness's supported history or session interfaces, an explicit export, or a documented local source, and read its source messages and available tool events. Determine transcript access, location, and format from that environment instead of assuming a provider's directory layout. Preserve the originating session identifier, source references, and coverage information. A compacted context or summary is not a complete transcript. When coverage is partial or unavailable, verify the evidence that is accessible and mark the affected transcript checks inconclusive, with the missing coverage named. Walk this run's rows against what actually happened. Each stretch of them begins at one of this run's `start` rows, or at the first row if this run created the log, and ends at the next `start` row of another run:

- Check that every row maps to a real decision or action.
- Check that each row's evidence resolves and shows what the row claims.
- A fork, pivot, or abandoned approach that shaped the work but isn't logged is a gap. Add it.

Correct the log, not the story. The audit never edits or removes a row, even an invented one. When a row records neither a real decision nor a real action, or its claim or evidence is wrong, add a row that supersedes it with what actually happened and a pointer that resolves. This audit does not check rows outside this run's stretches. If this run's own work shows one of them is wrong, supersede it like any wrong call.

## Independent review of the trail

Before handing back, the current agent creates a separate read-only reviewer subagent through the environment's available delegation tools using environment defaults. Give it a fresh conversation, the audit trail, and the originating session identifier, scope, source read access or source-derived snapshot, cutoff, and coverage information. Confirm that it can read the supplied evidence; its own new session is not the run under review. The reviewer flags what the user should pay attention to: a scan for what's suboptimal or risky, not a redo of the work. Self-review is not a substitute. If an independent reviewer cannot run or returns no usable review, report the review as not performed and explain why.

- Decisions logged with weak or absent evidence.
- Verification steps skipped or claimed without proof in the transcript.
- Choices that look risky in hindsight (premature, scope-creeping, papering over a symptom).
- Gaps the user would otherwise miss on a casual skim.

Every reply for a run that produced a trail ends with an "Attention" section. Lead with the reviewer's subagent identifier or assigned name on its own line (`reviewed by <reviewer>`), then list each flag pointing to specific rows or moments. "No flags" is valid only after a completed review with the required evidence coverage. If the review was not performed, say so instead; if transcript coverage was incomplete, name that gap and mark the affected checks inconclusive.

## Reviewing the trail

Read top to bottom, follow the evidence pointers, spot-check.  `column -s$'\t' -t decisions.tsv` renders it in a terminal.

When the work is tracked in Feishu Base and publishing the trail is part of the task, render it as comments on the existing task record. Use the **lark-base** skill to resolve the base, table, record, and view identifiers, then the **lark-drive** skill for record-local comments. Base comments require a record anchor; use the confirmed table, record, and view identifiers rather than a global Base comment. Read the skills' current comment instructions for the exact command and payload.

Render each decision as a short labeled text entry containing all six log columns, in source order. The comment interface supports text, user mentions, and Feishu document links; use multiline text entries rather than assuming TSV or Markdown tables will render as a grid. Keep external URLs and local evidence paths as text; a local path does not become accessible to collaborators merely by appearing in a comment. Include the run identifier and source row numbers so reviewers can trace every entry back to the canonical TSV.

Keep each comment's text within the documented 10,000-character limit, splitting at decision boundaries. Append continuations to the same unresolved record-comment thread when possible, and keep the returned comment and reply identifiers. Before retrying an uncertain write, check for the same run and row range to avoid duplicates. Publish corrections as new entries referring to the superseded rows. The TSV remains the canonical log; comments are a review copy. If the target record is unknown or publishing is not part of the task, prepare the comment text locally and report what is missing.

## Composing this skill

Other skills route their audit trail here instead of inventing one. Reference it by name and let it own the format. Don't restate the columns.
