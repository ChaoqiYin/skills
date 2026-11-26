---
name: bot-mode
description: "Coordinate an authorized task through its playbook, independent design when required, and verification. Use for bot-mode or requests to orchestrate work through completion. Use bot-help for skill-selection advice."
metadata:
  internal: true
---

# Bot mode

Complete the requested deliverable within the user's scope and existing authorization. Follow the user's language, project instructions, and tool restrictions. Apply this skill to the current task without claiming persistent activation.

## SOP

Use only the steps needed for the requested deliverable. At any step, route a genuine blocker to step 9.

1. **Classify the request.** Identify the goal, deliverable, and allowed actions before requiring project context. Keep advice, planning, and review within their requested scope. Route skill-selection advice to `bot-help` and requested project configuration to `setup-bot`.

2. **Load the needed context.** For project work, identify the actual project root and inspect its instructions and working state. Preserve unrelated changes. Read the domain documents, glossary, architecture decisions, and configuration relevant to the task. Follow the project's actual paths. Setup-bot defaults to `docs/agents/domain.md` and `docs/agents/issue-tracker.md`. For resumed work, use [Session](playbooks/session.md). For Feishu work, use [Feishu tasks](playbooks/issues.md). General advice does not require a project root or task tracker.

3. **Set the completion check.** Select the [playbook](#playbooks), deliverable, acceptance check, and required evidence. For substantial work, record the scope, authorization, limits, and phase checklist. For advice or one obvious change, keep the record in the response and use only relevant checks. Resolve helpers through [Skill invocation](#skill-invocation). Read only the applicable [principles](#principles).

4. **Complete required design.** Before affected implementation, satisfy the [independent-design gate](#independent-design-gate). If the user requests independent design without implementation, satisfy the gate before finalizing that deliverable. Read-only diagnosis, baseline checks, and isolated design probes can precede the gate. Record whether the gate applies and cite the actual decision or explicit requirement.

5. **Execute the technical work.** Follow the selected playbook in verifiable units. For delivery work, complete only [Prepare](playbooks/delivery.md#prepare) and any required [review or CI repairs](playbooks/delivery.md#address-review-or-ci). Reserve PR creation, release publication, deployment, and merging for step 7. Authorized task-record operations follow [Feishu tasks](playbooks/issues.md) throughout the run. If diagnosis leads to an authorized fix, update the task class and return to step 3. If scope or a material design premise changes, pause affected edits and return to step 3.

6. **Verify and repair.** Apply [Verification](#verification) to the actual deliverable. For a scoped failure, repair its root cause and repeat the affected work and checks. If repeated fixes fail, test their shared premise. If scope or a material design premise changes, return to step 3. Continue to step 7 only when the acceptance evidence is sufficient. At an agreed limit, preserve a handoff and report the unfinished work.

7. **Perform external delivery once.** If the request includes external delivery, use [Publish or merge](playbooks/delivery.md#publish-or-merge). Reconcile recorded operations before retrying. If permission is missing, finish authorized preparation and use step 9 with the reviewable artifact. If no external delivery is requested, continue to step 8.

8. **Report and finish.** Apply [Finish](#finish) to report the verified result and actual acceptance state. End the run after the requested deliverable or handoff is complete.

9. **Hand back a blocker.** Complete independent authorized preparation. For a Feishu decision, use [Handle blockers and replies](playbooks/issues.md#4-handle-blockers-and-replies). Otherwise, use [Pause or hand off](playbooks/session.md#pause-or-hand-off) and report the missing decision, capability, or permission through the current channel. After the handoff, end the run without waiting for a reply or starting another task. On a later authorized invocation, return to step 1 and recheck the release conditions.

## Default autonomy

Complete authorized, reversible work without asking whether to proceed. Resolve routine decisions and explain material choices with the result. Existing authorization remains valid for the current task. It does not grant unrelated messages, publication, deployment, or merging. Preserve account-holder requirements and tool confirmation gates.

For a business decision in configured Feishu work, use the task discussion and responsible decision-maker through the task playbook. Bot-mode creates no scheduler or listener. A later existing authorized invocation owns recovery.

## Playbooks

Choose the relevant technical playbook and combine it with Feishu task handling only when needed:

| Task | Read |
|---|---|
| Explain behavior, trace a decision, diagnose without fixing, or review | [Investigation](playbooks/investigation.md) |
| Produce a plan without implementation | [Planning](playbooks/planning.md) |
| Add a feature, fix a bug, improve performance, refactor, or migrate | [Implementation](playbooks/implementation.md) |
| Settle a technical uncertainty or compare candidate shapes | [Prototype](playbooks/prototype.md) |
| Prepare a PR, address review or CI, publish, or merge | [Delivery](playbooks/delivery.md) |
| Resume a known task, hand off, or pause safely | [Session](playbooks/session.md) |
| Create, revise, or evaluate a skill | [Authoring a skill](playbooks/authoring-a-skill.md) |
| Execute, discuss, resume, or update a Feishu requirement or issue | [Feishu tasks](playbooks/issues.md) |

Read only the playbooks needed for the task. For large work without a suitable sequence, build a phased checklist with outputs and checks. Use `figure-it-out` only when the user explicitly selects that command. Follow its workflow without routing recursively back here.

## Skill invocation

Resolve helpers through the current catalog or discovery metadata. Check the installed invocation policy before use. Locate a skill before resolving its internal resources.

Automatic dependencies and explicit-only commands are separated in [Select specialist skills](references/specialist-skills.md). A bot-mode request does not override an explicit-only policy. Do not load internal files to bypass that policy. Follow the playbook directly when an optional command is not selected. Report a required missing dependency or restricted invocation without claiming to have executed the helper.

## Principles

Use [Select task principles](references/principles.md) to find the applicable `principle-*` skills. Their source metadata permits automatic invocation. Read only the triggered principles, subject to the receiving environment's restrictions.

## Subagents

Delegate when independent evidence, separate coverage, or isolated implementation units help. Use the [worker contract](worker.md) for briefs, isolation, routine decision authority, retry limits, escalation, and reports. Use environment defaults rather than requiring model configuration. Review worker artifacts and verify the integrated result.

### Independent-design gate

Read [Complete the independent-design gate](references/independent-design.md) when implementation requires a material design decision or the user requests independent candidates. The reference defines the triggers, required results, comparison, and handling of changed premises.

### Unavailable capabilities

Distinguish a missing optional command, a restricted invocation, and unavailable subagent tools. If optional helpers are missing, follow the design gate and worker contract directly when possible. Preserve the full contract of an explicitly requested skill.

Respect concurrency limits. Independent conversations can run in batches or sequentially. If required delegation is unavailable or prohibited, complete feasible investigation, baseline checks, and acceptance preparation. Stop before affected implementation and use SOP step 9. Do not simulate independence or waive the gate.

## Verification

Check the actual artifact or requested behavior against the completion check. Use the project's existing checks for ordinary verification. Create or maintain a verification tool only when the task includes that work. A build proves compilation. Runtime claims require runtime evidence. Verify worker claims against their artifacts.

Keep intermediate and final checks separate. Expected failing tests or incomplete migration phases do not satisfy final acceptance. Distinguish baseline failures, regressions, skipped checks, and unavailable capabilities. Preserve the checks rather than adding compatibility code to hide incomplete work.

For changes to this skill, use [Evaluate bot-mode](references/evaluation.md). Distinguish structural inspection from actual agent behavior tests.

## Finish

Lead with the outcome, supporting evidence, and remaining limitations. For required delegation, include the actual worker identifiers, covered scope, artifact references, and comparison decision. Use supported history interfaces or explicit exports for transcript claims. A summary does not prove full transcript coverage.

For authorized Feishu updates, follow the task playbook's delivery and acceptance rules. Keep local evidence separate from artifacts accessible to collaborators. A commit, merge, or worker `PASS` alone does not mean that the task is accepted.

Stop when the deliverable passes its checks, the user stops the run, an agreed limit is reached, or a concrete prerequisite blocks progress. Preserve unfinished work and report the actual stop reason. Do not promise progress after the turn without an existing continuation mechanism.
