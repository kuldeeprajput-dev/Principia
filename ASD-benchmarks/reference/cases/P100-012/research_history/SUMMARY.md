# P100-012 exploration summary

The NIST source contains 56 measured X-ray reflectivity spectra from twelve hafnia-coated silicon wafers, produced in four deposition batches. The target is native intensity in counts at higher angles; a fixed five-point band near 2θ=1° supplies an explicitly allowed calibration for each spectrum. Whole deposition batches define validation, so positions from a wafer never cross partitions.

The selected finite-film interference surrogate reaches 6,200 counts wafer-balanced MAE on the fourth deposition batch, versus 11,368 for a smooth flexible envelope and 53,216 for the asymptotic Fresnel tail. Its fitted effective period is consistent with an approximately 8.64 nm optical thickness scale. This reproduces established thin-film interference and supports a useful calibrated transfer model; it does not establish a new optical law or certified absolute thickness.

Define q=4π sinθ/λ, λ=1.540593 Å and F(q)=[(q−√(q²−q_c²))/(q+√(q²−q_c²))]². The selected expression is Î(q)=I₀ F(q)/F(q₀) exp[−σ²(q²−q₀²)] [1+r cos(qd+φ)]/[1+r cos(q₀d+φ)]. Here q,q₀,q_c are Å⁻¹; σ,d are Å; r is dimensionless; φ is radians. The implementation guards the square root outside its admitted range. Every coefficient is listed below.

Further fringe decoherence, position-dependent thickness and additive background were tested and preserved. None improved the primary development criterion; several trade small secondary-error differences. One reserved batch is too little for population claims, and correlated parameters prevent a unique structural interpretation.

| Model | Development MAE | Reserved MAE | Reserved worst-group MAE |
|---|---:|---:|---:|
| flat_calibration | 1.92561e+06 | 1.94494e+06 | 2.16329e+06 |
| flexible | 10890.6 | 11368.2 | 14725.5 |
| fresnel_tail | 53063.8 | 53215.6 | 61941.9 |
| roughness_envelope | 14609.1 | 14928.4 | 15641.2 |
| finite_angle_fresnel | 10932 | 11243.9 | 11337.8 |
| kiessig_interference | 5988.58 | 6199.69 | 11319.3 |
| contrast_decoherence | 6031.67 | 6257.75 | 11123.3 |
| center_outer_thickness | 6166.24 | 6266.36 | 11109.5 |
| instrument_background | 6467.69 | 6693.92 | 11599.2 |


## Attempt history

**attempt-001 — roughness_envelope**: Attempt1: a Debye-Waller-like roughness envelope attenuates the asymptotic Fresnel tail. Test transfer of one effective interface width across complete deposition batches. Development MAE=14609.1; worst group=15823.1; fitted parameters=1.

**attempt-002 — finite_angle_fresnel**: Development evidence available before this fit: roughness_envelope: MAE 14609.1, worst group 15823.1.

Roughness improves the asymptotic tail but remains worse than the smooth control. Test finite-angle Fresnel refraction: calibration near the critical region may invalidate q^-4 normalization even at larger target angles. Development MAE=10932; worst group=11506.2; fitted parameters=2.

**attempt-003 — kiessig_interference**: Development evidence available before this fit: roughness_envelope: MAE 14609.1, worst group 15823.1; finite_angle_fresnel: MAE 10932, worst group 11506.2.

Test coherent finite-film Kiessig interference in addition to refraction/roughness. A transferable period should support a shared effective film scale, while phase/contrast remain potentially confounded. Development MAE=5988.58; worst group=11368.1; fitted parameters=5.

**attempt-004 — contrast_decoherence**: Development evidence available before this fit: finite_angle_fresnel: MAE 10932, worst group 11506.2; kiessig_interference: MAE 5988.58, worst group 11368.1.

Challenge the constant fringe-contrast assumption: differential interface roughness or thickness dispersion may wash out interference at high q. Test decaying contrast separately from the mean intensity envelope. Development MAE=6031.67; worst group=11179; fitted parameters=6.

**attempt-005 — center_outer_thickness**: Development evidence available before this fit: kiessig_interference: MAE 5988.58, worst group 11368.1; contrast_decoherence: MAE 6031.67, worst group 11179.

Test spatial growth nonuniformity: the effective fringe period may differ between center and noncenter sites while remaining common across deposition batches. All positions of each wafer remain linked. Development MAE=6166.24; worst group=11275.6; fitted parameters=6.

**attempt-006 — instrument_background**: Development evidence available before this fit: contrast_decoherence: MAE 6031.67, worst group 11179; center_outer_thickness: MAE 6166.24, worst group 11275.6.

Neither contrast decoherence nor center/outer period variation improves primary transfer. Test an instrument-count floor as the remaining alternative to extra film physics. A positive background could explain high-angle residuals while preserving the coherent film term. Development MAE=6467.69; worst group=11587.1; fitted parameters=6.

All substantive attempts and failures are retained. See FREEZE.json and CONFIRMATION_RECEIPT.json for chronology and exact evidence binding.
