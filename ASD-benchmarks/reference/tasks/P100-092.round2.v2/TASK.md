# P100-092.round2.v2

Documentation correction of P100-092.round2.v1. Native values, coefficients, grouping and numerical evidence are unchanged. No new fitting or confirmation.

**Target.** Channel-resolved burst-mean RSSI

**Target units.** dBm

**Metric kind.** mae

**Timing contract.** Only the initial calibration map and known date/furniture/antenna/channel metadata are allowed. Whole dates remain grouped; repeated packets/cells are not independent experiments. Expanded information budget: r0, channel_contrast, position_contrast, spatial_contrast, global_power_reference, local_channel_power_dB, furniture, day, lwa, port, channel

**Calibration.** The complete initial3120-cell measured RSSI map is permitted. Same-position channel, same-channel spatial, global-power and local-channel-power contrasts are calculated from that map, never from target-date RSSI. Fitted corrections and flexible transformations are learned only inside each preceding-date training fold; no target-date RSSI recalibration is permitted.

**Independent unit.** Complete measurement date with all available furniture states, antenna ports and channels;3forward-development validation dates. Rows and dates share one calibrated installation and cannot support independent-row population inference.

**Scope limits.** Repeatedly exposed development OOF cohort comprising complete dates2023-12-05,2023-12-13 and2023-12-20 (source group labels05122023,13122023,20122023),18720 observations. This task does not score the original reserved days51,86,94. All positions are covered by the original3120-cell calibration map in one installation. No unseen-position prediction, reduced calibration-cost result, localization result or independent antenna-efficiency identification is established.

## Permitted inputs

| Input | Units |
|---|---|
| r0 | dBm |
| channel_contrast | dB |
| position_contrast | dB |
| spatial_contrast | dB |
| global_power_reference | dBm; power-domain spatial calibration mean |
| local_channel_power_dB | dBm; power-domain channel calibration mean |
| furniture | binary indicator |
| day | elapsed days |
| lwa | binary indicator for ports P1-P4 |
| port | categorical P1–P8 |
| channel | channel number 37/38/39 |

Current outcomes are exposed. Alternatives may use the same information budget; different endpoints require a distinct reviewed contract.
