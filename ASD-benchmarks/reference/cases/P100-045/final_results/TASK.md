# P100-045.original.v1

**Target.** GBM NaI channel4 count rate during fixed post-trigger window

**Target units.** counts/s

**Metric kind.** mae

**Timing contract.** Same-bin channel2+3 count rates and previous-bin low-energy rate permitted; targetchannel4 observations aftertrigger forbidden as predictors.

**Calibration.** Pretrigger[-200,-100]s background rate in each low/high channel; instrument-specific energy edges recorded.

**Independent unit.** Detector within one GRB; detectors share one incident event

**Scope limits.** SingleGRB250206827, observed detector counts not deconvolved photon flux. NaI channel4 spans slightly different energy ranges by detector. No universal burst hardness law or independent event replication.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| low | counts/s in channels 2+3 |
| low_lag | counts/s in preceding bin, channels 2+3 |
| background_low | counts/s in pretrigger channels 2+3 |
| background_high | counts/s in pretrigger channel 4 |
| time_s | s after trigger |
| channel_low_keV | keV |
| channel_high_keV | keV |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-045.original.v1 --output NEW_SUBMISSION; then score --task P100-045.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
