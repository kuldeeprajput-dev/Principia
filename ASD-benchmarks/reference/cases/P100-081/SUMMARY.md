# P100-081 exploration summary

The source records soil health measurements at eight European agroforestry sites. The prediction endpoint is measured dry-soil bulk density; carbon stocks are excluded because their calculation contains that endpoint. The frozen complete-case contract requires organic carbon, interval depth and water pH. It retains 430 rows from six countries: four for development and Czechia/Germany for confirmation. UK and the Netherlands have no water-pH measurements in this workbook and are excluded transparently.

The development-selected two-phase volume relation fails to transfer reliably. Its reserved MAE is 0.336 g/cm³, compared with 0.173 for the simple mean-density control. This portfolio therefore contributes a falsification and a bounded evaluation task, not a positive pedotransfer law. No candidate was promoted after confirmation.

For carbon mass percentage C, define the conventional approximate organic fraction f=1.724 C/100. The candidate predicts ρ=[(1−f)/ρ_m+f/ρ_o]⁻¹, where the fitted component values are effective bulk densities, not measured intrinsic grain densities. Organic conversion and constant packing are modeling assumptions. Empty German and Czech country-metadata detail cells prevent stronger mechanistic attribution of the observed transfer failure; the native carbon units remain exactly the published column labels.

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


## Attempt history

**attempt-001 — two_phase_volume**: Attempt1: a two-phase organic/mineral volume mixture predicts decreasing bulk density through different effective component bulk densities. The1.724 conversion is an explicit approximate organic-matter convention, not a measured composition. Development MAE=0.259694; worst group=0.335395; fitted parameters=2.

**attempt-002 — structural_porosity**: Attempt2: two-phase mixing narrowly improves mean error over the flexible control but has worse worst-country error. Test a competing exponentially carbon-dependent pore-volume law with gradual depth consolidation rather than additive phase volumes. Development MAE=0.326218; worst group=0.434992; fitted parameters=3.

**attempt-003 — depth_compaction**: Attempt3: exponential structural porosity worsens held-country MAE to0.326. Reconcile that failure with the better mixture by allowing depth-dependent mineral packing, using a finite consolidation length rather than an unconstrained density-depth slope. Development MAE=0.312393; worst group=0.407062; fitted parameters=4.

**attempt-004 — organic_consolidation**: Attempt4: assigning depth consolidation to mineral packing did not help. Test the distinct mechanism that only the low-density organic phase consolidates with overburden; this predicts carbon-by-depth coupling and tends to constant mineral density as carbon vanishes. Development MAE=0.297844; worst group=0.356158; fitted parameters=3.

**attempt-005 — acidity_aggregation**: Attempt5: both depth-consolidation mechanisms worsen transfer. Test a chemical-aggregation alternative: pH modulates effective mineral packing through a positive exponential multiplier. pH is an observational proxy and a successful fit could not establish a causal acidity effect. Development MAE=0.326262; worst group=0.53854; fitted parameters=3.

All substantive attempts and failures are retained. See FREEZE.json and CONFIRMATION_RECEIPT.json for chronology and exact evidence binding.
