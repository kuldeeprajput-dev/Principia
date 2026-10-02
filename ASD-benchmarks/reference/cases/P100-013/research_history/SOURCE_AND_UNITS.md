# Source and units audit — NIST encapsulant cure

Source: https://data.nist.gov/od/id/mds2-3702. Native assets are checked against SOURCE_MANIFEST.json before parsing.

Target: conversion (1). Predictors: temperature_K (K), heating_rate_K_min (K/min).

Predict author-observed DSC conversion from temperature and imposed constant heating rate; no target history.

Source-fitted conversion excluded. Four development traces; one high-rate extrapolation confirmation. Audit exposed first four rows near zero of every trace.

Author-derived fitted columns, fracture toughness values and outcome class labels are never predictors. Source data are publicly exposed; campaign confirmation is internally withheld only. No cross-population inference.
