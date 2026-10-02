# P100-027.round2.v1

**Target.** Measured local vapor void fraction

**Units.** dimensionless

**Error units.** dimensionless

**Primary metric.** mae

**Primary metric units.** void fraction

**Cohort.** P100-027.round2.v1.development-oof

**Prediction time.** Boundary pressure, mass flux, supplied thermodynamic quality, density properties and measurement coordinate only; no measured target-derived velocity, dynamic pressure, phase label or fitted per-run offset. Expanded information budget: pressure_Pa, massflux_kg_m2_s, quality, radial_fraction, rho_liquid, rho_vapor

**Independent unit.** complete experimental run

**Hierarchy.** group

**Calibration and history.** See frozen development protocol and per-fold states; all learned calibration is training-partition-only. Saturation densities are fixed IAPWS-derived inputs from absolute pressure, not learned from void-fraction targets. Global profile coefficients use development runs only.

**Limits.** Three complete radial profiles at one KTH facility. Conditional on supplied boundary quality and normalized observed measurement coordinates; no universal closure, flow-regime discovery or physical wall-coordinate claim. Repeatedly exposed development out-of-fold cohort; not the original reserved cohort.

**Historical exposure record.** All old confirmation groups exposed. Only original development groups used for fitting/selection. No repeated old-test evaluation in this round.

**Current exposure.** All outcomes exposed; future scoring is retrospective.

**Source scope.** original_corpus

**Source.** https://zenodo.org/records/14627088

**Source terms.** Creative Commons Attribution 4.0 International (CC BY 4.0)

## Permitted prediction inputs

| Variable | Unit / interpretation |
|---|---|
| `pressure_Pa` | Pa, absolute |
| `massflux_kg_m2_s` | kg m^-2 s^-1 |
| `quality` | kg vapor per kg mixture |
| `radial_fraction` | dimensionless native coordinate / maximum sampled coordinate |
| `rho_liquid` | kg m^-3 |
| `rho_vapor` | kg m^-3 |
| `saturation_temperature_K` | K |

Identifiers and source locators are alignment metadata. They may route documented frozen calibration states; they are not a license to look up a scored target. Additional columns outside this list are not predictors.

## Reproduction and comparison

`run.py` and `rules.json` contain executable frozen equations and every coefficient. `evidence/metrics.csv` and `evidence/predictions.csv.gz` preserve the historical comparisons. The shared evaluator recalculates them and compares submitted predictions on identical covered observations. Model IDs are local to this task and are distinct from finding IDs.

Primary aggregation and eligible observations are frozen. Excluded/nonpositive log targets are reported separately from physical-unit error. Uncertainty is described at independent-group level; no row bootstrap is used. The raw adapter emits native anchors, eligibility, calibration and group records. Preparation does not fit or tune a model.

Default reference: `current/cycle-001`. Comparator models: `current/baseline-hgb`, `previous/cycle-001`, `previous/cycle-002`, `previous/baselines/old_radial`, `previous/cycle-004`, `previous/cycle-003`, `current/cycle-001`, `current/cycle-002`, `previous/baselines/kernel_nested`, `previous/baselines/old_drift`, `previous/baselines/old_homogeneous`, `previous/baselines/old_nested_flex`, `previous/baselines/old_mean`.

Use `python evaluation/benchmark.py example --task P100-027.round2.v1 --output NEW_FOLDER` from the benchmark root. Historical development/confirmation separation cannot be reused as a fresh holdout after exposure.
