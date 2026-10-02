# 082: Soil respiration - second continuation

Small positive wetting-history gain; drying and absolute-change controls weaken a direction-free explanation.

**Status:** retrospective_candidate. All old confirmation outcomes were already exposed. This round fits and selects using original development groups only; no old-test scores were reopened. The original final reference package remains unchanged.

## Scientific question

Positive change in measured soil moisture contains information beyond current temperature/moisture, consistent with a rewetting pulse.

Prior evidence: Activation splitting and past temperature did not improve the moisture control; current moisture can miss directional history.

## Completed investigations

| Version | Hypothesis / model | Primary error |
|---|---|---:|
| [cycle-001](PROTOCOL.json) | rewetting | 0.237048019 |
| [cycle-002](cycle-002/PROTOCOL.json) | drying | 0.240625348 |
| [cycle-003](cycle-003/PROTOCOL.json) | absolute | 0.240194288 |

Units: **g CO2 m^-2 h^-1**. Exact-cohort prior best: **0.240895176**, `previous/baselines/old_temperature_moisture`. New matched HGB: **0.242972557**. [All models and hashes](COMPARISON.csv) and [every group](BY_GROUP.csv) are retained.

Best tested extension: `cycle-001` (0.237048019); this is a research candidate, not fresh validation. The four favorable cases were selected before any further confirmation; see the collection selection record.

## Equation and evidence

```text
R=A_context*exp(b*x+c*z+d*z^2+e*x*z+m*I_missing+eta*max(Delta moisture/20,0)), eta>=0; x=(T-10C)/10C,z=(moisture-25)/20. Past moisture uses strictly earlier site dates within30days.
```

Full precision coefficients, calibration and fold-specific states: [cycle-001/states.json](cycle-001/states.json). Predictions and grouped scores are in the same directory. No fitted parameter variant is counted as another positive discovery.

## Scope and evaluator

The whole-group/chronological folds, targets and permitted calibration inherit the [earlier protocol](../continuation-20260930/PROTOCOL.json), with the explicit [new protocol](PROTOCOL.json) and any [shared documentation corrections](../../../_support/continuation_20260930b/READER.md). New source data are not normalized or overwritten.

Use the [shared evaluator](../../../_support/continuation_20260930b/EVALUATOR.md) for complete or explicitly abstaining submissions. It restricts every comparator to identical coverage and does not certify novelty or impact. The [collection report](../../../ASD_CONTINUATION_15_ROUND2.md) explains the strongest results and their counterexamples.

Original source/units audits and bounded prior-art reviews remain authoritative dependencies. No private reference data entered this campaign.
