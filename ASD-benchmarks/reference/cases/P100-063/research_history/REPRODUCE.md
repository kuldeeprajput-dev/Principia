# Reproducibility

The frozen final equations run with `python package/run.py`.

To refit the complete development campaign from hash-verified native corpus files, without editing this frozen history:

```bash
python replay_development.py --data-root /path/to/local-datas --output-root /new/disposable/directory
```

The replay reconstructs development rows from native assets, applies the recorded grouped folds, refits every baseline and attempt in recorded order, and checks primary metrics against the originals. It does not evaluate confirmation or modify source files. An existing output directory is rejected. Confirmation cannot be made fresh again: `confirm.py` intentionally refuses a second opening in this history.

Dependencies are listed in `dependencies.txt`. Standard figure generation and reader documents are not part of model inference.
