# Within-system hydrogen-permeation relaxation and identifiability

The original workbook contains two hydrogen-permeation current traces at 293 K under cathodic-current increases from 0.5 to 1 and from 5 to 10 mA/cm². It does not identify independent specimens. The task is therefore forward extrapolation within the measured system, using the first 80% of each trace for development and the last 20% for reserved confirmation.

Eleven substantive scientific attempts were completed, plus one invalid technical implementation retained separately. The selected activated-breakthrough surrogate attains 0.674 μA mean trace MAE on the reserved tails, compared with 4.278 μA for the polynomial control. The result supports a compact late-time forecast under these conditions. It does not identify a new physical law or a unique material diffusivity.

The equation is Î(t)=I₀+(A₀+A₁z) exp[−(τ exp(kz)/t)^β], where z identifies the known high-current condition, t and τ are seconds, I₀ is the initial three-point calibration, A₀ and A₁ are μA, and k and β are dimensionless. Condition-dependent effective timing improves prediction, but boundary entry, trapping and diffusion remain confounded.

For the slab competitors, `slab(x)` means S(x)=1+2Σₙ₌₁⁴⁰(−1)ⁿ exp(−n² max(x,0.001)); its argument is dimensionless. `erfc` is the complementary error function. The first slab implementation had a dimensional lag error and was excluded from selection and the final model package; its original files and correction are preserved in research history.

## Experimental scope and evaluation

Forward extrapolation within two linked permeation traces. Parameters are learned only from earlier chronological blocks; confirmation is the last20% of each trace. Known imposed current step and initial three-point current calibration are permitted.

Calibration: Mean first3 native current observations per trace; all candidate families receive identical values. Fit parameters may use development prefixes only.

Validation unit: Two chronological traces with no independent specimen identifiers; nonoverlapping temporal blocks are scoring units, not independent specimens. All trace linkage is explicit.

Report both trace-tail errors; no population interval or independent-specimen significance test.

Target: measured anodic permeation current (μA). Errors use μA. The selected reference is **activated_breakthrough**. Selection was frozen before confirmation; diagnostic winners are not substituted afterward.

| Predictor | Unit |
|---|---|
| t | s since third baseline observation |
| offset | μA; mean first3 observations |
| drive | mA/cm²; imposed cathodic-current step |
| high | binary known high-current condition |


## Matched comparison

| Model | Development MAE | Reserved MAE | Reserved worst-group MAE |
|---|---:|---:|---:|
| fixed_diffusion | 20.852 | 26.1811 | 47.9259 |
| flexible | 11.9525 | 4.27767 | 6.18262 |
| persistence | 27.6682 | 31.2127 | 48.0014 |
| shared_boundary_response | 7.31915 | 8.2512 | 8.56553 |
| fick_slab_corrected | 10.3538 | 5.92083 | 9.29837 |
| surface_saturation | 5.06106 | 2.36247 | 4.36316 |
| trapping_two_timescales | 7.04349 | 8.34861 | 12.2288 |
| occupancy_dependent_transport | 4.78902 | 2.31295 | 3.63909 |
| shared_fick_separate_amplitudes | 3.34284 | 0.854128 | 1.39143 |
| distributed_trapping | 2.52537 | 0.887883 | 1.52371 |
| finite_capacity_trapping | 5.11432 | 3.85729 | 5.91291 |
| activated_breakthrough | 1.51247 | 0.674135 | 0.876482 |
| semi_infinite_arrival | 3.42019 | 3.42719 | 5.12817 |
| common_breakthrough_scale | 3.77347 | 1.26306 | 1.79216 |


The primary error is mean group MAE. RMSE and signed bias are complementary; rows within a group do not establish independent replication. No accuracy percentage or industrial tolerance is invented.


## Executable equations and parameters

Each expression below uses the named inputs in the units table. `exp`, `log`, and `sqrt` have their conventional mathematical meanings. Coefficients are fitted on development data only; all calibration is declared above. The portable `rules.json` contains full precision and each model’s complete training scope.

**fixed_diffusion**

`offset+20*drive*(1-exp(-t/2000))`

Parameters: none.

**flexible**

`offset+b0*t/1000+b1*(t/1000)**2+b2*(t/1000)**3+b3*high*t/1000+b4*high*(t/1000)**2`

Parameters: b0 = 3.355656, b1 = -0.21126296, b2 = 0.0022113734, b3 = 16.575497, b4 = -1.8805105.

**persistence**

`offset`

Parameters: none.

**shared_boundary_response**

`offset+gain*drive*(1-exp(-t/tau))`

Parameters: gain = 13.195982, tau = 3296.055.

**fick_slab_corrected**

`offset+gain*drive*(slab(t/tau+lag)-slab(lag+0*t))`

Parameters: gain = 10.253304, tau = 1345.5102, lag = 0.22091361.

**surface_saturation**

`offset+gain*drive/(1+k*drive)*(1-exp(-t/tau))`

Parameters: gain = 33.833973, k = 0.39343637, tau = 2557.5851.

**trapping_two_timescales**

`offset+gain*drive*((1-w)*(1-exp(-t/tau))+w*(1-exp(-t/(tau+slow))))`

Parameters: gain = 360.64994, w = 0.98646832, tau = 1368.3663, slow = 313277.43.

**occupancy_dependent_transport**

`offset+(a0+a1*high)*(1-exp(-t/(tau*exp(k*high))))`

Parameters: a0 = 15.90924, a1 = 39.585013, tau = 3894.3753, k = -0.48290597.

**shared_fick_separate_amplitudes**

`offset+(a0+a1*high)*(slab(t/tau+lag)-slab(lag+0*t))`

Parameters: a0 = 13.032909, a1 = 35.662206, tau = 1172.2022, lag = 0.11815425.

**distributed_trapping**

`offset+(a0+a1*high)*(1-exp(-(t/(tau*exp(k*high)))**beta))`

Parameters: a0 = 14.172039, a1 = 32.30792, tau = 3182.9074, k = -0.59492788, beta = 1.8097042.

**finite_capacity_trapping**

`offset+(a0+a1*high)*t/(tau*exp(k*high)+t)`

Parameters: a0 = 21.984277, a1 = 59.554598, tau = 4806.3657, k = -0.37819539.

**activated_breakthrough**

`offset+(a0+a1*high)*exp(-(tau*exp(k*high)/t)**beta)`

Parameters: a0 = 15.667296, a1 = 36.58884, tau = 2087.4887, k = -0.57031044, beta = 1.5986771.

**semi_infinite_arrival**

`offset+(a0+a1*high)*erfc(sqrt(tau*exp(k*high)/t))`

Parameters: a0 = 24.622401, a1 = 62.290425, tau = 1344.4756, k = -0.48248702.

**common_breakthrough_scale**

`offset+(a0+a1*high)*exp(-(tau/t)**beta)`

Parameters: a0 = 14.127139, a1 = 40.480443, tau = 1232.8384, beta = 1.4449559.


## Applicability and limitations

- The two traces do not establish independent-specimen transfer. Temperature is293K; nominal sheet thickness1.2mm.
- Native time zero is used as reported; true boundary concentration and its step timing are not independently measured.
- An effective relaxation scale must not be relabeled a unique lattice diffusivity because trapping, boundary kinetics and baseline uncertainty can be confounded.

Firsttwo observations per sheet were inspected for schema and belong to permitted initial calibration. No reserved tail current was inspected before freeze.

## Reproduction

Run `python run.py` in this final package to verify hashes and reproduce every saved prediction. Use `python run.py --inputs new.csv --output predictions.csv --model reference` only with the declared inputs and units. Numerical prediction evaluation does not certify novelty or mechanism. Source anchors and reserved observations are separate from predictor inputs.

Source: https://data.mendeley.com/datasets/tnsgf7v76z/1. See source/units audit and prior-art records in research history.
