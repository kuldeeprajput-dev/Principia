# P100-004 source and units audit

How much of observed MET magnitude is explained by recoil geometry versus scalar activity?

**target:** Measured missing transverse momentum magnitude

**target units:** GeV

**timing contract:** Diagnostic event reconstruction from lepton and jet kinematics; met_phi/met_mpx/met_mpy and truth fields forbidden. Inputs are measured same-event objects, not a pre-collision forecast.

**calibration:** Training events only; no held-period target calibration.

**independent unit:** Run period, with unique runNumber+eventNumber observations

**scope limits:** 2015 four-lepton educational skim, no MC or control background supplied. Object recoil and MET share reconstruction components; predictive agreement is not independent discovery of momentum conservation or new physics.

**exposure:** Source-aware public data. Limited schema/header and first-row previews recorded before task freeze; any inspected examples remain explicitly exposed. Confirmation performance withheld until selection and stopping freeze.

Source data stay byte-identical. Exact consumed rows/members and transformations are in native.py. All outputs record native source anchors.
