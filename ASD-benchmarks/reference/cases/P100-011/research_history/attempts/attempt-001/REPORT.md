# Workload

Latency-constrained utilization is principally workload-specific. Fit one bounded utilization factor per workload and test whole unseen systems, using only matched Offline calibration.

This hypothesis/configuration was recorded before execution. Selection uses development data only. Every failure remains part of scientific history.

## Executable candidate

S_hat=Q*sigmoid(b_workload).

Coefficients: [1.2282496580943782, 7.999999999999999, 3.3154619422650367, 2.2420475241234703, 2.1919072081607656, 4.364494212903083].

## Grouped development evidence

Mean-group MAE 7642.96904 tokens/s; worst-group MAE 146735.983. Preserved alternative; not the selected reference.

## Falsification and interpretation

A workload-specific bounded utilization response with an accelerator-count term improves the reserved mean error over direct Offline transfer, a single utilization factor and the constrained flexible control. However, simpler workload-only alternatives perform better retrospectively and are retained without reselection. Reserved mean error is much larger than development error, reflecting difficult system-scale transfer. Several workload logits contact bounds; coefficients are not universal efficiencies. Offline calibration is mandatory, so this is not prediction from specifications alone.

Parameter sensitivity is in parameter_sensitivity.json. Fold extrema are descriptive, not population confidence intervals. All validation/training group memberships are retained in metrics.json and SCIENTIFIC_CHECKS.json.

## Replay

Run `python develop.py PATH_TO_LOCAL_DATAS attempts/attempt-001` only in a new exploratory workspace; the script refuses to overwrite completed evidence. The current confirmation outcomes are exposed. Frozen prediction replay is `python run.py` inside final_results.
