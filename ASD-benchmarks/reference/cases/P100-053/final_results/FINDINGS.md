# P100-053: Industrial screw driving dataset collection: Time series data for process monitoring and anomaly detection

> Principia-100 | Standardized portfolio | 1 October 2026

## Scenario and evaluation contract

Domain: Industrial manufacturing. The current default task predicts Angle-mean thread-forming torque, 700–1300 degrees in Nm. Independent unit: workpiece (both locations and every reuse cycle). Its packaged cohort contains 2,473 assigned rows in 50 groups.

**All supplied outcomes are now exposed.** Historical reserved evaluations remain part of the evidence record; future scores are retrospective. No newly established fundamental law or measured deployment impact is admitted by this packaging.

## Current portfolio findings

**Numerical control:** A six-coefficient engagement-history update compresses the original branches at a measured accuracy cost.

Limit: Its development MAE.0244117 Nm exceeds equally informed flexible accuracy; disturbance-reset .0244366 Nm adds no gain. Simplicity can be useful but is distinct from a new friction mechanism.

**Unsupported or falsified:** Multiplicative wear transfer fails against the additive/flexible history control; it is retained as a negative physical proposal.

Limit: Only 15/200 workpieces improve. Surface class, controller OK/NOK, clamping force and joint strength cannot be substituted for measured targets.

## Versioned tasks

| Task family | Target and information | Source scope |
|---|---|---|
| original | Angle-mean thread-forming torque, 700–1300 degrees (Nm) | original corpus |
| round2 | Angle-mean thread-forming torque, 700–1300 degrees (Nm) | original corpus |

Different targets, calibration budgets and cohorts have different task IDs. Their raw error values cannot be pooled into a scenario ranking. Exact equations, coefficients, permitted variables, timing, groups and per-model results are bound in the task packages.

Evaluation: the shared CLI provides numerical scoring, explicit coverage and abstention, uncertainty and event diagnostics. Agent review separately assesses scientific support; no aggregate discovery score is produced.

<!-- pagebreak -->

## Detailed reference note: Early prediction of screw-forming torque
> P100-053 | Scenario and findings | September 2026 reference results

The practical question is whether early torque measurements and completed reuse history can predict later thread-forming resistance. They provide useful predictive information within this station, but the proposed physical memory equation does not outperform the strongest matched comparators.

## 1. Scenario and available measurements

The selected surface-friction experiment from the TU Dortmund/RIF screw-driving collection contains 12,500 operations on 250 workpieces, spanning eight surface conditions. Each workpiece contributes two screw locations and repeated use cycles. Native JSON traces record torque, angle and process phases; labels and documentation describe the experimental conditions. Surface-class labels are reserved for grouping and evaluation, not supplied as predictors.

The response is angle-mean measured torque between 700 and 1,300 degrees of the thread-forming phase, in N m. It is not final tightening torque, joint strength, clamping force or the controller's OK/NOK decision. Those distinctions prevent controller settings from being mistaken for discovered material laws.

## 2. Experimental method

A fixed metadata-based allocation reserved 50 complete workpieces, stratified by surface condition; the other 200 supported development. Both holes and every reuse cycle stayed in the same partition. Ten substantive attempts investigated early friction, wear, history, location and virgin-thread behavior using grouped development validation. The selected A9 equation and matched baselines were frozen before confirmation.

Current predictors stop at the first sampled crossing of 250 degrees, including the native sampling overshoot, and may use the completed Finding phase. Prior torque responses enter only after the preceding same-hole operation has finished. The reserved set contains 2,473 eligible operations from 2,500 assigned operations. The 27 unavailable target windows remain documented and are not extrapolated.

## 3. Tested history equation

For an operation with completed same-hole history, the selected model updates the previous late torque:

$$
\widehat T_n=T_{\mathrm{prev}}+\boldsymbol{\beta}^{\mathsf{T}}\boldsymbol{x}_n.
$$

$$
\boldsymbol{x}_n=(1,\Delta E,\Delta G,q,\Delta E q,T_{\mathrm{prev}}-E_{\mathrm{prev}},L,|\Delta E|a)^{\mathsf{T}}.
$$

Here *E* is early mean torque, *G* an early torque-contrast feature (both N m), and Δ denotes the difference from the most recent eligible completed same-hole operation, labeled prev. *L* is the known left-location indicator. For reuse count *n*, the bounded features are:

$$
q=(1+n)^{-1},\qquad r=\dfrac{|\Delta E|}{|E_{\mathrm{prev}}|+0.05\,\mathrm{N\,m}},\qquad a=\dfrac{r}{1+r}.
$$

The terms represent persistence, early-response changes, conditioning with reuse and bounded disturbance magnitude. The coefficient units follow the corresponding features so that each contribution is torque. Separate frozen linear branches handle missing history and virgin workpieces; the virgin branch takes precedence at reuse count zero. All branch formulas and coefficients are explicit in `run.py` and `rules.json`.

<!-- pagebreak -->

## 4. Findings and predictive performance

**The history-based candidate predicts later torque, but its advantage over a simple matched model is small.** A9 attains 0.023164 N m mean workpiece MAE. Its 2.60% improvement over the original linear comparator misses the campaign's frozen 5% practical threshold.

| Frozen model | Mean workpiece MAE (N m) |
|---|---|
| A9 memory equation, selected before confirmation | 0.023164 |
| Matched ordinary linear comparator | 0.023783 |
| Matched robust linear comparator | 0.022803 |
| Frozen tree-ensemble comparator | 0.022296 |

The primary measure averages absolute error within each workpiece and then weights workpieces equally:

$$
E_{\mathrm{MAE}}=\dfrac{1}{50}\sum_{g=1}^{50}\dfrac{1}{n_g}\sum_{i=1}^{n_g}|\widehat T_{gi}-T_{gi}|.
$$

**The stronger comparators falsify the claimed predictive superiority of the proposed memory structure.** A9's error is 1.58% higher than the robust linear model and 3.89% higher than the tree ensemble. These models use matched prediction-time information, including permitted prior history. The comparison therefore does not isolate the benefit of history alone; it tests how that information is represented.

## 5. Interpretation, practical value and limits

A state-update interpretation is plausible: previously formed threads retain information about contact resistance, while changes in the current prefix indicate altered engagement. The data nevertheless do not separately identify friction, geometry, material wear and station effects. A well-fitting reuse term is not direct evidence for a universal wear mechanism. The tree model remains a predictive comparator, not a physical law.

The case is useful for evaluating whether an agent can turn early measurements into a reproducible late-torque estimate without future information or controller-label leakage. The observed error levels provide a concrete starting point for process-monitoring studies. Production alarm thresholds, scrap reduction, joint reliability and closed-loop control benefits were not measured, so none is claimed.

Validation covers this station and these surface conditions. The 27 unavailable target windows bound the eligible population. Uncertainty can be assessed by resampling whole workpieces within surface strata; resampling individual operations would ignore shared workpiece history. Any tolerance claim must additionally address sensor uncertainty and the intended process requirement.

## 6. Evidence and use

Reproduction: `python run.py` replays all four frozen predictors. Full-precision branch coefficients and the exported tree parameters are in `rules.json`. `data/eligibility.csv` records all assigned operations; `evidence/` retains the predictions and workpiece-level errors.

Evaluation: `evaluator/README.md` specifies the common submission interface, grouped metric, matched baselines, abstentions and scientific review. Exact agreement with A9 is not required of another valid discovery.

Status: A9 is not admitted as a new physical reuse law. The negative comparison remains valuable reference evidence. All confirmation targets are exposed; new physical claims require fresh experimental groups and independent scientific assessment.

Source: West and Deuse, [Industrial screw-driving dataset collection](https://zenodo.org/records/16031381), DOI 10.5281/zenodo.16031381, surface-friction subset. The source provides raw traces; the torque target and causal features described here are pilot analysis products.
