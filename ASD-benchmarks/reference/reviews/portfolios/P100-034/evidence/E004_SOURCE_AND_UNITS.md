# Native source and units audit

One muscle6 cell per animal, control and mutant. Dose sequence is confounded with time; sweeps are technical repetitions. Author peak measurements, not newly extracted raw-ABF amplitudes.

Endpoint: first_pulse_ePSC_magnitude (nA).

Calibration: First-pulse mean across ten sweeps at0.4 and0.75mM per animal. Later1.5/3/6mM targets are excluded from calibration.

Timing: After two lower-dose blocks, forecast mean first-pulse current at the three later calcium doses; all animal data linked.

Source: https://zenodo.org/records/15629377
Primary study: https://doi.org/10.1073/pnas.2514151122

Native bytes remain unchanged; deterministic adapters emit explicit source and calibration anchors. Publisher-calculated measurements remain labeled author-processed. No global normalization, model fitting or future-outcome features occur in preparation.


One mutant block labeled cell x has an explicitly missing6mM file and no ten-sweep values. Retain its observed1.5/3mM targets; omit unavailable6mM without imputing. Some workbook file labels have inconsistent dates; workbook anchors are authoritative for these author-extracted peaks.


Native Prism graph metadata explicitly identifies nA. Development ABF current channel reports pA; workbook peaks use nA. Baseline values unchanged; unit label corrected before any candidate attempt, without confirmation inspection.
