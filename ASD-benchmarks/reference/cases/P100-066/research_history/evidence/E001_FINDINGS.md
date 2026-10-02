# P100-066: Excess hydrogen uptake in MOF–graphite hybrids

> Local scientific reference, 1 October 2026. Scoped excess-uptake approximation. No independently established new physical law or measured deployment benefit is claimed.

## Scenario and experimental inputs

Adsorption/desorption branches at 77, 160 and 273 K for four graphite compositions. Excess uptake is the measured response; total-uptake and reuse-cycle derivatives are not independent confirmation of it. Four MOF/graphite compositions and one source campaign. A branch contrast has different sampled pressures and cannot by itself establish irreversible hysteresis.

The numerical target is **Excess hydrogen uptake**, in **wt.%**. Composition, pressure, temperature, branch only; no measured uptake-derived quantity as an input. All source bytes remain unchanged. Prepared analysis rows retain workbook, archive/member or signal-array anchors.

## Finding and executable equation

Adding gas-displacement curvature improves excess-uptake prediction over a monotone Langmuir comparator. Graphite-dilution, branch and heterogeneous-occupancy additions do not improve development evidence reliably. The compact equation does not establish correct optimal-storage pressures.

$$
\widehat{q}_{\rm ex}=A\frac{b(T)P}{1+b(T)P}-D\frac{P}{100},\qquad b(T)=0.03\exp\!\left[600\left(\frac{1}{T}-\frac{1}{160}\right)\right].
$$

The equation above is the compact physical candidate; the numerical default and every competing hypothesis are separately scored. Exact reference scales, clipping, causal sample recursion and every coefficient are in rules.json and run.py.

Here qex, A and D are in wt.%; P is the numerical pressure in bar, b is in inverse bar, T is in K and the effective affinity-temperature scale is 600 K. Pressure division is by 100 bar. This scale is not an independently measured adsorption enthalpy; cryogenic gas nonideality and site heterogeneity remain unresolved.

| Coefficient or dimensionless basis term | Frozen value |
|---|---|
| 1: Langmuir b(T)P/(1+b(T)P) | 4.306425 |
| 2: negative gas displacement P/(100bar) | 1.108106 |

<!-- pagebreak -->

## Methods and reserved-cohort performance

Five main, substantively different ASD attempts and four follow-up structural controls were completed. Controls may revisit an earlier structure; they do not count as additional discoveries. Development uses whole-group folds (forward batch blocks for case 86). A mean predictor, established/simple domain relation and fixed kernel model with at most 64 centers receive identical permitted inputs. Coefficients and candidate selection were frozen before the separate scoring process. The default was chosen from development evidence; it is never replaced by a final-test winner.

There are **1 reserved groups**, **58 eligible observations** and **58 assigned input rows**. Primary metric: **mae**, with equal-group weighting, in **wt.%**. Physical-unit MAE is also reported. Calibration rows and missing targets are not manufactured into successful predictions.

| Frozen model | Primary error | Group mean MAE |
|---|---|---|
| reference | 0.546458 | 0.546458 |
| mechanistic reference | 0.546458 | 0.546458 |
| mean | 1.49195 | 1.49195 |
| domain | 0.639155 | 0.639155 |
| rbf | 0.646811 | 0.646811 |

MAE units: **wt.%**. Lower is better; these are errors, not classification accuracy percentages. Row count does not imply independent experimental replication. The unfitted stationary-pressure check in evidence/peak_pressure_falsifier.json exposes disagreement with sampled uptake maxima; no optimal-pressure rule is admitted.

## Meaning, limitations and evaluation

Useful as a falsifiable excess-versus-absolute adsorption distinction. Source publications already report hybrid enhancements. Affinity and displacement parameters are effective and partly confounded; cryogenic high-pressure nonideality is unresolved. No fitted pathway is automatically causal. Finite basis clocks and correlated predictors limit identification; fold coefficients, rank/conditioning, residuals, sensitivities and unsuccessful hypotheses remain available in research_history. Future agents may submit different valid equations; exact formula matching is not required. Predictions, physical-unit errors, group effects, coverage and uncertainty are scored separately from a hash-bound scientific review.

Run the reference with `python run.py`. Create a runnable submission with `python evaluator/evaluate.py example --output NEW_DIRECTORY`, then score it with `score --submission SUBMISSION --output NEW_REPORT --replay`. The collection `_evaluation_25/` adds tolerance, tail-error, normalized-error, interval-score and risk/coverage diagnostics. All supplied targets are now exposed, so future scoring is retrospective and new confirmation requires fresh groups.

## Sources and prior analyses

Native source: https://doi.org/10.57745/KR8BIW. Source articles and known fitted relationships are disclosed in PRIOR_ART.json. Literature checking is targeted and non-exhaustive; model strength or a held-out numerical gain does not establish novelty. No private reference material enters this package.
