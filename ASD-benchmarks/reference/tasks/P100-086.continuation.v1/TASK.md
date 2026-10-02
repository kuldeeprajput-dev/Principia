# P100-086.continuation.v1

**Target.** Chemical potency six hours ahead

**Units.** source potency unit (undocumented)

**Error units.** source potency unit (undocumented)

**Primary metric.** mae

**Primary metric units.** source potency unit (undocumented)

**Cohort.** P100-086.continuation.v1.cohort-1

**Prediction time.** At native hour t, the current hx assay and strictly earlier assay history plus cultivation clock are allowed. Features use exact earlier1/3/6/12h observations, backward slope curvature, causal EWMA and past-rate variability; no later assay or target smoothing supplies inputs. Target is hx at t+6h. Assays are assumed available at their recorded source times; true receipt latency is unresolved. New history features expand the former current/slope6 information contract for every comparator.

**Independent unit.** whole production batch; chronologically latest 81 reserved

**Hierarchy.** group

**Calibration and history.** Native hx is the source-loader target. Other undocumented abbreviations are excluded. Source units are not asserted to be mg/L or activity U/mL. 406 independent production batches; rows with exact 6 h lag/horizon only. No target smoothing or imputation. This is a six-hour prediction conditional on an available current potency assay, not an inline soft sensor.

**Limits.** One industrial facility; currently available potency assay required. Native units, upstream interpolation and actual assay receipt latency remain unresolved. Predictive gain is numerical, not a biochemical mechanism or deployed impact.

**Historical exposure record.** All original diagnostic outcomes were already exposed. This is source-aware retrospective research. Documentation corrections do not create fresh confirmation or alter fit/selection.

**Current exposure.** All outcomes exposed; future scoring is retrospective.

**Source scope.** original_corpus

**Source.** https://zenodo.org/records/14619074

**Source terms.** cc-by-4.0

## Permitted prediction inputs

| Variable | Unit / interpretation |
|---|---|
| `time_h` | h |
| `current` | source potency unit |
| `slope1` | source potency unit/h |
| `slope3` | source potency unit/h |
| `slope6` | source potency unit/h |
| `slope12` | source potency unit/h |
| `past_acc6` | source potency unit/h^2 |
| `ewma3` | source potency unit/h |
| `ewma6` | source potency unit/h |
| `window6_sd` | source potency unit/h |

Identifiers and source locators are alignment metadata. They may route documented frozen calibration states; they are not a license to look up a scored target. Additional columns outside this list are not predictors.

## Reproduction and comparison

`run.py` and `rules.json` contain executable frozen equations and every coefficient. `evidence/metrics.csv` and `evidence/predictions.csv.gz` preserve the historical comparisons. The shared evaluator recalculates them and compares submitted predictions on identical covered observations. Model IDs are local to this task and are distinct from finding IDs.

Primary aggregation and eligible observations are frozen. Excluded/nonpositive log targets are reported separately from physical-unit error. Uncertainty is described at independent-group level; no row bootstrap is used. The raw adapter emits native anchors, eligibility, calibration and group records. Preparation does not fit or tune a model.

Default reference: `reference`. Comparator models: `reference`, `trend`, `multi`, `curvature`, `phase`, `memory`, `ar`, `asymmetry`, `hgb`.

Use `python evaluation/benchmark.py example --task P100-086.continuation.v1 --output NEW_FOLDER` from the benchmark root. Historical development/confirmation separation cannot be reused as a fresh holdout after exposure.
