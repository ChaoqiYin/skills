---
name: setup-bot
description: "Set up domain documentation and project configuration, including a Feishu task-table link. Use for initial bot setup or configuration changes."
metadata:
  internal: true
---

# Setup bot

Write domain documentation and necessary configuration in the actual project. Reuse existing files and conventions. For an assessment request, report findings without editing files.

## Steps

### 1. Detect available capabilities

Identify the target project from the request and active project context. Resolve an unknown target before writing files. Keep the project separate from the skill source repository and installed skills.

Locate required skills by name through the current agent's catalog or discovery metadata. Check command execution, subagent support, file isolation, repository access, and Feishu access for the selected workflow. Follow invocation restrictions and report missing dependencies. Use environment defaults when the current agent creates subagents. Do not configure model choices.

### 2. Load current state

Read existing project instructions and the documents they reference. Look for equivalents of `docs/agents/domain.md` and `docs/agents/issue-tracker.md`. Locate any `GLOSSARY.md`, `GLOSSARY-MAP.md`, and architecture decision records, or ADRs.

Reuse the project's tracker choice and domain document layout. Report stale settings before changing existing user choices. Resolve each helper skill by name and its resources relative to its installation. The project does not need the skill source repository or its category directories.

### 3. Workflows, map, and confirm

**(a) Collect missing inputs.** Reuse valid project settings. If Feishu tracking is requested and no task-table link is configured, ask the user for a link the current agent can access. Inspect the link. Ask which table to use only if the target remains ambiguous. Obtain resource IDs and table fields through the service. Ask only for unresolved choices, never credentials.

**(b) Map capabilities.** Use `lark-issue-tracker`'s bot-only wrapper to locate the task table and check access. Read helper instructions before choosing commands. Override user-identity defaults for this task workflow. Use `lark-shared` for permission diagnosis; never use user login or user identity to repair bot access. Read table fields and record-comment identifiers when needed. Choose the domain document layout from the existing project structure.

Record existing authorization for automated execution, task updates, comments, and owner mentions. Record its source, task scope, and stop conditions. Resolve decision-makers from task person fields or a project authority mapping. Save stable person identifiers and which decisions each person may make. Do not infer authority from a display name or mark missing authorization as granted.

**(c) Show the mapping and resolve gaps.** Present the document paths, domain layout, task-table link, and missing inputs. Continue with authorized setup without asking for approval again. Configuring a link does not authorize remote schema changes, issue imports, test comments, or messages. If Feishu access is pending, finish the independent documentation work and report the blocker.

### 4. Validate

Check that required skills are available and domain document paths match the project. For Feishu, resolve the supplied link and read the selected table as the bot. Check the returned identity. If the link is missing or inaccessible, mark Feishu setup as pending. The user's access does not prove the bot's access. Do not change global CLI authentication or configuration.

Report confirmed reads separately from untested writes and comments. Do not publish a test comment to complete setup.

### 5. Write the rule

Write these two documents in the actual project. Reuse existing equivalents:

- `docs/agents/domain.md`. Record the glossary and ADR locations. Instruct agents to read the relevant documents before exploring an area. Tell agents to use established terms and flag conflicts with ADRs. Default to root `GLOSSARY.md` and `docs/adr/`. Follow `GLOSSARY-MAP.md` or context-specific conventions when present. Missing domain files do not block work. Do not invent terms, decisions, or empty files to fill the layout.
- `docs/agents/issue-tracker.md`. Record the tracker choice, confirmed task-table link, and fixed operating identity `bot`. Include the authorized automation scope, execution and communication permissions, their sources, and decision-maker mappings. Record the existing state and field mappings when needed. State that a question ends the current task run after the blocked handoff. The next automation invocation checks ready and blocked tasks; no listener or scheduler is created by setup. Mark unconfirmed permissions as unavailable. If an existing user identity conflicts with this workflow, record the conflict and pending bot access instead of silently using that identity. Keep credentials in tool authentication storage.

If a recognized project instruction file exists, add or update short references to these documents. Preserve surrounding content and valid user edits. Otherwise, explain how to read the documents explicitly. Create no separate agent agreement or instruction file. On reruns, update the same documents. Write project outputs in the project, not in the installed skill directory.

### 6. Confirm

Re-read both documents. Check their paths and any references in project instructions. Report the written files, configured Feishu link, unverified operations, and blockers. Tell the user they can edit the documents directly. Re-running setup updates the same files.

### 7. Offer a verification skill (optional)

Check for an existing verification skill or tool that drives the real application. If none exists, offer once to create a project verification skill with `create-verification-skill`. If the user accepts, locate that skill by name and follow its instructions. Otherwise, continue setup without creating one.

### 8. Offer a formal verification skill (optional)

Check for a project skill that runs a model checker, proof, or another verifier against the code. If none exists, offer once to create one with `create-formal-verification-skill`. If the user accepts, locate that skill by name and follow its instructions. Otherwise, finish setup without installing formal verification tools.
