# Processed hippocampal trace and rejected endpoint

The archive contains157MATsessions from28animal suffixes, across days1–4,dorsal/ventralCA1,contexts and source groups1/3. Every suffix is linked across all files. Native processed.trace is a neuron-by-frame matrix, and all retained neuron rows enter population means. Native fitted spatial maps and population-vector summaries are not independent observations and are excluded from predictors.

The archive does not define exact trace normalization or establish spike/calcium-concentration units. We therefore retain author processed-trace units, signed values and frame indices. The source validTraceFrames examples include a duplicate finalframe, and fzframes appears start/duration without an authoritative retained indexing definition. We rejected behavioral-freezing and speed-aligned targets before fitting instead of manufacturing semantics. No claim of seconds,spikes or future fear behavior is made.

Author full-session denoising/normalization may use future observations, so causal-prefix validity pertains to the released trace, not raw fluorescence acquisition. Past population summaries are deterministic; whole animals remain independent validation groups, with shared source study limitations. Animal3DH2 was permanently assigned development before schema inspection.

Of157MATfiles,27Day4files provide only position/frame maps, without trace. SOURCE_EXCLUSIONS lists every such file;130trace sessions remain, covering all28animals. Twelve trace sessions have processed.exclude.SFPs flags with undocumented polarity. We retain these flags in source assets and do not silently decide1meanskeep/exclude. The target averages all released component rows; it is not a verified neuron-only or artifact-free population signal.
