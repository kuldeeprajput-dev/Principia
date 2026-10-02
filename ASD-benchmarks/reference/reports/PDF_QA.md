# Findings PDF quality assurance

**Pass:** 25 scenario PDFs, 74 pages and 3,181,533 stored bytes.

Every page was rendered with Poppler and visually inspected. Equations, tables, source notes and page furniture are readable, with no observed clipping, overlap, missing mathematical glyphs or blank pages. The renderer preserved the editable Markdown sources.

This is a layout and file-integrity review. Scientific support, numerical correctness and evaluator validation are covered by separate reports. The SHA-256 values below bind the reviewed output bytes; `PDF_QA.json` also records the matching editable-source hashes.

## Final usability revision

Eight reader documents now use the shared evaluator commands (`--trust-code`, `evaluation/`) and clarify preserved historical evidence. Their 23 pages were re-rendered and visually inspected again. The other 17 PDFs and editable sources are byte-identical to the already inspected versions. No scientific values were edited by the renderer.

## Render-only changes

The renderer applies a consistent title/body hierarchy, paragraph spacing and header/footer. Table widths were adjusted for long task-family labels. Literal multiplication operators are preserved, and Unicode dash variants are normalized for reliable font rendering.

## Reviewed artifacts

| Scenario | Pages | Bytes | PDF SHA-256 |
|---|---:|---:|---|
| [P100-023](../cases/P100-023/final_results/FINDINGS.pdf) | 2 | 116,481 | `d60a09c54a0f1fd4bc2d1d236027b02843dd2b108176e8dd3e68d3cf369c457d` |
| [P100-024](../cases/P100-024/final_results/FINDINGS.pdf) | 3 | 115,687 | `1d1aac7abe22a6b316acaf46b4fd5aa7dcb6c77eac691244adb7bf6cd28fa1b7` |
| [P100-027](../cases/P100-027/final_results/FINDINGS.pdf) | 3 | 118,219 | `81034d6e755fd264ae82fe9a0b1a041f3d93f6c64ad8c32b33364883d6e078ec` |
| [P100-037](../cases/P100-037/final_results/FINDINGS.pdf) | 3 | 149,269 | `efba759968f5ad182b5d651fc701ce4413839a35f40c71e1ee50d318fda5b61c` |
| [P100-052](../cases/P100-052/final_results/FINDINGS.pdf) | 3 | 143,310 | `26996f6135412558f83ae50f1b83d000f901fc267bfaafca68416221065fea81` |
| [P100-053](../cases/P100-053/final_results/FINDINGS.pdf) | 3 | 150,286 | `74976841f3789826c49bb5ee9bc3cd4c47381ece6bf0acc9374ffc2a302627c4` |
| [P100-055](../cases/P100-055/final_results/FINDINGS.pdf) | 3 | 119,994 | `95edafe8a2be5f6f6e681ce68a68d403094a70bc7096b42c42acaac2cb10fc13` |
| [P100-057](../cases/P100-057/final_results/FINDINGS.pdf) | 3 | 115,428 | `0b4b665b95c764f6832daa60352669354321d675a2bd561c272f72d7ffa57e0c` |
| [P100-058](../cases/P100-058/final_results/FINDINGS.pdf) | 3 | 120,222 | `88ffee7db83f4893381674dc125c38d32f788b0e7f6f4ea65c64e72a8dda4ab2` |
| [P100-059](../cases/P100-059/final_results/FINDINGS.pdf) | 3 | 123,471 | `47d682f8bfce0b6351a97a0cdd5fbebc1e44accc36e36b4ef793e1cd84a51c43` |
| [P100-060](../cases/P100-060/final_results/FINDINGS.pdf) | 3 | 118,429 | `5decce9e0e3417e5c951065b05825d58616f8f018bf5e4e024bf0c15db369bef` |
| [P100-061](../cases/P100-061/final_results/FINDINGS.pdf) | 3 | 136,885 | `98ec010b6f4df5d97dbc4112802de310030e00fdbf2a2d8d24ed4787f3e63b66` |
| [P100-066](../cases/P100-066/final_results/FINDINGS.pdf) | 3 | 124,222 | `bf4b76525bbb56f0c441fd3f5157263e6edbdd304dbd21efba62f26659a62785` |
| [P100-067](../cases/P100-067/final_results/FINDINGS.pdf) | 3 | 159,259 | `c6c88ec0985c1e5a90eb908e8cff096a27aa7a187ccef62e70e2b98d2031b856` |
| [P100-069](../cases/P100-069/final_results/FINDINGS.pdf) | 3 | 122,393 | `1e945e6eb87d48d9e6fef5f97898a7cdbe68682138a255f7e093ae7ff3c688a9` |
| [P100-071](../cases/P100-071/final_results/FINDINGS.pdf) | 3 | 157,383 | `9dd994b15e48f1f3080d58171085c0215a06b26c2a8bd13ec2e05ae63d4020aa` |
| [P100-072](../cases/P100-072/final_results/FINDINGS.pdf) | 3 | 116,369 | `2b96da74959918ed7cbfc21521152a089ea81b5749f84eea5c02f48bbcf0c068` |
| [P100-073](../cases/P100-073/final_results/FINDINGS.pdf) | 3 | 121,083 | `bd048ed34c29749ca1bf18640202a148abe985392a17ebae401deb0714196668` |
| [P100-078](../cases/P100-078/final_results/FINDINGS.pdf) | 3 | 119,315 | `8e683123e2be7a30ec27a6d5673f2d35cbcecee43b01aa4e6c8f40758c43dbdf` |
| [P100-082](../cases/P100-082/final_results/FINDINGS.pdf) | 3 | 117,838 | `e335751fa5a255b0d1bcd13ee3bc62ccf011144c94b1ffe13dd71e795500a4c7` |
| [P100-083](../cases/P100-083/final_results/FINDINGS.pdf) | 3 | 121,068 | `0ba9cc52523763e961dd415bd93f076424452baf36e4477f7280329fca0a2550` |
| [P100-086](../cases/P100-086/final_results/FINDINGS.pdf) | 3 | 114,111 | `6ddecbeee9b13609000cbeb9142f8c5fd9fa4ab6a4f7a9a1159164b33bb5228c` |
| [P100-092](../cases/P100-092/final_results/FINDINGS.pdf) | 3 | 148,449 | `1f4ec1f3a877f5f99b3f058db28e068ecdb3dc815bdda355196e65fb304498bc` |
| [P100-096](../cases/P100-096/final_results/FINDINGS.pdf) | 3 | 114,282 | `56fe3ff6cfe33a937126a2ce3aee2775afec2ea37997cae52bbf077a3599b7ac` |
| [P100-100](../cases/P100-100/final_results/FINDINGS.pdf) | 3 | 118,080 | `5df54daab747da1dfa62bd73b9cebd94645689f8ee96c309708b4e9af98faee1` |

The collection build must refresh its final-results and release manifests after incorporating these PDFs. Raster previews and generation scripts remain in local working support rather than the release allowlist.
