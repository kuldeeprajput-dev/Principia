# P100-097.original.v1

**Target.** pedestrian speed

**Target units.** m/s

**Metric kind.** mae

**Timing contract.** Source-processed paired density/speed ordinates, used for retrospective condition transfer. Density is the published local spatial descriptor; the task is not an online evacuation forecast.

**Calibration.** No held-condition speed calibration. The supplied paper fit is an explicitly exposed prior-art baseline, not a newly discovered coefficient set.

**Independent unit.** Complete source figure cohorts; F3D and F3E are linked as the multidirectional-study family and reserved together. Person/run identifiers are missing, so independence within or between figure cohorts is not established.

**Scope limits.** F3A simulation is excluded; source-processed plotting tables are not raw trajectories.; Panel-to-study mapping follows the article ordered empirical-condition list and cited original studies: F3B unidirectional/Zhang2011; F3C counterflow/Zhang2012; F3D/F3E cross/four-directional/Cao2017. Exact original run accession IDs are not retained.; Only within-source condition transfer is assessed. No independent population validation, causal pedestrian mechanism or safe capacity limit is claimed.; Flow and gait algebraic identities are excluded as predictive targets and confirmations.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| eta | m²/person specific volume |
| rho | persons/m², exact reciprocal of eta; predictor only |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-097.original.v1 --output NEW_SUBMISSION; then score --task P100-097.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
