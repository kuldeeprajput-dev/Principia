# P100-069: A compact causal gearbox-temperature observer

> Local scientific reference, 1 October 2026. Scoped observer extension. No independently established new physical law or measured deployment benefit is claimed.

## Scenario and experimental inputs

Five identification and eight source validation runs from one industrial robot gearbox. Housing/environment temperatures, speed and friction torque are measured. The initial lubricant temperature is explicitly allowed calibration. Evidence remains limited to this gearbox; no unseen-device or sensorless-temperature claim is made.

The numerical target is **Lubricant temperature**, in **degree C**. Causal housing/environment/friction history through current sample plus first lubricant temperature. Exclude t=0 from scoring because it is calibration, not a forecast. All source bytes remain unchanged. Prepared analysis rows retain workbook, archive/member or signal-array anchors.

## Finding and executable equation

A causal housing-temperature lag plus a speed-dependent offset is the strongest compact development hypothesis. Its ambient weight reaches a boundary, favoring simplification. Removing the friction-power term improves development evidence, so actual heat pathways are not identified by the fit.

$$
\frac{d\widehat{T}_L}{dt}=\frac{T_H+\gamma|\omega|-\widehat{T}_L}{\tau},\qquad\widehat{T}_L(0)=T_L(0),\quad\tau=200\ {\rm s},\quad\gamma=9.76855\ {\rm K}/({\rm rad\,s^{-1}}).
$$

The equation above is the compact physical candidate; the numerical default and every competing hypothesis are separately scored. Exact reference scales, clipping, causal sample recursion and every coefficient are in rules.json and run.py.

Here TL and TH are lubricant and housing temperature in degree C, t and tau are in seconds, omega is measured angular speed in rad/s and gamma converts absolute speed into an effective temperature offset. The executable recurrence uses previous-sample piecewise-constant forcing and the declared initial TL only. Gamma is a motion/heating proxy, not identified friction power or convection.

| Coefficient or dimensionless basis term | Frozen value |
|---|---|
| 1: causal housing-minus-environment convolution; complementary weights sum to one | 1 |
| 2: causal absolute-speed convection surrogate | 9.768554 |

<!-- pagebreak -->

## Methods and reserved-cohort performance

Five main, substantively different ASD attempts and four follow-up structural controls were completed. Controls may revisit an earlier structure; they do not count as additional discoveries. Development uses whole-group folds (forward batch blocks for case 86). A mean predictor, established/simple domain relation and fixed kernel model with at most 64 centers receive identical permitted inputs. Coefficients and candidate selection were frozen before the separate scoring process. The default was chosen from development evidence; it is never replaced by a final-test winner.

There are **8 reserved groups**, **16560 eligible observations** and **16568 assigned input rows**. Primary metric: **mae**, with equal-group weighting, in **degree C**. Physical-unit MAE is also reported. Calibration rows and missing targets are not manufactured into successful predictions.

| Frozen model | Primary error | Group mean MAE |
|---|---|---|
| reference | 1.40002 | 1.40002 |
| mechanistic reference | 1.40002 | 1.40002 |
| mean | 8.7333 | 8.7333 |
| domain | 4.02612 | 4.02612 |
| rbf | 6.17112 | 6.17112 |
| persistence | 4.02612 | 4.02612 |

MAE units: **degree C**. Lower is better; these are errors, not classification accuracy percentages. Row count does not imply independent experimental replication. The worst reserved run has MAE **2.728 degree C**. Every individual run remains in by_group.csv; cooldown and long-term errors are not hidden.

## Meaning, limitations and evaluation

Useful as a reproducible lubricant-temperature estimate when housing temperature, motion history and initial lubricant calibration are available. The source already presents an observer. One gearbox and no measured intervention costs cannot establish deployment impact. No fitted pathway is automatically causal. Finite basis clocks and correlated predictors limit identification; fold coefficients, rank/conditioning, residuals, sensitivities and unsuccessful hypotheses remain available in research_history. Future agents may submit different valid equations; exact formula matching is not required. Predictions, physical-unit errors, group effects, coverage and uncertainty are scored separately from a hash-bound scientific review.

Run the reference with `python run.py`. Create a runnable submission with `python evaluator/evaluate.py example --output NEW_DIRECTORY`, then score it with `score --submission SUBMISSION --output NEW_REPORT --replay`. The collection `_evaluation_25/` adds tolerance, tail-error, normalized-error, interval-score and risk/coverage diagnostics. All supplied targets are now exposed, so future scoring is retrospective and new confirmation requires fresh groups.

## Sources and prior analyses

Native source: https://doi.org/10.18419/DARUS-5015. Source articles and known fitted relationships are disclosed in PRIOR_ART.json. Literature checking is targeted and non-exhaustive; model strength or a held-out numerical gain does not establish novelty. No private reference material enters this package.
