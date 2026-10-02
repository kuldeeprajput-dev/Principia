# Attempt002: finite operating-point transfer

Attempt001 fails to improve affine achieved-throughput MAE (2.499vs2.488ms), with nonmonotonic rate residuals (mean bias +2.31,-1.43,-4.06,-0.36,+2.44,-0.45ms across the six settings). Competing explanation: repeatable operating-point response is more useful than a global queue law. Fit six training-location medians indexed only by offered rate; leave entire locations out. This is a finite-setting calibration rule, not interpolation or a physical law.
