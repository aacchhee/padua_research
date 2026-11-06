# N0 — exact predecessor replay

Verification record only; no new mathematical claim or rate. Developer: Codex,
requested gpt-6.1-sol medium (serving metadata is not independently exposed).
Rules and inputs read at `cafb74ab6f7738c8af83d0cd0f518b81af16f253`.
No Git mutation, shared log, registry or handoff edit by this worker.
The novelty gate is inapplicable to this bounded replay: no candidate,
mechanism, negative conclusion or priority claim is introduced.

## Scope and prospective interpretation

Handoff 01 asks for “three PD-T338 rows” but specifies two grids and two
rules. We resolve this ambiguity by checking **all four** combinations:
T24/rotQ24 × BJ/mirror at degree 12. The existing native implementation
also produces every degree 2–12 prefix, so all 44 rows are compared.
The quantities are the exact squared aggregate-source spectral-normal-output
capacity endpoints `Knode_squared`, `KHS_squared`, `Urow_squared` and
`upper_squared`, not exact capacities or scalar-operation error cubes.
This does not replay the later PD-T338 fits.

The SH checks execute the unchanged predecessor `sh_independent.py`: both
BJ and mirror at n=2,3,4, and 88 symbolic creator identities through degree
eight. Its accepted theorem hash pin matches before execution. The checker
uses arbitrary-precision integers in NumPy object arrays and SymPy rational
polynomials, rather than floating trigonometric node evaluations.

The coordinator wrote and pushed plan commit `ed5515e` before authorizing
these experiments. CLI help and source methods were inspected first. All
predecessor files remain unchanged. No family-admission or growth scan is
part of N0.

## Reproduction

From the repository root, using a fresh external working directory:

```sh
python -B topics/padua-lanczos-nonproduct-20261105/code/n0_replay.py --work-dir /tmp/padua-lanczos-nonproduct-20261105/n0/canonical --evidence topics/padua-lanczos-nonproduct-20261105/evidence/n0-replay.json
```

The wrapper first runs the predecessor SH checker and compares its scientific
rows, symbolic checks and pins with committed `sh-independent-current.json`.
It recovers the 616,693-byte legacy input read-only with:

```sh
git show 2b52b432fe59c9a50aef9deebe5152c5d6874465:topics/padua-lanczos-drift-20261101/evidence/e1-full-sweep.json
```

Input SHA-256 must equal
`0d9c236fe879879b7f546596c554d213b7b8c408d31dec08dd79146c7d629344`.
The wrapper compiles unchanged `g1_independent.cpp` with
`g++ -O3 -std=c++17 ... -lgmpxx -lgmp`, then executes:

```sh
/tmp/padua-lanczos-nonproduct-20261105/n0/canonical/g1_independent triangle 12 bj
/tmp/padua-lanczos-nonproduct-20261105/n0/canonical/g1_independent triangle 12 mirror
/tmp/padua-lanczos-nonproduct-20261105/n0/canonical/g1_independent rotated 12 bj
/tmp/padua-lanczos-nonproduct-20261105/n0/canonical/g1_independent rotated 12 mirror
```

Two independent native processes run concurrently with an 1800-second
per-case limit. The unchanged predecessor `g1_independent_run.equal`
compares every endpoint by exact rational cross multiplication, choices,
source and basis dimensions, node counts and normal-projector trace against
the pinned legacy input. The legacy schema has no pivot-tie field; the wrapper
checks that these fixed-rule native runs report no adaptive ties. The native
implementation checks exact Gram orthogonality and
positive pivots. All 90 sources appear in every degree-12 case; both grids
have M > N_12=91 (325 and 625 nodes respectively).

## Actual execution

The initial SH-only early replay passed in 0.889925922 seconds, with output
SHA-256 `1e3dff0655b22f943c0cda4ca2ec3f436aed80f7c288caf04ce838be53303dba`.
Its six rows and symbolic result equal the committed reference. The full
canonical wrapper reruns SH and records its separate timing and output hash.

**N0 PASS.** All six canonical SH rows and all 88 symbolic identities match;
all four requested degree-12 rows and all 44 degree-2–12 prefix endpoint
rows match exactly. SH canonical runtime is in the receipt. Native timings
below are actual native process wall times reported by the unchanged native
implementation, with the rotated cases run concurrently.

| Grid/rule | Native seconds | Raw output SHA-256 |
|---|---:|---|
| T24 BJ | 3.54016 | `d6ee83925cb809899f0bb91d2c5974081f0693fd1ba83b8e825d1eacbbafa0e5` |
| T24 mirror | 1.65532 | `413deae74b8a7bff12855d520d25ca099450048823fd94f376eab634faa99399` |
| rotQ24 BJ | 87.2075 | `94f11f2f820134eb27b534166241450f7faa14e7d1fcaab253a9f55b9e454c45` |
| rotQ24 mirror | 96.2293 | `4c20068748037f4de2f3ecdb5a06e1057b1ae269f1f4f1fa0c6e5ae9154e47ea` |

The initial wrapper encountered a receipt-only `KeyError: pivot_ties` after
exact endpoint comparison, because the legacy schema omits that key. Native
runs completed unchanged. The wrapper was corrected to check the fixed-rule
empty tie lists without comparing an absent field. Its `--resume-completed`
mode then verified the completed outputs and produced the final receipt,
without executing native cases again. The original wrapper hash is retained
in the receipt; no endpoint mismatch occurred. To reproduce that final
verification after running the original commands, append
`--resume-completed` to the wrapper command. A fresh run of the corrected
wrapper needs no recovery option.

The compact [execution receipt](evidence/n0-replay.json) records code/input
hashes, actual commands, environment, separate verification timings, and each
canonical degree-12 exact row's normalized-content hash.
External raw JSONL/logs stay under the command's working directory;
they are regenerable temporary artifacts, with archival pending.

## Limits

This replay is separate actual execution of predecessor code. It is not an
independent audit of newly developed mathematical claims. Supplemental exact
SH checks do not constitute a finite reduction of the all-degree theorem.
Exact finite endpoint agreement supplies no asymptotic growth or IEEE-error
claim, and does not admit any new genuinely non-product family.
