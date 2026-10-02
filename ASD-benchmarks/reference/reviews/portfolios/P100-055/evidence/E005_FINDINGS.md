# Case 55: calibrated aging of printable slag mixtures

> Principia-100 research continuation | 1 October 2026 | Retrospective calibrated task; no new constitutive law admitted

## Experiment and practical question

Ghent's CARBCOMN campaign measures penetration force for nine slag-based printable mixtures at mixing ages 0 and 30 min, with two independent trace columns per mixture and age. The practical question is whether a completed initial force curve can predict the aged force response of another mixture. Force is in newtons (N). The1-600 penetration coordinate remains a native acquisition index: the source does not establish its sampling interval or enough probe geometry to identify intrinsic yield stress.

The revised task, **P100-055-AGING30-v1**, explicitly permits the initial-age replicate-mean force map as per-mixture calibration. Known formulation and the earlier 50-index change in that initial map are also available. Every predictor has equal access. No aged target is an input, and no pairing of specimens across ages is assumed. This differs from the original uncalibrated task that predicted both ages; their error values are not directly comparable.

## Findings and executable rule

The development-selected reference is a single proportional aging gain:

$$
\widehat F_{30}(i)=g\,\overline{F}_0(i),\qquad g=1.713763480463801.
$$

Here, i is the native penetration index, both forces have units N, and g is dimensionless. The initial mean averages the two original age0 trace columns. This is an empirical calibration control, compatible with structural buildup but unable to distinguish chemical hardening, contact geometry or specimen variability.

Six material hypotheses tested bounded buildup, packing/additive effects, initial-curve shape, inverse water dependence, bounded penetration-clock response and a shape-water interaction. None improved on the gain control in whole-mixture development validation. Thus, extra physically plausible terms do not identify a more reliable mechanism in this small campaign. Their complete equations, parameters and unfavorable evidence are preserved.

## Experimental method and performance

Seven fixed development mixtures supply 8,400 aged rows. Outer leave-one-mixture-out validation retains both replicates together; tuning uses only inner whole-mixture folds. Two other previously exposed mixtures supply 2,400 diagnostic rows. Models and selection were frozen before this campaign's diagnostic scoring. Each mixture receives equal weight; correlated acquisition rows do not constitute 8,400 independent experiments.

| Predictor | Development MAE (N) | Exposed diagnostic MAE (N) |
|---|---|---|
| Selected proportional gain |0.08495|0.13632|
| Initial-force identity |0.24790|0.26198|
| Affine calibration control |0.09442|0.10342|
| Nested Gaussian-kernel control |0.13936|0.08282|
| Selected scientific shape candidate |0.09180|0.10042|
| Inverse-water candidate |0.09994|0.07286|

The diagnostic-better inverse-water or kernel models are retained rather than promoted. The selected gain's diagnostic group MAEs are 0.20374 N for 0.5_0.30 and 0.06891 N for 0.7_0.30. This uneven transfer falsifies a claim of uniformly accurate mixture-independent aging. Selection uncertainty and recipe confounding remain material.

## Source audit and independent-response limits

The final author formulation workbook contains the 1.0_0.25 recipe in row 75 although the PDF appendix omits it. Exact entered binder, superplasticizer and viscosity-modifier masses resolve that availability issue. Intermediate ratio fields disagree with final recipe labels; these inconsistencies remain recorded. Water, aggregate ratio and additive doses covary, so fitted additive or water coefficients would not establish causal effects.

A separate squeeze-flow sheet provides raw force and displacement. Threshold responses at compressive strains 0.10 and 0.20 were inventoried using author specimen heights. Some specimens never reach these thresholds; others cross them in large displacement jumps. Both source blocks labeled 1.0_0.30 are excluded from mixture mapping because the duplicate identity is unresolved. No missing threshold is imputed. These records are useful metrology evidence within the same campaign, not fresh confirmation or a validated cross-instrument constitutive law.

## Meaning, applicability and next evidence

The result provides a compact reproducible comparator for aged-force calibration and a clear test of additional mechanism claims. It can help evaluate whether an ASD agent improves prediction without introducing unsupported physics. It does not certify printability, industrial product performance, a universal aging gain, yield stress or a thixotropic time constant. Penetration-based structural buildup is already established prior art.

A stronger discovery would require documented probe geometry and acquisition spacing, independently replicated batches, controlled additive interventions and a reserved extrusion/shape-retention response. The current evidence supports a calibrated prediction task, source corrections and preserved falsifications; it does not demonstrate a new physical law or deployed industrial impact.

## Reproduction and evaluation

`run.py` and `rules.json` reproduce every frozen prediction using the declared input table. `evidence/` contains compact group errors, development comparison, formulation anchors and squeeze-response records. The evaluator accepts alternative executable equations, uncertainty intervals and justified abstention; it checks file bindings, replay and whole-mixture errors. All current diagnostic outcomes are exposed. New scientific confirmation requires additional unexposed groups, not better scores on this cohort.

Source: [CARBCOMN record 17092152](https://zenodo.org/records/17092152). Prior technique: [Pott and Stephan 2021](https://doi.org/10.1016/j.cemconcomp.2021.104066). Exact hypotheses, adaptive motivations, frozen states and negative results remain in the adjacent research history.
