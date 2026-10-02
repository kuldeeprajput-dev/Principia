# 060: Ultrasonic transmission - second continuation

Strong predictive gain; direct resonance interpretation rejected by native spectra.

**Status:** retrospective_candidate. All old confirmation outcomes were already exposed. This round fits and selects using original development groups only; no old-test scores were reopened. The original final reference package remains unchanged.

## Scientific question

The peak of a causal damped impulse difference is more faithful than a unit leading-edge floor plus an asymptotic phasor magnitude.

Prior evidence: The previous frequency-specific law helped physical volts but lost to constant gain on the normalized exposed track.

## Completed investigations

| Version | Hypothesis / model | Primary error |
|---|---|---:|
| [cycle-001](PROTOCOL.json) | exact_transient | 0.180706769 |
| [cycle-002](cycle-002/PROTOCOL.json) | effective_frequency | 0.148748783 |
| [cycle-003](cycle-003/PROTOCOL.json) | common_detuning | 0.119698676 |
| [cycle-004](cycle-004/PROTOCOL.json) | common_Q | 0.100100675 |
| [cycle-005](cycle-005/PROTOCOL.json) | common_tau | 0.159457518 |
| [cycle-006](cycle-006/PROTOCOL.json) | nominal_common_Q | 0.173373779 |

Units: **condition-normalized MAE**. Exact-cohort prior best: **0.155761471**, `previous/cycle-001`. New matched HGB: **0.483587225**. [All models and hashes](COMPARISON.csv) and [every group](BY_GROUP.csv) are retained.

Best tested extension: `cycle-004` (0.100100675); this is a research candidate, not fresh validation. The four favorable cases were selected before any further confirmation; see the collection selection record.

## Equation and evidence

```text
tau500=tau110*110/500, one common frequency ratio;6condition gains. Q equality is a falsifiable constraint, not a measured device property.
```

Full precision coefficients, calibration and fold-specific states: [cycle-004/states.json](cycle-004/states.json). Predictions and grouped scores are in the same directory. No fitted parameter variant is counted as another positive discovery.

## Scope and evaluator

The whole-group/chronological folds, targets and permitted calibration inherit the [earlier protocol](../continuation-20260930/PROTOCOL.json), with the explicit [new protocol](PROTOCOL.json) and any [shared documentation corrections](../../../_support/continuation_20260930b/READER.md). New source data are not normalized or overwritten.

Use the [shared evaluator](../../../_support/continuation_20260930b/EVALUATOR.md) for complete or explicitly abstaining submissions. It restricts every comparator to identical coverage and does not certify novelty or impact. The [collection report](../../../ASD_CONTINUATION_15_ROUND2.md) explains the strongest results and their counterexamples.

Original source/units audits and bounded prior-art reviews remain authoritative dependencies. No private reference data entered this campaign.
