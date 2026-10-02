# 072: Yeast fermentation - second continuation

Two early-assay-anchored clocks improve sugar prediction; uptake mechanism and population transfer remain unconfirmed.

**Status:** retrospective_candidate. All old confirmation outcomes were already exposed. This round fits and selects using original development groups only; no old-test scores were reopened. The original final reference package remains unchanged.

## Scientific question

The saturation parameter at its upper bound indicates a first-order limiting rule may suffice without an unidentifiable Monod constant.

Prior evidence: The earlier separate-pool model selected K=200g/L at the upper search boundary; coculture and arrest extensions did not help.

## Completed investigations

| Version | Hypothesis / model | Primary error |
|---|---|---:|
| [cycle-001](PROTOCOL.json) | power_depletion | 14.5585943 |
| [cycle-002](cycle-002/PROTOCOL.json) | biological_clock | 13.4642678 |
| [cycle-003](cycle-003/PROTOCOL.json) | context_clock | 13.3703408 |
| [cycle-004](cycle-004/PROTOCOL.json) | common_clock | 14.0810465 |

Units: **g/L**. Exact-cohort prior best: **14.6569744**, `previous/cycle-002`. New matched HGB: **14.56286**. [All models and hashes](COMPARISON.csv) and [every group](BY_GROUP.csv) are retained.

Best tested extension: `cycle-002` (13.4642678); this is a research candidate, not fresh validation. The four favorable cases were selected before any further confirmation; see the collection selection record.

## Equation and evidence

```text
q(t)=q72*exp[-max(log(q22/q72),0)*(((t-22h)/50h)^beta_q-1)],q in{G,F};beta_q in[0.1,4]. Passes through both prefixes when declining; the explicit max clips negative uptake from rising/noisy prefixes.
```

Full precision coefficients, calibration and fold-specific states: [cycle-002/states.json](cycle-002/states.json). Predictions and grouped scores are in the same directory. No fitted parameter variant is counted as another positive discovery.

## Scope and evaluator

The whole-group/chronological folds, targets and permitted calibration inherit the [earlier protocol](../continuation-20260930/PROTOCOL.json), with the explicit [new protocol](PROTOCOL.json) and any [shared documentation corrections](../../../_support/continuation_20260930b/READER.md). New source data are not normalized or overwritten.

Use the [shared evaluator](../../../_support/continuation_20260930b/EVALUATOR.md) for complete or explicitly abstaining submissions. It restricts every comparator to identical coverage and does not certify novelty or impact. The [collection report](../../../ASD_CONTINUATION_15_ROUND2.md) explains the strongest results and their counterexamples.

Original source/units audits and bounded prior-art reviews remain authoritative dependencies. No private reference data entered this campaign.
