# P100-046: Local electron-temperature closure

## Scenario and question

The retained MMS1 data contain clean electron moments and backward-matched clean magnetic-field samples. Ion moments are excluded because their error flags are nonzero. Four chronological20-minute blocks support development and the last two support confirmation.

Can double-adiabatic or polytropic electron-temperature closures explain local evolution beyond lag persistence?

## Experimental contract

Diagnostic closure using current electron density and magnetic-field magnitude plus electron temperature/density/field measured at least60s earlier; current temperature and tensor-derived equivalents forbidden. Causal60-second-old electron state, same information for every model. Magnetic matching backward only.

The campaign completed 5 substantive hypotheses. Native bytes and exact sample anchors are preserved. Model selection uses whole-group development error and a1% simplicity tolerance; selection and stopping were frozen before the separate no-fitting confirmation process. All outcomes are now exposed for future users.

## Main result and interpretation

A two-exponent local closure using density and field ratios improves confirmation error over persistence, fixed CGL scaling and the nonlinear control. The fitted density exponent is negative. That is a local empirical association along a spacecraft trajectory, not an independently identified thermodynamic polytropic index.

$$
\widehat T_\perp=T_0\exp\!\left[\operatorname{clip}\!\left(a\log(n/n_0)+b\log(B/B_0),-5,5\right)\right]
$$

The exact executable expression is: T_hat=T0*exp(clip(a*ln(n/n0)+b*ln(B/B0),-5,5)).

Parameters: b[0] = -0.2867018361; b[1] = 0.4474892625. Coefficient ordering follows run.py and rules.json.

T0 is the permitted earlier perpendicular temperature in eV; n/n0 and B/B0 are dimensionless ratios. The60-second anchor and backward field timestamps are recorded per observation.

## Performance and adverse evidence

| Model | Development MAE | Confirmation MAE |
|---|---:|---:|
| attempt 003 | 1.86833 | 1.17416 |
| cgl | 1.91511 | 1.45494 |
| rbf | 2.27377 | 1.32057 |

MAE is averaged within each complete group and then equally over the 2 reserved groups (533 observations). Errors are in eV. Per-group RMSE, bias and failures are available in evidence/by_group.csv; small or dependent group counts do not support population confidence claims.

The lowest retrospective confirmation error belongs to attempt 001. It did not change the frozen selection. Anisotropy relaxation is within the simplicity tolerance and beta-regime modulation worsens forward-block development; neither receives mechanistic admission.

## Value, limits and evaluation

The calibrated form preserves the initial temperature when both ratios equal one. It supplies an interpretable conditional closure test; anisotropy relaxation adds negligible development value and beta-dependent modulation worsens transfer. Current density and magnetic field are allowed, so this is a contemporaneous closure rather than future-state forecasting. Eulerian spacecraft samples are not tracked fluid parcels. Two held blocks and one orbit segment do not establish a universal plasma law.

Alternative agents can submit any predictor under this task's information budget. The shared evaluator reports physical-unit errors, whole-group and worst-group results, coverage, abstention, optional intervals and meaningful event diagnostics. A different endpoint requires an independently reviewed new-task contract. Numerical success alone does not certify mechanism, novelty or deployed impact.

## Reproducibility and source

Run `python run.py` for the frozen reference replay. `rules.json` contains every fitted value; `task_spec.json` defines units and access; `evidence/` contains compact predictions and numerical evidence. Research history preserves all hypotheses, failed candidates, technical corrections and the first confirmation receipt.

Authoritative source: https://spdf.gsfc.nasa.gov/pub/data/mms/mms1/. Redistribution terms: CC0 per NASA SPDF data-use policy. Primary-source prior-art searches and limitations are recorded in PRIOR_ART.json.
