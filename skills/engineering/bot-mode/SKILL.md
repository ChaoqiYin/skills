---
name: bot-mode
description: "Coordinate task workflows, relevant principles, subagents, and verification. Use for bot-mode or requests to orchestrate a task through completion. Use bot-help for skill-selection advice."
metadata:
  internal: true
---

# Bot mode

Own the task through verification. Choose a playbook, read the required guidance, and coordinate delegated work through available subagent tools.

Work in the actual project identified by the request and active context. Keep its root separate from the skill source repository and installed skills. Resolve project commands and edits against that root. If only the skill repository is known, identify the target project before editing.

## Start

1. Read the goal, deliverable, scope, and existing authorization. Inspect project instructions and working state. Preserve unrelated user changes.
2. Read referenced domain documents and configuration. Setup-bot defaults to `docs/agents/domain.md` and `docs/agents/issue-tracker.md`. Follow the project's actual paths. Read the relevant glossary and architecture decision records as directed. Resolve the tracker from configuration. Discover tools and verification commands from the project. Continue without setup when available information is sufficient.
3. Distinguish advice, investigation, planning, review, and execution. Keep plan-only and review-only work within those deliverables. Proceed through implementation and verification when requested. Route setup to `setup-bot` and skill-selection questions to `bot-help`. Suggest setup only when missing configuration affects the task.
4. Select the closest playbook. For substantial work, track phases with a task-list tool or written checklist. Handle a small, obvious change directly.
5. Before implementation, record the task class, authorized scope, deliverable, acceptance check, and required evidence. State whether the independent-design gate below applies, citing the actual design decisions or the user's requirement. Report unavailable capabilities needed by the chosen workflow. Use the phase checklist or a short in-chat record; a separate file is optional.
6. Read the relevant principle skills and selected helpers. Satisfy required design and review steps before implementation. A delegation plan alone does not satisfy them. Execute the playbook within the recorded scope.

Follow the user's language and scope, project instructions, and higher-priority rules. Keep existing tool restrictions and authorization boundaries. Apply this skill to the active task. Do not claim persistent activation or carry an old task into a clearly new request.

## Default autonomy

Complete authorized investigation, design, implementation, verification, and repairs without asking whether to proceed. Make routine reversible decisions and explain them with the result. Apply this rule from the start; it does not depend on a separate invocation of `principle-never-block-on-the-human`.

Give workers decision authority, retry limits, and escalation conditions in their briefs. Workers resolve ordinary implementation questions themselves. They return genuine blockers to the coordinator instead of asking the user for permission to continue. The coordinator replaces failed workers within existing limits without seeking routine confirmation. Preserve required design gates and explicit resource limits.

For a decision that needs a person, use the configured Feishu task discussion and the responsible decision-maker. Follow [Feishu tasks](playbooks/issues.md) and `lark-issue-tracker`. After recording the question, blocked state, and handoff, end the current task run. Do not wait for a reply. The next authorized automation run checks whether execution can resume.

Autonomy preserves the requested deliverable and existing authority. Advice, planning, and review remain within their scope. Use existing authorization for task updates, comments, and mentions. A task link alone does not grant that authorization. Report inaccessible task discussions or missing account-holder approval through the available channel after preserving the handoff. Do not turn a business reply into approval for unrelated actions or bypass a tool's confirmation gate.

## Playbooks

| Task | Read |
|---|---|
| Explain behavior, trace a decision, diagnose without fixing, or review | [Investigation](playbooks/investigation.md) |
| Produce a plan without implementation | [Planning](playbooks/planning.md) |
| Add a feature, fix a bug, improve performance, refactor, or migrate | [Implementation](playbooks/implementation.md) |
| Settle a technical uncertainty or compare candidate shapes | [Prototype](playbooks/prototype.md) |
| Prepare a PR, address review or CI, publish, or merge within authorization | [Delivery](playbooks/delivery.md) |
| Resume a known task, hand off, or pause safely | [Session](playbooks/session.md) |
| Create, revise, or evaluate a skill | [Authoring a skill](playbooks/authoring-a-skill.md) |
| Execute, discuss, resume, or update a requirement or issue in Feishu | [Feishu tasks](playbooks/issues.md) |

Read only the playbooks the task needs. For example, a requested bug fix can use investigation followed by implementation. Playbooks are local documents, not installed commands. Use Implementation's long-run guidance for extended work. For large tasks without a suitable sequence, consider `figure-it-out`. Follow its workflow without routing recursively back here.

## Specialist skills

Resolve each helper by its exact name through the current catalog or discovery metadata. Follow invocation restrictions. Locate another skill before reading its internal resources. Resolve this skill's relative links from the containing file.

Read a selected helper before using it. Follow its scope, dependencies, and stopping conditions. If it is unavailable, report the limitation. Use a direct approach only when it meets the requested contract. A direct attempt does not count as an independent review or candidate comparison.

Choose helpers by task:

| Need | Skill |
|---|---|
| Interfaces and ownership | `architect` |
| Independent candidate artifacts | `arena` |
| Divided coverage or worker races | `swarm` |
| Runtime explanation, historical rationale, or teaching | `how`, `why`, `teach` |
| Adversarial review or effects beyond the diff | `interrogate`, `blast-radius` |
| Test-first bug repair | `tdd` |
| Create or maintain a project verification tool | `create-verification-skill`, `maintain-verification-skill` |
| Decision trail for long work | `show-me-your-work` |
| Recent session context or current-chat summary | `recall`, `ketchup` |
| Feishu requirements, task states, dependencies, and discussions | `lark-issue-tracker` |
| Project configuration | `setup-bot` |
| Documents, plans, PR descriptions, and commit messages | `technical-writing`, with `unslop` |

Use the project's existing checks for ordinary verification. Create or maintain a verification tool only when the task includes that work. Use `lark-issue-tracker`'s current lark dependencies for the requested Feishu operations. Preserve project templates and the user's language when writing. Apply other available guidance, including language-specific or formal-verification skills, when relevant. Skill availability does not expand task scope.

## Principles

Locate a principle by the exact skill name in parentheses. Read its full instructions when the trigger applies. Load only relevant principles. Explain a principle when it clarifies an actual decision.

| Trigger | Principle |
|---|---|
| Size a change or consider another abstraction | Laziness Protocol (`principle-laziness-protocol`) |
| Choose core types, data structures, or shared scaffolding | Foundational Thinking (`principle-foundational-thinking`) |
| Integrate a requirement into an existing design | Redesign from First Principles (`principle-redesign-from-first-principles`) |
| Repeated fixes fail under the same assumption | Attack the Premise (`principle-attack-the-premise`) |
| Sequence an addition, rewrite, or cleanup | Subtract Before You Add (`principle-subtract-before-you-add`) |
| Simplify code that is hard to trace | Minimize Reader Load (`principle-minimize-reader-load`) |
| Execute a migration with explicit verification boundaries | Outcome-Oriented Execution (`principle-outcome-oriented-execution`) |
| Weigh product or interaction tradeoffs | Experience First (`principle-experience-first`) |
| Explore a novel interaction or architectural shape | Exhaust the Design Space (`principle-exhaust-the-design-space`) |
| Repeated or non-trivial work benefits from a reusable tool | Build the Lever (`principle-build-the-lever`) |
| Model stateful logic or repeated shape assumptions | Model the Domain (`principle-model-the-domain`) |
| Handle inputs, validation, errors, or adapters | Boundary Discipline (`principle-boundary-discipline`) |
| Design types or typed function signatures | Type System Discipline (`principle-type-system-discipline`) |
| Design retryable commands or lifecycle operations | Make Operations Idempotent (`principle-make-operations-idempotent`) |
| Replace an internal API and migrate its callers | Migrate Callers Then Delete Legacy APIs (`principle-migrate-callers-then-delete-legacy-apis`) |
| Concurrent workers might share writable state | Separate Before Serializing Shared State (`principle-separate-before-serializing-shared-state`) |
| Claim the task is complete | Prove It Works (`principle-prove-it-works`) |
| Diagnose a failure | Fix Root Causes (`principle-fix-root-causes`) |
| Sequence a sweep, migration, or multi-part change | Sequence Work into Verifiable Units (`principle-sequence-verifiable-units`) |
| Write or change tests | Test Behavior, Not Implementation (`principle-test-behavior-not-implementation`) |
| Large reads or fan-out consume the conversation | Guard the Context Window (`principle-guard-the-context-window`) |
| Consider asking for a routine reversible step | Never Block on the Human (`principle-never-block-on-the-human`) |
| A correction keeps recurring | Encode Lessons in Structure (`principle-encode-lessons-in-structure`) |

Keep verification boundaries explicit. An expected failing TDD test or incomplete migration phase is not ready for delivery. Check each phase's declared condition before advancing. Require final acceptance checks before declaring completion. Do not add disposable compatibility layers to disguise incomplete work or use migration guidance to dismiss unexpected regressions.

## Subagents

Apply the independent-design gate below before implementation. Outside required delegation, delegate when independent evidence, separate coverage, or isolated implementation units help. Create subagents using available tools and environment defaults. Do not require user-selected models, model configuration, or model-identity records.

Use the brief and reporting contract in [worker.md](worker.md). Supply its resolved path and the task-specific inputs. Ensure workers can read relevant project documents, or provide the required contents. A worker cannot expand authorization or override higher-priority instructions.

Give independent workers separate conversations. Respect concurrency limits and use batches when needed. Isolate writers in separate worktrees or directories. Branches alone do not isolate a shared checkout. If isolation is unavailable, collect proposals with one writer or work sequentially. Review worker artifacts and verify the integrated result.

### Independent-design gate

Require at least two independent candidate subagents when either condition holds:

- The user explicitly requests multiple independent designs or independently generated candidates for comparison. Follow any higher requested count and any specified workflow. An explicit request for another kind of delegation still requires that delegation within its requested scope.
- Implementation requires a design decision about a new or changed cross-module contract, state ownership, permission boundary, or external integration. Also apply the gate to unresolved choices that materially affect module boundaries, the data model, or the user flow.

Mechanical changes and small fixes within established project patterns can proceed directly when neither condition applies. File count, estimated effort, confidence, and a written justification cannot exempt a task that meets a condition. Advice and review remain within their requested deliverables. Architectural subject matter or comparison of already supplied designs alone does not authorize implementation or require new design candidates.

Before the first implementation edit, complete this sequence:

1. Give each candidate the same goal, project facts, constraints, and acceptance criteria in a separate conversation. Assign the complete core design problem, not separate frontend and backend slices. Use [worker.md](worker.md) for the design artifact contract. Candidates must not receive or read each other's first artifacts before returning their own. Check inherited context as well as explicit briefs. Use a fresh conversation without inherited candidate results when necessary; a new worker identifier alone does not establish independence.
2. Receive at least two complete candidate artifacts. Launching workers, pending results, coordinator-written alternatives, and divided coverage do not meet this requirement. Replace or retry failed candidates. If the required count cannot be reached, report the unmet gate and leave affected implementation blocked.
3. Read every completed candidate. Compare the candidates against the acceptance criteria and record the chosen base, adopted ideas, and rejected tradeoffs. Agreement is valid; do not manufacture differences. Show the worker identifiers, artifact paths or returned-result references, and the decision before implementation.

For an explicitly requested design or comparison without implementation, complete this sequence before finalizing that deliverable. Do not use the absence of implementation edits to skip requested independent work.

Use `arena` for its full candidate-comparison workflow when applicable and permitted. An additional independent judge or adversarial review depends on the task's risk or explicit request. Coverage workers and implementation workers do not replace complete independent designs.

Reading, baseline checks, task records, and isolated design artifacts may precede the gate. They remain subject to existing authorization. Do not start implementation while waiting for designs. If scope expands or a material design premise changes, pause affected implementation edits and satisfy the gate for the new scope. Preserve existing work and review it against the selected design; do not automatically roll it back or count it as design evidence.

### Unavailable capabilities

Distinguish a missing helper skill, restricted invocation, and unavailable subagent tools. If an optional helper is missing but delegation is available, follow the gate and worker contract directly and report the substitution. Do not claim to have executed the missing helper. Preserve the full contract of an explicitly requested skill; report an unmet requirement when it cannot be fulfilled.

Respect concurrency limits. Independent conversations may run in batches or sequentially. If required delegation is unavailable or prohibited, continue possible investigation, baseline checks, and acceptance preparation. Report the capability gap and stop before affected implementation. Do not silently downgrade to solo work or simulate independence. The coordinator's justification cannot waive required delegation; only a changed user instruction or a higher-priority rule can change the applicable requirement. Work that does not require delegation can continue directly.

## Evidence and finish

For configured Feishu work, combine the task playbook with the relevant technical playbook. Assign one writer for shared task state and comments, normally the coordinator. Workers return proposed updates and evidence. Keep code delivery status separate from task acceptance. A commit, merge, or worker `PASS` does not mean the task is accepted.

Exercise the requested behavior or inspect the actual artifact. Report evidence relevant to the acceptance check. Distinguish baseline failures, regressions, skipped checks, and unavailable capabilities. Verify worker claims against their artifacts.

Access conversation history through the environment's supported session interface, explicit exports, or documented local sources. Preserve source identifiers and report coverage gaps. A summary is not a complete transcript.

Stop when the deliverable passes its checks, the user stops the run, an agreed limit is reached, or a concrete prerequisite blocks progress. Finish authorized preparation before requesting missing permission. Do not ask again for existing authorization. A request to work autonomously does not authorize messages, publication, deployment, or merging.

Lead the final reply with the outcome. Describe the change or finding, supporting evidence, and remaining limitations. For required delegation, report the actual workers, covered scope, candidate artifacts, decision, and any missing results or capabilities. A claim that delegation occurred is not evidence without real worker results. Follow the user's language and project output conventions.
