# P100-023: Finger friction across people and liquids

> Local scientific reference, 1 October 2026. Reproduction; proposed extensions unsupported. No independently established new physical law or measured deployment benefit is claimed.

## Scenario and experimental inputs

Human finger-pad contact, fifteen fluids and eleven people; force/position telemetry, rheometry and separate hydration/area measurements are available. This task tests author-derived trial-median friction, not instantaneous instrument force. One substrate, eleven participants; transfer to reserved people under the same fluid panel, not other surfaces or contact systems. Fluids shared across participants.

The numerical target is **Author-derived median coefficient of friction**, in **1**. Conditional prediction at supplied trial-average speed/load. These trial summaries are not prospective controller inputs; no temporal forecasting claim. All source bytes remain unchanged. Prepared analysis rows retain workbook, archive/member or signal-array anchors.

## Finding and executable equation

The established Hersey/Stribeck response transfers better than the proposed physiological additions. Hydration, contact-pressure and material-residual hypotheses were tested and preserved, but are not admitted as new rules.

$$
\widehat{\mu}=c_0+c_1h^{-1/4}+c_2h^{0.55},\qquad h=H/0.02.
$$

The equation above is the compact physical candidate; the numerical default and every competing hypothesis are separately scored. Exact reference scales, clipping, causal sample recursion and every coefficient are in rules.json and run.py.

Here H is the dimensionless author-calibrated Hersey number and mu is the median dimensionless coefficient of friction. The three c coefficients are dimensionless. The source rheology calibration is disclosed; its fitted Hersey values are not independent validation of the same rheological mechanism.

| Coefficient or dimensionless basis term | Frozen value |
|---|---|
| 1 | 0 |
| (H/0.02)^(-1/4) | 0.1469803 |
| (H/0.02)^0.55 | 0.08365411 |

<!-- pagebreak -->

## Methods and reserved-cohort performance

Five main, substantively different ASD attempts and four follow-up structural controls were completed. Controls may revisit an earlier structure; they do not count as additional discoveries. Development uses whole-group folds (forward batch blocks for case 86). A mean predictor, established/simple domain relation and fixed kernel model with at most 64 centers receive identical permitted inputs. Coefficients and candidate selection were frozen before the separate scoring process. The default was chosen from development evidence; it is never replaced by a final-test winner.

There are **2 reserved groups**, **30 eligible observations** and **30 assigned input rows**. Primary metric: **mae**, with equal-group weighting, in **1**. Physical-unit MAE is also reported. Calibration rows and missing targets are not manufactured into successful predictions.

| Frozen model | Primary error | Group mean MAE |
|---|---|---|
| reference | 0.0876692 | 0.0876692 |
| mechanistic reference | 0.123484 | 0.123484 |
| mean | 0.252048 | 0.252048 |
| domain | 0.0876692 | 0.0876692 |
| rbf | 0.213502 | 0.213502 |

MAE units: **1**. Lower is better; these are errors, not classification accuracy percentages. Row count does not imply independent experimental replication.

## Meaning, limitations and evaluation

A compact known response is the useful numerical reference. More terms do not establish improved skin-contact physics. Independent surfaces or repeated sessions are needed before a new material-selection claim. No fitted pathway is automatically causal. Finite basis clocks and correlated predictors limit identification; fold coefficients, rank/conditioning, residuals, sensitivities and unsuccessful hypotheses remain available in research_history. Future agents may submit different valid equations; exact formula matching is not required. Predictions, physical-unit errors, group effects, coverage and uncertainty are scored separately from a hash-bound scientific review.

Run the reference with `python run.py`. Create a runnable submission with `python evaluator/evaluate.py example --output NEW_DIRECTORY`, then score it with `score --submission SUBMISSION --output NEW_REPORT --replay`. The collection `_evaluation_25/` adds tolerance, tail-error, normalized-error, interval-score and risk/coverage diagnostics. All supplied targets are now exposed, so future scoring is retrospective and new confirmation requires fresh groups.

## Sources and prior analyses

Native source: https://zenodo.org/records/15365365. Source articles and known fitted relationships are disclosed in PRIOR_ART.json. Literature checking is targeted and non-exhaustive; model strength or a held-out numerical gain does not establish novelty. No private reference material enters this package.
