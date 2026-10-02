# Native source and information audit

Calibrated Src biosensor fluorescence trajectories

Predict all t>7.5 min from source dose and same-curve measurements at 3,4.5,6 min. Calibration fixed at6 min; no later response access.

Complete dose curves; seven development and two hash-selected confirmation doses; leave-one-dose-out validation. No biological replicate identifiers.

First9 lines and schemas inspected; early values through6.75 min were visible across doses, outside target window. Later outcomes not printed before freeze.

- One source assay, source units are not enzyme concentration or clinical activity.
- Kinetic export lacks raw triplicate labels. Dose validation is not independent biological replication.
- Akt1 response copying time is excluded; source fitted velocity tables are never targets.

All consumed source hashes are in SOURCE_MANIFEST.json. Source instrument exports are author-calibrated/processed; no original bytes are changed. Native anchors and eligibility reasons accompany every observation. Repetitions and calibration measurements are not additional independent groups.
