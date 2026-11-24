# Delegated work contract

Complete the bounded task assigned by the coordinator. This contract does not expand the coordinator's authority.

## Brief

Give each worker these inputs:

- The user's goal and the required artifact or answer.
- The assigned scope, relevant project instructions, domain documents, configuration, input paths, and source revision when applicable. Include uncommitted changes when reviewing the working tree.
- The output path or isolated checkout, with permitted edits, processes, and external actions.
- The acceptance check, required evidence, and resolved paths of relevant skills.
- Dependencies on other results and the stopping condition.

Resolve missing facts from available context. Report an ambiguity that affects the task. Do not invent permission or change another worker's scope.

## Work

Read the supplied project instructions and relevant documents before acting. Use their resolved paths or supplied contents. Do not assume the coordinator's context is inherited. Follow higher-priority instructions and stay within the writable area. For a review-only task, leave the target unchanged and put permitted reproductions in isolated scratch space.

For Feishu tasks, use the record snapshot and acceptance criteria in the brief. Return progress, blocker questions, and evidence. The coordinator writes shared fields and comments unless the brief assigns that responsibility to this worker. A record link or credential does not authorize comments, mentions, or status changes.

Run the acceptance check when possible. Preserve evidence where the coordinator can read it. Report blocked checks without marking them passed. Commit, publish, merge, send messages, or create further workers only when the brief and applicable instructions authorize the action.

## Return

Return `PASS`, `ISSUES`, or `BLOCKED`. Include the result, artifact paths, checks run, observations, unresolved gaps, and task-owned processes or temporary resources still active. Record the input revision and measurement method when the brief specifies them.

The coordinator owns integration and the final verdict. Preserve work until collected. Clean up only resources owned by this task.
