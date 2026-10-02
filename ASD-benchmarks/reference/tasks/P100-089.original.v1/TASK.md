# P100-089.original.v1

**Target.** risky_choice

**Target units.** binary choice

**Metric kind.** brier

**Timing contract.** Before each choice using trial settings and only prior choices in that protocol; numeric Hidden and EV excluded.

**Calibration.** Causal previous choice and running mean within protocol, reset at protocol start; no future outcomes. Reward/probability are experimenter settings, not necessarily participant knowledge.

**Independent unit.** participant

**Scope limits.** 55 linked participants in E1.1/E1.2/E2.2; native file lacks E2.1. Age changes for two participants retained as per-trial metadata; identities stay linked. No population-wide cognitive mechanism claim.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| reward | points |
| probability | probability |
| child | binary |
| age_child | years; adult sentinel0 |
| multi | binary |
| description | binary |
| trial_progress | trial index/40 |
| lag_choice | binary or first-trial prior0.5 |
| history_mean | proportion or first-trial prior0.5 |
| has_history | binary |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-089.original.v1 --output NEW_SUBMISSION; then score --task P100-089.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
