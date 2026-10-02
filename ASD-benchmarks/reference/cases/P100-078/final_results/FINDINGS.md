# P100-078: Data for study "A Multicenter Study to Standardize a Mouse Pneumonia Model with Pseudomonas aeruginosa and Klebsiella pneumoniae for Antibiotic Development"

> Principia-100 | Standardized portfolio | 1 October 2026

## Scenario and evaluation contract

Domain: Preclinical reproducibility. The current default task predicts Untreated bacterial burden in total lung in log10 CFU / total lung. Independent unit: whole laboratory/site, all strains and studies. Its packaged cohort contains 15 assigned rows in 1 groups.

**All supplied outcomes are now exposed.** Historical reserved evaluations remain part of the evidence record; future scores are retrospective. No newly established fundamental law or measured deployment impact is admitted by this packaging.

## Current portfolio findings

**Numerical control:** The capacity-gap model is a retrospective endpoint reference after invalidated strain grouping; it is not independent biological confirmation.

Limit: Previously invalidated grouping exposed part of the GSK cohort; source strain/SITE alias inconsistencies make directory-level labs the only defensible existing group.

**Measurement audit:** All 15 GSK endpoints at 24 h reduce the chosen equation to almost a constant; the cohort cannot validate growth kinetics or initial burden memory.

Limit: Twenty untreated < 24 h humane endpoint assays have mean 9.2970/range 8.9120–9.3979 log units and are excluded from exact-time prediction. This nonrandom selection cannot be repaired by assigning 24 h.

## Versioned tasks

| Task family | Target and information | Source scope |
|---|---|---|
| original | Untreated bacterial burden in total lung (log10 CFU / total lung) | original corpus |
| continuation | Untreated bacterial burden in total lung (log10 CFU / total lung) | original corpus |

Different targets, calibration budgets and cohorts have different task IDs. Their raw error values cannot be pooled into a scenario ranking. Exact equations, coefficients, permitted variables, timing, groups and per-model results are bound in the task packages.

Evaluation: the shared CLI provides numerical scoring, explicit coverage and abstention, uncertainty and event diagnostics. Agent review separately assesses scientific support; no aggregate discovery score is produced.

<!-- pagebreak -->

## Detailed reference note: What the multicenter assay data can—and cannot—identify

## Scenario and experiment

The COMBINE source contains 49 heterogeneous workbooks from PEI, SSI and GSK laboratories, with strain identifiers, treatment groups, bacterial lung burdens, time-zero calibration animals and humane endpoints. The retained task uses explicitly untreated, author-valid, numerical equality log10 CFU per total lung observations at numeric actual times within 0–24 hours. Different animals supply each strain-study's time-zero cohort calibration.

All PEI/SSI development observations are used in leave-entire-laboratory-out folds; 661 observations span two labs and 30 study workbooks. The historically exposed GSK diagnostic cohort contains 15 observations, all at 24 hours. Previously invalidated grouping exposed some GSK values. No fresh confirmation is claimed.

Seven tests challenge the old capacity-gap description with time-conditioned median, clock-only, initial-burden, burden-memory, quadratic-clock and calibration-attenuation explanations. Full-laboratory validation is difficult because PEI concentrates late observations while SSI includes many earlier times; two labs do not identify a general laboratory distribution.

## Executable result and the kinetic falsifier

The old capacity-gap model remains the development-selected default:

$$
\widehat{L}(t)=L_0+2.0071696\frac{t}{24\,\mathrm{h}}+0.9807704\frac{t}{24\,\mathrm{h}}(7-L_0).
$$

Here L is log10 lung burden relative to one CFU per total lung, L0 is the permitted mean time-zero calibration, and the numerical reference 7 is not a clinical threshold. Its development equal-lab MAE is **0.793217 log10 CFU/lung**; exposed GSK MAE is **0.515603**.

At 24 hours, the equation reduces to

$$
\widehat{L}(24)=8.8725627+0.01922956L_0.
$$

Consequently, the 15-row diagnostic is almost a constant endpoint prediction. It cannot confirm the equation's growth trajectory, a carrying-capacity mechanism or initial-burden memory. A pure clock control and a burden-memory control give diagnostic MAEs **0.446767** and **0.434331**, despite worse development selection scores. These exposed outcomes are preserved and do not promote those alternatives. No positive kinetic rule is admitted.

## Calibration and censoring audits

The source audit identifies 97 raw strain-study time-zero cohorts, with 4–10 animals each. Their median descriptive standard error is **0.064421 log10 CFU/lung**. Under the frozen equation,

$$
\frac{\partial\widehat{L}}{\partial L_0}=1-0.9807704\frac{t}{24\,\mathrm{h}}.
$$

At the endpoint, propagating that median calibration error gives only **0.001239 log10 units**. This conditional calculation ignores coefficient uncertainty, alias errors and inter-lab heterogeneity. It establishes that the equation nearly ignores its initial calibration at the scored endpoint; it does not independently validate capacity-limited growth.

Twenty raw untreated GSK assays have actual-time strings `<24`, with mean burden **9.2970** and range **8.9120–9.3979**. They are excluded from exact-time prediction because converting them to 24 hours would invent death times. Their high recorded burdens reinforce the need to distinguish humane-endpoint selection from a random missingness assumption. These values do not establish mortality probabilities or a joint survival model.

## Scientific disposition

The continuation strengthens the evaluator and identifies an endpoint-information boundary; it does not improve confirmed biological kinetics. The known source study already examines virulence and inter-laboratory reproducibility. No antibiotic-effect, clinical efficacy, survival-safety or universal carrying-capacity claim is made.

The new Zenodo record 22280001 has matching COMBINE-study metadata in the official NLM catalog, but direct record/API access failed in this session. No new outcome data were acquired or counted as replication, and byte overlap/version corrections remain pending. A corrected publication copy is not automatically an independent experiment.

Further work should resolve study/strain/animal identities, retain early-death intervals rather than invent times, and obtain unexposed multi-timepoint studies from additional labs. Initial cohort uncertainty belongs in that future protocol. More endpoint fitting on these exposed 15 animals cannot resolve the kinetic question.

## Sources and use

[Original source](https://zenodo.org/records/15124940), [COMBINE primary paper](https://doi.org/10.1128/spectrum.03464-25), and [official new-version metadata](https://datasetcatalog.nlm.nih.gov/dataset?q=0003275942). Run `python run.py` to verify numerical replay. The evaluator scores alternative claims on the exposed retained cohort and requires separate mechanism/novelty review.
