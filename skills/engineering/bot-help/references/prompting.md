# Prompting guidance

Adapt prompts to the user's goal, scope, and evidence. Ask for missing information only when it affects the task.

## Give the agent a finish condition

Name the desired behavior, allowed changes, and evidence of success. Include an available reproduction, artifact, or constraint. Leave implementation choices to investigation unless the user has chosen an approach.

## Steer a run

| Problem | Useful steer |
|---|---|
| Advice became edits | "Only investigate and recommend. Do not implement." |
| A small fix became a redesign | "Keep the scope to the reported behavior. Explain necessary expansion before changing it." |
| Compilation was reported as completion | "Exercise the requested behavior and show the observed result." |
| The agent repeats a failed approach | "Test the shared premise before trying another fix." |
| Workers overwrite each other's work | "Give workers separate writable outputs. Let the coordinator integrate them." |
| A plan lacks executable steps | "Name each phase's output, dependencies, and acceptance check." |
| The explanation is hard to follow | "Use plain language. Start with what changes for me." |
| Earlier decisions were lost | "Recover relevant history through the current environment and identify missing coverage." |

## Bound autonomy by the task

For long work, state the completion check and relevant time, cost, or scope limits. Existing authorization governs external actions. "Keep going" does not authorize messages, publication, deployment, or merging.

Use subagents when independent work helps. Give each worker a scope and acceptance check. The current agent coordinates them using environment defaults. No worker-model configuration is needed.
