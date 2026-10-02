# P100-085.original.v1

**Target.** Glycolic acid concentration

**Target units.** g/L

**Metric kind.** mae

**Timing contract.** Diagnostic contemporaneous assay: initial and current independently measured EG and current pH, known medium and elapsed time. No GA calibration. Not an online forecast or replacement of HPLC.

**Calibration.** Diagnostic contemporaneous assay: initial and current independently measured EG and current pH, known medium and elapsed time. No GA calibration. Not an online forecast or replacement of HPLC.

**Independent unit.** Complete flask conditions; three development conditions and one metadata-hash confirmation condition; leave-one-condition-out folds keep all replicates together.

**Scope limits.** Only one held-out condition and two replicate curves; no precise population confidence.; Bioreactor filenames imply opposing feed regimes but members are byte-identical: both excluded.; Measured EG depletion can be negative from measurement error; preserve sign, do not impute.; Native early rows for most conditions were seen at schema audit: confirmation is outcome-exposed retrospective transfer, not fresh experimental confirmation.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| elapsed_h | h |
| eg_consumed_g_L | g/L |
| eg_initial_g_L | g/L |
| pH | dimensionless |
| acetate_cofeed | indicator |
| glucose_cofeed | indicator |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-085.original.v1 --output NEW_SUBMISSION; then score --task P100-085.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
