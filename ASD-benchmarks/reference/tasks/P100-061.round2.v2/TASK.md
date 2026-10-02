# P100-061.round2.v2

Documentation correction of P100-061.round2.v1. Native values, coefficients, grouping and numerical evidence are unchanged. No new fitting or confirmation.

**Target.** Measured hydrogen permeation flux

**Target units.** mol s^-1 m^-2

**Metric kind.** mae

**Timing contract.** Predict measured mixture hydrogen flux from membrane/gas identity, imposed temperature, feed fraction, absolute pressures, normal feed flow, geometry and the declared pure-hydrogen calibration_j0. Mixture-response targets from the outer held gas-temperature block cannot be used to fit that block.

**Calibration.** All models may use the 64 pure-hydrogen measurements at 350/450 °C through their explicitly frozen pressure/permeance calibration, including calibration at the temperature of a held mixture block. Mixture coefficients are fitted outside that held block. No 400 °C response enters this development-OOF task. The normal molar volume 22.414 L/mol is a declared convention; pressure units are absolute bar.

**Independent unit.** Complete inert-gas by temperature block across four calibrated membranes: Ar/He/N2 at 350/450 °C, six outer groups and 120 mixture observations.

**Scope limits.** Repeatedly exposed original-development out-of-fold cohort, distinct from the original 60-observation 400 °C reserved mixture cohort. Four calibrated specimens, two geometry families and two development temperatures do not establish new-membrane or general geometry transfer. Pure-gas calibration is permitted at both development temperatures; source normal-flow convention and unobserved annular-gap geometry limit causal film interpretation.

## Permitted inputs

| Input | Units |
|---|---|
| temperature_K | K |
| feed_fraction | mol H2 per mol feed, fraction |
| normal_flow_L_min | normal L min^-1; assumed 22.414 L mol^-1 |
| retentate_bar | bar, absolute |
| permeate_bar | bar, absolute |
| area_m2 | m^2 |
| calibration_j0 | mol H2 m^-2 s^-1; frozen pure-hydrogen calibration |
| membrane | categorical calibrated membrane |
| gas | categorical N2, Ar or He |
| membrane_index | dimensionless index of declared calibrated membrane |

Current outcomes are exposed. Alternatives may use the same information budget; different endpoints require a distinct reviewed contract.
