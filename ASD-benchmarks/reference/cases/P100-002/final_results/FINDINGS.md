# P100-002: Short-horizon stellar-flux response

## Scenario and question

Eight stars from the source TARS sector 96 product provide hourly medians of author-corrected relative flux. Six stars are used for development and two accession-hash-selected stars for confirmation. Each forecast uses 24 preceding hourly bins.

Does a damped local dynamical model transfer between stars better than persistence?

## Experimental contract

Predict next disjoint hourly bin using preceding observed hourly medians only. The released light curve was author-corrected using full-sector information; this is a retrospective product-space forecast, not a raw real-time pipeline. Causal observed flux history within each star; no fitted header period or future light curve values.

The campaign completed 5 substantive hypotheses. Native bytes and exact sample anchors are preserved. Model selection uses whole-group development error and a 1% simplicity tolerance; selection and stopping were frozen before the separate no-fitting confirmation process. All outcomes are now exposed for future users.

## Main result and interpretation

The selected two-term local response improves one-hour-ahead error over persistence and the constrained nonlinear comparator. Its negative slope coefficient damps the latest increment. That is consistent with short-timescale measurement fluctuations or mean reversion; it does not identify a physical rotation frequency or prove an oscillation mechanism.

$$
\widehat F_t=F_{t-1}+a(F_{t-1}-F_{t-2})+b(F_{t-1}-2F_{t-2}+F_{t-3})
$$

The exact executable expression is: F_hat=F1+a*(F1-F2)+b*(F1-2*F2+F3).

Parameters: b[0] = -0.9526276663; b[1] = 0.3080708902. Coefficient ordering follows run.py and rules.json.

## Performance and adverse evidence

| Model | Development MAE | Confirmation MAE |
|---|---:|---:|
| attempt 003 | 0.00296967 | 0.000865191 |
| persist | 0.00358913 | 0.00102924 |
| rbf | 0.00342515 | 0.000907603 |

MAE is averaged within each complete group and then equally over the 2 reserved groups (981 observations). Errors are in relative flux (native normalization). Per-group RMSE, bias and failures are available in evidence/by_group.csv; small or dependent group counts do not support population confidence claims.

The lowest retrospective confirmation error belongs to attempt 004. It did not change the frozen selection. Volatility gating and longer-timescale relaxation fail to improve the selected local response during development; some score better after confirmation and remain exposed diagnostic alternatives.

## Value, limits and evaluation

The result is useful for conditional prediction in this already corrected product. Full-sector author correction is part of the input lineage, so this is not a demonstration of raw online telescope forecasting. Two stars do not establish population-level precision. Later diagnostic candidates score better on confirmation but were not promoted. No period estimated from the full sector is a predictor.

Alternative agents can submit any predictor under this task's information budget. The shared evaluator reports task-unit errors, whole-group and worst-group results, coverage, abstention, optional intervals and meaningful event diagnostics. A different endpoint requires an independently reviewed new-task contract. Numerical success alone does not certify mechanism, novelty or deployed impact.

## Reproducibility and source

Run `python run.py` for the frozen reference replay. `rules.json` contains every fitted value; `task_spec.json` defines units and access; `evidence/` contains compact predictions and numerical evidence. Research history preserves all hypotheses, failed candidates, technical corrections and the first confirmation receipt.

Authoritative source: https://archive.stsci.edu/hlsp/tars. Redistribution terms: CC BY 4.0. Primary-source prior-art searches and limitations are recorded in PRIOR_ART.json.
