# P100-045 source and units audit

Does a common count-space hardness response transfer across detector orientations and burst phases?

**target:** GBM NaI channel4 count rate during fixed post-trigger window

**target units:** counts/s

**timing contract:** Same-bin channel2+3 count rates and previous-bin low-energy rate permitted; targetchannel4 observations aftertrigger forbidden as predictors.

**calibration:** Pretrigger[-200,-100]s background rate in each low/high channel; instrument-specific energy edges recorded.

**independent unit:** Detector within one GRB; detectors share one incident event

**scope limits:** SingleGRB250206827, observed detector counts not deconvolved photon flux. NaI channel4 spans slightly different energy ranges by detector. No universal burst hardness law or independent event replication.

**exposure:** Source-aware public data. Limited schema/header and first-row previews recorded before task freeze; any inspected examples remain explicitly exposed. Confirmation performance withheld until selection and stopping freeze.

Source data stay byte-identical. Exact consumed rows/members and transformations are in native.py. All outputs record native source anchors.
