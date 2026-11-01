# C3 evidence and reproducibility

Rules read and development base e949ef06895acd5463cdf8df7e0e5f795218f70f. Developer: Codex C3 subagent, assigned gpt-6.1-sol xhigh, runtime metadata unexposed. Root owns all Git/shared-state operations. All numerical/data claims below correspond to executed commands; no external source theorem is inherited.

Canonical machine manifest: artifact-manifest.json (full SHA256, byte counts, code/input identities). Every JSON output also embeds its actual argv, source hashes, Python version and deterministic seeds where applicable. Python3.12.14; SymPy1.14.0; NumPy2.3.5; SciPy1.17.0. The NumPy configuration/BLAS information is embedded in lebesgue.json. Numerical command pins OPENBLAS_NUM_THREADS=1 and OMP_NUM_THREADS=1.

## Completed runs

1. `python tracks/lattice-unisolvence/code/c3_rank.py topics/lattice-unisolvence-20261031/directions/C0/catalogue.json --output topics/lattice-unisolvence-20261031/directions/C3/ranks.json`

   Code a95afbb764838662358dc70d2fd5a7eddf335d3ae48254d29b717fa015143332; input21cd7610051d7f51e8578051da164f73ef112d9081765cea7156b26f01441430; output560471d0053fef785bcee9c64f1b7fe9a384e24c0c74ef3d4cd58b9d6c703130,535224bytes. Exit0,12.187seconds. Scope:412d3 C0 source patterns,364actual-set/reversal representatives, six exact modular draws each=2184tests. Primes1009,1013,1019; two trials each. Seed=`2026103103 + int(point_sha256[:16],16) + 1000003*p + 1000000007*trial`; every axis list stored.142reps full at least once,140full in every trial. Initial rank sanity checks on nonsingular and singular2x2 matrices passed.

2. `python tracks/lattice-unisolvence/code/c3_structure.py topics/lattice-unisolvence-20261031/directions/C3/ranks.json --output topics/lattice-unisolvence-20261031/directions/C3/structure.json`

   Code4a0695ef40f4f2d6d451c39df469eccc9b7287701c0e4baa628eaf1b16e39fdb; outputd5c34e03d7c62a0f0f63470a742ff1e6b26f4dd774bb1c916e6ebee1416144be,39828bytes. Exit0. Exhaustive restricted layer cover test:127/222deficient reps. Integer witnesses use69n<=2survivors, axis values sampled without replacement from[-30,30], seed=`2026103104 + int(point_sha256[:16],16)`;68nonzero Bareiss determinants, one accidental zero specialization retained. All50normalized n1 symbolic determinants computed;23have mixed factors. No full rank was inferred from floating arithmetic.

3. `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python tracks/lattice-unisolvence/code/c3_lebesgue.py topics/lattice-unisolvence-20261031/directions/C3/ranks.json topics/lattice-unisolvence-20261031/directions/C0/catalogue.json --output topics/lattice-unisolvence-20261031/directions/C3/lebesgue.json`

   Codebf9cdb7c057f6ddf1793d99e6d338b1c1cfa37a274e5a6ac9689085f6bb3d66e; outputee98828d9fe4b790c02059a60e00bacddcd9bceb835d90706c03cfb03bedb3a0,69136bytes. Exit0. All142rank-surviving reps included; targetk6,a111consecutive family explicitly retained.21³Lobatto sampling points, stable-solve cutoff condition2<10^12; no exact singularity inference. References: natural lower set, discrete-Leja-ordered lower set and SciPy pivoted-QR approximate Fekete extraction from(2n+1)³Lobatto mesh. Best sampled n1..6values2,4.84099,88.99387,1497.76641,3863.70206,97819.05677. All floating conclusions MEASURED; no growth-law inference.

4. `python tracks/lattice-unisolvence/code/c3_obstructions.py topics/lattice-unisolvence-20261031/directions/C3/ranks.json topics/lattice-unisolvence-20261031/directions/C3/structure.json --output topics/lattice-unisolvence-20261031/directions/C3/obstructions.json`

   Code9088670ef3aa95b8493b7afa6029e3f90a00a184e825e2045dd24fd8cad0f379; outputd61b0a60f1b99aad93b96514ef78f05f5e1542514d6db7756fbd916a54a76def,139840bytes. Exit0. Of95cover-unexplained deficient reps,86receive layer-removal/projected-count certificates. For142survivors, all3axis pairs tested in one2x2rectangle overF1009 with seed=`2026103105 + int(point_sha256[:16],16) + 1000000007*(3*pair[0]+pair[1])`. All axes and four determinant residues stored.114nonzero rectangle witnesses refute an axis-only rational product by the written exact reduction;28all-zero tests are inconclusive.

5. `python tracks/lattice-unisolvence/code/c3_lowdegree.py topics/lattice-unisolvence-20261031/directions/C3/ranks.json topics/lattice-unisolvence-20261031/directions/C3/obstructions.json --output topics/lattice-unisolvence-20261031/directions/C3/lowdegree.json`

   Final codefb4f249058d425a684ef7a62aaf674f00527e00e0848ae368d18fad4702331dd; outputc23ee5bf0ca2bc22576628965e882360e1ea66821f50d1e1d7030791b3650b8d,2933bytes. Exit0. Nine leftover deficient reps all fail exhaustive coordinate-subbox dimension certificates (0/9, route failure only). Direct normalized10x10 n2 determinant factors into axis blocks, checked by exact expansion. A separate direct determinant proof is in c3-n2-axis-factorization.md, not an unproved inference from zero rectangle tests.

6. `python tracks/lattice-unisolvence/code/c3_records.py`

   Exit0. Generates412row pattern-outcomes.tsv (all required properties, including unknown/untested) and artifact-manifest.json. Their identities are returned by the script and pinned in the manifest/audit handoff. No scientific result depends on the prose generator.

## Preserved failed runs and corrections

The first lowdegree.py run completed its mathematics but failed JSON serialization because a SymPy Integer multiplicity was not a native int. It returned exit1 and produced no usable evidence output. The one-line int conversion was applied, and the full canonical command reran successfully at the final code hash above. This is an implementation correction, not a failed mathematical result.

The first records.py invocation had an unterminated Python raw string ending in a Windows backslash; it returned exit1 before creating records. The path literal was corrected and the full command reran. No result is credited to that failed invocation. One seeded integer n1 determinant was exactly zero; it remains in structure.json and does not refute generic nonvanishing witnessed at other axes.

## Independent checks and acceptance

Supplementary Astra agent /root/adversarial separately reran all2184ranks and the structure/Lebesgue/obstruction/lowdegree scripts, and used fresh independent rank, recursive hitting-set, projected-count, determinant and subbox implementations. Its messages report agreement. It also checked the generic reduction, annihilator proofs, n1 mixed criterion and n2 direct factor proof. These are independently executed checks, not developer self-approval; the auditor's durable report and final signed hash snapshot control acceptance. Required Claude audit remains pending under campaign workflow.

## Evidence retention and runs needed

The five scientific outputs total786961bytes; each is below1MB. They are necessary small reproducibility evidence within workflow limits; root decides final commit inclusion and checks the campaign's combined5MB limit. No third-party PDF/fulltext is included. AC's designated cold destination is `C:\Users\andreyac\Downloads\padua\cold_storage\lattice-unisolvence-20261031\`; no Windows delivery is claimed and no cold-storage-dependent proof is used. Transfer receipt is pending only if root chooses cold archival.

Runs needed: no blind additional finite rank runs. Final supplementary Astra snapshot/claim disposition, required Claude audit, and any AC cold-storage receipt remain pending. The original unbounded-degree target and nine residual generic singularity cases remain OPEN; a future computation needs a concrete new structural question frozen before launch.
