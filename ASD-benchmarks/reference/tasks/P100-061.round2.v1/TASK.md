# P100-061.round2.v1

**Target.** Measured hydrogen permeation flux

**Units.** mol s^-1 m^-2

**Error units.** mol s^-1 m^-2

**Primary metric.** mae

**Primary metric units.** mol m^-2 s^-1

**Cohort.** P100-061.round2.v1.development-oof

**Prediction time.** Known membrane, inert gas, temperature, feed fraction, absolute pressures, normal feed flow and specimen geometry only; no mixture flux or held-out pure-hydrogen response. Expanded information budget: temperature_K, feed_fraction, normal_flow_L_min, retentate_bar, permeate_bar, area_m2, calibration_j0, membrane, gas, membrane_index, length_m, diameter_m

**Independent unit.** complete inert-gas block at reserved 400 C across the four calibrated membranes

**Hierarchy.** group

**Calibration and history.** See frozen development protocol and per-fold states; all learned calibration is training-partition-only. All models have the declared 64 pure-hydrogen measurements at 350/450 C through frozen pressure/permeance calibration. No 400 C calibration was available during fitting. Normal molar volume 22.414 L/mol is a stated convention.

**Limits.** Sixty mixture observations in three gas blocks at 400 C, on four previously calibrated membranes. Temperature interpolation in these systems, not independent new-specimen or separator transfer. Repeatedly exposed development out-of-fold cohort; not the original reserved cohort.

**Historical exposure record.** All old confirmation groups exposed. Only original development groups used for fitting/selection. No repeated old-test evaluation in this round.

**Current exposure.** All outcomes exposed; future scoring is retrospective.

**Source scope.** original_corpus

**Source.** https://zenodo.org/records/10691625

**Source terms.** cc-by-4.0

## Permitted prediction inputs

| Variable | Unit / interpretation |
|---|---|
| `temperature_K` | K |
| `feed_fraction` | mol H2 per mol feed, fraction |
| `normal_flow_L_min` | normal L min^-1; assumed 22.414 L mol^-1 |
| `retentate_bar` | bar, absolute |
| `permeate_bar` | bar, absolute |
| `area_m2` | m^2 |
| `calibration_j0` | mol H2 m^-2 s^-1; frozen pure-hydrogen calibration |
| `membrane` | categorical calibrated membrane |
| `gas` | categorical N2, Ar or He |
| `membrane_index` | dimensionless index of declared calibrated membrane |

Identifiers and source locators are alignment metadata. They may route documented frozen calibration states; they are not a license to look up a scored target. Additional columns outside this list are not predictors.

## Reproduction and comparison

`run.py` and `rules.json` contain executable frozen equations and every coefficient. `evidence/metrics.csv` and `evidence/predictions.csv.gz` preserve the historical comparisons. The shared evaluator recalculates them and compares submitted predictions on identical covered observations. Model IDs are local to this task and are distinct from finding IDs.

Primary aggregation and eligible observations are frozen. Excluded/nonpositive log targets are reported separately from physical-unit error. Uncertainty is described at independent-group level; no row bootstrap is used. The raw adapter emits native anchors, eligibility, calibration and group records. Preparation does not fit or tune a model.

Default reference: `current/cycle-001`. Comparator models: `current/cycle-006`, `current/cycle-005`, `current/cycle-004`, `current/cycle-002`, `previous/cycle-004`, `previous/cycle-006`, `previous/cycle-005`, `current/cycle-007`, `current/cycle-003`, `previous/baselines/kernel_nested`, `current/cycle-001`, `previous/baselines/membrane_residual_rbf_original_grid`, `current/cycle-008`, `current/baseline-hgb`, `previous/cycle-003`, `previous/cycle-002`, `previous/cycle-001`, `previous/baselines/old_coupled`, `previous/baselines/membrane_residual_rbf_nested`, `previous/baselines/old_rbf`, `previous/baselines/old_mean`, `previous/baselines/old_richardson`, `previous/baselines/old_sieverts`.

Use `python evaluation/benchmark.py example --task P100-061.round2.v1 --output NEW_FOLDER` from the benchmark root. Historical development/confirmation separation cannot be reused as a fresh holdout after exposure.
