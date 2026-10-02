# Executable equations

The exact frozen coefficients and feature transformations are in `rules.json` and `run.py`. No coefficient is fitted during replay.

Selected equation: P_hat(t+0.20 s) = beta_0 + sum_{j=1}^{13} beta_j * phi_j(t).

Here phi=(p0,p05,p10,p20,p30,p40,p50,di0,de0,di20,de20,p0*FEM,p0*BH). The p terms are gauge pressures at lags0,0.05,0.10,0.20,0.30,0.40 and0.50s; di and de are inspiratory/expiratory differential pressures, with0 and0.20s lags. Every pressure is in cmH2O; FEM and BH are declared trial indicators. The intercept is 0.04519408cmH2O, and the current gauge-pressure coefficient is 1.739696. All coefficients are already transformed back from training feature-RMS scaling: apply this dot product directly to the physical-unit inputs, with no additional scaling.

| Coefficient index | Value |
|---|---:|
| 0 | 0.045194079929 |
| 1 | 1.73969627178 |
| 2 | -0.426001524542 |
| 3 | -0.246147265174 |
| 4 | -0.133175859235 |
| 5 | 0.13796845256 |
| 6 | -0.0850321386862 |
| 7 | -0.0622066528154 |
| 8 | -0.296369242354 |
| 9 | -0.0375371076703 |
| 10 | 0.628367107014 |
| 11 | 0.0366539659112 |
| 12 | 0.0443104919149 |
| 13 | 0.00872955320039 |

Each model is separate from the scientific finding and evaluation task. All alternative states remain available for numerical comparison.

For the selected flexible model, the ordered feature vector is: 1, p0,p05,p10,p20,p30,p40,p50,di0,de0,di20,de20,p0*FEM,p0*BH. The predicted pressure is the dot product with the coefficient vector. All pressures are cmH2O; suffixes are lag in centiseconds.
