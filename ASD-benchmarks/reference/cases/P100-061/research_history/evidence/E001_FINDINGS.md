# Hydrogen transport through palladium-based membranes

> P100-061 · Six ASD attempts · Scoped transport-model reproduction

## 1. Scenario and available measurements

The native workbook contains 180 hydrogen-mixture tests and 96 pure-hydrogen calibration tests for four Pd/PdAg membranes, including two protective double-skin designs. Operating temperatures are 350, 400 and 450°C; inert gases are nitrogen, argon and helium. Each gas-temperature block has five operating points: three feed fractions at 5 normal L/min, and three flows at feed fraction 0.8, with the shared center counted once. Flux is already normalized by membrane area and is measured in mol s<super>-1</super> m<super>-2</super>.

## 2. Experimental method

All 400°C observations were reserved before fitting: 60 mixture targets and 32 secondary pure-hydrogen checks. Development used 120 mixture targets and 64 pure-hydrogen calibration measurements. Six development folds withheld complete gas-temperature blocks across all four membranes. Pure calibration at both development temperatures was explicitly available to every model. Six substantive attempts tested film resistance, depletion, algebraic suppression, their combination, parameter sharing and flow response. Selection and stopping were frozen before confirmation. A separately frozen nested kernel comparator challenged the initial fixed baseline.

## 3. Equation and physical interpretation

The selected compact model uses pure-hydrogen calibration and an implicit transport balance:

Define normalized absolute pressures π<sub>r</sub> = p<sub>r</sub>/(1 bar) and π<sub>p</sub> = p<sub>p</sub>/(1 bar), T<sub>0</sub> = 673.15 K, and J<sub>*</sub> = 1 mol s<super>-1</super> m<super>-2</super>.

$$
P_m(T)=J_*\exp[a_m+b_m(T_0^{-1}-T^{-1})]
$$

$$
z=\dfrac{JA}{F_{\rm mol}},\qquad \bar{x}=\dfrac{x-z/2}{1-z/2},\qquad \pi_s=\pi_r\bar{x}-\dfrac{J}{\kappa}
$$

$$
J=P_m(T)[\max(\pi_s,\pi_p)^{n_m}-\pi_p^{n_m}]
$$

$$
\kappa=K_mG_g\left(\dfrac{F}{5\,{\rm normal\ L/min}}\right)^{0.6}\left(\dfrac{T}{T_0}\right)^{1.75}
$$

Here T is kelvin, x the feed mole fraction, A the membrane area and F the normal feed flow. F<sub>mol</sub> = F/(60 × 22.414) mol/s when F is expressed in L/min. The positive root respects the available-feed bound. P and κ have flux units; a and n are dimensionless and b is kelvin. This notation exactly matches the implementation's numerical absolute-bar convention. Four K<sub>m</sub> values are 0.31238, 0.35015, 0.63131 and 0.60419 in flux units; G<sub>N2</sub> = 1, G<sub>Ar</sub> = 0.97902 and G<sub>He</sub> = 1.07867. Every coefficient is in `rules.json`.

This equation expresses established depletion and resistance mechanisms. The midpoint convention is an approximation, and κ combines unmeasured transport effects; these parameters do not identify a unique causal mechanism.

<!-- pagebreak -->

## 4. Findings and predictive performance

The primary metric is mean absolute flux error within each reserved gas group, then averaged equally over the three groups. Every model predicts the same 60 observations with identical calibration access.

| Frozen model | MAE (mol s<super>-1</super> m<super>-2</super>) |
|---|---:|
| Coupled transport model, attempt 004 | 0.012896 |
| Membrane-specific mixture mean | 0.044782 |
| Calibrated Sieverts/Arrhenius | 0.176675 |
| Calibrated Richardson/Arrhenius | 0.159518 |
| Fixed RBF calibration correction | 0.006740 |
| Nested RBF calibration correction | **0.001688** |

The compact model lowers error by 91.92% against the pressure/permeance-only Richardson model and by 71.20% against the membrane mean. Its gas-group errors are 0.012269 (Ar), 0.013340 (He) and 0.013081 (N₂). The flexible comparator is substantially more accurate, so predictive superiority of the compact equation is unsupported.

Pure calibration gives pressure exponents 0.633-0.668, consistent with a departure from the ideal diffusion-only exponent 0.5. On the 32 reserved pure-hydrogen points, Richardson calibration has MAE 0.003738. This reproduces an existing relationship rather than discovering a new law.

## 5. Value, characteristics and limits

The interpretable model provides a physically bounded screening estimate for these calibrated membranes; the flexible comparator gives the strongest reference predictions. Neither result establishes process savings, new-membrane transfer or universal separator design rules.

Positive roots, feed conservation and matched-input flow monotonicity passed structural checks. Conditional depletion profiles changed the fitted film coefficients and favored stronger depletion in sample; the midpoint value was not inferred as a physical constant. A 22.414-to-24.465 L/mol normal-volume sensitivity changed development predictions by mean 0.002217, so the source’s unspecified flow convention limits absolute transport interpretation.

Flow and composition are separately varied only along two intersecting operating slices, not a full factorial grid; their interaction is weakly identified. Four specimens and three gas groups at one reserved temperature support within-system interpolation. No replicate uncertainty or independent thickness measurements are supplied, and source publications already discuss concentration polarization, depletion and non-ideal pressure exponents. No novel physical principle is admitted.

## 6. Evidence and use

`run.py` reproduces six frozen models; `rules.json`, aligned data and compact CSV evidence retain exact coefficients and source anchors. The evaluator assesses future submissions under the same exposed reference protocol. `research_history/` preserves all six attempts, controls and the baseline-strength amendment. All final targets are now exposed.

Source: Ververs, Arratibel, Di Felice and Gallucci, [Zenodo 10691625](https://zenodo.org/records/10691625), CC BY 4.0. Prior analysis: [Ververs et al., International Journal of Hydrogen Energy (2024)](https://doi.org/10.1016/j.ijhydene.2024.04.337).
