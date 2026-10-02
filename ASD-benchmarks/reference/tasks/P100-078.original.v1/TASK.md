# P100-078.original.v1

**Target.** Untreated bacterial burden in total lung

**Units.** log10 CFU / total lung

**Error units.** log10 ratio (decades)

**Primary metric.** mae

**Primary metric units.** log10 CFU / total lung

**Cohort.** P100-078.original.v1.cohort-1

**Prediction time.** Initial cohort burden and time/site only. No post-baseline measured target is an input; study/strain IDs are anchors, not predictors.

**Independent unit.** whole laboratory/site, all strains and studies

**Hierarchy.** group

**Calibration and history.** DSM/site-reference strain aliases resolved from source RefToDict plus explicit single-strain-study Overview links (source labeling discrepancies retained) and kept together. All ExperimentResults sheets included. Explicit untreated CFU lung single-value observations only, equality operator, compatible log-CFU lung units, numeric actual times 0–24 h. Time-zero animals form an explicitly allowed cohort calibration, not the same later animals. Non-numeric early-death times and censoring cannot be interpreted as exact scheduled times; exclusions are counted, and this creates survivorship/measurement selection limits. Source already reports virulence/reproducibility criteria; no new clinical efficacy claim. Source laboratory directory supplies validation identity; the original SITE field is inconsistent in one workbook and is preserved as provided_site. Header templates and source censoring inconsistencies require caution.

**Limits.** Three laboratories with recurring bacterial strains; two development sites and one exposed reserved site. This is retrospective laboratory transfer, not new-strain generalization or independent confirmation. Unresolved source strain labels remain anchors, not split identities.

**Historical exposure record.** All packaged targets are exposed for future agents; future scoring is retrospective. Primary source label/DSM identities remained inconsistent. Earlier development used some later GSK targets. No independent confirmation claim is made after this metadata repair.

**Current exposure.** All outcomes exposed; future scoring is retrospective.

**Source scope.** original_corpus

**Source.** https://zenodo.org/records/15124940

**Source terms.** cc-by-4.0

## Permitted prediction inputs

| Variable | Unit / interpretation |
|---|---|
| `time_h` | h; numeric actual time only |
| `initial_logCFU` | log10 CFU / total lung; mean observed time-zero cohort |
| `site` | source laboratory label |

Identifiers and source locators are alignment metadata. They may route documented frozen calibration states; they are not a license to look up a scored target. Additional columns outside this list are not predictors.

## Reproduction and comparison

`run.py` and `rules.json` contain executable frozen equations and every coefficient. `evidence/metrics.csv` and `evidence/predictions.csv.gz` preserve the historical comparisons. The shared evaluator recalculates them and compares submitted predictions on identical covered observations. Model IDs are local to this task and are distinct from finding IDs.

Primary aggregation and eligible observations are frozen. Excluded/nonpositive log targets are reported separately from physical-unit error. Uncertainty is described at independent-group level; no row bootstrap is used. The raw adapter emits native anchors, eligibility, calibration and group records. Preparation does not fit or tune a model.

Default reference: `reference`. Comparator models: `reference`, `mechanistic_reference`, `attempt_001`, `attempt_002`, `attempt_003`, `attempt_004`, `attempt_005`, `attempt_006`, `attempt_007`, `baseline_mean`, `baseline_domain`, `baseline_rbf`, `attempt_008`, `attempt_009`.

Use `python evaluation/benchmark.py example --task P100-078.original.v1 --output NEW_FOLDER` from the benchmark root. Historical development/confirmation separation cannot be reused as a fresh holdout after exposure.
