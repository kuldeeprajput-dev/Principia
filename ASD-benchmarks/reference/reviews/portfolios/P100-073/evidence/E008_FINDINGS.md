# 073: Rumen gas production - second continuation

Fractional incremental gas curve fails substantially; retain stronger flexible/established controls.

**Status:** unsupported_or_negligible_extension. All old confirmation outcomes were already exposed. This round fits and selects using original development groups only; no old-test scores were reopened. The original final reference package remains unchanged.

## Scientific question

A broad distribution of digestion times yields a power-law incremental gas curve rather than identifiable fast/slow pools.

Prior evidence: Prefix-exact Gompertz and two-pool fits lost to the flexible model and the slow pool was weakly identified.

## Completed investigations

| Version | Hypothesis / model | Primary error |
|---|---|---:|
| [cycle-001](PROTOCOL.json) | fractional_gas | 29.8616074 |

Units: **mL**. Exact-cohort prior best: **7.61537029**, `previous/baselines/kernel_nested`. New matched HGB: **10.4047836**. [All models and hashes](COMPARISON.csv) and [every group](BY_GROUP.csv) are retained.

Best tested extension: `cycle-001` (29.8616074); this is a research candidate, not fresh validation. The four favorable cases were selected before any further confirmation; see the collection selection record.

## Equation and evidence

```text
G(t)=G8+(G8-G4)*[(t/8h)^beta-1]/[1-2^(-beta)], beta_trial>0. The beta->0 limit is logarithmic. This is total gas, not methane.
```

Full precision coefficients, calibration and fold-specific states: [cycle-001/states.json](cycle-001/states.json). Predictions and grouped scores are in the same directory. No fitted parameter variant is counted as another positive discovery.

## Scope and evaluator

The whole-group/chronological folds, targets and permitted calibration inherit the [earlier protocol](../continuation-20260930/PROTOCOL.json), with the explicit [new protocol](PROTOCOL.json) and any [shared documentation corrections](../../../_support/continuation_20260930b/READER.md). New source data are not normalized or overwritten.

Use the [shared evaluator](../../../_support/continuation_20260930b/EVALUATOR.md) for complete or explicitly abstaining submissions. It restricts every comparator to identical coverage and does not certify novelty or impact. The [collection report](../../../ASD_CONTINUATION_15_ROUND2.md) explains the strongest results and their counterexamples.

Original source/units audits and bounded prior-art reviews remain authoritative dependencies. No private reference data entered this campaign.
