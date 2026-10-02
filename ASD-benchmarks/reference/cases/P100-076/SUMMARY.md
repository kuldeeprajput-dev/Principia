# P100-076 campaign summary

The reference `baseline_persistence` was chosen before confirmation. Development error was **0.72486772**; reserved-group error is **0.44196429 spikes per stimulus** across **8 groups and 266 observations**. Scores use equal group weights, with equal row weights within each group. No population confidence interval is inferred from these small samples.

| Attempt | Hypothesis/model | Development error | Parameters | Improvement over incumbent>1% |
|---|---|---:|---:|---|
| 001 | attempt_001_condition_threshold | 0.95617488 | 5 | False |
| 002 | attempt_002_saturation | 0.83596413 | 2 | False |
| 003 | attempt_003_recruitment | 0.80815103 | 3 | False |
| 004 | attempt_004_block | 0.83150146 | 3 | False |
| 005 | attempt_005_condition_gain | 0.88396716 | 5 | False |

| Frozen model | Confirmation primary error |
|---|---:|
| reference | 0.44196429 |
| baseline_persistence | 0.44196429 |
| baseline_rheobase | 0.72560674 |
| baseline_flexible | 0.73781354 |

Useful scientific failures are preserved in `attempts/`. No unfavorable attempt is deleted. See `DEVELOPMENT_DIAGNOSTICS.json`, source/split/protocol freezes, first `CONFIRMATION.json`, and final reader.
