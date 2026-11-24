---
name: lark-issue-tracker
description: Manage requirements and issues in Feishu Base. Use when creating or updating task records, tracking status and dependencies, discussing blockers through comments, or resuming work from task history.
disable-model-invocation: true
---

# Manage Feishu task records

Use the project's existing Base task table. Keep requirements, current state, and execution history in its records. Use record comments for discussions. Do not switch to native Feishu todos or create another tracker.

## Resolve the task and capabilities

Read the actual project instructions and task configuration. `setup-bot` defaults to `docs/agents/issue-tracker.md`; follow the project's actual path. Resolve the task from the supplied link or configured table and record. A display task number is not a resource ID.

Read helper skills through the current catalog before using them:

- `lark-base` for table resolution, records, fields, dependencies, and history.
- `lark-drive` for anchored record comments, replies, and person mentions.
- `lark-contact` for bot-supported lookups of known person identifiers.
- `lark-shared` for CLI identity, output, permission errors, and confirmation gates.

Report unavailable dependencies. Do not assume another skill's directory from the source repository layout. Resolve this skill's own scripts relative to this file.

## Fix the operating identity

Perform all task reads, updates, comments, replies, and person lookups as the application bot. This requirement overrides the user-identity default and examples in helper skills. Do not inherit the CLI's selected identity or use the chat user's login.

Use the [bot-only wrapper](scripts/lark_bot.py) for these operations:

```bash
python3 <resolved-skill-directory>/scripts/lark_bot.py base +record-get --base-token <base-token> --table-id <table-id> --record-id <record-id>
```

The wrapper owns `--as bot` and `--format json`. Do not supply identity, format, output-file, or output-filter flags. Business input such as `--json` remains available. Read command help or schema with the CLI before choosing arguments. Local help and schema inspection do not perform task operations.

The wrapper supports the `base`, `drive`, and `contact` domains. It invokes the CLI once, checks the response identity, and preserves failure codes. It does not grant business authorization, confirm high-risk actions, retry writes, or change authentication. If a required operation is unsupported, record the capability gap instead of bypassing the wrapper. An unverified response does not prove a write failed; reconcile the remote state before retrying.

Use person identifiers from task fields or the project authority mapping. `contact +get-user` can verify a known identifier as the bot. Do not use user-only name search to resolve a person. If a bot-supported method cannot identify the responsible person, record that gap without switching identity.

On bot permission failure, preserve missing scopes or resource-access requirements for the appropriate administrator. Never fall back to `--as user`, run `auth login`, or change global CLI configuration to make the operation succeed. Do not print credentials. Respect the CLI's high-risk confirmation protocol, including exit code `10`; never add a confirmation flag automatically.

## Apply the existing authorization

Read execution, task-update, comment, and mention permissions from the current request or standing project authorization. Record their source and scope. A configured table, bot access, or task assignment alone does not authorize every action. Do not reconfirm actions already covered by valid authorization.

For a read-only assessment or status request, inspect and report without changing records, publishing comments, or starting implementation. Routine authorized execution choices belong to the agent. Workers return genuine blockers to the coordinator, who normally owns task writes and business questions.

Resolve the decision-maker from the task or project authority mapping. Verify their stable identifier and authority for the specific decision. Do not assume the chat user or every task assignee can approve all decisions. A business reply does not replace account-holder authorization or a tool confirmation gate.

## Create and maintain records

Before creating a task, check for an existing record with the same source or goal. Read current fields and state options before updating. Reuse existing names and mappings.

- Keep the task number, title, state, assignee, priority, and latest progress in existing fields.
- Keep the requirement, acceptance criteria, plan, dependencies, current decisions, and delivery links in task details.
- Keep attempts, questions, replies, and supporting evidence in anchored record comments.
- Re-read shared content before writing. Preserve others' valid changes and submit only the intended differences.
- Create tables or fields only when initialization is authorized. Do not add a blocker schema merely to use this workflow.

Use the table's existing state mapping. A new setup can use pending, ready, in progress, blocked, in review, awaiting acceptance, done, and cancelled. Starting execution moves the task to in progress. Delivery moves it to review or acceptance. Mark done only after acceptance under the project's rule. A commit or merge alone is not acceptance.

Return rejected review or acceptance work to in progress. Record the reason when cancelling or reopening a task. For a reopened task, select pending or ready according to its prerequisites. If a prerequisite is cancelled or reopened, recheck known dependent tasks and record the impact.

Reference other records by task number and real record link. Check dependencies for self-reference and cycles. Inspect actual prerequisite records rather than trusting an old blocker label. Text links do not propagate state changes automatically.

## Record a blocker and end the run

Complete independent authorized preparation before raising a question. Check the task's decisions and relevant comments first. Use a stable blocker key based on the task and unresolved decision. Reuse that key across retries and automation runs.

Persist these facts in existing task details, with a durable project handoff as a fallback:

- The blocker key, question, decision scope, and recommended answer.
- The decision-maker's identifier and authority source.
- Release conditions, prerequisite task links, and intended resume state.
- Completed work, accessible evidence, and the next executable step.
- Comment and reply identifiers, notification outcome, and unfinished remote updates.

Use `pending`, `sent`, or `unknown` to distinguish notification outcomes. A timeout is not proof that nothing was sent. Shared task details and comments are the cross-run source; a machine-local temporary file cannot be the sole recovery record for another machine.

Follow this sequence:

1. Re-read the record and related discussion. Reconcile any unfinished write and reuse an existing question for the same blocker.
2. Persist the blocker and recovery facts and set the configured blocked state. Save a durable local intent before remote writes when available.
3. With valid comment and mention authorization, publish the question on the correct record and truly mention the responsible person. Include the blocker key, evidence, recommendation, and required decision. Do not substitute a plain-text name for a mention.
4. Save the returned comment identifier and notification outcome. Re-read the record to verify the blocked state and handoff. Preserve any partial success or uncertain result accurately.
5. End the current task run. Do not wait, listen, sleep, poll for a reply, or start another task in that run. The next existing automation invocation owns the next check.

For Base comments, obtain the actual table, record, and comment-view identifiers required by `lark-drive`. Anchor the comment to that record. Filter returned comments to its anchor and complete relevant comment and reply pagination, including resolved discussions when recovering a decision.

If a comment may have succeeded, find it by blocker key and record anchor before retrying. Check author and content; do not treat an unrelated comment as the question. If the state update or comment fails, preserve the successful parts and pending operations. Do not claim that notification or blocking succeeded without evidence.

If bot access or missing communication authority prevents a remote handoff, save what can be preserved locally and report the unsent operation through an available channel. Do not switch to a user identity or broaden the notification audience. A missing decision-maker follows the configured escalation mapping; if none exists, record the unresolved target instead of guessing.

## Check work on the next automation run

An existing scheduled invocation can execute under standing authorization. This skill does not create a scheduler, listener, or background process. A status-only invocation remains read-only.

1. First inspect durable shared handoffs and reconcile their referenced records regardless of current task state. If no shared handoff index exists, also inspect in-progress records within the authorized scope for unfinished blocker handoffs. Complete pagination. Then scan ready and blocked tasks in that scope. Repair uncertain writes or unsent notifications before selecting work.
2. Start a ready task only with valid execution authority, a clear acceptance check, and satisfied prerequisites. Do not treat every visible record as assigned work.
3. For a blocked task, read the original question and all relevant replies. A valid answer must address the current question and come from a person authorized for that decision. Check later corrections, revocations, and changes in responsibility.
4. Recheck every release condition, permission, and prerequisite. A reply, reaction, acknowledgement, or the bot's own comment alone does not release the task.
5. If all conditions hold, update the task to its appropriate resume state and continue the authorized work. Otherwise keep it blocked and skip it. Do not repeat the question or mention because another run occurred.

A failed notification may be completed after reconciliation when access and authority become available. End that task run after the completed handoff. An already delivered unanswered question stays untouched. A materially new decision may use a new blocker key. Do not invent reminder schedules.

Before resuming, inspect relevant native record history when state conflicts, cancellations, reopened tasks, or ownership changes affect the decision. Do not resume cancelled work or revoked authorization.

## Report the actual outcome

Return the task number, real record link, verified state, completed work, evidence, and unresolved questions. Distinguish successful remote updates from pending or uncertain operations. Include the bot identity and returned operation identifiers when available. Keep local evidence paths separate from artifacts actually accessible to collaborators.
