# Investigation

Use for explanations, diagnosis, historical research, or review. Return findings unless the user also requested a fix.

1. Identify the question, target, and relevant revision or time window. Read the primary sources needed to answer it. State a reasonable interpretation when context resolves ambiguity. Ask when different interpretations would change the investigation.
2. Choose evidence for the question:
   - For runtime behavior or ownership, trace entry points, data flow, and state owners.
   - For historical rationale, read commits, reviews, issues, and decision records. Separate recorded reasons from inference.
   - For bugs or performance, reproduce the symptom and record a baseline. Test hypotheses at the first incorrect behavior.
   - For change review, inspect the requested diff, callers, and effects beyond the diff. Perform independent adversarial review when the user requests it.
3. Prefer read-only probes. Isolate tests or reproductions that write files in a scratch checkout. Leave the review target and external state unchanged. If a decisive experiment needs additional permission, report the limitation and proposed check.
4. Return findings with source references and observed evidence. State uncertainty and coverage gaps. Missing evidence does not prove there are no defects.

For a requested fix, carry the reproduction and scope into [Implementation](implementation.md). For findings-only work, stop after reporting.

Use named explanation or review commands only under the [skill invocation rules](../references/specialist-skills.md). Their availability alone does not select them.
