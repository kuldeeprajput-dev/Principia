# Electricity demand: combining recent and weekly forecast-error memory

**P100-041 · Source-aware scientific reference.** Supported as a scoped predictive extension; novelty and demonstrated industrial impact are not established.

## Scenario and measured endpoint

Unimputed hourly balancing-authority demand in MW. Retrospective published-snapshot forecast correction. Input official forecast for target hour, preceding-hour forecast, and actual/forecast residuals 48 and168 hours before target. Nominal issuance t−24h is an analysis convention, not observed release timestamp. Inputs at least24h older than nominal issuance; exact publication and revision vintages unavailable. No target-hour demand, generation or interchange predictor.

Authority-month groups; rolling train Jan–Feb->March, Jan–March->April, Jan–April->May. June confirmation. Same authorities across time, correlated national weather; no independence claim across all authorities. Development contains 181,474 eligible observations in 265 groups. Confirmation contains 37,889 eligible observations in 53 groups. Unimputed native Demand/Forecast only. Revised final public snapshot is not an as-issued operational backtest. Negative/nonfinite demand/forecasts excluded by validity rule before fitting. Primary MW MAE is not normalized by authority load.

## Findings and executable relation

Complementary recent and weekly forecast errors provide a compact bias-transport correction. The mechanism is persistent forecasting/operating context, not electrical power-balance identity. Retrospective error reduction does not demonstrate dispatch cost, reliability or causal industrial impact.

The reference selected before confirmation is `attempt-008`:

$$
\widehat D_t=F_t+a\,(D_{t-48h}-F_{t-48h})+b\,(D_{t-168h}-F_{t-168h})
$$

D and F are native unimputed demand and official demand forecast (MW). a and b are dimensionless robust development-fitted weights. The two historical residuals are at least24h older than the nominal t−24h issuance convention. Forecast snapshots may contain revisions; exact original publication timestamps are unavailable.

| Coefficient | Exact fitted value |
|---|---:|
| a | 0.4974490504629177 |
| b | 0.3525440289648312 |

All numerical constants, transformations, alternative equations and fitted coefficients are executable in `run.py` and serialized in `rules.json`. Any algebraic consequence of this equation is an implication of the same fitted model, not a second independently validated finding.

## Experimental method and evidence

10 substantive development attempts tested competing representations, controls and ablations. Fits use equal-group weighted least squares or declared robust loss, with all coefficients and radial-basis centers learned only inside each training fold. Selection minimizes mean group MAE, preferring fewer coefficients within1% of the minimum. Separate confirmation checks the frozen states and performs no fitting. Baselines share permitted information.

Primary errors are in MW; each group contributes equally regardless of row count.

| Frozen model | Development MAE | Confirmation MAE | Worst confirmation group |
|---|---:|---:|---:|
| reference | 215.716 | 283.872 | 2274.46 |
| flexible | 344.508 | 569.108 | 4742.24 |
| official | 337.849 | 464.341 | 4293.15 |
| residual48 | 247.569 | 323.862 | 2813.04 |
| weekly | 627.461 | 1005.93 | 11294.9 |
| attempt-001 | 254.819 | 331.817 | 2929.84 |
| attempt-002 | 227.967 | 296.154 | 2457.33 |
| attempt-003 | 331.767 | 452.411 | 4176.67 |
| attempt-004 | 232.272 | 301.764 | 2452.72 |
| attempt-005 | 240.255 | 306.017 | 2457.33 |
| attempt-006 | 215.836 | 283.972 | 2273.22 |
| attempt-007 | 227.501 | 295.69 | 2449.59 |
| attempt-008 | 215.716 | 283.872 | 2274.46 |
| attempt-009 | 235.551 | 310.679 | 2722.07 |
| attempt-010 | 244.212 | 329.406 | 2627.81 |

The frozen reference changes confirmation MAE by 12.3% relative to the strongest evaluated baseline `residual48` (323.862MW); it wins on 50/53 whole groups. This is descriptive, not a population significance test. Rows within runs, days, weeks, profiles or casts are dependent. The complete group errors, bias, RMSE and90th-percentile errors are in `evidence/by_group.csv`.

## Falsification, limits and value

- Multiplicative-response fitting is not interchangeable with physical-MW error optimization.
- The development-selected correction is a retrospective forecasting extension, not a new conservation law or an as-issued operational trial.
- Report whole-group errors and ranges; no independent-row population CI. Temporal/spatial dependence and small number of sites/floats limit inference.
- Public data and known physical parameterizations preclude automatic novelty certification. Predictive accuracy does not establish an industrial intervention or a new physical law.

Use the existing official forecast as a strong baseline and respect actual publication delays. Physical-unit validation exposes failures that relative-error fitting can conceal. Retain a simpler model when diurnal terms add no meaningful evidence.

## Reproduction and future evaluation

Run `python run.py` in this folder to verify allowlisted hashes and reproduce every saved confirmation prediction. This executes trusted bundled reference code; scoring an external prediction file should use the shared Principia evaluator without executing submitted code. Numerical alternatives need not resemble this equation. Use the exact registered task, timing/input budget, units, eligibility and group weighting. New endpoints or information access require a separately reviewed task version.

All confirmation outcomes are now exposed to future users. Source-stage exposure is recorded in `task_spec.json`; the first-use internal freeze history is preserved in research history. Independent source data are needed for a new confirmation campaign.

## Primary sources and existing analyses

- [https://www.eia.gov/opendata/browser/electricity/rto/region-sub-ba-data](https://www.eia.gov/opendata/browser/electricity/rto/region-sub-ba-data) — Official EIA dashboard describes hourly actual/day-ahead forecast demand and interchange. Forecast error correction is an established statistical operation; the source offers no as-issued revision archive in this local bundle.
- [https://www.eia.gov/outlooks/aeo/nems/documentation/electricity/pdf/EMM_AEO2025.pdf](https://www.eia.gov/outlooks/aeo/nems/documentation/electricity/pdf/EMM_AEO2025.pdf) — EIA-930 collects balancing-authority operating data. Final snapshots must not be represented as immutable real-time information availability.
