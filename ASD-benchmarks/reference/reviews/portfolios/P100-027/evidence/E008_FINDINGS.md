# 027: Boiling flow - second continuation

Positive-slip closures fail to beat the prior joint model. The new HGB control improves prediction but supplies no physical law.

**Status:** unsupported_or_negligible_extension. All old confirmation outcomes were already exposed. This round fits and selects using original development groups only; no old-test scores were reopened. The original final reference package remains unchanged.

## Scientific question

A positive liquid-slip contribution plus drift can reproduce the local profile without the earlier C0<1 denominator and arbitrary odds intercept.

Prior evidence: The earlier joint fit had C0=0.879 and strongly varying drift parameters; enforce correct dilute/pure-phase asymptotes to challenge compensation.

## Completed investigations

| Version | Hypothesis / model | Primary error |
|---|---|---:|
| [cycle-001](PROTOCOL.json) | slip_profile | 0.100510657 |
| [cycle-002](cycle-002/PROTOCOL.json) | quality_profile | 0.102012419 |

Units: **void fraction**. Exact-cohort prior best: **0.0840410285**, `previous/cycle-001`. New matched HGB: **0.0759142058**. [All models and hashes](COMPARISON.csv) and [every group](BY_GROUP.csv) are retained.

Best tested extension: `cycle-001` (0.100510657); this is a research candidate, not fresh validation. The four favorable cases were selected before any further confirmation; see the collection selection record.

## Equation and evidence

```text
alpha=expit(log(jg)-log(S*jl+V)+b2*s^2); S>0,V>0. s is the source-normalized coordinate; this is not an area-integrated conservation closure.
```

Full precision coefficients, calibration and fold-specific states: [cycle-001/states.json](cycle-001/states.json). Predictions and grouped scores are in the same directory. No fitted parameter variant is counted as another positive discovery.

## Scope and evaluator

The whole-group/chronological folds, targets and permitted calibration inherit the [earlier protocol](../continuation-20260930/PROTOCOL.json), with the explicit [new protocol](PROTOCOL.json) and any [shared documentation corrections](../../../_support/continuation_20260930b/READER.md). New source data are not normalized or overwritten.

Use the [shared evaluator](../../../_support/continuation_20260930b/EVALUATOR.md) for complete or explicitly abstaining submissions. It restricts every comparator to identical coverage and does not certify novelty or impact. The [collection report](../../../ASD_CONTINUATION_15_ROUND2.md) explains the strongest results and their counterexamples.

Original source/units audits and bounded prior-art reviews remain authoritative dependencies. No private reference data entered this campaign.
