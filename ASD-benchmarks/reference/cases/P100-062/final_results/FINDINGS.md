# Within-system hydrogen-permeation relaxation and identifiability

The original workbook contains two hydrogen-permeation current traces at 293 K under cathodic-current increases from 0.5 to 1 and from 5 to 10 mA/cm². It does not identify independent specimens. The task is therefore forward extrapolation within the measured system, using the first 80% of each trace for development and the last 20% for reserved confirmation.

Eleven substantive scientific attempts were completed, plus one invalid technical implementation retained separately. The selected activated-breakthrough surrogate attains 0.674 μA mean trace MAE on the reserved tails, compared with 4.278 μA for the polynomial control. The result supports a compact late-time forecast under these conditions. It does not identify a new physical law or a unique material diffusivity.

The equation is Î(t)=I₀+(A₀+A₁z) exp[−(τ exp(kz)/t)^β], where z identifies the known high-current condition, t and τ are seconds, I₀ is the initial three-point calibration, A₀ and A₁ are μA, and k and β are dimensionless. Condition-dependent effective timing improves prediction, but boundary entry, trapping and diffusion remain confounded.

For the slab competitors, the dimensionless response is

$$
S(x)=1+2\sum_{n=1}^{40}(-1)^n\exp[-n^2\max(x,0.001)].
$$

The function erfc is the complementary error function. A dimensional lag error invalidated the first slab implementation; its files and correction are preserved, and it is excluded from model selection.

## Experimental scope and evaluation

Forward extrapolation within two linked permeation traces. Parameters are learned only from earlier chronological blocks; confirmation is the last 20% of each trace. Known imposed current step and initial three-point current calibration are permitted.

Calibration: Mean first 3 native current observations per trace; all candidate families receive identical values. Fit parameters may use development prefixes only.

Validation unit: Two chronological traces with no independent specimen identifiers; nonoverlapping temporal blocks are scoring units, not independent specimens. All trace linkage is explicit.

Report both trace-tail errors; no population interval or independent-specimen significance test.

Target: measured anodic permeation current (μA). Errors use μA. The selected reference is **activated_breakthrough**. Selection was frozen before confirmation; diagnostic winners are not substituted afterward.

| Predictor | Unit |
|---|---|
| t | s since third baseline observation |
| offset | μA; mean first 3 observations |
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


## Selected equation and coefficients

$$
\widehat J(t)=J_0+(a_0+a_1H)\exp\!\left[-\left(\frac{\tau e^{kH}}{t}\right)^\beta\right]
$$

J0 is the allowed initial current offset in microamperes; H is the declared high-current-condition indicator. Time t and tau are in seconds; a 0 and a 1 are in microamperes, while k and beta are dimensionless. The effective timescale is not a uniquely identified diffusivity.

| Coefficient | Frozen value |
|---|---:|
| a 0 | 15.6672957 |
| a 1 | 36.5888402 |
| tau | 2087.48867 |
| k | -0.57031044 |
| beta | 1.59867711 |

All comparator expressions, numerical guards and full-precision values remain in EQUATIONS.md, rules.json and run.py.

## Applicability and limitations

- The two traces do not establish independent-specimen transfer. Temperature is 293 K; nominal sheet thickness 1.2 mm.
- Native time zero is used as reported; true boundary concentration and its step timing are not independently measured.
- An effective relaxation scale must not be relabeled a unique lattice diffusivity because trapping, boundary kinetics and baseline uncertainty can be confounded.

First two observations per sheet were inspected for schema and belong to permitted initial calibration. No reserved tail current was inspected before freeze.

## Reproduction

Run `python run.py` in this final package to verify hashes and reproduce every saved prediction. Use `python run.py --inputs new.csv --output predictions.csv --model reference` only with the declared inputs and units. Numerical prediction evaluation does not certify novelty or mechanism. Source anchors and reserved observations are separate from predictor inputs.

Source: https://data.mendeley.com/datasets/tnsgf7v76z/1. See source/units audit and prior-art records in research history.
