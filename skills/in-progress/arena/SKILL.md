---
name: arena
description: "Delegate the same task to independent candidate subagents, pick a base, and graft the strongest parts of the other candidates into it. Use for /arena, 'arena this', 'throw it in the arena', or when one attempt at a non-trivial artifact would lock in the wrong shape."
disable-model-invocation: true
---

# Arena

The current agent coordinates the run and delegates through the environment's available subagent tools using environment defaults. If independent subagents are unavailable, report that limitation and stop; drafts written in the coordinator's own conversation do not count as independent candidates.

Track one entry per phase (Frame, Fan out, Cross-judge, Pick, Graft, Verify) with the available task-list tool or a written checklist before launching anything.

## Phase A: Frame

Every candidate gets the same prompt, so the prompt is the contract.

1. State the artifact each candidate is producing.
2. Derive the rubric, 3-6 concrete gradeable criteria for what success looks like on *this* task. It is the picker's tool in Phase D. Candidates only see the task.
3. Plan at least two independent candidate subagents. Add more when the task warrants exploring more design directions.
4. Give each candidate its own output location (an isolated git worktree for code where possible, otherwise a separate directory under an available workspace or system temporary directory), per the **separate-before-serializing-shared-state** principle skill.

## Phase B: Fan out

Create the candidate subagents through the available delegation tools. Run them concurrently within the environment's concurrency limit, in batches when needed, or sequentially in independent subagent conversations when parallel execution is unavailable. Give each the same task and shared grounding, its own output path, and instructions to produce the artifact and a short rationale naming the alternatives it considered and what it rejected. Each candidate produces its first artifact without reading the other candidates' outputs.

Replace failed candidates when possible and note any dropouts. Proceed to comparison only with at least two complete candidate artifacts. If that minimum cannot be reached, report the run as incomplete and stop before picking or synthesizing a base.

## Phase C: Cross-judge

After Phase B finishes, create a separate judge subagent with a fresh conversation, the rubric, and all completed candidate artifacts. Give it read-only access to those artifacts using the available controls or explicit instructions. While you read in Phase D, the judge scores each candidate, by path label, on each rubric criterion and recommends a base. If a separate judge cannot be created or returns no usable review, record why Phase C skipped the judge and continue with the coordinator's scoring in Phase D.

## Phase D: Pick a base

Read every candidate end to end before picking. Score each against the rubric criterion by criterion, not on holistic feel, and compare with the cross-judge when Phase C ran one. Agreement on the base confirms the pick. Disagreement means one of you is biased or the rubric was ambiguous. Read both rationales before deciding.

Pick the base a future maintainer can extend most easily without breaking invariants. When two feel tied, prefer the cleaner boundary or smaller API, per the Laziness Protocol.

## Phase E: Graft

Walk each losing candidate once more for what is worth porting into the base, usually one or two things per candidate, not most of it. Fold each graft in by hand, per the **redesign-from-first-principles** principle skill, so the result stays coherent under one mental model. Don't paste mechanically.

If the candidates converge on one shape, that is strong agreement. Note it and ship the consensus shape. No graft is needed. If they wildly diverge, Phase A was under-specified. Reframe and re-run rather than averaging the divergence.

## Phase F: Verify

Verify the synthesized artifact like any other output, per the **prove-it-works** principle skill. If verification finds a problem the arena missed, either Phase A was wrong (re-frame and re-run) or a candidate caught it and you missed the graft (go back to Phase E). Don't paper over it.

## Outputs

One synthesized artifact, with a short synthesis note alongside naming the base and why, whether candidates ran concurrently, in batches, or sequentially, the cross-judge's verdict or why Phase C skipped the judge, each graft with its source candidate, what was rejected and why, any convergence or dropouts, and the verification result. If the run stopped before synthesis, report the incomplete outcome, the completed candidates, and the limitation instead.
