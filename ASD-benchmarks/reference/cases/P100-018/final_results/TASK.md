# P100-018.original.v1

**Target.** Log transformed reported tornado property-damage estimate

**Target units.** ln(1+property damage in USD)

**Metric kind.** mae

**Timing contract.** Post-event path and timing diagnostic of reported loss. EF damage-derived scale, casualty counts, narratives, monetary/crop losses excluded from predictors.

**Calibration.** Whole EPISODE_ID groups held; no held-event monetary outcomes. Linked tornado segments within episode remain together.

**Independent unit.** NOAA EPISODE_ID outbreak groups; nearby episodes may still be correlated or linked across offices. Not individual property samples.

**Scope limits.** 2025 tornado segments with nonmissing explicit damage. Broad estimates including reported0, not insured claim totals. Maximum width times length is bounding footprint proxy, not actual damaged area. Exposure/building stock and wind speed unavailable; no prospective loss or causal damage law.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| length_km | km path length |
| width_km | km maximum path width |
| duration_min | minutes event duration |
| latitude | degrees north |
| month | calendar1–12 |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-018.original.v1 --output NEW_SUBMISSION; then score --task P100-018.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
