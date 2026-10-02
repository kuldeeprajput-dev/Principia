# P100-065.original.v1

**Target.** Log frequency-noise spectral density

**Target units.** dB re 1 Hz^2/Hz

**Metric kind.** mae

**Timing contract.** The −30 and −15 dB spectra were developed with four complete log-frequency-band folds; the entire −20 dB spectrum was reserved. Both ratio conditions remain in each development training fold. Confirmation therefore adds ratio interpolation beyond the spectral-band validation used for selection.

**Calibration.** No held-ratio calibration. Log10 target transform fixed; measuredPSD only and100<=f<=1e6Hz.

**Independent unit.** Complete injection ratio; one laser/resonator setup. Development validation blocks complete log-frequency bands across two ratios.

**Scope limits.** Complete injection ratio; one laser/resonator setup. Development validation blocks complete log-frequency bands across two ratios.; A compact sum of feedback-sensitive and common noise contributions predicts the reserved injection ratio, but the selected extension loses to the simpler fixed-exponent domain control. This supports bounded reproduction and model ambiguity, not a new laser-noise law.; No independent population confidence interval from dependent rows.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| frequency_Hz | Hz |
| injection_dB | dB |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-065.original.v1 --output NEW_SUBMISSION; then score --task P100-065.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
