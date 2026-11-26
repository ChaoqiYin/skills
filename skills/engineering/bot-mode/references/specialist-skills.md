# Select specialist skills

Resolve each skill through the current catalog before use. Check the installed invocation policy rather than inferring permission from this table.

## Automatic dependencies

Use these dependencies only when their task branch applies:

| Need | Skill |
|---|---|
| Skill-selection advice | `bot-help` |
| Requested project configuration | `setup-bot` |
| Feishu task records, dependencies, and discussions | `lark-issue-tracker` |
| Task-specific engineering rules | The applicable `principle-*` skills in [Select task principles](principles.md) |

These source skills allow automatic invocation. A receiving environment can impose stricter rules. If an installed dependency cannot be invoked, report the gap and preserve its required contract.

## Explicit-only commands

Use the following commands only when the user requests the named skill or its documented explicit invocation. A general request to use bot-mode does not select every command in this table.

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
| Documents, plans, PR descriptions, and commit messages | `technical-writing`, with `unslop` |

For ordinary work without an explicitly selected command, follow the selected playbook and project checks directly. Do not read an explicit-only command's internal files to bypass its invocation policy. Required independent design uses bot-mode's own [design gate](independent-design.md), so it does not depend on invoking `arena`.

If the user selects an explicit-only command, read its full contract before use. Preserve its dependencies, additional review steps, and stopping conditions. Report unmet requirements rather than claiming that a direct alternative executed that command. Availability alone does not expand task scope.
