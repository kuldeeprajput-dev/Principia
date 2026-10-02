# P100-035.original.v1

**Target.** Source positive-context label probability

**Target units.** probability

**Metric kind.** brier

**Timing contract.** After the complete author-extracted call. Predictors only waveform summaries and known species. File context words, animal ID, call label and source reference are never predictors.

**Calibration.** No held-animal labeled calibration. Fixed waveform summaries; any coefficients, centers or species normalization fitted only on training animals.

**Independent unit.** Animal within species; all calls and typo-linked names grouped

**Scope limits.** Seven ungulate species, source behavioral contexts and recording studies. Labels are experimental context-based valence annotations, not independently verified subjective emotion; held animals do not remove study/recording confounding.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| log_duration | dimensionless |
| log_centroid | dimensionless |
| log_peak | dimensionless |
| high_share | dimensionless |
| entropy | dimensionless |
| flatness | dimensionless |
| envelope_cv | dimensionless |
| log_modulation | dimensionless |
| log_rms | dimensionless |
| species_code | dimensionless |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-035.original.v1 --output NEW_SUBMISSION; then score --task P100-035.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
