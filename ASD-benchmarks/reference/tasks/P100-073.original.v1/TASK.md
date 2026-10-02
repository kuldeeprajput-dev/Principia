# P100-073.original.v1

**Target.** Author-converted later fermentation gas volume at native 12/24/36/48 hours

**Units.** mL

**Error units.** mL

**Primary metric.** rmse

**Primary metric units.** mL

**Cohort.** P100-073.original.v1.cohort-1

**Prediction time.** Only native 4/8-hour gas volumes and known trial/algae/horizon; no later volume, end-of-incubation digestibility or GasDM target-derived normalization.

**Independent unit.** complete DG4 incubation run within each trial; every flask and horizon stay together

**Hierarchy.** group

**Calibration and history.** Trial/algae kinetic and empirical parameters come from development DG1–3; current flask gas at 4/8 h is declared early calibration available to all comparators.

**Limits.** Three reserved incubation runs in three protocols with known algae labels and an 8-hour prefix. No methane-specific prediction, unseen-treatment or in-vivo livestock transfer.

**Historical exposure record.** All reference confirmation targets are exposed. This is a retrospective diagnostic evaluation, not fresh independent confirmation.

**Current exposure.** All outcomes exposed; future scoring is retrospective.

**Source scope.** original_corpus

**Source.** https://zenodo.org/records/18335590

**Source terms.** cc-by-4.0

## Permitted prediction inputs

| Variable | Unit / interpretation |
|---|---|
| `trial` | categorical protocol 1, 2 or 3 |
| `algae` | categorical source substrate/treatment label |
| `hour` | h |
| `g4` | mL, native volume at 4 h |
| `g8` | mL, native volume at 8 h |

Identifiers and source locators are alignment metadata. They may route documented frozen calibration states; they are not a license to look up a scored target. Additional columns outside this list are not predictors.

## Reproduction and comparison

`run.py` and `rules.json` contain executable frozen equations and every coefficient. `evidence/metrics.csv` and `evidence/predictions.csv.gz` preserve the historical comparisons. The shared evaluator recalculates them and compares submitted predictions on identical covered observations. Model IDs are local to this task and are distinct from finding IDs.

Primary aggregation and eligible observations are frozen. Excluded/nonpositive log targets are reported separately from physical-unit error. Uncertainty is described at independent-group level; no row bootstrap is used. The raw adapter emits native anchors, eligibility, calibration and group records. Preparation does not fit or tune a model.

Default reference: `curvature_saturation`. Comparator models: `curvature_saturation`, `first_order`, `dual_pool`, `empirical_ratio`, `persistence`, `linear_prefix`, `flexible_fixed`, `flexible_nested`.

Use `python evaluation/benchmark.py example --task P100-073.original.v1 --output NEW_FOLDER` from the benchmark root. Historical development/confirmation separation cannot be reused as a fresh holdout after exposure.
