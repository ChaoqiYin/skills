# Feishu tasks

Combine this playbook with the required technical workflow. `lark-issue-tracker` owns task states, dependencies, and record discussions. Read its instructions and relevant lark dependencies before operating. Use task records, not native Feishu todos or a competing tracker.

Use `lark-issue-tracker`'s bot-only wrapper for all task reads, updates, comments, replies, and person lookups. This workflow overrides user-identity defaults in helper examples. Never fall back to a user identity or start user login to fix bot permissions.

## 1. Resolve scope and read the record

Read project instructions and referenced task configuration. Use an explicit task link for a task-specific target. Resolve dependencies by name through the current catalog or discovery metadata. Report missing dependencies without assuming sibling installation directories.

Use lark-base to resolve the Base, table, record, and comment view. A display task number is not a resource ID. Resolve missing or ambiguous targets before remote operations. Continue independent local work when possible.

Read task fields, details, acceptance criteria, dependencies, and relevant comments and replies. For historical decisions or conflicts, include resolved discussions and relevant record history. Follow pagination and filter comments to this record's anchor. Check prerequisite records instead of trusting an old blocker label. Keep the search within scope.

Determine the allowed actions. Reading a task does not change its state. Planning does not start execution. A configured tracker does not grant publication or notification permission. A request to implement and maintain task progress covers relevant record updates within that scope. Do not reconfirm each authorized update.

For an authorized automation sweep, inspect the configured task scope and include ready and blocked tasks. First reconcile records from shared unfinished handoffs regardless of current state. Without a shared handoff index, inspect authorized in-progress records for incomplete blocker handoffs. Ready tasks need current execution authorization, acceptance criteria, and satisfied prerequisites. For blocked tasks, read the original question and all relevant replies. Resume only after every release condition is satisfied, using `lark-issue-tracker`'s decision-authority checks. Skip unanswered tasks without repeating questions or mentions. A read-only sweep reports candidates without starting them or changing records.

## 2. Prepare or create work

For requested task creation, check for existing records with the same source or goal. Reuse them or create the requested parent and subtasks in the same table. Link tasks with real record URLs. Store the plan and acceptance criteria in details. Create tables or fields only when initialization was requested.

For implementation, derive the completion check from the task's acceptance criteria and inspect the project. Use [Implementation](implementation.md), [Prototype](prototype.md), or a relevant specialist. For planning or review, preserve the requested boundary. Publish a plan or review to the task only when authorized.

## 3. Execute and report progress

When execution starts and task updates are authorized, set the configured in-progress state and add a concise start comment. Re-read shared data before updates. Preserve others' valid changes and submit only changed fields. Keep current conclusions in details and latest progress. Use comments for decisions, attempts, failures, questions, and evidence.

Give workers the record identity, acceptance criteria, assigned scope, input revision, allowed actions, routine decision authority, and escalation conditions. Workers solve ordinary execution problems and return genuine blockers to the coordinator. Assign one writer for shared task updates, normally the coordinator. Integrate worker results and verify evidence before publishing conclusions.

## 4. Handle blockers and replies

Complete independent authorized preparation before raising a decision blocker. Check existing decisions and replies first. Use the responsible decision-maker from the task or configured authority mapping, not the chat user by default. A task assignee can approve only decisions within their documented authority.

Follow `lark-issue-tracker`'s blocker handoff sequence. Persist the blocker and recovery information, publish the question in the anchored task discussion, and use real mention elements when authorized. Save comment identifiers and verify the configured blocked state. Send a separate chat message only when separately authorized.

After the handoff, end the current task run. Do not wait, listen, poll for replies, or continue into another task. A later authorized automation run reads the reply and current prerequisites. It restores the appropriate state only after every blocker is resolved.

If a comment or state update fails, preserve the actual outcome and pending operation. A comment may exist even when its response was lost. Reconcile before retrying. If bot access prevents a remote handoff, save a durable local handoff and report the unsent operation through an available channel. Do not claim the owner was notified or the task was blocked when the write was not verified.

## 5. Deliver and accept

Publish requested delivery links and verification evidence. Move to the configured review stage, or acceptance when no review is required. Mark done only after user acceptance or the project's established acceptance rule is satisfied with evidence. A merge alone does not establish acceptance.

Keep PR discussion, CI, and merge operations on the repository host through [Delivery](delivery.md). Link those artifacts from the Feishu task.

For long work, `show-me-your-work` owns the canonical local trail. If publication is requested, let that skill render a review copy in record comments. Local evidence paths become accessible to collaborators only through an authorized upload or another shared location.

## 6. Reconcile and hand back

Follow the connector or CLI's result and consistency contract. Before retrying an uncertain record or comment creation, check the task source, run and row range, or returned identifiers. Avoid duplicate start comments and questions on resumed work.

Return the task number, real record link, current state, completed work, evidence, and unresolved questions. Identify remote operations that failed or lacked authorization. Preserve record and comment IDs for handoff. If Feishu is unavailable, separate local results from pending remote updates. Do not switch trackers silently or claim remote state is current.
