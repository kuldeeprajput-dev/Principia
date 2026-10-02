# Equations and frozen states

## generic

f_hat=70 (generic five-point upper case)

```json
{
  "case": 98,
  "kind": "generic",
  "training_groups": [],
  "training_rows": 0,
  "parameters": 0,
  "equation": "f_hat=70 (generic five-point upper case)"
}
```

## qhull

Construct conv{+/- (e_i-e_j)/d_ij} in four dimensions; count distinct normalized facet equations (rounded to 9 decimals)

```json
{
  "case": 98,
  "kind": "qhull",
  "training_groups": [],
  "training_rows": 0,
  "parameters": 0,
  "equation": "Construct conv{+/- (e_i-e_j)/d_ij} in four dimensions; count distinct normalized facet equations (rounded to 9 decimals)"
}
```

## attempt_001

f_hat=b0+b1*t; t=number of exact four-cycle distance ties

```json
{
  "case": 98,
  "kind": "ties",
  "training_groups": [
    "0288f3b02f917f5e119a",
    "028afed4d554c431651a",
    "1f7357342483b36cacd0",
    "27b8d34ddd469687dedc",
    "291b45fdb3c2cd49f2c6",
    "2c267eb626fedab5a299",
    "2f087477ef49a141631c",
    "3101c6033238dde2ab02",
    "32e44a721ebeef726c4d",
    "36f8e6eaadb292b1a6f2",
    "3765af74da302184295e",
    "3cc13c1d806cc92e7961",
    "3e12637f5262999b8e11",
    "477c977e4c435449b0c0",
    "4e314928d5225f1b4238",
    "4f5d91bb1fb0920c4564",
    "5190180166128cc1c820",
    "51eed56f2826c581b875",
    "582514787182f8d30c85",
    "5c0037b7c09797800b11",
    "5dcea5100fa669413fe2",
    "5fbe758176eaa1e54caa",
    "62766ae14a298fa70e87",
    "670a59ee11b2b98783a0",
    "690f1eb3f8f3386acf2e",
    "69ad66b75309be59546b",
    "6b786c3ec5f1af7ce6aa",
    "6dd87995d0416dab360d",
    "6f887688f26a2a3a62bc",
    "7752d114e35d02c3e69e",
    "957c98c8f9b4ddea8c77",
    "96ccf535d32b428a3308",
    "994edf3ed421604cc7c7",
    "9984e0332e8f3fe951df",
    "9ab1711b040323988411",
    "a598ee84ac81798c8dd1",
    "b0cec9ca268d31af665d",
    "b3c811706a084603284e",
    "b69d3b096813dcdf8f05",
    "b9d84d5a70d2a08c20c2",
    "bb804dc8262c5e61d598",
    "bc2c18d8e654c340a38b",
    "be149cc757d088eed556",
    "be29a7ae7a11cf62532e",
    "c2f027966b109396be88",
    "c385389464ffedb5c629",
    "cfef21812b7087f7922e",
    "d063e28474343fdfd670",
    "d203ce5d24f9a5e18696",
    "d455bce052bb1a8dab3b",
    "d534573c245060cc6b77",
    "d5818c150b14d68537a9",
    "d87c1d98322a204e746a",
    "e6cf09e283cd04661f52",
    "e6d3084d8adf90092dfd",
    "e6fd0cf12402f52ae1de",
    "e75e122c59619d0472a6",
    "e81517531ab933c5bbb3",
    "f479cb69b1294c128a6f",
    "f523057fad479269b057",
    "f6abc3db0171fc9690db",
    "ff53570bc6b68ffeb8a0"
  ],
  "training_rows": 62,
  "parameters": 2,
  "equation": "f_hat=b0+b1*t; t=number of exact four-cycle distance ties",
  "coefficients": [
    68.50493305144471,
    -2.940451021846374
  ],
  "feature_indices": [
    0,
    1
  ]
}
```

## attempt_002

f_hat=b0+b1*r; r=rank of equality normals

```json
{
  "case": 98,
  "kind": "rank",
  "training_groups": [
    "0288f3b02f917f5e119a",
    "028afed4d554c431651a",
    "1f7357342483b36cacd0",
    "27b8d34ddd469687dedc",
    "291b45fdb3c2cd49f2c6",
    "2c267eb626fedab5a299",
    "2f087477ef49a141631c",
    "3101c6033238dde2ab02",
    "32e44a721ebeef726c4d",
    "36f8e6eaadb292b1a6f2",
    "3765af74da302184295e",
    "3cc13c1d806cc92e7961",
    "3e12637f5262999b8e11",
    "477c977e4c435449b0c0",
    "4e314928d5225f1b4238",
    "4f5d91bb1fb0920c4564",
    "5190180166128cc1c820",
    "51eed56f2826c581b875",
    "582514787182f8d30c85",
    "5c0037b7c09797800b11",
    "5dcea5100fa669413fe2",
    "5fbe758176eaa1e54caa",
    "62766ae14a298fa70e87",
    "670a59ee11b2b98783a0",
    "690f1eb3f8f3386acf2e",
    "69ad66b75309be59546b",
    "6b786c3ec5f1af7ce6aa",
    "6dd87995d0416dab360d",
    "6f887688f26a2a3a62bc",
    "7752d114e35d02c3e69e",
    "957c98c8f9b4ddea8c77",
    "96ccf535d32b428a3308",
    "994edf3ed421604cc7c7",
    "9984e0332e8f3fe951df",
    "9ab1711b040323988411",
    "a598ee84ac81798c8dd1",
    "b0cec9ca268d31af665d",
    "b3c811706a084603284e",
    "b69d3b096813dcdf8f05",
    "b9d84d5a70d2a08c20c2",
    "bb804dc8262c5e61d598",
    "bc2c18d8e654c340a38b",
    "be149cc757d088eed556",
    "be29a7ae7a11cf62532e",
    "c2f027966b109396be88",
    "c385389464ffedb5c629",
    "cfef21812b7087f7922e",
    "d063e28474343fdfd670",
    "d203ce5d24f9a5e18696",
    "d455bce052bb1a8dab3b",
    "d534573c245060cc6b77",
    "d5818c150b14d68537a9",
    "d87c1d98322a204e746a",
    "e6cf09e283cd04661f52",
    "e6d3084d8adf90092dfd",
    "e6fd0cf12402f52ae1de",
    "e75e122c59619d0472a6",
    "e81517531ab933c5bbb3",
    "f479cb69b1294c128a6f",
    "f523057fad479269b057",
    "f6abc3db0171fc9690db",
    "ff53570bc6b68ffeb8a0"
  ],
  "training_rows": 62,
  "parameters": 2,
  "equation": "f_hat=b0+b1*r; r=rank of equality normals",
  "coefficients": [
    71.8669201520913,
    -5.797718631178718
  ],
  "feature_indices": [
    0,
    2
  ]
}
```

## attempt_003

f_hat=b0+b1*t+b2*r+b3*t^2

```json
{
  "case": 98,
  "kind": "interactions",
  "training_groups": [
    "0288f3b02f917f5e119a",
    "028afed4d554c431651a",
    "1f7357342483b36cacd0",
    "27b8d34ddd469687dedc",
    "291b45fdb3c2cd49f2c6",
    "2c267eb626fedab5a299",
    "2f087477ef49a141631c",
    "3101c6033238dde2ab02",
    "32e44a721ebeef726c4d",
    "36f8e6eaadb292b1a6f2",
    "3765af74da302184295e",
    "3cc13c1d806cc92e7961",
    "3e12637f5262999b8e11",
    "477c977e4c435449b0c0",
    "4e314928d5225f1b4238",
    "4f5d91bb1fb0920c4564",
    "5190180166128cc1c820",
    "51eed56f2826c581b875",
    "582514787182f8d30c85",
    "5c0037b7c09797800b11",
    "5dcea5100fa669413fe2",
    "5fbe758176eaa1e54caa",
    "62766ae14a298fa70e87",
    "670a59ee11b2b98783a0",
    "690f1eb3f8f3386acf2e",
    "69ad66b75309be59546b",
    "6b786c3ec5f1af7ce6aa",
    "6dd87995d0416dab360d",
    "6f887688f26a2a3a62bc",
    "7752d114e35d02c3e69e",
    "957c98c8f9b4ddea8c77",
    "96ccf535d32b428a3308",
    "994edf3ed421604cc7c7",
    "9984e0332e8f3fe951df",
    "9ab1711b040323988411",
    "a598ee84ac81798c8dd1",
    "b0cec9ca268d31af665d",
    "b3c811706a084603284e",
    "b69d3b096813dcdf8f05",
    "b9d84d5a70d2a08c20c2",
    "bb804dc8262c5e61d598",
    "bc2c18d8e654c340a38b",
    "be149cc757d088eed556",
    "be29a7ae7a11cf62532e",
    "c2f027966b109396be88",
    "c385389464ffedb5c629",
    "cfef21812b7087f7922e",
    "d063e28474343fdfd670",
    "d203ce5d24f9a5e18696",
    "d455bce052bb1a8dab3b",
    "d534573c245060cc6b77",
    "d5818c150b14d68537a9",
    "d87c1d98322a204e746a",
    "e6cf09e283cd04661f52",
    "e6d3084d8adf90092dfd",
    "e6fd0cf12402f52ae1de",
    "e75e122c59619d0472a6",
    "e81517531ab933c5bbb3",
    "f479cb69b1294c128a6f",
    "f523057fad479269b057",
    "f6abc3db0171fc9690db",
    "ff53570bc6b68ffeb8a0"
  ],
  "training_rows": 62,
  "parameters": 4,
  "equation": "f_hat=b0+b1*t+b2*r+b3*t^2",
  "coefficients": [
    70.10930266777277,
    -2.727328029272672,
    -1.4013279879266383,
    0.033181979639193906
  ],
  "feature_indices": [
    0,
    1,
    2,
    3
  ]
}
```

## attempt_004

f=number of distinct exact feasible potentials phi with phi_0=0 and abs(phi_i-phi_j)<=d_ij; enumerate all signed spanning trees

```json
{
  "case": 98,
  "kind": "polar",
  "training_groups": [],
  "training_rows": 0,
  "parameters": 0,
  "equation": "f=number of distinct exact feasible potentials phi with phi_0=0 and abs(phi_i-phi_j)<=d_ij; enumerate all signed spanning trees"
}
```

## attempt_005

Same potential construction restricted to star trees only; tested simplification

```json
{
  "case": 98,
  "kind": "star",
  "training_groups": [],
  "training_rows": 0,
  "parameters": 0,
  "equation": "Same potential construction restricted to star trees only; tested simplification"
}
```

## reference

Construct conv{+/- (e_i-e_j)/d_ij} in four dimensions; count distinct normalized facet equations (rounded to 9 decimals)

```json
{
  "case": 98,
  "kind": "qhull",
  "training_groups": [],
  "training_rows": 0,
  "parameters": 0,
  "equation": "Construct conv{+/- (e_i-e_j)/d_ij} in four dimensions; count distinct normalized facet equations (rounded to 9 decimals)"
}
```

