# P100-052.original.v1

**Target.** Interpolated time-average streamwise wake velocity

**Units.** m/s

**Error units.** m/s

**Primary metric.** mae

**Primary metric units.** m/s

**Cohort.** P100-052.original.v1.cohort-1

**Prediction time.** Geometry and actuation settings only; no reserved velocity or rotor-equivalent speed is a predictor.

**Independent unit.** whole control setting across turbines and downstream sections

**Hierarchy.** group

**Calibration and history.** Source-native lidar-derived uu grids; grid cells are correlated interpolated products. Raw vlos retained upstream. Rotor-equivalent wind and virtual turbine power are excluded as targets and predictors. No cubic-power identity is counted as a rule. ABL Type II only.

**Limits.** Only four controls and one wind-tunnel system; three development controls and one reserved. Spatial errors describe field interpolation/transfer, not independent grid replicates.

**Historical exposure record.** All packaged targets are exposed for future agents; future scoring is retrospective. Public source-aware corpus. Illustrative header/first-row values were inspected during the semantics audit; these do not constitute blind source acquisition. All delivered targets become exposed after confirmation.

**Current exposure.** All outcomes exposed; future scoring is retrospective.

**Source scope.** original_corpus

**Source.** https://zenodo.org/records/15356141

**Source terms.** cc-by-4.0

## Permitted prediction inputs

| Variable | Unit / interpretation |
|---|---|
| `turbine` | 1 or 2 (within installation) |
| `x_D` | downstream distance/0.58 m rotor diameter |
| `y_D` | lateral coordinate/rotor diameter |
| `z_D` | vertical coordinate/rotor diameter |
| `St` | actuation Strouhal number, 0 labels greedy baseline |

Identifiers and source locators are alignment metadata. They may route documented frozen calibration states; they are not a license to look up a scored target. Additional columns outside this list are not predictors.

## Reproduction and comparison

`run.py` and `rules.json` contain executable frozen equations and every coefficient. `evidence/metrics.csv` and `evidence/predictions.csv.gz` preserve the historical comparisons. The shared evaluator recalculates them and compares submitted predictions on identical covered observations. Model IDs are local to this task and are distinct from finding IDs.

Primary aggregation and eligible observations are frozen. Excluded/nonpositive log targets are reported separately from physical-unit error. Uncertainty is described at independent-group level; no row bootstrap is used. The raw adapter emits native anchors, eligibility, calibration and group records. Preparation does not fit or tune a model.

Default reference: `reference`. Comparator models: `reference`, `mechanistic_reference`, `attempt_001`, `attempt_002`, `attempt_003`, `attempt_004`, `attempt_005`, `attempt_006`, `attempt_007`, `baseline_mean`, `baseline_domain`, `baseline_rbf`, `attempt_008`, `attempt_009`.

Use `python evaluation/benchmark.py example --task P100-052.original.v1 --output NEW_FOLDER` from the benchmark root. Historical development/confirmation separation cannot be reused as a fresh holdout after exposure.
