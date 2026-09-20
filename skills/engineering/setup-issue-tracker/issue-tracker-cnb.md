# Issue tracker: CNB

Issues and specs for this repo live as CNB issues. Use the [`cnb`](https://www.npmjs.com/package/@cnbcool/cnb-cli) CLI for all operations.

## Conventions

See the `**/cnb-api**` skill for cnb CLI usage.

Infer the repository from `git remote -v`. The repository URL follows the format `cnb.cool/<repo>`

## Merge requests as a triage surface

**MRs are never treated as feature requests.**

Do not treat merge requests as a request surface under any circumstances. MRs are strictly for proposing code changes. Feature requests must be handled through issues, never through MRs.

## When a skill says "publish to the issue tracker"

Create a cnb issue.

## When a skill says "fetch the relevant ticket"

Refer to the `**/cnb-api**` skill for the cnb CLI command to view an issue and its comments.

# Issue tracker: CNB

Issues and specs for this repo live as CNB issues. Use the [`cnb`](https://www.npmjs.com/package/@cnbcool/cnb-cli) CLI for all operations.

## Conventions

Refer to the **`/cnb-api`** skill for cnb CLI usage.
Infer the repository from `git remote -v`. The repository URL follows the format `cnb.cool/<repo>`.

## Merge requests as a triage surface

**MRs are never treated as feature requests.**

Do not treat merge requests as a request surface under any circumstances. MRs are strictly for proposing code changes. Feature requests must be handled through issues, never through MRs.

## When a skill says "publish to the issue tracker"

Create a CNB issue.

## When a skill says "fetch the relevant ticket"

Refer to the **`/cnb-api`** skill for the cnb CLI command to view an issue and its comments.

## Wayfinding operations

Used by `/wayfinder`. The **map** is a single CNB issue with one **child** issue per ticket.

- **Map**: a single issue labelled `wayfinder:map`, holding the Notes / Decisions-so-far / Fog body.
- **Child ticket**: an issue carrying `Part of #<map>` at the top of its description, with the label `wayfinder:<type>` (`research` / `prototype` / `grilling` / `task`). Once claimed, the ticket is assigned to the driving dev.
- **Blocking**: a `Blocked by: #<n>, #<n>` line near the top of the description. A ticket is unblocked when every referenced blocker is closed.
- **Frontier**: list the map's child issues, then keep only tickets that are open, unblocked, and unclaimed; the first ticket in map order wins.
- **Claim**: assign the ticket to the current user and save before any work. This is the session's first write.
- **Resolve**: add the answer as an issue comment, close the issue, then append a context pointer (gist + link) to the map's Decisions-so-far.

