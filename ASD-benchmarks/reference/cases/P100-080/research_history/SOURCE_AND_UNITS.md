# Wearable physiology source audit

The coherent AEROBIC subset has30people; S11_a/b are separated recordings of the same person and cannot cross partitions. Source EDA is4Hz in microSiemens, temperature4Hz Celsius, accelerometry32Hz at1/64g per native unit. Each file declares its own start and rate; the adapter aligns causal windows by these headers without assuming equal lengths or bridging disconnects. The source clock strings can be2013; these are device-clock coordinates, not an assertion of measurement year.

The target is a future measured EDA level, not an author HR estimate or the experimental stress/exercise label. No BVP-derived HR is used. Manufacturer calibration/preprocessing is retained; signed finite values remain eligible. Source S03/S07 changed pedaling cadence early, S11 disconnected, and S12 is absent; these issues limit fixed-protocol interpretation. Exercise is only one part of the archive, declared before fitting.
