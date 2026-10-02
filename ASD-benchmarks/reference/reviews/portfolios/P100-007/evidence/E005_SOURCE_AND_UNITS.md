# Force and clock audit

The source contains only participant S1 at0.5,0.75 and1m/s. All six timestamp columns have exactly one unique value, zero. Time is reconstructed exclusively from the source-declared1000Hz force-platform sampling rate and native frame order; no external-clock alignment is claimed. The source paper describes vertical force in newtons (and later normalizedN/kg analyses); the CSV itself omits unit labels. Both plates are retained as named1/2; an inconsistent text statement about left-only data is not used to invent side identity.

EEG and EMG are not used because their synchronization requires additional assumptions. Author EMG files are MAV-processed. Our causal10ms means and5s past-only period estimation are transparent derived features; raw sources remain unchanged. The target is one force channel, not a clinical diagnosis, gait quality or independent biomechanical population outcome.
