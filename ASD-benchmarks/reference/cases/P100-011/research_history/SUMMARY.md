# P100-011: Latency-constrained inference throughput

5 substantive attempts; selected reference **attempt_002**. Primary units: tokens/s.

| Model | Development MAE | Complexity | Confirmation MAE |
|---|---:|---:|---:|
| offline | 8989.515 | 0 | 132542 |
| rbf | 9947.241 | 25 | 86915.27 |
| utilization | 7392.502 | 1 | 118091.8 |
| attempt_001 | 7642.969 | 6 | 67991.2 |
| attempt_002 | 7088.358 | 7 | 77726.76 |
| attempt_003 | 8137.275 | 6 | 70812.32 |
| attempt_004 | 7762.51 | 7 | 67991.71 |
| attempt_005 | 7569.859 | 7 | 68078.29 |

Attempts3,4,5 fail to improve the selected compact parallel-utilization response. Category boundary fits and the tiny independent-system confirmation set limit interpretation; the flexible control was corrected before selection.

A workload-specific bounded utilization response with an accelerator-count term improves the reserved mean error over direct Offline transfer, a single utilization factor and the constrained flexible control. However, simpler workload-only alternatives perform better retrospectively and are retained without reselection.

Reserved mean error is much larger than development error, reflecting difficult system-scale transfer. Several workload logits contact bounds; coefficients are not universal efficiencies. Offline calibration is mandatory, so this is not prediction from specifications alone.
