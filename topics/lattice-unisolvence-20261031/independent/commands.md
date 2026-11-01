# Independent execution record

All commands below were actually executed from `/workspace/padua_research` and completed with exit status zero. Paths shown are repository-relative. This is a consequential-command record, not a transcript of every read or exploratory comparison. Outputs belong only to `topics/lattice-unisolvence-20261031/independent/`. Python 3.12.14, SymPy 1.14.0, NumPy 2.3.5 and SciPy 1.17.0 were used where applicable.

## Separate implementations

These scripts were written by the adversarial auditor. They do not import developer implementations. Some share the auditor's own elementary rank helper. Each records its own hash and the relevant input hashes in its output.

```sh
python topics/lattice-unisolvence-20261031/independent/reconstruct_count.py topics/lattice-unisolvence-20261031/independent/count-reconstruction.json
python topics/lattice-unisolvence-20261031/independent/reconstruct_rank.py topics/lattice-unisolvence-20261031/independent/rank-reconstruction.json
python topics/lattice-unisolvence-20261031/independent/reconstruct_structure.py topics/lattice-unisolvence-20261031/independent/structure-reconstruction.json
python topics/lattice-unisolvence-20261031/independent/reconstruct_obstructions.py topics/lattice-unisolvence-20261031/independent/obstruction-reconstruction.json
python topics/lattice-unisolvence-20261031/independent/reconstruct_lowdegree.py topics/lattice-unisolvence-20261031/independent/lowdegree-reconstruction.json
python topics/lattice-unisolvence-20261031/independent/reconstruct_c1.py topics/lattice-unisolvence-20261031/independent/c1-reconstruction.json
python topics/lattice-unisolvence-20261031/independent/reconstruct_row_moments.py topics/lattice-unisolvence-20261031/independent/row-moments-reconstruction.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/lattice-unisolvence-20261031/independent/reconstruct_gram.py topics/lattice-unisolvence-20261031/independent/gram-reconstruction.json
```

The final row-moment run includes 200 exact kernel-dimension comparisons, empty and full rows, small characteristics, and the normalized symbolic n3 matrix. The final C1 reconstruction includes all 84 modular draws after the two-round extension. The finite Gram checks are floating MEASURED corroboration of a separately reconstructed written proof.

## Unchanged developer programs, independent executions

```sh
python tracks/lattice-unisolvence/code/c0_catalogue.py --output-dir topics/lattice-unisolvence-20261031/independent/c0-rerun
python tracks/lattice-unisolvence/code/c3_rank.py topics/lattice-unisolvence-20261031/directions/C0/catalogue.json --output topics/lattice-unisolvence-20261031/independent/c3-rerun.json
python tracks/lattice-unisolvence/code/c3_structure.py topics/lattice-unisolvence-20261031/directions/C3/ranks.json --output topics/lattice-unisolvence-20261031/independent/c3-structure-rerun.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python tracks/lattice-unisolvence/code/c3_lebesgue.py topics/lattice-unisolvence-20261031/directions/C3/ranks.json topics/lattice-unisolvence-20261031/directions/C0/catalogue.json --output topics/lattice-unisolvence-20261031/independent/c3-lebesgue-rerun.json
python tracks/lattice-unisolvence/code/c3_obstructions.py topics/lattice-unisolvence-20261031/directions/C3/ranks.json topics/lattice-unisolvence-20261031/directions/C3/structure.json --output topics/lattice-unisolvence-20261031/independent/c3-obstructions-rerun.json
python tracks/lattice-unisolvence/code/c3_lowdegree.py topics/lattice-unisolvence-20261031/directions/C3/ranks.json topics/lattice-unisolvence-20261031/directions/C3/obstructions.json --output topics/lattice-unisolvence-20261031/independent/c3-lowdegree-rerun.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python tracks/lattice-unisolvence/code/c1_mod4.py --output topics/lattice-unisolvence-20261031/independent/c1-rerun.json
OPENBLAS_NUM_THREADS=2 OMP_NUM_THREADS=2 MKL_NUM_THREADS=2 python tracks/lattice-unisolvence/code/c1_stability.py --output topics/lattice-unisolvence-20261031/independent/c1-stability-rerun.json
python tracks/lattice-unisolvence/code/c1_symbolic.py --output topics/lattice-unisolvence-20261031/independent/c1-symbolic-rerun.json
OPENBLAS_NUM_THREADS=2 OMP_NUM_THREADS=2 MKL_NUM_THREADS=2 python tracks/lattice-unisolvence/code/c1_gram.py --output topics/lattice-unisolvence-20261031/independent/c1-gram-rerun.json
OPENBLAS_NUM_THREADS=2 OMP_NUM_THREADS=2 MKL_NUM_THREADS=2 python tracks/lattice-unisolvence/code/c1_extension.py --output topics/lattice-unisolvence-20261031/independent/c1-extension-rerun.json
```

C1 stdout is retained in the corresponding `*-rerun.log` files. C0 outputs are byte-identical to the developer outputs. C3 scientific payloads agree after excluding command/output-path and timing metadata. C1 symbolic and Gram outputs are byte-identical. Stability/extension scientific payloads agree exactly after excluding wall-clock times. The main C1 rerun differs by at most 7.11e-15 in floating values; all nonfloating data agree.

An initial C1 stability execution with one BLAS thread produced minute floating differences and a different adaptive sample count near ties, so a strict comparison failed. The completed controlled replay used the developer's two-thread environment; its scientific payload agrees exactly. The first output was overwritten, not archived. This is an execution-environment observation, not an exact numerical certificate or a mathematical counterexample. All floating observations remain MEASURED.

Additional executed inline Python checks produced `c1-rectangle-check.json` (the n3 exact modular rectangle), `c3-records-check.json` (manifest and all 412 source-row coverage), and the three C1 rerun-comparison JSONs. The final hash verification is recorded in `audit-targets.json`. Native web-reader operations and precisely inspected primary sections are recorded in `literature-crosscheck.md`; no source-proof inheritance or complete-paper reading is claimed.
