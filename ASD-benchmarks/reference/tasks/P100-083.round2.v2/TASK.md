# P100-083.round2.v2

Documentation correction of P100-083.round2.v1. Native values, coefficients, grouping and numerical evidence are unchanged. No new fitting or confirmation.

**Target.** One-hour future internal sensor temperature

**Target units.** degree C

**Metric kind.** rmse

**Timing contract.** At each eligible hourly origin, predict internal temperature nominally one hour ahead using current and causal earlier internal/external temperatures, external humidity, source-clock phase and calibrated stream identity. Origin/lag/target matching retains the native rules: origin in first15minutes, causal one-hour lags within15minutes, target within5minutes and same calendar day; no response interpolation. This task scores three forward development blocks per stream, not the latest20percent original reserved dates.

**Calibration.** Five sensor-stream identities are calibrated using only the preceding training blocks for each outer fold. All coefficients and transformations are frozen per fold in the referenced states. The current weather-increment candidate uses internal/external temperature changes plus stream and clock terms. Numerical offsets and coefficients of the original static-gradient reference belong only to their historical comparator state; they are not a universal calibration rule for this task.

**Independent unit.** Complete forward native-date block within each calibrated sensor stream;15 validation groups across5streams and3forward folds,4111 scored observations. Streams share one apiary and are not independent sites.

**Scope limits.** Repeatedly exposed original-development OOF cohort. The latest20percent original reserved dates are excluded from this cohort. Sensor placement, colony/species and season remain confounded; no unseen-apiary, colony-health, physiological setpoint or identified heat-conductance claim.

## Permitted inputs

| Input | Units |
|---|---|
| T_now | degC |
| T_lag | degC,causal lag1h |
| T_external | degC,current |
| T_external_lag | degC, causal lag 1 h |
| RH_external | percent,current |
| hour_sin | dimensionless source-clock phase |
| hour_cos | dimensionless source-clock phase |
| stream | calibrated sensor label |

Current outcomes are exposed. Alternatives may use the same information budget; different endpoints require a distinct reviewed contract.
