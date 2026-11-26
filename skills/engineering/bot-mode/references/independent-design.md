# Complete the independent-design gate

Require at least two independent candidate subagents when either condition holds:

- The user explicitly requests multiple independent designs or independently generated candidates for comparison. Follow any higher requested count and any specified workflow. An explicit request for another kind of delegation still requires that delegation within its requested scope.
- Implementation requires a design decision about a new or changed cross-module contract, state ownership, permission boundary, or external integration. Also apply the gate to unresolved choices that materially affect module boundaries, the data model, or the user flow.

Mechanical changes and small fixes within established project patterns can proceed directly when neither condition applies. File count, estimated effort, confidence, and a written justification cannot exempt a task that meets a condition. Advice and review remain within their requested deliverables. Architectural subject matter or comparison of already supplied designs alone does not authorize implementation or require new design candidates.

Before the first implementation edit, complete this sequence:

1. Give each candidate the same goal, project facts, constraints, and acceptance criteria in a separate conversation. Assign the complete core design problem, not separate frontend and backend slices. Use [worker contract](../worker.md) for the design artifact contract. Candidates must not receive or read each other's first artifacts before returning their own. Check inherited context as well as explicit briefs. Use a fresh conversation without inherited candidate results when necessary; a new worker identifier alone does not establish independence.
2. Receive at least two complete candidate artifacts. Launching workers, pending results, coordinator-written alternatives, and divided coverage do not meet this requirement. Replace or retry failed candidates. If the required count cannot be reached, report the unmet gate and leave affected implementation blocked.
3. Read every completed candidate. Compare the candidates against the acceptance criteria and record the chosen base, adopted ideas, and rejected tradeoffs. Agreement is valid; do not manufacture differences. Show the worker identifiers, artifact paths or returned-result references, and the decision before implementation.

When the user requests independent candidates without implementation, complete this sequence before finalizing the design deliverable. Do not use the absence of implementation edits to skip requested independent work.

If the user explicitly requests `arena`, follow its full candidate-comparison workflow. An additional independent judge or adversarial review depends on the task's risk or explicit request. Coverage workers and implementation workers do not replace complete independent designs.

Reading, baseline checks, task records, and isolated design artifacts may precede the gate. They remain subject to existing authorization. Do not start implementation while waiting for designs. If scope expands or a material design premise changes, pause affected implementation edits and satisfy the gate for the new scope. Preserve existing work and review it against the selected design; do not automatically roll it back or count it as design evidence.

