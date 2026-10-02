# P100-058: A positive relaxation spectrum for PDLLA rheology

> Local scientific reference, 1 October 2026. Scoped constitutive approximation; known equation families. No independently established new physical law or measured deployment benefit is claimed.

## Scenario and experimental inputs

Nine native dynamic-frequency sweeps for one purchased polymer batch. Paired proprietary/text exports are linked duplicates. Storage modulus is the fitted response; loss modulus is withheld as a separate measured-response check. Temperature transfer within one material; no batch-to-batch or general polymer law claim. Positive modulus spans orders of magnitude.

The numerical target is **Storage modulus G prime**, in **Pa**. Temperature and imposed frequency only. Loss modulus is withheld as an orthogonal mechanistic check; never a primary predictor. All source bytes remain unchanged. Prepared analysis rows retain workbook, archive/member or signal-array anchors.

## Finding and executable equation

A positive generalized-Maxwell spectrum with a WLF temperature clock predicts reserved storage and loss responses. The loss-modulus cross-check uses the same frozen coefficients with no secondary fitting. A plateau is unnecessary; exact individual relaxation modes remain nonunique.

$$
G^{\prime}=\sum_jG_j\frac{q_j^2}{1+q_j^2},\qquad G^{\prime\prime}=\sum_jG_j\frac{q_j}{1+q_j^2},\quad q_j=\omega\tau_ja_T,\quad\log_{10}a_T=-\frac{8(T-60)}{70+(T-60)}.
$$

The equation above is the compact physical candidate; the numerical default and every competing hypothesis are separately scored. Exact reference scales, clipping, causal sample recursion and every coefficient are in rules.json and run.py.

Here G prime and G double-prime are storage/loss moduli in Pa; Gj are nonnegative effective mode stiffnesses in Pa, omega is imposed frequency in rad/s, tauj are fixed mode times in s, aT is a dimensionless temperature shift and T is the numerical Celsius temperature. Temperature differences are in K; the WLF constants are 8 (dimensionless) and 70 K at 60 degree C. The table identifies every retained tauj and Gj.

| Coefficient or dimensionless basis term | Frozen value |
|---|---|
| 1: Maxwell storage tau=1e-05s | 6.675384e+07 |
| 2: Maxwell storage tau=0.000177828s | 1.851323e+07 |
| 3: Maxwell storage tau=0.00316228s | 681872 |
| 4: Maxwell storage tau=0.0562341s | 58544.33 |
| 5: Maxwell storage tau=1s | 354.2067 |
| 6: Maxwell storage tau=17.7828s | 0.6691362 |
| 7: Maxwell storage tau=316.228s | 0 |
| 8: Maxwell storage tau=5623.41s | 1.293376 |

<!-- pagebreak -->

## Methods and reserved-cohort performance

Five main, substantively different ASD attempts and four follow-up structural controls were completed. Controls may revisit an earlier structure; they do not count as additional discoveries. Development uses whole-group folds (forward batch blocks for case 86). A mean predictor, established/simple domain relation and fixed kernel model with at most 64 centers receive identical permitted inputs. Coefficients and candidate selection were frozen before the separate scoring process. The default was chosen from development evidence; it is never replaced by a final-test winner.

There are **2 reserved groups**, **35 finite native observations (32 positive for log scoring)** and **35 assigned input rows**. Primary metric: **log_mae** on the 32 strictly positive readings, with equal-temperature weighting, in **dimensionless natural-log ratio**. Three negative native readings remain unchanged and contribute to all-row physical errors; they cannot validate a positive constitutive modulus. Physical-unit MAE is also reported. Calibration rows and missing targets are not manufactured into successful predictions.

| Frozen model | Primary error | Group mean MAE |
|---|---|---|
| reference | 0.404461 | 116.619 |
| mechanistic reference | 0.404461 | 116.619 |
| mean | 10.866 | 2.83526e+06 |
| domain | 1.53772 | 948.397 |
| rbf | 1.29345 | 712.468 |

MAE units: **Pa**. Lower is better; these are errors, not classification accuracy percentages. Row count does not imply independent experimental replication. The unfitted loss-modulus group mean absolute log error is **0.256751**, corresponding to a multiplicative error scale of **1.293**. This is a separate response from the same instrument, not independent experimental replication. Log eligibility was clarified during post-confirmation evaluator QA; the original calculation silently omitted undefined logs. No model or selection was revised.

## Meaning, limitations and evaluation

Useful for a compact frequency/temperature response of this batch, with a mechanistic cross-check. WLF and Maxwell physics are prior art. This is not a new universal polymer law; instrument compliance and batch transfer are unresolved. No fitted pathway is automatically causal. Finite basis clocks and correlated predictors limit identification; fold coefficients, rank/conditioning, residuals, sensitivities and unsuccessful hypotheses remain available in research_history. Future agents may submit different valid equations; exact formula matching is not required. Predictions, physical-unit errors, group effects, coverage and uncertainty are scored separately from a hash-bound scientific review.

Run the reference with `python run.py`. Create a runnable submission with `python evaluator/evaluate.py example --output NEW_DIRECTORY`, then score it with `score --submission SUBMISSION --output NEW_REPORT --replay`. The collection `_evaluation_25/` adds tolerance, tail-error, normalized-error, interval-score and risk/coverage diagnostics. All supplied targets are now exposed, so future scoring is retrospective and new confirmation requires fresh groups.

## Sources and prior analyses

Native source: https://zenodo.org/records/17294879. Source articles and known fitted relationships are disclosed in PRIOR_ART.json. Literature checking is targeted and non-exhaustive; model strength or a held-out numerical gain does not establish novelty. No private reference material enters this package.
