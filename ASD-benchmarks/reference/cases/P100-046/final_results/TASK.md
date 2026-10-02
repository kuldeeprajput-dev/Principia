# P100-046.original.v1

**Target.** Electron perpendicular temperature

**Target units.** eV

**Metric kind.** mae

**Timing contract.** Diagnostic closure using current electron density and magnetic-field magnitude plus electron temperature/density/field measured at least60s earlier; current temperature and tensor-derived equivalents forbidden.

**Calibration.** Causal60-second-old electron state, same information for every model. Magnetic matching backward only.

**Independent unit.** Contiguous20-minute blocks in one MMS1 passage, not independent spacecraft or experiments

**Scope limits.** One2-hour MMS1 interval. All ion moments have qualityflag66 (saturation plus highMach); ion targets excluded before any fit. Electron flags0 and FGMflags0 retained. Moment errors and unmeasured heat flux/geometry limit CGL interpretation.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| temperature_lag | eV |
| density_ratio | dimensionless n(t)/n(t-60s) |
| field_ratio | dimensionless B(t)/B(t-60s) |
| density_lag | cm^-3 |
| field_lag | nT |
| anisotropy_lag | dimensionless T_parallel/T_perpendicular |
| elapsed_lag_s | s |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-046.original.v1 --output NEW_SUBMISSION; then score --task P100-046.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
