# Photovoltaics: stable report-window rule, thermal ambiguity

## Scenario and practical question

Nine Coopérnico photovoltaic plants in six Portuguese cities provide hourly measured energy from 2019–2022, independent installed/connection capacities and supplied weather. Five cities are development groups; Loule is an exposed diagnostic. The input-defined daylight cohort uses radiation>20 W/m² and retains missing energy. Target energy/installed capacity is in kWh/kWp. Weather is contemporaneous, so this is conditional prediction rather than weather forecasting.

The new task permits exact one/two-hour-past native-clock radiation from the unchanged weather archive. Provider, timezone, daylight-saving and irradiance averaging are still not confirmed by the author record. Open-Meteo-like headers are only a resemblance; its preceding-hour documentation does not prove these files' provenance. No silent timestamp shift is applied.

## Compact reported equation and selected numerical control

Define G_eff=(G(t)+G(t−1 h))/2,s=2 pi d/365.25,h=(hour−12)/12 and L=(connection capacity/installed capacity) x 1 h. The hourly clipping limit assumes one-hour reporting windows. The compact rule is

$$
\widehat E=\operatorname{clip}\!\left(G_{\mathrm{eff}}[b_0+b_1\cos s+b_2\sin s+b_3 h+b_4 h^2+b_5 h\cos s],0,L\right).
$$

Here G is in kW/m², d is calendar day and source-clock hour is uncorrected. The fitted gain coefficients have units m² h/kWp; their frozen values are (0.890843, 0.248482, -0.029082, 0.253709, -0.575536, -0.563191). This is an interpretable effective reporting-window/calibration rule; it does not identify physical panel orientation, thermal constants or true clock convention.

The preselected numerical reference is a regularized richer calendar/weather basis, not this compact rule. It remains an empirical control with rank-deficient correlated basis terms; individual coefficients are not mechanisms. Exact full-precision states for both are in rules.json.

## Findings, robustness and rejected mechanisms

1. **Stable causal-history candidate:** all five development folds select equal current/previous-hour radiation weighting. Compact lag+geometry MAE 0.090830 improves calendar-only 0.093644 in all five cities and in all four yearly residual strata. Exposed MAE improves 0.108275→0.104717 kWh/kWp. The annual strata are not independent prospective validation. Lag-only coefficients are positive but do not outperform geometry; neither a pure clock correction nor generic smoothing alone explains the full fit.
2. **Stronger comparator limits the claim:** calendar ridge has development 0.089011 and exposed 0.100732 kWh/kWp, beating the compact rule. The original lower-history reference exposes 0.109696; this difference includes new information and increased flexibility, not a new physical law.
3. **Thermal identification fails:** Faiman-inspired cell temperature uses assumed U 0=25,U 1=6.84 and supplied horizontal radiation in place of measured plane-of-array input. The best constrained temperature coefficient is zero in 3/5 folds and−0.002/K in 2/5; adding it barely changes geometry MAE 0.093644→0.093618. Unrestricted ambient coefficients switch signs across folds. The earlier positive coefficient cannot be defended as verified thermal derating, while this result also does not show that real thermal derating is absent.
4. **Persistent site bias:** default Loule bias is−0.013229 kWh/kWp and p 95 absolute error 0.292671. Faro/Tavira development biases have opposite signs. Unmeasured orientation, shading, outage and weather representativeness limit one-city transfer.

## Significance and next discriminating evidence

An effective half-hour radiation-memory representation is useful for audited hourly energy calibration and offers a concrete metrology hypothesis. It is not enough to claim maintenance impact, identify faults or correct timestamps. Obtain author clock/provider/averaging metadata and panel tilt/azimuth; compare actual plane-of-array and module-temperature models, reserve fresh plant-years and use independent maintenance/outage records for industrial decisions. Do not choose new fits from Loule scores.

## Source and replay

[Author dataset](https://data.mendeley.com/datasets/dbh93b6vp8/3); [Sandia module-temperature methods](https://pvpmc.sandia.gov/modeling-guide/2-dc-module-iv/module-temperature/); [Open-Meteo timing documentation](https://open-meteo.com/en/docs/historical-weather-api)(possible provider semantics only, not source identification). Source anchors, all coefficients and priors are preserved. Run `python run.py`; the evaluator's causal-weather-history protocol distinguishes this edition from the historical task.

## Experimental and evaluation contract

All native assets and original final packages remain unchanged. Source hashes and prepared inputs were frozen before fitting. Training uses only the original development groups; leave-one-complete-group-out predictions determine the selection. Least-squares coefficients use equal-group weighting, while tuning/selection uses equal-group MAE. Candidate grids are training-only inside each outer fold. The preselected default is the least complex model within 1% of the lowest development MAE, including strong controls. It is **ridge_calendar**.

Only after candidate and stopping freeze were all original confirmation groups replayed. They were already exposed in the previous campaign: every score below is a **retrospective diagnostic, not fresh confirmation**. All candidates remain visible, including those whose diagnostic error is lower than the selected default. They are not promoted afterward. Error units are kWh/kWp; thousands of correlated rows do not create thousands of independent experiments. No population confidence, new-law or deployed-impact claim is admitted.

## Whole-group numerical evidence

| Model/test | Development OOF MAE | Exposed diagnostic MAE | Fitted constants/clocks |
|---|---:|---:|---:|
| signed_control | 0.128051 | 0.154029 | 2 |
| geometry | 0.093644 | 0.108275 | 6 |
| lag_response | 0.103458 | 0.126868 | 3 |
| signed_thermal | 0.093618 | 0.108192 | 7 |
| lag_geometry | 0.090830 | 0.104717 | 7 |
| unrestricted_thermal | 0.093689 | 0.108316 | 8 |
| ridge_calendar | 0.089011 | 0.100732 | 19 |

The prior frozen reference has diagnostic MAE **0.109696**. The historical reference lacks the newly declared weather history, so that comparison changes the information contract and is not a matched claim of algorithmic superiority. The new controls have identical access to the new permitted inputs. Inspect evidence/by_group.csv for bias, RMSE, p 95 and adverse groups.

## Evaluator and scope

The standalone evaluator supports explicit abstention, matched covered-cohort baselines, intervals, code replay and separate scientific review. Prediction quality does not automatically admit novelty. Future agents must declare inputs/calibration and obtain new experimental groups for fresh confirmation. All point-reference intervals here are absent; error percentiles are descriptive, not calibrated confidence intervals.
