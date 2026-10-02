# P100-068.original.v1

**Target.** raw LDV voltage5ms ahead

**Target units.** V

**Metric kind.** mae

**Timing contract.** Predict raw voltage5ms ahead using up to15ms of causal delay samples and a fixed initial20sampleoffset. Issue every5ms after50ms; no future filtering.

**Calibration.** Initial20 raw samples only; no GHKSS/noise-reducedseries or future spectral estimate is used.

**Independent unit.** Complete acquisitiontrace, with raw/denoised pair linked; sixmetadata-hashselectedtracesconfirm. Alltraces shareone levitator/object setup.

**Scope limits.** Primarysource conversion lists125/4 while suppliedMATLABcode uses500/4; nativevoltage is retained to avoid asserting an unsupportedvelocityscale.; Stored1/2kHz sample grids differs from article4kHz acquisition; the adapter preserves storedtiming.; The filename-to-excitation-amplitude mapping is not supplied. Cross-traceprediction is not proof of independentobject or arbitraryexcitationtransfer.; Polynomial coefficients in voltage-delay space are not mechanical force coefficients.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| y0 | V; currentrawminusinitialoffset |
| y1 | V;5mslagminusoffset |
| y2 | V;10mslagminusoffset |
| y3 | V;15mslagminusoffset |
| offset | V; first20samplemean |
| t | s; storedtimestamp |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-068.original.v1 --output NEW_SUBMISSION; then score --task P100-068.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
