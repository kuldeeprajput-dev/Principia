# Soil bulk density from organic carbon and sampled depth

The source records soil health measurements at eight European agroforestry sites. The prediction endpoint is measured dry-soil bulk density; carbon stocks are excluded because their calculation contains that endpoint. The frozen complete-case contract requires organic carbon, interval depth and water pH. It retains 430 rows from six countries: four for development and Czechia/Germany for confirmation. UK and the Netherlands have no water-pH measurements in this workbook and are excluded transparently.

The development-selected two-phase volume relation fails to transfer reliably. Its reserved MAE is 0.336 g/cm³, compared with 0.173 for the simple mean-density control. This portfolio therefore contributes a falsification and a bounded evaluation task, not a positive pedotransfer law. No candidate was promoted after confirmation.

For carbon mass percentage $C$, the conventional approximate organic fraction is $f=1.724C/100$. The volume-mixture equation below uses effective component bulk densities, not measured intrinsic grain densities. Organic conversion and constant packing are modeling assumptions. Empty German and Czech country-metadata cells prevent stronger attribution of the transfer failure; native carbon units remain exactly the published column labels.

## Experimental scope and evaluation

Same soil-sampling occasion; Corg, sampling depth and pH are measured covariates available before BD inference. This is a laboratory-measurement substitution task, not a future forecast.

Calibration: No held-out country BD calibration; country identifiers are grouping metadata, never predictors.

Validation unit: Entire country/site portfolio, with all transects, fields and depths linked. Eight countries are convenience samples, not a random population sample.

Country-balanced errors and explicit individual-country results; two confirmation countries are insufficient for precise population confidence.

Target: measured soil bulk density (g/cm³). Errors use g/cm³. The selected reference is **two_phase_volume**. Selection was frozen before confirmation; diagnostic winners are not substituted afterward.

| Predictor | Unit |
|---|---|
| C | mass % organic carbon |
| depth | cm midpoint of sampled interval |
| pH | pH unit in water |


## Matched comparison

| Model | Development MAE | Reserved MAE | Reserved worst-group MAE |
|---|---:|---:|---:|
| constant | 0.369453 | 0.172601 | 0.21367 |
| flexible | 0.26609 | 0.314545 | 0.556889 |
| linear | 0.319091 | 0.312858 | 0.573624 |
| two_phase_volume | 0.259694 | 0.336125 | 0.608326 |
| structural_porosity | 0.326218 | 0.337788 | 0.615075 |
| depth_compaction | 0.312393 | 0.323582 | 0.578477 |
| organic_consolidation | 0.297844 | 0.326608 | 0.594189 |
| acidity_aggregation | 0.326262 | 0.359424 | 0.621493 |


The primary error is mean group MAE. RMSE and signed bias are complementary; rows within a group do not establish independent replication. No accuracy percentage or industrial tolerance is invented.


## Selected equation and coefficients

$$
\widehat\rho=\left[\frac{1-f}{\rho_m}+\frac{f}{\rho_o}\right]^{-1},\qquad f=1.724C/100
$$

C is the source carbon percentage used by the declared surrogate, with the conventional 1.724 conversion. The source ambiguity and failed country transfer preclude interpreting this as a validated density law. Density parameters use g/cm^3.

| Coefficient | Frozen value |
|---|---:|
| mineral | 1.59923279 |
| organic | 0.142370917 |

All comparator expressions, numerical guards and full-precision values remain in EQUATIONS.md, rules.json and run.py.

## Applicability and limitations

- Texture is unavailable in six countries and excluded rather than imputed. C stocks are excluded because they use bulk density algebraically.
- Observational associations do not identify an agroforestry treatment effect. Protocol adaptations and country effects may limit transfer.

Two Finland rows were seen during schema inspection, so Finland is development-only. Reserved countries were allocated by metadata-only hash before target inspection. All outputs are exposed after this campaign.

## Reproduction

Run `python run.py` in this final package to verify hashes and reproduce every saved prediction. Use `python run.py --inputs new.csv --output predictions.csv --model reference` only with the declared inputs and units. Numerical prediction evaluation does not certify novelty or mechanism. Source anchors and reserved observations are separate from predictor inputs.

Source: https://zenodo.org/records/21204617. See source/units audit and prior-art records in research history.
