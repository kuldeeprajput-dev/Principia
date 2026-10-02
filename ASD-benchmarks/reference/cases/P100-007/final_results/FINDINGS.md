# Single-participant gait: phase memory beats local extrapolation

The retained source contains three treadmill force-platform runs from participant S1 at 0.5, 0.75 and 1 m/s. Both native vertical-force channels are present. The 0.5/0.75 m/s runs develop models in whole-run folds; the 1 m/s run is reserved. This tests within-person speed transfer, not generalization to other people.

## Task and selected rule

At each forecast time, the target is the 10 ms-averaged plate 1 force ending 100 ms later, in newtons. Features may use only prior force samples and the known treadmill speed. Let $F_t$ denote the causal 10 ms block mean. Estimate a period $T_t$ from the largest interior autocorrelation peak of the preceding 5 s, searching 0.6-2 s. Then

$$
\widehat F_{t+0.1\mathrm{s}}=F_{t+0.1\mathrm{s}-T_t}.
$$

The right-hand side is always historical because the shortest searched period exceeds the forecast horizon. No fitted response coefficient is required. Source timestamps are all zero; native order and the source-declared 1000 Hz sampling rate define time. The new blocks are deterministic 10 ms means; no cross-modal synchronization is asserted.

Five substantive extensions tested local damping/curvature, phase-slope fusion, bilateral load transfer, load-dependent local stiffness, and combined phase/bilateral correction. None beat the prior-cycle control on the development runs.


## Frozen results

|Model|Development group error|Reserved group error|
|---|---:|---:|
|baseline_persistence|170.5079|238.925|
|baseline_velocity|156.3821|288.3787|
|baseline_periodic|86.91508|55.87341|
|baseline_flexible|250.2433|173.0685|
|attempt_001_damped|130.9386|219.8783|
|attempt_002_phase|100.7851|94.17585|
|attempt_003_bilateral|123.4378|212.95|
|attempt_004_stance|128.1003|208.4907|
|attempt_005_phase_bilateral|101.2272|100.3414|

Selected before confirmation: **baseline_periodic**. Primary error is mean absolute error in N, averaged within each independent group and then equally across groups. All candidates are shown to preserve unfavorable results; a lower retrospective score does not change the selected reference.

The prior-cycle rule achieves 55.8734 N reserved-run MAE versus 238.9250 N persistence, 288.3787 N linear extrapolation and 173.0685 N flexible prediction. The large improvement demonstrates useful phase memory in this one gait record, but it reproduces established periodic prediction rather than discovering a new biomechanical law. The fitted local or bilateral coefficients did not transfer better; they should not be interpreted as stiffness, damping or causal limb-coupling constants. There is only one reserved run, so no population confidence interval or clinical outcome is justified.

## Validation and reproducibility

Causal 10 ms block means sampled 100 Hz from source 1000 Hz sequence. At block end t, predict the 10 ms block ending t+100 ms. Every feature uses blocks ending at or before t. No target calibration from held run; preceding five seconds of its force waveform supply causal period and history. Known treadmill speed is permitted.

One participant, three treadmill speeds; no independent-person generalization. Force-platform channels are signed and the source timing columns are unusable. All outcomes are now exposed to later agents. Claims of new validation require fresh data or an explicitly retrospective designation. Source study and processing are disclosed in SOURCE_AND_UNITS and PRIOR_ART; this is computational confirmation, not independent experimental replication.

`python run.py` verifies the allowlisted package and reproduces all saved predictions. `rules.json` contains exact coefficients and all learned transforms; `EQUATIONS.md` names each feature and equation. The adjacent native adapter reconstructs source-hash-verified observations and predictors; `task_spec.json` declares input, timing, calibration and grouping budgets. Future proposals may use different equations under the same contract, or seek review of a genuinely different measured task.

Source: [Single-participant vertical-force anticipation](https://physionet.org/content/multimodal-gait-dataset/1.0.0/); [primary source/prior art](https://doi.org/10.1186/s42490-026-00118-7). License recorded by source: CC BY4.0. Literature and semantics audited 2 October 2026.
