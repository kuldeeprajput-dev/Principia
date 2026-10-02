# Source and units audit: P100-026

Catalytic induction trajectory transfer. Native bytes are hash-verified by native.py. Primary publication: https://pubs.rsc.org/en/content/articlepdf/2025/cy/d5cy00544b.

Endpoint: Dimethoxymethane selectivity, percentage points. Inputs: elapsed_min (min), anchor_selectivity_pct (percent), prefix_slope_pct_min (percent/min), ag_wt_pct (wt percent).

Complete reactor run. Diagnostic forecast after 300 min with fixed prefix calibration; no future conversion/selectivity predictors.

Last available DMM selectivity at t<=300min plus least-squares prefix slope on120<=t<=300; both recomputed independently per run. Score300<t<=1500.

Public source-aware corpus; source plots and published analyses known. Schema previews exposed first rows only. Case30 speeds>=13.9mm/s previewed; scored0.28–10mm/s unviewed. Case22 initial~0.006V row previewed; targetV>=0.05V unviewed. Case65 10Hz first rows previewed; scoref>=100Hz. Reserved response distributions and scores unopened.

## Native semantics, prior processing and limitations

The eight selected native reactor tables carry time in min, methanol conversion percent, activity and DME/MF/DMM selectivitypercent. DMM is scored directly, never reconstructed from selectivity closure or supplied formula columns. Figure1_longterm andFigureS14b have the same released run; onlyFigureS14b enters and the duplicate cannot cross splits. Each entire file is a group; restart segments, if present, stay linked. Calibration uses the last t<=300min selectivity and an explicitly fixed120–300min slope; it is performed separately for each run. Prediction covers300<t<=1500min. Time-temperature/pretreatment labels do not establish independent replicate reactors; temperature is omitted as predictor because other runs' naming/metadata are insufficient to assign all temperatures without ambiguity. Loading1,5,20wtpercent is explicit in filenames. Source work already interprets induction via evolving silver oxidation and coupled acid/metal chemistry, reports temperature/loading optimization and reversibility. Our prefix-conditioned response cannot directly identify Ag oxidation state or prove an industrial optimum. Measurements include2023 instrument characterization; complete reactor dates are unknown.
