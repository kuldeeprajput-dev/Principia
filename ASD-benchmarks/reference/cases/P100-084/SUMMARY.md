# P100-084 exploration summary

The source contains paired approach/retraction AFM curves from flat, low-roughness and high-roughness cellulose acetate surfaces. The task predicts later retraction force after the complete approach and the first five retraction measurements are available. Those measurements constitute explicit calibration, rather than hidden target information. Measured deflection at the predicted point is excluded because force is its calibrated multiple.

A spherical-contact shape plus localized attraction is the development-selected reference. It obtains 1.360 nN reserved curve-balanced MAE, compared with 2.212 nN for the repulsive spherical shape and 1.522 nN for the flexible polynomial. It also improves reserved RMSE and worst-curve error over the polynomial. A later diagnostic exponent model has lower confirmation MAE but does not replace the frozen reference.

The equation F̂=B+P max(x,0)³ᐟ²−A P exp(−|x|/ℓ) uses force baseline B and early-retraction amplitude P in nN. The coordinate x is dimensionless normalized piezo position relative to a fixed approach-force crossing; A and ℓ are dimensionless. The attraction term captures a localized force deficit around detachment. Because x is not true indentation, this equation is an effective calibrated surrogate and cannot certify Young’s modulus, adhesion energy or a new constitutive law.

There are 13 curve locations and three physical sample categories, with one whole curve per category reserved. Neither independent manufacturing transfer nor a biological cell-response claim is established.

| Model | Development MAE | Reserved MAE | Reserved worst-group MAE |
|---|---:|---:|---:|
| flexible | 1.66724 | 1.52241 | 1.81065 |
| hertz_shape | 2.11141 | 2.21229 | 2.9722 |
| initial_level | 38.1091 | 38.0093 | 38.7841 |
| conical_contact | 2.01419 | 2.12941 | 2.78362 |
| localized_adhesion | 1.56177 | 1.35975 | 1.72774 |
| shifted_contact_pull_off | 1.81803 | 1.39355 | 1.88172 |
| rough_asperity_exponent | 1.64024 | 1.28194 | 1.54597 |
| hysteretic_detachment | 1.72594 | 1.3856 | 2.21132 |


## Attempt history

**attempt-001 — conical_contact**: Attempt1: a conical/Sneddon-inspired response competes with sphericalHertz scaling; effective tip/rough-asperity geometry could alter the force exponent. Development MAE=2.01419; worst group=4.97149; fitted parameters=0.

**attempt-002 — localized_adhesion**: Development evidence available before this fit: conical_contact: MAE 2.01419, worst group 4.97149.

The conical shape is only slightly better than Hertz and loses to flexible interpolation. Test a localized attractive-force well around contact loss, with no inferred modulus: adhesion may explain the missing negative retraction force. Development MAE=1.56177; worst group=6.11862; fitted parameters=2.

**attempt-003 — shifted_contact_pull_off**: Development evidence available before this fit: conical_contact: MAE 2.01419, worst group 4.97149; localized_adhesion: MAE 1.56177, worst group 6.11862.

Separate effective contact registration from the pull-off well. A shifted spherical contact and localized detachment response compete with a symmetric contact-centered attraction; neither uses target deflection. Development MAE=1.81803; worst group=6.39742; fitted parameters=4.

**attempt-004 — rough_asperity_exponent**: Development evidence available before this fit: localized_adhesion: MAE 1.56177, worst group 6.11862; shifted_contact_pull_off: MAE 1.81803, worst group 6.39742.

Test whether rough-asperity geometry changes the repulsive exponent after adhesion is included. A stable non-Hertz exponent would be an effective response descriptor, not a universal tip-contact law. Development MAE=1.64024; worst group=6.5072; fitted parameters=3.

**attempt-005 — hysteretic_detachment**: Development evidence available before this fit: shifted_contact_pull_off: MAE 1.81803, worst group 6.39742; rough_asperity_exponent: MAE 1.64024, worst group 6.5072.

Test persistent adhesive contact followed by a finite detachment threshold. This asymmetric hysteresis mechanism contrasts with a symmetric attractive well; the smooth switch approximates heterogeneous pull-off rather than claiming an exactDMTlaw. Development MAE=1.72594; worst group=5.48338; fitted parameters=3.

All substantive attempts and failures are retained. See FREEZE.json and CONFIRMATION_RECEIPT.json for chronology and exact evidence binding.
