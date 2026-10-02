# P100-033.original.v1

**Target.** ECG reference heart rate

**Target units.** bpm

**Metric kind.** mae

**Timing contract.** After the complete ten-second PPG segment; simultaneous ECG supplies the target but is never an input. Known recording motion/contact conditions are allowed. No human quality annotation is a predictor.

**Calibration.** No per-person ECG or target calibration. Spectral transforms are fixed within each PPG window; any fusion/shrinkage parameters or flexible scaling are trained on development people only.

**Independent unit.** Person; every recording from one person linked

**Scope limits.** 50 participants in one smartphone protocol;10 held people. ECG-derived rate is an independent sensor reference, but no clinical agreement threshold or cardiovascular diagnosis is established.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| fft_bpm | bpm |
| acf_bpm | bpm |
| half_bpm | bpm |
| half_strength | dimensionless |
| spectral_quality | dimensionless |
| agreement | bpm |
| motion | dimensionless |
| ear | dimensionless |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-033.original.v1 --output NEW_SUBMISSION; then score --task P100-033.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
