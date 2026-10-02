# P100-037.round2.v1

**Target.** Measured electrical router power

**Units.** W

**Error units.** W

**Primary metric.** mae

**Primary metric units.** W

**Cohort.** P100-037.round2.v1.development-oof

**Prediction time.** Current throughput and packet-size metadata only. Derived packet-rate proxies are not independent measurements; no measured temperature supports a thermal mechanism. Expanded information budget: u, q, packet_bytes, router

**Independent unit.** complete native run

**Hierarchy.** group

**Calibration and history.** See frozen development protocol and per-fold states; all learned calibration is training-partition-only. Separate A/B model parameters from the original development runs; no target-run refit.

**Limits.** Five reserved runs on two calibrated router models. No new-router or identified component-energy law is established. Repeatedly exposed development out-of-fold cohort; not the original reserved cohort.

**Historical exposure record.** All old confirmation groups exposed. Only original development groups used for fitting/selection. No repeated old-test evaluation in this round.

**Current exposure.** All outcomes exposed; future scoring is retrospective.

**Source scope.** original_corpus

**Source.** https://zenodo.org/records/17282065

**Source terms.** Creative Commons Attribution 4.0 International (CC BY 4.0)

## Permitted prediction inputs

| Variable | Unit / interpretation |
|---|---|
| `u` | dimensionless throughput / (200 Gbit/s) |
| `q` | dimensionless packet rate / (100 million packets/s) |
| `packet_bytes` | bytes |
| `router` | categorical A/B |

Identifiers and source locators are alignment metadata. They may route documented frozen calibration states; they are not a license to look up a scored target. Additional columns outside this list are not predictors.

## Reproduction and comparison

`run.py` and `rules.json` contain executable frozen equations and every coefficient. `evidence/metrics.csv` and `evidence/predictions.csv.gz` preserve the historical comparisons. The shared evaluator recalculates them and compares submitted predictions on identical covered observations. Model IDs are local to this task and are distinct from finding IDs.

Primary aggregation and eligible observations are frozen. Excluded/nonpositive log targets are reported separately from physical-unit error. Uncertainty is described at independent-group level; no row bootstrap is used. The raw adapter emits native anchors, eligibility, calibration and group records. Preparation does not fit or tune a model.

Default reference: `current/cycle-001`. Comparator models: `current/baseline-hgb`, `previous/results-v2/flexible`, `previous/results-v2/unconstrained1`, `previous/results-v2/cycle2`, `previous/results-v2/cycle1`, `previous/results-v2/unconstrained2`, `current/cycle-001`, `previous/results-v2/simple`, `previous/results-v2/linear`.

Use `python evaluation/benchmark.py example --task P100-037.round2.v1 --output NEW_FOLDER` from the benchmark root. Historical development/confirmation separation cannot be reused as a fresh holdout after exposure.
