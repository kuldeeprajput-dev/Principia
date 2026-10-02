# P100-078.continuation.v1

**Target.** Untreated bacterial burden in total lung

**Units.** log10 CFU / total lung

**Error units.** log10 ratio (decades)

**Primary metric.** mae

**Primary metric units.** log10 CFU / total lung

**Cohort.** P100-078.continuation.v1.cohort-1

**Prediction time.** Only numeric actual time within0-24h and the mean time-zero log burden for the linked strain-study are prediction inputs. Different time-zero animals supply declared cohort calibration. No later burden, laboratory parameter, animal outcome or study/strain identity is a numerical predictor. Numeric <24 strings and censored inequality burdens are not exact-time targets.

**Independent unit.** whole laboratory/site, all strains and studies

**Hierarchy.** group

**Calibration and history.** DSM/site-reference strain aliases resolved from source RefToDict plus explicit single-strain-study Overview links (source labeling discrepancies retained) and kept together. All ExperimentResults sheets included. Explicit untreated CFU lung single-value observations only, equality operator, compatible log-CFU lung units, numeric actual times 0–24 h. Time-zero animals form an explicitly allowed cohort calibration, not the same later animals. Non-numeric early-death times and censoring cannot be interpreted as exact scheduled times; exclusions are counted, and this creates survivorship/measurement selection limits. Source already reports virulence/reproducibility criteria; no new clinical efficacy claim. Source laboratory directory supplies validation identity; the original SITE field is inconsistent in one workbook and is preserved as provided_site. Header templates and source censoring inconsistencies require caution.

**Limits.** Two development laboratories and one historically exposed diagnostic laboratory. All15scored GSK observations are at24h; no kinetic, survival or antibiotic-efficacy admission. The continuation removes site from numerical inputs; site remains the whole-group validation identity.

**Historical exposure record.** All original diagnostic outcomes were already exposed. This is source-aware retrospective research. Documentation corrections do not create fresh confirmation or alter fit/selection.

**Current exposure.** All outcomes exposed; future scoring is retrospective.

**Source scope.** original_corpus

**Source.** https://zenodo.org/records/15124940

**Source terms.** cc-by-4.0

## Permitted prediction inputs

| Variable | Unit / interpretation |
|---|---|
| `time_h` | h |
| `initial_logCFU` | log10 CFU per total lung |

Identifiers and source locators are alignment metadata. They may route documented frozen calibration states; they are not a license to look up a scored target. Additional columns outside this list are not predictors.

## Reproduction and comparison

`run.py` and `rules.json` contain executable frozen equations and every coefficient. `evidence/metrics.csv` and `evidence/predictions.csv.gz` preserve the historical comparisons. The shared evaluator recalculates them and compares submitted predictions on identical covered observations. Model IDs are local to this task and are distinct from finding IDs.

Primary aggregation and eligible observations are frozen. Excluded/nonpositive log targets are reported separately from physical-unit error. Uncertainty is described at independent-group level; no row bootstrap is used. The raw adapter emits native anchors, eligibility, calibration and group records. Preparation does not fit or tune a model.

Default reference: `reference`. Comparator models: `reference`, `endpoint`, `clock`, `burden`, `burden_clock`, `quadratic`, `capacity`, `shrink`.

Use `python evaluation/benchmark.py example --task P100-078.continuation.v1 --output NEW_FOLDER` from the benchmark root. Historical development/confirmation separation cannot be reused as a fresh holdout after exposure.
