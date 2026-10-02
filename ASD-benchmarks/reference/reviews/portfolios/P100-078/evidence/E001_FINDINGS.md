# P100-078: Limits of multicenter control-growth inference

> Local scientific reference, 1 October 2026. Exploratory reproduction; no fresh confirmation. No independently established new physical law or measured deployment benefit is claimed.

## Scenario and experimental inputs

Untreated, author-valid, numeric-equality log-CFU lung observations with numeric actual times within twenty-four hours. Time-zero cohort averages are allowed calibration. Censored early-death records are not silently converted to scheduled endpoints. Three laboratories with recurring bacterial strains; two development sites and one exposed reserved site. This is retrospective laboratory transfer, not new-strain generalization or independent confirmation. Unresolved source strain labels remain anchors, not split identities.

The numerical target is **Untreated bacterial burden in total lung**, in **log10 CFU / total lung**. Initial cohort burden and time/site only. No post-baseline measured target is an input; study/strain IDs are anchors, not predictors. All source bytes remain unchanged. Prepared analysis rows retain workbook, archive/member or signal-array anchors.

## Finding and executable equation

A capacity-gap control-growth approximation is executable, but its laboratory transfer is retrospective. Strain labels and one native SITE field are inconsistent; whole source-laboratory directories replace unreliable biological labels as validation groups. The invalidated grouping phase is preserved.

$$
\widehat{L}(t)=L_0+2.00717\frac{t}{24}+0.98077\frac{t}{24}(7-L_0).
$$

The equation above is the compact physical candidate; the numerical default and every competing hypothesis are separately scored. Exact reference scales, clipping, causal sample recursion and every coefficient are in rules.json and run.py.

Here L is the conventional log10 total-lung CFU burden (formally log10 of burden relative to one CFU per total lung), L0 is the permitted time-zero cohort mean, and t is numeric actual elapsed hours. The value 7 is a fixed log-CFU capacity reference, not a fitted clinical safety threshold. All later measured burdens are excluded from predictors.

| Coefficient or dimensionless basis term | Frozen value |
|---|---|
| 1: elapsed time/(24h) | 2.00717 |
| 2: capacity-gap growth: time * (7-initial burden) | 0.9807704 |

<!-- pagebreak -->

## Methods and reserved-cohort performance

Five main, substantively different ASD attempts and four follow-up structural controls were completed. Controls may revisit an earlier structure; they do not count as additional discoveries. Development uses whole-group folds (forward batch blocks for case 86). A mean predictor, established/simple domain relation and fixed kernel model with at most 64 centers receive identical permitted inputs. Coefficients and candidate selection were frozen before the separate scoring process. The default was chosen from development evidence; it is never replaced by a final-test winner.

There are **1 reserved groups**, **15 eligible observations** and **15 assigned input rows**. Primary metric: **mae**, with equal-group weighting, in **log10 CFU / total lung**. Physical-unit MAE is also reported. Calibration rows and missing targets are not manufactured into successful predictions.

| Frozen model | Primary error | Group mean MAE |
|---|---|---|
| reference | 0.515603 | 0.515603 |
| mechanistic reference | 0.515603 | 0.515603 |
| mean | 0.586658 | 0.586658 |
| domain | 0.672927 | 0.672927 |
| rbf | 0.527731 | 0.527731 |

MAE units: **log10 CFU / total lung**. Lower is better; these are errors, not classification accuracy percentages. Row count does not imply independent experimental replication. No fresh confirmation is claimed: the invalidated source-label-grouped phase used part of the later laboratory cohort. Source selection/censoring prevents clinical or population conclusions.

## Meaning, limitations and evaluation

Useful as an evaluator and a source-quality/censoring lesson. The selected uncensored cohort does not establish survival safety, antibiotic efficacy or general virulence. Only fifteen GSK observations remain eligible under the fixed censoring rule. No fitted pathway is automatically causal. Finite basis clocks and correlated predictors limit identification; fold coefficients, rank/conditioning, residuals, sensitivities and unsuccessful hypotheses remain available in research_history. Future agents may submit different valid equations; exact formula matching is not required. Predictions, physical-unit errors, group effects, coverage and uncertainty are scored separately from a hash-bound scientific review.

Run the reference with `python run.py`. Create a runnable submission with `python evaluator/evaluate.py example --output NEW_DIRECTORY`, then score it with `score --submission SUBMISSION --output NEW_REPORT --replay`. The collection `_evaluation_25/` adds tolerance, tail-error, normalized-error, interval-score and risk/coverage diagnostics. All supplied targets are now exposed, so future scoring is retrospective and new confirmation requires fresh groups.

## Sources and prior analyses

Native source: https://zenodo.org/records/15124940. Source articles and known fitted relationships are disclosed in PRIOR_ART.json. Literature checking is targeted and non-exhaustive; model strength or a held-out numerical gain does not establish novelty. No private reference material enters this package.
