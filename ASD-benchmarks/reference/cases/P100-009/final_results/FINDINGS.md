# Pupil forecasting: a strong persistence null result

Seven released NWB sessions contain pupil radius and treadmill velocity from three animals. Animals 16 and 22713 supply development folds; every session of animal 18 is reserved. Radius is in pixels, not millimeters. Animal 16/18 recordings accompany ACh-M1 measurements, while animal 22713 accompanies ACh-V1; animal, region and optical setup are therefore confounded.

## Endpoint and reference

The task predicts the mean pupil radius over the final 0.25 s of a one-second horizon, using only preceding released pupil and treadmill traces. The selected rule is the transparent persistence control:

$$
\widehat r_{t+1\mathrm{s}}=\overline{r}_{[t-0.25\mathrm{s},t]}.
$$

No coefficients or labeled held-animal calibration are fitted. A complete five-second prior pupil window and valid future target are required; NaN padding, blinks and gaps are excluded without interpolation or bridging. Every tenth native pupil sample is a forecast time. Treadmill summaries use only samples at or before issuance.

Five substantive attempts challenged persistence with local relaxation, damped inertia, movement-related arousal, asymmetric dilation/constriction and curvature. None improved whole-animal development error by the prespecified 1% threshold, so the simpler zero-parameter rule remained selected.


## Frozen results

|Model|Development group error|Reserved group error|
|---|---:|---:|
|baseline_persistence|1.215004|0.6672838|
|baseline_velocity|1.997211|1.052835|
|baseline_flexible|1.486282|0.6775208|
|attempt_001_relaxation|1.213808|0.6886343|
|attempt_002_inertia|1.222108|0.6870538|
|attempt_003_arousal|1.303822|0.6828302|
|attempt_004_asymmetry|1.234848|0.6821776|
|attempt_005_curvature|1.210643|0.6880599|

Selected before confirmation: **baseline_persistence**. Primary error is mean absolute error in px, averaged within each independent group and then equally across groups. All candidates are shown to preserve unfavorable results; a lower retrospective score does not change the selected reference.

Persistence achieves 0.6673 px MAE on the one held animal, versus 1.0528 px local velocity and 0.6775 px flexible prediction. This is a scientifically useful null result: the tested additional state/movement equations do not establish robust incremental transfer. It does not show that real pupil mechanics or arousal coupling are absent. Source preprocessing already includes DeepLabCut estimation, 1 Hz low-pass filtering and blink removal; its filter causality is unspecified. Thus all causal-prefix claims apply to the released trace, not raw-camera real-time forecasting. One held animal cannot support a population confidence interval or a new cholinergic mechanism.

## Validation and reproducibility

Predict 1 s-ahead author-released pupil radius from prior pupil and treadmill samples. Source prior filtering may be noncausal; causal-prefix guarantee applies to released traces only, not original camera pixels. No held-target calibration; observed past 5 s from each session supplies history. Pixel units are retained without invented millimeter scaling.

Only three retained animals. Optical pixel calibration differs by animal/session; source ACh-M1/V1 recordings confound region and animal. No retinal physiology or real-time instrument claim. All outcomes are now exposed to later agents. Claims of new validation require fresh data or an explicitly retrospective designation. Source study and processing are disclosed in SOURCE_AND_UNITS and PRIOR_ART; this is computational confirmation, not independent experimental replication.

`python run.py` verifies the allowlisted package and reproduces all saved predictions. `rules.json` contains exact coefficients and all learned transforms; `EQUATIONS.md` names each feature and equation. The adjacent native adapter reconstructs source-hash-verified observations and predictors; `task_spec.json` declares input, timing, calibration and grouping budgets. Future proposals may use different equations under the same contract, or seek review of a genuinely different measured task.

Source: [Within-installation pupil-state forecasting](https://dandiarchive.org/dandiset/001176); [primary source/prior art](https://doi.org/10.1016/j.celrep.2024.114808). License recorded by source: CC BY4.0. Literature and semantics audited 2 October 2026.
