# Rumen fermentation: continuation findings

**Status: retrospective scientific exploration; no fresh confirmation and no new physical law admitted.** Original final results are preserved. The best new candidate is `cycle-002`; the development-selected predictor is `kernel_nested`. The latter selection and stopping decision were frozen before old-cohort error evaluation. Results on that exposed cohort cannot change the selection.

## Scenario and experimental method

Gas accumulation at 12–48 h using only measured 4/8 h prefixes. The target unit is **mL**. The 568 development observations cover 142 flasks across three native protocols and three development DG runs. Leave-one-DG-run-out validation keeps its entire set of flasks and protocols together. Errors are calculated as RMSE within each complete protocol × DG-run group, then averaged over nine groups. The 142 flasks do not imply 142 independent run-level experiments. The old cohort contains 216 observations in three protocol × run-4 groups; its diagnostic metric averages those three complete groups, following the original evaluator.

Fitting uses only the applicable training groups. Kernel scaling, center selection, missing-value handling and hyperparameter tuning use inner grouped or forward folds. Calibration information is supplied equally to relevant baselines. Whole linked measurements stay in one partition. There is no random-row split or row-bootstrap population confidence claim.

## What the equations establish

For $\Delta=t-8\ \mathrm h$ and $q=\log(G_8/G_4)$, the first test is

$$\widehat G(t)=G_8\exp\!\left[q\frac{1-e^{-k\Delta}}{e^{4\mathrm h\,k}-1}\right].$$

The competing increment model is

$$\widehat G(t)=G_8+(G_8-G_4)\left[w\frac{1-e^{-k_f\Delta}}{e^{4\mathrm h\,k_f}-1}+(1-w)\frac{1-e^{-k_s\Delta}}{e^{4\mathrm h\,k_s}-1}\right].$$

Gas volumes use mL, rates use h⁻¹, and $w$ is dimensionless. Every logarithm is a dimensionless volume ratio. Each protocol has fitted rates; all original positive prefix values remain unchanged. Both equations reproduce 4/8 h measurements to numerical precision but are rejected as improved forecasting references.

Exact agreement with both early prefix values is insufficient to identify future fermentation. The declining relative-hazard (Gompertz) closure fails badly. A prefix-exact two-pool increment is better than Gompertz but still worse than the old curvature predictor and the matched nested kernel. Two protocol-specific slow rates reach the fixed upper boundary, so fitted pools should not be interpreted as measured biological substrate fractions.

## Performance and counterexamples

Development error is equal whole-group RMSE; numerical errors below use the stated target units. Old-cohort diagnostic errors use the original complete-group task averaging, as explained above. They are not a fresh test of discoveries made during this continuation.

| Model | Development error | Exposed-cohort diagnostic |
|---|---:|---:|
| kernel_nested | 7.6153703 | 6.5617142 |
| old_curvature | 8.6534368 | 7.5014541 |
| old_dual_pool | 8.6680461 | 7.9301438 |
| old_empirical_ratio | 9.4193943 | 11.180496 |
| old_first_order | 8.9257858 | 8.1297405 |
| old_linear_prefix | 212.20486 | 237.51363 |
| old_persistence | 49.216186 | 53.609193 |
| cycle-001 | 17.437881 | 20.471441 |
| cycle-002 | 9.1943456 | 10.785128 |

The best new candidate scores **9.1943456** against the strongest development baseline `kernel_nested` at **7.6153703**, winning 2 of 9 development groups. Its exposed-cohort error is **10.785128**, against the same comparator at **6.5617142**, winning 0 of 3 groups. The strongest baseline on the exposed cohort is `kernel_nested` at **6.5617142**; the best new candidate wins 0 of 3 groups against it. The complete unfavorable group results are retained in `by_group.csv`; aggregate gains are not universal-transfer evidence.

## Practical significance and limits

The preserved negatives warn against extrapolating feed-screening gas curves solely from an exact early-prefix fit. Existing calibrated forecasting comparators remain available; no feeding decision or animal-production impact has been established.

Gas volume alone does not establish feed digestibility, methane production, microbial yield or an animal response. Only three development DG runs and one already-exposed later run are available under familiar protocols. There is no held-out new-feed or new-laboratory test. The slow-rate prior bounds the forecast but does not identify an asymptotic biological capacity.

## Evidence and further work

Collect independent fermentation runs with denser early sampling and simultaneous substrate depletion, gas composition and microbial biomass. Reserve new substrates and laboratories; test whether a constrained two-pool interpretation predicts those independent measurements.

[Native dataset](https://zenodo.org/records/18335590); [relevant primary source](https://doi.org/10.1006/jtbi.1993.1109). Prior-art review is bounded and is not an exhaustive priority search or human scientific adjudication. Computational review does not constitute an independent experiment.

`CANDIDATE_FREEZE.json` binds selection, stopping and every fitted rule. `FALSIFYING_TESTS.json` records identifiability, ablations and applicable physical/numerical controls. `PARAMETERS_BY_FOLD.csv` preserves calibrated-coefficient instability. `VERIFICATION.json` checks exact predictions/metrics and target-input independence. `INPUT_INTEGRITY_TESTS.json` contains four disposable-file fault tests. Original source and final-package preservation is recorded separately. No unfavorable cycle is deleted or moved into discard candidates.

Replay: `python campaign.py 73 replay`. Refit reproduction belongs in a disposable new work root; existing freeze receipts must not be overwritten. `finish.py` provides the explicit freeze, controls and retrospective stages; they reject an existing freeze/diagnostic rather than silently replace it.
