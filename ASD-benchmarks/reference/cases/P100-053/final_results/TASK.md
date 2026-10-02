# P100-053.original.v1

**Target.** Angle-mean thread-forming torque, 700–1300 degrees

**Units.** Nm

**Error units.** Nm

**Primary metric.** mae

**Primary metric units.** Nm

**Cohort.** P100-053.original.v1.cohort-1

**Prediction time.** Current measurements stop at the frozen first-forward-crossing prefix (first sampled angle at/above 250 degrees); prior responses only from completed same-hole operations. Both holes and every reuse of a workpiece stay together.

**Independent unit.** workpiece (both locations and every reuse cycle)

**Hierarchy.** group

**Calibration and history.** Early and completed Finding-phase features; prior completed same-hole cycles are permitted. No current late-window target calibration.

**Limits.** 50 workpieces in eight observed surface conditions; predict torque, not clamping force, joint strength or the controller OK/NOK label.

**Historical exposure record.** All reference confirmation targets are exposed. This is a retrospective diagnostic evaluation, not fresh independent confirmation.

**Current exposure.** All outcomes exposed; future scoring is retrospective.

**Source scope.** original_corpus

**Source.** https://zenodo.org/records/16031381

**Source terms.** cc-by-4.0

## Permitted prediction inputs

| Variable | Unit / interpretation |
|---|---|
| `early` | Nm |
| `finding` | Nm |
| `gradient_proxy` | Nm |
| `roughness` | Nm |
| `usage` | cycle count |
| `left` | binary indicator |
| `has_history` | binary indicator |
| `prev_y` | Nm |
| `prev_early` | Nm |
| `prev_gradient` | Nm |
| `first_y` | Nm |
| `mean_past_y` | Nm |
| `history_gap` | cycle count |

Identifiers and source locators are alignment metadata. They may route documented frozen calibration states; they are not a license to look up a scored target. Additional columns outside this list are not predictors.

## Reproduction and comparison

`run.py` and `rules.json` contain executable frozen equations and every coefficient. `evidence/metrics.csv` and `evidence/predictions.csv.gz` preserve the historical comparisons. The shared evaluator recalculates them and compares submitted predictions on identical covered observations. Model IDs are local to this task and are distinct from finding IDs.

Primary aggregation and eligible observations are frozen. Excluded/nonpositive log targets are reported separately from physical-unit error. Uncertainty is described at independent-group level; no row bootstrap is used. The raw adapter emits native anchors, eligibility, calibration and group records. Preparation does not fit or tune a model.

Default reference: `memory`. Comparator models: `memory`, `linear`, `robust_linear`, `flexible`.

Use `python evaluation/benchmark.py example --task P100-053.original.v1 --output NEW_FOLDER` from the benchmark root. Historical development/confirmation separation cannot be reused as a fresh holdout after exposure.
