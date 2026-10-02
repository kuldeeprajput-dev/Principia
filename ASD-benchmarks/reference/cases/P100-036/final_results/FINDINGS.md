# Tomato stress: a compact photosynthetic-readout relation

## Scenario and endpoint

The source provides 347 integrated imaging/laboratory observations from 81 plants, two dwarf tomato cultivars and control, salt and drought treatments. Source RGB morphology and chlorophyll-fluorescence traits are already extracted by the authors. Repeated observations of one plant remain together: 65 development plants, 16 reserved plants (66 observations). Development uses five whole-plant folds.

The response is the author-reported maximum quantum yield, **QY_max**, dimensionless and bounded by 0-1. Inputs are contemporaneous source NPQ_Lss, Rfd_Lss, RGB greenness NGRDI, morphology and known cultivar/treatment. This is a source-derived imaging diagnostic, not an independent molecular or hydration assay. Before fitting, we abandoned the proposed RWC target because its fraction/percent convention was undocumented. We also excluded DAS/age: the main workbook says days after sowing while the author’s code says days after stress. No source value was repaired or silently reinterpreted.

## Selected equation

Define $q=\operatorname{asinh}(\mathrm{NPQ})$, $r=\mathrm{Rfd}/(1+|\mathrm{Rfd}|)$, $g=\mathrm{NGRDI}$, and $t=1$ for Tiny Tim and 0 for Micro-Tom. With $\sigma(z)=(1+e^{-z})^{-1}$,

$$
\widehat Q=\sigma(2.1466193-1.0330324r+0.44660751q-0.9491477g-0.59390734qg+0.065658968t).
$$

The equation combines a bounded recovery coordinate with dissipative quenching and pigment/color modulation. The signs are conditional predictive coefficients in correlated readouts, **not isolated causal effects or rate constants**. NPQ, Rfd and QY_max can share source fluorescence measurements and calibration; their agreement is not independent physiological confirmation.

| Model | Development plant MAE | Reserved plant MAE |
|---|---:|---:|
| Constant yield |0.010544|0.011138|
| Cultivar/treatment design |0.006253|0.005051|
| Matched flexible imaging model |0.006065|0.005728|
| Selected pigment-quenching relation |0.004883|0.004833|

Errors are absolute dimensionless quantum-yield differences, averaged within plants and then equally across plants. The selected relation beats the registered controls numerically. The improvement over the strong treatment/cultivar baseline is small: paired difference **-0.000218**, exploratory plant-resampling 95% interval **[-0.001338, 0.001096]**, with 13/16 plant wins. Do not infer universal superiority from the mean alone.

## Investigation and limitations

Five adaptive attempts tested reciprocal quenching, fluorescence recovery, pigment coupling, morphology-mediated response and stress-specific quenching slopes. Recovery and pigment information improved development; adding size or stress-specific interaction did not. Selection and those stopping decisions were frozen before the held plants were scored.

This is a compact validated descriptor of the retained assay. The source already studies stress imaging biomarkers; no new photosynthetic law or demonstrated agricultural deployment benefit is claimed. The exact manuscript DOI was not available in the author repository at review time, limiting novelty assessment. Field lighting, cultivars, chambers and independent physiological assays remain untested. Morphology’s AREA_MM source scale is retained without inventing an area conversion or heat-balance interpretation.

The methodological value is a reproducible equation and evaluation task with plant-level validation, honest assay dependence and metadata exclusions. Additional independent hydration/gas-exchange measurements and new cultivars would be needed for a mechanistic extension.

## Reproduction

`python run.py` verifies hashes and replays every frozen model. `rules.json` includes all coefficients and training-only flexible transforms; `EQUATIONS.md` lists each family. The native adapter joins treatment by exact plantID, not workbook row order, and reconstructs targets and source anchors from the two original workbooks. `task_spec.json` freezes the same information budget for future agents. All confirmation outcomes are now exposed; they must not guide revisions advertised as untouched validation.

[Author dataset](https://zenodo.org/records/20638584) and [author processing repository](https://github.com/giorgiadelc/tom-phenotyping). Native data: CC BY4.0. Literature checked 2 October 2026; original manuscript citation remains incomplete.
