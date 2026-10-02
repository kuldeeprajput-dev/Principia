# P100-092: Bluetooth Low Energy Separate Channel Fingerprinting dataset with Frequency-Scanned Antennas and Monopole

> Principia-100 | Standardized portfolio | 1 October 2026

## Scenario and evaluation contract

Domain: Wireless sensing. The current default task predicts Channel-resolved burst-mean RSSI in dBm. Independent unit: complete measurement date (all available furniture states). Its packaged cohort contains 15,600 assigned rows in 3 groups.

**All supplied outcomes are now exposed.** Historical reserved evaluations remain part of the evidence record; future scores are retrospective. No newly established fundamental law or measured deployment impact is admitted by this packaging.

## Current portfolio findings

**Numerical control:** Exact positive-power mixing compresses the calibration correction to three parameters but remains weaker than flexible prediction.

Limit: Exposed MAE 3.581295 dB vs 3.438900 dBflexible, losing every date; the initial 3120-cell map remains required. Improved correction is not reduced calibration cost or a propagation law.

**Unsupported or falsified:** Local channel-power redistribution fails to replace the prior globally calibrated/flexible descriptions.

Limit: All three development dates lose. Earlier positive-power correction diagnostic 3.581295 dB still loses flexible 3.438900 dB on every exposed date.

## Versioned tasks

| Task family | Target and information | Source scope |
|---|---|---|
| original | Channel-resolved burst-mean RSSI (dBm) | original corpus |
| round2 | Channel-resolved burst-mean RSSI (dBm) | original corpus |

Different targets, calibration budgets and cohorts have different task IDs. Their raw error values cannot be pooled into a scenario ranking. Exact equations, coefficients, permitted variables, timing, groups and per-model results are bound in the task packages.

Evaluation: the shared CLI provides numerical scoring, explicit coverage and abstention, uncertainty and event diagnostics. Agent review separately assesses scientific support; no aggregate discovery score is produced.

<!-- pagebreak -->

## Detailed reference note: Stability of a calibrated BLE radio map
> P100-092 | Scenario and findings | September 2026 reference results

The practical question is whether an initial Bluetooth Low Energy (BLE) calibration map can predict later channel-resolved received-signal strength. A six-coefficient correction improves the unchanged map in this installation, but remains slightly weaker than a flexible comparator and does not establish a propagation law.

## 1. Scenario and available measurements

The Cartagena BLE fingerprinting dataset contains 1,820 native position files, covering 130 positions across nine dates, eight beacon/antenna ports and advertising channels 37, 38 and 39. Each native row records timestamp, port, channel and RSSI. Antenna and furniture conditions provide controlled contrasts within one installation.

The response is the mean RSSI of a later acquisition burst at a known position, port and channel. RSSI is represented in dBm; prediction differences are in dB. The initial map contains 3,120 calibration-cell means. Two calibration cells have fewer than the usual 100 packets; their actual observations remain included. Later bursts contain ten packets, which are not ten independent scientific replicates.

## 2. Experimental method

Five post-calibration dates supported development, with forward validation that used earlier dates to predict later development dates. Nine substantive attempts examined channel contrast, power addition, temporal change, furniture effects, spatial contrast and antenna-dependent corrections. The compact candidate was selected and frozen before the three final dates were scored.

Confirmation includes every available burst cell on elapsed days 51, 86 and 94: 15,600 rows in total. Furniture states stay with their date; day 86 has no recorded furniture variant. Models use actual elapsed calendar time where needed, preserving the distinction from an inconsistent native day label. All positions were calibrated in advance. No response or fitted offset from the target date is available to a predictor.

## 3. Tested calibration equation

Let *R*<sub>0</sub> be the initial RSSI at the same position, port and channel. Channel contrast *c* subtracts the same-position/port mean across channels. Spatial contrast *s* subtracts the mean across positions for that port/channel. Both contrasts use only the initial map and have units dB. Define dimensionless normalized contrasts:

$$
c^*=\dfrac{c}{10\,\mathrm{dB}},\qquad s^*=\dfrac{s}{10\,\mathrm{dB}}.
$$

For furniture indicator *f*, the frozen correction is:

$$
\widehat R=R_0+a+df+b_c c^*+b_{cf}fc^*+b_s s^*+b_{sf}fs^*.
$$

In the displayed order, the six coefficients are (0.065404, -0.336774, -1.928850, -1.067131, -1.883365, -0.821530) dB. Adding the correction in dB to *R*<sub>0</sub> in dBm yields predicted RSSI in dBm. Negative contrast coefficients shrink initially extreme map values toward their channel or spatial averages; furniture modifies this response.

The model has six fitted correction coefficients **plus the measured 3,120-cell calibration map**. The map is a declared input, not hidden free calibration. The equation summarizes temporal response behavior; it does not separate multipath, receiver drift and physical installation changes.

<!-- pagebreak -->

## 4. Findings and predictive performance

**A small correction improves the unchanged calibration map.** Mean date MAE decreases from 3.92336 to 3.68956 dB, a 5.96% reduction on the reserved dates. This supports a useful scoped calibration comparison, with no target-date recalibration.

| Frozen model | Mean date MAE (dB) |
|---|---|
| Six-coefficient correction, selected before confirmation | 3.68956 |
| Flexible port/channel and quadratic comparator | 3.65548 |
| Unchanged initial map | 3.92336 |

For dates *g*, each containing *n* burst cells, the primary measure is:

$$
E_{\mathrm{MAE}}=\dfrac{1}{3}\sum_{g=1}^{3}\dfrac{1}{n_g}\sum_{i=1}^{n_g}|\widehat R_{gi}-R_{gi}|.
$$

Dates receive equal weight despite different row counts. The selected model's MAEs are 3.77594, 3.61042 and 3.68234 dB on days 51, 86 and 94. A dB error cannot be interpreted directly as localization accuracy or a fraction of successfully received packets.

**The compact rule is not the strongest predictor.** The flexible comparator uses fixed port/channel offsets and quadratic features and reaches 3.65548 dB. The compact rule is 0.03408 dB, or 0.93%, worse in the primary measure; it beats that comparator on only one of the three dates. It therefore fails the campaign's strongest-comparator admission requirement, even though its small parameter count is attractive.

## 5. Interpretation, practical value and limits

Contrast shrinkage offers a clear description of calibration instability: some initially strong or weak cells become less extreme later. It is compatible with changes in propagation and averaging, but also with regression toward the mean, hardware offsets or environmental change. Predictive shrinkage alone cannot identify a causal propagation mechanism.

The result is useful as a transparent comparator when studying how often a radio map needs recalibration or whether a compact correction is adequate. No reduced-calibration schedule, deployment saving or localization improvement was experimentally demonstrated. The 3,120-cell initial map remains a substantial measurement requirement.

Evidence is limited to temporal transfer at calibrated positions in one installation. It does not establish performance at unseen positions, in another room or with other devices. Date-level dependence, quantization, weak calibration cells and uncertain absolute receiver calibration remain relevant. The three dates are reported individually rather than treated as thousands of independent validation trials.

## 6. Evidence and use

Reproduction: `python run.py` replays the three frozen models. `rules.json` contains full-precision coefficients and map-access assumptions. Native archive members, source line numbers, positions and packet counts remain attached to the measured targets; `evidence/` gives every date-level result.

Evaluation: `evaluator/README.md` defines RSSI predictions, complete-date grouping, matched baseline comparisons, explicit abstentions and separate scientific review. Its task is known-position temporal response prediction, not a localization benchmark.

Status: the calibration comparison is retained as reference evidence; no new propagation law was admitted. All confirmation dates are now exposed. A revised rule needs fresh dates or installations, allocated before fitting, for new confirmation.

Source: López-Pastor and colleagues, [BLE fingerprinting measurements](https://zenodo.org/records/14548531), DOI 10.5281/zenodo.14548531. The source study is identified in the preserved research record; exact source hashes are in `rules.json`.
