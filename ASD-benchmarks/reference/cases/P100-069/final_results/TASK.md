# P100-069.continuation.v1

**Target.** Lubricant temperature

**Units.** degree C

**Error units.** degree C

**Primary metric.** mae

**Primary metric units.** degree C

**Cohort.** P100-069.continuation.v1.cohort-1

**Prediction time.** Current/past housing, ambient, speed/friction only; first lubricant calibration, no later TL.

**Independent unit.** whole thermal experiment/run

**Hierarchy.** group

**Calibration and history.** Original TL(0) calibration, no later lubricant measurement.

**Limits.** Five identification runs and eight source validation runs in one gearbox. Initial calibration and measured housing/friction signals are required; no unseen gearbox or sensorless temperature claim.

**Historical exposure record.** ALL original confirmation exposed; no fresh confirmation; diagnostics opened only after candidate/stopping freeze; all future evaluations are retrospective

**Current exposure.** All outcomes exposed; future scoring is retrospective.

**Source scope.** original_corpus

**Source.** https://doi.org/10.18419/DARUS-5015

**Source terms.** CC BY 4.0

## Permitted prediction inputs

| Variable | Unit / interpretation |
|---|---|
| `time_s` | s |
| `housing_C` | degree C |
| `environment_C` | degree C |
| `speed` | rad/s |
| `friction` | N m; source friction torque |
| `initial_C` | degree C; explicitly permitted initial lubricant measurement |

Identifiers and source locators are alignment metadata. They may route documented frozen calibration states; they are not a license to look up a scored target. Additional columns outside this list are not predictors.

## Reproduction and comparison

`run.py` and `rules.json` contain executable frozen equations and every coefficient. `evidence/metrics.csv` and `evidence/predictions.csv.gz` preserve the historical comparisons. The shared evaluator recalculates them and compares submitted predictions on identical covered observations. Model IDs are local to this task and are distinct from finding IDs.

Primary aggregation and eligible observations are frozen. Excluded/nonpositive log targets are reported separately from physical-unit error. Uncertainty is described at independent-group level; no row bootstrap is used. The raw adapter emits native anchors, eligibility, calibration and group records. Preparation does not fit or tune a model.

Default reference: `reference`. Comparator models: `reference`, `compact_candidate`, `housing`, `single_speed`, `single_power`, `double_speed`, `innovation_power`, `innovation_speed`, `variable_tau`, `temperature_power`, `ridge_history`, `legacy_reference`.

Use `python evaluation/benchmark.py example --task P100-069.continuation.v1 --output NEW_FOLDER` from the benchmark root. Historical development/confirmation separation cannot be reused as a fresh holdout after exposure.
