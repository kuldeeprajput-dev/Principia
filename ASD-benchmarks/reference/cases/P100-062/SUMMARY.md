# P100-062 exploration summary

The original workbook contains two hydrogen-permeation current traces at 293 K under cathodic-current increases from 0.5 to 1 and from 5 to 10 mA/cm². It does not identify independent specimens. The task is therefore forward extrapolation within the measured system, using the first 80% of each trace for development and the last 20% for reserved confirmation.

Eleven substantive scientific attempts were completed, plus one invalid technical implementation retained separately. The selected activated-breakthrough surrogate attains 0.674 μA mean trace MAE on the reserved tails, compared with 4.278 μA for the polynomial control. The result supports a compact late-time forecast under these conditions. It does not identify a new physical law or a unique material diffusivity.

The equation is Î(t)=I₀+(A₀+A₁z) exp[−(τ exp(kz)/t)^β], where z identifies the known high-current condition, t and τ are seconds, I₀ is the initial three-point calibration, A₀ and A₁ are μA, and k and β are dimensionless. Condition-dependent effective timing improves prediction, but boundary entry, trapping and diffusion remain confounded.

For the slab competitors, `slab(x)` means S(x)=1+2Σₙ₌₁⁴⁰(−1)ⁿ exp(−n² max(x,0.001)); its argument is dimensionless. `erfc` is the complementary error function. The first slab implementation had a dimensional lag error and was excluded from selection and the final model package; its original files and correction are preserved in research history.

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


## Attempt history

**attempt-001 — shared_boundary_response**: Attempt1: a common linear permeation gain and relaxation time describe both applied-current increments. Failure would challenge proportional boundary-concentration response under a shared effective transport mode. Development MAE=7.31915; worst group=15.7251; fitted parameters=2.

**attempt-002 — fick_slab**: Development evidence available before this fit: shared_boundary_response: MAE 7.31915, worst group 15.7251.

The shared first-order response improves over polynomial extrapolation. Test the full Fickian slab breakthrough shape, allowing a boundary-onset lag rather than assuming first-order arrival. The normalized lag is explicit; model failure is not evidence against diffusion generally. Development MAE=5.99224; worst group=9.37037; fitted parameters=3.

**attempt-003 — fick_slab_corrected**: Development evidence available before this fit: shared_boundary_response: MAE 7.31915, worst group 15.7251; fick_slab: MAE 5.99224, worst group 9.37037.

Technical correction of dimensional lag error in the first slab implementation. Original result is invalid and excluded from selection; this corrected first full-slab scientific test uses dimensionless t/tau plus a dimensionless initial lag. It counts as one substantive slab hypothesis, not an extra discovery. Development MAE=10.3538; worst group=21.6434; fitted parameters=3.

**attempt-004 — surface_saturation**: Development evidence available before this fit: fick_slab: MAE 5.99224, worst group 9.37037; fick_slab_corrected: MAE 10.3538, worst group 21.6434.

Test nonproportional boundary supply: the high cathodic step may saturate adsorption/entry so that permeation amplitude is sublinear in imposed charging current. This competes with a shared diffusion coefficient explanation. Development MAE=5.06106; worst group=11.946; fitted parameters=3.

**attempt-005 — trapping_two_timescales**: Development evidence available before this fit: fick_slab_corrected: MAE 10.3538, worst group 21.6434; surface_saturation: MAE 5.06106, worst group 11.946.

Test a distinct reversible-storage mechanism: a fast mobile response plus slow trap-filling response. Both gains stay shared across traces; boundaries and identifiability diagnose whether the extra timescale is actually resolved. Development MAE=7.04349; worst group=15.7037; fitted parameters=4.

**attempt-006 — occupancy_dependent_transport**: Development evidence available before this fit: surface_saturation: MAE 5.06106, worst group 11.946; trapping_two_timescales: MAE 7.04349, worst group 15.7037.

Test whether trap occupancy/current condition requires a different effective timescale, while allowing separate measured-condition amplitudes. Improved forward prediction would support an effective condition-dependent surrogate, not a unique lattice diffusivity. Development MAE=4.78902; worst group=11.5347; fitted parameters=4.

**attempt-007 — shared_fick_separate_amplitudes**: Development evidence available before this fit: trapping_two_timescales: MAE 7.04349, worst group 15.7037; occupancy_dependent_transport: MAE 4.78902, worst group 11.5347.

Condition-dependent first-order response improves development prediction. Test whether that apparent timescale change is instead an amplitude/boundary confound: a shared full-slab transport scale with separate condition amplitudes may suffice. Development MAE=3.34284; worst group=10.8982; fitted parameters=4.

**attempt-008 — distributed_trapping**: Development evidence available before this fit: occupancy_dependent_transport: MAE 4.78902, worst group 11.5347; shared_fick_separate_amplitudes: MAE 3.34284, worst group 10.8982.

Test a distribution of trapping times through a shared stretched-exponential exponent. This challenges whether the simpler condition-dependent first-order surrogate misses a reproducible early/late curvature pattern. Development MAE=2.52537; worst group=6.36307; fitted parameters=5.

**attempt-009 — finite_capacity_trapping**: Development evidence available before this fit: shared_fick_separate_amplitudes: MAE 3.34284, worst group 10.8982; distributed_trapping: MAE 2.52537, worst group 6.36307.

The stretched response improves forward error. A competing finite-capacity trapping model gives algebraic rather than exponential saturation; it challenges whether the tail shape requires a distributed-timescale interpretation. Development MAE=5.11432; worst group=10.9732; fitted parameters=4.

**attempt-010 — activated_breakthrough**: Development evidence available before this fit: distributed_trapping: MAE 2.52537, worst group 6.36307; finite_capacity_trapping: MAE 5.11432, worst group 10.9732.

Test delayed diffusion-front breakthrough with an inverse-time activation form. Unlike stretched saturation, this suppresses very early response and represents arrival-time dispersion; it must improve forward groups without inventing a measured boundary concentration. Development MAE=1.51247; worst group=3.73404; fitted parameters=5.

**attempt-011 — semi_infinite_arrival**: Development evidence available before this fit: finite_capacity_trapping: MAE 5.11432, worst group 10.9732; activated_breakthrough: MAE 1.51247, worst group 3.73404.

Activated breakthrough improves development MAE to1.512μA. Test the established semi-infinite diffusion arrival solution, which imposes an erfc tail rather than an unconstrained inverse-Weibull exponent. This supplies a stronger physical-shape falsifier. Development MAE=3.42019; worst group=5.52057; fitted parameters=4.

**attempt-012 — common_breakthrough_scale**: Development evidence available before this fit: activated_breakthrough: MAE 1.51247, worst group 3.73404; semi_infinite_arrival: MAE 3.42019, worst group 5.52057.

Challenge the need for condition-dependent transport: keep separate amplitudes but require the same breakthrough time scale under both charging conditions. This controlled mechanism restriction tests whether a common effective diffusivity-shaped response is defensible. Development MAE=3.77347; worst group=11.9629; fitted parameters=4.

All substantive attempts and failures are retained. See FREEZE.json and CONFIRMATION_RECEIPT.json for chronology and exact evidence binding.
