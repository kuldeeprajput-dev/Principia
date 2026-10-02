# P100-058: Differential scanning calorimetry, gel permeation chromatography and linear rheology measurements of poly(D,L-lactide) (Aldrich 805734)

> Principia-100 | Standardized portfolio | 1 October 2026

## Scenario and evaluation contract

Domain: Polymer physics. The current default task predicts Storage modulus G prime in Pa. Independent unit: whole temperature sweep. Its packaged cohort contains 35 assigned rows in 2 groups.

**All supplied outcomes are now exposed.** Historical reserved evaluations remain part of the evidence record; future scores are retrospective. No newly established fundamental law or measured deployment impact is admitted by this packaging.

## Current portfolio findings

**Validated extension:** Unfitted PLA3D850 loss prediction is a useful orthogonal response check under frozen storage calibration.

Limit: Loss comes from the same instrument/experiments and does not establish independent replication or fully identified modes.

**Unsupported or falsified:** Recycled-PLA loss response falsifies general storage-to-loss reliability of the calibrated family.

Limit: Material-specific dissipative behavior or metrology is unresolved; parameters must not be retuned against these exposed outcomes and relabeled fresh.

## Versioned tasks

| Task family | Target and information | Source scope |
|---|---|---|
| original | Storage modulus G prime (Pa) | original corpus |
| continuation | Storage modulus G prime (Pa) | original corpus |
| PLA PLA3D850-loss | Unfitted loss modulus (Pa) | supplemental |
| PLA PLA3D850-storage | Storage modulus (Pa) | supplemental |
| PLA PLA_recycled-loss | Unfitted loss modulus (Pa) | supplemental |
| PLA PLA_recycled-storage | Storage modulus (Pa) | supplemental |

Different targets, calibration budgets and cohorts have different task IDs. Their raw error values cannot be pooled into a scenario ranking. Exact equations, coefficients, permitted variables, timing, groups and per-model results are bound in the task packages.

Evaluation: the shared CLI provides numerical scoring, explicit coverage and abstention, uncertainty and event diagnostics. Agent review separately assesses scientific support; no aggregate discovery score is produced.

<!-- pagebreak -->

## Detailed reference note: Polymer rheology: thermal transfer and its loss-response limit

**Research edition: 1 October 2026. Historical results remain preserved; this reader edition uses the shared benchmark evaluator.**

## Supported findings and constitutive equation

The response is native storage modulus G' in Pa; independently recorded loss modulus G'' is never fitted or used for selection. Whole-temperature development uses 7 sweeps of one PDLLA15k batch. The existing T70/T80 cohort is now exposed; all revised comparisons there are retrospective.

$$
G'(\omega,T)=\sum_jG_j\frac{(\omega a_T\tau_j)^2}{1+(\omega a_T\tau_j)^2}.
$$

$$
G''(\omega,T)=\sum_jG_j\frac{\omega a_T\tau_j}{1+(\omega a_T\tau_j)^2},
$$

$$
\log_{10}a_T=-\frac{C_1(T-T_r)}{C_2+T-T_r}.
$$

The selected PDLLA state has T_r=60 C, C_1=12, C_2=100 K and 13 fixed clocks from 10<super>-6</super> to10<super>6</super> seconds. Nonnegative amplitudes and all fold states are in rules.json. Ridge was allowed in nested whole-temperature tuning; the full-development selection uses ridge 0. This is a stronger implementation of established Maxwell/WLF physics, not a new constitutive law.

Positive-response development logMAE is 0.571979; the exposed cohort gives 0.311133 and physical MAE 54.2685 Pa, versus the old 0.404461 and 116.619 Pa. Logs score 32 positive readings; physical errors preserve all 35, including 3 negative native readings. The unfitted loss response gives 0.152957 logMAE, using identical coefficients, versus old 0.256751. Sparse, Arrhenius and fractional competitors do not improve the development primary error.

## Fresh material challenge and its failure boundary

Before opening new numeric responses, a separate protocol reserved higher temperatures of two commercial PLA materials from Zenodo 17288444. Lower-temperature storage sweeps supplied declared material calibration: 110–140 C for PLA3D850 and 130–150 C for recycled PLA. Independent reserved sweeps were 150–180 C and 160–170 C respectively. Publisher MD5/local SHA256, filename-only selection, parser header repair, model freeze and first response opening are traceable. These are distinct material measurements from the same authors/instrument, not independent laboratories. This is calibrated physical-family transfer, not zero-shot coefficient transfer.

WLF storage logMAE is 0.709324 versus Arrhenius 1.199815 for PLA3D850 (66 rows/4 temperatures), and 0.379836 versus 0.808621 for recycled PLA (30 rows/2 temperatures). Yet all held-temperature biases are negative, and error grows at hotter temperatures. Unfitted loss logMAE is 0.464169 for PLA3D850 but 1.860375 for recycled PLA: the latter falsifies a generally reliable storage-to-loss transfer claim. Old PDLLA zero-shot parameters fail badly on both. No final-test performance was used to revise or promote models.

## Value, identifiability and next evidence

The solid contribution is a frozen cross-material challenge plus preserved orthogonal-response failure. Mode conditioning reaches 2.4 x10<super>16</super>; individual clocks, exact band masses and zero-frequency viscosity are not identified. An elastic plateau and very slow tail are indistinguishable in these observations. Compliance remains uncorrected. New creep/relaxation or independently calibrated complex-modulus measurements are needed to distinguish spectra and establish processing relevance. Fresh-challenge storage/loss tables and frozen calibrated models are separate from the old-task candidate.

## Reproduction and evaluation

Run `python run.py` to verify frozen predictions. Use `python evaluator/evaluate.py example --output /tmp/submission` and `python evaluator/evaluate.py score --submission /tmp/submission --output /tmp/report --trust-code` in a new output location. This trusted-code replay is not a security sandbox. Evaluator scores exposed targets and does not grant novelty from error. Exact source/sample anchors are in data/observations.csv.gz; complete numerical evidence and unfavorable models remain in evidence/.

## Sources and prior art

- [Native PDLLA record](https://zenodo.org/records/17294879)
- [Commercial PLA challenge record](https://zenodo.org/records/17288444)
- [Generalized versus fractional Maxwell prior work](https://pubs.rsc.org/en/content/articlehtml/2024/sm/d4sm00749b)
- [Spectrum identification prior work](https://doi.org/10.1016/j.ijsolstr.2015.04.018)

Targeted primary-source checking is not exhaustive novelty adjudication. Established model-family success is distinguished from a new physical law.
