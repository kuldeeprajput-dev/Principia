# 100: Mobile latency - second continuation

Minimum-variance parity filter loses to lag2; equal-variance stationary-noise assumptions are unsupported.

**Status:** unsupported_or_negligible_extension. All old confirmation outcomes were already exposed. This round fits and selects using original development groups only; no old-test scores were reopened. The original final reference package remains unchanged.

## Scientific question

A minimum-variance unbiased estimate of a locally constant alternating phase improves on lag-two persistence if independent equal-variance measurement noise dominates.

Prior evidence: Unbounded and robust fitted lag-two corrections lost to lag-two persistence; the alternation mechanism itself remains unknown.

## Completed investigations

| Version | Hypothesis / model | Primary error |
|---|---|---:|
| [cycle-001](PROTOCOL.json) | parity_blue | 2.69166704 |

Units: **ms**. Exact-cohort prior best: **2.422715**, `previous/baseline-lag2`. New matched HGB: **3.01743129**. [All models and hashes](COMPARISON.csv) and [every group](BY_GROUP.csv) are retained.

Best tested extension: `cycle-001` (2.69166704); this is a research candidate, not fresh validation. The four favorable cases were selected before any further confirmation; see the collection selection record.

## Equation and evidence

```text
rhat=max(0,(3*last2+10*mean5-3*last-3*last3)/7). Derived from the five-probe phase model and available aggregate history; no fitted coefficients. Correlation, changing phase means or unequal variance falsify its optimality assumptions. This is a filtering hypothesis, not queue physics.
```

Full precision coefficients, calibration and fold-specific states: [cycle-001/states.json](cycle-001/states.json). Predictions and grouped scores are in the same directory. No fitted parameter variant is counted as another positive discovery.

## Scope and evaluator

The whole-group/chronological folds, targets and permitted calibration inherit the [earlier protocol](../continuation-20260930/PROTOCOL.json), with the explicit [new protocol](PROTOCOL.json) and any [shared documentation corrections](../../../_support/continuation_20260930b/READER.md). New source data are not normalized or overwritten.

Use the [shared evaluator](../../../_support/continuation_20260930b/EVALUATOR.md) for complete or explicitly abstaining submissions. It restricts every comparator to identical coverage and does not certify novelty or impact. The [collection report](../../../ASD_CONTINUATION_15_ROUND2.md) explains the strongest results and their counterexamples.

Original source/units audits and bounded prior-art reviews remain authoritative dependencies. No private reference data entered this campaign.
