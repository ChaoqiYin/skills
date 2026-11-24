---
name: bot-help
description: "Explain skill usage, recommend workflows, and troubleshoot skill discovery. Use for bot-help, skill-selection questions, or help getting started with bot-mode."
metadata:
  internal: true
---

# Bot help

Recommend a next step using skills available to the current agent. Use `bot-mode` for execution and `setup-bot` for domain documentation and project configuration.

## Answer from the current collection

1. Identify whether the user wants an explanation, recommendation, setup help, or execution. Recommending a workflow does not authorize execution. If the user requests the work, continue through `bot-mode` in the same turn when available and permitted.
2. Read the current skill catalog and relevant project instructions. Read a selected skill's description and body before describing its behavior, dependencies, or invocation method.
3. Recommend the smallest workflow that meets the goal. State its output and required capabilities. Give one primary recommendation. Include an alternative only when the distinction matters.
4. Use the user's requested language. Give at most one example prompt unless the user requests several examples or a catalog. Link to the source you consulted.

Resolve skill names through the environment's catalog or discovery metadata. Locate another skill before resolving resources inside it. Use its actual installation location. Skills can be installed independently outside the project. Report missing dependencies. Follow invocation restrictions, and promise a command or persistent mode only when the environment supports it.

## Choose a capability

| User needs | Start here |
|---|---|
| One entry point to plan, execute, and verify a task | `bot-mode` |
| Configure project activation, capabilities, verification, or Feishu bindings | `setup-bot` |
| Track requirements, issues, dependencies, and record-comment discussions in Feishu | `lark-issue-tracker` |
| Write docs, plans, PR descriptions, or commit messages | `technical-writing` |
| Remove filler and AI writing patterns | `unslop` |
| Understand runtime behavior or ownership | `how` |
| Understand the reasons behind a decision | `why` |
| Learn a subsystem or change in plain language | `teach` |
| Restate the goal before proceeding | `in-your-own-words` |
| Improve a task prompt without expanding its scope | `sharpen` |
| Simplify the previous explanation | `bro` |
| Rebuild working context across recent sessions | `recall` |
| Catch up on this conversation | `ketchup` |
| Design interfaces, types, and module boundaries | `architect` |
| Compare independent attempts at the same artifact | `arena` |
| Split coverage across independent workers or race attempts | `swarm` |
| Find proven defects with independent adversarial review | `interrogate` |
| Investigate breakage beyond the changed lines | `blast-radius` |
| Fix a bug through a test-first loop | `tdd` |
| Apply TypeScript-specific implementation guidance | `typescript-best-practices` |
| Create or refresh a project-local verification workflow | `create-verification-skill`, `maintain-verification-skill` |
| Model an invariant or maintain its formal verification | `create-formal-verification-skill`, `maintain-formal-verification-skill` |
| Explain user-visible states with a checked model | `statechart` |
| Design a rigorous workflow for an ambitious change | `figure-it-out` |
| Keep and review a decision trail | `show-me-your-work` |
| Turn a recurring correction into project guidance | `correct` |

Check the catalog for skills absent from this table. Use the Principles section of `bot-mode` to find relevant `principle-*` skills.

Distinguish these workflows when the request could fit more than one:

- `arena` compares complete candidate artifacts. `swarm` divides coverage or races workers and consolidates reports. `interrogate` tries to break a change and reports verified defects without applying fixes.
- `recall` reconstructs work across sessions. `ketchup` summarizes this conversation. To resume one known branch or session, read the `bot-mode` skill's `playbooks/session.md`.
- The `bot-mode` skill's `playbooks/planning.md` delivers a plan. `figure-it-out` designs and executes a workflow. Preserve a plan-only request's boundary.

## Setup and troubleshooting

Read project instructions and referenced configuration before recommending setup changes. For installation or discovery questions, consult the active agent's documented discovery rules. Report the recognized path and invocation method when known. Explain `setup-bot` for advice requests. Run it only when configuration is requested.

Describe the two setup outputs when asked. Domain conventions default to `docs/agents/domain.md`. Configuration defaults to `docs/agents/issue-tracker.md`. Reuse the project's existing equivalents. Feishu configuration can contain only the confirmed task-table link, with overrides where needed. If no valid link exists, ask the user for one and verify the agent's access. A saved link does not prove access.

For Feishu work, consult the configured task table and `lark-issue-tracker`. Fields and details hold current task state. Record comments hold discussions. Native record history holds changes. A configured table does not authorize comments or notifications. Historical imports are separate from setup. Keep code review, CI, and merging on the repository host. For requested task execution, read the `bot-mode` skill's `playbooks/issues.md`.

For a missing skill, distinguish a missing installation, invalid metadata, restricted invocation, and a missing dependency. Inspect the relevant state before proposing a fix. A skill present only in the source repository must be available to the active agent before execution.

For delegation questions, explain that the current agent creates subagents through available tools using environment defaults. The user need not select worker models or configure routing rules. Independent candidates require separate subagent conversations.

For history questions, use the environment's supported session interface, an explicit export, or a documented local source. Report coverage gaps. Do not assume another provider's transcript layout.

For a run that drifts, read [prompting guidance](references/prompting.md). For a starting prompt, adapt an example from [recipes](references/recipes.md). Examples do not add mandatory steps.
