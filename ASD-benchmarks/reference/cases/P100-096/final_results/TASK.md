# P100-096.original.v1

**Target.** Author-extracted cyclist speed one second ahead

**Units.** m/s

**Error units.** m/s

**Primary metric.** mae

**Primary metric units.** m/s

**Cohort.** P100-096.original.v1.cohort-1

**Prediction time.** Only current and past extracted speeds and current geometry/neighbor state. Future target speed is inaccessible to candidate replay.

**Independent unit.** whole original video, all parts/participants

**Hierarchy.** group

**Calibration and history.** Source computer-vision/Kalman trajectories, 25 Hz; select every 25th frame and exact +/-25-frame pairs. Parts of the same original video remain together. Track IDs may be ambiguous; all 28 riders recur across videos. Source preprocessing may use future smoothing, so predictions are retrospective trajectory dynamics and not certified online safety. Angular-neighbor interaction is a testable approximation; lateral separation and direction reversal are falsifiers.

**Limits.** One controlled circular-track session, recurring riders; no new-rider, on-road safety or crash-prevention transfer claim.

**Historical exposure record.** All packaged targets are exposed for future agents; future scoring is retrospective. Public source-aware corpus. Illustrative header/first-row values were inspected during the semantics audit; these do not constitute blind source acquisition. All delivered targets become exposed after confirmation.

**Current exposure.** All outcomes exposed; future scoring is retrospective.

**Source scope.** original_corpus

**Source.** https://zenodo.org/records/18098714

**Source terms.** cc-by-4.0

## Permitted prediction inputs

| Variable | Unit / interpretation |
|---|---|
| `speed` | m/s at current native frame |
| `past_acc` | m/s^2 from native speed 1 s earlier |
| `gap` | m; positive-angle arc gap to nearest forward angular bicycle |
| `relative_speed` | m/s; leader minus follower |
| `radius` | m |
| `lateral_gap` | m; radial separation to angular leader |
| `count` | tracked bicycles in frame |

Identifiers and source locators are alignment metadata. They may route documented frozen calibration states; they are not a license to look up a scored target. Additional columns outside this list are not predictors.

## Reproduction and comparison

`run.py` and `rules.json` contain executable frozen equations and every coefficient. `evidence/metrics.csv` and `evidence/predictions.csv.gz` preserve the historical comparisons. The shared evaluator recalculates them and compares submitted predictions on identical covered observations. Model IDs are local to this task and are distinct from finding IDs.

Primary aggregation and eligible observations are frozen. Excluded/nonpositive log targets are reported separately from physical-unit error. Uncertainty is described at independent-group level; no row bootstrap is used. The raw adapter emits native anchors, eligibility, calibration and group records. Preparation does not fit or tune a model.

Default reference: `reference`. Comparator models: `reference`, `mechanistic_reference`, `attempt_001`, `attempt_002`, `attempt_003`, `attempt_004`, `attempt_005`, `attempt_006`, `attempt_007`, `baseline_mean`, `baseline_domain`, `baseline_rbf`, `baseline_persistence`, `attempt_008`, `attempt_009`.

Use `python evaluation/benchmark.py example --task P100-096.original.v1 --output NEW_FOLDER` from the benchmark root. Historical development/confirmation separation cannot be reused as a fresh holdout after exposure.
