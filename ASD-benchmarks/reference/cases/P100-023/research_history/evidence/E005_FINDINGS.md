# Finger-liquid friction: a person-transfer rule with fluid limits

**Research edition: 1 October 2026. Existing final_results remain frozen.**

## Supported findings and the competing explanation

The original source reports a full Stribeck collapse and its high-H exponent 0.55. This continuation fits both branch exponents only on the original development participants, removing that source fitted exponent advantage. The pressure-conditioned candidate is

$$
\widehat\mu=a+b h^{-p}\pi^r+c h^q,\qquad h=H/0.02,\quad\pi=(F_N/1\mathrm{N})/(A/4\mathrm{cm}^2).
$$

Here A is photographic pad area, not the instantaneous loaded contact area. Frozen coefficients are a=2.5790e-11, b=0.126335, c=0.0405567, p=0.263105, q=0.754523, r=-0.322758. At fixed author H, the boundary contribution decreases with normalized force/area. The sign is negative in 9/9 participant-fold fits, ranging-0.454 to-0.163. However H itself contains inverse force; these observational data do not identify causal pressure physics.

Whole-person development MAE is 0.077064 versus 0.078925 without pressure and 0.104467 with fixed original exponents. The exposed two-person diagnostic gives 0.084917, versus 0.097362 fixed-exponent and 0.081720 kernel control. The kernel has lower diagnostic error; it is not promoted after exposure.

The stricter development-only challenge removes both a person and the tested fluid from training. Pressure MAE rises to 0.120469, versus 0.090762 without pressure. This falsifies a transferable fluid-independent pressure law. The free-exponent curve is the better structural explanation for unseen-fluid development stress, but the original preselected same-fluid candidate is preserved. Fixed 500/s viscosity Hersey also loses to the shear-thinning source Hersey, reproducing the importance of rheology calibration rather than discovering it.

## Value, limits and next evidence

The value is a more honest source-exponent comparison and a concrete example of participant-transfer gains failing fluid transfer. Hydration additions do not improve the main development task. Fixed fluid order, one substrate, trial-median target and shared fluid calibrations prevent prospective formulation or causal skin-state claims. No new universal friction law or deployed benefit is admitted. Randomized repeated fluid trials and independent contact geometry are needed before promotion.

## Reproduction and evaluation

Run `python run.py` to verify frozen predictions. Use `python evaluator/evaluate.py example --output /tmp/submission` and `python evaluator/evaluate.py score --submission /tmp/submission --output /tmp/report --replay` in a new output location. This trusted-code replay is not a security sandbox. Evaluator scores exposed targets and does not grant novelty from error. Exact source/sample anchors are in data/observations.csv.gz; complete numerical evidence and unfavorable models remain in evidence/.

## Sources and prior art

- [Native record](https://zenodo.org/records/15365365)
- [Original Stribeck study](https://link.springer.com/article/10.1007/s11249-025-02024-w)

Targeted primary-source checking is not exhaustive novelty adjudication. Established model-family success is distinguished from a new physical law.
