# Planning

Deliver a plan without implementation. Keep this boundary even when the change is straightforward.

1. Inspect the architecture, affected callers, project constraints, and available checks. Reuse supplied context after verifying the facts the plan depends on.
2. Resolve technical unknowns through read-only inspection first. Run a prototype only when permitted, in isolated scratch space. Keep product code unchanged. Identify unresolved preferences and unavailable facts.
3. Describe the target behavior and smallest coherent scope. Give each substantial unit an output, affected area, dependencies, and acceptance check. Identify independent units and integration dependencies.
4. For migrations, identify caller changes, legacy deletion, allowed incomplete phases, and each phase's closing check. Address the riskiest unknown early.
5. Specify checks relevant to the change. Include live or performance evidence when the task depends on it. Do not require benchmarks, formal verification, or deployment for every change.
6. Deliver the requested format. Write a plan file when requested or required by project convention. Otherwise, the response can contain the plan. Give a short plan for a small change.

List unresolved decisions and the evidence needed to settle them. Do not create PRs, assign PR numbers, or begin implementation.

If publishing the plan as Feishu work items is also requested, follow [Feishu tasks](issues.md). Reuse or create the authorized records. Publication does not start execution or move those tasks to in progress.
