# Causal voltage relaxation after GITT pulses

The source contains measured Li-graphite half-cell GITT and POCV exports. This task uses the GITT campaign only. A completed current pulse is followed by a long rest; the practical question is whether two early rest-voltage observations can forecast the subsequent 30 minutes.

The strongest development-selected rule is finite-pulse diffusion, with no fitted global coefficient. Its reserved MAE is 0.686 mV, a 12.2% improvement over the constrained flexible control and 80.1% over persistence. The advantage is specific to MAE: its RMSE and worst-block error are worse than the flexible control. This is a useful scoped forecasting result, not a newly discovered universal electrochemical law.

Let g(t)=√(t+T)−√t. Eliminating the unknown amplitude and equilibrium offset from U(t)=U∞+A g(t) gives Û(t)=U_b+(U_b−U_a)[g(t)−g(b)]/[g(b)−g(a)]. Here T is the measured pulse duration and a, b are the actual causal calibration times. The cancellation explains both its simplicity and why it cannot identify a unique diffusivity.

## Experimental scope and evaluation

Issue predictions at 120 s of each current-free block; only actual samples at or before 10/60/120 s and completed preceding current pulse are predictors. Targets are nearest native samples to 300/600/1200/1800 s, tolerance 15 s.

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


## Selected equation and coefficients

$$
\widehat U(t)=U_b+(U_b-U_a)\frac{g(t)-g(b)}{g(b)-g(a)},\qquad g(t)=\sqrt{t+T}-\sqrt{t}
$$

T is completed pulse duration; a and b are actual calibration timestamps at or before 60 and 120 s. Voltages U_a and U_b are measured calibration values. No global coefficient is fitted.

This reference has no globally fitted coefficients.

All comparator expressions, numerical guards and full-precision values remain in EQUATIONS.md, rules.json and run.py.

## Applicability and limitations

- One Li-graphite half-cell and one GITT campaign; no population transfer or diffusion-coefficient identification.
- POCV file is preserved but not used because it has a different protocol.

Only initial pre-GITT voltage rows were inspected at schema stage. Eligible reserved relaxation targets were not inspected. All packaged outcomes become public/exposed.

## Reproduction

Run `python run.py` in this final package to verify hashes and reproduce every saved prediction. Use `python run.py --inputs new.csv --output predictions.csv --model reference` only with the declared inputs and units. Numerical prediction evaluation does not certify novelty or mechanism. Source anchors and reserved observations are separate from predictor inputs.

Source: https://zenodo.org/records/17295469. See source/units audit and prior-art records in research history.
