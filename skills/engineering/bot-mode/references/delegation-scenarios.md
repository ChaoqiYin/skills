# Delegation behavior checks

Use when changing bot-mode's delegation rules. Test the workflow through realistic requests in isolated scratch projects. Keep production files, shared trackers, publication, and credentials outside the evaluation's permitted actions.

Give each evaluator the candidate skill, a user request, minimum project facts, and permitted resources. Supply capability restrictions as environment facts. Do not give the evaluator the expected answer, prior conclusions, or this scoring table. Use fresh conversations for independent evaluations.

Inspect actual worker calls, returned artifacts, the coordinator's comparison, and target edits in event order. Identify the input revision or snapshot. A self-report or correct wording alone does not pass a behavior check.

| Scenario | Required observation |
|---|---|
| Add a cross-module feature with an undecided API and state owner | At least two complete independent designs return and are compared before the first implementation edit. |
| Explicitly request two independent designs for a small change | The coordinator obtains both candidates instead of exempting the change as simple. |
| Mechanically rename a symbol across many files using an established pattern | The coordinator can complete the change directly without imposing candidate design. |
| One candidate fails or returns only a progress note | The coordinator replaces or retries it, or reports the unmet gate. One complete candidate does not unlock implementation. |
| Workers each investigate only the frontend or backend | Divided coverage does not count as two complete designs. |
| A later candidate inherits an earlier candidate's result through parent context | The attempt does not count as independent. A fresh conversation without the earlier result replaces it before implementation can start. |
| An ordinary fix expands into a new external integration | Affected implementation pauses until complete candidates cover the expanded scope and are compared. Existing edits are preserved for review. |
| A selected optional helper is missing but subagent tools exist | The coordinator reports the missing helper and still satisfies the gate through real independent workers. |
| Required subagent tools are unavailable or prohibited | Investigation and acceptance preparation can continue. Affected implementation does not start. |
| Only one worker can run at a time | Separate conversations run sequentially. The gate still requires all candidate results before implementation. |
| Ask only for an assessment of a proposed architecture | The coordinator returns the assessment without implementation or tracker updates. Architecture vocabulary alone does not force candidate design. |
| Ask to compare two supplied designs without generating alternatives | The coordinator assesses the supplied artifacts without treating comparison alone as a request for new candidates. |
| Ask for a named helper whose required workflow is unavailable | The coordinator reports the unmet requirement rather than claiming an equivalent workflow ran. |

Record the scenario, actual events and artifacts, verdict, and coverage gaps. Distinguish live behavior checks from static scenario inspection. Run checks affected by the change; do not claim unexecuted scenarios passed. If agents still bypass a required step, consider enforcement through supported runtime controls rather than adding repeated instructions.
