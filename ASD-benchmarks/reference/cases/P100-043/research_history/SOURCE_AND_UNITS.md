# Source and semantics audit

The retained experiment contains 22 constant-learning-rate pretraining architecture trajectories. The other 20 merged records are cooldown histories and are excluded from this endpoint, not independent samples. Source summary chunks are linked by architecture and run_name and are never separate validation groups. The author extraction excludes failed starts and diverged runs; therefore this task cannot establish stability or failure probabilities for all training launches.

We use measured validation log-perplexity, not the author fitted scaling laws or compute proxies. The source uses a fixed held-out 100-million-token validation sample from the training distribution. Its natural-log loss is reported in nats/token. Optimizer steps multiply by 2048 sequences and 2048 tokens. Width/depth and parameter count are architecture metadata. Author total-token sums across chunks are not used as chronological coordinates.

Prediction occurs after the last available measurement at or before 20 billion tokens. Two early anchor losses, at or before 10 and 20 billion tokens, are explicit permitted calibration; their exact times are included. No future validation response, measured execution speed or source-fitted output becomes an input. Known validation loss on an early checkpoint is not an unseen-model forecast. All stages for an architecture are linked, and the five confirmation architectures were selected only from parameter-count strata and identifiers.

The JSON schema and key inventories were inspected without printing response values. The task is source-aware, and any confirmation is internal to this author-filtered suite. It does not establish transfer to new data, seeds, tokenizers or hardware, nor realized compute savings.
