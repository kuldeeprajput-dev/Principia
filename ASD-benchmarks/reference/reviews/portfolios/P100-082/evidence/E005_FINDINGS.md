# Soil respiration: continuation findings

**Status: retrospective scientific exploration; no fresh confirmation and no new physical law admitted.** Original final results are preserved. The best new candidate is `cycle-002`; the development-selected predictor is `old_temperature_moisture`. The latter selection and stopping decision were frozen before old-cohort error evaluation. Results on that exposed cohort cannot change the selection.

## Scenario and experimental method

Later-date chamber-derived CO₂ mass flux at established sites. The target unit is **g CO2 m^-2 h^-1**. The original development subset contains 31,461 eligible observations at 16 sites. Three forward folds train through 40%, 55% and 70% of each site’s dates and evaluate the next complete date blocks. The primary metric averages 48 site × forward-block RMSEs. Context amplitudes are calibrated only on earlier training dates. Finite negative/high flux values remain scored. Missing moisture stays explicit; three source sites without usable 5 cm soil temperature remain outside this task. The old cohort has 6,928 observations at 15 sites.

Fitting uses only the applicable training groups. Kernel scaling, center selection, missing-value handling and hyperparameter tuning use inner grouped or forward folds. Calibration information is supplied equally to relevant baselines. Whole linked measurements stay in one partition. There is no random-row split or row-bootstrap population confidence claim.

## What the equations establish

With $T_0=-46.02^\circ$C and $T_\mathrm{ref}=10^\circ$C, let $h(T)=1/(T_\mathrm{ref}-T_0)-1/(T-T_0)$, measured in K⁻¹. The repaired baseline is

$$\widehat R=A_c e^{E_0h(T)}.$$

The new tests use a positive two-activation sum and a strictly backward-looking history term:

$$\widehat R=A_c[w e^{E_1h(T)}+(1-w)e^{E_2h(T)}],\qquad
\widehat R=A_c\exp\!\left[E_0h(T)-\gamma\frac{\overline T_{\mathrm{past},30}-10^\circ\mathrm C}{10\ \mathrm K}\right].$$

$A_c$ has flux units g CO₂ m⁻² h⁻¹; activation coefficients have units kelvin. The 30-day mean uses only strictly earlier site dates, with a declared 10°C fallback. All 96 full-development context amplitudes, site/global fallbacks and fold-specific states are serialized; these are substantive calibration parameters, not hidden constants.

Dimensionless profiling repairs the Lloyd–Taylor optimizer and yields E₀≈208.04 K with a near-zero profile gradient. The repair is a baseline correction, not a discovery. A two-activation mixture collapses to its boundary (99% low-activation contribution), and backward-only thermal history changes development error negligibly. Neither establishes root/microbial pools or thermal acclimation.

## Performance and counterexamples

Development error is equal whole-group RMSE; numerical errors below use the stated target units. Old-cohort diagnostic errors use the original complete-group task averaging, as explained above. They are not a fresh test of discoveries made during this continuation.

| Model | Development error | Exposed-cohort diagnostic |
|---|---:|---:|
| kernel_nested | 0.24819251 | 0.29313336 |
| kernel_with_history | 0.25261744 | 0.30023734 |
| lt_repaired | 0.24294543 | 0.28719724 |
| lt_with_history_information_access | 0.24294543 | 0.28719724 |
| old_context_mean | 0.28181643 | 0.33395347 |
| old_lloyd_taylor | 0.24284625 | 0.28747418 |
| old_q10 | 0.24815157 | 0.29107335 |
| old_temperature_moisture | 0.24089518 | 0.2876755 |
| cycle-001 | 0.24294467 | 0.28720109 |
| cycle-002 | 0.24291328 | 0.28628881 |

The best new candidate scores **0.24291328** against the strongest development baseline `old_temperature_moisture` at **0.24089518**, winning 23 of 48 development groups. Its exposed-cohort error is **0.28628881**, against the same comparator at **0.2876755**, winning 7 of 15 groups. The strongest baseline on the exposed cohort is `lt_repaired` at **0.28719724**; the best new candidate wins 13 of 15 groups against it. The complete unfavorable group results are retained in `by_group.csv`; aggregate gains are not universal-transfer evidence.

## Practical significance and limits

A better verified thermal baseline supports honest carbon-flux modeling comparisons. No forestry intervention, carbon-accounting benefit or operational reduction in measurement burden has been demonstrated.

The source response is an author-derived chamber slope flux. Context calibration and shared ecological drivers prevent causal attribution to temperature, moisture, trenching or physiological acclimation. Site/date blocks are dependent within biological systems. This task assesses later measurements at known sites, not uncalibrated transfer to new sites or collars.

## Evidence and further work

Reserve new measurement seasons before analysis and obtain independent moisture, substrate and microbial/root measurements. Use controlled temperature or moisture perturbations where feasible to distinguish thermal history from unmeasured seasonal substrate availability.

[Native dataset](https://zenodo.org/records/17519671); [relevant primary source](https://doi.org/10.2307/2389824). Prior-art review is bounded and is not an exhaustive priority search or human scientific adjudication. Computational review does not constitute an independent experiment.

`CANDIDATE_FREEZE.json` binds selection, stopping and every fitted rule. `FALSIFYING_TESTS.json` records identifiability, ablations and applicable physical/numerical controls. `PARAMETERS_BY_FOLD.csv` preserves calibrated-coefficient instability. `VERIFICATION.json` checks exact predictions/metrics and target-input independence. `INPUT_INTEGRITY_TESTS.json` contains four disposable-file fault tests. Original source and final-package preservation is recorded separately. No unfavorable cycle is deleted or moved into discard candidates.

Replay: `python campaign.py 82 replay`. Refit reproduction belongs in a disposable new work root; existing freeze receipts must not be overwritten. `finish.py` provides the explicit freeze, controls and retrospective stages; they reject an existing freeze/diagnostic rather than silently replace it.
