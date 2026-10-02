# 083: Hive microclimate - second continuation

Weather-increment model is better than the rejected passive model but still worse than the flexible baseline.

**Status:** unsupported_or_negligible_extension. All old confirmation outcomes were already exposed. This round fits and selects using original development groups only; no old-test scores were reopened. The original final reference package remains unchanged.

## Scientific question

External temperature change, rather than a static external/internal gradient, carries the useful thermal forcing.

Prior evidence: A positive level-gradient model lost to flexible forecasting and removing its ambient level term helped.

## Completed investigations

| Version | Hypothesis / model | Primary error |
|---|---|---:|
| [cycle-001](PROTOCOL.json) | weather_increment | 0.186824253 |

Units: **degC**. Exact-cohort prior best: **0.160961448**, `previous/baseline-flex`. New matched HGB: **0.197319377**. [All models and hashes](COMPARISON.csv) and [every group](BY_GROUP.csv) are retained.

Best tested extension: `cycle-001` (0.186824253); this is a research candidate, not fresh validation. The four favorable cases were selected before any further confirmation; see the collection selection record.

## Equation and evidence

```text
T_next=T_now+a*(T_now-T_lag)+b*(Text-Text_lag)+c_stream+d*sin(hour)+e*cos(hour),0<=a,b<=1. An ARX forecasting rule, not identified heat conductance.
```

Full precision coefficients, calibration and fold-specific states: [cycle-001/states.json](cycle-001/states.json). Predictions and grouped scores are in the same directory. No fitted parameter variant is counted as another positive discovery.

## Scope and evaluator

The whole-group/chronological folds, targets and permitted calibration inherit the [earlier protocol](../continuation-20260930/PROTOCOL.json), with the explicit [new protocol](PROTOCOL.json) and any [shared documentation corrections](../../../_support/continuation_20260930b/READER.md). New source data are not normalized or overwritten.

Use the [shared evaluator](../../../_support/continuation_20260930b/EVALUATOR.md) for complete or explicitly abstaining submissions. It restricts every comparator to identical coverage and does not certify novelty or impact. The [collection report](../../../ASD_CONTINUATION_15_ROUND2.md) explains the strongest results and their counterexamples.

Original source/units audits and bounded prior-art reviews remain authoritative dependencies. No private reference data entered this campaign.
