# P100-045: Count-space spectral response in a gamma-ray burst

## Scenario and question

Twelve NaI detectors from GRB 250206827 contribute native CTIME spectra. Fixed one-second bins in the first 100 seconds are retained with declared quality and exposure criteria. Two detectors are reserved; all observe the same event. Backgrounds use only the interval from -200 to -100 seconds.

Does a common count-space hardness response transfer across detector orientations and burst phases?

## Experimental contract

Same-bin channels 2+3 count rates and previous-bin low-energy rate permitted; target channel 4 observations after trigger forbidden as predictors. The pretrigger interval from -200 to -100 s background rate in each low/high channel; instrument-specific energy edges recorded.

The campaign completed 5 substantive hypotheses. Native bytes and exact sample anchors are preserved. Model selection uses whole-group development error and a 1% simplicity tolerance; selection and stopping were frozen before the separate no-fitting confirmation process. All outcomes are now exposed for future users.

## Main result and interpretation

A power response of high-channel excess to low-channel excess improves transfer over fixed hardness, background-ratio and flexible controls. The exponent describes detector count-space hardening across this event, not a deconvolved photon spectrum.

$$
\widehat H=\max\!\left(0,B_H+1000a\,\operatorname{sgn}(z)|z|^b\right)
$$

The exact executable expression is: H_hat=max(0, B_H+1000*a*sign(z)*abs(z)^b); z=(L-B_L)/1000.

Parameters: b[0] = 0.8565904676; b[1] = 1.375998282. Coefficient ordering follows run.py and rules.json.

H and L are high-channel and combined low-channel count rates; B_H and B_L are pretrigger backgrounds. The dimensionless excess is z=(L-B_L)/(1000 counts/s). The coefficient a and exponent b are dimensionless.

## Performance and adverse evidence

| Model | Development MAE | Confirmation MAE |
|---|---:|---:|
| attempt 002 | 14.2649 | 22.088 |
| background ratio | 15.491 | 23.7119 |
| rbf | 18.7266 | 34.0513 |

MAE is averaged within each complete group and then equally over the 2 reserved groups (200 observations). Errors are in counts/s. Per-group RMSE, bias and failures are available in evidence/by_group.csv; small or dependent group counts do not support population confidence claims.

The lowest retrospective confirmation error belongs to attempt 002. It did not change the frozen selection. The proposed saturation scale is not identified within the parameter range; reaching its upper bound is evidence against interpreting this fit as measured detector saturation.

## Value, limits and evaluation

The result can serve as a compact calibrated count-response reference. Saturation is not identified: its fitted scale reaches the upper bound. Added lag hysteresis and channel-edge correction do not improve development transfer. Detectors share one incident burst and differ in response and orientation. No independent-event replication, dead-time correction claim or universal hardness-intensity law follows.

Alternative agents can submit any predictor under this task's information budget. The shared evaluator reports task-unit errors, whole-group and worst-group results, coverage, abstention, optional intervals and meaningful event diagnostics. A different endpoint requires an independently reviewed new-task contract. Numerical success alone does not certify mechanism, novelty or deployed impact.

## Reproducibility and source

Run `python run.py` for the frozen reference replay. `rules.json` contains every fitted value; `task_spec.json` defines units and access; `evidence/` contains compact predictions and numerical evidence. Research history preserves all hypotheses, failed candidates, technical corrections and the first confirmation receipt.

Authoritative source: https://heasarc.gsfc.nasa.gov/FTP/fermi/data/gbm/triggers/2025/bn250206827/current/. Redistribution terms: Public domain; Fermi/HEASARC acknowledgment. Primary-source prior-art searches and limitations are recorded in PRIOR_ART.json.
