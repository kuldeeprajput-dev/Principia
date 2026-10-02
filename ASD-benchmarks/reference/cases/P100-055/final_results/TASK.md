# P100-055.original.v1

**Target.** Individual penetration normal force

**Units.** N

**Error units.** N

**Primary metric.** mae

**Primary metric units.** N

**Cohort.** P100-055.original.v1.cohort-1

**Prediction time.** Known mix label, age and elapsed penetration index only; force is never an input.

**Independent unit.** whole mixture across both ages and replicates

**Hierarchy.** group

**Calibration and history.** Two independent trace columns per mixture/age are retained; source average columns excluded. Time header supplies time, without an explicit unit in the workbook; the native penetration clock unit is unresolved; no physical time constant is claimed. Dimensionless t/t_ref used in equations. Mix-label ratio meanings require author PDF; do not call these stress or yield-stress measurements.

**Limits.** Nine mix labels, two batches per mixture/age according to the source PDF, one early research campaign. Force–penetration-time relationships cannot identify intrinsic constitutive stress without probe kinematics/geometry.

**Historical exposure record.** All packaged targets are exposed for future agents; future scoring is retrospective. Public source-aware corpus. Illustrative header/first-row values were inspected during the semantics audit; these do not constitute blind source acquisition. All delivered targets become exposed after confirmation.

**Current exposure.** All outcomes exposed; future scoring is retrospective.

**Source scope.** original_corpus

**Source.** https://zenodo.org/records/17092152

**Source terms.** cc-by-4.0

## Permitted prediction inputs

| Variable | Unit / interpretation |
|---|---|
| `ratio` | mix-design ratio encoded in author mixture label |
| `water` | water ratio encoded in author mixture label |
| `age_min` | min since mixing; 0 or 30 |
| `time_s` | native penetration clock index; unit unspecified |

Identifiers and source locators are alignment metadata. They may route documented frozen calibration states; they are not a license to look up a scored target. Additional columns outside this list are not predictors.

## Reproduction and comparison

`run.py` and `rules.json` contain executable frozen equations and every coefficient. `evidence/metrics.csv` and `evidence/predictions.csv.gz` preserve the historical comparisons. The shared evaluator recalculates them and compares submitted predictions on identical covered observations. Model IDs are local to this task and are distinct from finding IDs.

Primary aggregation and eligible observations are frozen. Excluded/nonpositive log targets are reported separately from physical-unit error. Uncertainty is described at independent-group level; no row bootstrap is used. The raw adapter emits native anchors, eligibility, calibration and group records. Preparation does not fit or tune a model.

Default reference: `reference`. Comparator models: `reference`, `mechanistic_reference`, `attempt_001`, `attempt_002`, `attempt_003`, `attempt_004`, `attempt_005`, `attempt_006`, `attempt_007`, `baseline_mean`, `baseline_domain`, `baseline_rbf`, `attempt_008`, `attempt_009`.

Use `python evaluation/benchmark.py example --task P100-055.original.v1 --output NEW_FOLDER` from the benchmark root. Historical development/confirmation separation cannot be reused as a fresh holdout after exposure.
