# Interim prior-results audit

Rules and audited input: `5440555cf326afdbd66b75bed195802013901c2d`.
Date: 2026-11-07. Auditor: distinct Codex worker, assigned `gpt-6-astra`
xhigh; runtime model/effort metadata is not independently exposed.
Role: supplementary adversarial audit authorized for this interim session,
not the pending formal Claude audit04, an AC convention decision, or PR
readiness approval. No producer, theory, historical audit, handoff, registry
or Git state was changed by this worker.

## Findings first

**No BLOCKING, MAJOR or MINOR finding was identified within the declared
scope.** The exact reruns below agree with the scoped claims. The following
NOTEs preserve boundaries that matter to the U1/U2/U3 decision; they are
not new defects and require no silent claim correction.

| ID / severity | Location at audited input | Assessment and decision consequence |
|---|---|---|
| IAP-N1 / NOTE | `response-03.md:11–38`; `theory/t10-log3-corollary.md:9–17`; `theory/r08-lattice-minima.md` | E4 remains AC's pending convention decision. The local implications explicitly depend on the named literature statements. This audit does not approve the label convention, verify the external proofs, or establish fresh primary-source reading. U1 operational/noise conclusions need no packing or sharp-kernel literature premise. |
| IAP-N2 / NOTE | `theory/r08-lattice-reduction.md`, parts 5–6; `theory/r08-lattice-higher.md:12–25` | The exclusions cover the full unshifted cosine image with strictly positive full-support weights. The global full-rank minima at degrees 3–5 and exclusions through degree 7 do not exclude phases, removed zero-mass nodes, arbitrary nonlinear sets, or U3 mixed constructions. Window minima 91/128 at degrees 6/7 are not established global minima. |
| IAP-N3 / NOTE | `theory/t8-r08-cubic-classification.md`; `theory/t8-r08-halfshift-measurements.md:53–68,83–86`; `attempts/T8-round08.md` | Complete exact rank classification is cubic. Even-degree failure is analytic for the first-unit half-shift class. Degrees 5/7 have selected exact-positive witnesses and floating determinant screens; no exact global determinant maximizer or full rank classification is claimed there. The cubic tie correction is disclosed as post-quality repair. The two-eligible-Leja-loss trigger remains unfulfilled. |

## Reading and novelty scope

Read AGENTS, WORKFLOW and the Codex role at the audited input, the current
log opening, preserved handoffs09/11, report-round08, response03, the four
`r08-lattice-*` proofs, the four `t8-r08-*` records, the rational-phase
certificate reduction, T8's attempt and tie-correction code, the lattice
independent report, and the necessary positive-weight/phase-boundary
arguments. Result-bearing code inspected includes the complete C++ lattice
enumerator, its Python driver and alternate checker, the complete
`t8_r08_check.py`, and the tie-correction runner. The lattice completion
driver was inspected to compare its scientific digest convention.

Literature/application review read the packing-source consequence,
R-Leja transfer, sharp projection corollary, and local parity log-four
proof, plus the relevant existing Betke–Henk, Chkifa and kernel source
records. `literature/INDEX.md` was consulted first through its coverage
header and targeted matching entries; the initial broad output was
truncated, and no complete index reading is claimed. No primary PDF was
opened or newly verified in this worker's session. Existing primary-reading
attestations remain attributed to their original readers. The complete
Minkowski source, Henk erratum, Belinsky text, supporting Chkifa chapter and
Kolomoitsev–Lomako proof chain were not read here.

This scope checks existing finite arithmetic, proof reductions, boundaries,
and literature-dependency labels. It proposes no mechanism, candidate,
priority claim or new negative-family conclusion. Accordingly the full
IDEAS novelty audit is not duplicated here; the root-assigned strategy
audit owns that broader gate. The accepted complete T7 quadratic
classification and unrelated historical theories were not reopened.

## Proof reconstruction

The row-HNF reduction is sound: positive diagonal factors and bounded
off-diagonal entries exhaust each full-rank integer lattice exactly once.
The pure third-axis test, the `u=0,v>0` test, and the `u>0` tests exhaust
short vectors by negation symmetry. For each fixed first two coordinates,
the distance to a multiple of `f` gives the exact minimum third-coordinate
absolute value. The formulas for the dual group solve `B h=0 mod q` and
enumerate exactly `q` distinct elements. Coordinatewise reflection of
residues decides cosine equality exactly, including boundary points.

Each cosine fiber has at most eight elements. Hence `q<=8|X|`; an attained
full-rank support of size `t`, coupled with complete enumeration through
`8(t-1)` and exact deficiencies for every smaller support, proves the
global minimum in this class. Character independence transfers rational
Fourier-incidence rank to real evaluation rank. The new rank reducer uses
monomial binomial Fourier columns reduced by triangular lattice quotient
division, rather than the producer's signed Chebyshev incidence columns.
Both full rank and deficiency are decided over the rationals.

The strictly-positive-weight transfer is also sound. A short three-support
relation gives `F=1-v²-w²+2uvw=u²` on the support, with degree at most the
relation's l1 length, integral zero and identity value one. Nonnegative
weights with positive identity mass contradict exactness. The one- and
two-support cases have the stated simpler witnesses. Thus the lattice
enumeration legitimately excludes arbitrary strictly positive weights on
the full unshifted image; it does not merely test one prescribed Haar rule.
Conversely admissibility makes folded Haar weights positive and exact.

For half-shifts, first-coordinate equality gives the fixed-point-free
pairing `k <-> M-1-k` and exactly `N` nodes. Translation by `N` induces the
coordinate-sign action with exactly `N mod 2` physical fixed nodes. The
domain trace and node permutation eigenspace dimensions give
`rank <= N-|D_t-(N mod 2)|/2`. The displayed trace formulas rule out every
even degree at least 2; at odd degrees only `t=2` can pass. This is a
necessary condition, not a sufficiency result at odd degrees.

For the cubic census, the DCT basis is invertible and exact alias reduction
gives `V=B C/8`. A separately assembled monomial dictionary gives the same
741 rational ranks. Nonzero characteristic-zero determinants for the old
nine witnesses follow from the written cyclotomic ring homomorphism and
the new nonzero determinants at splitting primes. A deficient modular rank
is never used as a characteristic-zero upper bound.

The local imported-theorem applications were checked at the implication
level. Packing scaling gives `det L >=38 n³/27`, followed by the fiber
bound and the degree-110 threshold. The R-Leja bound sums every-prefix
differences over a lower set, with coefficient series
`(1+t)^3/(1-t)^10`. Integer translation of the octahedron leaves its Fourier
kernel L1 norm unchanged and gives a fixed triangulation in `[0,2n]^3`;
the local sampling/Gram correction transfers the named polyhedral bound
to the oversampled projection. None of these steps proves the external
theorem itself or supplies a minimal-node interpolation norm bound.

## Executed exact checks

All runs below actually completed. No timeout or incomplete prefix is
reported as a success. All are deterministic; no random seeds are used.

### Lattice global minima and exclusions

A fresh `g++ -O3 -std=c++17 -Wall -Wextra` build of the frozen producer
enumerator supplied complete raw streams. Every retained smaller-fold case
was independently recounted using rational triangular node construction,
then ranked by the new monomial/Fraction reducer. The attaining supports
were independently recounted/ranked and separately tested against every
integer vector of l1 norm below `2n`.

| n | Complete determinant interval | All HNFs | Admissible | All smaller-fold `(fold,rank,count)` cases |
|---:|---:|---:|---:|---|
| 3 | 1–184 | 4,140,222 | 1,710,190 | `(16,15,1),(20,17,20),(20,18,3),(22,18,68)` |
| 4 | 1–352 | 28,911,538 | 8,634,185 | `(35,30,1),(39,33,3),(43,32,24)` |
| 5 | 1–592 | 137,029,493 | 30,171,840 | `(54,48,1),(63,53,3),(72,53,3)` |
| 6 | 1–672 | 200,821,041 | 12,910,075 | no fold at most 84 |
| 7 | 1–960 | 584,906,253 | 21,354,010 | no fold at most 120 |

The fresh exact attaining ranks/folds are `20/24`, `35/45`, `56/75` at
degrees 3/4/5. Their shortest dual lengths are exactly 6/8/10. Therefore
the global full-rank minima 24/45/75 and global folded minima 16/35/54
reproduce. Degrees 6/7 reproduce the scoped exact-N exclusions and bounded
minimum folds 91/128, without upgrading those bounded minima to globality.

The n7 execution took 161.825 seconds and matched the earlier scientific
digest over **all 960** per-determinant rows:
`909f9922a468ac00745d180344299e62d35e9b17e2b16ec881bd707eece5ae39`.
This is a fresh complete execution, not reuse of the old three-segment
raw files. The complete lattice driver took 358.952 seconds. Timings are
observations on the shared executor, not performance guarantees.

The same fresh complete streams independently have first admissible
determinants `38,92,178,304,486` at degrees 3–7, with respective counts
`8,24,24,8,24`. No source bound is needed for this from-1 arithmetic.
This supplies additional evidence without changing producer statuses.

The alternate forbidden-congruence checker was freshly executed for all
131,943 direct short-vector/HNF comparisons at degrees 1/2/3 and
determinants 1–40. A new rational node constructor also checked all 2,961
HNFs at determinants 1–16 against the alternate fold routine and `q/8`;
the largest actual fiber was eight.

The alternate degree-16 window completed determinants 5765–5772. All
5765–5771 were empty; 5772 had exactly 24 admissible HNFs, each with 2,887
folded nodes. Its lower-window global interpretation still uses the
explicit imported packing theorem. The alternate control/window driver
took 44.500 seconds. Degree-8–15 determinant windows were **not** freshly
rerun here; their reported results were reviewed through the proof and
existing independent record. Degrees 1/2's complete minima/classification
were not reopened.

Receipts: [lattice enumeration](evidence/iap-lattice-enumeration.json),
[alternate controls/window](evidence/iap-lattice-alternate.json),
[boundary controls](evidence/iap-boundaries.json).

### Half-shifts, old finite existence and structural boundaries

The independently assembled monomial DCT census covers all 741 cubic
parameters, giving the exact rank histogram

```
4:3, 7:21, 9:35, 10:82, 12:52, 13:8, 14:40,
15:132, 16:64, 17:188, 18:48, 19:60, 20:8.
```

Its eight full-rank parameters are precisely the eight claimed tuples.
Each has exact Chebyshev coefficient determinant absolute value `2^49`;
fresh actual-node modular certificates also pass for each. Thus the
mathematical lexicographic determinant tie selects `(1,4,11)`. This does
not erase or re-date the original post-quality repair.

The trace formulas were independently re-evaluated through degree 40;
the existing structural checker directly recounts the prescribed fold
and fixed-node samples at degrees 3–8. All selected degree-3/5/7
half-shifts have exact rational monomial-DCT rank `N`, exact node count
`N`, and two nonzero actual-node monomial determinants at fresh primes.

All nine old `M=N` witnesses at degrees
`1,3,4,5,7,8,9,11,12` have exact count `N` and two full-rank nonzero
monomial determinants. The new prime floor is 1,800,000,000; the resulting
primes differ from both the original certificates and the round08
1.7-billion-prime receipt. For degree 12 the new primes are 1,800,097,391
and 1,801,500,611. Exact root orders, primes, determinants and matrix hashes
are retained in [the T8 receipt](evidence/iap-t8.json).

The modular implementation is the inspected historical independent
`t8_r08_check.py`, freshly executed with different prime floors. It is not
represented as a newly independent modular-elimination implementation.
Its integer inputs and guarded int64 elimination products are below
signed-64-bit capacity. The new census assembly and lattice rank reducers
are independent implementations of the existing reductions.

Additional exact controls reproduce the phased tensor Gauss counterexample
for `q=2..8` by cyclotomic polynomial reduction, including all nonconstant
one-dimensional Chebyshev moments through `2q-1` and the `T_q` annihilator.
The `q=2` case indeed has 8 nodes versus dimension 10. Rational tetrahedron
controls at `t=1,1/2,1/3,1/10` reproduce the cardinal identities and vertex
maxima `max(1/t,(1/t+3)/2)`. The four existing order-19 examples reproduce
dual minima `4,4,4,3` and Haar `T111` moments `0,0,0,1/4`; this is a
boundary control, not a reopened exhaustive T7 census.

The nine-witness finite PROVED proposal has the needed written reduction,
committed regenerating checker/explicit finite inputs, exact positive
certificates and actual independent executions. This assessment does not
upgrade its old floating quality subsection or any all-degree existence
claim. No fresh Lebesgue mesh or degree-5/7 determinant-screen/selector
replay was performed in this arithmetic-focused worker.

## Reproduction and artifact identities

Executed from `/workspace/padua_research`:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-3d-20261106/interim-audit-01/code/iap_lattice.py enumeration --scratch /tmp/padua-iap-5440555-6phpcM/enumeration --receipt topics/padua-3d-20261106/interim-audit-01/evidence/iap-lattice-enumeration.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-3d-20261106/interim-audit-01/code/iap_lattice.py alternate --scratch /tmp/padua-iap-5440555-6phpcM/alternate --receipt topics/padua-3d-20261106/interim-audit-01/evidence/iap-lattice-alternate.json
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-3d-20261106/interim-audit-01/code/iap_t8.py --scratch /tmp/padua-iap-5440555-6phpcM/t8 --receipt topics/padua-3d-20261106/interim-audit-01/evidence/iap-t8.json
PYTHONDONTWRITEBYTECODE=1 python topics/padua-3d-20261106/interim-audit-01/code/iap_boundaries.py --receipt topics/padua-3d-20261106/interim-audit-01/evidence/iap-boundaries.json
PYTHONDONTWRITEBYTECODE=1 python topics/padua-3d-20261106/interim-audit-01/code/iap_validate.py --receipt topics/padua-3d-20261106/interim-audit-01/evidence/iap-validation.json
```

For another replay choose fresh scratch and receipt destinations; the
enumeration and cubic-census paths reject existing raw filenames. The raw records are local,
regenerate-only artifacts, not durable cold-storage delivery. All required
code and small evidence are in the repository; no inaccessible historical
raw file is required for the reruns. No new checker pins prose.

Environment: Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0, SymPy 1.14.0,
g++ Debian 14.2.0-19, Linux 6.18.57 x86_64 / glibc 2.41. The cloud runtime
skill was read and current running-environment status checked. No network
request, dependency installation or external source retrieval was needed.

The receipts identify actual commands, code/data/raw byte sizes and full
SHA-256 values. All eight reused source/input files checked by
`iap_boundaries.py` equal their bytes at the assigned commit. The frozen
C++ core remains
`e07ad9e51d5b883e7c6d813d396ef32ea0ac24eda253a73f6137f8b8f86feaa4`.
Audit checker identities:

| Code | SHA-256 |
|---|---|
| `iap_lattice.py` | `b40ba6e377a52ab6e398f1b59621ef28309faf931f30fb3ec39fadcffc50fc99` |
| `iap_t8.py` | `fab0101046b6e56b9d1ad052ad46d77100578d4c4a16f805d04f3c86c88228c3` |
| `iap_boundaries.py` | `35db71dc3e14002d29673bc940e8468e5aaca3d348991ecdad717b9991a68df9` |
| `iap_validate.py` | `a90de46c3203a2442b54c0df5527fcd9fde08cb1e38a872aa8c3995620e88e94` |

[Final validation](evidence/iap-validation.json) verifies 27 referenced
artifact identities and the n7 scientific digest. The five receipts are
5,609 / 1,959 / 10,322 / 3,153 / 1,885 bytes respectively, each below
16 KiB. No generated bulk output was added to Git by this worker.

## Coverage, verdict and residual uncertainty

**Interim verdict: supports the scoped prior claims audited here; no
material obstacle to the U1/U2/U3 strategic comparison was found.** The
finite lattice exclusions are strong only within their stated positive,
unshifted full-support class. They leave phased/mixed U3 possibilities
open. The exact nine-witness and half-shift certificates establish finite
unisolvence, without establishing good interpolation norms or an
all-degree construction. The source-dependent log-cubed estimate concerns
oversampled projection, without supplying minimal-node extraction bounds.

Uncovered here: fresh degree-8–15 determinant windows; complete accepted
degree-1/2 lattice/T7 classification; degree-6/7 global minima beyond the
recorded determinant windows; degree-8–109 finite complement; floating
quality/selection reruns; external primary theorem/proof verification; the
entire source/novelty/chronology and code-manifest audit; and the new usable
U1/U2/U3 claims assigned to other workers. These are not claimed as checked
by this report. E4 and every earlier AC decision remain pending exactly as
preserved. Formal Claude audit04 and readiness are not replaced.
