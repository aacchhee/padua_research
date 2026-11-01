# PD-N?mz2d-codex-01 — A finite signed-Padua eta greater than three quarters

ID kind: PD-N.
Aliases: Padua m30 threshold witness; integer Chebyshev Rayleigh
counterexample; eta-three-quarter transfer.
Split from: the finite threshold test of IDEA?mz2d-codex-02; the
exact spectral enclosures remain separate in PD-T?mz2d-codex-02.
Split into: none.

## Statement

Let `Q_30` be the signed interpolatory Lebesgue rule on the fixed even
checkerboard `Pad_30`, and use total-degree `Pi_29` and orthonormal
Legendre normalization from the campaign definitions. Define the
integer-coefficient polynomial

\[
 p(x,y)=\sum_{(a,b,z)\in\mathcal C}zT_a(x)T_b(y),
\]

where `C` is **exactly** the 225 coefficient triples in
`results` with `m=30`, key `witness.coefficients`, in
`topics/padua-mz-2d-20261101/evidence/exact-spectra.json`, SHA-256
`5456917afe8fea69b0a776270ef3ae79fdc33deb02d27f89648fc342f78b93de`.
All omitted coefficients are zero. Every listed triple has
`a>=0,b>=0,a+b<=29`, so `p in Pi_29`.

For this explicit polynomial the claimed exact quadratic forms are

\[
 a:=Q_{30}(p^2)=
 \frac{21630961033257675132463}{120778706923875},
\]
\[
 b:=\int_{[-1,1]^2}p^2\,dx\,dy=
 \frac{3706008529790577774590124820358984174828596}
 {4898119912995148468245072420339375},
\]
\[
 b-4a=
 \frac{197077405333321381064181772316715549492616}
 {4898119912995148468245072420339375}>0.             \tag{1}
\]

Consequently

\[
 \lambda_-(30,29)\le\frac ab=
 \frac{877232781114314098381485762010567156333995}
 {3706008529790577774590124820358984174828596}
 <\frac14,
 \qquad \eta(30,29)>\frac34.                       \tag{2}
\]

The exact producer check and actual different-agent replay passed,
including direct evaluation of the **stored** coefficient list. This is
a proved finite computer-assisted statement; required Claude
mathematical audit remains pending.

## Definitions

All integrals use unnormalized `dx dy`, mass four. `p` uses
unnormalized first-kind Chebyshev products. `lambda_-` is the least
eigenvalue of the signed-rule Gram matrix in the continuous
orthonormal Legendre basis; negative quadrature weights are allowed.
`eta=||G-I||_2`. The coefficient-list identity above is part of the
definition of this finite witness, not an asymptotic description or
an unspecified numerical eigenvector.

## Assumptions

Precisely `m=30,n=29`, the fixed node orientation/checkerboard,
interpolatory `dx dy` weights and exact coefficient artifact identity.
Exact arithmetic trusts Python integer/Fraction and the declared
computational environment. No numerical eigenvector accuracy,
positivity of weights or all-degree spectral hypothesis is assumed.

## Status by part

Overall status: **PROVED** (computer-assisted development, actual
independent exact execution complete; Claude mathematical audit pending).
The exact producer and different-agent stored-vector checks establish
(1); the analytic Rayleigh implication establishes (2). A finite
floating observation alone is not the basis of this claim.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Explicit m=30 polynomial has exact forms (1) and therefore eta>3/4 | PROVED | Exact producer and independent stored-vector evaluations passed |

Candidate / claim disposition: **REJECTED: refuted** for the proposed
uniform `eta(m,m-1)<=3/4` transfer. This disposition concerns that
specific threshold claim; `eta<1` and universal positivity are not
refuted.
Rejection reason: refuted at the single admissible parameter `m=30`,
using an explicit polynomial of total degree at most 29, with actual
different-agent exact verification.

## Negative-result scope (PD-N only)

Attempted mechanism: IDEA?mz2d-codex-02, the suggested uniform
three-quarter MZ threshold for the signed Lebesgue Padua rules in the
window `n=m-1`. The closest local predecessor is PD-N004/IDEA-068,
the separate one-dimensional CC eta-threshold refutation. This is a
two-dimensional finite variant; it does not claim a new generic
Rayleigh-witness mechanism.

Parameter range: a single explicit `m=30,n=29` refutes the threshold
claimed for all `m>=2`. The result does not classify all other `m`,
does not refute `eta<1`, and does not rule out positive lower
eigenvalues, convergence to one or endpoint logarithmic laws.

## Depends on

PD-T?mz2d-codex-01 exact aliases and rational Gram pencil, plus the
finite-dimensional symmetric Rayleigh principle. It does **not**
depend on proving all eight intervals in PD-T?mz2d-codex-02: direct
evaluation of this fixed polynomial suffices.

## Checks

Producer code and receipt:

- `tracks/mz-constants/code/mz2d_exact.py`, SHA-256
  `5d1f005e2307d3a26badc9c1a44ce313dc9126625a49fba5d59430c151cf9c70`.
- `topics/padua-mz-2d-20261101/evidence/exact-spectra.json`, SHA-256
  `5456917afe8fea69b0a776270ef3ae79fdc33deb02d27f89648fc342f78b93de`,
  31,822 bytes; the m=30 witness object stores the triples and exact
  reduced forms.
- Definitions content hash at producer execution:
  `4ac0e391859a14e4d6f752f1244df0701e99d9b3d8ab8570bd632520f517c7db`.

The exact worker reported the executed command:

```sh
PYTHONPATH=/tmp/padua-flint OPENBLAS_NUM_THREADS=1 python tracks/mz-constants/code/mz2d_exact.py --m 10 20 30 40 --output topics/padua-mz-2d-20261101/evidence/exact-spectra.json
```

Python 3.12.14, python-flint 0.9.0, NumPy 2.3.5, SciPy 1.17.0.
Numerical eigenvectors select a candidate only; the final vector has
integer coefficients and the two quadratic forms are evaluated with
exact rational arithmetic by `exact_witness`. `b>0` and `4a<b` are
exact acceptance assertions. Python optimization `-O` must not be
used. This mathematical writer inspected the checker and producer
receipt; the separate exact execution below belongs to its named worker.

An independent rerun may select a slightly different rounded vector
if numerical eigensolvers differ; that still proves existence if its
own exact test succeeds, but does not by itself verify the particular
stored-polynomial equalities in (1). The actual independent replay did read these stored triples and directly
evaluated `z^TQz`, `z^THz`, matching all stored rational forms.

Independent worker: Codex `/root/protocol`, requested `gpt-6.1-sol`
medium technical effort; the producer code was frozen at the hash
above, committed at `e59f57c`, and execution began from input head
`0b526915eed8fba9a5d5509d6ec62e763a9a7983`. The orchestrator committed
completed replay artifacts at `df44db4`. The dated receipt is
`topics/padua-mz-2d-20261101/independent-checks.md`.

Actually executed, exit 0:

```sh
PYTHONPATH=/tmp/padua-flint OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python tracks/mz-constants/code/mz2d_exact.py --m 10 20 30 40 --output topics/padua-mz-2d-20261101/evidence/independent-exact-spectra.json
PYTHONPATH=/tmp/padua-flint OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python tracks/mz-constants/code/mz2d_independent_check.py
```

Independent source/receipt hashes verified by this mathematical writer:

- `mz2d_independent_check.py`:
  `5e455d747dc5dca84c883ed900095ff4a2bb40767f4ebcb3261d7d583df7bdfc`.
- `evidence/independent-exact-spectra.json`:
  `18c8623442664aa119d3581b701d200315d454071d6b8f6c89cbaf540fe34d9c`.
- `evidence/independent-additional-checks.json`:
  `2da16fa5c8f2f480ab7c12270b8c9b95ec49028f9df6b1cf4062af4f11897717`.

The additional checker uses a separately written mode-reflection
implementation and explicit Fraction double sums over the stored 225
triples; exact `a,b,b-4a,a/b` all match (1)--(2). It checks the list has
225 unique admissible integer terms and rejects a one-integer
coefficient corruption with unchanged advertised forms. SymPy 1.14.0
supports the separate small-degree nodal regressions; the stored
witness verification itself uses Python integers/Fraction.

## Sources

Local PD-N004, IDEA-068 and their M2 candidate record are the closest
eta-threshold predecessor. The underlying An--Wu application is a
conditional theorem in a one-dimensional positive-rule setting; this
signed-Padua witness does not refute that conditional theorem. Primary
Padua/CC literature attribution remains the separate campaign worker's
task. No historical novelty claim is made.

## Proof or evidence

By the exact moment formula in PD-T?mz2d-codex-01, all entries of the
Chebyshev continuous mass `H` and quadrature mass `Q` on `Pi_29` are
rational and are obtained by the four product-to-sum moments with
multiplicities. Insert the explicitly stored integer vector `z`.
Exact finite summation gives `a=z^TQz`, `b=z^THz`, and the positive
rational difference in (1), as recorded by the producer. `b>0` also
shows `p` is nonzero.

For an orthonormal Legendre expansion of the same polynomial, the
continuous squared coefficient norm is `b` and the discrete quadratic
form is `a`. The Rayleigh principle for the real symmetric Gram
matrix therefore gives `lambda_min<=a/b`. The exact inequality
`b-4a>0` yields `a/b<1/4`. Finally

\[
 \eta=\max\{1-\lambda_-,\lambda_+-1\}
 \ge1-\lambda_->3/4.
\]

No positivity assumption on the quadrature form is used in these
inequalities. The claimed finite refutation follows from this analytic implication
and the completed producer and independent exact evaluations. ∎

## Scope

This is an explicit finite negative result about the threshold
`eta<=3/4`. It supplies neither a sign failure nor a counterexample
to `eta<1`. The separate finite enclosure record places both extreme
eigenvalues in `(0,2)` at m=30, consistently with
the present threshold refutation.

## Open items

- Different-agent exact replay and stored-vector evaluation are complete;
  their commands, hashes and actual outcomes are integrated above.
- Required Claude mathematical audit remains pending independently
  of computational replay.
- All general endpoint/upper/lower claims retain their own OPEN
  status and must not inherit a finite-sample conclusion.

## History

2026-11-01, exact producer `/root/exact_engine`, Codex requested
`gpt-6.1-sol` medium technical effort, found and exactly checked the
225-term integer witness only after D1 structural PASS. At the
orchestrator's request `/root/d1_aliasing`, Codex requested
`gpt-6.1-sol` xhigh, wrote this scoped negative record and the
analytic Rayleigh reduction. Resolved runtime model/effort metadata
not exposed. Independent replay remains explicitly PENDING at
creation; this record does not claim a run by its mathematical writer.

2026-11-01, actual independent producer and stored-vector replays
completed. Writer verified the code/evidence hashes and updated the
finite negative statement from CONDITIONAL to PROVED. The scoped
uniform `eta<=3/4` applicability claim is REJECTED: refuted; required
Claude mathematical audit remains PENDING.
