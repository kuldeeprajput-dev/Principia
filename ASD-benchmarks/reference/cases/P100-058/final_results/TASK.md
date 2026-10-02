# P100-058.continuation.v1

**Target.** Storage modulus G prime

**Units.** Pa

**Error units.** Pa

**Primary metric.** log_mae

**Primary metric units.** dimensionless natural-log ratio

**Cohort.** P100-058.continuation.v1.cohort-1

**Prediction time.** Temperature and imposed frequency only. Loss modulus is withheld as an orthogonal mechanistic check; never a primary predictor.

**Independent unit.** whole temperature sweep

**Hierarchy.** group

**Calibration and history.** Native DFS text exports only; paired TAD exports are linked duplicates, not independent samples. Target storage modulus and secondary loss modulus are separate native instrument outputs, though both share systematic calibration. No compliance correction was applied by the authors. A single purchased polymer batch.

**Limits.** Temperature transfer within one material; no batch-to-batch or general polymer law claim. Positive modulus spans orders of magnitude. Three native negative storage readings limit low-modulus physical interpretation; logarithmic performance is conditional on 32 positive responses.

**Historical exposure record.** Original confirmation is exposed. New candidates chosen only development and frozen before this retrospective diagnostic.

**Current exposure.** All outcomes exposed; future scoring is retrospective.

**Source scope.** original_corpus

**Source.** https://zenodo.org/records/17294879

**Source terms.** cc-by-4.0

## Permitted prediction inputs

| Variable | Unit / interpretation |
|---|---|
| `temperature_C` | degree C |
| `omega` | rad/s |

Identifiers and source locators are alignment metadata. They may route documented frozen calibration states; they are not a license to look up a scored target. Additional columns outside this list are not predictors.

## Reproduction and comparison

`run.py` and `rules.json` contain executable frozen equations and every coefficient. `evidence/metrics.csv` and `evidence/predictions.csv.gz` preserve the historical comparisons. The shared evaluator recalculates them and compares submitted predictions on identical covered observations. Model IDs are local to this task and are distinct from finding IDs.

Primary aggregation and eligible observations are frozen. Excluded/nonpositive log targets are reported separately from physical-unit error. Uncertainty is described at independent-group level; no row bootstrap is used. The raw adapter emits native anchors, eligibility, calibration and group records. Preparation does not fit or tune a model.

Default reference: `reference`. Comparator models: `reference`, `wlf`, `arrhenius`, `fractional`, `plateau`, `wlf_sparse`, `constant`, `kernel`.

Use `python evaluation/benchmark.py example --task P100-058.continuation.v1 --output NEW_FOLDER` from the benchmark root. Historical development/confirmation separation cannot be reused as a fresh holdout after exposure.
