# P100-030.original.v1

**Target.** Coefficient of friction

**Target units.** dimensionless

**Metric kind.** mae

**Timing contract.** Six formulations were developed with leave-formulation-out validation; N+S functionalization and NG supplier curves were reserved. Duplicate curves cannot cross partitions. Both endpoint calibrations are provided for every curve. Scoring covers only 0.28–10 mm/s and tests calibrated shape transfer, not unmeasured-lubricant performance.

**Calibration.** Two exact endpoint friction measurements at0.2 and500mm/s on the same curve; endpoint rows excluded from scored set.

**Independent unit.** Material formulation, repeated representations linked. Two-point calibration at 0.2 and500 mm/s; score0.28–10 mm/s.

**Scope limits.** Material formulation, repeated representations linked. Two-point calibration at 0.2 and500 mm/s; score0.28–10 mm/s.; The concentration-dependent load-sharing extension does not survive reserved-formulation comparison with simple calibrated log-speed interpolation. Its development gain is preserved as a failed transfer hypothesis, not benchmark ground truth.; No independent population confidence interval from dependent rows.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| speed_mm_s | mm/s |
| boundary_cof | dimensionless |
| highspeed_cof | dimensionless |
| concentration_wt_pct | wt percent |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-030.original.v1 --output NEW_SUBMISSION; then score --task P100-030.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
