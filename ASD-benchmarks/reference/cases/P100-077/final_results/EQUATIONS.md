# Frozen equations

## reference

j*(1-p-q+j)=exp(beta)*(p-j)*(q-j); y_hat=100*j, L=max(0,p+q-1), U=min(p,q)

Coefficients: `[4.066978644629878]`. Full bounds in rules.json.

## baseline_independence

j=p*q; y_hat=100*j, L=max(0,p+q-1), U=min(p,q)

Coefficients: `[]`. Full bounds in rules.json.

## baseline_constant

j=clip(b0,L,U); y_hat=100*j, L=max(0,p+q-1), U=min(p,q)

Coefficients: `[0.05]`. Full bounds in rules.json.

## baseline_flexible

j=clip(b0+b1*p+b2*q+b3*ln(dose),L,U); y_hat=100*j, L=max(0,p+q-1), U=min(p,q)

Coefficients: `[0.0010661845979413058, 0.17253653715745357, -0.10845480072459561, -0.00039845755554133674]`. Full bounds in rules.json.

## attempt_001_competence

j=p*q+alpha*(min(p,q)-p*q); y_hat=100*j, L=max(0,p+q-1), U=min(p,q)

Coefficients: `[0.44585696657558344]`. Full bounds in rules.json.

## attempt_002_odds_ratio

j*(1-p-q+j)=exp(beta)*(p-j)*(q-j); y_hat=100*j, L=max(0,p+q-1), U=min(p,q)

Coefficients: `[4.066978644629878]`. Full bounds in rules.json.

## attempt_003_common_fraction

j=clip(p*q/tau,L,U); y_hat=100*j, L=max(0,p+q-1), U=min(p,q)

Coefficients: `[0.044369258522499566]`. Full bounds in rules.json.

## attempt_004_dose_competence

j=p*q+sigmoid(b0+b1*ln(dose))*(min(p,q)-p*q); y_hat=100*j, L=max(0,p+q-1), U=min(p,q)

Coefficients: `[0.17994276798883393, -0.29216775314321874]`. Full bounds in rules.json.

## attempt_005_competition

j=p*q+alpha*(p*q-L), -1<=alpha<=0; y_hat=100*j, L=max(0,p+q-1), U=min(p,q)

Coefficients: `[-2.7318353725398715e-14]`. Full bounds in rules.json.

