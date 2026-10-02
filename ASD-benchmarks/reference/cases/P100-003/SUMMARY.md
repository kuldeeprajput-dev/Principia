# P100-003: Recorded interferometer band-power stability

5 substantive attempts; selected reference **constant**. Primary units: 10^-21 strain.

| Model | Development MAE | Complexity | Confirmation MAE |
|---|---:|---:|---:|
| constant | 0.01018148 | 1 | 0.008555377 |
| median4 | 0.01114828 | 0 | 0.008420087 |
| rbf | 0.01240749 | 25 | 0.008214949 |
| attempt_001 | 0.01109974 | 1 | 0.008243811 |
| attempt_002 | 0.0130433 | 3 | 0.01127274 |
| attempt_003 | 0.01361764 | 2 | 0.008687224 |
| attempt_004 | 0.01139422 | 1 | 0.008052007 |
| attempt_005 | 0.01162997 | 2 | 0.008212009 |

All five extensions lose to the stationary training median. The final two robust/volatility hypotheses add no predictive or robust-transfer gain. Instrumental attribution is unidentifiable under the retained CW injection.

None of the five proposed relaxation, cross-band or robust-response extensions beats the stationary training median during forward development. The retained reference also loses modestly to several controls on the final blocks. These adverse outcomes are part of the result.

All data come from one short segment. The DATA bit and declared injection bits are required; other quality bits are retained rather than silently asserted clean. No injection/noise decomposition is identified.
