# PD-T111 — Exact signed Lebesgue weights at the Padua node corners

Provisional alias: `PD-T?mz2d-codex-20`. Final ID assigned at PR preparation, 2026-11-01; required Claude audit PENDING.

ID kind: PD-T.
Aliases: harmonic corner-weight formula; two negative node corners;
logarithmic corner mass.
Split from: supporting signed-form analysis for PD-T028, not a proved
conjunct of its lower-spectrum or endpoint-order targets.
Split into: the failed continuous-metric subtraction mechanism is recorded
separately in [PD-N048](mz2d-lower-corner-subtraction-obstruction.md).

## Statement

Use the fixed even-checkerboard Padua rule `Q_m` for unnormalized `dx dy`,
with `m>=2`. Put

\[
 r=\lfloor m/2\rfloor,\qquad N=2r+1,\qquad
 S_r=\sum_{i=1}^r\frac1{2i-1},\qquad
 A_r=\frac8{N(N+1)}-\frac{16S_r}{N^2-1}.
\]

The two corners belonging to the Padua set are

\[
 \mathcal C_m=\begin{cases}
 \{(1,1),(-1,1)\},&m\text{ even},\\
 \{(1,1),(1,-1)\},&m\text{ odd}.
 \end{cases}
\]

Their interpolatory **Lebesgue** weights are equal, and for every
`c in C_m` satisfy

\[
 w_c=\frac{A_r-2h_m}{2m(m+1)},\qquad
 h_m=\begin{cases}2/(1-m^2),&m\text{ even},\\0,&m\text{ odd}.
 \end{cases}                                                   \tag{1}
\]

They vanish at `m=2` and are strictly negative for every `m>=3`.
Uniformly over the two parities,

\[
 w_c=-\frac{4\log m+O(1)}{m^4}\quad(m\longrightarrow\infty).
                                                               \tag{2}
\]

## Definitions and assumptions

The support, degree, signed interpolatory weights and moments `h_a` are
those of [definitions.md](../../../topics/padua-mz-2d-20261101/definitions.md).
In particular these weights are different from the positive product-
Chebyshev weights `rho_B` in the cardinal formula.
All arithmetic is exact real arithmetic. No weight sign at any noncorner
node is assumed or classified.

## Status by part

Overall status: **PROVED** (written analytic proof; required independent
and Claude audits pending).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Exact formula (1), equality of the node-corner weights | PROVED | Accepted cardinal identity and finite partial fractions |
| Vanishing at m=2 and negativity for all m>=3 | PROVED | Explicit rational inequalities below |
| Asymptotic (2) over both parities | PROVED | Elementary harmonic asymptotic |

Candidate disposition: retained supporting result from
IDEA-217; no historical novelty claim. The signed lower-spectrum
and matching-order targets PD-T028 remain OPEN.

## Depends on

**PD-T101**, accepted cardinal normalization, specifically

\[
 L_B(z)=\rho_B\left[
   \sum_{a+b\le m}c_ac_bT_a(z_1)T_a(B_1)T_b(z_2)T_b(B_2)
   -T_m(z_1)T_m(B_1)\right],
\]

where `c_0=1`, `c_a=2` for `a>0`, and
`rho_B=2 epsilon_j eta_k/[m(m+1)]`. At any node corner,
`rho_B=1/[2m(m+1)]`. This identity is locally proved in PD-T101, rather
than inherited from a literature quotation. No A2 statement is a proof
dependency; its pinned records were read only for the gate.

## Proof

Integrating the cardinal identity gives the Lebesgue cubature weight.
Only even a,b survive. At every corner their Chebyshev values are one.
The exceptional term integrates to `2h_m T_m(B_1)`, equal to `2h_m`:
for even m its corner value is one, and for odd m `h_m=0`.
Thus

\[
 w_c=\rho_c\left[\sum_{i+j\le r}t_it_j-2h_m\right],\quad
 t_0=2,\qquad t_i=-\frac4{4i^2-1}\ (i\ge1).                 \tag{3}
\]

The sum of the first q+1 coefficients telescopes:

\[
 \sum_{j=0}^q t_j=\frac2{2q+1}.
\]

Writing `N=2r+1`, the triangular sum in (3) therefore equals

\[
 \sum_{i=0}^r t_i\frac2{2(r-i)+1}
 =\frac4N-8\sum_{i=1}^r
 \frac1{(2i-1)(2i+1)(N-2i)}.                              \tag{4}
\]

The partial-fraction identity

\[
 \frac1{(x-1)(x+1)(N-x)}
 =\frac1{2(N-1)(x-1)}
  -\frac1{2(N+1)(x+1)}
  +\frac1{(N^2-1)(N-x)}                                  \tag{5}
\]

is checked by multiplying the denominators. In the sum with `x=2i`,
the first and third reciprocal sums both equal `S_r`, while the second
is `S_r+1/N-1`. Hence that sum is

\[
 \frac{2S_r}{N^2-1}+\frac{N-1}{2N(N+1)}.
\]

Substitution into (4) yields exactly `A_r`, proving (1).

If m is odd, `m>=3`, then `N=m`, `h_m=0` and

\[
 A_r=-\frac{16}{N^2-1}
       \left(S_r-\frac{N-1}{2N}\right)<0,
\]

because `S_r>=1` and the subtracted number is less than one half.
For even m, `N=m+1`, and the numerator in (1) is

\[
 \frac8{(m+1)(m+2)}-\frac{16S_r}{m(m+2)}
   +\frac4{(m-1)(m+1)}.                                  \tag{6}
\]

It equals zero at m=2. For even m>2, replace `S_r` by its lower bound
one. The strict comparison

\[
 \frac{16}{m(m+2)}>
 \frac8{(m+1)(m+2)}+\frac4{(m-1)(m+1)}
\]

follows after multiplication by the positive common denominator from
`16(m^2-1)>12m^2`, which is precisely `m>2`. Thus (6) is negative.

Finally `S_r=H_(2r)-H_r/2=(1/2)log m+O(1)` by integral comparison
for harmonic numbers. Since `N=m+O(1)`, the triangular numerator is
`-8log(m)/m^2+O(m^-2)`; the exceptional correction is `O(m^-2)`.
Divide by `2m(m+1)` to obtain (2). This proves every claim. ∎

## Checks and sources

This is an analytic theorem without a finite-check dependency. The exact
engine was asked for an independent rational finite-sum regression; that
request is not recorded as an executed check until its receipt arrives.
No external corner-weight theorem or exhaustive-priority claim is used.

## Scope and open items

There are at least two strictly negative weights for each m>=3. The proof
does **not** establish that all other weights are nonnegative, positivity
of the form on `Pi_(m-1)`, or an endpoint asymptotic of its eigenvalues.
Required audit remains pending.

## History

2026-11-01, Codex D3 developer, requested gpt-6.1-sol xhigh. Rules SHA
`806cc7b4509fd93bae652f9545d32d95529f8281`. Derived after D1 PASS in
round2, following the complete documented gate. No A2 audit-pending
claim was promoted or used.
