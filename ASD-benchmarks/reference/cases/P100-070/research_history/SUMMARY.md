# P100-070 exploration summary

The source supplies measured magnetic-field maps from two laboratory-fault specimens and several temperature-inversion products. This task uses only the Bz map ordinates from CSH/119DOA and CSL/129DOA. Author-inferred temperatures and MCMC samples are retained in the source inventory but excluded as independent truth.

CSH supplies development data, split into complete horizontal strips. CSL is the reserved specimen. The task reconstructs fixed withheld pixels using twelve neighboring Bz measurements from the same image; target centers cannot occur in any calibration neighborhood. Spatial blocks balance the numerical error, but36 blocks in one specimen are not36 independent experiments.

The selected parameter-free two-scale stencil achieves MAE2.084×10⁻⁶ in native Bz units, versus2.283×10⁻⁶ for the matched affine control and2.468×10⁻⁶ for the local mean. Five attempts compared directional anisotropy, curvature retention, contrast-adaptive weighting, additional smoothing and bounded extrema.

The result reproduces a useful interpolation principle within this metrology setup. It does not identify a new magnetic or heating law. The distributed README does not establish the numerical conversion of Bz to SI units, so no guessed conversion is applied. The strong source-paper temperature conclusions are prior art and are not independently revalidated by this task.

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


## Attempt history

**attempt-001 — fault_axis_anisotropy**: Attempt1: fixed imaging-axis anisotropy may represent elongated fault-field structure. Learn a convex directional weight on development strips and test whole-specimen transfer. Development MAE=3.18349e-06; worst group=9.41171e-06; fitted parameters=1.

**attempt-002 — dipole_curvature**: Development evidence available before this fit: fault_axis_anisotropy: MAE 3.18349e-06, worst group 9.41171e-06.

A smoothly varying field from finite-depth magnetic sources may retain local curvature. Test two-scale Taylor cancellation instead of first-order averaging. This is a smoothness approximation, not an assertion of two-dimensional magnetostatic harmonicity. Development MAE=2.90193e-06; worst group=8.85771e-06; fitted parameters=0.

**attempt-003 — domain_boundary_adaptive**: Development evidence available before this fit: fault_axis_anisotropy: MAE 3.18349e-06, worst group 9.41171e-06; dipole_curvature: MAE 2.90193e-06, worst group 8.85771e-06.

Test whether sharp directional contrasts from localized magnetic heterogeneity favor interpolation along the less-varying direction. Normalize contrast using neighbor RMS to avoid arbitrary unit dependence. Development MAE=3.0771e-06; worst group=8.43658e-06; fitted parameters=1.

**attempt-004 — finite_footprint_smoothing**: Development evidence available before this fit: dipole_curvature: MAE 2.90193e-06, worst group 8.85771e-06; domain_boundary_adaptive: MAE 3.0771e-06, worst group 8.43658e-06.

Test a competing observation explanation: unresolved source heterogeneity or map noise may favor additional spatial averaging rather than curvature enhancement. A positive k broadens the footprint. Development MAE=3.13526e-06; worst group=8.83425e-06; fitted parameters=1.

**attempt-005 — bounded_extrema**: Development evidence available before this fit: domain_boundary_adaptive: MAE 3.0771e-06, worst group 8.43658e-06; finite_footprint_smoothing: MAE 3.13526e-06, worst group 8.83425e-06.

Test whether limiting curvature overshoot to the measured neighboring range helps retain stable extrema near heterogeneous source concentrations. This tests interpolation reliability, not a magnetic maximum principle in a horizontal plane. Development MAE=2.90691e-06; worst group=8.85771e-06; fitted parameters=0.

All substantive attempts and failures are retained. See FREEZE.json and CONFIRMATION_RECEIPT.json for chronology and exact evidence binding.
