# Composite fatigue: continuation findings

**Status: retrospective scientific exploration; no fresh confirmation and no new physical law admitted.** Original final results are preserved. The best new candidate is `cycle-002`; the development-selected predictor is `old_log`. The latter selection and stopping decision were frozen before old-cohort error evaluation. Results on that exposed cohort cannot change the selection.

## Scenario and experimental method

Recorded dynamic modulus after an early stiffness calibration. The target unit is **GPa**. The development population contains 17 complete fatigue specimens. Leave-one-specimen-out validation keeps every later cycle of a specimen together. Early modulus E₀ is the original mean from cycles 10–20; no future modulus enters predictors. The original source-extracted target eligibility is retained, including unusually high finite values. The old cohort contains six specimens and 3,086 assigned rows, of which five nonfinite targets are excluded under the original task policy.

Fitting uses only the applicable training groups. Kernel scaling, center selection, missing-value handling and hyperparameter tuning use inner grouped or forward folds. Calibration information is supplied equally to relevant baselines. Whole linked measurements stay in one partition. There is no random-row split or row-bootstrap population confidence claim.

## What the equations establish

Let $u=\varepsilon/(1\%)$, $z=u^2\log[1+\max(N-20,0)/(1000\ \mathrm{cycles})]$, and let $E_0$ be the declared early modulus. The tests were

$$\widehat E=E_0\{r+(1-r)e^{-\beta z}\},\qquad 0\le r<1,$$

$$\widehat E=E_0\sqrt{\max\{r^2,1-2\beta z[E_0/(40\ \mathrm{GPa})]\}}.$$

Both exponents and square-root arguments are dimensionless. The logarithmic baseline is the first equation with $r=0$. Full and fold coefficients are in each cycle's `rules.json`. Neither additional mechanism is admitted.

Neither proposed mechanism improves the simple established logarithmic degradation predictor materially. The full parallel-floor fit collapses to a zero surviving fraction. The load-feedback floor is unidentifiable: setting its fitted 0.5 to zero leaves every development prediction unchanged. These observations favor restraint over claiming a surviving material component or accelerated-damage mechanism.

## Performance and counterexamples

Development error is equal whole-group MAE; numerical errors below use the stated target units. Old-cohort diagnostic errors use the original complete-group task averaging, as explained above. They are not a fresh test of discoveries made during this continuation.

| Model | Development error | Exposed-cohort diagnostic |
|---|---:|---:|
| kernel_nested | 1.7088752 | 2.8866978 |
| old_log | 1.6365408 | 1.8254476 |
| old_nested_flex | 1.719452 | 1.9380085 |
| old_persistence | 2.2591124 | 2.4910339 |
| cycle-001 | 1.6347277 | 1.8254475 |
| cycle-002 | 1.6315446 | 1.8314411 |

The best new candidate scores **1.6315446** against the strongest development baseline `old_log` at **1.6365408**, winning 10 of 17 development groups. Its exposed-cohort error is **1.8314411**, against the same comparator at **1.8254476**, winning 3 of 6 groups. The strongest baseline on the exposed cohort is `old_log` at **1.8254476**; the best new candidate wins 3 of 6 groups against it. The complete unfavorable group results are retained in `by_group.csv`; aggregate gains are not universal-transfer evidence.

## Practical significance and limits

A bounded stiffness-monitoring comparator remains useful. There is no demonstrated improvement in maintenance decisions, rejection rates or composite design; the negative mechanistic tests reduce the risk of making such decisions from an unidentifiable floor.

Prediction is conditional on early calibration and recorded survival. It does not predict fatigue life, failure load, residual strength or an unobserved failure threshold. Author-extraction anomalies cannot be treated as high-quality material mechanics. Three cure recipes and this laboratory campaign do not establish production transfer.

## Evidence and further work

Collect independent fatigue specimens with measured instantaneous stress/strain, calibrated dynamic modulus, interrupted residual-strength tests and complete failure outcomes. Freeze specimen-level validation before receiving their later-cycle responses.

[Native dataset](https://zenodo.org/records/15665325); [relevant primary source](https://doi.org/10.1088/1757-899X/1338/1/012018). Prior-art review is bounded and is not an exhaustive priority search or human scientific adjudication. Computational review does not constitute an independent experiment.

`CANDIDATE_FREEZE.json` binds selection, stopping and every fitted rule. `FALSIFYING_TESTS.json` records identifiability, ablations and applicable physical/numerical controls. `PARAMETERS_BY_FOLD.csv` preserves calibrated-coefficient instability. `VERIFICATION.json` checks exact predictions/metrics and target-input independence. `INPUT_INTEGRITY_TESTS.json` contains four disposable-file fault tests. Original source and final-package preservation is recorded separately. No unfavorable cycle is deleted or moved into discard candidates.

Replay: `python campaign.py 24 replay`. Refit reproduction belongs in a disposable new work root; existing freeze receipts must not be overwritten. `finish.py` provides the explicit freeze, controls and retrospective stages; they reject an existing freeze/diagnostic rather than silently replace it.
