# P100-072: dataset of the data obtained for publication: Saccharomyces cerevisiae wine strains show a wide range of competitive abilities and differential nutrient uptake behavior in co-culture with S. kudriavzevii

> Principia-100 | Standardized portfolio | 1 October 2026

## Scenario and evaluation contract

Domain: Food microbiology. The current default task predicts Later author qPCR S.kudriavzevii percentage in percentage points. Independent unit: whole co-cultured strain including every replicate/time. Its packaged cohort contains 18 assigned rows in 2 groups.

**All supplied outcomes are now exposed.** Historical reserved evaluations remain part of the evidence record; future scores are retrospective. No newly established fundamental law or measured deployment impact is admitted by this packaging.

## Current portfolio findings

**Retrospective extension:** HPLC glucose+fructose forecasting creates a distinct measured endpoint from the original qPCR competition percentage.

Limit: Separate-pool development MAE 14.656974 g/L vs 17.782176 flexible; fitted Monod-like K=200 g/L hits upper search bound. An upper-bound parameter is not an identified uptake constant; the later two-clock model simplifies it.

**Retrospective extension:** Separate early-assay clocks improve later HPLC residual-sugar prediction over the prior chemistry model and a matched flexible control.

Limit: Fiveof 6 strains improve; Ec 1118 worsens. Smaller 3 parameter error 13.370341 waswithin 1 %simplicity margin. Prefix agreement is imposed and is not validation.

## Versioned tasks

| Task family | Target and information | Source scope |
|---|---|---|
| original | Later author qPCR S.kudriavzevii percentage (percentage points) | original corpus |
| round2 | Residual glucose plus fructose (g/L) | original corpus |

Different targets, calibration budgets and cohorts have different task IDs. Their raw error values cannot be pooled into a scenario ranking. Exact equations, coefficients, permitted variables, timing, groups and per-model results are bound in the task packages.

Evaluation: the shared CLI provides numerical scoring, explicit coverage and abstention, uncertainty and event diagnostics. Agent review separately assesses scientific support; no aggregate discovery score is produced.

<!-- pagebreak -->

## Detailed reference note: Yeast competition: a scoped ASD reference
> Principia-100 | Case 72 | Provisional retrospective competition predictor; independent confirmation required

## 1. Scenario and measured quantities

Zenodo 18757697, IATA-CSIC competition with S.kudriavzevii CR85; linked study doi 10.1016/j.fm.2023.104276. Native qPCR exports 2020; workbook analytical sections 2021/2022; public deposit 2026. The pilot target is **Later author qPCR S.kudriavzevii percentage** in **percentage points**, with 43 development and 18 reserved prepared observations. Source bytes remain unchanged; prepared target/predictor transformations are labeled analysis products.

## 2. Experimental design

Six strain groups develop the model and two metadata-hashed strains are reserved. All biological replicates and times stay together. Only own 22/72 h percentages predict later times. Ambiguous 500/504 h rows and missing-prefix replicates are explicitly excluded. 6 substantive attempts tested competing physical or process explanations. Baseline reproduction is excluded from that count. All scales, coefficients and tuning are trained inside applicable development folds. Direct and residual Gaussian-kernel comparators share the same available information. Candidate selection and stopping were frozen before the separate final scoring process; no final-score-driven revision occurred.

## 3. Executable equation and interpretation

$$
s=\dfrac{\operatorname{logit}(p_{72})-\operatorname{logit}(p_{22})}{50}
$$

$$
\operatorname{logit}(\widehat p)=\operatorname{logit}(p_{72})-0.077454s\Delta-0.101446\dfrac{\Delta^2}{75(\Delta+75)}
$$

p22 and p72 are own-replicate fractions (source percentages/100). Delta = t - 72 h, and s is early log-odds change per hour. Fractions are clipped to0.0001-0.9999 only for log-odds calculation; original targets are unchanged. The output is 100 times logistic(log-odds), in percentage points.75 h is a development-selected shape scale. This early/late conditional equation does not estimate an independently measured fitness coefficient.

<!-- pagebreak -->

## 4. Findings, accuracy and counterexamples

| Frozen model | Final MAE (percentage points) |
|---|---:|
| reference | 6.438128 |
| challenger | 6.939264 |
| baseline_constant_selection | 28.890654 |
| baseline_persistence | 7.373589 |
| baseline_rbf | 9.582172 |
| baseline_residual_rbf | 10.097963 |

Reference MAE is 6.438128 percentage points versus persistence 7.373589. T73 improves 5.278519 versus 7.158378, while D245 slightly worsens 7.597738 versus 7.588800. The fitted early-rate coefficient is negative, challenging literal continuation of early competitive advantage. Neither nitrogen limitation nor a selection-reversal mechanism is identified. Schema exposure and two groups prevent a fresh discovery-admission claim.

## 5. Applicability, practical value and limits

Two reserved yeast strain labels, eighteen later author-derived qPCR percentages, same experiment campaign with audit-exposed targets; no blind validation or nutrient mechanism identification. The equation and preserved falsifications provide an auditable test of whether an ASD agent can produce a useful conditional numerical relationship. They do not establish industrial savings, causal mechanism or universal transfer. The source-aware corpus contains known physics and previously analyzed observations; no previously unknown physical law is admitted. Individual group errors are reported, without row-level confidence intervals that treat repeated samples as independent.

## 6. Reproduction and scientific status

run.py checks package hashes and reproduces all predictions/metrics without fitting. rules.json contains full precision coefficients and calibration. The evaluator accepts alternative equations and abstention, scores common rows fairly and keeps scientific review separate from numerical scoring. All targets are now exposed. The yeast schema audit also exposed some later percentages before model construction; these scores are explicitly retrospective. Computational review is a separate checking phase by the same operator, not independent experimental replication or human adjudication.

Source: [Authoritative release](https://zenodo.org/records/18757697); [Source competition study (2023)](https://pubmed.ncbi.nlm.nih.gov/37290881/). Evidence: `evidence/metrics.csv`, `by_group.csv`, `sample_anchors.csv.gz` and the source/units audit. Rejected hypotheses remain in research history.
