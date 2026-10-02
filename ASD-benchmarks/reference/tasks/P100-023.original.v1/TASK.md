# P100-023.original.v1

**Target.** Author-derived median coefficient of friction

**Units.** 1

**Error units.** 1

**Primary metric.** mae

**Primary metric units.** 1

**Cohort.** P100-023.original.v1.cohort-1

**Prediction time.** Conditional prediction at supplied trial-average speed/load. These trial summaries are not prospective controller inputs; no temporal forecasting claim.

**Independent unit.** whole participant

**Hierarchy.** group

**Calibration and history.** 165 participant–fluid observations (check actual count); primary response is author-derived median CoF, not instantaneous raw telemetry. Source already reports the Stribeck collapse and hydrodynamic exponent. Area/hydration are separate measurements; author-fit Hersey coefficients cannot validate their own physics. Raw force/position files remain untouched.

**Limits.** One substrate, eleven participants; transfer to reserved people under the same fluid panel, not other surfaces or contact systems. Fluids shared across participants.

**Historical exposure record.** All packaged targets are exposed for future agents; future scoring is retrospective. Public source-aware corpus. Illustrative header/first-row values were inspected during the semantics audit; these do not constitute blind source acquisition. All delivered targets become exposed after confirmation.

**Current exposure.** All outcomes exposed; future scoring is retrospective.

**Source scope.** original_corpus

**Source.** https://zenodo.org/records/15365365

**Source terms.** Creative Commons Attribution 4.0 International (CC BY 4.0)

## Permitted prediction inputs

| Variable | Unit / interpretation |
|---|---|
| `H` | dimensionless; author Hersey calibration |
| `viscosity` | Pa s at 500 s^-1; author rheology fit |
| `speed` | m/s |
| `load` | N |
| `hydration` | corneometer instrument units |
| `area` | cm^2 |

Identifiers and source locators are alignment metadata. They may route documented frozen calibration states; they are not a license to look up a scored target. Additional columns outside this list are not predictors.

## Reproduction and comparison

`run.py` and `rules.json` contain executable frozen equations and every coefficient. `evidence/metrics.csv` and `evidence/predictions.csv.gz` preserve the historical comparisons. The shared evaluator recalculates them and compares submitted predictions on identical covered observations. Model IDs are local to this task and are distinct from finding IDs.

Primary aggregation and eligible observations are frozen. Excluded/nonpositive log targets are reported separately from physical-unit error. Uncertainty is described at independent-group level; no row bootstrap is used. The raw adapter emits native anchors, eligibility, calibration and group records. Preparation does not fit or tune a model.

Default reference: `reference`. Comparator models: `reference`, `mechanistic_reference`, `attempt_001`, `attempt_002`, `attempt_003`, `attempt_004`, `attempt_005`, `attempt_006`, `attempt_007`, `baseline_mean`, `baseline_domain`, `baseline_rbf`, `attempt_008`, `attempt_009`.

Use `python evaluation/benchmark.py example --task P100-023.original.v1 --output NEW_FOLDER` from the benchmark root. Historical development/confirmation separation cannot be reused as a fresh holdout after exposure.
