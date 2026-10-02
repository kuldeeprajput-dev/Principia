# P100-059.original.v1

**Target.** Hourly produced energy divided by installed capacity

**Units.** kWh/kWp

**Error units.** kWh/kWp

**Primary metric.** mae

**Primary metric units.** kWh/kWp

**Cohort.** P100-059.original.v1.cohort-1

**Prediction time.** Contemporaneous weather and calendar/plant metadata only; no target energy, source specific-energy or emissions as inputs.

**Independent unit.** whole city/location

**Hierarchy.** group

**Calibration and history.** Native measured energy is divided by independently supplied installed power; source specific-energy and avoided-CO2 columns are excluded. Weather provider/provenance and timezone are unresolved, so the case is mixed measured/author-supplied weather. Daylight cohort fixed by input irradiance >20 W/m^2; no target-based filtering. Missing native energy retained as missing targets. All nine plants and all years retained subject to declared daylight availability.

**Limits.** Six cities, nine plants; plants within a city share weather and are not independent weather sites. Same-hour conditional energy prediction, not weather forecasting or proven thermal causality.

**Historical exposure record.** All packaged targets are exposed for future agents; future scoring is retrospective. Public source-aware corpus. Illustrative header/first-row values were inspected during the semantics audit; these do not constitute blind source acquisition. All delivered targets become exposed after confirmation.

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

Identifiers and source locators are alignment metadata. They may route documented frozen calibration states; they are not a license to look up a scored target. Additional columns outside this list are not predictors.

## Reproduction and comparison

`run.py` and `rules.json` contain executable frozen equations and every coefficient. `evidence/metrics.csv` and `evidence/predictions.csv.gz` preserve the historical comparisons. The shared evaluator recalculates them and compares submitted predictions on identical covered observations. Model IDs are local to this task and are distinct from finding IDs.

Primary aggregation and eligible observations are frozen. Excluded/nonpositive log targets are reported separately from physical-unit error. Uncertainty is described at independent-group level; no row bootstrap is used. The raw adapter emits native anchors, eligibility, calibration and group records. Preparation does not fit or tune a model.

Default reference: `reference`. Comparator models: `reference`, `mechanistic_reference`, `attempt_001`, `attempt_002`, `attempt_003`, `attempt_004`, `attempt_005`, `attempt_006`, `attempt_007`, `baseline_mean`, `baseline_domain`, `baseline_rbf`, `attempt_008`, `attempt_009`.

Use `python evaluation/benchmark.py example --task P100-059.original.v1 --output NEW_FOLDER` from the benchmark root. Historical development/confirmation separation cannot be reused as a fresh holdout after exposure.
