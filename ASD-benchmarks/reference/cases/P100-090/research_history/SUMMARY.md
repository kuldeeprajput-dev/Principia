# P100-090 attempt portfolio

A compact aggregate-memory rule tests whether directional heterogeneity adds useful short-horizon information beyond current collective rotation. Its interpretation is phenomenological and limited to the released group experiments.

| Attempt/model | Development error | Worst development group | Coefficients | Final confirmation error |
|---|---:|---:|---:|---:|
| calibration | 0.1588337 | 0.3657689 | 0 | 0.1835706 |
| constant | 0.2039894 | 0.602738 | 1 | 0.2243616 |
| current | 0.07054484 | 0.09771443 | 0 | 0.06571862 |
| flexible | 0.08384881 | 0.2218331 | 33 | 0.06474652 |
| persistence | 0.07350839 | 0.1109798 | 0 | 0.07354352 |
| attempt_001 | 0.06973392 | 0.09937075 | 2 | 0.06590347 |
| attempt_002 | 0.07122576 | 0.1095555 | 3 | 0.07247815 |
| attempt_003 | 0.07058978 | 0.1020539 | 4 | 0.06655616 |
| attempt_004 | 0.06901736 | 0.09689204 | 3 | 0.06614825 |
| attempt_005 | 0.06946779 | 0.09711878 | 2 | 0.06595787 |
| attempt_006 | 0.0696907 | 0.09908691 | 3 | 0.06611649 |

Development-selected reference: **attempt_005**. Attempt004 improved mean and worst development error. Attempts005 and006 provided no new predictive or worst-group gain. Stop after those two substantive failures; complexity tie rule selects the simpler frozen candidate before any confirmation.

All confirmation results are now exposed; they did not guide revisions. Future uses are retrospective/source-aware.
