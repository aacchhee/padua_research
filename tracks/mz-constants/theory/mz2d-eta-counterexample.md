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

The exact producer check passed. This computer-assisted statement is
presently conditional on an independent exact replay, including direct
evaluation of the **stored** coefficient list, as specified below.

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

Overall status: **CONDITIONAL**, pending a different-agent exact replay
and direct stored-vector check. The exact producer checked (1);
the analytic implication (1) -> (2) is fully written below. A finite
floating observation alone is not the basis of this claim.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Explicit m=30 polynomial has exact forms (1) and therefore eta>3/4 | CONDITIONAL | Producer exact check passed; independent stored-vector replay pending |

Candidate / claim disposition: **REJECTED: refuted** for the proposed
uniform `eta(m,m-1)<=3/4` transfer, conditional on completing the named
computer-proof replay obligation. This disposition concerns that
specific threshold claim; `eta<1` and universal positivity are not
refuted.
Rejection reason: refuted at the single admissible parameter `m=30`,
using an explicit polynomial of total degree at most 29. Until replay
the exact refutation retains CONDITIONAL status.

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
receipt but has not independently executed that exact calculation.

An independent rerun may select a slightly different rounded vector
if numerical eigensolvers differ; that still proves existence if its
own exact test succeeds, but does not by itself verify the particular
stored-polynomial equalities in (1). Therefore the named replay
obligation also reads these stored triples and directly evaluates
`z^TQz`, `z^THz`, matching all stored rational forms.

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
inequalities. The claimed finite refutation follows once the
independent exact evaluation obligation is completed. ∎

## Scope

This is an explicit finite negative result about the threshold
`eta<=3/4`. It supplies neither a sign failure nor a counterexample
to `eta<1`. The separate finite enclosure record places both extreme
eigenvalues in `(0,2)` at m=30 after its replay, consistently with
the present threshold refutation.

## Open items

- Different-agent exact replay, including direct evaluation of the
  stored polynomial and equality with (1); record source, artifact
  hashes, environment, command and actual result.
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
