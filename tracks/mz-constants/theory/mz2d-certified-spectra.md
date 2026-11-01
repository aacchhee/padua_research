# PD-T107 — Exact finite Padua spectrum enclosures

Provisional alias: `PD-T?mz2d-codex-02`. Final ID assigned at PR preparation, 2026-11-01; required Claude audit PENDING.

ID kind: PD-T.
Aliases: signed-dominance congruence certificate; rational Padua pencil
inertia; finite two-dimensional MZ verification.
Split from: finite verification support for PD-T028; no all-degree target
is narrowed to these four cases.
Split into: the separate eta-threshold refutation has its own negative
record PD-N044 in `mz2d-eta-counterexample.md`.

## Statement

For the signed interpolatory `dx dy` Padua rule, fixed even checkerboard,
total-degree orthonormal Legendre Gram `G_(m,m-1)` and conventions in
`topics/padua-mz-2d-20261101/definitions.md`, the following **strict open
intervals** enclose the extreme eigenvalues. Every decimal endpoint
denotes the exact terminating rational number.

| m | n | Dimension | lambda minimum | lambda maximum |
|---|---|---|---|---|
| 10 | 9 | 55 | (0.356191, 0.356192) | (1.634856, 1.634857) |
| 20 | 19 | 210 | (0.272233, 0.272234) | (1.723313, 1.723314) |
| 30 | 29 | 465 | (0.236705, 0.236706) | (1.757929, 1.757930) |
| 40 | 39 | 820 | (0.214817, 0.214818) | (1.778088, 1.778089) |

The mathematical reduction, exact producer acceptance checks and actual
different-agent replay are complete. Required Claude mathematical audit
remains pending and is not replaced by the replay.

## Definitions

In this file `H` is the continuous Chebyshev product mass matrix and `Q`
is the quadrature mass matrix on `Pi_(m-1)`. These are `M,R` in
[PD-T106](mz2d-aliasing.md). A different matrix called `R_t`
below is an integer change-of-coordinate proposal; it is never the
quadrature mass matrix. Inertia counts are ordered `(negative,zero,positive)`.

## Assumptions

Precisely `m in {10,20,30,40}`, `n=m-1`, the signed Lebesgue rule and
fixed coordinates. The analytic alias formula is as proved in
PD-T106. Exact execution trusts Python integer/Fraction and
FLINT integer matrix arithmetic, the interpreter and the recorded
execution environment. Numerical eigensolvers only select rational
endpoints and integer transformation proposals; their accuracy is not
an acceptance premise. Run Python without `-O`, because exact acceptance
conditions are implemented as assertions.

## Status by part

Overall status: **PROVED** (computer-assisted development, independent
exact execution complete; required Claude mathematical audit pending).
The written finite reduction, exact arithmetic checker, essential
evidence and actual different-agent replay are all present. This is a
finite computer-assisted claim, not MEASURED floating evidence.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| All eight finite open eigenvalue intervals | PROVED | Exact producer checks and separately executed replay passed |

Candidate / claim disposition: retained verification of a known
rational-pencil mechanism; no novelty claim. General positivity,
`eta<1`, upper gaps and endpoint rates beyond these four cases remain
OPEN under their own targets.

## Depends on

PD-T106: rational exact moments, Chebyshev mass pencil and
Legendre change-of-basis identity. Elementary symmetric-matrix
variational principles, continuous dependence of eigenvalues and
Sylvester's law of inertia. No external numerical theorem is used.

## Checks

Producer: `/root/exact_engine`, Codex, requested `gpt-6.1-sol` medium
technical effort. Mathematical reduction writer: `/root/d1_aliasing`,
Codex, requested `gpt-6.1-sol` xhigh; resolved runtime metadata is not
independently exposed. Rules SHA used by the checker:
`806cc7b4509fd93bae652f9545d32d95529f8281`.

Executed producer command, as recorded by that worker:

```sh
PYTHONPATH=/tmp/padua-flint OPENBLAS_NUM_THREADS=1 python tracks/mz-constants/code/mz2d_exact.py --m 10 20 30 40 --output topics/padua-mz-2d-20261101/evidence/exact-spectra.json
```

| Artifact | SHA-256 / size |
|---|---|
| `tracks/mz-constants/code/mz2d_exact.py` | `5d1f005e2307d3a26badc9c1a44ce313dc9126625a49fba5d59430c151cf9c70` |
| `topics/padua-mz-2d-20261101/evidence/exact-spectra.json` | `5456917afe8fea69b0a776270ef3ae79fdc33deb02d27f89648fc342f78b93de`, 31,822 bytes |
| Fixed definitions used by producer | `4ac0e391859a14e4d6f752f1244df0701e99d9b3d8ab8570bd632520f517c7db` |

Environment: Python 3.12.14; python-flint 0.9.0; NumPy 2.3.5; SciPy
1.17.0; Linux/glibc details in the receipt. Endpoint arithmetic uses
Python `fractions.Fraction`; acceptance products use FLINT `fmpz_mat`.
The receipt records all 16 endpoint inertia counts, dimensions, positive
denominator scales, signed diagonals, positive strict-dominance row
margins, transform hashes and runtime metadata. Reconstructing and
checking those matrices is performed by the committed code. Small
essential evidence is retained within the repository limits; external
archival export remains the orchestrator's task.

The mathematical writer inspected the complete checker, D6 reduction,
producer metadata and the separately executed replay records. The
writer did not claim the replay as their own execution; the replay was
actually performed by Codex `/root/protocol`, requested `gpt-6.1-sol`
medium technical effort, and committed by the orchestrator at `df44db4`.
The dated receipt is
`topics/padua-mz-2d-20261101/independent-checks.md`.

Independent producer command, exit 0:

```sh
PYTHONPATH=/tmp/padua-flint OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python tracks/mz-constants/code/mz2d_exact.py --m 10 20 30 40 --output topics/padua-mz-2d-20261101/evidence/independent-exact-spectra.json
PYTHONPATH=/tmp/padua-flint OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python tracks/mz-constants/code/mz2d_independent_check.py
```

The actual independent producer receipt has SHA-256
`18c8623442664aa119d3581b701d200315d454071d6b8f6c89cbaf540fe34d9c`.
The independently written additional checker has SHA-256
`5e455d747dc5dca84c883ed900095ff4a2bb40767f4ebcb3261d7d583df7bdfc`,
and its receipt `evidence/independent-additional-checks.json` has
SHA-256 `2da16fa5c8f2f480ab7c12270b8c9b95ec49028f9df6b1cf4062af4f11897717`.
The mathematical writer verified these source/receipt hashes after the
worker reported completion. All producer result fields match after
removing **only** nested runtime `seconds`; command/output paths remain
explicit. Exact counts, denominators, signed diagonals, strict margins,
intervals and the stored m=30 polynomial agree.

The additional checker independently constructs exact signed nodal
weights over cyclotomic fields at m=1,...,5: 245 moments and 371
nodal-Gram/symbolic-integral pairs agree with the pencil. Every alias
region is tested in 1,221 moment comparisons for m=2,...,12. All six
recorded malformed-certificate/input controls reject. The stored m=30
coefficient list is evaluated directly with separate Fraction sums.
Those regressions supplement, rather than replace, the all-degree
analytic reduction. Trusted additional arithmetic includes SymPy
1.14.0 cyclotomic quotients and polynomial integration; other versions
match the producer environment.

## Sources

Local exact alias theorem and
`topics/padua-mz-2d-20261101/directions/D6.md`. No primary-literature
statement supplies the finite enclosures. Classical positive
Chebyshev cubature has a different measure and is not silently
substituted for this signed Lebesgue rule.

## Proof or evidence

### 1. Exact construction and an optional parity reduction

For basis indices `(a,b),(c,d)` with `a+b,c+d<=m-1`, use the four
product-to-sum modes `(r,s)` from `{a+c,|a-c|} x {b+d,|b-d|}`.
The continuous mass entry is one quarter of the sum of `h_r h_s`;
the quadrature mass entry is one quarter of the sum of the exact
`q_m(r,s)` in PD-T106. Multiplicities are retained. These
formulas construct both matrices in rational arithmetic before any
eigensolve is called. `H` is positive definite, since a nonzero real
polynomial has positive squared Lebesgue integral. The generalized
eigenvalues of `(Q,H)` are the stated Legendre eigenvalues.

The exact checker uses two blocks. If `m` is even, a nonzero direct
alias moment requires `r` even, and a nonzero complementary moment
also requires `m-f_m(r)` even. Since folding preserves parity, every
nonzero moment has `r` even. The two x-degree parity blocks therefore
decouple. If `m` is odd, the same argument uses `m+1` even and gives
two y-degree parity blocks. Every off-block entry of both `H` and `Q`
is explicitly checked to be zero, so no unjustified two-coordinate
parity symmetry is assumed. All four certified cases have even `m`.

### 2. Exact signed-dominance congruence certifies inertia

Fix one rational endpoint `t` and one parity block. Clear a common
**positive** denominator `d_t` to form the symmetric integer matrix

\[
 A_t=d_t(Q-tH).
\]

A numerical generalized eigenbasis proposes a square integer matrix
`R_t` by scaling its entries by `10^12` and rounding. No claim about
its invertibility or conditioning is assumed. Compute

\[
 B_t=R_t^\mathsf T A_tR_t
\]

in exact integer arithmetic, check symmetry, and check for every row
the strict integer inequality

\[
 |(B_t)_{ii}|>\sum_{j\ne i}|(B_t)_{ij}|.            \tag{1}
\]

In particular all its diagonal entries are nonzero. For `s in [0,1]`,
let `B_t(s)` retain the same diagonal and multiply every off-diagonal
entry by `s`. Every matrix along this path satisfies strict dominance.
It is nonsingular: if `B_t(s)x=0`, choose `i` maximizing nonzero
`|x_i|`; the `i`th row would give
`|B_ii||x_i| <= sum_(j!=i)|s B_ij||x_j| < |B_ii||x_i|`, a contradiction.
Its eigenvalues cannot cross zero along the continuous symmetric path.
Its inertia therefore equals that of the diagonal matrix `B_t(0)`,
namely the counts of negative and positive diagonal entries and no
zeros.

Nonsingularity of `B_t` itself proves `R_t` invertible: a nonzero
vector in `ker R_t` would also be in `ker B_t`. Sylvester's law
identifies the inertia of `A_t` with that of `B_t`. Multiplication by
the positive denominator `d_t` preserves inertia. Summing exact
counts over the two blocks gives the exact inertia of `Q-tH`.

Thus any numerical error in the proposed transform can only cause
failure of the exact acceptance check. The eigensolver is not trusted
to give either the inertia or a correct approximate eigenvector.

### 3. Inertia counts imply strict open endpoints

Since `H` is positive definite, congruence by its inverse square root
turns `Q-tH` into `H^(-1/2)QH^(-1/2)-tI`. Its negative inertia is
exactly the number of generalized eigenvalues below `t`. Strict
dominance has ruled out eigenvalues equal to `t`.

For each lower-eigenvalue bracket `(a,b)`, the code requires negative
counts zero at `a` and one at `b`. This proves `a<lambda_min<b`.
For each upper-eigenvalue bracket `(c,d)`, with full dimension `N`,
it requires negative counts `N-1` at `c` and `N` at `d`. This proves
`c<lambda_max<d`. The producer receipt records exactly these accepted
counts at every listed endpoint. The table follows from the exact
checks, which the independent worker separately executed successfully. ∎

## Scope

These certificates establish only the four explicit finite cases.
They show positivity and `eta<1` in those cases, but give
no all-`m` bound, rate, limit, signed-weight positivity claim or sharp
constant. Floating spectra at larger `m` remain separate MEASURED
evidence. The exact m=30 witness is separated into its own PD-N record
because a threshold refutation is a different substantive conclusion.

## Open items

- Independent exact replay is complete and its evidence is integrated
  above. Required mathematical audit is still pending.
- The general signed Padua upper/lower and endpoint questions remain
  OPEN under PD-T028 and campaign D2/D3 records.
- Required Claude mathematical audit remains separate from the
  different-agent computational rerun.

## History

2026-11-01, exact producer completed m=10,20,30,40 by integer
congruence after abandoning a slower fraction-free LU implementation.
Only the final signed-dominance checker is a proof dependency. Codex
mathematical developer `/root/d1_aliasing` wrote this reduction at the
orchestrator's explicit request, while leaving independent rerun
PENDING. No Git mutation or shared-registry edit.

2026-11-01, after independent replay was actually executed, the writer
verified the frozen checker and all cited receipt hashes. Updated
CONDITIONAL to PROVED with explicit computational trust and finite
scope. The separate required Claude audit remains PENDING; supplementary
Codex execution and peer checks do not replace it.
