# BLS CPI/CES source and units

Six explicitly named national seasonally adjusted series are parsed from native tab-separated bulk files. CPI series are AllItems CUSR0000SA0, Housing CUSR0000SAH, MedicalCare CUSR0000SAM. CES series are employment CES0000000001, CES3000000001, CES5000000001 (thousands of persons). Annual M13 records are excluded. Exact monthly log growth100ln(level_t/level_(t-1)) removes arbitrary CPI base and employment level units; percentage-point errors remain interpretable. The target is the next monthly CPI growth, never an accounting sum of sector components.

No values are imputed. Complete calendar lags are required, including12previous CPI months. Original raw files remain unchanged. CPI seasonal revisions and CES annual benchmarks mean these are revised snapshots with future-informed processing. Calendar-causal code is not a real-time-vintage backtest. Employment changes are descriptive covariates, not unemployment gaps or causal cost pressure. All development and confirmation dates are predefined before fitting; only metadata were exposed in schema inspection.

Source prior art includes conventional inertial inflation forecasts and Phillips-curve/activity relationships. The selected data do not identify exogenous policy shocks or a structural inflation equation. Claims must be scoped to retrospective forecast comparison and preserved failures.
