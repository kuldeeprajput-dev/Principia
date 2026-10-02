# 071: CHO cultivation - second continuation

Optical/electrical moment closure fails to improve the strongest linear spectral control.

**Status:** unsupported_or_negligible_extension. All old confirmation outcomes were already exposed. This round fits and selects using original development groups only; no old-test scores were reopened. The original final reference package remains unchanged.

## Scientific question

A constrained optical/electrical moment ratio approximates number concentration better than a single dielectric signal.

Prior evidence: The previous decline rule was beaten by the linear spectral control on development and benefited only one of three exposed pairs.

## Completed investigations

| Version | Hypothesis / model | Primary error |
|---|---|---:|
| [cycle-001](PROTOCOL.json) | moment_fusion | 2.02258982 |

Units: **million cells/mL**. Exact-cohort prior best: **1.79365036**, `previous/adaptive-003/results/linear_magnitude`. New matched HGB: **2.21481949**. [All models and hashes](COMPARISON.csv) and [every group](BY_GROUP.csv) are retained.

Best tested extension: `cycle-001` (2.02258982); this is a research candidate, not fresh validation. The four favorable cases were selected before any further confirmation; see the collection selection record.

## Equation and evidence

```text
N=b0+bP*P+bQ*(OD/OD_ref)^2/(P/P_ref)+missingness offsets, bP,bQ>=0. This moment closure requires constant dielectric membrane properties and an effective optical area law; those assumptions are falsifiable, not observed.
```

Full precision coefficients, calibration and fold-specific states: [cycle-001/states.json](cycle-001/states.json). Predictions and grouped scores are in the same directory. No fitted parameter variant is counted as another positive discovery.

## Scope and evaluator

The whole-group/chronological folds, targets and permitted calibration inherit the [earlier protocol](../continuation-20260930/PROTOCOL.json), with the explicit [new protocol](PROTOCOL.json) and any [shared documentation corrections](../../../_support/continuation_20260930b/READER.md). New source data are not normalized or overwritten.

Use the [shared evaluator](../../../_support/continuation_20260930b/EVALUATOR.md) for complete or explicitly abstaining submissions. It restricts every comparator to identical coverage and does not certify novelty or impact. The [collection report](../../../ASD_CONTINUATION_15_ROUND2.md) explains the strongest results and their counterexamples.

Original source/units audits and bounded prior-art reviews remain authoritative dependencies. No private reference data entered this campaign.
