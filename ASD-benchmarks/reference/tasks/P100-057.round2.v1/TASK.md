# P100-057.round2.v1

**Target.** Next-temperature-block viscosity

**Units.** cP

**Error units.** cP

**Primary metric.** mae

**Primary metric units.** cP

**Cohort.** P100-057.round2.v1.development-oof

**Prediction time.** Parse native numeric rows only; no smoothing, imputation or log-based target exclusion. All temperatures/rates in each Test ID stay together. Expanded information budget: T_C, shear_s, T_previous, eta_previous, eta_first, previous_shear_s, first_shear_s, formulation

**Independent unit.** whole Test ID; synthesis lots not identified

**Hierarchy.** group

**Calibration and history.** See frozen development protocol and per-fold states; all learned calibration is training-partition-only. T_K is absolute temperature in kelvin; eta is cP. The factor1000 carries kelvin, so9 is dimensionless and represents an effective activation scale9000K. Formulation amplitudes a_f range52.1603–218.5126cP at333.15K; all ten exact values are in rules.json. A shear-rate input is allowed for competitors, but the selected thermal reference does not use it.

**Limits.** Repeated tests of ten already calibrated formulations in one rheometer dataset; no independent synthesis-lot or unseen-loading transfer. Repeatedly exposed development out-of-fold cohort; not the original reserved cohort.

**Historical exposure record.** All old confirmation groups exposed. Only original development groups used for fitting/selection. No repeated old-test evaluation in this round.

**Current exposure.** All outcomes exposed; future scoring is retrospective.

**Source scope.** original_corpus

**Source.** https://zenodo.org/records/19699588

**Source terms.** cc-by-4.0

## Permitted prediction inputs

| Variable | Unit / interpretation |
|---|---|
| `T_C` | degC |
| `shear_s` | s^-1 |
| `T_previous` | degC |
| `eta_previous` | Pa s |
| `eta_first` | Pa s |
| `previous_shear_s` | s^-1 |
| `first_shear_s` | s^-1 |
| `formulation` | source label; calibrated category |

Identifiers and source locators are alignment metadata. They may route documented frozen calibration states; they are not a license to look up a scored target. Additional columns outside this list are not predictors.

## Reproduction and comparison

`run.py` and `rules.json` contain executable frozen equations and every coefficient. `evidence/metrics.csv` and `evidence/predictions.csv.gz` preserve the historical comparisons. The shared evaluator recalculates them and compares submitted predictions on identical covered observations. Model IDs are local to this task and are distinct from finding IDs.

Primary aggregation and eligible observations are frozen. Excluded/nonpositive log targets are reported separately from physical-unit error. Uncertainty is described at independent-group level; no row bootstrap is used. The raw adapter emits native anchors, eligibility, calibration and group records. Preparation does not fit or tune a model.

Default reference: `current/cycle-001`. Comparator models: `previous/cycle-002`, `current/cycle-001`, `previous/cycle-001`, `previous/baseline-old`, `previous/baseline-signed_history`, `previous/baseline-previous`, `current/baseline-hgb`, `previous/baseline-flex`, `previous/cycle-003`.

Use `python evaluation/benchmark.py example --task P100-057.round2.v1 --output NEW_FOLDER` from the benchmark root. Historical development/confirmation separation cannot be reused as a fresh holdout after exposure.
