# P100-086: Erythromycin fermentation process dataset

> Principia-100 | Standardized portfolio | 1 October 2026

## Scenario and evaluation contract

Domain: Industrial fermentation. The current default task predicts Chemical potency six hours ahead in source potency unit (undocumented). Independent unit: whole production batch; chronologically latest 81 reserved. Its packaged cohort contains 9,132 assigned rows in 81 groups.

**All supplied outcomes are now exposed.** Historical reserved evaluations remain part of the evidence record; future scores are retrospective. No newly established fundamental law or measured deployment impact is admitted by this packaging.

## Current portfolio findings

**Reproduction:** A damped six-hour secant is a strong transparent forecast conditional on current potency, without identifying biochemical growth.

Limit: Saturation was not selected in development and cannot be promoted for its exposedscore. Current assay availability is essential; native hx physical units are unresolved.

**Numerical control:** A stronger multiscale causal-history ensemble improves forecasting substantially; delay and smoothness audits limit online/physical interpretation.

Limit: New 1/3/6/12 hslopes and memory are a different input budget .92.646 %of 39217 hourlytriples have second-difference ≤ 1 native unit; interpolation/assay receipt timing remain unknown. No comparison to author MASTER under matched contract exists.

## Versioned tasks

| Task family | Target and information | Source scope |
|---|---|---|
| original | Chemical potency six hours ahead (source potency unit (undocumented)) | original corpus |
| continuation | Chemical potency six hours ahead (source potency unit (undocumented)) | original corpus |

Different targets, calibration budgets and cohorts have different task IDs. Their raw error values cannot be pooled into a scenario ranking. Exact equations, coefficients, permitted variables, timing, groups and per-model results are bound in the task packages.

Evaluation: the shared CLI provides numerical scoring, explicit coverage and abstention, uncertainty and event diagnostics. Agent review separately assesses scientific support; no aggregate discovery score is produced.

<!-- pagebreak -->

## Detailed reference note: P100-086: Six-hour industrial fermentation potency prediction

> Local scientific reference, 1 October 2026. Causal forecasting reproduction; unconfirmed saturation candidate. No independently established new physical law or measured deployment benefit is claimed.

## Scenario and experimental inputs

Hourly historical erythromycin production exports, 406 source batches; 405 have usable exact six-hour lag/horizon pairs. The target hx is source-defined potency. Its physical unit and other process abbreviations remain undocumented. One industrial facility and one year; historical operational forecasting, no mechanistic law from unmapped sensors. Earlier batches only train later validation blocks.

The numerical target is **Chemical potency six hours ahead**, in **source potency unit (undocumented)**. Strictly causal potency history and cultivation clock. Matching plus/minus 6 h uses source clock; future values only become targets. All source bytes remain unchanged. Prepared analysis rows retain workbook, archive/member or signal-array anchors.

## Finding and executable equation

The frozen default is a simple damped trend extrapolation. A saturation candidate performs slightly better on final data but was not selected from those scores and is not promoted. Extra clock/asymmetry hypotheses fail to improve development evidence consistently.

$$
\widehat{c}(t+6)=c(t)+6\beta s_6(t),\qquad s_6(t)=\frac{c(t)-c(t-6)}{6}.
$$

The equation above is the compact physical candidate; the numerical default and every competing hypothesis are separately scored. Exact reference scales, clipping, causal sample recursion and every coefficient are in rules.json and run.py.

Here c is source-defined chemical potency in its undocumented native unit, t is the native hourly cultivation clock, s6 is the strictly past six-hour slope in source-unit/h, and beta is dimensionless. A measured current potency assay is explicitly required; the equation is not a sensor-only biochemical soft sensor.

| Coefficient or dimensionless basis term | Frozen value |
|---|---|
| Trend attenuation beta | 0.98065907 |

<!-- pagebreak -->

## Methods and reserved-cohort performance

Five main, substantively different ASD attempts and four follow-up structural controls were completed. Controls may revisit an earlier structure; they do not count as additional discoveries. Development uses whole-group folds (forward batch blocks for case 86). A mean predictor, established/simple domain relation and fixed kernel model with at most 64 centers receive identical permitted inputs. Coefficients and candidate selection were frozen before the separate scoring process. The default was chosen from development evidence; it is never replaced by a final-test winner.

There are **81 reserved groups**, **9132 eligible observations** and **9132 assigned input rows**. Primary metric: **mae**, with equal-group weighting, in **source potency unit (undocumented)**. Physical-unit MAE is also reported. Calibration rows and missing targets are not manufactured into successful predictions.

| Frozen model | Primary error | Group mean MAE |
|---|---|---|
| reference | 37.7591 | 37.7591 |
| mechanistic reference | 36.8173 | 36.8173 |
| mean | 2183.82 | 2183.82 |
| domain | 37.7591 | 37.7591 |
| rbf | 86.2487 | 86.2487 |
| persistence | 425.116 | 425.116 |

MAE units: **source potency unit (undocumented)**. Lower is better; these are errors, not classification accuracy percentages. Row count does not imply independent experimental replication.

## Meaning, limitations and evaluation

Useful for six-hour potency expectations conditional on an available current assay. It is not an inline biochemical sensor or established metabolite-growth law. Later production batches are held apart chronologically. No fitted pathway is automatically causal. Finite basis clocks and correlated predictors limit identification; fold coefficients, rank/conditioning, residuals, sensitivities and unsuccessful hypotheses remain available in research_history. Future agents may submit different valid equations; exact formula matching is not required. Predictions, physical-unit errors, group effects, coverage and uncertainty are scored separately from a hash-bound scientific review.

Run the reference with `python run.py`. Create a runnable submission with `python evaluator/evaluate.py example --output NEW_DIRECTORY`, then score it with `score --submission SUBMISSION --output NEW_REPORT --trust-code`. The collection `evaluation/` adds tolerance, tail-error, normalized-error, interval-score and risk/coverage diagnostics. All supplied targets are now exposed, so future scoring is retrospective and new confirmation requires fresh groups.

## Sources and prior analyses

Native source: https://zenodo.org/records/14619074. Source articles and known fitted relationships are disclosed in PRIOR_ART.json. Literature checking is targeted and non-exhaustive; model strength or a held-out numerical gain does not establish novelty. No private reference material enters this package.
