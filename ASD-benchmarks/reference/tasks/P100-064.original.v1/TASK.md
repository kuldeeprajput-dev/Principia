# P100-064.original.v1

**Target.** signed photodiode current after early calibration during operation

**Target units.** nA

**Metric kind.** mae

**Timing contract.** online simultaneous optical-response estimation after first20s: latest electrical observation at or before optical timestamp, maximum2s old; cumulative charge uses current history only

**Calibration.** Median optical current at aligned0..20s and median electrical current first20s per run. No later optical responses enter predictors.

**Independent unit.** complete polymer-fraction/device number; all voltage runs and paired optical/electrical traces

**Scope limits.** 17 named devices; source lacks complete strain timeline, device emissive area and causal interventions. Endpoint remains signed photocurrent, not calibrated luminance. Uneven lengths and malformed/restarted clocks explicitly handled. Fixed>=3 optical calibration points in first20s and <=2s electrical staleness restricts slower-cadence runs. One held-devicegroup has only4eligible rows. This task does not assess the entire native timing range.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| time_s | s |
| current_uA | uA |
| voltage_V | V |
| polymer_fraction | mass fraction |
| charge_uC | uC |
| cal_photo_nA | nA |
| cal_current_uA | uA |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-064.original.v1 --output NEW_SUBMISSION; then score --task P100-064.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
