# P100-011: Latency-constrained inference throughput

## Scenario and question

Source MLPerf results provide matched Offline and Server measurements for 127 eligible workload/system pairs across 74 complete systems. Eleven systems are reserved. Offline throughput is explicitly permitted calibration; results inferred by the source and alternate quality-threshold aliases are excluded.

Can a compact utilization law transfer Offline capacity to latency-constrained Server throughput?

## Experimental contract

Predict reported Server throughput using same-system Offline benchmark result, workload label and accelerator count. This is calibrated scenario transfer, not performance prediction before benchmarking. Matched Offline throughput on every evaluation system; held-system Server/Interactive results forbidden.

The campaign completed 5 substantive hypotheses. Native bytes and exact sample anchors are preserved. Model selection uses whole-group development error and a 1% simplicity tolerance; selection and stopping were frozen before the separate no-fitting confirmation process. All outcomes are now exposed for future users.

## Main result and interpretation

A workload-specific bounded utilization response with an accelerator-count term improves the reserved mean error over direct Offline transfer, a single utilization factor and the constrained flexible control. However, simpler workload-only alternatives perform better retrospectively and are retained without reselection.

$$
\widehat S=Q\,\sigma\!\left(b_{w}+a\log(1+N)\right)
$$

The exact executable expression is: S_hat=Q*sigmoid(b_workload+a*ln(1+N)).

Parameters: b[0] = 0.5549975531; b[1] = 8; b[2] = 2.618949012; b[3] = 1.529323229; b[4] = 1.836037547; b[5] = 4.014159041; b[6] = 0.1647651826. Coefficient ordering follows run.py and rules.json.

Q is calibrated Offline throughput in tokens/s, N is accelerator count, w is workload and sigma is the logistic function. Workload coefficients and their ordering are explicit in rules.json; unseen workloads use the declared fallback.

## Performance and adverse evidence

| Model | Development MAE | Confirmation MAE |
|---|---:|---:|
| attempt 002 | 7088.36 | 77726.8 |
| utilization | 7392.5 | 118092 |
| rbf | 9947.24 | 86915.3 |

MAE is averaged within each complete group and then equally over the 11 reserved groups (16 observations). Errors are in tokens/s. Per-group RMSE, bias and failures are available in evidence/by_group.csv; small or dependent group counts do not support population confidence claims.

The lowest retrospective confirmation error belongs to attempt 001. It did not change the frozen selection. The direction and boundary behavior of fitted utilization terms do not identify a hardware-overhead mechanism. Retrospective workload-only gains were not used to reselect the reference.

## Value, limits and evaluation

This is a calibrated benchmark association, useful for assessing conversion between two evaluation modes. The fitted accelerator effect is not an identified coordination or hardware-efficiency law: platforms, software, precision and submitter choices are not randomized. Reserved mean error is much larger than development error, reflecting difficult system-scale transfer. Several workload logits contact bounds; coefficients are not universal efficiencies. Offline calibration is mandatory, so this is not prediction from specifications alone.

Alternative agents can submit any predictor under this task's information budget. The shared evaluator reports task-unit errors, whole-group and worst-group results, coverage, abstention, optional intervals and meaningful event diagnostics. A different endpoint requires an independently reviewed new-task contract. Numerical success alone does not certify mechanism, novelty or deployed impact.

## Reproducibility and source

Run `python run.py` for the frozen reference replay. `rules.json` contains every fitted value; `task_spec.json` defines units and access; `evidence/` contains compact predictions and numerical evidence. Research history preserves all hypotheses, failed candidates, technical corrections and the first confirmation receipt.

Authoritative source: https://github.com/mlcommons/inference_results_v6.0. Redistribution terms: Apache License 2.0. Primary-source prior-art searches and limitations are recorded in PRIOR_ART.json.
