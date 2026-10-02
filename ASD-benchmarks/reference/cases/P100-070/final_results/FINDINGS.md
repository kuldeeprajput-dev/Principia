# Local reconstruction of measured earthquake magnetic microscopy maps

The source supplies measured magnetic-field maps from two laboratory-fault specimens and several temperature-inversion products. This task uses only the Bz map ordinates from CSH/119 DOA and CSL/129 DOA. Author-inferred temperatures and MCMC samples are retained in the source inventory but excluded as independent truth.

CSH supplies development data, split into complete horizontal strips. CSL is the reserved specimen. The task reconstructs fixed withheld pixels using twelve neighboring Bz measurements from the same image; target centers cannot occur in any calibration neighborhood. Spatial blocks balance the numerical error, but 36 blocks in one specimen are not 36 independent experiments.

The selected parameter-free two-scale stencil achieves MAE $2.084\times 10^{-6}$ in native Bz units, versus $2.283\times 10^{-6}$ for the matched affine control and $2.468\times 10^{-6}$ for the local mean. Five attempts compared directional anisotropy, curvature retention, contrast-adaptive weighting, additional smoothing and bounded extrema.

The result is a useful within-setup interpolation reference, with no new magnetic or heating law. SI calibration of native Bz is unresolved. Published temperature claims remain prior art and are not tested here.

## Experimental scope and evaluation

Retrospective reconstruction at one microscopy acquisition; all neighboring measurements are available. No prediction of an earthquake or temperature history.

Calibration: Twelve same-map neighbors: cardinal offsets 4/8 pixels and diagonal 4 pixels. Centers are 20 pixel lattice points, none can be a calibration point for another scored center.

Validation unit: Two specimens: CSH/119 DOA development and CSL/129 DOA confirmation. Spatial blocks balance errors but are not independent specimens; development folds are entire 200 row strips.

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


## Selected equation and coefficients

$$
\widehat B_z=[4(h_x+h_y)-(o_x+o_y)]/6
$$

The h terms average opposite neighboring measured pixels at one grid step, and o terms at two steps. Bz and all neighbor values remain in source-native units. This fourth-order local smoothness stencil does not infer source temperature or earthquake heat.

This reference has no globally fitted coefficients.

All comparator expressions, numerical guards and full-precision values remain in EQUATIONS.md, rules.json and run.py.

## Applicability and limitations

- Native README identifies Bz maps but does not establish numerical SI conversion; scores deliberately remain source-native units.
- Temperature profiles, MCMC inversion outputs and maximum-temperature samples are author-derived and excluded as independent targets.
- A two-dimensional smooth stencil is not a consequence of the three-dimensional magnetostatic Laplace equation without information about vertical derivatives.

Only variable dimensions and README were inspected before assigning whole CSL to confirmation. No confirmation Bz values were viewed.

## Reproduction

Run `python run.py` in this final package to verify hashes and reproduce every saved prediction. Use `python run.py --inputs new.csv --output predictions.csv --model reference` only with the declared inputs and units. Numerical prediction evaluation does not certify novelty or mechanism. Source anchors and reserved observations are separate from predictor inputs.

Source: https://zenodo.org/records/14776881. See source/units audit and prior-art records in research history.
