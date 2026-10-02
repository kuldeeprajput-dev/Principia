# P100-026.original.v1

**Target.** Dimethoxymethane selectivity

**Target units.** percentage points

**Metric kind.** mae

**Timing contract.** Six complete reactor runs were developed with leave-run-out validation; the 220°C-labelled and calcined-catalyst runs were reserved. All models receive the same fixed 300-minute calibration prefix. The long-term figure duplicated in the source is counted once. No instantaneous conversion or other selectivity enters the predictor.

**Calibration.** Last available DMM selectivity at t<=300min plus least-squares prefix slope on120<=t<=300; both recomputed independently per run. Score300<t<=1500.

**Independent unit.** Complete reactor run. Diagnostic forecast after 300 min with fixed prefix calibration; no future conversion/selectivity predictors.

**Scope limits.** Complete reactor run. Diagnostic forecast after 300 min with fixed prefix calibration; no future conversion/selectivity predictors.; A two-parameter, causal prefix-conditioned forecast improves persistence and straight-line continuation on two reserved reactor runs. It loses to the flexible control and several other frozen candidates, so evidence supports useful short-horizon calibration rather than a superior or universal kinetic law.; No independent population confidence interval from dependent rows.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| elapsed_min | min |
| anchor_selectivity_pct | percent |
| prefix_slope_pct_min | percent/min |
| ag_wt_pct | wt percent |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-026.original.v1 --output NEW_SUBMISSION; then score --task P100-026.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
