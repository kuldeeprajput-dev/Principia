# Hydrogen adsorption: corrected excess response and bounded peaks

**Research edition: 1 October 2026. Existing final_results remain frozen.**

## Supported findings and corrected physical model

The native target is excess hydrogen uptake in wt.%, not absolute storage capacity. Three compositions EG0/EG1/EG10 supply development; whole EG5 is an exposed diagnostic. Entire temperature and adsorption/desorption curves remain together. Independent normal hydrogen density and fugacity come from the Leachman equation of state through CoolProp 7.2.0; the frozen lookup is embedded in model state, so prediction needs no CoolProp or network.

$$
q_{\mathrm{ex}}(P,T)=\sum_{j=1}^{2}A_j\frac{b_j(T)f(P,T)}{1+b_j(T)f(P,T)}-100V\rho_g(P,T),
$$

$$
b_j(T)=\exp[\ell_j+Q_j(1/T-1/(160\mathrm{K}))].
$$

With f in bar, rho in g/cm<super>3</super>, V in cm<super>3</super>/g, the displacement term is wt.%. Coefficients are A_1=1.15792, ell 1=-3.407412, Q_1=627.7136 K, A_2=5.97028, ell 2=-5.465494, Q_2=466.2582 K, V=0.870508 cm<super>3</super>/g. Q is an effective fitted thermal scale, not a measured adsorption enthalpy. V is estimated from uptake and is not an independent pore-volume measurement. Normal hydrogen is an explicit ortho/para assumption.

Whole-composition development MAE is 0.128481, versus a correctly specified ideal-density excess-Langmuir 0.141589 and real-gas one-site 0.152111. EG5 exposed diagnostic MAE is 0.201460, versus 0.208098 for the corrected ideal baseline and old 0.546458. Thus most headline improvement repairs the previous weak specification; the two-site gain over the strong ideal comparison is only 3.19% on the diagnostic. Global EG5 bias is -0.194047 wt.%, retained as a warning.

## Curve-shape and operating-quantity falsifiers

At 77 K adsorption, the corrected model's continuous peak is within 3.91 bar of the sampled EG5 maximum, much closer than the old rule. At 160/273 K the predicted and sampled maxima are at the measured upper boundary: these are not identified interior optima. The 5-to-100 bar excess-uptake swing errors are 0.44658, 0.20761 and 0.03424 wt.% at 77/160/273 K. This is an excess-curve diagnostic, not independently measured absolute deliverable hydrogen. Desorption coverage differs and cannot supply matched-pressure causal hysteresis.

Pure graphite dilution, branch offsets and temperature-dependent capacity do not improve development sufficiently. Two-site effective parameters have similar fold ranges but appreciable conditioning; fitted sites do not establish physical pore populations. The publisher README describes PSD as MIL101/GO despite MOF5/EG filenames, preventing silent admission of its cumulative volume as independent hydrogen displacement calibration.

## Value, limits and next evidence

The solid contribution is physically correct excess modeling, honest strong-baseline comparison and a much better bounded curve-shape prediction. This is known adsorption-family reproduction with a scoped retrospective approximation; no new pore mechanism, optimum-pressure law or deployed storage benefit is admitted. Independently documented pore/displacement volume, repeated freshly synthesized samples and matched operating cycles are needed for stronger claims.

## Reproduction and evaluation

Run `python run.py` to verify frozen predictions. Use `python evaluator/evaluate.py example --output /tmp/submission` and `python evaluator/evaluate.py score --submission /tmp/submission --output /tmp/report --replay` in a new output location. This trusted-code replay is not a security sandbox. Evaluator scores exposed targets and does not grant novelty from error. Exact source/sample anchors are in data/observations.csv.gz; complete numerical evidence and unfavorable models remain in evidence/.

## Sources and prior art

- [Native MOF hybrid record](https://doi.org/10.57745/KR8BIW)
- [Leachman hydrogen EOS](https://www.nist.gov/publications/fundamental-equations-state-parahydrogen-normal-hydrogen-and-orthohydrogen)
- [Dual-site MOF hydrogen prior work](https://doi.org/10.1039/D0EE02448A)

Targeted primary-source checking is not exhaustive novelty adjudication. Established model-family success is distinguished from a new physical law.
