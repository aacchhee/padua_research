# Claude audit handoff — lattice-unisolvence

Stage AUDIT at final delivery. **Required Claude (Opus5.5 xhigh) audit PENDING.** This is Codex development; separate Astra reconstruction supplements rather than replaces the cross-agent audit. Do not approve a merge from the presence of this file.

## Entry point and provenance

Branch `codex/lattice-unisolvence-20261031`, stacked on `codex/charter-unisolvence-20261031`; original base `eb7bdcdf3a587dd49ea9d692b1d27c7af053fe64`, audited update `3bd9d4e8e7817eaf0abd5b7a750ea77eb8101342`, administrative response `317a26597dedc9adc9cfc6a26fa00078df7d29e4` merged without rebasing. Rules read `e949ef06895acd5463cdf8df7e0e5f795218f70f`; unchanged rule blobs at subsequent parent merges. Exact launch/preparation pins: [provenance.json](provenance.json). Exact final review bytes: [audit-targets.json](audit-targets.json), checked by the committed content verifier; the eventual enclosing commit may also contain bookkeeping files outside its own self-excluding hash set.

Root orchestrator runtime model/effort metadata unexposed. Assigned developers: gpt-6.1-sol high literature; xhigh mathematical C0/C1/C3. Separate adversarial reconstruction: gpt-6-astra xhigh. Protocol review: gpt-6-astra medium. No ultra assignment. No agent besides root changed Git state. Two administrative merge commits' missing trailers are disclosed in LOG; no published-history rewrite was used to repair metadata.

Read AGENTS/WORKFLOW/CODEX at the audit head, then complete state/IDEAS.md including all old and appended obstruction/disposition tables. AC's task-specific exceptions are retained verbatim in REQUEST.md: Step0 baseline before exploration, no full duplicate screen required before launch, independent prior-art/reconstruction before acceptance, at most two directions, ten rounds with a justified two-round C1 extension, provisional theory IDs, interpolation rather than cubature. The charter text is preserved. A single CURRENT paragraph records this campaign at preparation.

## Claims and coverage to challenge

Use [report](report.md), [plan](plan.md), [progress](progress.md), direction candidate/round records and canonical [theory](../../tracks/lattice-unisolvence/README.md). PROVED direct statements, MEASURED computations and OPEN targets are separate files. No publication-level novelty claim.

C0: density q/k=1/d!, complete residue correction for the infinite diagonal mod6 count, and short-axis obstruction. The 5061 canonical count-trial rows represent77616 raw tuples and451 matching patterns (39d2/412d3). Completeness is only within the frozen nonzero-coefficient primitive single-fiber catalogue; omitted zeros/unions/boundary corrections are retained deferred, not excluded by theorem. Check every-pattern template inheritance and orbit quotient.

C3: all412 source patterns map to364 tested point-set representatives,2184 exact modular matrices,142 nonzero-witness survivors. Written determinant-polynomial degree and lifting/probability statements do not assert all-axis unisolvence or make deterministic seeds into random-event guarantees. General annihilator reductions support213 finite certificate instances among222 sampled deficiencies;9 unexplained cases remain OPEN.114 rectangle witnesses obstruct only pure axis rational-product determinants. Verify the explicit n1 mixed-axis obstruction and the isolated n2 all-field axis factorization directly, including signs and scale exponents. The n2 case is a finite-degree(a,b) survivor; its naive extension fails the tested scopes, and the unbounded3D target remains OPEN.

C1: distinguish exact count, complete quadratic criterion and scoped symmetry/mixed-factor obstructions from the unresolved growing-degree family. Odd-degree and shifted-phase cases escape the initial Chebyshev singularity; their measured stability must not be erased by that negative theorem or promoted into a log² theorem. Read the final analytic reductions and remaining contractivity/kernel obligations at their exact written scopes.

C3 sampled Lebesgue values and C1 adaptive sampled maxima are MEASURED floating estimates, not certified continuous suprema or asymptotic laws. Source facts are LITERATURE with named coverage, not inherited local proofs. No cubature property is assumed and no cubature lower bound rules out interpolation.

## Independent reconstruction and response

[Supplementary Astra report](independent/report.md) records its own input hashes, fresh independent implementations, developer reruns, literature crosschecks and any findings. [Protocol review](protocol/report.md) checks evidence links, scope, IDs and public-file constraints. Reading a result is not a rerun; the actual executions and content comparisons are recorded separately. Any new Claude findings go in audit-01.md; Codex answers in response-01.md without editing that audit. Material mathematical changes return to AUDIT.

## Reproduce consequential computations

From the repository root with Python3.12.14 (developer), NumPy2.3.5, SciPy1.17.0, SymPy1.14.0. Use a fresh output directory, and compare payloads independently of argv/timing metadata. Exact command/input/source hashes are also in each direction's evidence records.

```sh
mkdir -p /tmp/lattice-claude/c0
python tracks/lattice-unisolvence/code/c0_catalogue.py --output-dir /tmp/lattice-claude/c0
python tracks/lattice-unisolvence/code/c3_rank.py topics/lattice-unisolvence-20261031/directions/C0/catalogue.json --output /tmp/lattice-claude/ranks.json
python tracks/lattice-unisolvence/code/c3_structure.py topics/lattice-unisolvence-20261031/directions/C3/ranks.json --output /tmp/lattice-claude/structure.json
python tracks/lattice-unisolvence/code/c3_obstructions.py topics/lattice-unisolvence-20261031/directions/C3/ranks.json topics/lattice-unisolvence-20261031/directions/C3/structure.json --output /tmp/lattice-claude/obstructions.json
python tracks/lattice-unisolvence/code/c3_lowdegree.py topics/lattice-unisolvence-20261031/directions/C3/ranks.json topics/lattice-unisolvence-20261031/directions/C3/obstructions.json --output /tmp/lattice-claude/lowdegree.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python tracks/lattice-unisolvence/code/c3_lebesgue.py topics/lattice-unisolvence-20261031/directions/C3/ranks.json topics/lattice-unisolvence-20261031/directions/C0/catalogue.json --output /tmp/lattice-claude/lebesgue.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python tracks/lattice-unisolvence/code/c1_mod4.py --output /tmp/lattice-claude/mod4.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python tracks/lattice-unisolvence/code/c1_stability.py --output /tmp/lattice-claude/stability.json
python tracks/lattice-unisolvence/code/c1_symbolic.py --output /tmp/lattice-claude/symbolic.json
OPENBLAS_NUM_THREADS=2 OMP_NUM_THREADS=2 MKL_NUM_THREADS=2 python tracks/lattice-unisolvence/code/c1_gram.py --output /tmp/lattice-claude/gram.json
OPENBLAS_NUM_THREADS=2 OMP_NUM_THREADS=2 MKL_NUM_THREADS=2 python tracks/lattice-unisolvence/code/c1_extension.py --output /tmp/lattice-claude/extension.json
python tracks/lattice-unisolvence/code/verify_artifacts.py topics/lattice-unisolvence-20261031/audit-targets.json
git diff --check
```

The independent/ directory contains fresh separate checkers in addition to the reruns. The scientific proofs are written in theory files rather than delegated to CAS agreement. No large NTNU run is necessary for the stated finite/analytic claims; the OPEN asymptotic targets require mathematics rather than an unrecorded larger search.

## Integration, storage and requested next action

[Shared ledger](../padua-batch-20261031/ALLOCATIONS.md) preserves charter/MZ final ranges and lists this topic's provisional reservations. AC explicitly requested provisional theory IDs, so no competing final range is allocated. Coordinate final allocation with the named owner before readiness. The draft initially targets the charter branch; after AC merges charter PR#2, refresh/merge the charter-bearing main and retarget the PR as appropriate. Never rewrite the base, rebase published history, merge a PR, or push main.

The actual local squash rehearsal and its scope/conflicts are recorded in integration-rehearsal.md. It does not authorize a live merge or imply that all batch members are ready. [Cold storage](COLD_STORAGE.md) identifies staged bytes, hashes and regeneration/check commands; Windows receipt is not claimed. The parent's archival waiver is not substituted for a receipt here. No third-party PDF or fulltext extract is committed.

Next: `Claude (Opus 5.5 xhigh): Continue codex/lattice-unisolvence-20261031.`
