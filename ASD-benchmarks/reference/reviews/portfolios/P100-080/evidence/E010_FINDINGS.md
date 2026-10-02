# Exercise electrodermal dynamics: persistence survives physiological challenges

The coherent aerobic subset contains30participants with wrist electrodermal activity (EDA), temperature and accelerometry. Six people are reserved, including both linked S11 recording segments;24 people develop models in five whole-person folds. Source4Hz EDA is in microSiemens, temperature in Celsius, and accelerometer units are converted using the source1/64g convention.

## Task and equation

Every five seconds after120seconds of observed history, the task predicts mean EDA over seconds25–30 ahead. The development-selected reference is

$$\widehat E_{[t+25,t+30]}=\overline E_{[t-5,t]}.$$

The rule has no fitted parameters. Each sensor's own start timestamp and sampling rate determine alignment; recording breaks are never bridged. The authors shift dates by a random number of days exceeding one year for privacy, consistently across sensors; these are alignment coordinates, not measurement calendar dates. Signed finite EDA is retained as released rather than silently clipped or excluded.

Five hypotheses tested tonic relaxation, damped drift, preceding activity, thermal change and asymmetric rising/recovery dynamics. Every extension was fitted only on training people with whole-person validation and identical observed-history access. The apparent physiological coefficients failed to improve the strong persistence control.


## Frozen results

|Model|Development group error|Reserved group error|
|---|---:|---:|
|baseline_persistence|0.8210218|0.4901973|
|baseline_velocity|1.469895|1.123018|
|baseline_flexible|0.8902059|0.5420116|
|attempt_001_relaxation|0.8367453|0.500288|
|attempt_002_damped_drift|0.8598989|0.5246933|
|attempt_003_activity|0.8732695|0.5355587|
|attempt_004_thermal|0.8601812|0.5246942|
|attempt_005_asymmetry|0.8500905|0.5206393|

Selected before confirmation: **baseline_persistence**. Primary error is mean absolute error in uS, averaged within each independent group and then equally across groups. All candidates are shown to preserve unfavorable results; a lower retrospective score does not change the selected reference.

Reserved participant-balanced MAE is0.4902uS for persistence, versus1.1230uS linear extrapolation and0.5420uS flexible prediction. This is useful bounded forecasting evidence and a negative result for the tested physiological extensions. It is not a new sweat-production law, a mental-stress classifier or a clinically validated wearable. Source exercise cadence changes and disconnections are preserved; the two source protocol versions within one study do not isolate temperature, autonomic activity and motion causally. Six held people warrant per-person error reporting, not narrow population confidence intervals.

## Validation and reproducibility

After120s observed history, every5s predict a future5s EDA mean ending30s later. All EDA,temperature and accelerometer summaries are causal and aligned by native starts/sample rates. No held-person outcome calibration. Past120s EDA is permitted state, identical for every model; response coefficients and flexible transforms fit training people only.

One aerobic study with two protocol versions; no mental-stress or clinical diagnosis. Source device clocks are not necessarily calendar measurement dates, and manufacturer EDA calibration remains author-provided. All outcomes are now exposed to later agents. Claims of new validation require fresh data or an explicitly retrospective designation. Source study and processing are disclosed in SOURCE_AND_UNITS and PRIOR_ART; this is computational confirmation, not independent experimental replication.

`python run.py` verifies the allowlisted package and reproduces all saved predictions. `rules.json` contains exact coefficients and all learned transforms; `EQUATIONS.md` names each feature and equation. The adjacent native adapter reconstructs source-hash-verified observations and predictors; `task_spec.json` declares input, timing, calibration and grouping budgets. Future proposals may use different equations under the same contract, or seek review of a genuinely different measured task.

Source: [Causal electrodermal response during exercise](https://physionet.org/content/wearable-device-dataset/1.0.1/); [primary source/prior art](https://doi.org/10.1038/s41597-025-04845-9). License recorded by source: ODC Attribution1.0. Literature and semantics audited2 October2026.

The official version1.0.1 dataset DOI is [10.13026/he0v-tf17](https://doi.org/10.13026/he0v-tf17). The two source recruitment stages use different aerobic schedules (Sxx/fxx); holding out participants does not establish transfer to an independently designed study.
