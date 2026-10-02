# P100-094.original.v1

**Target.** Calibrated CDOM fluorescence channel

**Target units.** ppb

**Metric kind.** mae

**Timing contract.** Contemporaneous calibrated CDOM fluorescence diagnostic using pressure,T1,S1; no other optical or oxygen response input. Good T/S flags0, pump on,5–500dbar. CDOM has no independent QC column.

**Calibration.** No confirmation target fitting. Causal target histories only for 38/41/95 as explicitly declared.

**Independent unit.** Entire station casts02,06,08 development (cast04 has no eligible good-QC observations) leave-one-cast-out; casts10 and12 confirmation. Same expedition/instrument, spatial transfer not independent sensor calibration.

**Scope limits.** CDOM ppb is the publisher-calibrated fluorescence channel, not chemically measured DOC concentration. Quality control does not establish a universal conservative-mixing relationship. No target-based outlier removal.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| pressure | dbar |
| temperature | degC |
| salinity | psu |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-094.original.v1 --output NEW_SUBMISSION; then score --task P100-094.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
