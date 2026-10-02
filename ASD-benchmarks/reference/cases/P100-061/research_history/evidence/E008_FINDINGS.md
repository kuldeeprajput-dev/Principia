# 061: Membrane permeation - second continuation

Smaller, conservative transport closure improves error; mixture gas sign and geometry calibration matter.

**Status:** retrospective_candidate. All old confirmation outcomes were already exposed. This round fits and selects using original development groups only; no old-test scores were reopened. The original final reference package remains unchanged.

## Scientific question

A shared gas-film coefficient with length/diameter scaling transfers across the four calibrated membrane designs.

Prior evidence: The preceding model used four independent film scales; prediction alone did not distinguish membrane-specific defects from external transport.

## Completed investigations

| Version | Hypothesis / model | Primary error |
|---|---|---:|
| [cycle-001](PROTOCOL.json) | geometry_film | 0.00490599824 |
| [cycle-002](cycle-002/PROTOCOL.json) | paired_film | 0.00408759611 |
| [cycle-003](cycle-003/PROTOCOL.json) | no_gas_effect | 0.0045840887 |
| [cycle-004](cycle-004/PROTOCOL.json) | mass_only_gas | 0.00366589067 |
| [cycle-005](cycle-005/PROTOCOL.json) | linked_sherwood | 0.00342801387 |
| [cycle-006](cycle-006/PROTOCOL.json) | developing_film | 0.00333993965 |
| [cycle-007](cycle-007/PROTOCOL.json) | one_film_scale | 0.00427677033 |
| [cycle-008](cycle-008/PROTOCOL.json) | reversed_mass | 0.00620033009 |

Units: **mol m^-2 s^-1**. Exact-cohort prior best: **0.00410891989**, `previous/cycle-004`. New matched HGB: **0.00804889854**. [All models and hashes](COMPARISON.csv) and [every group](BY_GROUP.csv) are retained.

Best tested extension: `cycle-006` (0.00333993965); this is a research candidate, not fresh validation. The four favorable cases were selected before any further confirmation; see the collection selection record.

## Equation and evidence

```text
Use64cells with normalized local kappa(z) proportional z^(-1/3); keepa=0.6 and twofamily scales. This known entrance-layer approximation is not a new transport theory.
```

Full precision coefficients, calibration and fold-specific states: [cycle-006/states.json](cycle-006/states.json). Predictions and grouped scores are in the same directory. No fitted parameter variant is counted as another positive discovery.

## Scope and evaluator

The whole-group/chronological folds, targets and permitted calibration inherit the [earlier protocol](../continuation-20260930/PROTOCOL.json), with the explicit [new protocol](PROTOCOL.json) and any [shared documentation corrections](../../../_support/continuation_20260930b/READER.md). New source data are not normalized or overwritten.

Use the [shared evaluator](../../../_support/continuation_20260930b/EVALUATOR.md) for complete or explicitly abstaining submissions. It restricts every comparator to identical coverage and does not certify novelty or impact. The [collection report](../../../ASD_CONTINUATION_15_ROUND2.md) explains the strongest results and their counterexamples.

Original source/units audits and bounded prior-art reviews remain authoritative dependencies. No private reference data entered this campaign.
