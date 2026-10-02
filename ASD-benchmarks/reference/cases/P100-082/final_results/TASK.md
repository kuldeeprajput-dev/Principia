# P100-082.original.v1

**Target.** Author-derived forest-soil CO2 mass flux on reserved future dates

**Units.** g CO2 m^-2 h^-1

**Error units.** g CO2 m^-2 h^-1

**Primary metric.** rmse

**Primary metric units.** g CO2 m^-2 h^-1

**Cohort.** P100-082.original.v1.cohort-1

**Prediction time.** Known site/context, measurement date, native 5-cm soil temperature and soil moisture only; exclude author response-fit slopes, chamber conversions, confidence bounds and future flux.

**Independent unit.** complete reserved future temporal block at each calibrated site

**Hierarchy.** group

**Calibration and history.** Context/site amplitudes are trained on earlier dates only. Lloyd–Taylor E0 is near 200 K with a documented optimizer-scaling limitation; it is not an identified globally optimized physiological coefficient.

**Limits.** Future dates at fifteen input-eligible calibrated sites, including a Uruguay site in the source. Not unseen-site transfer or causal treatment effects. Native negative flux measurements remain scored; missing 5-cm temperature limits coverage.

**Historical exposure record.** All reference confirmation targets are exposed. This is a retrospective diagnostic evaluation, not fresh independent confirmation.

**Current exposure.** All outcomes exposed; future scoring is retrospective.

**Source scope.** original_corpus

**Source.** https://zenodo.org/records/17519671

**Source terms.** cc-by-4.0

## Permitted prediction inputs

| Variable | Unit / interpretation |
|---|---|
| `site` | categorical calibrated site |
| `context` | categorical subsite/trenching context |
| `t05` | degrees Celsius, native 5-cm soil temperature |
| `tsmoisture` | native soil-water-content percent; may be missing |
| `doy` | day of year |

Identifiers and source locators are alignment metadata. They may route documented frozen calibration states; they are not a license to look up a scored target. Additional columns outside this list are not predictors.

## Reproduction and comparison

`run.py` and `rules.json` contain executable frozen equations and every coefficient. `evidence/metrics.csv` and `evidence/predictions.csv.gz` preserve the historical comparisons. The shared evaluator recalculates them and compares submitted predictions on identical covered observations. Model IDs are local to this task and are distinct from finding IDs.

Primary aggregation and eligible observations are frozen. Excluded/nonpositive log targets are reported separately from physical-unit error. Uncertainty is described at independent-group level; no row bootstrap is used. The raw adapter emits native anchors, eligibility, calibration and group records. Preparation does not fit or tune a model.

Default reference: `lloyd_taylor`. Comparator models: `lloyd_taylor`, `temperature_moisture`, `q10`, `context_mean`, `flexible_fixed`, `flexible_nested`.

Use `python evaluation/benchmark.py example --task P100-082.original.v1 --output NEW_FOLDER` from the benchmark root. Historical development/confirmation separation cannot be reused as a fresh holdout after exposure.
