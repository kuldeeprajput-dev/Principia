# P100-079 campaign summary

The reference `baseline_persistence` was chosen before confirmation. Development error was **0.024515141**; reserved-group error is **0.061158553 ug animal^-1 h^-1** across **2 groups and 10 observations**. Scores use equal group weights, with equal row weights within each group. No population confidence interval is inferred from these small samples.

| Attempt | Hypothesis/model | Development error | Parameters | Improvement over incumbent>1% |
|---|---|---:|---:|---|
| 001 | attempt_001_bateman | 0.025287239 | 3 | False |
| 002 | attempt_002_relative_decay | 0.027442272 | 2 | False |
| 003 | attempt_003_two_decay | 0.024715595 | 4 | False |
| 004 | attempt_004_baseline_drift | 0.029255905 | 3 | False |
| 005 | attempt_005_lognormal | 0.024601453 | 3 | False |

| Frozen model | Confirmation primary error |
|---|---:|
| reference | 0.061158553 |
| baseline_persistence | 0.061158553 |
| baseline_decay | 0.052842084 |
| baseline_flexible | 0.055993567 |

Useful scientific failures are preserved in `attempts/`. No unfavorable attempt is deleted. See `DEVELOPMENT_DIAGNOSTICS.json`, source/split/protocol freezes, first `CONFIRMATION.json`, and final reader.
