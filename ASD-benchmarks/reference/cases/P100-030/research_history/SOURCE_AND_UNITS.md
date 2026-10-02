# Source and units audit: P100-030

Calibrated low-speed lubricant friction. Native bytes are hash-verified by native.py. Primary publication: https://www.sciencedirect.com/science/article/pii/S0301679X26007504.

Endpoint: Coefficient of friction, dimensionless. Inputs: speed_mm_s (mm/s), boundary_cof (dimensionless), highspeed_cof (dimensionless), concentration_wt_pct (wt percent).

Material formulation, repeated representations linked. Two-point calibration at 0.2 and500 mm/s; score0.28–10 mm/s.

Two exact endpoint friction measurements at0.2 and500mm/s on the same curve; endpoint rows excluded from scored set.

Public source-aware corpus; source plots and published analyses known. Schema previews exposed first rows only. Case30 speeds>=13.9mm/s previewed; scored0.28–10mm/s unviewed. Case22 initial~0.006V row previewed; targetV>=0.05V unviewed. Case65 10Hz first rows previewed; scoref>=100Hz. Reserved response distributions and scores unopened.

## Native semantics, prior processing and limitations

Three CoF CSVs include concentration, functionalization andsupplier curves at550MPa, steel100Cr6 againstBK7 glass, SRR=-20percent andapproximately26C. Fixed25 speed coordinates0.2–500mm/s are measured CoF traces. We retain9 unique curves across8 formulationgroups: exact PEG/pure duplicated representations are removed, while the different functionalization-series pure curve remains in the sameP5group. The fitting target0.28–10mm/s was not previewed; high-speed samples>=13.9mm/s were exposed during schema review. Calibration at0.2 and500mm/s is deliberately available for every unseen curve, so this is curve reconstruction under a two-point calibration budget, not prediction of an untested lubricant. Surface treatment/supplier identities group observations but are not predictors; endpoints and concentration are. Known source analyses already describe particle-size, agglomeration, functionalization and friction-reduction percentages. Do not recast those as novel. Particle concentrations, load, temperature and source selectivity constrain transfer; independent repeat uncertainty is unavailable. Source metadata have inconsistent release/deposit/publication dates; no corrected chronology is invented.
