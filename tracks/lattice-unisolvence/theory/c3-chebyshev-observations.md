# PD-N?lattice-c3-codex-03 — Finite Chebyshev tests do not support the small-index 3D fibres as a high-quality family

ID kind: PD-N. Aliases: sampled Lebesgue comparison; finite Lobatto screen. Split from: c3-rank-observations.md. Split into: none.

## Statement and negative-result scope

Attempted mechanism: use the modular-rank-surviving small-index single-congruence fibres directly on Chebyshev–Lobatto axes as a competitive 3D total-degree interpolation family. In the frozen degrees n=1..6, c3_lebesgue.py evaluated all142 representative rank survivors. At n=3..6, every specialization with condition2<10^12 has a sampled21^3-mesh Lebesgue value exceeding the corresponding discrete-Leja-ordered lower-set reference and tensor-mesh QR approximate-Fekete reference. The other specializations are numerically singular or ill-conditioned and were not assigned a Lebesgue value. This finite screen gives no favorable higher-degree performance lead in the catalogue.

Overall status: MEASURED floating arithmetic. Candidate disposition: failed as an immediately competitive family within this numerical screen; no asymptotic theorem, universal lower bound, exact singularity classification or rejection of other character patterns is claimed. The measured mesh maximum is a sampled lower bound on the true Lebesgue constant only if interpolation exists; floating numerical rank does not itself prove that hypothesis.

## Observations

| n | stable solves / tested | best sampled value | Leja lower-set reference | QR approximate Fekete reference |
|---|---:|---:|---:|---:|
| 1 |32/50|2.0000|5.0000|2.0000|
| 2 |9/19|4.8410|7.0000|7.0000|
| 3 |11/32|88.9939|13.1747|8.3207|
| 4 |8/18|1497.7664|19.4982|11.2449|
| 5 |8/16|3863.7021|26.3366|13.8575|
| 6 |4/7|97819.0568|40.2764|22.1915|

The ordinary unpermuted lower set is substantially worse (sampled values5,49,901,19259,430999,9884927). It is retained, but comparison only to this poor ordering would be misleading: axis ordering matters even for an abstract lower set. Discrete Leja ordering is therefore included explicitly.

For the k6,a111 consecutive-axis subfamily, all represented n2..6 rows were included. At n3 some residues are numerically singular and the stable sampled values include172.53 and3573.31; n4 includes1717.23,2965.55 and5205465.94; n5 includes29178.66 and1910673.94 with others numerically singular; n6's residue0 has condition196942.64 and sampled value128122.67. No such list of finite observations proves exponential growth or disproves a polylogarithmic asymptotic statement.

The isolated degree2 axis-factorable pattern C3-8ea9e9f33e3d has condition4.89725 and sampled value5.84805. Its exact unisolvence follows from PD-T?lattice-c3-codex-04, not numerical rank. The best degree2 value4.84099 belongs to a different mixed-axis pattern.

## Methods / checks

Total-degree product-Chebyshev basis. Candidate axes are Lobatto at their specified lengths. Mesh is the21^3 tensor Lobatto mesh. Cardinal functions are computed from V^T solves; only condition<10^12 cases are solved. Reference lower sets use three(n+1)-point Lobatto axes with natural or greedy discrete-Leja ordering. The QR reference uses SciPy pivoted QR on the transpose of the evaluation matrix of the(2n+1)^3 tensor Lobatto mesh. This is standard mesh extraction and is not claimed to reproduce the Bos–De Marchi–Vianello curve-specific construction.

NumPy2.3.5, SciPy1.17.0, Python3.12.14; exact configuration is embedded in lebesgue.json. Canonical code SHA256bf9cdb7c057f6ddf1793d99e6d338b1c1cfa37a274e5a6ac9689085f6bb3d66e; output SHA256ee98828d9fe4b790c02059a60e00bacddcd9bceb835d90706c03cfb03bedb3a0. Independent Astra rerun reproduced the reported values; its durable audit owns the acceptance disposition. Finite differences between numerical implementations would not create an asymptotic conclusion.

Axis-reversal/permutation transport is justified by physical cube reflections/permutations as explained in c3-rank-observations.md. No cubature property is used.

## Sources / limits / history

Closest source leads: Bos–De Marchi–Vianello trivariate Lissajous extraction, Dencker–Erb spectral-space interpolation and lower-set interpolation; literature baseline states their reading limits. No source theorem is a dependency. Remaining work would require a different cardinality-valid structural family or a proved degree-dependent estimate, not more unstructured repetitions of this finite screen. 2026-10-31, Codex C3 developer, assigned gpt-6.1-sol xhigh, rules/base e949ef06895acd5463cdf8df7e0e5f795218f70f.
