# Download and verify Principia-100 v0.2.0

[Overview](README.md) · [Catalog](CATALOG.md) · [Evaluation guide](reference/docs/EXTERNAL_AGENT_GUIDE.md)

Install Git and [Git LFS](https://git-lfs.com/) first. The immutable release tag is `asd-benchmark-v0.2.0`; record its resolved commit with every study. Use `main` only when deliberately following updates. The application is not needed to use this benchmark.

## Reference results and evaluators only

Use this route to read all 100 PDFs or score prediction files against the existing measured targets. It downloads approximately 1 GB of reference material without the 4.8 GB source corpus.

```bash
git lfs install
GIT_LFS_SKIP_SMUDGE=1 git clone --depth 1 --filter=blob:none --sparse \
  --branch asd-benchmark-v0.2.0 https://github.com/pzqpzq/Principia.git
cd Principia
git sparse-checkout set ASD-benchmarks/reference ASD-benchmarks/tools ASD-benchmarks/schemas ASD-benchmarks/assets
cd ASD-benchmarks/reference
```

Skip-smudge applies only to the initial clone. Once it is unset, sparse checkout retrieves the selected LFS payloads. Root benchmark documentation and manifests are included automatically by cone-mode sparse checkout. Do not use the ordinary GitHub source ZIP as a substitute: it may contain pointer files.

Create a Python 3.12 environment **outside** the release, then install:

```bash
python -m pip install -r evaluation/requirements.lock.txt
python evaluation/benchmark.py verify
```

Use `python3` if that is your Python command. The lock records the validated numerical and native-reader environment. Other environments receive a runtime fingerprint and need their own parity check. Native formats may also need the libraries listed in the source-reader reports. No model API or paid discovery run is required for scoring.

## Add source data for one scenario

From the repository root, add the exact source folder named in the catalog. For the router example:

```bash
git sparse-checkout add ASD-benchmarks/scenarios/37_networks_router_power
cd ASD-benchmarks
python3 tools/replay.py --root . --mode verify --case P100-037
cd reference
python evaluation/benchmark.py prepare --task P100-037.original.v1 --data-root ../scenarios --output /tmp/p100-native
```

Read the case's neutral brief and approved source assets. Use the task's information budget when evaluating a registered endpoint. Source archives can contain labels, source analyses and publisher code; presence in the archive does not make every field an admissible predictor.

To use source data alone, select `ASD-benchmarks/tools`, `ASD-benchmarks/schemas` and the desired `ASD-benchmarks/scenarios/<folder>` instead of the reference directory. Source integrity tools require Python 3.9+; the evaluator uses Python 3.12.

## Complete benchmark

Starting from a new clone as above, run:

```bash
git sparse-checkout set ASD-benchmarks
cd ASD-benchmarks
python3 tools/validate_release.py .
python3 tools/replay.py --root . --mode verify
python3 tools/test_publication.py
cd reference
python evaluation/benchmark.py verify
python evaluation/benchmark.py assess --case P100-008 --data-root ../scenarios --output /tmp/p100-adequacy
```

The full working files occupy approximately **5.8 GB**. Reserve at least **16 GB** for the checkout and Git/LFS caches before source-archive extraction or derived outputs. Expanded native payloads add up to about 7.31 GB across the corpus; peak analysis memory and outputs are additional. Keep original archives intact and extract temporary copies only when needed.

Every raw scenario remains below 500 MB stored and expanded. That per-case acquisition limit does not apply to the combined reference/evaluation history. Exact current stored and LFS sizes are in [RELEASE_MANIFEST.json](RELEASE_MANIFEST.json).

## Native reconstruction of the entire reference

After downloading all sources and installing the native-reader environment, run from `ASD-benchmarks/reference/evaluation`:

```bash
python -m preparation.verify_reconstruction --benchmark .. --data-root ../../scenarios \
  --supplemental-58 ../supplements/P100-058 --report /tmp/p100-native-reconstruction.json
```

The four optional PLA tasks declare the supplied supplemental archives. The unresolved case-96 supplement is not required or distributed. Native reconstruction performs no fitting and compares identifiers/groups exactly and numeric values at declared floating-point tolerances.

## Windows PowerShell

Set skip-smudge for the initial clone, then remove it before selecting files:

```powershell
git lfs install
$env:GIT_LFS_SKIP_SMUDGE = '1'
git clone --depth 1 --filter=blob:none --sparse --branch asd-benchmark-v0.2.0 https://github.com/pzqpzq/Principia.git
Remove-Item Env:GIT_LFS_SKIP_SMUDGE
cd Principia
git sparse-checkout set ASD-benchmarks
```

Use a Windows virtual environment and paths in place of the POSIX `/tmp` examples. Preserve filenames and bytes; `.gitattributes` disables automatic newline conversion. Install dependencies using the selected Python 3.12 interpreter.

## Integrity and recovery

`tools/validate_release.py .` validates the **complete** integrated release. It rejects missing, changed or unallowlisted files; use an external directory for experiments. A selective checkout is intentionally incomplete and should use per-case source verification or reference-only evaluation instead.

A file beginning `version https://git-lfs.github.com/spec/v1` is a pointer, not data. Confirm Git LFS is installed and `GIT_LFS_SKIP_SMUDGE` is unset. GitHub hosting quotas can affect availability. The [acquisition manifest](ACQUISITION_MANIFEST.json) records original publisher locations; recovery must match the frozen hash, never silently substitute a newer dataset.

For an intentionally pointer-only checkout:

```bash
python3 tools/verify_git_release.py . --allow-lfs-pointers
```

That validates pointer identities and sizes; it does not verify remotely stored payload bytes. Publication auditing separately checks real files and public downloads. Historical acquisition and local acceptance receipts are retained as history; [RELEASE_AUDIT.md](RELEASE_AUDIT.md) describes the current integrated release.
