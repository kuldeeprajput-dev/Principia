# P100-057: Rheological Data For Syntactic Foam

> Principia-100 | Standardized portfolio | 1 October 2026

## Scenario and evaluation contract

Domain: Suspension rheology. The current default task predicts Native dynamic viscosity in cP. Independent unit: whole Test ID; synthesis lots not identified. Its packaged cohort contains 2,500 assigned rows in 10 groups.

**All supplied outcomes are now exposed.** Historical reserved evaluations remain part of the evidence record; future scores are retrospective. No newly established fundamental law or measured deployment impact is admitted by this packaging.

## Current portfolio findings

**Numerical control:** A causal previous-temperature viscosity track is a distinct history-calibrated task, not a gain on the original static input budget.

Limit: The thermal history rule improves only about .26%; four activation coefficients hit zero and 190 negative/64 verylarge outcomes remain. Known-formulation repeat tests do not identify equilibrium rheology.

**Unsupported or falsified:** Causal shear-rate transport is not a supported improvement over the history-aware control.

Limit: Four activation estimates hit zero; 190 negative outcomes and 64 values ≥ 100000 cP in the earlier history task make equilibrium constitutive interpretation doubtful. Static vs history errors are not an algorithm-only comparison.

## Versioned tasks

| Task family | Target and information | Source scope |
|---|---|---|
| original | Native dynamic viscosity (cP) | original corpus |
| round2 | Next-temperature-block viscosity (cP) | original corpus |

Different targets, calibration budgets and cohorts have different task IDs. Their raw error values cannot be pooled into a scenario ranking. Exact equations, coefficients, permitted variables, timing, groups and per-model results are bound in the task packages.

Evaluation: the shared CLI provides numerical scoring, explicit coverage and abstention, uncertainty and event diagnostics. Agent review separately assesses scientific support; no aggregate discovery score is produced.

<!-- pagebreak -->

## Detailed reference note: Syntactic-foam rheology: a scoped ASD reference
> Principia-100 | Case 57 | Reproduction and negative constitutive evidence; no admitted extension

## 1. Scenario and measured quantities

Zenodo 19699588, NYU Anton Paar RheoCompass exports. Native metadata 2024-2025; release 2026-04-22. The pilot target is **Native dynamic viscosity** in **cP**, with 10000 development and 2500 reserved prepared observations. Source bytes remain unchanged; prepared target/predictor transformations are labeled analysis products.

## 2. Experimental design

Four complete tests per formulation develop the models; one test per formulation is reserved by metadata hashing. Every temperature/shear point in a test stays together. 6 substantive attempts tested competing physical or process explanations. Baseline reproduction is excluded from that count. All scales, coefficients and tuning are trained inside applicable development folds. Direct and residual Gaussian-kernel comparators share the same available information. Candidate selection and stopping were frozen before the separate final scoring process; no final-score-driven revision occurred.

## 3. Executable equation and interpretation

$$
\widehat{\eta}_f=a_f\exp[9(1000/T_K-1000/333.15)]
$$

T_K is absolute temperature in kelvin; eta is cP. The factor 1000 carries kelvin, so 9 is dimensionless and represents an effective activation scale 9000 K. Formulation amplitudes a_f range 52.1603-218.5126 cP at 333.15 K; all ten exact values are in rules.json. A shear-rate input is allowed for competitors, but the selected thermal reference does not use it.

<!-- pagebreak -->

## 4. Findings, accuracy and counterexamples

| Frozen model | Final MAE (cP) |
|---|---:|
| reference | 3291.165871 |
| challenger | 3288.612122 |
| baseline_mean | 5961.384618 |
| baseline_rbf | 4575.906906 |
| baseline_residual_rbf | 4576.250618 |

The Arrhenius reference was selected before confirmation for simplicity. The yield/shear challenger changes final MAE by only 0.078 percent despite extra parameters. Test errors range 43.9-15958 cP: formulation-specific amplitudes and a common activation do not explain all high-viscosity structure. Repeated curves are very similar but not exact duplicates; fifty target vectors differ. Heating order and aging remain confounded. No microscopic yield mechanism or universal filler law is admitted.

## 5. Applicability, practical value and limits

Repeated tests of ten already calibrated formulations in one rheometer dataset; no independent synthesis-lot or unseen-loading transfer. The equation and preserved falsifications provide an auditable test of whether an ASD agent can produce a useful conditional numerical relationship. They do not establish industrial savings, causal mechanism or universal transfer. The source-aware corpus contains known physics and previously analyzed observations; no previously unknown physical law is admitted. Individual group errors are reported, without row-level confidence intervals that treat repeated samples as independent.

## 6. Reproduction and scientific status

run.py checks package hashes and reproduces all predictions/metrics without fitting. rules.json contains full precision coefficients and calibration. The evaluator accepts alternative equations and abstention, scores common rows fairly and keeps scientific review separate from numerical scoring. All targets are now exposed. Fresh confirmation of a later method requires new reserved experimental groups. Computational review is a separate checking phase by the same operator, not independent experimental replication or human adjudication.

Source: [Authoritative release](https://zenodo.org/records/19699588); [Carreau(1972), molecular-network rheology](https://doi.org/10.1122/1.549276); [Cross(1965), rational shear relaxation](https://doi.org/10.1016/0095-8522%2865%2990022-X). Evidence: `evidence/metrics.csv`, `by_group.csv`, `sample_anchors.csv.gz` and the source/units audit. Rejected hypotheses remain in research history.
