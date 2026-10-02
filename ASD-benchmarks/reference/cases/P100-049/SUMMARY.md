# P100-049 exploration summary

The source contains measured Li-graphite half-cell GITT and POCV exports. This task uses the GITT campaign only. A completed current pulse is followed by a long rest; the practical question is whether two early rest-voltage observations can forecast the subsequent30minutes.

The strongest development-selected rule is finite-pulse diffusion, with no fitted global coefficient. Its reserved MAE is0.686mV, a12.2% improvement over the constrained flexible control and80.1% over persistence. The advantage is specific to MAE: its RMSE and worst-block error are worse than the flexible control. This is a useful scoped forecasting result, not a newly discovered universal electrochemical law.

Let g(t)=√(t+T)−√t. Eliminating the unknown amplitude and equilibrium offset from U(t)=U∞+A g(t) gives Û(t)=U_b+(U_b−U_a)[g(t)−g(b)]/[g(b)−g(a)]. Here T is the measured pulse duration and a,b are the actual causal calibration times. The cancellation explains both its simplicity and why it cannot identify a unique diffusivity.

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


## Attempt history

**attempt-001 — finite_pulse_diffusion**: Attempt1: finite-duration diffusion relaxation fixes its shape from the measured pulse duration; it can extrapolate voltage increments without identifying equilibrium voltage or diffusivity. Development MAE=0.000391423; worst group=0.00130773; fitted parameters=0.

**attempt-002 — learned_rc**: Attempt2: finite-pulse diffusion reduced chronological MAE to0.391mV versus fixedRC1.398mV. A competing lumped charge-transfer RC mechanism could explain that improvement through a fitted timescale rather than distributed diffusion. Development MAE=0.000670335; worst group=0.00184043; fitted parameters=1.

**attempt-003 — fractional_tail**: Attempt3: learnedRC remains worse(0.670mV) than finite-pulse diffusion(0.391mV). Test a scale-free distribution of relaxation times through a fractional algebraic tail, which removes pulse-duration geometry and estimates its exponent. Development MAE=0.000459116; worst group=0.00147082; fitted parameters=1.

**attempt-004 — diffusion_rc_mixture**: Attempt4: fractional tail did not improve finite-pulse diffusion; test superposed charge-transfer and diffusion channels. A nonzero fast-channel contribution should improve transfer if the60–120s calibration still contains RC contamination; otherwise the extra mechanism is unsupported. Development MAE=0.000391423; worst group=0.00130773; fitted parameters=2.

**attempt-005 — boundary_storage**: Attempt5: the two-channel mixture collapses to diffusion and provides no benefit. Test whether voltage-dependent chemical storage breaks shape invariance: a bounded affine gain in causal120s voltage represents local variation of chemical capacitance. Failure on forward blocks falsifies its useful transfer, not the existence of graphite staging. Development MAE=0.000392807; worst group=0.00153442; fitted parameters=2.

All substantive attempts and failures are retained. See FREEZE.json and CONFIRMATION_RECEIPT.json for chronology and exact evidence binding.
