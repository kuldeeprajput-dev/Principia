# Frozen scoring cohort

Author-extracted cyclist speed one second ahead (m/s). Independent unit: whole original video, all parts/participants. Source computer-vision/Kalman trajectories, 25 Hz; select every 25th frame and exact +/-25-frame pairs. Parts of the same original video remain together. Track IDs may be ambiguous; all 28 riders recur across videos. Source preprocessing may use future smoothing, so predictions are retrospective trajectory dynamics and not certified online safety. Angular-neighbor interaction is a testable approximation; lateral separation and direction reversal are falsifiers.

Only current and past extracted speeds and current geometry/neighbor state. Future target speed is inaccessible to candidate replay.

inputs.csv.gz contains IDs and permitted predictors only; observations.csv.gz contains the corresponding measured/author-derived target. Native anchors are in native_anchors.csv.gz; source hashes are in SOURCE_ASSETS.json. Missing native targets remain missing and cannot be manufactured into zeros. Startup calibration for the gearbox is explicitly unscored. All targets are now exposed for future agents. One controlled circular-track session, recurring riders; no new-rider, on-road safety or crash-prevention transfer claim.
