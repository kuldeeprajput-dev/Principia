# Prepared-input contract

`inputs.csv.gz` has one row per complete reserved flask/horizon. Required keys are unique `sample_id` and string `group` (the complete trial/run). `trial` is the exact protocol ID `1`, `2` or `3`; `algae` preserves the native label. `hour` is 12, 24, 36 or 48 h. `g4` and `g8` are the same flask's native, blank-corrected, author-converted volumes in mL at 4 h and 8 h. G8 must be positive. These inputs are available at the prediction time, 8 h. No response from a later time is used.

`observations.csv.gz` separately contains `target` (native future GasVolume in mL), the exact native filename and source CSV row, prefix source rows, flask and run anchors. Nothing is fitted from this table. Identical early prefixes repeated across four horizons do not constitute independent vessels. All horizons and representations of a flask remain in one partition.

GasDM and end-of-incubation dry-matter degradation are not prediction inputs. The native pressure-to-volume conversion and blank correction are source preprocessing; our preparation merely selects exact observed hours and adds IDs. No interpolation, imputation, resampling or scientific normalization of source values is performed. Native file SHA-256 values and partition allocation are preserved in the research audit.

The task has 216 final rows, 54 flasks and three complete runs. These are exposed reference observations. Custom data must meet the same units and known-protocol scope; forecasts outside measured horizons or new biological systems have no validation claim.
