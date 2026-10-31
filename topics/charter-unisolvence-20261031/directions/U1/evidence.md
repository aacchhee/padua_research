# U1 execution and evidence record

Rules/base `d36722823441dc40c6e19d69a174459348dd309c`. Producer: Codex, assigned/inherited `gpt-6.1-sol` xhigh. All commands below were actually executed in `/workspace/padua_research` on 2026-10-31. Root owns Git and will pin the staged source commit/blob IDs; until then content hashes identify the exact tested code.

## Canonical checker and environment

`exact_checker.py` SHA-256: `4216b9944c45345709ba11ffbb59b70799432329b646c0c44446da9be2cff56b`.

Python 3.12.14, Clang22.1.3 build; SymPy1.14.0 for the symbolic mode only. Linux6.18.57 x86_64, glibc2.41. Finite arithmetic uses the committed local exact implementation: prime fields and F4/F8/F16 in polynomial bases modulo respectively t²+t+1, t³+t+1, t⁴+t+1. These are exact arithmetic tests, not floating point. The proof is self-contained algebra; the finite samples are verification and do not prove the universal theorem.

## Final executed commands and compact output

`python3 topics/charter-unisolvence-20261031/directions/U1/exact_checker.py --samples 20 --output /workspace/padua-cold/charter-unisolvence-20261031/U1/exact-fields.json`

Result: exit0, all assertions PASS. Seed20261031, 55 field/degree settings, 20 random labelled axis pairs each =1100 pairs and2200 parity checks. Prime fields p=2,3,5,7,11,13,31 and binary extension fields F4,F8,F16; m=0,…,min(7,q−2), so each required axis has enough distinct elements. Axes are sampled independently and may overlap; actual overlaps are recorded by setting. The checker compares both determinant identities, complementary-minor symmetry, Δr=2^rH_r in its valid range, full-minor normalization, the corrected all-characteristic iff, both parities, and the original iff in odd characteristic. It separately exhausts every ordered length2 X and length3 Y over F4 for m=1:288 pairs and576 boards, all unisolvent and all violating the original quasi-definiteness necessity. Explicit examples are F4 m1 determinants[2,2] and F8 m2 determinants[6,4], with bit encodings documented in the negative theorem.

`python3 topics/charter-unisolvence-20261031/directions/U1/exact_checker.py --symbolic --output /workspace/padua-cold/charter-unisolvence-20261031/U1/symbolic-factors.json`

Result: exit0, all assertions PASS, six cases (m=2,3,4, both parities). Direct full multivariate m2 determinants; exact axis-factor/Hankel conversion and squared identity for full m3/4 factors; direct one-variable checkerboard determinants for all six cases. The full multivariate m3/4 checkerboard determinants were not directly expanded. `symbolic-factors.md` gives every factor, multiplicity, compact quartic definition, direct-slice output and sign convention.

An additional scratch exact SymPy command verified the compact length5 quadratic and length6 quartic definitions against the small axis determinant quotient; both assertions passed. This supports the readable record and is not a claimed separate theorem or computer proof.

## Noncanonical earlier runs and source reproduction

The unchanged imported source hs_ff.py was actually run by U0 within run_all.py, exit0. Its source-copy log and identities are recorded in U0 evidence, not inherited from supplied prose. Scope:14(p,m) settings,600 random disjoint-axis labellings each and both parities=16800 parity checks, seed1; agreement1.0000 for its odd-prime samples. This is measured reproduction only.

The first local symbolic implementation was interrupted with exit130 at global rational numerator/denominator expansion; it supplied no canonical result. An intermediate factor-assembly implementation then completed successfully, but expensive rational moment determinants motivated the final polynomial-axis implementation. Earlier finite/symbolic executions with other code hashes are historical development, not canonical evidence. Both final modes were rerun after the last code edit, and their JSON embeds the frozen code hash above. No failed computation route is promoted into a PD-N statement.

## Independence and remaining work

Producer reruns are not independent audit. The orchestrator arranged a distinct Astra adversarial reconstruction and rerun; its report/output is stored separately under `independent/u1/`. This record does not claim its outcome before delivery. Final Claude handoff, ID allocation, Git pinning, and Windows cold-storage delivery belong to the orchestrator. There are no unexecuted producer checks required for the stated proofs. Further random sampling is not needed to establish them.

## Cold-storage manifest and retrieval

Only staged artifacts are listed. No Windows delivery is claimed.

| Artifact | Actual staged location | Bytes | SHA-256 | Frozen generator / checker result |
|---|---|---|---|---|
| Exact field report | `/workspace/padua-cold/charter-unisolvence-20261031/U1/exact-fields.json` | 10186 | `2e11931b57274e3444a93ea92755fac79b1cbd2d4d1fd24136760a9c4f3db937` | final finite command above / PASS |
| Symbolic factor report | `/workspace/padua-cold/charter-unisolvence-20261031/U1/symbolic-factors.json` | 18648 | `df44efc4f554d14f825f6ec42eb917cd73b1e515e0da55193b8db52034728342` | final symbolic command above / PASS |

Both are generated by the checker hash above; source commit/blob pinning is pending root's checkpoint. Compact committed evidence is this file plus symbolic-factors.md; neither large output is a proof dependency. The two stdout copies are byte-identical duplicates and are not essential artifacts. Retain the canonical reports and source in Padua campaign storage until AC directs otherwise. Retrieve from the actual paths above or rerun the frozen commands, then verify byte count and SHA-256. Intended final destination is AC's `C:\Users\andreyac\Downloads\padua\cold_storage\charter-unisolvence-20261031\`; cloud staging is not a delivery receipt.
