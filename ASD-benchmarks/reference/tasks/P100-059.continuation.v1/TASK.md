# P100-059.continuation.v1

**Target.** Hourly produced energy divided by installed capacity

**Units.** kWh/kWp

**Error units.** kWh/kWp

**Primary metric.** mae

**Primary metric units.** kWh/kWp

**Cohort.** P100-059.continuation.v1.cohort-1

**Prediction time.** Same native-clock current weather plus exact previous1/2hour weather; energy response is not predictor. Physical reporting/timezone semantics unresolved.

**Independent unit.** whole city/location

**Hierarchy.** group

**Calibration and history.** Strict past weather history added without shifting energy or provider/timezone assumptions. No plant-specific response calibration.

**Limits.** Six cities, nine plants; plants within a city share weather and are not independent weather sites. Same-hour conditional energy prediction, not weather forecasting or proven thermal causality.

**Historical exposure record.** ALL original confirmation exposed; no fresh confirmation; diagnostics opened only after candidate/stopping freeze; all future evaluations are retrospective

**Current exposure.** All outcomes exposed; future scoring is retrospective.

**Source scope.** original_corpus

**Source.** https://data.mendeley.com/datasets/dbh93b6vp8/3

**Source terms.** CC BY 4.0

## Permitted prediction inputs

| Variable | Unit / interpretation |
|---|---|
| `irradiance` | kW/m^2; supplied weather shortwave radiation |
| `temp_C` | degree C; supplied 2 m temperature |
| `wind` | m/s; supplied 10 m wind converted from km/h |
| `hour` | source-clock hour; no timezone assumed |
| `doy` | calendar day of year |
| `limit` | connection kW / installed kWp |
| `latitude` | degree north |
| `Gpast1` | kW/m2; exact previous native-clock hour supplied radiation |
| `Gpast2` | kW/m2; exact two-hour-past radiation |

Identifiers and source locators are alignment metadata. They may route documented frozen calibration states; they are not a license to look up a scored target. Additional columns outside this list are not predictors.

## Reproduction and comparison

`run.py` and `rules.json` contain executable frozen equations and every coefficient. `evidence/metrics.csv` and `evidence/predictions.csv.gz` preserve the historical comparisons. The shared evaluator recalculates them and compares submitted predictions on identical covered observations. Model IDs are local to this task and are distinct from finding IDs.

Primary aggregation and eligible observations are frozen. Excluded/nonpositive log targets are reported separately from physical-unit error. Uncertainty is described at independent-group level; no row bootstrap is used. The raw adapter emits native anchors, eligibility, calibration and group records. Preparation does not fit or tune a model.

Default reference: `reference`. Comparator models: `reference`, `compact_candidate`, `signed_control`, `geometry`, `lag_response`, `signed_thermal`, `lag_geometry`, `unrestricted_thermal`, `ridge_calendar`, `legacy_reference`.

Use `python evaluation/benchmark.py example --task P100-059.continuation.v1 --output NEW_FOLDER` from the benchmark root. Historical development/confirmation separation cannot be reused as a fresh holdout after exposure.
