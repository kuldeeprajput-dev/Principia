# Complete frozen equation register

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


