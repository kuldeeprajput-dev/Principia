# Source and units audit — P100-047

Source: https://argo.ucsd.edu/data/how-to-use-argo-files/. Redistribution: Argo open data with attribution. Native bytes are hash-checked and never modified.

Target: Adjusted dissolved oxygen at observed nitrate/water-mass state (umol/kg). Inputs: pressure [dbar]; temperature [degC]; salinity [psu]; nitrate [umol/kg]; float_id [identifier].

Contemporaneous adjusted oxygen diagnostic using independently instrumented nitrate and CTD measurements from the same aligned synthetic profile. No prospective acquisition claim. Adjusted T/S flags1,2,8 permit source interpolation; oxygen/nitrate/pressure flags1,2 only.

Whole float profiles; rolling half-year tests 2023H2,2024H1,H2,2025H1, earlier times train. July2025 onward reserved. Two serially sampled floats, not hundreds of independent oceans.

Author-adjusted, aligned/calibrated products. In-situ-temperature surface oxygen-solubility proxy used for comparison; no potential-temperature or pressure-corrected AOU claim. No causal Redfield stoichiometry from correlated water masses.

Exposure: Inspected dimensions, parameter names/QC inventories and dates only, no numerical oxygen values.

Every output retains exact native row or NetCDF profile/level anchors. Missing/invalid measurements are excluded explicitly; none are imputed. Quality-screening defines the task, not claimed population coverage. No scientific source values are rewritten.
