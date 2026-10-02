# P100-055: CARBCOMN - Dataset of Early Research Outcomes - Mix Design of 3D-printable Mixes Based on Industrial Slags

> Principia-100 | Standardized portfolio | 1 October 2026

## Scenario and evaluation contract

Domain: Construction materials. The current default task predicts Individual penetration normal force in N. Independent unit: whole mixture across both ages and replicates. Its packaged cohort contains 4,800 assigned rows in 2 groups.

**All supplied outcomes are now exposed.** Historical reserved evaluations remain part of the evidence record; future scores are retrospective. No newly established fundamental law or measured deployment impact is admitted by this packaging.

## Current portfolio findings

**Numerical control:** The uncalibrated original task supports a flexible force reference and physical-law abstention.

Limit: Native 1–600 penetration index lacks documented sampling interval and enough probe geometry; force cannot identify intrinsic yield stress.

**Numerical control:** A single proportional aging gain wins development selection; six plausible material extensions do not improve it.

Limit: Gain errors .203735/.068910 N are uneven; diagnostic-better models are not promoted. Water/aggregate/additive covariation and independent specimens across ages prevent a causal aging or paired-specimen mechanism.

## Versioned tasks

| Task family | Target and information | Source scope |
|---|---|---|
| original | Individual penetration normal force (N) | original corpus |
| continuation | Individual penetration normal force at mixing age30min (N) | original corpus |

Different targets, calibration budgets and cohorts have different task IDs. Their raw error values cannot be pooled into a scenario ranking. Exact equations, coefficients, permitted variables, timing, groups and per-model results are bound in the task packages.

Evaluation: the shared CLI provides numerical scoring, explicit coverage and abstention, uncertainty and event diagnostics. Agent review separately assesses scientific support; no aggregate discovery score is produced.

<!-- pagebreak -->

## Detailed reference note: P100-055: Penetration resistance of printable slag mixtures

> Local scientific reference, 1 October 2026. Physical-law abstention; flexible numerical reference. No independently established new physical law or measured deployment benefit is claimed.

## Scenario and experimental inputs

Nine source mix labels, two batches per mixture/age and tests at zero and thirty minutes after mixing. Individual normal-force columns are used; author-average and derived-yield-stress columns are excluded. Nine mix labels, two batches per mixture/age according to the source PDF, one early research campaign. Force–penetration-time relationships cannot identify intrinsic constitutive stress without probe kinematics/geometry.

The numerical target is **Individual penetration normal force**, in **N**. Known mix label, age and elapsed penetration index only; force is never an input. All source bytes remain unchanged. Prepared analysis rows retain workbook, archive/member or signal-array anchors.

## Finding and executable equation

The best simple physical candidate loses to the fixed flexible comparator on the reserved mixtures. Its reduced water/aging response does not establish a transferable constitutive law; aggregate/aging curvature proposals are preserved as unsuccessful tests.

$$
\widehat{F}=c_0+c_1\frac{\theta}{w}+c_2\frac{a\theta}{w},\qquad\theta=t_{\rm native}/100,\quad w=w_{\rm label}/0.30,\quad a=t_{\rm age}/30.
$$

The equation above is the compact physical candidate; the numerical default and every competing hypothesis are separately scored. For case 55, the stronger numerical default is a frozen Gaussian-kernel predictor, not an admitted physical law. Exact reference scales, clipping, causal sample recursion and every coefficient are in rules.json and run.py.

Here F is normal force in N, theta is the native penetration clock divided by 100 source-clock units, w is the water-ratio label divided by 0.30, and a is the known mixing age divided by 30 minutes. Coefficients are in N. The physical candidate is contrasted with the stronger fixed kernel default; neither constitutes an identified intrinsic yield-stress law.

| Coefficient or dimensionless basis term | Frozen value |
|---|---|
| 1: 1 | 0.3336024 |
| 2: clock/100 divided by water-ratio/0.30 | 0.01072374 |
| 3: age * clock / water | 0.05891234 |
| Flexible default | 64 fixed-center kernel coefficients; all values in rules.json |

<!-- pagebreak -->

## Methods and reserved-cohort performance

Five main, substantively different ASD attempts and four follow-up structural controls were completed. Controls may revisit an earlier structure; they do not count as additional discoveries. Development uses whole-group folds (forward batch blocks for case 86). A mean predictor, established/simple domain relation and fixed kernel model with at most 64 centers receive identical permitted inputs. Coefficients and candidate selection were frozen before the separate scoring process. The default was chosen from development evidence; it is never replaced by a final-test winner.

There are **2 reserved groups**, **4800 eligible observations** and **4800 assigned input rows**. Primary metric: **mae**, with equal-group weighting, in **N**. Physical-unit MAE is also reported. Calibration rows and missing targets are not manufactured into successful predictions.

| Frozen model | Primary error | Group mean MAE |
|---|---|---|
| reference | 0.150097 | 0.150097 |
| mechanistic reference | 0.211628 | 0.211628 |
| mean | 0.236713 | 0.236713 |
| domain | 0.21173 | 0.21173 |
| rbf | 0.150097 | 0.150097 |

MAE units: **N**. Lower is better; these are errors, not classification accuracy percentages. Row count does not imply independent experimental replication.

## Meaning, limitations and evaluation

Useful for screening what this native test can and cannot identify. The penetration-clock unit and mixture-label quantities are insufficiently documented for intrinsic material time constants or general printability thresholds. No fitted pathway is automatically causal. Finite basis clocks and correlated predictors limit identification; fold coefficients, rank/conditioning, residuals, sensitivities and unsuccessful hypotheses remain available in research_history. Future agents may submit different valid equations; exact formula matching is not required. Predictions, physical-unit errors, group effects, coverage and uncertainty are scored separately from a hash-bound scientific review.

Run the reference with `python run.py`. Create a runnable submission with `python evaluator/evaluate.py example --output NEW_DIRECTORY`, then score it with `score --submission SUBMISSION --output NEW_REPORT --trust-code`. The collection `evaluation/` adds tolerance, tail-error, normalized-error, interval-score and risk/coverage diagnostics. All supplied targets are now exposed, so future scoring is retrospective and new confirmation requires fresh groups.

## Sources and prior analyses

Native source: https://zenodo.org/records/17092152. Source articles and known fitted relationships are disclosed in PRIOR_ART.json. Literature checking is targeted and non-exhaustive; model strength or a held-out numerical gain does not establish novelty. No private reference material enters this package.
