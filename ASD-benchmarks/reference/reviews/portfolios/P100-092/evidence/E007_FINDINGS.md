# 092: BLE antennas - second continuation

Local channel redistribution loses to the previous flexible model; global calibrated-map correction remains useful.

**Status:** unsupported_or_negligible_extension. All old confirmation outcomes were already exposed. This round fits and selects using original development groups only; no old-test scores were reopened. The original final reference package remains unchanged.

## Scientific question

Furniture redistributes initial received power across channels locally rather than mixing every cell with a global power reference.

Prior evidence: Global positive power mixing remained worse than HGB on every exposed date.

## Completed investigations

| Version | Hypothesis / model | Primary error |
|---|---|---:|
| [cycle-001](PROTOCOL.json) | channel_redistribution | 3.57649332 |

Units: **dB**. Exact-cohort prior best: **3.34805792**, `previous/results-v2/flexible`. New matched HGB: **3.33980226**. [All models and hashes](COMPARISON.csv) and [every group](BY_GROUP.csv) are retained.

Best tested extension: `cycle-001` (3.57649332); this is a research candidate, not fresh validation. The four favorable cases were selected before any further confirmation; see the collection selection record.

## Equation and evidence

```text
Rhat=10log10((1-lambda_f)*10^(R0/10)+lambda_f*mean_channel(10^(R0/10)))+b0+bf*furniture; calibration map only, two furniture-specific lambdas.
```

Full precision coefficients, calibration and fold-specific states: [cycle-001/states.json](cycle-001/states.json). Predictions and grouped scores are in the same directory. No fitted parameter variant is counted as another positive discovery.

## Scope and evaluator

The whole-group/chronological folds, targets and permitted calibration inherit the [earlier protocol](../continuation-20260930/PROTOCOL.json), with the explicit [new protocol](PROTOCOL.json) and any [shared documentation corrections](../../../_support/continuation_20260930b/READER.md). New source data are not normalized or overwritten.

Use the [shared evaluator](../../../_support/continuation_20260930b/EVALUATOR.md) for complete or explicitly abstaining submissions. It restricts every comparator to identical coverage and does not certify novelty or impact. The [collection report](../../../ASD_CONTINUATION_15_ROUND2.md) explains the strongest results and their counterexamples.

Original source/units audits and bounded prior-art reviews remain authoritative dependencies. No private reference data entered this campaign.
