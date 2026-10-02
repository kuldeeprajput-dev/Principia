# P100-043.original.v1

**Target.** hot-run validation log-perplexity at20–100B tokens

**Target units.** nats per token

**Metric kind.** mae

**Timing contract.** Only checkpoints at or before10B/20B tokens may calibrate the20–100B forecast

**Calibration.** Two same-architecture early validation checkpoints, exact native anchors in observations

**Independent unit.** complete architecture

**Scope limits.** One source corpus, tokenizer, optimization protocol and fixed validation set;22 architectures without repeated independent training seeds. Calibration losses from each evaluated architecture are required. Forecast20–100B tokens only; no universal compute-optimal rule.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| tokens_B | billions of training tokens |
| anchor_tokens_B | billions of training tokens |
| early_tokens_B | billions of training tokens |
| anchor_loss | nats per token |
| early_loss | nats per token |
| params_B | billions of parameters |
| width | embedding dimensions |
| depth | layers |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-043.original.v1 --output NEW_SUBMISSION; then score --task P100-043.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
