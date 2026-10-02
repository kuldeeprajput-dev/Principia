# Executable equations

The exact frozen coefficients and feature transformations are in `rules.json` and `run.py`. No coefficient is fitted during replay.

Selected equation: Ihat=I(.75)+max(A+B*I(.4)-I(.75),0)*(Ca-.75)/(K+Ca-.75); exact unit depletion coefficient.

| Coefficient index | Value |
|---|---:|
| 0 | 148.32641679 |
| 1 | -1.48768394348 |
| 2 | 0.798307532989 |

Each model is separate from the scientific finding and evaluation task. All alternative states remain available for numerical comparison.

Let u=I(0.4mM), v=I(0.75mM), d=C-0.75mM. The conserved reserve reference is I_hat=v+max(A+B*u-v,0)*d/(K+d), when selected. A is nA, B dimensionless and K mM. Numerical values are the frozen coefficient vector in this order. Other selected forms are identified explicitly above.
