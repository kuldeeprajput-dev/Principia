# FACS calibration and semantic limits

18FCS files comprise uninduced/Dox triplicates of MFSD5,WT SLC30A8,andD110N_D224N mutant. The sample list is authoritative for condition identity. Three matched technical blocks AD/BE/CF conservatively link each cell line and its paired control. Wells, not individual cells or quantiles, are replication; all18wells derive from one plate.

FCS has B/E AF488-A and PE-TexasRed channels, unit gain and an identity2channel compensation matrix marked applied. The paper methods specify biotinVVL plus Alexa488, matching the AF488 header, but figure captions say Alexa647. This unresolved author inconsistency is preserved: the numerical task is explicitly the native AF488 channel, not an invented dye conversion. Native fluorescence is in arbitrary detector units, not glycan molecules.

Original FlowJo/manual gates are not retained. Our finite-event, positive-FSC/SSC inclusion is explicit and does not claim to reproduce author gated geometric means or eliminate all debris/doublets. Quantiles are deterministic linear sample quantiles. Induced targets use only their paired uninduced calibration as an input.
