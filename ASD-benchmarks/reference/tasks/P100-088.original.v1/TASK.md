# P100-088.original.v1

**Target.** Current risky choice

**Target units.** binary choice

**Metric kind.** brier

**Timing contract.** Prediction precedes each current choice. Current lottery information is available; feedback availability is given only if block instructions announce it or an earlier trial revealed it. Previous choice and observed feedback from the same block are allowed; current choice, current outcomes, future trials and response time are prohibited. Complete-feedback type is zero unless currently announced with feedback present or revealed by a strictly previous trial; when inferred from history its previous TYPE_FEEDBACK is used.

**Calibration.** No participant-specific fitted calibration. Online historical choices/visible outcomes are allowed identically for all models, beginning with neutral prior 0.5; history resets at every block.

**Independent unit.** Participant; full blocks and all trials linked

**Scope limits.** Seven source experiments, participant transfer within the same laboratory task designs; no financial-advice, causal psychology identification or real-world impact claim.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| ev_difference | expected points difference / abs(risky magnitude) |
| probability | dimensionless |
| valence | dimensionless |
| safe_risk | dimensionless |
| feedback_known | dimensionless |
| feedback_observed | dimensionless |
| complete | dimensionless |
| trial_progress | dimensionless |
| lag_choice | dimensionless |
| history_mean | dimensionless |
| visible_pe | previous visible reward prediction error / abs(risky magnitude) |
| visible_regret | previous visible counterfactual minus chosen reward / abs(risky magnitude) |
| has_history | dimensionless |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-088.original.v1 --output NEW_SUBMISSION; then score --task P100-088.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
