# Evaluate bot-mode

Use this procedure after changes to routing, invocation, design, delivery, or recovery. Keep live systems and credentials outside the evaluation.

## Check structure

Validate changed skill frontmatter with the available skill validator. Check local links and heading anchors. Compare automatic dependencies with their actual invocation metadata. An explicit-only command must remain optional unless the user selects it.

Run the bot wrapper's process tests without contacting Feishu:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s skills/engineering/lark-issue-tracker/tests -v
```

Run repository-relative commands from the skill source repository. In another installation, resolve paths from the discovered skill locations.

## Prepare isolated behavior cases

From the source repository, create a fresh evaluation directory:

```bash
python3 skills/engineering/bot-mode/scripts/prepare-evaluation.py --output /tmp/bot-mode-evaluation
```

Use a new output path for each evaluation. The script copies the current engineering skills, records their hashes, and creates isolated cases. It does not start agents, contact services, install skills, or change the source files.

For each case, give a fresh evaluator only its `request.txt`, the snapshot's skill entrypoint, `catalog.json`, the case directory, and the permitted tool capabilities. Keep `snapshot.json`, other cases, previous evaluator results, and the scoring references outside that evaluator's allowed reads. Do not include the expected result in the brief.

Use environment-default agents. For `independent-design`, leave capacity for its coordinator and two candidate workers. Run that case separately if the concurrency limit requires it. For other cases, permit delegation only when their fixture instructions allow it. Use the fixture CLI instead of real service tools.

## Inspect observable outcomes

Check each case against its actual artifacts and tool events:

| Case | Required evidence |
|---|---|
| `advice` | A recommendation without a project-root question, implementation, or external operations. |
| `mechanical` | The label change passes the fixture check. No unselected explicit-only command or independent design is invoked. |
| `review-only` | Findings cite the faulty behavior. The product files remain unchanged. |
| `missing-delegation` | Required design remains unmet, feasible preparation is preserved, and product files remain unchanged. |
| `independent-design` | Two complete designs from independent conversations return and are compared before product edits. The expiry behavior passes its checks. |
| `delivery` | The fixture registry contains one publication for the requested revision. The CLI call log shows no second publication attempt. |
| `unanswered-blocker` | The existing blocked record and unanswered question remain unchanged. All task operations use the bot wrapper. No comment, mention, listener, or retry loop is created. |

Use [Delegation behavior checks](delegation-scenarios.md) and [Check autonomous task execution](autonomy-scenarios.md) for additional cases affected by the change. The prepared cases cover only part of those references.

## Record the result

Record the skill snapshot hash, case, evaluator identifier, permitted actions, observed events, artifact paths, verdict, and coverage gaps. Use `PASS`, `ISSUES`, or `INCONCLUSIVE` for each case. Link command logs and diffs rather than relying on evaluator self-reports.

A successful wrapper test proves the wrapper boundary under the fake CLI. A successful fixture publication proves only that isolated delivery case. Static inspection does not prove agent behavior. Missing transcript events make event-order claims inconclusive even when the final artifacts are correct.

The [recorded evaluation results](evaluation-results.json) contain the checked snapshot, evaluator identifiers, local observations, commands, and coverage limits. Evidence paths refer to the retained local evaluation directory.
