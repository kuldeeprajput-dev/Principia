# P100-071.original.v1

**Target.** Viable-cell density

**Units.** million cells/mL

**Error units.** million cells/mL

**Primary metric.** rmse

**Primary metric units.** million cells/mL

**Cohort.** P100-071.original.v1.cohort-1

**Prediction time.** Sensor median in [t−0.5h,t], fallback latest valid <=2h old; quality Ok and Cole R²>=0.9 where applicable. Lags and peaks use only the past. Do not use aligned duplicate tables as independent evidence.

**Independent unit.** experiment pair (both reactors)

**Hierarchy.** group

**Calibration and history.** Training-only imputation, scale and missingness transforms; causal native sensors with quality flags. Offline VCD and its SEM are responses, never online predictors.

**Limits.** Three reserved cultivation pairs: EXP005 and EXP009 batch; EXP012 fed-batch. Limited process-domain evidence, not universal cell-line or plant transfer.

**Historical exposure record.** All reference confirmation targets are exposed. This is a retrospective diagnostic evaluation, not fresh independent confirmation.

**Current exposure.** All outcomes exposed; future scoring is retrospective.

**Source scope.** original_corpus

**Source.** https://zenodo.org/records/20829178

**Source terms.** cc-by-4.0

## Permitted prediction inputs

| Variable | Unit / interpretation |
|---|---|
| `perm` | pF/cm |
| `deltaeps_fc4` | (pF/cm)*MHz^4 |
| `transmission` | source arbitrary units |
| `reflection` | source arbitrary units |
| `conductivity` | mS/cm |
| `deltaeps` | pF/cm |
| `fc` | kHz |
| `cole_alpha` | dimensionless |
| `c300` | source units unspecified |
| `c1118` | source units unspecified |
| `c9995` | source units unspecified |
| `cole_r2` | dimensionless |
| `co2` | source percent |
| `ph` | dimensionless pH |
| `do` | percent saturation |
| `temperature` | degrees Celsius |
| `agitation` | rpm |
| `aeration` | standard L/h |
| `o2_inlet` | percent inlet oxygen fraction |
| `volume` | L |
| `perm_lag24` | pF/cm |
| `transmission_lag24` | source arbitrary units |
| `perm_peak_past` | pF/cm |
| `fed_batch` | binary indicator |
| `od` | dimensionless source optical-density transform |
| `dperm24` | (pF/cm)/h |
| `dod24` | 1/h |
| `spectral_span` | source capacitance units unspecified |
| `spectral_midspan` | source capacitance units unspecified |
| `fc_mhz` | MHz |
| `permittivity_decline` | pF/cm |
| `perm_decline_fraction` | dimensionless |
| `od_sq` | dimensionless |
| `perm_sq` | (pF/cm)^2 |
| `perm_fc` | (pF/cm)*MHz |
| `perm_x_decline` | pF/cm |
| `perm_x_conductivity` | (pF/cm)*(mS/cm) |
| `perm_x_growth` | (pF/cm)^2/h |
| `od_x_decline` | dimensionless |
| `time_h` | h |

Identifiers and source locators are alignment metadata. They may route documented frozen calibration states; they are not a license to look up a scored target. Additional columns outside this list are not predictors.

## Reproduction and comparison

`run.py` and `rules.json` contain executable frozen equations and every coefficient. `evidence/metrics.csv` and `evidence/predictions.csv.gz` preserve the historical comparisons. The shared evaluator recalculates them and compares submitted predictions on identical covered observations. Model IDs are local to this task and are distinct from finding IDs.

Primary aggregation and eligible observations are frozen. Excluded/nonpositive log targets are reported separately from physical-unit error. Uncertainty is described at independent-group level; no row bootstrap is used. The raw adapter emits native anchors, eligibility, calibration and group records. Preparation does not fit or tune a model.

Default reference: `spectral`. Comparator models: `spectral`, `linear_permittivity`, `availability_control`, `flexible`.

Use `python evaluation/benchmark.py example --task P100-071.original.v1 --output NEW_FOLDER` from the benchmark root. Historical development/confirmation separation cannot be reused as a fresh holdout after exposure.
