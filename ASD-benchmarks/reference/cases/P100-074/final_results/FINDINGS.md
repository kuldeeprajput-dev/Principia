# Calibrated Src biosensor fluorescence trajectories

## Scenario and task

Calibrated Src biosensor fluorescence trajectories. Native measurements come from [the authoritative source](https://zenodo.org/records/18911385). Complete dose curves; seven development and two hash-selected confirmation doses; leave-one-dose-out validation. No biological replicate identifiers.

Predict all t>7.5 min from source dose and same-curve measurements at 3,4.5,6 min. Calibration fixed at 6 min; no later response access.

## Experimental method

8 substantive development attempts tested distinct dynamic, mechanistic or ablation hypotheses. Selection used equally weighted whole-group MAE, with a 1% simpler-model tie rule. Baseline fitting and preparation did not count as attempts. All states and stopping were frozen before a separate confirmation command; confirmation never changed the reference.

First 9 lines and schemas inspected; early values through 6.75 min were visible across doses, outside target window. Later outcomes not printed before freeze.

## Reference equation and interpretation

$$
\widehat F(t)=F_6+(t-\tau)\left(a v_6+\tau b c_6\right),\qquad a=0.882574,\quad b=0.122161.
$$

Let $\tau=6\,\mathrm{min}$. Here F is fluorescence in source instrument units, t is minutes, $v_6=(F_6-F_{4.5})/(1.5\,\mathrm{min})$ is the calibrated slope, and $c_6=(F_6-2F_{4.5}+F_3)/(2.25\,\mathrm{min}^2)$ is calibrated curvature; a and b are dimensionless. The equation is a predictive tangent correction, not an identified phosphorylation law.

Full-precision coefficients and all comparator states are in `rules.json`. 

<!-- pagebreak -->

## Findings and performance

The development-selected curvature projection does not confirm a prediction gain. Its held-out MAE is 130.233 source units, versus 126.725 for the unadjusted early tangent,111.214 for the flexible control and 82.729 for the concentration-based Michaelis-Menten rate control. The lower-error controls were not promoted after confirmation.

| Frozen model | Confirmation MAE (source fluorescence units) |
|---|---:|
| reference | 130.233 |
| baseline persistence | 291.155 |
| baseline linear | 126.725 |
| baseline mm | 82.729 |
| baseline flexible | 111.214 |

All candidate results and per-group errors remain in `evidence/metrics.csv` and `evidence/by_group.csv`. The reference is the preselected model, not the retrospectively best confirmation model. No error is converted into invented percentage accuracy.

| Reserved group | Selected reference MAE |
|---|---:|
| dose-1 | 95.6238 |
| dose-5 | 164.843 |

## Value, limits and negative evidence

Nine source dose curves are not nine biological replicates. Source calibration maps intensity to fluorescence units rather than enzyme amount; optical and kinetic effects remain confounded. An Akt 1 CSV response equals its time axis and is excluded; no synthetic identity is scored as discovery. Calibration is permitted for every comparator. No new physical law or clinical impact is established.

Early curvature improved development but not reserved doses. Include a concentration-law control even when it looks weak on development. Optimization boundary contact and independent-dose failures are evidence against mechanistic identification. Never score a copied time axis as biochemical response.

## Reproduction and sources

Run `python run.py` inside this final package to verify its manifest and replay every frozen model. `rules.json` defines the exact coefficients, permitted input columns and units. `task_spec.json` and the shared evaluator provide the evaluation contract; valid alternative equations need not resemble these references.

Original study: [https://pubmed.ncbi.nlm.nih.gov/42619562/](https://pubmed.ncbi.nlm.nih.gov/42619562/). PET-quenching relief under phosphorylation and Michaelis-Menten initial velocities are reported by the authors. Our late-curve calibrated forecast is separate; neither first-order saturation nor power laws are novel families.
All packaged outcomes are exposed to future users. Agent review is computational/scientific criticism, not independent experimental replication or proof of novelty.
