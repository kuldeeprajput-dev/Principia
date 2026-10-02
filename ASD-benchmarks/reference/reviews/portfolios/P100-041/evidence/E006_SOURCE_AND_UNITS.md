# Source and units audit — P100-041

Source: https://www.eia.gov/electricity/gridmonitor/about. Redistribution: US government public domain. Native bytes are hash-checked and never modified.

Target: Unimputed hourly balancing-authority demand (MW). Inputs: forecast [MW]; error48 [MW]; error168 [MW]; load48 [MW]; load168 [MW]; ramp [MW]; hour [UTC hour]; weekend [indicator].

Retrospective published-snapshot forecast correction. Input official forecast for target hour, preceding-hour forecast, and actual/forecast residuals 48 and168 hours before target. Nominal issuance t−24h is an analysis convention, not observed release timestamp. Inputs at least24h older than nominal issuance; exact publication and revision vintages unavailable. No target-hour demand, generation or interchange predictor.

Authority-month groups; rolling train Jan–Feb->March, Jan–March->April, Jan–April->May. June confirmation. Same authorities across time, correlated national weather; no independence claim across all authorities.

Unimputed native Demand/Forecast only. Revised final public snapshot is not an as-issued operational backtest. Negative/nonfinite demand/forecasts excluded by validity rule before fitting. Primary MW MAE is not normalized by authority load.

Exposure: Schema-stage first row of original table inspected. First row belongs to January development. No June targets/scores inspected.

Every output retains exact native row or NetCDF profile/level anchors. Missing/invalid measurements are excluded explicitly; none are imputed. Quality-screening defines the task, not claimed population coverage. No scientific source values are rewritten.
