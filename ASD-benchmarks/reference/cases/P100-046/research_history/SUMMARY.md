# P100-046: Local electron-temperature closure

5 substantive attempts; selected reference **attempt_003**. Primary units: eV.

| Model | Development MAE | Complexity | Confirmation MAE |
|---|---:|---:|---:|
| adiabatic | 4.136326 | 0 | 2.662154 |
| cgl | 1.915109 | 0 | 1.454935 |
| persist | 2.449774 | 0 | 1.541007 |
| rbf | 2.273772 | 25 | 1.320566 |
| attempt_001 | 1.936528 | 1 | 1.159812 |
| attempt_002 | 2.005227 | 1 | 1.454534 |
| attempt_003 | 1.868328 | 2 | 1.174159 |
| attempt_004 | 1.866079 | 3 | 1.168273 |
| attempt_005 | 1.944592 | 3 | 1.320078 |

Attempt4 is within1% of the two-exponent closure with one extra coefficient; attempt5 worsens transfer. No identifiable anisotropy or beta-regime improvement justifies continuation.

A two-exponent local closure using density and field ratios improves confirmation error over persistence, fixed CGL scaling and the nonlinear control. The fitted density exponent is negative. That is a local empirical association along a spacecraft trajectory, not an independently identified thermodynamic polytropic index.

Current density and magnetic field are allowed, so this is a contemporaneous closure rather than future-state forecasting. Eulerian spacecraft samples are not tracked fluid parcels. Two held blocks and one orbit segment do not establish a universal plasma law.
