# Source and units audit — P100-038

Source: https://zenodo.org/records/16673883. Redistribution: CC-BY-4.0. Native bytes are hash-checked and never modified.

Target: First reported RSRP-vector component at first recorded point 1.0–1.6 s after issuance (dBm). Inputs: last [dBm]; mean5 [dBm]; mean20 [dBm]; slope [dB/s]; spread [dB]; elapsed [s].

At a recorded RSRP sample, use only component 1 in the native comma-separated RSRP vector over the preceding 20 seconds. Predict first subsequently recorded component-1 value at 1.0–1.6 s. First qualifying issuance per target; no actual future horizon feature in predictor. Unknown component antenna/beam semantics prevent propagation-law claims.

Entire flight; forward folds 1->2,1–2->3,1–3->4; flight5 confirmation. Same installation/day only.

Telemetry files1–2 do not overlap the radio clock windows and contain repeated headers; no invented offset or geometry pairing. Vector component ordering is taken literally, not identified as a specific antenna.

Exposure: Schema inspection: first two finite RSRP records of flight1 and source first telemetry rows; no flight5 RSRP values or scores printed.

Every output retains exact native row or NetCDF profile/level anchors. Missing/invalid measurements are excluded explicitly; none are imputed. Quality-screening defines the task, not claimed population coverage. No scientific source values are rewritten.
