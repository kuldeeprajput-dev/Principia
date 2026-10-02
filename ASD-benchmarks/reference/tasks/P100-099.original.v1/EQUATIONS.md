# Frozen equations and complete coefficients

## reference

e+b0*r+b1*max(v,0)+b2*min(v,0); e=current30frame population mean,v=2*(e-e_t-30frames),r=prior300frame mean-e,a=e-2*e_t-30+e_t-60,sd=across-neuron SD of current30frame means,z=fraction of exactly-zero current neuron means,V=ventralCA1,G=sourcegroup3. All trace terms author processed units; coefficients dimensionless except RBF response coefficients in trace units.

Coefficients: `[0.6867260870834122, -0.08899487451882716, -0.006503860674957402]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## baseline_persistence

e; e=current30frame population mean,v=2*(e-e_t-30frames),r=prior300frame mean-e,a=e-2*e_t-30+e_t-60,sd=across-neuron SD of current30frame means,z=fraction of exactly-zero current neuron means,V=ventralCA1,G=sourcegroup3. All trace terms author processed units; coefficients dimensionless except RBF response coefficients in trace units.

Coefficients: `[]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## baseline_velocity

e+v; e=current30frame population mean,v=2*(e-e_t-30frames),r=prior300frame mean-e,a=e-2*e_t-30+e_t-60,sd=across-neuron SD of current30frame means,z=fraction of exactly-zero current neuron means,V=ventralCA1,G=sourcegroup3. All trace terms author processed units; coefficients dimensionless except RBF response coefficients in trace units.

Coefficients: `[]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## baseline_flexible

e+b0+sum_j b_j exp(-mean((z-center_j)^2)/2); e=current30frame population mean,v=2*(e-e_t-30frames),r=prior300frame mean-e,a=e-2*e_t-30+e_t-60,sd=across-neuron SD of current30frame means,z=fraction of exactly-zero current neuron means,V=ventralCA1,G=sourcegroup3. All trace terms author processed units; coefficients dimensionless except RBF response coefficients in trace units.

Coefficients: `[-0.0005049592767836469, 0.0003160050448351667, 4.09017601466013e-05, 6.1187987639189e-05, 0.00014650615340824552, 0.00011799086153481533, 9.919393991499227e-05, -0.0005649126137181538, 0.0002631659088357077, -1.550109780423279e-05, 4.3750256502862156e-05, 0.00017277390032070837, -0.0006173231900306478, -0.0003513802893839875, -0.00016166009456824136, 0.0003172479392720686, 0.0005555440961025343, -4.147254969441319e-05, 0.00013386285616404268, -1.6421072649031487e-06, 0.0006323095070026591]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## attempt_001_decay

(1+b0)*e; e=current30frame population mean,v=2*(e-e_t-30frames),r=prior300frame mean-e,a=e-2*e_t-30+e_t-60,sd=across-neuron SD of current30frame means,z=fraction of exactly-zero current neuron means,V=ventralCA1,G=sourcegroup3. All trace terms author processed units; coefficients dimensionless except RBF response coefficients in trace units.

Coefficients: `[-0.19844155353437315]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## attempt_002_relaxation

e+b0*r; e=current30frame population mean,v=2*(e-e_t-30frames),r=prior300frame mean-e,a=e-2*e_t-30+e_t-60,sd=across-neuron SD of current30frame means,z=fraction of exactly-zero current neuron means,V=ventralCA1,G=sourcegroup3. All trace terms author processed units; coefficients dimensionless except RBF response coefficients in trace units.

Coefficients: `[0.7947001656871333]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## attempt_003_inertia

e+b0*r+b1*v; e=current30frame population mean,v=2*(e-e_t-30frames),r=prior300frame mean-e,a=e-2*e_t-30+e_t-60,sd=across-neuron SD of current30frame means,z=fraction of exactly-zero current neuron means,V=ventralCA1,G=sourcegroup3. All trace terms author processed units; coefficients dimensionless except RBF response coefficients in trace units.

Coefficients: `[0.7324726723669354, -0.03729934822501623]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## attempt_004_heterogeneity

e+b0*r+b1*v+b2*sd+b3*sd*z; e=current30frame population mean,v=2*(e-e_t-30frames),r=prior300frame mean-e,a=e-2*e_t-30+e_t-60,sd=across-neuron SD of current30frame means,z=fraction of exactly-zero current neuron means,V=ventralCA1,G=sourcegroup3. All trace terms author processed units; coefficients dimensionless except RBF response coefficients in trace units.

Coefficients: `[0.658137543772557, -0.036825403285895675, -0.13788345268989236, 0.22921486766651822]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## attempt_005_region

e+b0*r+b1*v+b2*r*V+b3*v*V; e=current30frame population mean,v=2*(e-e_t-30frames),r=prior300frame mean-e,a=e-2*e_t-30+e_t-60,sd=across-neuron SD of current30frame means,z=fraction of exactly-zero current neuron means,V=ventralCA1,G=sourcegroup3. All trace terms author processed units; coefficients dimensionless except RBF response coefficients in trace units.

Coefficients: `[0.6460576121154069, -0.015906734691591273, 0.1169777731665511, -0.023067043497606493]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## attempt_006_asymmetry

e+b0*r+b1*max(v,0)+b2*min(v,0); e=current30frame population mean,v=2*(e-e_t-30frames),r=prior300frame mean-e,a=e-2*e_t-30+e_t-60,sd=across-neuron SD of current30frame means,z=fraction of exactly-zero current neuron means,V=ventralCA1,G=sourcegroup3. All trace terms author processed units; coefficients dimensionless except RBF response coefficients in trace units.

Coefficients: `[0.6867260870834122, -0.08899487451882716, -0.006503860674957402]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

