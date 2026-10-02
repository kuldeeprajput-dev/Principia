# Josephson junctions: geometry scaling and its failure cases

## Scenario and task

The Heidelberg source provides voltage/current waveforms for junctions on two wafers. We reconstruct 76 unambiguously named junctions on 19 dies. The task predicts effective high-current resistance from nominal width and wafer/region metadata, before electrical characterization. Resistance is the mean slope in the lower and upper current quintiles. Generator voltage is divided by the source-specified 100 ohm resistance. The response-channel gain is undocumented, so these are **recorded-channel ohms**, not certified intrinsic junction resistances.

Fourteen complete dies were used for development and five hash-selected dies for confirmation. All widths from one die stay together. The ambiguous `1_0_2um` filename is excluded by a metadata-only rule. Five attempts tested width loss, perimeter conductance, wafer-dependent widths, region effects and a simplified wafer prefactor. Confirmation was opened only after models and stopping were frozen.

## Findings and interpretation

The preselected reference reproduces the established area-scaling form:

$$
\widehat R = A\left(\frac{w}{1\,\mu\mathrm{m}}\right)^{-2},\qquad A=1602.846063\,\Omega.
$$

Here nominal design width is $w$. The model is consistent with conductance proportional to nominal junction area when barrier and acquisition conditions are comparable. It is a useful coarse reference, **not a new physical law**. It does not establish an oxide thickness, critical-current density or microscopic edge mechanism.

|Frozen model|Development MAE (ohm)|Confirmation MAE (ohm)|
|---|---:|---:|
|Inverse-area reference|2137.90|766.27|
|Constant reference|2369.24|975.58|
|Flexible geometry control|5413.87|1237.10|

The primary metric averages junction absolute errors within each die, then weights dies equally. Inverse area reduces confirmation error by 21.5% relative to the constant, but it remains inaccurate for important devices. Confirmation die errors are 3096.46, 56.51, 78.03, 137.20 and 463.16 ohm. A 140852.67 ohm development junction remains included. Its upper/lower tail slopes differ by only about 2.6%, so directional slope asymmetry does not explain away the anomaly.

**Useful negative result:** none of the added edge/wafer/region hypotheses improved development selection. The common width correction collapsed near zero; richer terms lacked stable transfer. One region model scores slightly better after confirmation, but it remains a diagnostic comparator and is not promoted. These data support coarse geometry scaling plus explicit failure cases; they do not justify a universal yield or reliability rule.

## Scope, value and reproducibility

This task supports screening model comparisons within the two measured wafers. It does not demonstrate fabrication savings, new-wafer transfer or causal process optimization. Obtain calibrated response gain, measured junction dimensions and failure metadata before attributing anomalies to barrier physics. With five held dies, report individual results rather than row-based population confidence.

`rules.json` contains every frozen coefficient and equation; `run.py` verifies predictions and metrics. `data/observations.csv.gz` identifies native ZIP members and endpoint extraction. `evidence/by_group.csv` retains every group. The collection evaluator accepts different equations under the same input budget. All packaged outcomes are now exposed.

Source: Stoll et al., [Zenodo 22113590](https://zenodo.org/records/22113590), CC BY 4.0. The source states that the data were already analyzed for a submitted publication; an accessible full source paper was not linked in the inspected record. No definitive novelty claim is made.
