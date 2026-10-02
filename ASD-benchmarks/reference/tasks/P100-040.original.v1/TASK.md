# P100-040.original.v1

**Target.** Recorded completed-trip duration conditional on recorded trip distance

**Target units.** minutes

**Metric kind.** mae

**Timing contract.** Trip distance is recorded after the journey. Task is retrospective travel-time diagnostics with completed distance, not pickup-time ETA. Pickup time and endpoint categories are known; no fare/payment/duration-derived predictors.

**Calibration.** Forward training on earlier whole days. Jan–Sepdevelopment,Oct–Decconfirmation. Same city/provider system; no future-day targets enter coefficients. Fixed clock windows, no held tuning.

**Independent unit.** Whole pickup calendar days; serial weather/traffic/vendor dependence persists. Forward month blocks, not random trips.

**Scope limits.** Green-taxi2025 declared routine records, duration0–24h and distance0–1000km; known officialzones and source-month-consistent timestamps. Provider-reported records may contain errors; no congestion intervention, routing policy or achieved operational benefit.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| distance_km | recorded post-trip miles*1.609344 |
| hour | pickup local clock hour including fraction |
| weekend | Saturday/Sunday binary |
| peak | fixed7–10 or16–19localclock binary |
| airport | either endpoint in official JFK/LGA/Newark zones |
| manhattan | either endpoint boroughManhattan |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-040.original.v1 --output NEW_SUBMISSION; then score --task P100-040.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
