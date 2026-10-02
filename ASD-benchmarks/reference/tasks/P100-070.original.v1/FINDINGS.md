# Local reconstruction of measured earthquake magnetic microscopy maps

The source supplies measured magnetic-field maps from two laboratory-fault specimens and several temperature-inversion products. This task uses only the Bz map ordinates from CSH/119DOA and CSL/129DOA. Author-inferred temperatures and MCMC samples are retained in the source inventory but excluded as independent truth.

CSH supplies development data, split into complete horizontal strips. CSL is the reserved specimen. The task reconstructs fixed withheld pixels using twelve neighboring Bz measurements from the same image; target centers cannot occur in any calibration neighborhood. Spatial blocks balance the numerical error, but36 blocks in one specimen are not36 independent experiments.

The selected parameter-free two-scale stencil achieves MAE2.084×10⁻⁶ in native Bz units, versus2.283×10⁻⁶ for the matched affine control and2.468×10⁻⁶ for the local mean. Five attempts compared directional anisotropy, curvature retention, contrast-adaptive weighting, additional smoothing and bounded extrema.

The result reproduces a useful interpolation principle within this metrology setup. It does not identify a new magnetic or heating law. The distributed README does not establish the numerical conversion of Bz to SI units, so no guessed conversion is applied. The strong source-paper temperature conclusions are prior art and are not independently revalidated by this task.

## Experimental scope and evaluation

Retrospective reconstruction at one microscopy acquisition; all neighboring measurements are available. No prediction of an earthquake or temperature history.

Calibration: Twelve same-map neighbors: cardinal offsets4/8pixels and diagonal4pixels. Centers are20pixel lattice points, none can be a calibration point for another scored center.

Validation unit: Two specimens: CSH/119DOA development and CSL/129DOA confirmation. Spatial blocks balance errors but are not independent specimens; development folds are entire200row strips.

Report spatial blocks and one specimen result; no confidence interval claiming specimen population generalization.

Target: native Bz map ordinate at a withheld pixel (source-native Bz unit (SI conversion unresolved)). Errors use source-native Bz unit (SI conversion unresolved). The selected reference is **dipole_curvature**. Selection was frozen before confirmation; diagnostic winners are not substituted afterward.

| Predictor | Unit |
|---|---|
| hx | source-native Bz unit |
| hy | source-native Bz unit |
| ox | source-native Bz unit |
| oy | source-native Bz unit |
| dg | source-native Bz unit |
| lo | source-native Bz unit |
| hi | source-native Bz unit |
| gx | dimensionless local contrast |
| gy | dimensionless local contrast |


## Matched comparison

| Model | Development MAE | Reserved MAE | Reserved worst-group MAE |
|---|---:|---:|---:|
| flexible | 3.12746e-06 | 2.28349e-06 | 7.63516e-06 |
| local_mean | 3.13526e-06 | 2.46793e-06 | 8.81621e-06 |
| zero_field | 9.38778e-06 | 8.16981e-06 | 2.59155e-05 |
| fault_axis_anisotropy | 3.18349e-06 | 2.46647e-06 | 8.78365e-06 |
| dipole_curvature | 2.90193e-06 | 2.08396e-06 | 7.38033e-06 |
| domain_boundary_adaptive | 3.0771e-06 | 2.44398e-06 | 8.77655e-06 |
| finite_footprint_smoothing | 3.13526e-06 | 2.46793e-06 | 8.81621e-06 |
| bounded_extrema | 2.90691e-06 | 2.08686e-06 | 7.38962e-06 |


The primary error is mean group MAE. RMSE and signed bias are complementary; rows within a group do not establish independent replication. No accuracy percentage or industrial tolerance is invented.


## Executable equations and parameters

Each expression below uses the named inputs in the units table. `exp`, `log`, and `sqrt` have their conventional mathematical meanings. Coefficients are fitted on development data only; all calibration is declared above. The portable `rules.json` contains full precision and each model’s complete training scope.

**flexible**

`b0+b1*hx+b2*hy+b3*ox+b4*oy+b5*dg`

Parameters: b0 = -1.4395409e-07, b1 = 0.52181762, b2 = 0.66219179, b3 = -0.090550196, b4 = -0.26870013, b5 = 0.19873701.

**local_mean**

`(hx+hy)/2`

Parameters: none.

**zero_field**

`0`

Parameters: none.

**fault_axis_anisotropy**

`w*hx+(1-w)*hy`

Parameters: w = 0.49266599.

**dipole_curvature**

`(4*(hx+hy)-(ox+oy))/6`

Parameters: none.

**domain_boundary_adaptive**

`(hx/(gx*gx+eps*eps)+hy/(gy*gy+eps*eps))/(1/(gx*gx+eps*eps)+1/(gy*gy+eps*eps))`

Parameters: eps = 1.4555642.

**finite_footprint_smoothing**

`(hx+hy)/2+k*((ox+oy)-(hx+hy))/2`

Parameters: k = 8.6531364e-21.

**bounded_extrema**

`clip((4*(hx+hy)-(ox+oy))/6,lo,hi)`

Parameters: none.


## Applicability and limitations

- Native README identifies Bz maps but does not establish numerical SI conversion; scores deliberately remain source-native units.
- Temperature profiles, MCMC inversion outputs and maximum-temperature samples are author-derived and excluded as independent targets.
- A two-dimensional smooth stencil is not a consequence of the three-dimensional magnetostatic Laplace equation without information about vertical derivatives.

Only variable dimensions and README were inspected before assigning whole CSL to confirmation. No confirmation Bz values were viewed.

## Reproduction

Run `python run.py` in this final package to verify hashes and reproduce every saved prediction. Use `python run.py --inputs new.csv --output predictions.csv --model reference` only with the declared inputs and units. Numerical prediction evaluation does not certify novelty or mechanism. Source anchors and reserved observations are separate from predictor inputs.

Source: https://zenodo.org/records/14776881. See source/units audit and prior-art records in research history.
