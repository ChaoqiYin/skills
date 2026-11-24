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
5. Define the acceptance check before changing anything. Read the relevant principle skills and selected helpers. Execute the playbook.
6. Before the first write, record an execution contract:
   - Task class and deliverable.
   - Acceptance check and the evidence that will prove it.
   - Explicit non-goals.
   - Delegation plan: which independent scopes are delegated, or why solo work is sufficient.
   - Helper availability; name any unavailable helper.
   Do not enter Implementation until this contract exists.

Follow the user's language and scope, project instructions, and higher-priority rules. Keep existing tool restrictions and authorization boundaries. Apply this skill to the active task. Do not claim persistent activation or carry an old task into a clearly new request.

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

Delegate when independent evidence, separate coverage, or isolated implementation units help. The current agent divides work and creates subagents using available tools and environment defaults. Do not require user-selected models, model configuration, or model-identity records.

Use the brief and reporting contract in [worker.md](worker.md). Supply its resolved path and the task-specific inputs. Ensure workers can read relevant project documents, or provide the required contents. A worker cannot expand authorization or override higher-priority instructions.

Give independent workers separate conversations. Respect concurrency limits and use batches when needed. Isolate writers in separate worktrees or directories. Branches alone do not isolate a shared checkout. If isolation is unavailable, collect proposals with one writer or work sequentially. Review worker artifacts and verify the integrated result.

If delegation is unavailable, ordinary work can continue directly with that limitation reported. Preserve the minimum requirements of a requested `arena`, `swarm`, or independent review. Report incomplete work when those requirements cannot be met. Do not simulate independence in one conversation.

### Delegation gate
Substantial work is any change spanning 3+ files, crossing server/client boundaries,
or adding an API contract, configuration, or external integration. Before editing it requires:
- one independent pass for domain/data model and one for UI/integration points,
  or a written justification that a single pass covers both;
- an independent design review when interfaces or ownership are unresolved;
- a brief and returned evidence for every worker.

When a named helper is unavailable, substitute a general-purpose agent for the same
independent scope and report the substitution. Never silently downgrade to solo work.

## Evidence and finish

For configured Feishu work, combine the task playbook with the relevant technical playbook. Assign one writer for shared task state and comments, normally the coordinator. Workers return proposed updates and evidence. Keep code delivery status separate from task acceptance. A commit, merge, or worker `PASS` does not mean the task is accepted.

Exercise the requested behavior or inspect the actual artifact. Report evidence relevant to the acceptance check. Distinguish baseline failures, regressions, skipped checks, and unavailable capabilities. Verify worker claims against their artifacts.

Access conversation history through the environment's supported session interface, explicit exports, or documented local sources. Preserve source identifiers and report coverage gaps. A summary is not a complete transcript.

Stop when the deliverable passes its checks, the user stops the run, an agreed limit is reached, or a concrete prerequisite blocks progress. Finish authorized preparation before requesting missing permission. Do not ask again for existing authorization. A request to work autonomously does not authorize messages, publication, deployment, or merging.

Lead the final reply with the outcome. Describe the change or finding, supporting evidence, and remaining limitations. Follow the user's language and project output conventions.
