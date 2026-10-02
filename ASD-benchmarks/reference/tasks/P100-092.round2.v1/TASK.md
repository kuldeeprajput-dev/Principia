# P100-092.round2.v1

**Target.** Channel-resolved burst-mean RSSI

**Units.** dBm

**Error units.** dB

**Primary metric.** mae

**Primary metric units.** dB

**Cohort.** P100-092.round2.v1.development-oof

**Prediction time.** Only the initial calibration map and known date/furniture/antenna/channel metadata are allowed. Whole dates remain grouped; repeated packets/cells are not independent experiments. Expanded information budget: r0, channel_contrast, position_contrast, spatial_contrast, global_power_reference, local_channel_power_dB, furniture, day, lwa, port, channel

**Independent unit.** complete measurement date (all available furniture states)

**Hierarchy.** group

**Calibration and history.** See frozen development protocol and per-fold states; all learned calibration is training-partition-only. Initial 3120-cell measured RSSI map is a declared input, with same-position channel and same-channel spatial contrasts. No target-date RSSI recalibration.

**Limits.** Temporal transfer on days 51,86,94 at calibrated positions in one installation. Not unseen-position prediction or independent antenna-efficiency identification. Repeatedly exposed development out-of-fold cohort; not the original reserved cohort.

**Historical exposure record.** All old confirmation groups exposed. Only original development groups used for fitting/selection. No repeated old-test evaluation in this round.

**Current exposure.** All outcomes exposed; future scoring is retrospective.

**Source scope.** original_corpus

**Source.** https://zenodo.org/records/14548531

**Source terms.** cc-by-4.0

## Permitted prediction inputs

| Variable | Unit / interpretation |
|---|---|
| `r0` | dBm |
| `channel_contrast` | dB |
| `position_contrast` | dB |
| `spatial_contrast` | dB |
| `global_power_reference` | dBm; power-domain spatial calibration mean |
| `local_channel_power_dB` | dBm; power-domain channel calibration mean |
| `furniture` | binary indicator |
| `day` | elapsed days |
| `lwa` | binary indicator for ports P1-P4 |
| `port` | categorical P1–P8 |
| `channel` | channel number 37/38/39 |

Identifiers and source locators are alignment metadata. They may route documented frozen calibration states; they are not a license to look up a scored target. Additional columns outside this list are not predictors.

## Reproduction and comparison

`run.py` and `rules.json` contain executable frozen equations and every coefficient. `evidence/metrics.csv` and `evidence/predictions.csv.gz` preserve the historical comparisons. The shared evaluator recalculates them and compares submitted predictions on identical covered observations. Model IDs are local to this task and are distinct from finding IDs.

Primary aggregation and eligible observations are frozen. Excluded/nonpositive log targets are reported separately from physical-unit error. Uncertainty is described at independent-group level; no row bootstrap is used. The raw adapter emits native anchors, eligibility, calibration and group records. Preparation does not fit or tune a model.

Default reference: `current/cycle-001`. Comparator models: `current/baseline-hgb`, `previous/results-v2/flexible`, `previous/results-v2/unconstrained1`, `previous/results-v2/cycle1`, `previous/results-v2/linear`, `current/cycle-001`, `previous/results-v2/unconstrained2`, `previous/results-v2/cycle2`, `previous/results-v2/simple`, `previous/results/simple`.

Use `python evaluation/benchmark.py example --task P100-092.round2.v1 --output NEW_FOLDER` from the benchmark root. Historical development/confirmation separation cannot be reused as a fresh holdout after exposure.
