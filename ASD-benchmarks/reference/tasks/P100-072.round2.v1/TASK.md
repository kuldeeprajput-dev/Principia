# P100-072.round2.v1

**Target.** Residual glucose plus fructose

**Units.** g/L

**Error units.** g/L

**Primary metric.** mae

**Primary metric units.** g/L

**Cohort.** P100-072.round2.v1.development-oof

**Prediction time.** Author cached spreadsheet percentage from same-row qPCR ratio is the target. No same-time Cp/ratio is a predictor. Use only own replicate22/72-hour percentages to forecast96h and later. Biological replicate pairing from Sample Name. Expanded information budget: S22, S72, G22, G72, F22, F72, time_h, coculture

**Independent unit.** whole co-cultured strain including every replicate/time

**Hierarchy.** group

**Calibration and history.** See frozen development protocol and per-fold states; all learned calibration is training-partition-only. p22 and p72 are own-replicate fractions (source percentages/100). Delta=t−72h, and s is early log-odds change per hour. Fractions are clipped to0.0001–0.9999 only for log-odds calculation; original targets are unchanged. The output is100 times logistic(log-odds), in percentage points.75h is a development-selected shape scale. This early/late conditional equation does not estimate an independently measured fitness coefficient.

**Limits.** Two reserved yeast strain labels, eighteen later author-derived qPCR percentages, same experiment campaign with audit-exposed targets; no blind validation or nutrient mechanism identification. Repeatedly exposed development out-of-fold cohort; not the original reserved cohort.

**Historical exposure record.** All old confirmation groups exposed. Only original development groups used for fitting/selection. No repeated old-test evaluation in this round.

**Current exposure.** All outcomes exposed; future scoring is retrospective.

**Source scope.** original_corpus

**Source.** https://zenodo.org/records/18757697

**Source terms.** cc-by-4.0

## Permitted prediction inputs

| Variable | Unit / interpretation |
|---|---|
| `S22` | g/L; glucose + fructose at 22 h |
| `S72` | g/L; glucose + fructose at 72 h |
| `G22` | g/L glucose |
| `G72` | g/L glucose |
| `F22` | g/L fructose |
| `F72` | g/L fructose |
| `time_h` | h since inoculation |
| `coculture` | binary indicator |

Identifiers and source locators are alignment metadata. They may route documented frozen calibration states; they are not a license to look up a scored target. Additional columns outside this list are not predictors.

## Reproduction and comparison

`run.py` and `rules.json` contain executable frozen equations and every coefficient. `evidence/metrics.csv` and `evidence/predictions.csv.gz` preserve the historical comparisons. The shared evaluator recalculates them and compares submitted predictions on identical covered observations. Model IDs are local to this task and are distinct from finding IDs.

Primary aggregation and eligible observations are frozen. Excluded/nonpositive log targets are reported separately from physical-unit error. Uncertainty is described at independent-group level; no row bootstrap is used. The raw adapter emits native anchors, eligibility, calibration and group records. Preparation does not fit or tune a model.

Default reference: `current/cycle-001`. Comparator models: `current/cycle-003`, `current/cycle-002`, `current/cycle-004`, `current/cycle-001`, `current/baseline-hgb`, `previous/cycle-002`, `previous/cycle-003`, `previous/cycle-004`, `previous/cycle-001`, `previous/baseline-flex`, `previous/baseline-linear_sugar`, `previous/baseline-first_order`, `previous/baseline-persistence`.

Use `python evaluation/benchmark.py example --task P100-072.round2.v1 --output NEW_FOLDER` from the benchmark root. Historical development/confirmation separation cannot be reused as a fresh holdout after exposure.
