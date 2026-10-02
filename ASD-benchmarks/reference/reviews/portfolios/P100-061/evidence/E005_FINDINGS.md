# Hydrogen membrane permeation: continuation findings

**Status: retrospective scientific exploration; no fresh confirmation and no new physical law admitted.** Original final results are preserved. The best new candidate is `cycle-004`; the development-selected predictor is `cycle-004`. The latter selection and stopping decision were frozen before old-cohort error evaluation. Results on that exposed cohort cannot change the selection.

## Scenario and experimental method

Area-normalized hydrogen molar flux through four calibrated membrane designs. The target unit is **mol s^-1 m^-2**. The 120 development mixture measurements form six whole gas × temperature blocks across four membrane designs. Every outer fold withholds one complete block, including all five native fraction/flow points. All candidates and flexible comparators have the same declared 64 pure-H₂ calibration measurements at 350/450°C. The original 400°C cohort has 60 mixture observations in three gas blocks. It is an exposed retrospective diagnostic. Pure calibration is not silently treated as unavailable to the flexible comparators.

Fitting uses only the applicable training groups. Kernel scaling, center selection, missing-value handling and hyperparameter tuning use inner grouped or forward folds. Calibration information is supplied equally to relevant baselines. Whole linked measurements stay in one partition. There is no random-row split or row-bootstrap population confidence claim.

## What the equations establish

Define $\pi_r=p_r/(1\ \mathrm{bar})$, $\pi_p=p_p/(1\ \mathrm{bar})$, and $F=(F_n/V_m)(1\,\mathrm{min}/60\,\mathrm{s})$ with $V_m=22.414$ L/mol. If cumulative removed hydrogen is $q$, local bulk fraction is $x_b=(Fx_{\mathrm{in}}-q)/(F-q)$. The selected model solves

$$x_s=1-(1-x_b)\exp[J/(\kappa\pi_r)],\qquad
J=P_m(T)[(\pi_rx_s)^{n_m}-\pi_p^{n_m}]_+,$$

$$\kappa=K_mG_g\left(\frac{F_n}{5\,\mathrm{L\,min^{-1}}}\right)^{0.60}\left(\frac{T}{673.15\,\mathrm{K}}\right)^{0.30},\qquad dq=J\,dA.$$

$J,P_m,K_m,\kappa$ have flux units mol s⁻¹ m⁻²; $G_g,n_m$ are dimensionless. The pure calibration is $P_m(T)=P_{m,\mathrm{ref}}\exp[B_m(1/T_\mathrm{ref}-1/T)]$, with $B_m$ in kelvin. All 12 calibration coefficients and six mixture coefficients are saved at full precision. The mixture coefficients are four log reference-film coefficients and log Ar/He factors relative to N₂, so logarithms apply to coefficients normalized by one flux unit.

Removal is explicitly bounded by $q\le F(x_{\mathrm{in}}-\pi_p/\pi_r)/(1-\pi_p/\pi_r)$. Sixty-four midpoint axial cells and local bisection solve the closure. This equilibrium/material-balance bound is a physical constraint, not an independent discovery.

Distributed axial depletion, consistent pressure-normalized temperature scaling and nonlinear stagnant-inert film transport give a substantially better compact physical implementation than the earlier linear-film approximation. These mechanisms are established prior art. The development-selected Stefan closure beats the strongest development comparator, but the recreated original-grid residual RBF is stronger on all three old-cohort gas blocks. There is consequently no all-comparator superiority claim or newly discovered physical law.

## Performance and counterexamples

Development error is equal whole-group MAE; numerical errors below use the stated target units. Old-cohort diagnostic errors use the original complete-group task averaging, as explained above. They are not a fresh test of discoveries made during this continuation.

| Model | Development error | Exposed-cohort diagnostic |
|---|---:|---:|
| kernel_nested | 0.0046582048 | 0.0058603344 |
| membrane_residual_rbf_nested | 0.031571702 | 0.0085438863 |
| membrane_residual_rbf_original_grid | 0.0053248297 | 0.0016878248 |
| old_coupled | 0.023269584 | 0.012896336 |
| old_mean | 0.048415024 | 0.044782248 |
| old_rbf | 0.034081804 | 0.0067404997 |
| old_richardson | 0.15804312 | 0.15951774 |
| old_sieverts | 0.17517664 | 0.17667522 |
| cycle-001 | 0.02206686 | 0.012689675 |
| cycle-002 | 0.020969008 | 0.012263999 |
| cycle-003 | 0.012681438 | 0.012597519 |
| cycle-004 | 0.0041089199 | 0.0038528441 |
| cycle-005 | 0.004269796 | 0.0030608583 |
| cycle-006 | 0.0042244082 | 0.0027840148 |

The best new candidate scores **0.0041089199** against the strongest development baseline `kernel_nested` at **0.0046582048**, winning 5 of 6 development groups. Its exposed-cohort error is **0.0038528441**, against the same comparator at **0.0058603344**, winning 3 of 3 groups. The strongest baseline on the exposed cohort is `membrane_residual_rbf_original_grid` at **0.0016878248**; the best new candidate wins 0 of 3 groups against it. The complete unfavorable group results are retained in `by_group.csv`; aggregate gains are not universal-transfer evidence.

## Practical significance and limits

The compact model provides executable, nonnegative flux and recovery forecasts with explicit feed and equilibrium bounds. This is useful separator-screening infrastructure. No process-energy savings, validated design change, deployment or operating-cost reduction has been demonstrated.

Four membrane designs and calibrated pure-H₂ responses do not establish transfer to a new specimen. The simple closure lumps support/selective-layer effects into the pure-response calibration, rather than reproducing the source layered model completely. Mixture measurements use 3 bar absolute retentate pressure and a nominal 1 bar permeate; mixture-pressure transfer outside that setting is untested. The five operating points are feed fractions 0.7/0.8/0.9 at 5 normal L/min, plus 3 and 7 normal L/min at fraction 0.8. Development temperatures are 350/450°C; the exposed diagnostic is 400°C. Flow/fraction sampling comprises matched slices, not a full factorial interaction experiment. Measurement uncertainty and instrument-specific calibration certificates are unavailable. The developing-layer alternative has larger numerical segment sensitivity and is not selected.

## Evidence and further work

Acquire machine-readable independent membrane cohorts with pure-H₂ calibration, active geometry, specified reference-flow conditions and mixed-gas recovery measurements. Use new devices and conditions reserved before fitting, and compare against the source layered model and equally calibrated residual predictors.

[Native dataset](https://zenodo.org/records/10691625); [relevant primary source](https://doi.org/10.1016/j.ijhydene.2024.05.225). Prior-art review is bounded and is not an exhaustive priority search or human scientific adjudication. Computational review does not constitute an independent experiment.

`CANDIDATE_FREEZE.json` binds selection, stopping and every fitted rule. `FALSIFYING_TESTS.json` records identifiability, ablations and applicable physical/numerical controls. `PARAMETERS_BY_FOLD.csv` preserves calibrated-coefficient instability. `VERIFICATION.json` checks exact predictions/metrics and target-input independence. `INPUT_INTEGRITY_TESTS.json` contains four disposable-file fault tests. Original source and final-package preservation is recorded separately. No unfavorable cycle is deleted or moved into discard candidates.

Replay: `python campaign.py 61 replay`. Refit reproduction belongs in a disposable new work root; existing freeze receipts must not be overwritten. `finish.py` provides the explicit freeze, controls and retrospective stages; they reject an existing freeze/diagnostic rather than silently replace it.

The matching native-source paper is DOI 10.1016/j.ijhydene.2024.05.225. It already models axial depletion and external film transfer; the earlier DOI 10.1016/j.ijhydene.2024.04.337 supplies the Sherwood context. The source paper supplies layer thickness and geometry beyond the workbook. This continuation does not silently import those measurements into fitted inputs. See `NORMAL_FLOW_CONVENTION.md`: native `ln/min` and manufacturer documentation support 22.414 L/mol; the 24.465 L/mol result is a reference-condition stress test, not a measured uncertainty interval. The selected closure converges at 64 axial segments; the unselected entrance-layer model has larger segment sensitivity.
