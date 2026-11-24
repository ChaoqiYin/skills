# Session

Resume one known task, prepare a handoff, or pause safely. For recent work across several sessions, consider `recall`.

## Resume

1. Read the supplied handoff, branch, or session reference. Access history through the environment's supported session interface, an explicit export, or a documented local source. Do not assume provider-specific transcript paths or filenames.
2. Recover the goal, user corrections, authorized scope, decisions, completed checks, open work, and owned processes. Preserve source identifiers and evidence references. Report history gaps. A summary can orient the task without proving the complete conversation was reviewed.
3. For Feishu work, read current details and relevant replies through [Feishu tasks](issues.md). Include the record link and ID, blocker keys, comment IDs, decision-makers, release conditions, unfinished remote updates, and next action in the handoff. Confirm that an authorized reply and all prerequisites remove the blocker before resuming. Do not repeat an existing question.
4. Compare recovered context with the current tree, branch, artifacts, and accessible external state. Inspect uncommitted changes. Do not repeat completed external actions because a handoff lists them as pending.
5. Resume when the current request or standing automation authorization covers execution. An authorized scheduled run does not need another user confirmation. A request for status or review remains read-only. For a scheduled task sweep, follow the selection and recovery rules in [Feishu tasks](issues.md).

## Pause or hand off

Preserve work and evidence. At the requested handoff location, record the goal, paths, revision, changed files, checks and outcomes, unfinished step, blockers, and next action. Include authorization boundaries that affect continuation.

Stop or transfer task-owned processes when appropriate, preserving outputs first. Preserve user changes and shared resources. Do not create a commit merely to tidy a pause. If work cannot continue after the turn, state that limitation.

After a task question and blocked handoff, end the current task run. Do not start a listener, wait loop, or another task in that run. A later automation invocation owns the next check; this playbook does not create a scheduler.
