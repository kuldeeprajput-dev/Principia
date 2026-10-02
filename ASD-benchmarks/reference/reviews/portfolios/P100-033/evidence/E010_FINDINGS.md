# Smartphone pulse measurement: uncertainty-aware shrinkage

The released dataset contains3888 ten-second smartphone photoplethysmography segments from50 people, with simultaneous ECG-derived reference heart rate. Forty people develop the models in five whole-person folds; ten people (756 segments) are reserved. Human quality labels are preserved for diagnostics, not used as predictors or inclusion filters.

## Equation and information budget

Let $F$ be the dominant Fourier rate in bpm and $Q$ the fraction of fixed-band spectral energy around its peak. The selected rule is

$$w=\sigma(-2.1392928+2.1042882(Q-0.3)),\qquad \widehat h=\operatorname{clip}(wF+(1-w)84.61005,30,240)\;\mathrm{bpm}.$$

The search band is0.5–4Hz. The ECG-derived target never enters a waveform feature or per-person calibration. The coefficient84.61bpm is a development population prior, not a physiological constant. Signal concentration raises confidence in the Fourier estimate; it does not establish a calibrated probability of correctness.

Six substantive attempts tested harmonic correction, Fourier/autocorrelation fusion, quality shrinkage, motion/contact effects, discrete harmonic gating and agreement-conditioned consensus shrinkage. The shrinkage result motivated an additional development-only constant-median control before freezing; its historical addition is explicit.


## Frozen results

|Model|Development group error|Reserved group error|
|---|---:|---:|
|baseline_constant|11.65943|9.800231|
|baseline_fourier|32.2896|30.77508|
|baseline_autocorrelation|31.58865|30.12645|
|baseline_flexible|11.74158|9.031956|
|attempt_001_alias|34.25331|32.07775|
|attempt_002_fusion|30.50684|29.27755|
|attempt_003_shrinkage|11.2705|9.329169|
|attempt_004_motion_fusion|28.59009|29.69514|
|attempt_005_agreement_gate|32.52944|31.30643|
|attempt_006_consensus_shrink|11.42728|9.411953|

Selected before confirmation: **attempt_003_shrinkage**. Primary error is mean absolute error in bpm, averaged within each independent group and then equally across groups. All candidates are shown to preserve unfavorable results; a lower retrospective score does not change the selected reference.

The selected rule gives9.3292bpm held-person MAE, versus9.8002 for a population median and9.0320 for the flexible fusion comparator. It improves severely noisy direct estimators but does not beat the strongest flexible reference. Most apparent gain is attributable to the population prior, so this is a bounded calibration/robustness descriptor, not a new pulse law or clinically validated monitor. The waveform reader must honor gain/baseline encoding:48 records store300 channels in one frame, while later records store three RGB time series. Their native bytes are unchanged. Clinical acceptance tolerances and independent device transfer are absent.

## Validation and reproducibility

After the complete ten-second PPG segment; simultaneous ECG supplies the target but is never an input. Known recording motion/contact conditions are allowed. No human quality annotation is a predictor. No per-person ECG or target calibration. Spectral transforms are fixed within each PPG window; any fusion/shrinkage parameters or flexible scaling are trained on development people only.

50 participants in one smartphone protocol;10 held people. ECG-derived rate is an independent sensor reference, but no clinical agreement threshold or cardiovascular diagnosis is established. All outcomes are now exposed to later agents. Claims of new validation require fresh data or an explicitly retrospective designation. Source study and processing are disclosed in SOURCE_AND_UNITS and PRIOR_ART; this is computational confirmation, not independent experimental replication.

`python run.py` verifies the allowlisted package and reproduces all saved predictions. `rules.json` contains exact coefficients and all learned transforms; `EQUATIONS.md` names each feature and equation. The adjacent native adapter reconstructs source-hash-verified observations and predictors; `task_spec.json` declares input, timing, calibration and grouping budgets. Future proposals may use different equations under the same contract, or seek review of a genuinely different measured task.

Source: [PPG pulse-rate harmonic ambiguity](https://physionet.org/content/butppg/2.0.0/); [primary source/prior art](https://doi.org/10.13026/tn53-8153). License recorded by source: CC BY 4.0. Literature and semantics audited2 October2026.
