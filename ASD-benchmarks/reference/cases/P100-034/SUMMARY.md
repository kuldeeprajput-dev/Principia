# P100-034 campaign summary

The reference `attempt_008_reserve_conserved` was chosen before confirmation. Development error was **13.65332**; reserved-group error is **17.139171 nA** across **6 groups and 18 observations**. Scores use equal group weights, with equal row weights within each group. No population confidence interval is inferred from these small samples.

| Attempt | Hypothesis/model | Development error | Parameters | Improvement over incumbent>1% |
|---|---|---:|---:|---|
| 001 | attempt_001_genotype_hill | 38.452771 | 3 | False |
| 002 | attempt_002_local_hill | 710.64538 | 1 | False |
| 003 | attempt_003_two_pool | 41.33442 | 3 | False |
| 004 | attempt_004_reserve | 16.396078 | 4 | True |
| 005 | attempt_005_reserve_pooled | 15.624515 | 3 | True |
| 006 | attempt_006_reserve_low04 | 14.769448 | 4 | True |
| 007 | attempt_007_reserve_rational | 14.525333 | 4 | True |
| 008 | attempt_008_reserve_conserved | 13.65332 | 3 | True |
| 009 | attempt_009_reserve_genotype_rate | 14.289409 | 4 | False |
| 010 | attempt_010_reserve_no04 | 15.272774 | 2 | False |

| Frozen model | Confirmation primary error |
|---|---:|
| reference | 17.139171 |
| baseline_persistence | 66.578997 |
| baseline_hill4 | 35.04473 |
| baseline_flexible | 20.678893 |

Useful scientific failures are preserved in `attempts/`. No unfavorable attempt is deleted. See `DEVELOPMENT_DIAGNOSTICS.json`, source/split/protocol freezes, first `CONFIRMATION.json`, and final reader.
