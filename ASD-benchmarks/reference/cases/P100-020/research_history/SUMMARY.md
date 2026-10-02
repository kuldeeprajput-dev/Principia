# P100-020 exploration summary

The input is one NOAA global nighttime sea-surface-temperature anomaly map, dated16August2026, with a1991–2020 climatological baseline. Its NetCDF contains one time plane, a0.01degreeC scale factor and explicit water, land, missing and ice flags. This is a processed satellite product.

The task reconstructs fixed water-pixel targets from twelve neighboring pixels on the same map. Target centers lie on a40pixel lattice; none of those centers can appear among any other target's calibration pixels. Complete20degree geographic tiles are assigned by a fixed hash, with23 eligible tiles reserved.

The selected six-coefficient local stencil achieves0.03284degreeC tile-balanced MAE and0.06714degreeC worst-tile MAE. Unweighted local averaging gives0.05750 and0.2450degreeC. Eight attempts examined spherical distances, Taylor curvature cancellation, directional fronts, diagonal geometry, curvature limiting, latitude correction, range preservation and observation-noise averaging.

These results establish useful numerical reconstruction references. They do not establish ocean dynamics, future heat stress or coral bleaching thresholds. The same-map calibration and exclusion of incomplete coastal/ice neighborhoods are essential parts of the task, and no population confidence is inferred from dependent pixels.

| Model | Development MAE | Reserved MAE | Reserved worst-group MAE |
|---|---:|---:|---:|
| flexible | 0.0356912 | 0.0328365 | 0.0671359 |
| local_mean | 0.0521489 | 0.0574952 | 0.245 |
| zero_anomaly | 0.853588 | 0.798152 | 2.05919 |
| spherical_distance | 0.0501236 | 0.0503713 | 0.134759 |
| fourth_order_smooth | 0.0398408 | 0.0401033 | 0.136667 |
| front_adaptive | 0.0507908 | 0.0496442 | 0.0785472 |
| rotational_ninepoint | 0.0444504 | 0.0454642 | 0.14875 |
| limited_curvature | 0.0392258 | 0.0378708 | 0.101033 |
| latitude_curvature | 0.0371352 | 0.0345851 | 0.0798387 |
| range_preserving | 0.0436794 | 0.0441662 | 0.136667 |
| broad_noise_average | 0.0837839 | 0.0952444 | 0.4075 |


## Attempt history

**attempt-001 — spherical_distance**: Attempt1: equal angular longitude spacing shrinks physically with latitude. Inverse squared physical-distance weighting should prioritize the east-west pair at high latitude. Development MAE=0.0501236; worst group=0.157522; fitted parameters=0.

**attempt-002 — fourth_order_smooth**: Development evidence available before this fit: spherical_distance: MAE 0.0501236, worst group 0.157522.

The physical-distance correction remains worse than the flexible stencil. Test a competing smooth-field hypothesis: two-scale Taylor cancellation removes the leading quadratic interpolation bias without fitted parameters. Development MAE=0.0398408; worst group=0.105833; fitted parameters=0.

**attempt-003 — front_adaptive**: Development evidence available before this fit: spherical_distance: MAE 0.0501236, worst group 0.157522; fourth_order_smooth: MAE 0.0398408, worst group 0.105833.

Test frontal anisotropy rather than isotropic smoothness. Weight the direction with less observed cross-front contrast more strongly; eps is a development-fitted temperature contrast regularizer. Development MAE=0.0507908; worst group=0.153314; fitted parameters=1.

**attempt-004 — rotational_ninepoint**: Development evidence available before this fit: fourth_order_smooth: MAE 0.0398408, worst group 0.105833; front_adaptive: MAE 0.0507908, worst group 0.153314.

Test rotational consistency of the local stencil: diagonal observations constrain mixed curvature and may reduce cardinal-grid directional bias. This is a standard smooth-field reconstruction hypothesis, not a dynamical ocean equation. Development MAE=0.0444504; worst group=0.114452; fitted parameters=0.

**attempt-005 — limited_curvature**: Development evidence available before this fit: front_adaptive: MAE 0.0507908, worst group 0.153314; rotational_ninepoint: MAE 0.0444504, worst group 0.114452.

Reconcile curvature recovery with front preservation. A learned curvature coefficient is attenuated in high-contrast neighborhoods; both scales are determined using development tiles only. Development MAE=0.0392258; worst group=0.0932574; fitted parameters=2.

**attempt-006 — latitude_curvature**: Development evidence available before this fit: rotational_ninepoint: MAE 0.0444504, worst group 0.114452; limited_curvature: MAE 0.0392258, worst group 0.0932574.

Test whether curvature correction benefits from spherical distance rather than treating latitude-longitude cells as squares. This competes directly with the unweighted limited-curvature explanation. Development MAE=0.0371352; worst group=0.0874195; fitted parameters=1.

**attempt-007 — range_preserving**: Development evidence available before this fit: limited_curvature: MAE 0.0392258, worst group 0.0932574; latitude_curvature: MAE 0.0371352, worst group 0.0874195.

Test a falsifying monotonicity constraint: rejecting curvature overshoot may improve reliability if unresolved fronts dominate. The bound comes only from allowed neighboring calibration values. Development MAE=0.0436794; worst group=0.15; fitted parameters=0.

**attempt-008 — broad_noise_average**: Development evidence available before this fit: latitude_curvature: MAE 0.0371352, worst group 0.0874195; range_preserving: MAE 0.0436794, worst group 0.15.

Test an independent observation-noise explanation: a broader equal-weight spatial average should help if instrument noise, rather than unresolved curvature, dominates the center error. Its opposite curvature sign provides a falsifying control to high-order reconstruction. Development MAE=0.0837839; worst group=0.250464; fitted parameters=0.

All substantive attempts and failures are retained. See FREEZE.json and CONFIRMATION_RECEIPT.json for chronology and exact evidence binding.
