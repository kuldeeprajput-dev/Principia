# Hippocampal processed traces: a bounded population-state forecast

The source archive contains157MATsessions from28animal suffixes across dorsal/ventralCA1,contexts and study days. Twenty-seven Day4files have no processed.trace endpoint, leaving130trace sessions. All sessions from each animal are linked:23development animals and five reserved animals. A schema-inspected animal was permanently assigned development before numerical fitting.

## Endpoint and selected equation

The task predicts the source-component population mean over native frames $t+31$ through $t+60$. Let $e_t$ be the current30-frame population mean, $m_t$ the preceding300-frame mean, and $v_t=2(e_t-e_{t-30})$. The selected compact equation is

$$\widehat e=0.31327391e_t+0.68672609m_t-0.088994875\max(v_t,0)-0.0065038607\min(v_t,0).$$

All amplitudes remain **author processed-trace units** and all times remain native frame indices. The dimensionless coefficients describe released-signal recovery/asymmetry; they are not calcium lifetimes, spike rates or neuronal coupling constants. The current and historical summaries use only frames at or before $t$.

Six adaptive attempts tested uniform decay, local set-point recovery, inertia, cross-component heterogeneity, regional response and asymmetric rising/declining states. Development selected the compact asymmetric recovery relation within the1% simplicity tolerance. All coefficient states and alternative results remain available.


## Frozen results

|Model|Development group error|Reserved group error|
|---|---:|---:|
|baseline_persistence|0.0002879488|0.0003369348|
|baseline_velocity|0.0007027432|0.00083927|
|baseline_flexible|0.0002585612|0.0003032324|
|attempt_001_decay|0.0002784271|0.0003252555|
|attempt_002_relaxation|0.0002456698|0.0002824797|
|attempt_003_inertia|0.0002449329|0.0002814723|
|attempt_004_heterogeneity|0.0002407902|0.0002759831|
|attempt_005_region|0.0002447443|0.0002818887|
|attempt_006_asymmetry|0.0002403833|0.0002761791|

Selected before confirmation: **attempt_006_asymmetry**. Primary error is mean absolute error in author processed-trace units, averaged within each independent group and then equally across groups. All candidates are shown to preserve unfavorable results; a lower retrospective score does not change the selected reference.

The selected rule gives0.000276179author-trace-unit MAE on five reserved animals, compared with0.000336935persistence,0.000839270linear extrapolation and0.000303232flexible prediction. This is a useful scoped processed-signal forecasting extension, with no claim of a new neural law or demonstrated behavioral impact. The source does not document exact trace normalization or the polarity of exclude.SFPs flags in twelve sessions. Accordingly, all released component rows contribute; this is not an independently curated neuron-only target. Behavior arrays and validTraceFrames have unresolved indexing semantics, so freezing, speed alignment and seconds were excluded before fitting. Upstream author denoising/normalization may use future observations: causal-prefix guarantees apply to the released trace, not real-time fluorescence acquisition. Source fear/context findings are prior art, and this forecast cannot independently confirm them.

## Validation and reproducibility

Every30 native frames after300-frame history, forecast next30-frame population mean ending60 frames later. Only trace frames<=t are inputs. Native frame index is used without inferring seconds or behavior alignment. Past observed trace history is allowed. No held future calibration or source fitted maps/pvpreS/pvpostS enter features. All model parameters and flexible transforms are fitted on development animals.

Retained author-processed calcium traces only; amplitude normalization/calcium-event interpretation is not documented in the archive. No spikes,absolute calcium concentration or real-time physiology claim. Twenty-eight source animals; held animals stay within the same study. All outcomes are now exposed to later agents. Claims of new validation require fresh data or an explicitly retrospective designation. Source study and processing are disclosed in SOURCE_AND_UNITS and PRIOR_ART; this is computational confirmation, not independent experimental replication.

`python run.py` verifies the allowlisted package and reproduces all saved predictions. `rules.json` contains exact coefficients and all learned transforms; `EQUATIONS.md` names each feature and equation. The adjacent native adapter reconstructs source-hash-verified observations and predictors; `task_spec.json` declares input, timing, calibration and grouping budgets. Future proposals may use different equations under the same contract, or seek review of a genuinely different measured task.

Source: [Hippocampal processed-population trace forecasting](https://zenodo.org/records/21225888); [primary source/prior art](https://doi.org/10.1038/s41593-026-02435-5). License recorded by source: CC BY4.0. Literature and semantics audited2 October2026.
