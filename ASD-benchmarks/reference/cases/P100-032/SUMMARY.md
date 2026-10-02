# P100-032 campaign summary

The reference `baseline_flexible` was chosen before confirmation. Development error was **0.30952647**; reserved-group error is **0.37185336 cmH2O** across **5 groups and 3768 observations**. Scores use equal group weights, with equal row weights within each group. No population confidence interval is inferred from these small samples.

| Attempt | Hypothesis/model | Development error | Parameters | Improvement over incumbent>1% |
|---|---|---:|---:|---|
| 001 | attempt_001_damped | 0.32749661 | 1 | False |
| 002 | attempt_002_periodic | 0.31941485 | 2 | False |
| 003 | attempt_003_flow | 0.32437411 | 4 | False |
| 004 | attempt_004_regime | 0.32280054 | 6 | False |
| 005 | attempt_005_limited | 0.31912585 | 2 | False |

| Frozen model | Confirmation primary error |
|---|---:|
| reference | 0.37185336 |
| baseline_persistence | 0.49150667 |
| baseline_tangent | 0.5091419 |
| baseline_flexible | 0.37185336 |

Useful scientific failures are preserved in `attempts/`. No unfavorable attempt is deleted. See `DEVELOPMENT_DIAGNOSTICS.json`, source/split/protocol freezes, first `CONFIRMATION.json`, and final reader.
