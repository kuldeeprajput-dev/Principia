# P100-076.original.v1

**Target.** evoked_spike_count

**Target units.** spikes per stimulus

**Metric kind.** mae

**Timing contract.** Predict higher-current evoked spike counts after the lower-current prefix for that cell. No future rheobase or peak-response calibration.

**Calibration.** Per-cell spike counts at applied current<=10pA; later currents>10pA forecast. Source manual FI eligibility preserved.

**Independent unit.** complete culture dish within recording date

**Scope limits.** DIV7 cells only; complete dishes linked, final recording date reserved. Culture/animal provenance may share latent batches; do not treat cells or dishes as independent donor replications.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| current | pA |
| soft | binary |
| kd | binary |
| cal_mean | spikes per stimulus |
| cal_last | spikes per stimulus |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-076.original.v1 --output NEW_SUBMISSION; then score --task P100-076.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
