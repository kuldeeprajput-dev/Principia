# P100-055.continuation.v1

**Target.** Individual penetration normal force at mixing age30min

**Units.** N

**Error units.** N

**Primary metric.** mae

**Primary metric units.** N

**Cohort.** P100-055.continuation.v1.cohort-1

**Prediction time.** Completed age0 mean force curve and known formulation precede every age30 target. Native index is supplied; no future age30 target, stress fit or mislabeled mixture supplies predictors.

**Independent unit.** whole mixture, all aged traces; age0 calibration available

**Hierarchy.** group

**Calibration and history.** Complete age0 traces are permitted per-mixture calibration for every model. No age30 force is an input. SP/VMA fractions use final author-entered masses; intermediate label inconsistencies are retained in the audit.

**Limits.** Nine mixtures, two initial and two aged traces per mixture. Aged prediction is calibrated with the completed initial-force map. No intrinsic stress/rate or causal additive law identified.

**Historical exposure record.** Every original source outcome is exposed. Development used seven fixed mixtures; diagnostic used the other two after selection freeze. Scores are retrospective. Revised calibration task differs from the old both-age uncalibrated task; do not compare their MAEs directly.

**Current exposure.** All outcomes exposed; future scoring is retrospective.

**Source scope.** original_corpus

**Source.** https://zenodo.org/records/17092152

**Source terms.** cc-by-4.0

## Permitted prediction inputs

| Variable | Unit / interpretation |
|---|---|
| `ratio` | dimensionless author aggregate/binder mass ratio |
| `water` | dimensionless author water/binder ratio |
| `sp_fraction` | SP/binder mass ratio, dimensionless |
| `vma_fraction` | VMA/binder mass ratio, dimensionless |
| `penetration_index` | native index; sampling interval unresolved |
| `initial_force` | N, measured age0 replicate mean at matching index |
| `initial_shape_change` | N, age0 mean difference over50native indices |

Identifiers and source locators are alignment metadata. They may route documented frozen calibration states; they are not a license to look up a scored target. Additional columns outside this list are not predictors.

## Reproduction and comparison

`run.py` and `rules.json` contain executable frozen equations and every coefficient. `evidence/metrics.csv` and `evidence/predictions.csv.gz` preserve the historical comparisons. The shared evaluator recalculates them and compares submitted predictions on identical covered observations. Model IDs are local to this task and are distinct from finding IDs.

Primary aggregation and eligible observations are frozen. Excluded/nonpositive log targets are reported separately from physical-unit error. Uncertainty is described at independent-group level; no row bootstrap is used. The raw adapter emits native anchors, eligibility, calibration and group records. Preparation does not fit or tune a model.

Default reference: `reference`. Comparator models: `reference`, `scientific_candidate`, `baseline_affine`, `baseline_gain`, `baseline_identity`, `baseline_kernel`, `baseline_mean`, `cycle_001_finite_buildup`, `cycle_002_packing_additives`, `cycle_003_shape_memory`, `cycle_004_water_rebuild`, `cycle_005_clock_build`, `cycle_006_shape_water`, `cycle_007_parsimonious_gain`.

Use `python evaluation/benchmark.py example --task P100-055.continuation.v1 --output NEW_FOLDER` from the benchmark root. Historical development/confirmation separation cannot be reused as a fresh holdout after exposure.
