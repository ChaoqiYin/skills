# Starting prompts

Adapt one matching example to the user's task. Use the active environment's supported skill-invocation syntax.

## Choose a workflow

> Use bot-help to recommend a workflow for intermittent checkout failures. Explain its output. Do not investigate yet.

## Configure the project

> Use setup-bot for the project at the supplied path. Write domain-documentation conventions and minimal task configuration. Reuse existing equivalents. Configure the Feishu task-table link and verify the agent's access. Ask for a link if none is configured. Do not create tables or publish test comments.

## Execute a Feishu task

> Use bot-mode to implement this Feishu task. Read its requirements and discussions. Maintain progress and blockers in the record. Post verification evidence when the change is ready for acceptance. Do not merge or mark it accepted on my behalf.

## Move existing issues

> Use bot-mode to plan importing the specified project issues into its configured Feishu task table. Follow lark-issue-tracker's task conventions. Provide field and status mappings, duplicate checks, and an import preview. Do not write remote data.

## Implement a feature

> Use bot-mode to add an empty state to saved searches. Follow the existing design. Verify the empty and populated states. Keep unrelated cleanup out.

## Fix a bug

> Use bot-mode to fix the duplicate submission in this reproduction. Find the cause, add a behavioral regression test, and rerun the reproduction.

## Plan without implementing

> Use bot-mode to plan the legacy cache API migration. Identify callers, phase dependencies, and verification boundaries. Do not change product code.

## Compare designs

> Use arena to create independent parser-interface candidates. The current agent should create the subagents, compare their artifacts, and verify the combined result.

## Review a change

> Use interrogate to review this branch for reproducible defects. Report evidence and coverage gaps. Do not apply fixes.

## Resume work

> Use bot-mode to resume this branch from the handoff. Verify its claims against the current tree. Continue unfinished implementation within the recorded scope.

## Run a bounded task

> Use bot-mode to fix the failing import cases until they pass or a missing external prerequisite blocks progress. Keep a concise decision trail and report unverified cases. Do not publish or merge.
