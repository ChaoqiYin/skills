---
name: swarm
description: "Delegate work to independent subagents, collect their results, and return one consolidated report. Use for /swarm, 'swarm this', or parallel coverage, races, gauntlets, and exploration."
disable-model-invocation: true
---

# Swarm

## Start

The current agent coordinates the run and creates workers through the environment's available subagent tools using environment defaults. If independent subagents are unavailable, report the limitation as blocked and stop.

Track one entry per phase with the available task-list tool or a written checklist before launching anything.

1. Frame
2. Fan out
3. Aggregate
4. Report

## Phase A: Frame

1. State the done predicate and the artifact or report the swarm must return.
2. Choose the shape. Partition into slices, race N workers on identical briefs, or mix both. For a race or mixed shape, declare `first pass`, `rank all`, or `best-of` before spawning.
3. Choose the number of worker subagents to cover the slices or race arms.
4. Give each worker its own writable output when it writes. When workers verify or measure commits, each brief names the exact SHAs. A measurement brief also names the method (sample count, what one sample is, order). The worker records both in its result.

## Phase B: Fan out

Create workers through the available delegation tools, each in its own conversation with access to the resources its brief requires. Run them concurrently within the environment's concurrency limit, in batches when needed, or sequentially in independent subagent conversations when parallel execution is unavailable.

When a worker needs a non-default branch, use the environment's supported workspace or branch controls to give it the correct checkout, and include the branch or commit in its brief.

Every brief stands alone. Include the goal, scope, exact slice or race arm, how to verify, and what to report. Reports use `PASS`, `ISSUES`, or `BLOCKED` with evidence. A worker that can prove a defect reports `ISSUES` and lists every issue it can prove, not only the first.

If a worker drops out, proceed with N-1 and note it.

## Phase C: Aggregate

Read the terminal results. Drop a result that does not record the SHAs and method its brief names, and respawn that worker once. After a second miss, record a gap. A gap does not count as a pass. For coverage, every required slice needs a result. For a race, apply the selection rule declared up front. Use first pass, rank all, or best-of. Do not paste raw worker dumps.

## Phase D: Report

Return one consolidated in-chat report with a result table, issue one-liners, gaps or dropouts, whether workers ran concurrently, in batches, or sequentially, and the race rule when used.
