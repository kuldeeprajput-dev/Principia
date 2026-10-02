# P100-052: Wind-wake fields under dynamic induction control

> Local scientific reference, 1 October 2026. Scoped predictive extension. No independently established new physical law or measured deployment benefit is claimed.

## Scenario and experimental inputs

Lidar-derived time-average velocity grids from two turbines, four controls and several downstream sections under ABL Type II. Raw line-of-sight measurements remain upstream; interpolated cells are correlated. Only four controls and one wind-tunnel system; three development controls and one reserved. Spatial errors describe field interpolation/transfer, not independent grid replicates.

The numerical target is **Interpolated time-average streamwise wake velocity**, in **m/s**. Geometry and actuation settings only; no reserved velocity or rotor-equivalent speed is a predictor. All source bytes remain unchanged. Prepared analysis rows retain workbook, archive/member or signal-array anchors.

## Finding and executable equation

A Gaussian deficit plus background vertical shear and an anisotropic perturbation transfers to the reserved Strouhal control. The actuation coefficients are small relative to the base deficit; gains do not prove a new induction-control mechanism.

$$
\widehat{u}=7-\frac{(A_0+A_1I_2+A_2s+A_3sI_2)g}{(1+kx)^2}+Bz+Cg\frac{y^2-z^2}{\sigma^2}.\quad g=e^{-(y^2+z^2)/(2\sigma^2)},\quad\sigma=0.35+kx.
$$

The equation above is the compact physical candidate; the numerical default and every competing hypothesis are separately scored. Exact reference scales, clipping, causal sample recursion and every coefficient are in rules.json and run.py.

Here x, y and z are downstream-section/lateral/vertical coordinates normalized by the 0.58 m rotor diameter; I2 is one for the downstream turbine and zero otherwise, s is Strouhal number, k is a dimensionless wake-spreading parameter, sigma is dimensionless width, and g is the Gaussian field. All A, B and C coefficients have units m/s. The fixed 7 m/s is the documented nominal inflow, not a fitted held-out velocity.

| Coefficient or dimensionless basis term | Frozen value |
|---|---|
| 1: -Gaussian(r/(0.35+k*xD))/(1+k*xD)^2 | 3.512222 |
| 2: wake * indicator(turbine2) | 0.5114602 |
| 3: wake * Strouhal | 0.0458071 |
| 4: wake * Strouhal * turbine2 | -0.3502961 |
| 5: vertical ABL shear z/D | 0.9738138 |
| 6: wake anisotropy quadrupole | 0.3113348 |

<!-- pagebreak -->

## Methods and reserved-cohort performance

Five main, substantively different ASD attempts and four follow-up structural controls were completed. Controls may revisit an earlier structure; they do not count as additional discoveries. Development uses whole-group folds (forward batch blocks for case 86). A mean predictor, established/simple domain relation and fixed kernel model with at most 64 centers receive identical permitted inputs. Coefficients and candidate selection were frozen before the separate scoring process. The default was chosen from development evidence; it is never replaced by a final-test winner.

There are **1 reserved groups**, **2205 eligible observations** and **2205 assigned input rows**. Primary metric: **mae**, with equal-group weighting, in **m/s**. Physical-unit MAE is also reported. Calibration rows and missing targets are not manufactured into successful predictions.

| Frozen model | Primary error | Group mean MAE |
|---|---|---|
| reference | 0.32626 | 0.32626 |
| mechanistic reference | 0.32626 | 0.32626 |
| mean | 0.925392 | 0.925392 |
| domain | 0.703965 | 0.703965 |
| rbf | 0.639929 | 0.639929 |

MAE units: **m/s**. Lower is better; these are errors, not classification accuracy percentages. Row count does not imply independent experimental replication.

## Meaning, limitations and evaluation

Useful as a compact reconstruction/calibration relation for this wind-tunnel field. The source already studies dynamic induction. One reserved operating setting is insufficient for a new wake law or wind-farm energy-benefit claim. No fitted pathway is automatically causal. Finite basis clocks and correlated predictors limit identification; fold coefficients, rank/conditioning, residuals, sensitivities and unsuccessful hypotheses remain available in research_history. Future agents may submit different valid equations; exact formula matching is not required. Predictions, physical-unit errors, group effects, coverage and uncertainty are scored separately from a hash-bound scientific review.

Run the reference with `python run.py`. Create a runnable submission with `python evaluator/evaluate.py example --output NEW_DIRECTORY`, then score it with `score --submission SUBMISSION --output NEW_REPORT --replay`. The collection `_evaluation_25/` adds tolerance, tail-error, normalized-error, interval-score and risk/coverage diagnostics. All supplied targets are now exposed, so future scoring is retrospective and new confirmation requires fresh groups.

## Sources and prior analyses

Native source: https://zenodo.org/records/15356141. Source articles and known fitted relationships are disclosed in PRIOR_ART.json. Literature checking is targeted and non-exhaustive; model strength or a held-out numerical gain does not establish novelty. No private reference material enters this package.
