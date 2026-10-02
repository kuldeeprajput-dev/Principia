# attempt-002

Attempt001 fails to improve affine achieved-throughput MAE (2.499vs2.488ms), with nonmonotonic rate residuals (mean bias +2.31,-1.43,-4.06,-0.36,+2.44,-0.45ms across the six settings). Competing explanation: repeatable operating-point response is more useful than a global queue law. Fit six training-location medians indexed only by offered rate; leave entire locations out. This is a finite-setting calibration rule, not interpolation or a physical law.

Development leave-location-out MAE: 1.5841014814814813ms; worst group: 1.9434333333333327ms. Full fold states and per-row predictions are retained. State: `model.json`. Not selected; retained as a scientific counterexample or comparator.

Interpretation: these are empirical conditional latency rules. Throughput deficit is not a measured loss quantity. Operating-point response is not a universal monotonic queue law. No new network capacity or component-specific causal mechanism is identified.
