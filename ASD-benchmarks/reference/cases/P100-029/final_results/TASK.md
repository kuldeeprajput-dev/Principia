# P100-029.original.v1

**Target.** spectral_mean_fluorescence

**Target units.** source fluorescence a.u.

**Metric kind.** mae

**Timing contract.** Predict remaining higher-dose assay values after declared lower-dose measurements; sequential assay not real-time kinetics.

**Calibration.** Spectrum-wide mean fluorescence at native concentrations 0,1,2,5 nominal uM, per replicate; target concentrations 7.5 to30. No maximal-response normalization.

**Independent unit.** peptide-dye condition

**Scope limits.** Six peptide–dye conditions; four contiguous replicate curves per condition are linked. Shared peptide/dye factors make this condition transfer, not fully independent molecular systems. Low-dose calibration is required; no spectral peak chosen using outcomes.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| dose | uM barrel |
| dose_cal | uM barrel |
| F0 | fluorescence a.u. |
| F1 | fluorescence a.u. |
| F2 | fluorescence a.u. |
| F5 | fluorescence a.u. |
| dose1 | uM barrel |
| dose2 | uM barrel |
| dye_NR | binary |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-029.original.v1 --output NEW_SUBMISSION; then score --task P100-029.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
