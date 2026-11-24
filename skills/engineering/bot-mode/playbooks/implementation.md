# Implementation

Use for requested changes. Keep one checkable goal through diagnosis, implementation, and verification.

## Frame and choose the evidence

1. Read the relevant code and project instructions. Record existing user changes. Capture a baseline for checks that require comparison.
2. Define the acceptance check from the requested behavior. Apply the [independent-design gate](../SKILL.md#independent-design-gate) and record the execution scope before implementation. Choose the relevant approach below. Combine approaches only when needed.

| Change | Approach |
|---|---|
| Feature | Follow existing patterns. Choose data shape and ownership. Implement the smallest complete user flow and exercise its meaningful states. Use `architect` for unresolved interface choices. |
| Bug fix | Reproduce the failure, find the first incorrect state, and fix its cause. Use `tdd` for a cheap behavioral regression test. Distinguish an expected failing test from a broken final result. |
| Performance | Define the workload, baseline, and measurement method before editing. Identify the limiting operation. Compare equivalent runs and check behavior as well as the metric. |
| Refactor | State the behavior that must remain unchanged. Establish checks, simplify ownership or boundaries, and rerun them. Exclude unrelated feature changes. |
| Migration | Inventory callers and define phase checks. Move callers to the target design and remove superseded APIs. Allow temporary incompleteness only within declared phases. Close each phase with its check. |

## Execute and integrate

3. Complete required independent designs and comparison before the first implementation edit. Implement in verifiable units. Use [Prototype](prototype.md) for unresolved technical uncertainty. Delegate separable coverage or implementation work when useful, after satisfying the required design gate. Follow each selected helper's contract. Recheck the gate when scope or design premises change.
4. Inspect each change and run its check before advancing beyond the declared boundary. Distinguish expected intermediate failures, baseline failures, and regressions. Fix regressions without weakening checks.
5. Verify the integrated result against the requested behavior. A successful build confirms compilation. Runtime claims need runtime evidence. Use project checks and add tests that provide meaningful regression protection.
6. Return the change, evidence, and remaining gaps. Use [Delivery](delivery.md) only for requested or already authorized delivery actions.

## Long or unattended work

State a checkable completion condition and respect scope, time, and cost limits. Record the current hypothesis, change, observation, and next action. Use `show-me-your-work` when a decision trail helps review.

Use supported jobs, events, or polling to wait. Promise progress after the turn only when a continuation mechanism exists. When failures repeat, test their shared premise before retrying.

Continue through fixable failures within scope. Stop for an unavailable prerequisite, agreed limit, or user instruction. Report incomplete work honestly. "Keep going" does not expand scope or authorize external actions. Keep the original completion condition.
