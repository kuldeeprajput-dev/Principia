# P100-068 exploration summary

The archive contains 31 raw laser-Doppler voltage traces and paired noise-reduced representations from an acoustically levitated object. This task forecasts the raw voltage 5 ms ahead, using only a 15 ms causal delay history and an initial offset calibration. The paired GHKSS outputs never serve as targets or predictors. Most stored traces use a 0.5 ms step; trace1172 uses 1 ms, and the adapter preserves both grids while maintaining the physical forecast horizon.

The strongest development-selected result is the constrained seven-coefficient delay predictor, with 0.109 V reserved MAE across six traces. This is a reproducible forecast reference, not a discovered mechanical law. A useful complementary result is that a DC-invariant harmonic recurrence reduces reserved error from 0.197 to 0.133 V and largely removes systematic bias.

For a known constant-plus-harmonic signal, the recurrence is V̂=offset+(1+2cosωh)y₀−(1+2cosωh)y₁+y₂, with h=0.005 s and yⱼ the centered voltage at j delayed steps. Its coefficients sum to one, preserving a constant level. The measured improvement tests the relevance of that invariance, rather than claiming the identity is new.

The source paper and supplied code disagree on the LDV velocity conversion. Consequently, voltage remains the endpoint, and fitted nonlinear delay coefficients are not labeled as damping, stiffness or mechanical force coefficients. Whole-trace transfer in one installation is the maximum supported scope.

| Model | Development MAE | Reserved MAE | Reserved worst-group MAE |
|---|---:|---:|---:|
| driven_harmonic | 0.241871 | 0.213469 | 0.726943 |
| flexible | 0.105944 | 0.109126 | 0.190553 |
| persistence | 0.520368 | 0.438805 | 0.585286 |
| effective_harmonic | 0.222198 | 0.197191 | 0.589883 |
| dc_invariant_harmonic | 0.162204 | 0.133286 | 0.21399 |
| duffing_delay_closure | 0.188062 | 0.185089 | 0.466788 |
| quadratic_drag_closure | 0.18744 | 0.186061 | 0.470078 |
| parametric_drive_closure | 0.165916 | 0.191568 | 0.453074 |


## Attempt history

**attempt-001 — effective_harmonic**: Attempt1: a fitted effective harmonic frequency tests whether the raw voltage evolution is dominated by the assumed32Hz drive or a shifted response mode. Development MAE=0.222198; worst group=0.400385; fitted parameters=1.

**attempt-002 — dc_invariant_harmonic**: Development evidence available before this fit: effective_harmonic: MAE 0.222198, worst group 0.400385.

The effective harmonic has substantial positive bias. Test a distinct calibration explanation: initial-window centering is phase-dependent, so enforce exact invariance to a constant voltageoffset through a third-order harmonic-plus-DC recurrence. Development MAE=0.162204; worst group=0.227994; fitted parameters=1.

**attempt-003 — duffing_delay_closure**: Development evidence available before this fit: effective_harmonic: MAE 0.222198, worst group 0.400385; dc_invariant_harmonic: MAE 0.162204, worst group 0.227994.

Test an amplitude-dependent cubic restoring closure in the voltage-delay embedding. It is inspired by Duffing dynamics but cannot be interpreted as mechanical displacement-force coefficients because the voltage conversion is unresolved. Development MAE=0.188062; worst group=0.43015; fitted parameters=4.

**attempt-004 — quadratic_drag_closure**: Development evidence available before this fit: dc_invariant_harmonic: MAE 0.162204, worst group 0.227994; duffing_delay_closure: MAE 0.188062, worst group 0.43015.

Compete with cubic restoring force using amplitude-dependent quadratic damping in the delayed voltageincrement. This tests the sourcepaper’s qualitativevelocity-nonlinearitytheme without claiming its physical units or reusing its fittedcoefficients. Development MAE=0.18744; worst group=0.42435; fitted parameters=4.

**attempt-005 — parametric_drive_closure**: Development evidence available before this fit: duffing_delay_closure: MAE 0.188062, worst group 0.43015; quadratic_drag_closure: MAE 0.18744, worst group 0.42435.

Test whether the known32Hz drive modulates response beyond autonomous delay dynamics. Both sine and cosine quadratures are allowed, but a shared clock-phase relation must transfer across entire acquiredtraces. Development MAE=0.165916; worst group=0.408667; fitted parameters=5.

All substantive attempts and failures are retained. See FREEZE.json and CONFIRMATION_RECEIPT.json for chronology and exact evidence binding.
