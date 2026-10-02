# 024: Composite fatigue - second continuation

Free strain exponent does not beat the established log family; no lifetime claim.

**Status:** unsupported_or_negligible_extension. All old confirmation outcomes were already exposed. This round fits and selects using original development groups only; no old-test scores were reopened. The original final reference package remains unchanged.

## Scientific question

A common strain-squared damage proxy may conceal a different strain dependence. Fit a strain exponent while holding the logarithmic cycle exposure fixed.

Prior evidence: The preceding floor and load-feedback models did not improve the log baseline; their extra mechanisms were inactive or weakly identified.

## Completed investigations

| Version | Hypothesis / model | Primary error |
|---|---|---:|
| [cycle-001](PROTOCOL.json) | strain_exponent | 1.64900275 |

Units: **GPa**. Exact-cohort prior best: **1.63154464**, `previous/cycle-002`. New matched HGB: **3.1117731**. [All models and hashes](COMPARISON.csv) and [every group](BY_GROUP.csv) are retained.

Best tested extension: `cycle-001` (1.64900275); this is a research candidate, not fresh validation. The four favorable cases were selected before any further confirmation; see the collection selection record.

## Equation and evidence

```text
E/E0=clip(1-k*(strain_percent/1)^p*log1p((N-20)_+/1000),0,1). This is conditional recorded stiffness, not fatigue life.
```

Full precision coefficients, calibration and fold-specific states: [cycle-001/states.json](cycle-001/states.json). Predictions and grouped scores are in the same directory. No fitted parameter variant is counted as another positive discovery.

## Scope and evaluator

The whole-group/chronological folds, targets and permitted calibration inherit the [earlier protocol](../continuation-20260930/PROTOCOL.json), with the explicit [new protocol](PROTOCOL.json) and any [shared documentation corrections](../../../_support/continuation_20260930b/READER.md). New source data are not normalized or overwritten.

Use the [shared evaluator](../../../_support/continuation_20260930b/EVALUATOR.md) for complete or explicitly abstaining submissions. It restricts every comparator to identical coverage and does not certify novelty or impact. The [collection report](../../../ASD_CONTINUATION_15_ROUND2.md) explains the strongest results and their counterexamples.

Original source/units audits and bounded prior-art reviews remain authoritative dependencies. No private reference data entered this campaign.
