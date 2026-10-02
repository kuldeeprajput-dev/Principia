# P100-057.round2.v2

Documentation correction of P100-057.round2.v1. Native values, coefficients, grouping and numerical evidence are unchanged. No new fitting or confirmation.

**Target.** Next-temperature-block viscosity

**Target units.** cP

**Metric kind.** mae

**Timing contract.** Before each temperature block after the first, predict viscosity from current imposed temperature/shear settings and measured viscosity at the corresponding ordinal shear point in the completed previous and first blocks of the same Test ID. Blocks are ordered by native Result Start Time. Previous shear rate is supplied explicitly because matched ordinal points can differ in actual rate. No current-block or future target response enters predictors.

**Calibration.** Permitted within-Test-ID causal history comprises eta_previous, eta_first, T_previous, previous_shear_s and first_shear_s. Model coefficients are fitted only on the applicable outer training Test IDs. Historical static-reference formulation amplitudes and activation coefficients belong to separate comparator states, not a blanket calibration rule for the history task. Signed and extreme native outcomes remain in physical-unit scoring.

**Independent unit.** Whole Test ID across all temperature/shear blocks; 40 original-development Test IDs contribute 9,000 out-of-fold rows. Synthesis lots are not identified.

**Scope limits.** Retrospective, repeatedly exposed development out-of-fold cohort on already represented formulations. The original ten reserved Test IDs are not this task cohort. Causal within-test history is explicitly allowed, so comparison to the static task is not an algorithm-only improvement. Thermal order, aging and formulation effects remain confounded; no equilibrium constitutive or independent-lot law is established.

## Permitted inputs

| Input | Units |
|---|---|
| T_C | degC |
| shear_s | s^-1 |
| T_previous | degC |
| eta_previous | Pa s |
| eta_first | Pa s |
| previous_shear_s | s^-1 |
| first_shear_s | s^-1 |
| formulation | source label; calibrated category |

Current outcomes are exposed. Alternatives may use the same information budget; different endpoints require a distinct reviewed contract.
