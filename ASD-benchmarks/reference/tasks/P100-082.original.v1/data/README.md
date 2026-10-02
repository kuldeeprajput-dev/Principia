# Prepared-input contract

Required keys are unique `sample_id` and string `group`, one complete future temporal block per site. `site` preserves the native label. `context` concatenates site, native subsite and trenching status, preserving the exact spelling used in training. Inputs are `t05` (5 cm soil temperature, Celsius), `tsmoisture` (native volumetric water content percent, possibly missing) and `doy` (day of year). Day and site/context are known before the chamber response is measured.

The task requires finite t05 in [-15,50], moisture missing or in [0,100], and finite native flux. Author-supplied response outlier filtering is not applied: negative and large finite flux values remain. Slope, intercept, slope confidence interval and chamber conversion quantities are excluded because they can encode the measured response.

`observations.csv.gz` separately stores native flux in **g CO2 m^-2 h^-1**, exact source CSV row, date, point, treatment and trenching anchors. Values are source-derived chamber fits, not raw gas traces. Prepared rows are selections of native values; no unverified percent/fraction conversion or new concentration fitting is performed. Missingness and all fixed training transformations are visible in serialized model states.

Latest 20% native dates per site were reserved by metadata, keeping whole dates together. Three sites have no native t05 anywhere, and Dobroc has none on the reserved dates. There are 6,928 eligible final observations in 15 whole-site blocks, versus 31,461 development observations at 16 sites. Eligibility and every source date allocation are preserved in the audit. Context calibration uses earlier data only; unseen training contexts use disclosed site/global fallbacks. This does not establish new-site transfer.
