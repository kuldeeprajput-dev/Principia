# P100-027: KTH boiling two-phase water flow

> Principia-100 | Standardized portfolio | 1 October 2026

## Scenario and evaluation contract

Domain: thermal-fluid engineering. The current default task predicts Measured local vapor void fraction in dimensionless. Independent unit: complete experimental run. Its packaged cohort contains 36 assigned rows in 3 groups.

**All supplied outcomes are now exposed.** Historical reserved evaluations remain part of the evidence record; future scores are retrospective. No newly established fundamental law or measured deployment impact is admitted by this packaging.

## Current portfolio findings

**Retrospective extension:** Joint drift-flux/spatial calibration improves local development prediction but cannot identify universal slip constants.

Limit: C 0=.87924253 lies below one and compensates with odds/spatial terms; source coordinate geometry remains unresolved. The later positive-slip revision loses; the joint model remains an empirical calibrated reference.

**Unsupported or falsified:** A positive-slip physical revision does not improve the prior joint profile; the new flexible control sets a stronger numerical target.

Limit: Earlier joint C 0=0.879 can compensate with spatial/intercept terms. Enforcing positive slip alone loses; parameters are not uniquely identified.

## Versioned tasks

| Task family | Target and information | Source scope |
|---|---|---|
| original | Measured local vapor void fraction (dimensionless) | original corpus |
| round2 | Measured local vapor void fraction (dimensionless) | original corpus |

Different targets, calibration budgets and cohorts have different task IDs. Their raw error values cannot be pooled into a scenario ranking. Exact equations, coefficients, permitted variables, timing, groups and per-model results are bound in the task packages.

Evaluation: the shared CLI provides numerical scoring, explicit coverage and abstention, uncertainty and event diagnostics. Agent review separately assesses scientific support; no aggregate discovery score is produced.

<!-- pagebreak -->

## Detailed reference note: Boiling flow: a conditional radial void-profile reference
> Principia-100 · Case 27 · Calibrated within-facility extension

## 1. Scenario and available measurements

The KTH/Westinghouse HWAT corpus contains 12 boiling-water runs from 2023, released in 2025. Each XML run supplies boundary metadata, axial pressure/wall temperature and 12 radial void, velocity and phase-size records. These are processed experimental products. The target is local vapor void fraction, dimensionless; measured velocity and phase scales are excluded from predictors.

## 2. Experimental method

Metadata hashing reserved three whole runs and 36 positions; nine runs supported whole-run development validation. Five hypotheses tested slip, spatial profiles, mass-flux dependence, quality/profile interactions and established drift flux. Selection and stopping preceded confirmation. Flexible comparators used identical inputs, with nested training-group folds selecting kernel width and ridge. No target-derived regime label is used. Densities follow fixed IAPWS saturation calculations from absolute pressure; conclusions condition on supplied exit quality.

## 3. Equation and physical interpretation

Let x denote exit quality, ρ<sub>l</sub> and ρ<sub>v</sub> saturated densities, and s the native coordinate divided by its maximum sampled value in the run. Define

$$
\alpha_h=\dfrac{x/\rho_v}{x/\rho_v+(1-x)/\rho_l}.
$$

$$
\operatorname{logit}(\widehat{\alpha})=\operatorname{logit}(\alpha_h)+b_0+b_2s^2.
$$

Here b<sub>0</sub> = 0.644498 and b<sub>2</sub> = -2.411380, both dimensionless. The bounded equation describes spatial redistribution of phase odds. It is not an area-averaged conservation closure. Coordinate units are uncertain; s does not establish physical tube-radius or wall-distance geometry. The drift-flux comparator uses α = j<sub>g</sub> / [C<sub>0</sub>(j<sub>g</sub> + j<sub>l</sub>) + V<sub>d</sub>], with superficial fluxes and drift velocity in m/s. Exact parameters are in `rules.json`.

<!-- pagebreak -->

## 4. Findings and predictive performance

Primary MAE averages the 12 positions within each run, then the three run errors equally. All 36 assigned positions were scored.

| Frozen representation | Mean run MAE (void fraction) |
|---|---:|
| Quadratic profile correction | 0.106701 |
| Homogeneous saturated mixture | 0.182569 |
| Established drift-flux competitor | 0.139195 |
| Constant development mean | 0.323480 |
| Fixed flexible RBF | 0.207382 |
| Group-tuned flexible RBF | 0.254019 |

The correction lowers aggregate error by 41.56% versus homogeneous and improves all three runs against it. Individual MAE ranges 0.044966-0.187872. Drift flux wins the low-quality Run 32 counterexample: 0.051245 versus 0.187872 for the profile model. Added quality-dependent gradient terms failed development improvement. These are scoped predictive and negative findings; radial redistribution is established prior art and no novel physics is admitted.

## 5. Practical value and limits

The compact correction supplies an interpretable profile benchmark for thermal-hydraulic code development in this facility. Low quality/pressure confirmation conditions extend beyond development ranges; Run 32 demonstrates weak extrapolation. Source XOUT generation is not fully documented, so boundary conditioning is explicit. Three runs with possible shared-date calibration cannot establish population confidence, cross-geometry transfer or reactor safety certification. POWER/HEATFLUX scaling is unresolved and excluded. No industrial savings or critical heat-flux prediction is tested.

## 6. Evidence and use

`run.py` replays frozen equations without fitting. `rules.json` and native XML anchors make calculations auditable. Compact evidence retains all reserved runs and comparators. The evaluator scores alternative rules under the same information contract; admission and novelty remain scientific judgments. Targets are now exposed and rejected hypotheses remain in history.

Sources: [HWAT dataset, Zenodo 14627088](https://zenodo.org/records/14627088); Le Corre et al. (2025), [source publication](https://doi.org/10.1016/j.nucengdes.2025.114249); [IAPWS saturation release](https://www.iapws.org/relguide/Supp-sat.html). Drift flux follows Zuber and Findlay (1965), [doi:10.1115/1.3689137](https://doi.org/10.1115/1.3689137).
