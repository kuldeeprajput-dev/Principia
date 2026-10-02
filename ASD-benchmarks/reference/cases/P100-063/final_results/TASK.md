# P100-063.original.v1

**Target.** Noise power spectral density

**Target units.** nV^2/Hz

**Metric kind.** mae

**Timing contract.** All 77, 293 and 389 K traces were used for whole-temperature leave-out development; all 195 and 352 K traces were reserved. Field traces and frequency bins are nested within temperature. Source background subtraction is retained and disclosed; it is not fitted by this campaign.

**Calibration.** No held-condition calibration. Publisher background subtraction retained, not refitted.

**Independent unit.** Entire termination temperature; magnetic-field traces nested. One74nm YIG film, frequencies dependent.

**Scope limits.** Entire termination temperature; magnetic-field traces nested. One74nm YIG film, frequencies dependent.; The measured thermal peak/dip response is reproducible with a compact Lorentzian family across two reserved termination temperatures. The extra dispersive term is effectively tied with the symmetric control; no new magnon law is established.; No independent population confidence interval from dependent rows.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| frequency_GHz | GHz |
| field_T | T |
| termination_K | K |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-063.original.v1 --output NEW_SUBMISSION; then score --task P100-063.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
