# Heterostructure FETs: sparse calibration of transfer-curve shape

## Scenario and task

The source Fig. 2 e table contains 36 measured NbS2-MoS2 FET transfer curves, with 201 gate voltages from -20 to 20 V. These are transistor measurements, distinct from the source's memory retention tests and device simulations. The source describes 10 micrometre channels and nominal 50 mV drain bias.

The task reconstructs current after obtaining **three same-device calibration currents**, at -20, 0 and 20 V. Those anchors are excluded from scoring. This is offline sparse characterization, not uncalibrated prediction or a forward sweep forecast. Twenty-seven whole devices were used for development and nine hash-selected devices for confirmation, with 198 scored points per device. Seven adaptive attempts compared power curvature, smooth turn-on, separate regimes, contact saturation, calibration-dependent curvature, cubic bending and template shrinkage. The selected equation and stopping were frozen before confirmation.

## Calibrated shape finding

Let $I_-$, $I_0$, and $I_+$ denote the measured calibration currents in microamperes. Define

$$
r=\mathrm{clip}\left(\frac{I_0-I_-}{I_+-I_-},10^{-9},1\right),\qquad
p=\mathrm{clip}\left(1.963555864-(1.2894033\times10^{-2})\log r,0.1,8\right).
$$

For positive gate voltage, the selected compact response is

$$
\widehat I(V)=I_0+(I_+-I_0)\left(\frac{V}{20\,\mathrm{V}}\right)^p.
$$

For negative voltage, use $\widehat I=I_-+(I_0-I_-)[(V+20\,\mathrm{V})/(20\,\mathrm{V})]^q$, with $q=12$. Full numerical precision and clipping are in `rules.json`. The current floor in the ratio denominator is a fixed numerical safeguard, not a fitted physical parameter.

The calibration ratio supplies threshold/turn-on information beyond an overall current scale. This gives a **scoped predictive extension** within the measured array. It is not a microscopic mobility or contact-resistance identification. In particular, near-quadratic gate curvature at low drain bias is not proof of a saturation-regime square law.

|Frozen model|Development MAE (uA)|Confirmation MAE (uA)|
|---|---:|---:|
|Calibration-dependent exponent|0.016647|0.016304|
|Training-only normalized template|0.018067|0.017657|
|Shared power exponent|0.019210|0.018139|
|Piecewise linear interpolation|0.166101|0.170782|

Errors are mean absolute current errors within each device, then equally averaged across devices. The selected equation improves 7 of 9 held devices over the strong template control, with 7.7% lower average error. Individual selected-model errors range from 0.00608 to 0.02975 uA. This is not an invented percentage accuracy or evidence of deployed production savings.

## Counterexamples and limits

The source already established transport quality and device uniformity. This analysis adds a reserved-device calibration test, not a newly discovered material mechanism. A contact-saturation extension did not help and its coefficient approached zero. The negative-gate exponent hit its allowed upper bound: off-regime current contributes very little physical-unit error, so that exponent is weakly identified and should not receive a microscopic interpretation. Two held devices favor the flexible template. Independent fabrication lots and operational measurement-cost trials were not tested.

Run `python run.py` to reproduce all frozen predictions and metrics. Exact sample columns, calibration anchors, coefficients and competing results are in the data and evidence directories. The shared evaluator accepts alternative equations with the same three-anchor budget. Outcomes are now exposed to future agents.

Sources: Wang et al., [Nature Electronics (2026)](https://www.nature.com/articles/s41928-026-01634-z); [Zenodo 19003428](https://zenodo.org/records/19003428), CC BY 4.0. The literature check was targeted, not an exhaustive novelty review.
