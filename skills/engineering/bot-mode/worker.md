# Delegated work contract

Complete the bounded task assigned by the coordinator. This contract does not expand the coordinator's authority.

## Brief

Give each worker these inputs:

- The user's goal and the required artifact or answer.
- The assigned scope, relevant project instructions, domain documents, configuration, input paths, and source revision when applicable. Include uncommitted changes when reviewing the working tree.
- The output path or isolated checkout, with permitted edits, processes, and external actions.
- The acceptance check, required evidence, and resolved paths of relevant skills.
- Dependencies on other results and the stopping condition.
- Routine decisions the worker may make, retry limits, and conditions that require escalation to the coordinator.

Resolve missing facts and routine implementation choices from available context. Proceed within the assigned scope without asking the user whether to continue. Return genuine blockers to the coordinator with evidence, attempts, a recommended next action, and release conditions. The coordinator owns questions to business decision-makers. Do not invent permission or change another worker's scope.

## Work

Read the supplied project instructions and relevant documents before acting. Use their resolved paths or supplied contents. Do not assume the coordinator's context is inherited. Follow higher-priority instructions and stay within the writable area. For a review-only task, leave the target unchanged and put permitted reproductions in isolated scratch space.

For Feishu tasks, use the record snapshot and acceptance criteria in the brief. Return progress, blocker questions, and evidence. The coordinator writes shared fields and comments unless the brief assigns that responsibility to this worker. Use `lark-issue-tracker`'s bot-only command wrapper for any assigned task operations. A record link or credential does not authorize comments, mentions, or status changes. If assigned to publish a blocker, save the question and task state, then end the run without waiting for a reply.

Run the acceptance check when possible. Preserve evidence where the coordinator can read it. Report blocked checks without marking them passed. Commit, publish, merge, send messages, or create further workers only when the brief and applicable instructions authorize the action.

## Independent design candidates

When assigned a candidate design, cover the complete core problem using the shared goal, project facts, constraints, and acceptance criteria. Return a concrete design with:

- Data and state ownership, interface contracts, and module boundaries.
- Important failure states and recovery behavior.
- A verification method tied to the requested behavior.
- Alternatives considered and the reasons for the proposed tradeoffs.

Use a separate conversation. Do not receive or read other candidates' first artifacts before returning your own. If inherited context already contains another candidate's result, report the contamination; that attempt cannot count as an independent candidate. Record your worker identifier, input revision or supplied snapshot, and artifact path or returned-result reference. Return the complete design, including known gaps. A progress note or a partial frontend or backend investigation is not a complete candidate. Do not implement the design unless a later brief authorizes implementation after the coordinator's comparison.

## Return

Return `PASS`, `ISSUES`, or `BLOCKED`. Include the result, artifact paths, checks run, observations, unresolved gaps, and task-owned processes or temporary resources still active. Record the input revision and measurement method when the brief specifies them.

The coordinator owns integration and the final verdict. Preserve work until collected. Clean up only resources owned by this task.
