# P100-072.original.v1

**Target.** Later author qPCR S.kudriavzevii percentage

**Units.** percentage points

**Error units.** percentage points

**Primary metric.** mae

**Primary metric units.** percentage points

**Cohort.** P100-072.original.v1.cohort-1

**Prediction time.** Author cached spreadsheet percentage from same-row qPCR ratio is the target. No same-time Cp/ratio is a predictor. Use only own replicate22/72-hour percentages to forecast96h and later. Biological replicate pairing from Sample Name.

**Independent unit.** whole co-cultured strain including every replicate/time

**Hierarchy.** group

**Calibration and history.** p22 and p72 are own-replicate fractions (source percentages/100). Delta=t−72h, and s is early log-odds change per hour. Fractions are clipped to0.0001–0.9999 only for log-odds calculation; original targets are unchanged. The output is100 times logistic(log-odds), in percentage points.75h is a development-selected shape scale. This early/late conditional equation does not estimate an independently measured fitness coefficient.

**Limits.** Two reserved yeast strain labels, eighteen later author-derived qPCR percentages, same experiment campaign with audit-exposed targets; no blind validation or nutrient mechanism identification.

**Historical exposure record.** All packaged targets are now exposed; future scoring is retrospective. Schema audit printed first13 spreadsheet rows before model construction, including several later percentages across all strains. Allocation is still metadata-only and no fit/selection uses reserved targets, but confirmation is audit-exposed retrospective evidence, not a fully blind independent confirmation.

**Current exposure.** All outcomes exposed; future scoring is retrospective.

**Source scope.** original_corpus

**Source.** https://zenodo.org/records/18757697

**Source terms.** cc-by-4.0

## Permitted prediction inputs

| Variable | Unit / interpretation |
|---|---|
| `p22_pct` | percentage points; own replicate at22h |
| `p72_pct` | percentage points; own replicate at72h |
| `time_h` | h since inoculation |

Identifiers and source locators are alignment metadata. They may route documented frozen calibration states; they are not a license to look up a scored target. Additional columns outside this list are not predictors.

## Reproduction and comparison

`run.py` and `rules.json` contain executable frozen equations and every coefficient. `evidence/metrics.csv` and `evidence/predictions.csv.gz` preserve the historical comparisons. The shared evaluator recalculates them and compares submitted predictions on identical covered observations. Model IDs are local to this task and are distinct from finding IDs.

Primary aggregation and eligible observations are frozen. Excluded/nonpositive log targets are reported separately from physical-unit error. Uncertainty is described at independent-group level; no row bootstrap is used. The raw adapter emits native anchors, eligibility, calibration and group records. Preparation does not fit or tune a model.

Default reference: `reference`. Comparator models: `reference`, `challenger`, `baseline_constant_selection`, `baseline_persistence`, `baseline_rbf`, `baseline_residual_rbf`.

Use `python evaluation/benchmark.py example --task P100-072.original.v1 --output NEW_FOLDER` from the benchmark root. Historical development/confirmation separation cannot be reused as a fresh holdout after exposure.
