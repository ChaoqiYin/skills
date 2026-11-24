# Feishu tasks

Combine this playbook with the required technical workflow. `lark-issue-tracker` owns task states, dependencies, and record discussions. Read its instructions and relevant lark dependencies before operating. Use task records, not native Feishu todos or a competing tracker.

## 1. Resolve scope and read the record

Read project instructions and referenced task configuration. Use an explicit task link for a task-specific target. Resolve dependencies by name through the current catalog or discovery metadata. Report missing dependencies without assuming sibling installation directories.

Use lark-base to resolve the Base, table, record, and comment view. A display task number is not a resource ID. Resolve missing or ambiguous targets before remote operations. Continue independent local work when possible.

Read task fields, details, acceptance criteria, dependencies, and relevant comments and replies. For historical decisions or conflicts, include resolved discussions and relevant record history. Follow pagination and filter comments to this record's anchor. Check prerequisite records instead of trusting an old blocker label. Keep the search within scope.

Determine the allowed actions. Reading a task does not change its state. Planning does not start execution. A configured tracker does not grant publication or notification permission. A request to implement and maintain task progress covers relevant record updates within that scope. Do not reconfirm each authorized update.

## 2. Prepare or create work

For requested task creation, check for existing records with the same source or goal. Reuse them or create the requested parent and subtasks in the same table. Link tasks with real record URLs. Store the plan and acceptance criteria in details. Create tables or fields only when initialization was requested.

For implementation, derive the completion check from the task's acceptance criteria and inspect the project. Use [Implementation](implementation.md), [Prototype](prototype.md), or a relevant specialist. For planning or review, preserve the requested boundary. Publish a plan or review to the task only when authorized.

## 3. Execute and report progress

When execution starts and task updates are authorized, set the configured in-progress state and add a concise start comment. Re-read shared data before updates. Preserve others' valid changes and submit only changed fields. Keep current conclusions in details and latest progress. Use comments for decisions, attempts, failures, questions, and evidence.

Give workers the record identity, acceptance criteria, assigned scope, input revision, and allowed actions. By default, the coordinator writes shared task state and comments. Assign one writer for shared remote updates. Integrate worker results and verify evidence before publishing conclusions.

## 4. Handle blockers and replies

Continue work that is possible. When the next step cannot proceed, record the blocker, release condition, responsible person, and resume state. Set the configured blocked status. Check dependencies for self-reference and cycles. Text links do not propagate state changes automatically.

For an authorized question, use the existing record discussion. State the question, evidence, and needed decision. Use real mention elements through lark-drive and lark-contact when notification is within scope. Send a separate chat message only when that action is also authorized. Preserve comment IDs, reply IDs, and pending questions.

On resume, read existing replies and the current record before asking again. Check all blockers before restoring a state. A reply alone does not prove a prerequisite or acceptance condition is met.

## 5. Deliver and accept

Publish requested delivery links and verification evidence. Move to the configured review stage, or acceptance when no review is required. Mark done only after user acceptance or the project's established acceptance rule is satisfied with evidence. A merge alone does not establish acceptance.

Keep PR discussion, CI, and merge operations on the repository host through [Delivery](delivery.md). Link those artifacts from the Feishu task.

For long work, `show-me-your-work` owns the canonical local trail. If publication is requested, let that skill render a review copy in record comments. Local evidence paths become accessible to collaborators only through an authorized upload or another shared location.

## 6. Reconcile and hand back

Follow the connector or CLI's result and consistency contract. Before retrying an uncertain record or comment creation, check the task source, run and row range, or returned identifiers. Avoid duplicate start comments and questions on resumed work.

Return the task number, real record link, current state, completed work, evidence, and unresolved questions. Identify remote operations that failed or lacked authorization. Preserve record and comment IDs for handoff. If Feishu is unavailable, separate local results from pending remote updates. Do not switch trackers silently or claim remote state is current.
