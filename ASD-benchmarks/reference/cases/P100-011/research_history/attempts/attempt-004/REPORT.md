# Fixed overhead

Cross-system residuals may reflect node coordination rather than raw accelerator count. Add a bounded nodes-per-accelerator overhead and test identifiability of shared utilization versus overhead.

This hypothesis/configuration was recorded before execution. Selection uses development data only. Every failure remains part of scientific history.

## Executable candidate

S_hat=Q*sigmoid(b_workload)/(1+exp(a)*nodes/N).

Coefficients: [1.2282984673305322, 7.999999999999999, 3.3156476136522417, 2.2421619051644357, 2.1919656973640733, 4.364930631953728, -9.999999999999977].

## Grouped development evidence

Mean-group MAE 7762.51015 tokens/s; worst-group MAE 152247.158. Preserved alternative; not the selected reference.

## Falsification and interpretation

A workload-specific bounded utilization response with an accelerator-count term improves the reserved mean error over direct Offline transfer, a single utilization factor and the constrained flexible control. However, simpler workload-only alternatives perform better retrospectively and are retained without reselection. Reserved mean error is much larger than development error, reflecting difficult system-scale transfer. Several workload logits contact bounds; coefficients are not universal efficiencies. Offline calibration is mandatory, so this is not prediction from specifications alone.

Parameter sensitivity is in parameter_sensitivity.json. Fold extrema are descriptive, not population confidence intervals. All validation/training group memberships are retained in metrics.json and SCIENTIFIC_CHECKS.json.

## Replay

Run `python develop.py PATH_TO_LOCAL_DATAS attempts/attempt-004` only in a new exploratory workspace; the script refuses to overwrite completed evidence. The current confirmation outcomes are exposed. Frozen prediction replay is `python run.py` inside final_results.
