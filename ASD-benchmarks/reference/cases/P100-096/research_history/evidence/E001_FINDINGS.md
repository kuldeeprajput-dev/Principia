# P100-096: One-second cycling dynamics on a circular track

> Local scientific reference, 1 October 2026. Near-tie to persistence; no new-law admission. No independently established new physical law or measured deployment benefit is claimed.

## Scenario and experimental inputs

Author-extracted, Kalman-processed trajectories from nine original videos and twenty-one parts in one controlled cycling session. Every part of a video stays together; riders recur across videos. One controlled circular-track session, recurring riders; no new-rider, on-road safety or crash-prevention transfer claim.

The numerical target is **Author-extracted cyclist speed one second ahead**, in **m/s**. Only current and past extracted speeds and current geometry/neighbor state. Future target speed is inaccessible to candidate replay. All source bytes remain unchanged. Prepared analysis rows retain workbook, archive/member or signal-array anchors.

## Finding and executable equation

A very small leader-speed relaxation survives simplification, while inertia, gap, lateral and curvature additions provide little reliable benefit. The final gain over speed persistence is below two percent and does not justify a new traffic law.

$$
\widehat{v}(t+1)=v(t)+0.097579\,[v_{\rm lead}(t)-v(t)].
$$

The equation above is the compact physical candidate; the numerical default and every competing hypothesis are separately scored. Exact reference scales, clipping, causal sample recursion and every coefficient are in rules.json and run.py.

Here v and vlead are source-extracted speeds in m/s and t is in seconds. The leader is the nearest bicycle along the positive source polar-angle direction at the current frame, irrespective of lane; this is a declared geometric approximation. The coefficient is a dimensionless one-second relaxation fraction. Author Kalman preprocessing may contain smoothing.

| Coefficient or dimensionless basis term | Frozen value |
|---|---|
| 1: leader relative speed * relaxation | 0.09757907 |

<!-- pagebreak -->

## Methods and reserved-cohort performance

Five main, substantively different ASD attempts and four follow-up structural controls were completed. Controls may revisit an earlier structure; they do not count as additional discoveries. Development uses whole-group folds (forward batch blocks for case 86). A mean predictor, established/simple domain relation and fixed kernel model with at most 64 centers receive identical permitted inputs. Coefficients and candidate selection were frozen before the separate scoring process. The default was chosen from development evidence; it is never replaced by a final-test winner.

There are **2 reserved groups**, **4437 eligible observations** and **4437 assigned input rows**. Primary metric: **mae**, with equal-group weighting, in **m/s**. Physical-unit MAE is also reported. Calibration rows and missing targets are not manufactured into successful predictions.

| Frozen model | Primary error | Group mean MAE |
|---|---|---|
| reference | 0.261642 | 0.261642 |
| mechanistic reference | 0.261642 | 0.261642 |
| mean | 0.851296 | 0.851296 |
| domain | 0.271487 | 0.271487 |
| rbf | 0.370173 | 0.370173 |
| persistence | 0.265823 | 0.265823 |

MAE units: **m/s**. Lower is better; these are errors, not classification accuracy percentages. Row count does not imply independent experimental replication.

## Meaning, limitations and evaluation

Useful as a stringent inertia/persistence control and a track-processing audit. The leader is defined geometrically; author smoothing and repeated riders prevent certified online safety or independent rider transfer. No fitted pathway is automatically causal. Finite basis clocks and correlated predictors limit identification; fold coefficients, rank/conditioning, residuals, sensitivities and unsuccessful hypotheses remain available in research_history. Future agents may submit different valid equations; exact formula matching is not required. Predictions, physical-unit errors, group effects, coverage and uncertainty are scored separately from a hash-bound scientific review.

Run the reference with `python run.py`. Create a runnable submission with `python evaluator/evaluate.py example --output NEW_DIRECTORY`, then score it with `score --submission SUBMISSION --output NEW_REPORT --replay`. The collection `_evaluation_25/` adds tolerance, tail-error, normalized-error, interval-score and risk/coverage diagnostics. All supplied targets are now exposed, so future scoring is retrospective and new confirmation requires fresh groups.

## Sources and prior analyses

Native source: https://zenodo.org/records/18098714. Source articles and known fitted relationships are disclosed in PRIOR_ART.json. Literature checking is targeted and non-exhaustive; model strength or a held-out numerical gain does not establish novelty. No private reference material enters this package.
