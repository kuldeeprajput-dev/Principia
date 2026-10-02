# P100-003: Recorded interferometer band-power stability

## Scenario and question

One4096-second H1 strain segment is summarized with nonoverlapping16-second Welch windows. Four past windows predict the next30–80Hz RMS. Six512-second blocks are development and the final two are confirmation.

Is local strain-band noise stationary, mean reverting or driven by coupled bands?

## Experimental contract

Only earlier16-second strain summaries used. Quality masks applied to entire predictor and target windows; no centered filters or future PSD. Four preceding16-second windows; training-only global coefficients.

The campaign completed 5 substantive hypotheses. Native bytes and exact sample anchors are preserved. Model selection uses whole-group development error and a1% simplicity tolerance; selection and stopping were frozen before the separate no-fitting confirmation process. All outcomes are now exposed for future users.

## Main result and interpretation

None of the five proposed relaxation, cross-band or robust-response extensions beats the stationary training median during forward development. The retained reference also loses modestly to several controls on the final blocks. These adverse outcomes are part of the result.

$$
\widehat R_t=\operatorname{median}_{\mathrm{development}} R
$$

The exact executable expression is: y_hat = training-fold median(target); final coefficient refit on development only.

Parameters: b[0] = 0.08835148233. Coefficient ordering follows run.py and rules.json.

## Performance and adverse evidence

| Model | Development MAE | Confirmation MAE |
|---|---:|---:|
| constant | 0.0101815 | 0.00855538 |
| median4 | 0.0111483 | 0.00842009 |
| rbf | 0.0124075 | 0.00821495 |

MAE is averaged within each complete group and then equally over the 2 reserved groups (64 observations). Errors are in 10^-21 strain. Per-group RMSE, bias and failures are available in evidence/by_group.csv; small or dependent group counts do not support population confidence claims.

The lowest retrospective confirmation error belongs to attempt 004. It did not change the frozen selection. Cross-band regressors and robust-response additions fail the development comparison. Final results also fail to establish superiority of the selected stationary baseline.

## Value, limits and evaluation

The primary contribution is a bounded negative result and a quality-mask correction: the entire segment carries a continuous-wave hardware injection. Recorded band power cannot be relabeled uncontaminated detector noise or astrophysical evidence. All data come from one short segment. The DATA bit and declared injection bits are required; other quality bits are retained rather than silently asserted clean. No injection/noise decomposition is identified.

Alternative agents can submit any predictor under this task's information budget. The shared evaluator reports physical-unit errors, whole-group and worst-group results, coverage, abstention, optional intervals and meaningful event diagnostics. A different endpoint requires an independently reviewed new-task contract. Numerical success alone does not certify mechanism, novelty or deployed impact.

## Reproducibility and source

Run `python run.py` for the frozen reference replay. `rules.json` contains every fitted value; `task_spec.json` defines units and access; `evidence/` contains compact predictions and numerical evidence. Research history preserves all hypotheses, failed candidates, technical corrections and the first confirmation receipt.

Authoritative source: https://gwosc.org/O4/O4a/. Redistribution terms: CC BY 4.0. Primary-source prior-art searches and limitations are recorded in PRIOR_ART.json.
