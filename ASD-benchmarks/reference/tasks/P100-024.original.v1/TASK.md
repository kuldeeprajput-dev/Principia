# P100-024.original.v1

**Target.** Future measured composite stiffness conditional on continued recorded survival

**Units.** GPa

**Error units.** GPa

**Primary metric.** mae

**Primary metric units.** GPa

**Cohort.** P100-024.original.v1.cohort-1

**Prediction time.** Use cycle count, prescribed strain, supplied cure/header-frequency metadata and early E0 calibration only; no failure-cycle normalization or future measured stiffness. Exact header-frequency acquisition timing is undocumented; the selected log equation does not use frequency, while comparators condition on its availability.

**Independent unit.** complete specimen

**Hierarchy.** group

**Calibration and history.** E0 is the median native stiffness at cycles 10–20 for the same specimen; later stiffness and terminal cycle are unavailable to predictors.

**Limits.** Six specimens from three cure profiles in one glass-fiber campaign, with declared cycles-10-to-20 initial calibration. Not a remaining-life, runout or new-material prediction.

**Historical exposure record.** All reference confirmation targets are exposed. This is a retrospective diagnostic evaluation, not fresh independent confirmation.

**Current exposure.** All outcomes exposed; future scoring is retrospective.

**Source scope.** original_corpus

**Source.** https://zenodo.org/records/15665325

**Source terms.** Creative Commons Attribution 4.0 International (CC BY 4.0)

## Permitted prediction inputs

| Variable | Unit / interpretation |
|---|---|
| `cycle` | cycle count |
| `E0_GPa` | GPa |
| `strain_percent` | percent; numerical 1 means 1 percent strain |
| `frequency_Hz` | Hz; supplied source header |
| `cure` | categorical laminate/cure label |

Identifiers and source locators are alignment metadata. They may route documented frozen calibration states; they are not a license to look up a scored target. Additional columns outside this list are not predictors.

## Reproduction and comparison

`run.py` and `rules.json` contain executable frozen equations and every coefficient. `evidence/metrics.csv` and `evidence/predictions.csv.gz` preserve the historical comparisons. The shared evaluator recalculates them and compares submitted predictions on identical covered observations. Model IDs are local to this task and are distinct from finding IDs.

Primary aggregation and eligible observations are frozen. Excluded/nonpositive log targets are reported separately from physical-unit error. Uncertainty is described at independent-group level; no row bootstrap is used. The raw adapter emits native anchors, eligibility, calibration and group records. Preparation does not fit or tune a model.

Default reference: `attempt_001_log`. Comparator models: `attempt_001_log`, `baseline_persistence`, `baseline_log`, `baseline_flex`, `baseline_nested_flex`, `competitor_two_mechanism`.

Use `python evaluation/benchmark.py example --task P100-024.original.v1 --output NEW_FOLDER` from the benchmark root. Historical development/confirmation separation cannot be reused as a fresh holdout after exposure.
