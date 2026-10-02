# P100-061.original.v1

**Target.** Measured hydrogen permeation flux

**Units.** mol s^-1 m^-2

**Error units.** mol s^-1 m^-2

**Primary metric.** mae

**Primary metric units.** mol s^-1 m^-2

**Cohort.** P100-061.original.v1.cohort-1

**Prediction time.** Known membrane, inert gas, temperature, feed fraction, absolute pressures, normal feed flow and specimen geometry only; no mixture flux or held-out pure-hydrogen response.

**Independent unit.** complete inert-gas block at reserved 400 C across the four calibrated membranes

**Hierarchy.** group

**Calibration and history.** All models have the declared 64 pure-hydrogen measurements at 350/450 C through frozen pressure/permeance calibration. No 400 C calibration was available during fitting. Normal molar volume 22.414 L/mol is a stated convention.

**Limits.** Sixty mixture observations in three gas blocks at 400 C, on four previously calibrated membranes. Temperature interpolation in these systems, not independent new-specimen or separator transfer.

**Historical exposure record.** All reference confirmation targets are exposed. This is a retrospective diagnostic evaluation, not fresh independent confirmation.

**Current exposure.** All outcomes exposed; future scoring is retrospective.

**Source scope.** original_corpus

**Source.** https://zenodo.org/records/10691625

**Source terms.** cc-by-4.0

## Permitted prediction inputs

| Variable | Unit / interpretation |
|---|---|
| `membrane_index` | integer index 0 to 3 of calibrated membrane |
| `gas` | categorical N2, Ar or He |
| `temperature_K` | K |
| `feed_fraction` | mol H2 per mol feed, fraction |
| `normal_flow_L_min` | normal L min^-1; assumed 22.414 L mol^-1 |
| `permeate_bar` | bar, absolute |
| `retentate_bar` | bar, absolute |
| `area_m2` | m^2 |
| `diameter_m` | m |

Identifiers and source locators are alignment metadata. They may route documented frozen calibration states; they are not a license to look up a scored target. Additional columns outside this list are not predictors.

## Reproduction and comparison

`run.py` and `rules.json` contain executable frozen equations and every coefficient. `evidence/metrics.csv` and `evidence/predictions.csv.gz` preserve the historical comparisons. The shared evaluator recalculates them and compares submitted predictions on identical covered observations. Model IDs are local to this task and are distinct from finding IDs.

Primary aggregation and eligible observations are frozen. Excluded/nonpositive log targets are reported separately from physical-unit error. Uncertainty is described at independent-group level; no row bootstrap is used. The raw adapter emits native anchors, eligibility, calibration and group records. Preparation does not fit or tune a model.

Default reference: `attempt-004`. Comparator models: `attempt-004`, `mean`, `sieverts`, `richardson`, `rbf`, `rbf_nested`.

Use `python evaluation/benchmark.py example --task P100-061.original.v1 --output NEW_FOLDER` from the benchmark root. Historical development/confirmation separation cannot be reused as a fresh holdout after exposure.
