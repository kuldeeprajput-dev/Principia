# P100-067.original.v1

**Target.** Interface transit time

**Units.** s

**Error units.** s

**Primary metric.** log_transit

**Primary metric units.** absolute log ratio

**Cohort.** P100-067.original.v1.cohort-1

**Prediction time.** Use native upstream observations ending before interface entry; no interpolation across entry. orientation_cos2 is mean cos(2 theta), NOT mean cos²(theta).

**Independent unit.** complete fluid configuration; particles balanced within configuration

**Hierarchy.** group → particle

**Calibration and history.** Source-defined interface width; upstream speed and orientation from the strict upstream observation prefix. No target transit is an input.

**Limits.** Three reserved configurations (1.1,2.1,3.1), one from each observed family. No universal sedimentation law, normal-stress inference or thickness-dependent claim is supported.

**Historical exposure record.** All reference confirmation targets are exposed. This is a retrospective diagnostic evaluation, not fresh independent confirmation.

**Current exposure.** All outcomes exposed; future scoring is retrospective.

**Source scope.** original_corpus

**Source.** https://data.mendeley.com/datasets/ccm9k8pjft/1

**Source terms.** CC BY 4.0

## Permitted prediction inputs

| Variable | Unit / interpretation |
|---|---|
| `width_m` | m |
| `v_up_m_s` | m/s |
| `orientation_cos2` | dimensionless mean cos(2 theta), range [-1,1] |
| `particle` | categorical particle ID |
| `family` | categorical fluid family |

Identifiers and source locators are alignment metadata. They may route documented frozen calibration states; they are not a license to look up a scored target. Additional columns outside this list are not predictors.

## Reproduction and comparison

`run.py` and `rules.json` contain executable frozen equations and every coefficient. `evidence/metrics.csv` and `evidence/predictions.csv.gz` preserve the historical comparisons. The shared evaluator recalculates them and compares submitted predictions on identical covered observations. Model IDs are local to this task and are distinct from finding IDs.

Primary aggregation and eligible observations are frozen. Excluded/nonpositive log targets are reported separately from physical-unit error. Uncertainty is described at independent-group level; no row bootstrap is used. The raw adapter emits native anchors, eligibility, calibration and group records. Preparation does not fit or tune a model.

Default reference: `orientation`. Comparator models: `orientation`, `ballistic`, `particle_family`, `mean_orientation_control`.

Use `python evaluation/benchmark.py example --task P100-067.original.v1 --output NEW_FOLDER` from the benchmark root. Historical development/confirmation separation cannot be reused as a fresh holdout after exposure.
