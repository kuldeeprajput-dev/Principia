# P100-025 exploration summary

The archive contains operando X-ray absorption spectra, reference compounds, electrochemical records and author analyses. This task retains the 194 original LiFePO4 spectra and two supplied endpoint references. Three consecutive spectra remain linked because the source also distributes three-spectrum averaged representations. Thirteen complete triplets were reserved by a fixed identifier hash.

The endpoint is the original dimensionless absorption ordinate, scored in the 7070–7200 eV edge window. Each spectrum supplies fixed pre-edge and post-edge calibration outside that window. Consequently, this is retrospective spectral compression rather than online state-of-charge prediction.

The selected six-coefficient response model yields reserved MAE 0.06130, against 0.13619 for a nominal-time two-phase mixture. Its predictors are the two reference shapes, nominal protocol progress, discharge/rest indicators and a linear energy term. The five more restrictive mechanistic candidates did not improve development accuracy.

This outcome supports a reproducible compression reference and a useful negative constraint: clock progress alone is not a validated phase-fraction measurement. The fitted mixture coefficient must not be interpreted as an absolute FePO4 fraction. One sequence cannot establish general battery transfer or a new electrochemical mechanism.

| Model | Development MAE | Reserved MAE | Reserved worst-group MAE |
|---|---:|---:|---:|
| equal_mixture | 0.136341 | 0.143238 | 0.161557 |
| flexible | 0.0612244 | 0.0613018 | 0.0777837 |
| lfp_reference | 0.176445 | 0.185151 | 0.203821 |
| protocol_two_phase | 0.141528 | 0.136187 | 0.177433 |
| continuous_edge_shift | 0.146753 | 0.141959 | 0.177433 |
| partial_transformation | 0.10592 | 0.112433 | 0.131155 |
| intermediate_spectral_component | 0.138931 | 0.132147 | 0.177433 |
| branch_hysteresis | 0.120676 | 0.119764 | 0.177433 |


## Attempt history

**attempt-001 — protocol_two_phase**: Attempt1: measuredendpoint spectra mix linearly in nominalcharge/dischargeprogress. This is a physicallyinterpretable two-phaseshape hypothesis, not an assertion that normalizedtimeisexactSOC. Development MAE=0.141528; worst group=0.178854; fitted parameters=0.

**attempt-002 — continuous_edge_shift**: Development evidence available before this fit: protocol_two_phase: MAE 0.141528, worst group 0.178854.

Nominal two-phase mixing is worse than a staticequalmixture. Test the competing solid-solution-like explanation of a continuouslyshifting LFPedge, using a second-order expansion of the measuredreference. A successfulshift remains an effective spectraldescription,not directphaseidentification. Development MAE=0.146753; worst group=0.178854; fitted parameters=1.

**attempt-003 — partial_transformation**: Development evidence available before this fit: protocol_two_phase: MAE 0.141528, worst group 0.178854; continuous_edge_shift: MAE 0.146753, worst group 0.178854.

Test incompleteaccessible transformation or time/SOCmismatch: a bounded affine phasefraction may explain why nominalprogress fails. The two measuredendpoint spectra remain the onlycomponents. Development MAE=0.10592; worst group=0.13708; fitted parameters=2.

**attempt-004 — intermediate_spectral_component**: Development evidence available before this fit: continuous_edge_shift: MAE 0.146753, worst group 0.178854; partial_transformation: MAE 0.10592, worst group 0.13708.

Test transient spectralbroadening/heterogeneity beyond a two-endpointmixture. The additionalcurvature component peaks at intermediateprogress and vanishes at endpoints; it cannot on its own identify a thirdchemicalspecies. Development MAE=0.138931; worst group=0.178854; fitted parameters=1.

**attempt-005 — branch_hysteresis**: Development evidence available before this fit: partial_transformation: MAE 0.10592, worst group 0.13708; intermediate_spectral_component: MAE 0.138931, worst group 0.178854.

Test charge/discharge asymmetry in progress-to-spectralfraction rather than a new spectralcomponent. Separate branch exponents capture nonuniform galvanostatic/CV timing or hysteresis, but must transfer across wholeacquisitionblocks. Development MAE=0.120676; worst group=0.178854; fitted parameters=2.

All substantive attempts and failures are retained. See FREEZE.json and CONFIRMATION_RECEIPT.json for chronology and exact evidence binding.
