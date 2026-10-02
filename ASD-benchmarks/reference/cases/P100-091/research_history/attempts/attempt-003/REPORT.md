# attempt-003

The six-setting median transfer improves development error to1.584ms and worst-location error1.943ms, slightly simpler/better than nested RBF1.611ms. Reconcile this success with failed global deficit model: permit a shared within-setting congestion slope in addition to six offered-rate offsets. If rate offsets were masking useful instantaneous traffic degradation, the added slope should improve group errors consistently. Inspect fold coefficient signs/identifiability and compare against removing the deficit term.

Development leave-location-out MAE: 1.5093866148148145ms; worst group: 1.9212999999999998ms. Full fold states and per-row predictions are retained. State: `model.json`. Selected solely from development evidence.

Interpretation: these are empirical conditional latency rules. Throughput deficit is not a measured loss quantity. Operating-point response is not a universal monotonic queue law. No new network capacity or component-specific causal mechanism is identified.
