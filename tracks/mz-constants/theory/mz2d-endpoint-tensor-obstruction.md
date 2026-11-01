# PD-N?mz2d-codex-20 — Two critical coordinate packets do not tensorize at total degree m-1

ID kind: PD-N.
Aliases: naive product log-four witness; critical-mesh degree obstruction.
Split from: IDEA?mz2d-codex-21.
Split into: none.

## Statement

For m>=3, the nonzero harmonic witness `p_m` of PD-T018 has degree
exactly m-1. The corresponding critical witness for the y mesh m+1,
`p_(m+1)`, has degree exactly m. Their product therefore has total
degree 2m-1 and does not belong to `Pi_(m-1)`.

More generally, products whose factors both have degree at most a fixed
ratio below the actual x/y meshes cannot obtain two critical logarithmic
losses from the **tensor-CC** norm. Precisely, for every 0<epsilon<1,
m>=2, and nonzero real polynomials f,g with

\[
 \deg f\le(1-\epsilon)m,\qquad
 \deg g\le(1-\epsilon)(m+1),
\]

the actual tensor control satisfies

\[
 \frac{(C_m\otimes C_{m+1})(f^2g^2)}
 {\int f^2\,\int g^2}\ge\frac{\epsilon^4}{C_*^2}>0,
 \qquad C_*=12(1+\pi)^4(1+2/\pi).                         \tag{1}
\]

## Definitions and assumptions

The exact harmonic witness for N>=3 is

\[
 p_N=\sum_{j=1}^{M_N}
 \frac{U_{N-1-2j}-(1-2j/N)U_{N-1}}j,\qquad
 M_N=\lfloor(N-1)/2\rfloor.
\]

All degrees are algebraic degrees in their stated coordinates; a product
has total degree equal to the sum. The tensor control in (1) is the
positive full-grid rule from the campaign definitions. It is different
from the signed Padua rule.

## Status and disposition

Overall status: **PROVED**, analytic; audit pending.
IDEA?mz2d-codex-21 is **REJECTED: failed** only as a direct multiplication
of the two known critical CC witnesses, or as an inference of two critical
losses from their fixed-ratio tensor factors. This is not a refutation of
a Padua log-four endpoint law or of all separable polynomial trials.

## Negative-result scope

Attempted mechanism: multiply two independently critical univariate
quotients while retaining the total-degree cutoff. Scope: the exact
PD-T018 witnesses on meshes m,m+1; and the fixed-ratio tensor assertion
(1). Signed Padua cancellation beyond the tensor control is not excluded.

## Depends on

PD-T018, witness definition only; PD-T023, its proved all-N fixed-ratio
CC lower bound. No A1/A2 or floating dependency.

## Proof

The coefficient of the top U polynomial in p_N is

\[
 -\sum_{j=1}^{M_N}\frac{1-2j/N}{j}.
\]

It is strictly negative because every summand is positive: `2j<N` for
this range. All other U terms have smaller degree. Since `U_(N-1)`
has nonzero leading coefficient, the degree is exactly N-1.
The two leading monomials multiply with a nonzero coefficient, so
`deg_total[p_m(x)p_(m+1)(y)]=(m-1)+m=2m-1>m-1`.
In particular retaining a critical x factor of degree m-1 leaves only a
constant y factor under the cutoff.

For (1), PD-T023 gives separately

\[
 C_m(f^2)\ge\epsilon^2\|f\|_2^2/C_*,\qquad
 C_{m+1}(g^2)\ge\epsilon^2\|g\|_2^2/C_*.
\]

The tensor sum and the continuous integral both factor exactly for a
separated product. Multiplying gives (1). Balanced allocations, such as
both degrees at most three quarters of the respective actual mesh,
therefore have a uniform tensor-control lower bound, regardless of
whether their coefficients were borrowed from a smaller-grid critical
construction. ∎

## Checks, sources and scope

Entirely analytic; no experiment supplies the degree test or (1).
Closest predecessors are IDEA-066/072. No historical novelty claim.
The signed Padua norm of a product does not generally factor, so (1)
must not be quoted as a Padua lower theorem. A surviving product route
would have to prove an additional signed cancellation estimate.

## Open items and history

Universal Padua positivity and endpoint order remain PD-T028 OPEN.
2026-11-01, Codex D3, requested gpt-6.1-sol xhigh, rules
`806cc7b4509fd93bae652f9545d32d95529f8281`. First bounded round;
degree test performed before any norm calculation.
