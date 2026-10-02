# P100-087.original.v1

**Target.** Next-round individual contribution

**Target units.** experimental tokens

**Metric kind.** mae

**Timing contract.** One-step prediction before round3..20 using strictly prior own/peer contributions and publicly announced rules. Earlier confirmation responses are permitted causal online history, never fitted parameters. Surveys and session2 excluded.

**Calibration.** One-step prediction before round3..20 using strictly prior own/peer contributions and publicly announced rules. Earlier confirmation responses are permitted causal online history, never fitted parameters. Surveys and session2 excluded.

**Independent unit.** Complete first-session interacting pair;20% hash heldout in each treatment; remaining groups in5 deterministic whole-pair folds. Both players remain together.

**Scope limits.** University laboratory sample; observational behavioral forecasts, no causal policy effect.; Type2 records duplicate Type1 interactions; session2 reuses participants, both excluded.; Prior outcomes available online are not unknown fixed-horizon trajectories.; Threshold matching is a known game-rule calculation; predicting measured contributions remains nontrivial.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| round | round |
| own_previous | experimental tokens |
| peer_previous | experimental tokens |
| own_lag2 | experimental tokens |
| peer_lag2 | experimental tokens |
| own_history_mean | experimental tokens |
| peer_history_mean | experimental tokens |
| endowment | experimental tokens |
| peer_endowment | experimental tokens |
| productivity | dimensionless |
| peer_productivity | dimensionless |
| threshold | productivity-weighted tokens |
| previous_success | indicator |
| required_contribution | experimental tokens |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-087.original.v1 --output NEW_SUBMISSION; then score --task P100-087.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
