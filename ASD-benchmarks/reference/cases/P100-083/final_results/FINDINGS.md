# P100-083: Hive Monitoring (Apis mellifera and Stingless Bees) and Rainfall Data - Federal University of Ceará (UFC) Apiary - Brazil

> Principia-100 | Standardized portfolio | 1 October 2026

## Scenario and evaluation contract

Domain: Animal ecology. The current default task predicts One-hour future internal sensor temperature in degC. Independent unit: future native-date block per calibrated sensor stream. Its packaged cohort contains 1,282 assigned rows in 5 groups.

**All supplied outcomes are now exposed.** Historical reserved evaluations remain part of the evidence record; future scores are retrospective. No newly established fundamental law or measured deployment impact is admitted by this packaging.

## Current portfolio findings

**Unsupported or falsified:** A physically signed passive-temperature competitor is falsified as the strongest forecast.

Limit: Development RMSE.19148704 C vs .16096145 C flexible; evaporation coefficient reaches zero, and ambient-level ablation improves the model. Conductance and behavioral heat regulation remain unidentifiable.

**Unsupported or falsified:** Weather-increment forecasting remains weaker than the flexible control; physical sign constraints are informative falsifiers.

Limit: Only 2/15 blocks improve. A known ARX forecast is not an identified heat-balance or colony-health rule.

## Versioned tasks

| Task family | Target and information | Source scope |
|---|---|---|
| original | One-hour future internal sensor temperature (degC) | original corpus |
| round2 | One-hour future internal sensor temperature (degree C) | original corpus |

Different targets, calibration budgets and cohorts have different task IDs. Their raw error values cannot be pooled into a scenario ranking. Exact equations, coefficients, permitted variables, timing, groups and per-model results are bound in the task packages.

Evaluation: the shared CLI provides numerical scoring, explicit coverage and abstention, uncertainty and event diagnostics. Agent review separately assesses scientific support; no aggregate discovery score is produced.

<!-- pagebreak -->

## Detailed reference note: Hive microclimate: a scoped ASD reference
> Principia-100 | Case 83 | Interpretable thermal comparisons; strongest-comparator superiority fails

## 1. Scenario and measured quantities

Zenodo 20399470, Federal University of Ceará apiary. Apis: Dec 2024-Mar 2025; Meliponini: Sep 2025-Mar 2026; releaseMay 2026. The pilot target is **One-hour future internal sensor temperature** in **degC**, with 5531 development and 1282 reserved prepared observations. Source bytes remain unchanged; prepared target/predictor transformations are labeled analysis products.

## 2. Experimental design

The latest 20 percent native dates per stream are reserved; development uses forward temporal blocks. Each input comes from an hourly native origin, with a one-hour target matched within five minutes on the same day. No interpolation or future rainfall is used. 10 substantive attempts tested competing physical or process explanations. Baseline reproduction is excluded from that count. All scales, coefficients and tuning are trained inside applicable development folds. Direct and residual Gaussian-kernel comparators share the same available information. Candidate selection and stopping were frozen before the separate final scoring process; no final-score-driven revision occurred.

## 3. Executable equation and interpretation

$$
v=0.6108e^{17.27T_e/(T_e+237.3)}(1-H_e/100)
$$

$$
\widehat T_{+1}=T+c_s+b_a(T_e-T)+b_r(30-T)+b_m(T-T_{-1})+b_vv+b_{vr}v(30-T)
$$

T and Te are current internal/external Celsius temperatures; T(-1) is a causal one-hour lag, He is current external relative humidity percent, and v is external vapor-pressure deficit in kPa. Five offsets c_s are−0.384543, −0.316614, −0.340834, +0.138741, +0.323654 degC in rules.json sensor order. Coefficients ba=−0.002878, br=0.050874, bm=0.083403 are dimensionless; bv=0.481876 degC/kPa and bvr=0.084243/kPa. The reference 30 degC is an algebraic centering constant, not a prescribed biological setpoint.

<!-- pagebreak -->

## 4. Findings, accuracy and counterexamples

| Frozen model | Final RMSE (degC) |
|---|---:|
| reference | 0.204548 |
| challenger | 0.203768 |
| baseline_newton | 0.328411 |
| baseline_persistence | 0.215706 |
| baseline_rbf | 0.985854 |
| baseline_residual_rbf | 0.202103 |

Reference mean-stream RMSE is 0.204548 degC; persistence 0.215706, residual-kernel 0.202103. It improves four streams against persistence but worsens the second Apis stream 0.151843 versus 0.139689. The ambient-gradient coefficient is slightly negative, so an identified passive heat conductance is not supported. The VPD interaction can be algebraically read as a dry-response attraction near 35.72 degC, but this is a conditional coefficient combination, not a measured brood setpoint. Superiority over the strongest comparator fails.

## 5. Applicability, practical value and limits

Latest native dates at five calibrated sensor streams from one apiary; sensor/colony, species and season are confounded. No unseen-apiary or colony-health prediction. The equation and preserved falsifications provide an auditable test of whether an ASD agent can produce a useful conditional numerical relationship. They do not establish industrial savings, causal mechanism or universal transfer. The source-aware corpus contains known physics and previously analyzed observations; no previously unknown physical law is admitted. Individual group errors are reported, without row-level confidence intervals that treat repeated samples as independent.

## 6. Reproduction and scientific status

run.py checks package hashes and reproduces all predictions/metrics without fitting. rules.json contains full precision coefficients and calibration. The evaluator accepts alternative equations and abstention, scores common rows fairly and keeps scientific review separate from numerical scoring. All targets are now exposed. Fresh confirmation of a later method requires new reserved experimental groups. Computational review is a separate checking phase by the same operator, not independent experimental replication or human adjudication.

Source: [Authoritative release](https://zenodo.org/records/20399470); [Stabentheiner et al.(2010), honeybee colony thermoregulation](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0008967). Evidence: `evidence/metrics.csv`, `by_group.csv`, `sample_anchors.csv.gz` and the source/units audit. Rejected hypotheses remain in research history.
