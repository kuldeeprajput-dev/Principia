# Predicting forest-soil respiration at calibrated sites
> Principia-100 · P100-082 · Frozen scientific reference, 30 September 2026

## 1. Scenario and available measurements

The HoliSoils release contains 50,140 chamber observations, environmental measurements and management contexts from 2021-2025. Its 19 site labels mostly represent European forests; RincondelBatovi is in Uruguay. Flux is an author-calibrated chamber-slope product in g CO<sub>2</sub> m<super>-2</super> h<super>-1</super>. Native metadata also document soil temperature, volumetric water content, management and root-exclusion trenching. Raw chamber concentration time series are not supplied.

This task predicts a future chamber observation at an already calibrated site, using same-date environmental conditions and known context. It addresses interpretable environmental response models for monitoring. It does not evaluate unseen-site transfer, annual carbon budgets or causal management effects.

## 2. Experimental method

Inputs are native 5 cm soil temperature, volumetric moisture, day of year, site and subsite/trenching context. Rows require finite temperature within -15 to 50 degrees Celsius, moisture missing or within 0-100 native percent, and finite flux. All negative and unusually high finite flux values remain scored. The input-defined scope retains 38,389 rows; three Dutch sites lack 5 cm temperature entirely.

The latest 20% of native dates per site were reserved before fitting. Development contains 31,461 eligible rows at 16 sites; confirmation contains 6,928 rows at 15 sites. Dobroc has no eligible temperature input on its reserved dates, so it contributes no final score and is not resplit. Three forward development folds fit only earlier dates; all points and contexts on a date remain together. Context calibration, missingness treatment and flexible-model tuning use training data only.

Five cycles test moisture optimum, dry saturation, thermal-moisture interaction, site heterogeneity and seasonal response. The frozen selection favors a simpler domain model when its development error is within 1% of the best extension. Confirmation is scored in a separate process after selection; these targets are now exposed. Response slope, intercept, slope confidence interval and chamber-conversion quantities are forbidden predictors.

## 3. Reference equation and physical interpretation

The selected reference is the established Lloyd-Taylor temperature response. For a calibrated context c, with soil temperature T in degrees Celsius:

$$
\widehat R_c(T)=A_c\exp\!\left[E_0\left(\dfrac{1}{10+46.02}-\dfrac{1}{T+46.02}\right)\right]
$$

The reference coefficient is E<sub>0</sub> = 200.000005 K. Context amplitudes A have the same flux units as R; all 96 fitted amplitudes and site/global fallbacks are disclosed in `rules.json`. The denominator offsets represent temperature differences in kelvin, so the exponent is dimensionless. A is the fitted response at 10 degrees Celsius.

This is an apparent ecological temperature response. It combines microbial, root, substrate and transport effects rather than identifying one biochemical activation energy. A computational audit found that thermal-parameter scaling limited optimization and left E0 near its starting value. The unchanged frozen equation is therefore a near-200 K calibrated reference, not a claim of globally optimized thermal coefficients. A development-only profile found a small objective improvement near 210 K; no final data guided a revision.

<!-- pagebreak -->

## 4. Findings and predictive performance

The primary metric is mean RMSE over the 15 whole reserved site blocks. Each site receives equal weight regardless of its row count; multiple chambers and dates do not become independent sites.

| Frozen model | Mean site RMSE (g CO<sub>2</sub> m<super>-2</super> h<super>-1</super>) |
|---|---:|
| Selected Lloyd-Taylor reference | 0.287474 |
| Thermal-moisture interaction | 0.287676 |
| Q10 temperature response | 0.291073 |
| Calibrated context mean | 0.333953 |
| Fixed kernel comparator | 0.292475 |
| Nested-tuned kernel comparator | 0.290985 |

The reference improves mean error by 13.92% over context means, winning 14 of 15 sites. Its gain over Q10 is 1.24%; gains over kernel comparators are also below 2%. It fails the 5% improvement gate against every baseline. Site RMSE spans approximately 0.119-0.577 in native flux units, which exposes meaningful differences in reliability across systems.

The moisture interaction was the best ASD extension in development, but its gain over the simpler temperature reference was below 1%; on reserved sites their errors differ by only 0.000202. Added site-specific slopes and seasonal coefficients did not improve development evidence. These negative results constrain claims that extra mechanisms automatically yield better transfer. The frozen simpler selection is retained even though each comparison has different group-level strengths.

## 5. Practical value and limits

The reference provides a transparent, executable monitoring response with declared site calibration. Its value is a reproducible performance standard and evidence for the limits of added environmental complexity. It cannot replace sensor calibration or independent ecological measurements. A fitted context offset does not establish treatment causality or isolate root respiration.

Instrument differences, recurring collars, site/date correlations, missing moisture and unverified cross-site moisture conventions limit interpretation. No percent/fraction correction was invented. Negative flux and author-derived values are visible in the evidence. Coverage excludes rows without valid 5 cm inputs and all final observations at Dobroc. Fifteen calibrated systems do not establish universal geographic transfer; uncertainty cannot be estimated by treating 6,928 rows as independent replicates.

## 6. Evidence and use

`run.py` reproduces all frozen predictions and grouped errors; `rules.json` exposes every coefficient and calibration term. `data/` separates allowed predictors from source-row-anchored responses. `evidence/` and the evaluator support comparisons with other declared ASD outputs. `research_history/` retains all five cycles, date/eligibility manifests, prior art, freeze and optimizer qualification. Further score-guided revisions require fresh confirmation evidence.

Source: Lehtonen, Mäkipää and colleagues, [HoliSoils v1](https://zenodo.org/records/17519671), DOI 10.5281/zenodo.17519671. Prior art: [Lloyd and Taylor (1994)](https://doi.org/10.2307/2389824) and [Ruehr et al. (2010)](https://link.springer.com/article/10.1007/s10533-009-9383-z). Classification: established-model reproduction, reference comparison and preserved negative extension evidence; no adjudicated novelty.
