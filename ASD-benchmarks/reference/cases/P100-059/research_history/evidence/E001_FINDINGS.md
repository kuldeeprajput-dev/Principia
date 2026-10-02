# P100-059: Conditional photovoltaic yield across locations

> Local scientific reference, 1 October 2026. Scoped conditional predictive extension. No independently established new physical law or measured deployment benefit is claimed.

## Scenario and experimental inputs

Hourly measured energy from nine Portuguese plants in six cities, 2019–2022, paired with supplied city weather. Energy is divided by independent installed capacity. Only the input-defined daylight cohort is scored. Six cities, nine plants; plants within a city share weather and are not independent weather sites. Same-hour conditional energy prediction, not weather forecasting or proven thermal causality.

The numerical target is **Hourly produced energy divided by installed capacity**, in **kWh/kWp**. Contemporaneous weather and calendar/plant metadata only; no target energy, source specific-energy or emissions as inputs. All source bytes remain unchanged. Prepared analysis rows retain workbook, archive/member or signal-array anchors.

## Finding and executable equation

A radiation-scaled response with season and morning/afternoon asymmetry improves transfer to Loule. The fitted ambient-temperature coefficient is positive, so it must not be presented as identified physical thermal derating. Weather provenance and timezone remain unresolved.

$$
\widehat{e}=\operatorname{clip}\!\left[G\!\left(c_0+c_T\frac{T-25}{25}+c_GG+\frac{c_W}{1+v}+c_S\cos\frac{2\pi d}{365.25}+c_h\frac{h-12}{12}\right),0,e_{\rm grid}\right].
$$

The equation above is the compact physical candidate; the numerical default and every competing hypothesis are separately scored. Exact reference scales, clipping, causal sample recursion and every coefficient are in rules.json and run.py.

Here e is one-hour specific energy in kWh/kWp; G is supplied shortwave radiation divided by 1 kW/m2, T is ambient degree C, v is wind divided by 1 m/s, d is calendar day-of-year and h is source-clock hour. egrid is connection power/installed capacity times one hour. All c coefficients carry kWh/kWp. Clock alignment is source-based, with no unverified timezone conversion.

| Coefficient or dimensionless basis term | Frozen value |
|---|---|
| 1: irradiance/(1kW m^-2) | 0.8332719 |
| 2: irradiance * (ambientC-25)/25K | 0.09745504 |
| 3: irradiance^2: heating/clipping surrogate | -0.04884969 |
| 4: irradiance/(1+wind/(1m/s)) | 0.03052162 |
| 5: irradiance * seasonal cosine | 0.1975796 |
| 6: irradiance * afternoon asymmetry | 0.8929951 |

<!-- pagebreak -->

## Methods and reserved-cohort performance

Five main, substantively different ASD attempts and four follow-up structural controls were completed. Controls may revisit an earlier structure; they do not count as additional discoveries. Development uses whole-group folds (forward batch blocks for case 86). A mean predictor, established/simple domain relation and fixed kernel model with at most 64 centers receive identical permitted inputs. Coefficients and candidate selection were frozen before the separate scoring process. The default was chosen from development evidence; it is never replaced by a final-test winner.

There are **1 reserved groups**, **16966 eligible observations** and **16966 assigned input rows**. Primary metric: **mae**, with equal-group weighting, in **kWh/kWp**. Physical-unit MAE is also reported. Calibration rows and missing targets are not manufactured into successful predictions.

| Frozen model | Primary error | Group mean MAE |
|---|---|---|
| reference | 0.109696 | 0.109696 |
| mechanistic reference | 0.109696 | 0.109696 |
| mean | 0.242188 | 0.242188 |
| domain | 0.156793 | 0.156793 |
| rbf | 0.129916 | 0.129916 |

MAE units: **kWh/kWp**. Lower is better; these are errors, not classification accuracy percentages. Row count does not imply independent experimental replication.

## Meaning, limitations and evaluation

Useful for a same-hour yield expectation and anomaly-review baseline. It is not a weather forecast, module-temperature law, or demonstrated maintenance benefit. Location transfer is assessed at one reserved city. No fitted pathway is automatically causal. Finite basis clocks and correlated predictors limit identification; fold coefficients, rank/conditioning, residuals, sensitivities and unsuccessful hypotheses remain available in research_history. Future agents may submit different valid equations; exact formula matching is not required. Predictions, physical-unit errors, group effects, coverage and uncertainty are scored separately from a hash-bound scientific review.

Run the reference with `python run.py`. Create a runnable submission with `python evaluator/evaluate.py example --output NEW_DIRECTORY`, then score it with `score --submission SUBMISSION --output NEW_REPORT --replay`. The collection `_evaluation_25/` adds tolerance, tail-error, normalized-error, interval-score and risk/coverage diagnostics. All supplied targets are now exposed, so future scoring is retrospective and new confirmation requires fresh groups.

## Sources and prior analyses

Native source: https://data.mendeley.com/datasets/dbh93b6vp8/3. Source articles and known fitted relationships are disclosed in PRIOR_ART.json. Literature checking is targeted and non-exhaustive; model strength or a held-out numerical gain does not establish novelty. No private reference material enters this package.
