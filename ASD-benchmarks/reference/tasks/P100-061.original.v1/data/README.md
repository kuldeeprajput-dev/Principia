# Prepared membrane-flux task

The input table contains all 60 reserved mixture observations at 400 degrees Celsius, across four previously calibrated membranes and three inert gases. `observations.csv.gz` retains measured hydrogen flux in mol s^-1 m^-2 and exact workbook, sheet, row and cell anchors. Inputs and responses are joined by `sample_id`; `group` identifies each complete gas block and is not a scientific predictor.

| Input | Units and meaning |
|---|---|
| `membrane_index` | Integer 0–3, identifying the calibrated source membrane |
| `gas` | N2, Ar or He |
| `temperature_K` | Kelvin |
| `feed_fraction` | Hydrogen mole fraction, 0 < x <= 1 |
| `normal_flow_L_min` | Normal L/min; the frozen model assumes 22.414 L/mol |
| `retentate_bar`, `permeate_bar` | Absolute bar |
| `area_m2`, `diameter_m` | Membrane area in m² and diameter in m |

Pure-hydrogen calibration at 350/450 degrees Celsius is serialized in `rules.json` and available identically to every comparator. Neither mixture flux nor reserved 400-degree pure-hydrogen measurements enter prediction inputs. Source flux is already area-normalized.

These are pilot-prepared analysis products; native workbooks remain unchanged. See `FINDINGS.md` for source-header corrections, calibration and identifiability limits. Operating points form two intersecting flow/composition slices, not a full factorial experiment. All targets are now exposed; this package supports retrospective comparison, not fresh blind confirmation.
