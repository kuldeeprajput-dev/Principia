# P100-058.supplemental-PLA_recycled-loss.v1

**Target.** Unfitted loss modulus

**Units.** Pa

**Error units.** Pa

**Primary metric.** log_mae

**Primary metric units.** dimensionless natural-log ratio

**Cohort.** P100-058.supplemental-PLA_recycled-loss.v1.cohort-1

**Prediction time.** Temperature and imposed frequency only. Loss modulus is withheld as an orthogonal mechanistic check; never a primary predictor.

**Independent unit.** whole temperature sweep

**Hierarchy.** group

**Calibration and history.** Only the registered lower-temperature storage sweeps supplied calibration. Loss modulus never fitted. Calibrated model states frozen before reserved response opening.

**Limits.** One commercial material from the same authors/instrument; calibrated temperature transfer and unfitted loss response, not universal physics or independent laboratory replication.

**Historical exposure record.** Reserved outcomes were unopened at first frozen evaluation. They are now packaged/exposed; future evaluator scores are retrospective.

**Current exposure.** All outcomes exposed; future scoring is retrospective.

**Source scope.** supplemental

**Source.** https://zenodo.org/records/17288444

**Source terms.** CC BY 4.0

## Permitted prediction inputs

| Variable | Unit / interpretation |
|---|---|
| `temperature_C` | degree C |
| `omega` | rad/s |

Identifiers and source locators are alignment metadata. They may route documented frozen calibration states; they are not a license to look up a scored target. Additional columns outside this list are not predictors.

## Reproduction and comparison

`run.py` and `rules.json` contain executable frozen equations and every coefficient. `evidence/metrics.csv` and `evidence/predictions.csv.gz` preserve the historical comparisons. The shared evaluator recalculates them and compares submitted predictions on identical covered observations. Model IDs are local to this task and are distinct from finding IDs.

Primary aggregation and eligible observations are frozen. Excluded/nonpositive log targets are reported separately from physical-unit error. Uncertainty is described at independent-group level; no row bootstrap is used. The raw adapter emits native anchors, eligibility, calibration and group records. Preparation does not fit or tune a model.

Default reference: `reference`. Comparator models: `reference`, `wlf`, `arrhenius`, `zero_shot_old_PDLLA`.

Use `python evaluation/benchmark.py example --task P100-058.supplemental-PLA_recycled-loss.v1 --output NEW_FOLDER` from the benchmark root. Historical development/confirmation separation cannot be reused as a fresh holdout after exposure.
