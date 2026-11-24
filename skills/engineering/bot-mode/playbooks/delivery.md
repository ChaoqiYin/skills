# Delivery

Use for a requested PR, review follow-up, release, or merge. Prepare the reviewable artifact, then perform the external actions already authorized.

## Prepare

1. Inspect the branch, diff, project conventions, and current checks. Identify task changes and preserve unrelated work.
2. Prepare the requested patch, commit, PR description, release material, or branch for review. Follow project templates and available writing guidance. Do not impose a universal PR format.
3. Run relevant checks. Include evidence and unresolved gaps in the review material. A request for local edits does not require a PR.

## Address review or CI

Read the failing job or review comment. Assess it against the task's intent and reproduce the problem when practical. Fix confirmed problems within scope and rerun affected checks. Evaluate automated comments by their evidence.

Report unavailable checks. For requested monitoring, use supported polling or events with a stopping condition. Claim continued monitoring only when a running process can continue after the turn.

## Publish or merge

Before an authorized publication, deployment, or merge, verify the target, exact revision, and required checks. Use available service tools. If permission is missing, finish authorized preparation and present the artifact for approval. Do not request permission already given.

After acting, check the service's actual state. Distinguish ready to merge from merged. A successful upload does not prove the deployed application works. Report only the verified state.

For Feishu tasks, follow [Feishu tasks](issues.md) to attach delivery and verification links and update the authorized review or acceptance stage. Keep code review and CI on the repository host. A merge alone does not close the task.
