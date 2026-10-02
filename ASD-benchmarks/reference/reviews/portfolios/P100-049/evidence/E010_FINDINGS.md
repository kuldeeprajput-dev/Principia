# Causal voltage relaxation after GITT pulses

The source contains measured Li-graphite half-cell GITT and POCV exports. This task uses the GITT campaign only. A completed current pulse is followed by a long rest; the practical question is whether two early rest-voltage observations can forecast the subsequent30minutes.

The strongest development-selected rule is finite-pulse diffusion, with no fitted global coefficient. Its reserved MAE is0.686mV, a12.2% improvement over the constrained flexible control and80.1% over persistence. The advantage is specific to MAE: its RMSE and worst-block error are worse than the flexible control. This is a useful scoped forecasting result, not a newly discovered universal electrochemical law.

Let g(t)=√(t+T)−√t. Eliminating the unknown amplitude and equilibrium offset from U(t)=U∞+A g(t) gives Û(t)=U_b+(U_b−U_a)[g(t)−g(b)]/[g(b)−g(a)]. Here T is the measured pulse duration and a,b are the actual causal calibration times. The cancellation explains both its simplicity and why it cannot identify a unique diffusivity.

## Experimental scope and evaluation

Issue predictions at120s of each current-free block; only actual samples at or before10/60/120s and completed preceding current pulse are predictors. Targets are nearest native samples to300/600/1200/1800s, tolerance15s.

Calibration: Three causal voltage samples per block; no fit to later outcomes. Calibration access is identical for every model.

Validation unit: Complete rest block linked to preceding current pulse; all blocks belong to one half-cell, so block summaries are not independent-cell confidence.

Report chronological block errors; no independent-cell confidence interval.

Target: voltage during current-free relaxation (V). Errors use V. The selected reference is **finite_pulse_diffusion**. Selection was frozen before confirmation; diagnostic winners are not substituted afterward.

| Predictor | Unit |
|---|---|
| t | s |
| t60 | s |
| t120 | s |
| u60 | V |
| u120 | V |
| u10 | V |
| pulse_s | s |
| current | A |


## Matched comparison

| Model | Development MAE | Reserved MAE | Reserved worst-group MAE |
|---|---:|---:|---:|
| fixed_rc | 0.00139811 | 0.00218012 | 0.0509115 |
| flexible | 0.00060865 | 0.000782191 | 0.0115079 |
| persistence | 0.00150566 | 0.00344433 | 0.100651 |
| finite_pulse_diffusion | 0.000391423 | 0.000686422 | 0.0144938 |
| learned_rc | 0.000670335 | 0.000993741 | 0.0151337 |
| fractional_tail | 0.000459116 | 0.000604582 | 0.00785862 |
| diffusion_rc_mixture | 0.000391423 | 0.000686422 | 0.0144938 |
| boundary_storage | 0.000392807 | 0.000568418 | 0.00734045 |


The primary error is mean group MAE. RMSE and signed bias are complementary; rows within a group do not establish independent replication. No accuracy percentage or industrial tolerance is invented.


## Executable equations and parameters

Each expression below uses the named inputs in the units table. `exp`, `log`, and `sqrt` have their conventional mathematical meanings. Coefficients are fitted on development data only; all calibration is declared above. The portable `rules.json` contains full precision and each model’s complete training scope.

**fixed_rc**

`u120+(u120-u60)*(exp(-t/300)-exp(-t120/300))/(exp(-t120/300)-exp(-t60/300))`

Parameters: none.

**flexible**

`u120+b0*(u120-u60)+b1*(u120-u60)*log(t/t120)+b2*(u120-u60)*log(t/t120)**2+b3*(u120-u10)`

Parameters: b0 = -1.5063359, b1 = 1.4451086, b2 = -0.067591093, b3 = 0.42957476.

**persistence**

`u120`

Parameters: none.

**finite_pulse_diffusion**

`u120+(u120-u60)*(sqrt(t+pulse_s)-sqrt(t)-sqrt(t120+pulse_s)+sqrt(t120))/(sqrt(t120+pulse_s)-sqrt(t120)-sqrt(t60+pulse_s)+sqrt(t60))`

Parameters: none.

**learned_rc**

`u120+(u120-u60)*(exp(-t/tau)-exp(-t120/tau))/(exp(-t120/tau)-exp(-t60/tau))`

Parameters: tau = 204.3657.

**fractional_tail**

`u120+(u120-u60)*(t**(-alpha)-t120**(-alpha))/(t120**(-alpha)-t60**(-alpha))`

Parameters: alpha = 0.066641325.

**diffusion_rc_mixture**

`u120+(u120-u60)*(((1-w)*(sqrt(t+pulse_s)-sqrt(t))/sqrt(pulse_s)+w*exp(-t/tau))-((1-w)*(sqrt(t120+pulse_s)-sqrt(t120))/sqrt(pulse_s)+w*exp(-t120/tau)))/(((1-w)*(sqrt(t120+pulse_s)-sqrt(t120))/sqrt(pulse_s)+w*exp(-t120/tau))-((1-w)*(sqrt(t60+pulse_s)-sqrt(t60))/sqrt(pulse_s)+w*exp(-t60/tau)))`

Parameters: w = 6.3752069e-12, tau = 10.

**boundary_storage**

`u120+(u120-u60)*clip(a+b*u120,0,3)*((sqrt(t+pulse_s)-sqrt(t))-(sqrt(t120+pulse_s)-sqrt(t120)))/((sqrt(t120+pulse_s)-sqrt(t120))-(sqrt(t60+pulse_s)-sqrt(t60)))`

Parameters: a = 0.93003938, b = 0.19250262.


## Applicability and limitations

- One Li-graphite half-cell and one GITT campaign; no population transfer or diffusion-coefficient identification.
- POCV file is preserved but not used because it has a different protocol.

Only initial pre-GITT voltage rows were inspected at schema stage. Eligible reserved relaxation targets were not inspected. All packaged outcomes become public/exposed.

## Reproduction

Run `python run.py` in this final package to verify hashes and reproduce every saved prediction. Use `python run.py --inputs new.csv --output predictions.csv --model reference` only with the declared inputs and units. Numerical prediction evaluation does not certify novelty or mechanism. Source anchors and reserved observations are separate from predictor inputs.

Source: https://zenodo.org/records/17295469. See source/units audit and prior-art records in research history.
