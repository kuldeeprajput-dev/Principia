# Frozen equations

## reference

sigmoid(b0+b1*r+b2*q+b3*NGRDI+b4*q*NGRDI+b5*tiny); r=Rfd/(1+abs(Rfd)), q=asinh(NPQ), size=ln(1+max(AREA_MM,0))/10

Coefficients in equation order: `[2.146619322140566, -1.0330324348456008, 0.44660750994737547, -0.9491476981650554, -0.5939073445142461, 0.06565896793020384]`. RBF mean/scale/centers are fully recorded in rules.json; those are learned transformation state, additional to the displayed coefficient count.

## baseline_constant

sigmoid(b0); r=Rfd/(1+abs(Rfd)), q=asinh(NPQ), size=ln(1+max(AREA_MM,0))/10

Coefficients in equation order: `[1.6623695231202744]`. RBF mean/scale/centers are fully recorded in rules.json; those are learned transformation state, additional to the displayed coefficient count.

## baseline_context

sigmoid(b0+b1*tiny+b2*salt+b3*drought+b4*highstress); r=Rfd/(1+abs(Rfd)), q=asinh(NPQ), size=ln(1+max(AREA_MM,0))/10

Coefficients in equation order: `[1.6068050120096518, 0.16137010021253675, -0.008831377982053922, -0.01049465684849475, 0.007742479279900696]`. RBF mean/scale/centers are fully recorded in rules.json; those are learned transformation state, additional to the displayed coefficient count.

## baseline_flexible

sigmoid(b0+sum_j b_j exp(-mean((z-center_j)^2)/2)); training-only standardization; r=Rfd/(1+abs(Rfd)), q=asinh(NPQ), size=ln(1+max(AREA_MM,0))/10

Coefficients in equation order: `[1.6028164800675464, -0.055432835744819275, -0.06409576215501837, -0.05389832021282944, 0.007879209126313456, 0.06701499914651333, -0.05408327309455587, 0.003553696730347372, 0.0677362143274463, 0.05400006900287537, -0.0195304894029623, 0.014257848774184685, 0.05762923401196398, 0.015189784898163576, 0.07679691043584463, 0.04518384457582821, -0.028706751916481192]`. RBF mean/scale/centers are fully recorded in rules.json; those are learned transformation state, additional to the displayed coefficient count.

## attempt_001_quenching

sigmoid(b0+b1/(1+max(NPQ,0))+b2*tiny); r=Rfd/(1+abs(Rfd)), q=asinh(NPQ), size=ln(1+max(AREA_MM,0))/10

Coefficients in equation order: `[1.5436972900938115, 0.12224853012130389, 0.15497876411765613]`. RBF mean/scale/centers are fully recorded in rules.json; those are learned transformation state, additional to the displayed coefficient count.

## attempt_002_recovery

sigmoid(b0+b1*Rfd/(1+abs(Rfd))+b2*asinh(NPQ)+b3*tiny); r=Rfd/(1+abs(Rfd)), q=asinh(NPQ), size=ln(1+max(AREA_MM,0))/10

Coefficients in equation order: `[2.09722457131003, -1.113167853969117, 0.3422015430843391, 0.03189577722432247]`. RBF mean/scale/centers are fully recorded in rules.json; those are learned transformation state, additional to the displayed coefficient count.

## attempt_003_pigment

sigmoid(b0+b1*r+b2*q+b3*NGRDI+b4*q*NGRDI+b5*tiny); r=Rfd/(1+abs(Rfd)), q=asinh(NPQ), size=ln(1+max(AREA_MM,0))/10

Coefficients in equation order: `[2.146619322140566, -1.0330324348456008, 0.44660750994737547, -0.9491476981650554, -0.5939073445142461, 0.06565896793020384]`. RBF mean/scale/centers are fully recorded in rules.json; those are learned transformation state, additional to the displayed coefficient count.

## attempt_004_morphology

sigmoid(b0+b1*r+b2*q+b3*NGRDI+b4*size+b5*size*q+b6*tiny); r=Rfd/(1+abs(Rfd)), q=asinh(NPQ), size=ln(1+max(AREA_MM,0))/10

Coefficients in equation order: `[1.956452879796881, -0.9450788784876437, 0.26658842446556985, -0.9749693565305201, 0.18233339652504374, 0.06932096345204805, 0.03493940161452631]`. RBF mean/scale/centers are fully recorded in rules.json; those are learned transformation state, additional to the displayed coefficient count.

## attempt_005_stress_regime

sigmoid(b0+b1*r+b2*q+b3*NGRDI+b4*tiny+b5*salt+b6*drought+b7*highstress+b8*q*salt+b9*q*drought); r=Rfd/(1+abs(Rfd)), q=asinh(NPQ), size=ln(1+max(AREA_MM,0))/10

Coefficients in equation order: `[2.3267909928753725, -1.1898021694183305, 0.39248881972369415, -1.4926769410972334, 0.047790491658704186, -0.041813710833844796, -0.03646198931865995, 0.018828393107361403, 0.0029918687342500054, 0.012437790703488978]`. RBF mean/scale/centers are fully recorded in rules.json; those are learned transformation state, additional to the displayed coefficient count.

