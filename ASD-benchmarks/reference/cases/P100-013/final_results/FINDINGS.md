# P100-013 - Two-channel encapsulant cure kinetics

## Scenario and task

The seven native workbooks combine differential scanning calorimetry, infrared and Raman spectroscopy, and rheology. This task uses observed DSC conversion from five constant heating rates; author-fitted columns are excluded. Spectroscopy and rheology provide source context, not independent validation of the fitted kinetic channels.

## Experimental and validation design

The prediction target is dimensionless conversion, alpha. Temperature T is in kelvin and heating rate beta in K/min. Four full traces at 1, 3, 5 and 10 K/min support leave-one-rate-out development; the complete 20 K/min trace is reserved. No measured conversion is an input. All 501 confirmation rows belong to one experiment, so there is no population confidence interval.

At least five adaptive attempts preceded a code-and-state freeze; confirmation was then evaluated without fitting or reselection. Source publications and supplied analyses are known. All packaged outcomes are now exposed to later users.

## Frozen equation and interpretation

Let the reference temperature be $T_r=423.15\,\mathrm{K}$ and $R=8.314462618\,\mathrm{J\,mol^{-1}\,K^{-1}}$. For each channel,

$$
q_j(T,\beta)=\frac{k_{j,r}}{\beta}\int_{273.15}^{T}\exp\!\left[\frac{E_j}{R}\left(\frac{1}{T_r}-\frac{1}{u}\right)\right]du,
\qquad \widehat\alpha=w(1-e^{-q_1})+(1-w)(1-e^{-q_2}).
$$

The energies are 133.625 and 67.794 kJ/mol, reference log-rates are-3.30765 and -4.06157, and w=0.555544. Full precision is in rules.json. The integration limit is a fixed 273.15 K reference, not a fitted onset. This is a bounded phenomenological kinetic mixture; channels are not assigned to chemical species.

<!-- pagebreak -->

## Evidence and limitations

The primary metric is the equally weighted mean of within-group mean absolute errors in conversion fraction; sample counts do not create independent replicates.

| Model | Development MAE | Confirmation MAE |
|---|---:|---:|
| First-order Arrhenius control | 0.047399 | 0.0752806 |
| Shifted-logistic control | 0.0384896 | 0.0836005 |
| General reaction order | 0.0394337 | 0.084525 |
| Avrami-type conversion | 0.0457055 | 0.076912 |
| Two-channel mixture (selected) | 0.0273381 | 0.0589466 |
| Shared-barrier mixture | 0.0347738 | 0.0766603 |
| Inaccessible-fraction model | 0.0373012 | 0.0684777 |


Selected-reference group errors: rate 20: 0.0589466.

A shared activation barrier gives development MAE 0.03477 rather than 0.02734, supporting the predictive usefulness of distinct temperature responses. The full-fit Jacobian condition is 771, and only four heating histories constrain five parameters, so individual energies are not unique chemical constants. A single inaccessible-fraction alternative fails to improve transfer. The confirmation error is 0.05895 conversion units, or 5.895 percentage points; this is error, not percentage accuracy.

## Practical meaning and reproducibility

The two-channel model offers a compact cure-schedule interpolation/extrapolation reference and reduces error on the faster reserved ramp. It does not certify complete cure, component reliability, processing yield or a new reaction mechanism. A second material batch, isothermal schedules and independent chemical measurements are needed before process qualification.

Run `python run.py` to check hashes and reproduce every saved equation, prediction and metric. `rules.json` holds all coefficients, parameter names and fit scope; `findings.json` separates supported claims, failed hypotheses and abstentions. The shared benchmark evaluator accepts alternative equations under this same information budget; exact agreement with this reference is not required.

## Sources

[NIST source publication](https://www.nist.gov/publications/advanced-characterization-cure-kinetics-liquid-encapsulant)

[NIST data record](https://data.nist.gov/od/id/mds2-3702)

