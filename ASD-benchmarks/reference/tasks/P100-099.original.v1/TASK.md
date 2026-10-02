# P100-099.original.v1

**Target.** Population trace mean over native frames t+31 through t+60

**Target units.** author processed-trace units

**Metric kind.** mae

**Timing contract.** Every30 native frames after300-frame history, forecast next30-frame population mean ending60 frames later. Only trace frames<=t are inputs. Native frame index is used without inferring seconds or behavior alignment.

**Calibration.** Past observed trace history is allowed. No held future calibration or source fitted maps/pvpreS/pvpostS enter features. All model parameters and flexible transforms are fitted on development animals.

**Independent unit.** Animal suffix across all days,contexts and sessions

**Scope limits.** Retained author-processed calcium traces only; amplitude normalization/calcium-event interpretation is not documented in the archive. No spikes,absolute calcium concentration or real-time physiology claim. Twenty-eight source animals; held animals stay within the same study.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| level | author processed-trace units |
| lag30 | author processed-trace units |
| lag60 | author processed-trace units |
| mean300 | author processed-trace units |
| dispersion | author processed-trace units |
| zero_fraction | dimensionless |
| ventral | binary |
| condition_group3 | binary |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-099.original.v1 --output NEW_SUBMISSION; then score --task P100-099.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
