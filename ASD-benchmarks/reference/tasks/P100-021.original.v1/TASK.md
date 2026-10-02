# P100-021.original.v1

**Target.** effective high-current differential resistance of recorded voltage/current channels

**Target units.** ohm

**Metric kind.** mae

**Timing contract.** design prediction before electrical measurement; wafer and inner/outer region known

**Calibration.** No per-device response calibration. Current conversion V_gen/100 ohm is source-provided. Native response gain is not documented; endpoint is recorded-channel differential resistance, not intrinsic junction resistance.

**Independent unit.** complete wafer die: all junction widths and paired traces

**Scope limits.** 19 dies on two wafers. Unknown acquisition gain/offset, nominal rather than measured area. Tail fits operationally define a response and may include defective junctions; all unambiguous devices retained.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| width_um | um |
| wafer_b | dimensionless indicator |
| outer | dimensionless indicator |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-021.original.v1 --output NEW_SUBMISSION; then score --task P100-021.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
