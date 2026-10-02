# Paired-well fluorescence: a compact distribution-scaling reference

The source contains18flow-cytometry files: uninduced and doxycycline-induced triplicates of MFSD5,WT SLC30A8 and the D110N_D224N mutant. One matched technical block (AD) is reserved; the other two blocks develop models. Each block includes all three cell lines and their paired controls. Nine quantiles per induced well yield27 reserved endpoints; cells and quantiles are not independent biological replicates.

## Endpoint and equation

The numerical response is the native AF488-channel fluorescence quantile, using a declared finite-event, positive-FSC/SSC gate. Let $C_\ell(q)$ be the paired uninduced control quantile, where $q=0.1,0.2,\ldots,0.9$. The selected equation is

$$\widehat Y_\ell(q)=a_\ell C_\ell(q),\qquad (a_{\mathrm{MFSD5}},a_{\mathrm{WT}},a_{\mathrm{mutant}})=(8.581667,2.8155461,1.0296662).$$

Factors are dimensionless. This is a calibrated distribution mapping in arbitrary detector units, not a glycan concentration or transport-affinity law. Paired uninduced measurements are allowed to every model; induced outcomes never enter predictors.

Five adaptive attempts compared multiplicative scaling, quantile-dependent recruitment, location/scale deformation, saturation and a WT-specific tail change. Simple multiplicative scaling remained the smallest model within1% of best development performance. Profiled saturation scales and recruitment thresholds are preserved as additional fitted state, not counted as independent discoveries.


## Frozen results

|Model|Development group error|Reserved group error|
|---|---:|---:|
|baseline_copy|12047.52|14030.59|
|baseline_shift|8722.627|9471.531|
|baseline_flexible|11800.14|8023.274|
|attempt_001_multiplicative|3510.698|3272.206|
|attempt_002_recruitment|3821.699|4505.16|
|attempt_003_location_scale|3510.193|3756.221|
|attempt_004_saturation|3534.02|3019.117|
|attempt_005_tail_selective|7920.459|8670.019|

Selected before confirmation: **attempt_001_multiplicative**. Primary error is mean absolute error in native AF488 channel units, averaged within each independent group and then equally across groups. All candidates are shown to preserve unfavorable results; a lower retrospective score does not change the selected reference.

The selected mapping gives3272.21native-unit MAE on the held technical block, compared with14030.59 for control-copy,9471.53 for line-specific shifts and8023.27 for the flexible comparator. The mutant factor is close to one while the WT factor is larger, consistent with the source study’s already-published selective response. This is replication-compatible technical calibration evidence, not a new transporter mechanism. The paper methods say Alexa488, matching native AF488, but figure captions say Alexa647; the discrepancy remains unresolved. Original manual FlowJo gates are absent, so these summaries do not claim exact reproduction of the published gated geometric means. One plate and one held technical block do not establish biological or instrument transfer.

## Validation and reproducibility

After paired uninduced control well is measured, before observing induced well target. Quantiles0.1–0.9 and cell-line identity are known; no induced fluorescence enters predictors. Same-block, same-cell-line uninduced distribution is permitted calibration for every model. Source identity compensation retained; no fitted manual gates or target-based threshold.

One plate and three technical replicate blocks. Does not establish biological-replicate transfer, transporter causality or glycan concentration. The channel/caption inconsistency prevents unqualified dye-specific biological claims. All outcomes are now exposed to later agents. Claims of new validation require fresh data or an explicitly retrospective designation. Source study and processing are disclosed in SOURCE_AND_UNITS and PRIOR_ART; this is computational confirmation, not independent experimental replication.

`python run.py` verifies the allowlisted package and reproduces all saved predictions. `rules.json` contains exact coefficients and all learned transforms; `EQUATIONS.md` names each feature and equation. The adjacent native adapter reconstructs source-hash-verified observations and predictors; `task_spec.json` declares input, timing, calibration and grouping budgets. Future proposals may use different equations under the same contract, or seek review of a genuinely different measured task.

Source: [Paired-well lectin-fluorescence response distributions](https://zenodo.org/records/14720967); [primary source/prior art](https://doi.org/10.1038/s44320-025-00106-4). License recorded by source: CC BY4.0. Literature and semantics audited2 October2026.
