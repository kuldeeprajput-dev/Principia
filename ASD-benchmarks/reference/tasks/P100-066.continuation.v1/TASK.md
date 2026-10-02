# P100-066.continuation.v1

**Target.** Excess hydrogen uptake

**Units.** wt.%

**Error units.** wt.%

**Primary metric.** mae

**Primary metric units.** wt.%

**Cohort.** P100-066.continuation.v1.cohort-1

**Prediction time.** Composition, pressure, temperature, branch only; no measured uptake-derived quantity as an input.

**Independent unit.** whole material composition across temperatures and both branches

**Hierarchy.** group

**Calibration and history.** Excess uptake is the native experimental response. Total uptake, cyclic reuse files and descriptor curves remain upstream; they are not independent excess-uptake confirmation. Excess adsorption can decline with pressure through gas-volume displacement; a monotone absolute-Langmuir law alone is an intentionally falsifiable baseline.

**Limits.** Four MOF/graphite compositions and one source campaign. A branch contrast has different sampled pressures and cannot by itself establish irreversible hysteresis.

**Historical exposure record.** Original confirmation is exposed. New candidates chosen only development and frozen before this retrospective diagnostic.

**Current exposure.** All outcomes exposed; future scoring is retrospective.

**Source scope.** original_corpus

**Source.** https://doi.org/10.57745/KR8BIW

**Source terms.** etalab 2.0

## Permitted prediction inputs

| Variable | Unit / interpretation |
|---|---|
| `eg_pct` | wt.% expanded graphite in material label |
| `temperature_K` | K |
| `pressure_bar` | bar |
| `branch` | 0 adsorption, 1 desorption |

Identifiers and source locators are alignment metadata. They may route documented frozen calibration states; they are not a license to look up a scored target. Additional columns outside this list are not predictors.

## Reproduction and comparison

`run.py` and `rules.json` contain executable frozen equations and every coefficient. `evidence/metrics.csv` and `evidence/predictions.csv.gz` preserve the historical comparisons. The shared evaluator recalculates them and compares submitted predictions on identical covered observations. Model IDs are local to this task and are distinct from finding IDs.

Primary aggregation and eligible observations are frozen. Excluded/nonpositive log targets are reported separately from physical-unit error. Uncertainty is described at independent-group level; no row bootstrap is used. The raw adapter emits native anchors, eligibility, calibration and group records. Preparation does not fit or tune a model.

Default reference: `reference`. Comparator models: `reference`, `ideal`, `eos`, `sips`, `thermal_capacity`, `dilution`, `branch`, `dual`, `constant`, `kernel`.

Use `python evaluation/benchmark.py example --task P100-066.continuation.v1 --output NEW_FOLDER` from the benchmark root. Historical development/confirmation separation cannot be reused as a fresh holdout after exposure.
