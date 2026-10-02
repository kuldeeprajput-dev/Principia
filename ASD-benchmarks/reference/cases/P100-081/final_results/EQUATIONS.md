# Complete frozen equation register

## Executable equations and parameters

Each expression below uses the named inputs in the units table. `exp`, `log`, and `sqrt` have their conventional mathematical meanings. Coefficients are fitted on development data only; all calibration is declared above. The portable `rules.json` contains full precision and each model’s complete training scope.

**constant**

`b0`

Parameters: b0 = 1.2071758.

**flexible**

`b0+b1*C+b2*depth+b3*pH+b4*C**2+b5*C*depth+b6*depth**2`

Parameters: b0 = 0.55164746, b1 = -0.080971448, b2 = 0.032799586, b3 = 0.10070533, b4 = 0.0026804512, b5 = -0.0017541724, b6 = -0.00069846712.

**linear**

`b0+b1*C+b2*depth`

Parameters: b0 = 1.3344542, b1 = -0.07849868, b2 = 0.0054155674.

**two_phase_volume**

`1/((1-1.724*C/100)/mineral+(1.724*C/100)/organic)`

Parameters: mineral = 1.5992328, organic = 0.14237092.

**structural_porosity**

`a*exp(-b*C)+c*log1p(depth/10)`

Parameters: a = 1.4296668, b = 0.12316888, c = 0.1274077.

**depth_compaction**

`1/((1-1.724*C/100)/(m0+m1*(1-exp(-depth/L)))+(1.724*C/100)/organic)`

Parameters: m0 = 1.1115082, m1 = 0.5996835, L = 4.9562483, organic = 0.14665741.

**organic_consolidation**

`1/((1-1.724*C/100)/mineral+(1.724*C/100)/(organic*(1+depth/L)))`

Parameters: mineral = 1.599659, organic = 0.12703903, L = 93.147201.

**acidity_aggregation**

`1/((1-1.724*C/100)/(mineral*exp(k*(pH-6)))+(1.724*C/100)/organic)`

Parameters: mineral = 1.5107712, organic = 0.15141003, k = 0.093844854.


