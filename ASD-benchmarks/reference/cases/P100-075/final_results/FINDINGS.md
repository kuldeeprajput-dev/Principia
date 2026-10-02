# Endothelial VCAM1: a donor-transfer falsification

## Experiment and task

The source measures RNA counts in 24 endothelial cultures: four donors, three substrate stiffnesses (30, 200 and 1000 kPa), and two shear conditions (4 and 10 dyn/cm²). We selected **VCAM1, Entrez 7412**, before inspecting count responses because the source study already identifies it as a mechanosensitive inflammatory marker. Counts are converted per library to $y=\log_2(1+10^6 n_{VCAM1}/N)$, where $N$ is the sum of gene counts. These are normalized count units, not absolute transcript concentration.

The task gives every model one donor-specific calibration, $c$, measured at 30 kPa and low shear. It predicts the five remaining culture conditions. Donors A, B and D were used for development with whole-donor folds; donor C was reserved by a recorded identifier hash. This is a calibrated culture-response diagnostic. It requires an expression assay and does not support uncalibrated real-time vascular monitoring.

## Main finding

**Mechanistically plausible response terms did not establish robust donor transfer.** Seven successive hypotheses tested bounded stiffness occupancy, shear-stiffness interaction, stiffness alone, a measured-design threshold, shear alone, calibration-dependent interaction and saturating interaction. The development-selected equation was the compact shear shift

$$
\widehat y=\max(0,c-0.8590802454\,s),
$$

where $s=1$ for high shear and $s=0$ for low shear. This coefficient is an effective expression change; it is not a mechanotransduction constant. Removing stiffness improved development MAE from 0.9192 for calibration alone to 0.8841 log-count units. The last two mechanistic challenges failed to improve that result, so selection and all states were frozen before confirmation.

On the reserved donor, the selected equation has **MAE 0.7635**, whereas simply predicting $\widehat y=c$ gives **0.4963**. The selected equation therefore **fails confirmation against the simplest matched-calibration comparator**. It remains the frozen selected reference for reproducibility; the retrospectively better calibration control is not silently promoted.

| Model | Development donor-balanced MAE | Reserved donor C MAE |
|---|---:|---:|
| Calibration copy | 0.9192 | 0.4963 |
| Additive log stiffness + shear | 0.9556 | 0.8247 |
| Constrained quadratic comparator | 0.9894 | 0.8724 |
| Selected shear-only response | 0.8841 | 0.7635 |

All errors use $\log_2(1+\mathrm{CPM})$ units. The five confirmation conditions belong to **one donor**, not five independent replications. No narrow population confidence interval or industrial benefit is claimed.

## Interpretation, value and limits

The evidence falsifies the proposed transferable calibrated response under this protocol. It does not disprove the source paper’s experimental association or establish absence of mechanosensing. Donor heterogeneity, low expression/count noise, only three stiffness levels and one culture per condition limit identification. The source’s known VCAM1 result is disclosed as prior art; no new molecular law is admitted.

A practical lesson is to compare mechanistic equations against equally calibrated simple controls and preserve donor grouping. A visually meaningful stiffness curve can transfer worse than one baseline assay. Additional donors and biological replicates, ideally with independent protein/inflammatory measurements, would be needed to evaluate a genuinely transferable mechanism.

## Reproduction and evaluation

`python run.py` verifies package hashes and reproduces every saved prediction from explicit frozen states in `rules.json`. `data/inputs.csv.gz` exposes only declared inputs; observations and native anchors are separate. `evidence/` retains all model and group outcomes, including failures. The research native adapter rebuilds counts, calibration and grouping directly from checksum-verified RDS/CSV files. `task_spec.json` defines identical information access for alternative equations; lower numerical error does not alone establish mechanism, novelty or clinical significance. All confirmation outcomes are now exposed for future users.

[Native source](https://zenodo.org/records/17925228), [original study](https://doi.org/10.1016/j.biomaterials.2025.123932), and [VCAM1 gene mapping](https://www.ncbi.nlm.nih.gov/gene/7412/). Native data: CC BY 4.0. Literature consulted 2 October 2026.
