# 057: Foam rheology - second continuation

Shear-rate correction is negligible; anomalous instrument values and thermal/history confounding remain.

**Status:** unsupported_or_negligible_extension. All old confirmation outcomes were already exposed. This round fits and selects using original development groups only; no old-test scores were reopened. The original final reference package remains unchanged.

## Scientific question

A physically signed shear-thinning correction explains the mismatch between nominally matched successive temperature blocks.

Prior evidence: Native corresponding rates differ by up to6.667%; thermal history gave only0.26% improvement and four activation coefficients hit zero.

## Completed investigations

| Version | Hypothesis / model | Primary error |
|---|---|---:|
| [cycle-001](PROTOCOL.json) | shear_transport | 3628.02813 |

Units: **cP**. Exact-cohort prior best: **3604.80227**, `previous/cycle-002`. New matched HGB: **4160.15626**. [All models and hashes](COMPARISON.csv) and [every group](BY_GROUP.csv) are retained.

Best tested extension: `cycle-001` (3628.02813); this is a research candidate, not fresh validation. The four favorable cases were selected before any further confirmation; see the collection selection record.

## Equation and evidence

```text
eta=eta_previous*exp(B_formulation*Delta(1000K/T)+c_formulation*log(gamma/gamma_previous)), B>=0,-1<=c<=0.
```

Full precision coefficients, calibration and fold-specific states: [cycle-001/states.json](cycle-001/states.json). Predictions and grouped scores are in the same directory. No fitted parameter variant is counted as another positive discovery.

## Scope and evaluator

The whole-group/chronological folds, targets and permitted calibration inherit the [earlier protocol](../continuation-20260930/PROTOCOL.json), with the explicit [new protocol](PROTOCOL.json) and any [shared documentation corrections](../../../_support/continuation_20260930b/READER.md). New source data are not normalized or overwritten.

Use the [shared evaluator](../../../_support/continuation_20260930b/EVALUATOR.md) for complete or explicitly abstaining submissions. It restricts every comparator to identical coverage and does not certify novelty or impact. The [collection report](../../../ASD_CONTINUATION_15_ROUND2.md) explains the strongest results and their counterexamples.

Original source/units audits and bounded prior-art reviews remain authoritative dependencies. No private reference data entered this campaign.
