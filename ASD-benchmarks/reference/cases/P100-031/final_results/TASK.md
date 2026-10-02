# P100-031.original.v1

**Target.** Author-benchmarked mean compilation wall time after matched Qiskit pilot

**Target units.** seconds

**Metric kind.** log_mae

**Timing contract.** Must execute the complete Qiskit pilot first; its runtime and resulting circuit statistics are known only afterward. Candidate SDK timing is withheld. Pilot cost is not free. This is runtime diagnostics, not pre-compilation prediction or quantum-device performance.

**Calibration.** Whole circuit families held across allSDKs; exact same inputfilename matched. No held family candidate-runtime measurements enter fitting. Qiskit pilot is declared per-instance calibration.

**Independent unit.** Circuit family after stripping numeric size suffixes; compiler observations on each family stay linked. One local CPU family; no independent hardware transfer.

**Scope limits.** Only device-transpilation successful matched tasks forTket/BQSKIT/Staq; no service remote latency. Missing/failed/timeouts excluded from conditional-success runtime target and retained in source audit; cannot infer success probability or realized routing speedup. Author timing environment differs in frequency/run state despite same CPU model.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| pilot_seconds | seconds Qiskit calibration cost |
| qubits | input qubit count |
| pilot_gates | Qiskit output two-qubit gate count |
| pilot_depth | Qiskit output two-qubit depth |
| load_seconds | Qiskit QASM loading seconds |
| is_tket | SDK indicator |
| is_bqskit | SDK indicator,elseStaq |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-031.original.v1 --output NEW_SUBMISSION; then score --task P100-031.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
