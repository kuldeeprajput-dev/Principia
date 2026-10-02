# P100-037.original.v1

**Target.** Measured electrical router power

**Units.** W

**Error units.** W

**Primary metric.** mae

**Primary metric units.** W

**Cohort.** P100-037.original.v1.cohort-1

**Prediction time.** Current throughput and packet-size metadata only. Derived packet-rate proxies are not independent measurements; no measured temperature supports a thermal mechanism.

**Independent unit.** complete native run

**Hierarchy.** group

**Calibration and history.** Separate A/B model parameters from the original development runs; no target-run refit.

**Limits.** Five reserved runs on two calibrated router models. No new-router or identified component-energy law is established.

**Historical exposure record.** All reference confirmation targets are exposed. This is a retrospective diagnostic evaluation, not fresh independent confirmation.

**Current exposure.** All outcomes exposed; future scoring is retrospective.

**Source scope.** original_corpus

**Source.** https://zenodo.org/records/17282065

**Source terms.** Creative Commons Attribution 4.0 International (CC BY 4.0)

## Permitted prediction inputs

| Variable | Unit / interpretation |
|---|---|
| `router` | categorical A/B |
| `throughput_Gbps` | Gbit/s |
| `packet_bytes` | bytes |

Identifiers and source locators are alignment metadata. They may route documented frozen calibration states; they are not a license to look up a scored target. Additional columns outside this list are not predictors.

## Reproduction and comparison

`run.py` and `rules.json` contain executable frozen equations and every coefficient. `evidence/metrics.csv` and `evidence/predictions.csv.gz` preserve the historical comparisons. The shared evaluator recalculates them and compares submitted predictions on identical covered observations. Model IDs are local to this task and are distinct from finding IDs.

Primary aggregation and eligible observations are frozen. Excluded/nonpositive log targets are reported separately from physical-unit error. Uncertainty is described at independent-group level; no row bootstrap is used. The raw adapter emits native anchors, eligibility, calibration and group records. Preparation does not fit or tune a model.

Default reference: `compact`. Comparator models: `compact`, `flexible`, `throughput_only`.

Use `python evaluation/benchmark.py example --task P100-037.original.v1 --output NEW_FOLDER` from the benchmark root. Historical development/confirmation separation cannot be reused as a fresh holdout after exposure.
