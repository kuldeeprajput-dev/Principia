# Source and units

USGS analog laser at33m station during April2024 gate-release experiments. CSVTime is seconds on a1ms grid; everyresponse column is meters, with small signed baseline noise retained. Fixed past-window means/medians are declared predictor construction only; target values remain native.

The source paper validates a swath instrument against independent lasers. This task does not reproduce a hidden alignment: it forecasts one measured analog channel using only its causal history. The source script uses peak-centered plotting windows; no such operation enters this adapter.
