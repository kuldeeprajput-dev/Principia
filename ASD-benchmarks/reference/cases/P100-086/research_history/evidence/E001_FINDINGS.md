# P100-086: Six-hour industrial fermentation potency prediction

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

Run the reference with `python run.py`. Create a runnable submission with `python evaluator/evaluate.py example --output NEW_DIRECTORY`, then score it with `score --submission SUBMISSION --output NEW_REPORT --replay`. The collection `_evaluation_25/` adds tolerance, tail-error, normalized-error, interval-score and risk/coverage diagnostics. All supplied targets are now exposed, so future scoring is retrospective and new confirmation requires fresh groups.

## Sources and prior analyses

Native source: https://zenodo.org/records/14619074. Source articles and known fitted relationships are disclosed in PRIOR_ART.json. Literature checking is targeted and non-exhaustive; model strength or a held-out numerical gain does not establish novelty. No private reference material enters this package.
