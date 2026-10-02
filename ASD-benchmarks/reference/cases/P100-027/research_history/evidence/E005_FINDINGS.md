# Boiling-flow void profiles: continuation findings

**Status: retrospective scientific exploration; no fresh confirmation and no new physical law admitted.** Original final results are preserved. The best new candidate is `cycle-001`; the development-selected predictor is `cycle-001`. The latter selection and stopping decision were frozen before old-cohort error evaluation. Results on that exposed cohort cannot change the selection.

## Scenario and experimental method

Source-measured local void fraction at normalized probe positions. The target unit is **dimensionless void fraction**. Nine complete development runs, containing 108 probe-position observations, are evaluated by leaving one whole run out. Three original confirmation runs contain 36 observations; these targets were already exposed before this continuation. Superficial vapor/liquid velocities are computed from the supplied mass flux, quality and calibrated saturation densities. The coordinate is normalized by the largest observed coordinate; it is not independently verified as a wall radius.

Fitting uses only the applicable training groups. Kernel scaling, center selection, missing-value handling and hyperparameter tuning use inner grouped or forward folds. Calibration information is supplied equally to relevant baselines. Whole linked measurements stay in one partition. There is no random-row split or row-bootstrap population confidence claim.

## What the equations establish

With $j_g=Gx/\rho_g$, $j_l=G(1-x)/\rho_l$, and $s=r/r_{\max,\mathrm{observed}}$, the selected candidate is

$$a_d=\frac{j_g}{C_0(j_g+j_l)+V_d},\qquad
\widehat\alpha=\operatorname{logit}^{-1}[\operatorname{logit}(a_d)+b_0+b_2s^2].$$

Here $j_g,j_l,V_d$ have units m/s; $C_0,b_0,b_2,s$ are dimensionless. Numerical probabilities are clipped to $[10^{-7},1-10^{-7}]$ before the logit. Full-development coefficients are $C_0=0.87924253$, $V_d=0.81488727$ m/s, $b_0=1.28308128$ and $b_2=-2.58284817$; all fold states are retained at full precision.

The failed capillary alternative fixes $C_0=1$ and uses $V_d=K[g\sigma(T)(\rho_l-\rho_g)/\rho_l^2]^{1/4}$. Surface tension follows the known IAPWS saturation equation; this conversion is not a discovery.

Joint slip and spatial redistribution improve development prediction over a homogeneous-odds spatial correction. Fixing C₀=1 and imposing a known capillary velocity scale fail to preserve that advantage. Thus the successful fitted coefficients are useful conditional calibration terms; they are not separately identified universal slip constants. The old-cohort diagnostic retains a run where the simpler spatial baseline wins.

## Performance and counterexamples

Development error is equal whole-group MAE; numerical errors below use the stated target units. Old-cohort diagnostic errors use the original complete-group task averaging, as explained above. They are not a fresh test of discoveries made during this continuation.

| Model | Development error | Exposed-cohort diagnostic |
|---|---:|---:|
| kernel_nested | 0.12974641 | 0.3043548 |
| old_drift | 0.1586945 | 0.13919484 |
| old_homogeneous | 0.16292874 | 0.18256888 |
| old_mean | 0.27682198 | 0.32347983 |
| old_nested_flex | 0.2297623 | 0.25401873 |
| old_radial | 0.095049585 | 0.10670133 |
| cycle-001 | 0.084041029 | 0.095210129 |
| cycle-002 | 0.085568061 | 0.083838829 |
| cycle-003 | 0.098765796 | 0.092559347 |
| cycle-004 | 0.097107946 | 0.092009968 |

The best new candidate scores **0.084041029** against the strongest development baseline `old_radial` at **0.095049585**, winning 7 of 9 development groups. Its exposed-cohort error is **0.095210129**, against the same comparator at **0.10670133**, winning 2 of 3 groups. The strongest baseline on the exposed cohort is `old_radial` at **0.10670133**; the best new candidate wins 2 of 3 groups against it. The complete unfavorable group results are retained in `by_group.csv`; aggregate gains are not universal-transfer evidence.

## Practical significance and limits

The calibrated profile may support approximate local phase-distribution screening in this measured facility. No pressure-drop, heat-transfer or safety-margin improvement was measured, and no deployed controller is assessed.

Source radial units, coordinate orientation, geometry and supplied outlet-quality provenance remain limitations. Saturation-property calculations and homogeneous-velocity ratios are known physical relations, not discoveries. The fitted distribution coefficient is applied inside a local-profile correction and should not be equated to a uniquely measured cross-sectional drift-flux coefficient. No cross-facility, geometry or safety-certification claim is made.

## Evidence and further work

Verify probe-coordinate orientation and the source outlet-quality calculation; acquire independent runs spanning pressure, quality and geometry with simultaneous local void and velocity measurements. Reserve complete new dates and operating regimes before fitting.

[Native dataset](https://zenodo.org/records/14627088); [relevant primary source](https://iapws.org/public/documents/CH-L9/Surf-H2O-2014.pdf). Prior-art review is bounded and is not an exhaustive priority search or human scientific adjudication. Computational review does not constitute an independent experiment.

`CANDIDATE_FREEZE.json` binds selection, stopping and every fitted rule. `FALSIFYING_TESTS.json` records identifiability, ablations and applicable physical/numerical controls. `PARAMETERS_BY_FOLD.csv` preserves calibrated-coefficient instability. `VERIFICATION.json` checks exact predictions/metrics and target-input independence. `INPUT_INTEGRITY_TESTS.json` contains four disposable-file fault tests. Original source and final-package preservation is recorded separately. No unfavorable cycle is deleted or moved into discard candidates.

Replay: `python campaign.py 27 replay`. Refit reproduction belongs in a disposable new work root; existing freeze receipts must not be overwritten. `finish.py` provides the explicit freeze, controls and retrospective stages; they reject an existing freeze/diagnostic rather than silently replace it.
