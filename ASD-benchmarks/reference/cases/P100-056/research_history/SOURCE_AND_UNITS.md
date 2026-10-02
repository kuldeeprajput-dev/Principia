# Source and units audit — Timber-concrete beam response

Source: https://zenodo.org/records/17967735. Native assets are checked against SOURCE_MANIFEST.json before parsing.

Target: applied force (kN). Predictors: deflection_mm (mm), calibration_deflection_mm (mm), calibration_force_kN (kN), initial_stiffness_kN_mm (kN/mm), recent_stiffness_kN_mm (kN/mm), lightweight (1).

Given current imposed displacement, concrete class, and beam-specific initial force-displacement calibration prefix through≤10mm; no later force or failure capacity allowed.

Four development beams and two confirmation beams. Header audit exposed confirmation first11points (all below10mm); these are permitted calibration only. All late damage rows retained.

Author-derived fitted columns, fracture toughness values and outcome class labels are never predictors. Source data are publicly exposed; campaign confirmation is internally withheld only. No cross-population inference.
