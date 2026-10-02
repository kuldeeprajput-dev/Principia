# P100-010.original.v1

**Target.** NVD-authored CVSSv3.1 assessment present in current snapshot

**Target units.** binary source=nvd@nist.gov in cvssMetricV31

**Metric kind.** brier

**Timing contract.** All covariates are snapshot-available contemporaneous metadata. Source-day count and CNA assessment may be added after initial disclosure. This is current coverage diagnostics, not prediction of future NVD action or security exploitation.

**Calibration.** Whole CNA/source group folds and held sources; no held-source target calibration.

**Independent unit.** CVE records nested in complete assigning sources; duplicated JSON/gzip representations linked. Source-day batches dependent.

**Scope limits.** August23,2026 recent-feed snapshot only. Source status code is excluded; CVSS score formula and severity are not predicted. NIST policy deprioritizes duplicate scoring, so absence is not unsafe analysis failure.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| age_days | days since publication at snapshot |
| cna_score | non-NVD CVSSv3.1 assessment present binary |
| batch_size | records from same assigning source and publication day |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-010.original.v1 --output NEW_SUBMISSION; then score --task P100-010.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
