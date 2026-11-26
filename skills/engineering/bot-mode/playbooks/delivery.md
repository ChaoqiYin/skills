# Delivery

Use for a requested PR, review follow-up, release, deployment, or merge. Follow each section only in its assigned SOP phase.

## Prepare

During SOP step 5, prepare the artifact without creating a PR, publishing a release, deploying, or merging.

1. Inspect the branch, diff, project conventions, and current checks. Identify task changes and preserve unrelated work.
2. Prepare the requested patch, commit, PR description, release material, or branch for review. Follow project templates and available writing guidance. Do not impose a universal PR format.
3. Run relevant checks. Include evidence and unresolved gaps in the review material. A request for local edits does not require a PR.

## Address review or CI

During SOP step 5, repair the confirmed review or CI problems before verification.

Read the failing job or review comment. Assess it against the task's intent and reproduce the problem when practical. Fix confirmed problems within scope and rerun affected checks. Evaluate automated comments by their evidence.

Report unavailable checks. For requested monitoring, use supported polling or events with a stopping condition. Claim continued monitoring only when a running process can continue after the turn.

## Publish or merge

Enter this section only from SOP step 7, after verification. A preparation-only request ends with the reviewable artifact.

Record the requested operation, target, exact revision, authorization source, and required checks before acting. Use existing authorization without asking again. If permission is missing, finish authorized preparation and return the artifact through the blocked handoff.

Before an action or retry, read the operation record and check the service's actual state. If the requested result already exists for the target revision, reuse its identifier. If an earlier result is uncertain, reconcile the target before another write. Do not repeat a successful action merely because another SOP phase or resumed run reaches delivery.

Perform the authorized operation through the available service tools. Preserve its returned identifier and observed outcome. On a confirmed failure, repair within the authorized scope and rerun affected checks. On a new prerequisite or missing permission, use the blocked handoff. Preserve successful and uncertain parts separately.

After acting, check the service's actual state. Distinguish ready to merge from merged. A successful upload does not prove the deployed application works. Report only the verified state.

For Feishu tasks, follow [Feishu tasks](issues.md) to attach delivery and verification links and update the authorized review or acceptance stage. Keep code review and CI on the repository host. A merge alone does not close the task.
