# Source and units audit — P100-048

Source: https://gml.noaa.gov/grad/surfrad/overview.html. Redistribution: US government public domain. Native bytes are hash-checked and never modified.

Target: Daylight downwelling longwave irradiance (W/m2). Inputs: temperature [degC]; humidity [percent]; solar [W/m2]; diffuse [W/m2]; zenith [degree]; site_dra [indicator].

Contemporaneous daytime downwelling longwave from independently measured temperature/RH and solar/diffuse channels. Zenith<75deg, globalSW>20W/m2, required QC=0. Cloud proxy is clipped diffuse/global ratio; not net-radiation closure.

Whole site-day blocks; forward folds Jan21–31,July8–15,July16–24 trained on preceding dates. July25–31 both sites reserved. Two sites only and correlated days.

Only daytime empirical clear/all-sky emissivity diagnostics; no nighttime extension, no independent cloud observations, no cloud causality.

Exposure: First row of dra26190.dat (July9) inspected; this belongs to development. No reserved July25–31 target values printed.

Every output retains exact native row or NetCDF profile/level anchors. Missing/invalid measurements are excluded explicitly; none are imputed. Quality-screening defines the task, not claimed population coverage. No scientific source values are rewritten.
