# Frozen scoring cohort

Hourly produced energy divided by installed capacity (kWh/kWp). Independent unit: whole city/location. Native measured energy is divided by independently supplied installed power; source specific-energy and avoided-CO2 columns are excluded. Weather provider/provenance and timezone are unresolved, so the case is mixed measured/author-supplied weather. Daylight cohort fixed by input irradiance >20 W/m^2; no target-based filtering. Missing native energy retained as missing targets. All nine plants and all years retained subject to declared daylight availability.

Contemporaneous weather and calendar/plant metadata only; no target energy, source specific-energy or emissions as inputs.

inputs.csv.gz contains IDs and permitted predictors only; observations.csv.gz contains the corresponding measured/author-derived target. Native anchors are in native_anchors.csv.gz; source hashes are in SOURCE_ASSETS.json. Missing native targets remain missing and cannot be manufactured into zeros. Startup calibration for the gearbox is explicitly unscored. All targets are now exposed for future agents. Six cities, nine plants; plants within a city share weather and are not independent weather sites. Same-hour conditional energy prediction, not weather forecasting or proven thermal causality.
