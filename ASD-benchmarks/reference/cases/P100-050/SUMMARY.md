# P100-050 exploration summary

The source provides high-frequency analog-laser measurements from five controlled gate releases, together with additional rangefinder data and the authors’ swath-processing script. This task keeps the analog depth measurements at the 33 m station in their native units and predicts the signal 200 ms ahead. It uses causal recent history, without future-peak alignment or target smoothing.

Five mechanistic or measurement hypotheses were tested after the baseline controls. The development-selected oscillatory memory model achieves 12.228 mm reserved MAE, beating the flexible control (13.688 mm) but losing to simple native persistence (11.667 mm). It therefore does not earn a positive claim of improved general prediction. The clearest supported finding is negative: unattenuated slope extrapolation roughly doubles error relative to persistence.

The oscillatory equation ĥ=h+v sin(ωH)/ω+a[1−cos(ωH)]/ω² propagates a local level, slope and curvature over H=0.2 s. Its fitted ω is an effective forecast parameter, not an independently measured flow-mode frequency. This distinction prevents a useful equation comparison from becoming a false constitutive-law claim.

| Model | Development MAE | Reserved MAE | Reserved worst-group MAE |
|---|---:|---:|---:|
| constant_velocity | 0.0289558 | 0.0231933 | 0.0231933 |
| flexible | 0.0142275 | 0.0136883 | 0.0136883 |
| persistence | 0.0137181 | 0.0116672 | 0.0116672 |
| damped_velocity | 0.013819 | 0.0120813 | 0.0120813 |
| oscillatory_memory | 0.0132228 | 0.0122284 | 0.0122284 |
| depth_dependent_memory | 0.0138252 | 0.0120793 | 0.0120793 |
| front_recession_asymmetry | 0.0138483 | 0.0120813 | 0.0120813 |
| robust_surface_level | 0.0139806 | 0.0121693 | 0.0121693 |


## Attempt history

**attempt-001 — damped_velocity**: Attempt1: front-height increments decorrelate through a dissipative velocity memory; exponential damping may prevent constant-velocity overshoot. Development MAE=0.013819; worst group=0.0160151; fitted parameters=1.

**attempt-002 — oscillatory_memory**: Development evidence available before this fit: damped_velocity: MAE 0.013819, worst group 0.0160151.

Damped drift did not beat native persistence. Test a competing local oscillatory-wave explanation: displacement, velocity and curvature propagate as a harmonic mode, rather than monotone relaxation. Development MAE=0.0132228; worst group=0.0153772; fitted parameters=1.

**attempt-003 — depth_dependent_memory**: Development evidence available before this fit: damped_velocity: MAE 0.013819, worst group 0.0160151; oscillatory_memory: MAE 0.0132228, worst group 0.0153772.

A flow-depth-dependent decorrelation scale tests the expectation that advective/wave speed changes with square-root depth. This remains an effective local forecast, not direct measurement of wave speed. Development MAE=0.0138252; worst group=0.0159915; fitted parameters=1.

**attempt-004 — front_recession_asymmetry**: Development evidence available before this fit: oscillatory_memory: MAE 0.0132228, worst group 0.0153772; depth_dependent_memory: MAE 0.0138252, worst group 0.0159915.

Test separate rising-front and recession memories: arrival may retain its slope longer than turbulent drawdown. A useful asymmetry must transfer as a complete-run prediction gain. Development MAE=0.0138483; worst group=0.0160151; fitted parameters=2.

**attempt-005 — robust_surface_level**: Development evidence available before this fit: depth_dependent_memory: MAE 0.0138252, worst group 0.0159915; front_recession_asymmetry: MAE 0.0138483, worst group 0.0160151.

Test a competing observation mechanism: short-lived laser/surface spikes, rather than deterministic flow acceleration, may explain persistence errors. A causal20ms median with no fitted parameter estimates persistent local surface level. Development MAE=0.0139806; worst group=0.0161235; fitted parameters=0.

All substantive attempts and failures are retained. See FREEZE.json and CONFIRMATION_RECEIPT.json for chronology and exact evidence binding.
