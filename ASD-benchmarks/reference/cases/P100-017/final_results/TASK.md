# P100-017.original.v1

**Target.** Author-reported origin depth uncertainty

**Target units.** km

**Metric kind.** log_mae

**Timing contract.** Contemporaneous reported location-quality diagnostics, never pre-event earthquake forecast or independent true depth error.

**Calibration.** Complete spatiotemporal connected clusters held out; same snapshot networks/measurement procedures. No new waveform or independent hypocenter calibration.

**Independent unit.** Transitive clusters within100km great-circle chord and7days; complete cluster hashfolds. Distant events may still share network/systematic velocity model errors.

**Scope limits.** One July2026 catalog snapshot. Positive uncertainty reports only; mixed network estimation conventions, no universal standard-error confidence interpretation. Counts/geometry are outputs of location processing and causality is not identified.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| depth_km | km below network reference (may negative) |
| rms_s | seconds phase residual standardError |
| phases | used phase count |
| stations | used station count |
| gap_deg | largest azimuthal gap degrees |
| dmin_km | minimum angular station distance*111.195km/degree |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-017.original.v1 --output NEW_SUBMISSION; then score --task P100-017.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
