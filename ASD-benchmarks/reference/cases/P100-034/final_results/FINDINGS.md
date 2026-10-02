# Calcium recruitment of synaptic response: calibrated finite reserve

Figure 5 of the Unc13 study contains control and C1-mutant Drosophila animal recordings. Each cell is tested sequentially at 0.4,0.75,1.5,3 and 6 mM extracellular calcium, with 10 paired-pulse sweeps per dose. This task predicts the author-extracted first-pulse mean current at the final three doses from the first two dose means. One explicitly missing6 mM observation remains excluded, without imputing it.

## Question and information budget

After two lower-dose blocks, forecast mean first-pulse current at the three later calcium doses; all animal data linked. First-pulse mean across ten sweeps at 0.4 and 0.75 mM per animal. Later 1.5/3/6 mM targets are excluded from calibration.

## Findings and interpretation

A finite recruitable response gives a compact alternative to normalizing the entire dose curve by one low-dose value. The earlier calibration can carry information about the later response ceiling. The effective ceiling is measured in current; it is not a counted vesicle pool.

The selected executable relation is:

Let $C$ be extracellular calcium in mM and $I_{0.4},I_{0.75}$ be the two early current measurements in nA. The effective ceiling is $A+B I_{0.4}$; $A$ has units nA, $B$ is dimensionless and $K$ has units mM.

$$
\widehat I(C)=I_{0.75}+\max(A+B I_{0.4}-I_{0.75},0)\frac{C-0.75}{K+C-0.75}.
$$

All concentration numbers in this expression are in mM. The unit coefficient on the subtracted early current is a model constraint; it does not identify a molecular depletion process.

The full coefficient table and variable ordering are in `EQUATIONS.md`; `rules.json` contains exact precision. All equation inputs and their units are declared in `task_spec.json`.

Local Hill inversion is unstable; common Hill occupancy and two-pool mixtures transfer poorly. Genotype-specific capacity or recruitment rates can add complexity without improving transfer after calibration. Specific comparisons remain in the attempt history.

## Experimental design and performance

The reference `attempt_008_reserve_conserved` was chosen before confirmation. Development error was **13.65332**; reserved-group error is **17.139171 nA** across **6 groups and 18 observations**. Scores use equal group weights, with equal row weights within each group. No population confidence interval is inferred from these small samples.

| Frozen model | Confirmation primary error |
|---|---:|
| reference | 17.139171 |
| baseline_persistence | 66.578997 |
| baseline_hill4 | 35.04473 |
| baseline_flexible | 20.678893 |

10 substantive development attempts were preserved. Selection used whole-group out-of-fold errors and preferred the simplest model within 1% of the minimum. Continuation ended only after two consecutive substantive attempts failed to improve prediction and no supported mechanism/robustness gain justified another candidate. Confirmation ran separately after code, source, states, selection and stopping were frozen. No later diagnostic winner was promoted.

## Scope, prior work and value

Six reserved animals provide internal experimental-group evidence. Calcium is increased sequentially, so dose and recording time are confounded. Currents also depend on postsynaptic responsiveness and recording stability. The negative early-calibration coefficient is predictive, not a demonstrated causal depletion effect.

Blaum et al., PNAS 2025, already report genotype-related calcium sensitivity and short-term depression. Hill dose-response families, saturation and depletion are established. The candidate here is a calibrated predictive extension within these data, not a newly established molecular release mechanism.

No new universal law, independent experimental replication, clinical benefit or demonstrated industrial impact is claimed. Alternative valid discoveries can be evaluated using the same task contract; exact agreement with this equation is unnecessary. Negative findings describe failed tested hypotheses, not a lack of scientific phenomena.

## Reproduction and evaluation

Run `python run.py` inside this folder to verify frozen asset hashes and reproduce all saved predictions. It uses no network, fitting, research-history import or hidden model state. Submitter predictions must use the same sample IDs, units, information budget and group cohort. `scientific_checks.py` adds domain diagnostics to the shared benchmark scorer; it does not execute submitted code. New endpoints require a separately reviewed task.

Sources: [authoritative data](https://zenodo.org/records/15629377), [primary study](https://doi.org/10.1073/pnas.2514151122). Source assets are CC BY 4.0; citations and exact native hashes are retained in the scenario research layer. Current confirmation outcomes are exposed for all future users.
