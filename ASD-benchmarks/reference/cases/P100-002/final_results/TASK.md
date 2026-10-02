# P100-002.original.v1

**Target.** Next hourly median systematics-corrected stellar flux

**Target units.** relative flux (native normalization)

**Metric kind.** mae

**Timing contract.** Predict next disjoint hourly bin using preceding observed hourly medians only. The released light curve was author-corrected using full-sector information; this is a retrospective product-space forecast, not a raw real-time pipeline.

**Calibration.** Causal observed flux history within each star; no fitted header period or future light curve values.

**Independent unit.** Star; repeated hourly bins are dependent

**Scope limits.** Eight selected stars in one TESS sector; no new planet, stellar period or universal rotation law. Missing per-cadence quality/error columns limit robustness.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| lag1 | author-normalized relative flux |
| lag2 | author-normalized relative flux |
| lag3 | author-normalized relative flux |
| lag4 | author-normalized relative flux |
| lag6 | author-normalized relative flux |
| lag12 | author-normalized relative flux |
| lag24 | author-normalized relative flux |
| median6 | author-normalized relative flux |
| median24 | author-normalized relative flux |
| mad6 | author-normalized relative flux |
| delta_h | hours |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-002.original.v1 --output NEW_SUBMISSION; then score --task P100-002.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
