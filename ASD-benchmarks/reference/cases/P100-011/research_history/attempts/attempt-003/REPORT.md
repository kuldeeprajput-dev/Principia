# Capacity

Instead of a direct utilization factor, test a reciprocal capacity law: Server capacity is limited by calibrated Offline capacity plus a workload-specific per-accelerator service constraint.

This hypothesis/configuration was recorded before execution. Selection uses development data only. Every failure remains part of scientific history.

## Executable candidate

S_hat=Q/(1+exp(-b_workload)*Q/(100000*N)).

Coefficients: [-1.204391127202631, 7.999999999999999, 1.1841016903488097, -3.901653766603104, 0.3931264698285723, 5.37831166906534].

## Grouped development evidence

Mean-group MAE 8137.27502 tokens/s; worst-group MAE 161724.286. Preserved alternative; not the selected reference.

## Falsification and interpretation

A workload-specific bounded utilization response with an accelerator-count term improves the reserved mean error over direct Offline transfer, a single utilization factor and the constrained flexible control. However, simpler workload-only alternatives perform better retrospectively and are retained without reselection. Reserved mean error is much larger than development error, reflecting difficult system-scale transfer. Several workload logits contact bounds; coefficients are not universal efficiencies. Offline calibration is mandatory, so this is not prediction from specifications alone.

Parameter sensitivity is in parameter_sensitivity.json. Fold extrema are descriptive, not population confidence intervals. All validation/training group memberships are retained in metrics.json and SCIENTIFIC_CHECKS.json.

## Replay

Run `python develop.py PATH_TO_LOCAL_DATAS attempts/attempt-003` only in a new exploratory workspace; the script refuses to overwrite completed evidence. The current confirmation outcomes are exposed. Frozen prediction replay is `python run.py` inside final_results.
