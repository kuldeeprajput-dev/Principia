# P100-071.round2.v1

**Target.** Viable-cell density

**Units.** million cells/mL

**Error units.** million cells/mL

**Primary metric.** rmse

**Primary metric units.** million cells/mL

**Cohort.** P100-071.round2.v1.development-oof

**Prediction time.** Sensor median in [t−0.5h,t], fallback latest valid <=2h old; quality Ok and Cole R²>=0.9 where applicable. Lags and peaks use only the past. Do not use aligned duplicate tables as independent evidence. Expanded information budget: perm, permittivity_decline, perm_decline_fraction, perm_peak_past, deltaeps, fc, conductivity, cole_r2, od, transmission, reflection, time_h, fed_batch, dperm24, dod24

**Independent unit.** experiment pair (both reactors)

**Hierarchy.** group

**Calibration and history.** See frozen development protocol and per-fold states; all learned calibration is training-partition-only. Training-only imputation, scale and missingness transforms; causal native sensors with quality flags. Offline VCD and its SEM are responses, never online predictors.

**Limits.** Three reserved cultivation pairs: EXP005 and EXP009 batch; EXP012 fed-batch. Limited process-domain evidence, not universal cell-line or plant transfer. Repeatedly exposed development out-of-fold cohort; not the original reserved cohort.

**Historical exposure record.** All old confirmation groups exposed. Only original development groups used for fitting/selection. No repeated old-test evaluation in this round.

**Current exposure.** All outcomes exposed; future scoring is retrospective.

**Source scope.** original_corpus

**Source.** https://zenodo.org/records/20829178

**Source terms.** cc-by-4.0

## Permitted prediction inputs

| Variable | Unit / interpretation |
|---|---|
| `perm` | pF/cm |
| `permittivity_decline` | pF/cm |
| `perm_decline_fraction` | dimensionless |
| `perm_peak_past` | pF/cm |
| `deltaeps` | pF/cm |
| `fc` | kHz |
| `conductivity` | mS/cm |
| `cole_r2` | dimensionless |
| `od` | dimensionless source optical-density transform |
| `transmission` | source arbitrary units |
| `reflection` | source arbitrary units |
| `time_h` | h |
| `fed_batch` | binary indicator |
| `dperm24` | (pF/cm)/h |
| `dod24` | 1/h |

Identifiers and source locators are alignment metadata. They may route documented frozen calibration states; they are not a license to look up a scored target. Additional columns outside this list are not predictors.

## Reproduction and comparison

`run.py` and `rules.json` contain executable frozen equations and every coefficient. `evidence/metrics.csv` and `evidence/predictions.csv.gz` preserve the historical comparisons. The shared evaluator recalculates them and compares submitted predictions on identical covered observations. Model IDs are local to this task and are distinct from finding IDs.

Primary aggregation and eligible observations are frozen. Excluded/nonpositive log targets are reported separately from physical-unit error. Uncertainty is described at independent-group level; no row bootstrap is used. The raw adapter emits native anchors, eligibility, calibration and group records. Preparation does not fit or tune a model.

Default reference: `current/cycle-001`. Comparator models: `previous/adaptive-003/results/linear_magnitude`, `previous/results-v2/unconstrained2`, `previous/adaptive-003/results/availability`, `previous/adaptive-003/results/unconstrained`, `previous/adaptive-003/results/bounded_correction`, `previous/results-v2/availability`, `previous/results-v2/cycle1`, `previous/results-v2/unconstrained1`, `previous/results-v2/cycle2`, `previous/results-v2/simple`, `current/cycle-001`, `previous/results-v2/rbf`, `previous/results-v2/flexible`, `current/baseline-hgb`, `previous/results-v2/linear`.

Use `python evaluation/benchmark.py example --task P100-071.round2.v1 --output NEW_FOLDER` from the benchmark root. Historical development/confirmation separation cannot be reused as a fresh holdout after exposure.
