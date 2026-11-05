# PD-N?mz2d-frontier-codex-14 — an admissible odd-node carrier has unbounded upper Padua quotient

ID kind: PD-N.
Aliases: sine-product upper countersequence; odd-odd logarithmic energy;
failure of the universal signed Padua upper threshold.
Split from: IDEA?mz2d-frontier-codex-16 and the PD-T110 upper target.
Split into: the common weight lemma is PD-T?...-12, the negative carrier
is PD-N?...-13. This is a separate upper countersequence.

## Statement

Fix a,b>0 with 2a+b<1/2. Let m tend to infinity through even integers,
put `r=floor(a*m)`, `s=floor(b*m)`, and let F_r be exactly the degree-r
Fejer polynomial in PD-N?mz2d-frontier-codex-13 equation (1), with
endpoint value r+1. Define

\[
 p^+_m(x,y)=\frac12
 \{T_{m/2-r}(x)-T_{m/2+r}(x)\}F_r(x)F_s(y).           \tag{1}
\]

For all sufficiently large even m this is a nonzero polynomial of
total degree `m/2+2r+s<=m−1`. Its actual signed Padua energy satisfies

\[
 \lim_{\substack{m\to\infty\\2\mid m}}
 \frac{Q_m((p^+_m)^2)}{\log m}=\frac{8ab}{9}>0,         \tag{2}
\]

and its continuous squared norm is at most `C_0²`, with
`C_0=(1+pi^4)/2`. Consequently

\[
 \lambda_+(m,m-1)\longrightarrow+\infty
 \quad\hbox{along the even integers}.                 \tag{3}
\]

The universal upper threshold `lambda_+(m,m−1)<2 for every m>=2` is
therefore false. No explicit finite crossing or threshold is asserted.

## Definitions

All signed rule, measure and total-degree conventions are the frozen
Padua definitions. Let `theta_j=j*pi/m`, `phi_k=k*pi/(m+1)`.
At x=cos t, the first factor in (1) equals

\[
 \sin(mt/2)\sin(rt),                                 \tag{4}
\]

by the cosine-difference identity. This *product* is a polynomial in x;
no lone sine factor is being treated as a polynomial.

## Assumptions

a,b>0 fixed, 2a+b<1/2, even m tending to infinity. Then a<1/4,
r<m/2, 4r<m and 2s<m+1 eventually. Restrict to sufficiently large m
so r,s>=1 and the degree fits m−1.

## Status by part

Overall status: **PROVED** (analytic development; independent reconstruction complete; Claude audit-01 accepted).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Polynomiality, degree, bounded norm and positive limit (2) | PROVED | Exact sine-product and finite DCT |
| Upper threshold failure and unbounded upper quotients (3) | PROVED | Variational implication |

Candidate / claim disposition: the universal PD-T110 upper threshold
is **REJECTED: refuted** by this analytic sequence. The packet mechanism
is retained; the discarded pointwise and coefficient-sign mechanisms
are not being revived.

## Negative-result scope

Refuted statement: the endpoint upper threshold below two for the
actual signed Lebesgue Padua rule for every integer m>=2. The divergence
is along even m; no odd-m classification, smallest crossing or sharp
extremal coefficient is claimed. A positive Chebyshev cubature or the
tensor-CC control is a different rule.

For fixed theta>1/2, choose a=b=(theta−1/2)/4; then
`1/2+2a+b<theta`. The same construction belongs to
Pi_floor(theta*m) eventually. The complete ratio classification is
recorded in the separate F3 synthesis.

## Depends on

PD-T?mz2d-frontier-codex-12: fixed-node weight asymptotic and global
majorant. PD-N?mz2d-frontier-codex-13 supplies only the Fejer definition,
elementary bounded-norm proof and finite DCT conventions (not its negative
spectral conclusion). All necessary new coefficient calculations are
written below.

[Claude audit-01](../audit-01.md) accepted the mathematics at its stated scope; [response-01](../response-01.md) addresses the editorial findings. Supplementary reconstruction is recorded in [independent-checks-math.md](../independent-checks-math.md).

## Checks

Rules/input `83cf6f1ee244f2e72057332a7ec04ee74db1f0de`. No mathematical
program was executed by this developer. The separate numerical worker
reported positive growing carrier quotients through m2000 for other
parameters; those finite measurements are not used as proof. Completed independent full-file checks and hashes are in
independent-checks-math.md; Claude audit-01 accepted, with the editorial
response recorded in response-01.md.

## Sources

Complete gate, exact failed/deferred predecessors and candidate record:
../ideas-f12.md. This construction retains sign and restricted values;
PD-N045/046's failed scalar Z-matrix and nodal majorant hypotheses are
unneeded. No external theorem or historical priority claim.

## Proof or evidence

### Admissibility and bounded norm

Equation (4) proves the stated sample carrier identity. The highest
Chebyshev degree in (1) is m/2+r, multiplied by degree-r and degree-s
factors with nonzero leading coefficients. Thus total degree is exactly
m/2+2r+s, which is at most m−1 eventually since 2a+b<1/2. For r>=1
the two Chebyshev terms are distinct and the polynomial is nonzero.

The absolute value of the sine product in (4) is at most one.
The Fejer bound and product integration in -13 equations (5)–(6)
therefore give `0<||p^+_m||_2²<=C_0²`.

### Exact x-parity energy

At the x nodes, `sin(m*theta_j/2)=sin(j*pi/2)`, so (1) vanishes
for every even j. Define the nonnegative polynomial

\[
 h_r(\cos t)=\sin^2(rt)F_r(\cos t)^2
 =\frac12(1-T_{2r}(\cos t))F_r(\cos t)^2.
\]

It has degree 4r<m eventually. Write D_r for the exact constant
coefficient of F_r² from -13 equation (8). The coefficient of T_(2r)
in F_r² is exactly `2/(r+1)²`: it arises only from the squared top
term `[2T_r/(r+1)]²`. Product-to-sum then gives the constant coefficient
of h_r:

\[
 c_0(h_r)=\frac12D_r-\frac14\frac{2}{(r+1)^2}.         \tag{5}
\]

The finite DCT identities apply to h_r because 4r<m. Its ordinary
endpoint-halfweighted sum is `m c_0(h_r)`, and its alternating sum
is zero. Hence with

\[
 U^+_{m,j}=\sin^2(j\pi/2)\sin^2(r\theta_j)
                  \left(\frac{F_r(\cos\theta_j)}m\right)^2,
\]

we obtain exactly

\[
 \sum_j\epsilon_j U^+_{m,j}
 =\frac{c_0(h_r)}{2m}\longrightarrow\frac a6,
 \qquad U^+_{m,j}=0\quad(j\text{ even}).              \tag{6}
\]

The y energy is unchanged from -13:

\[
 V_{m,k}=\left(\frac{F_s(\cos\phi_k)}m\right)^2,
\quad
 \sum_k\eta_kV_{m,k}\to\frac{2b}3,
\quad
 \sum_k\eta_k(-1)^kV_{m,k}=0.                        \tag{7}
\]

### Limit of the complete signed sum

The profiles have pointwise limits

\[
 U^+_{m,j}\to u_j^+
 =\sin^2(j\pi/2)\sin^2(a\pi j)f_a(j)^2,
 \qquad V_{m,k}\to v_k=f_b(k)^2,
\]

where f_a,f_b are the explicit functions in -13 equation (10).
Every carrier factor has absolute value at most one. Thus the same
whole-grid domination from -13 equations (11)–(14) applies, using the
global weight theorem -12. It justifies both the profile sums in
(6)–(7) and dominated convergence in

\[
 \frac{Q_m((p^+_m)^2)}{\log m}
 =\sum_{j+k\ {\rm even}}
 \frac{m^4w^{(m)}_{j,k}}{\log m}\,U^+_{m,j}V_{m,k}.
\]

Only odd j survive; the checkerboard then retains odd k. The leading
weight in -12 is positive there, equal to `+16e_je_k`. Equations
(6)–(7) therefore give

\[
 \lim\frac{Q_m((p^+_m)^2)}{\log m}
 =16\left(\sum_{j\ {\rm odd}}e_ju_j^+\right)
      \left(\sum_{k\ {\rm odd}}e_kv_k\right)
 =16\frac a6\frac b3=\frac{8ab}{9}.
\]

This proves (2). Finally, for any fixed `0<c<8ab/(9C_0²)`, the
Rayleigh quotient of this nonzero admitted polynomial is at least
`c log m` for all sufficiently large even m. The variational principle
proves (3), and hence eventual violation of the upper threshold two. ∎

## Scope

The upper claim fails for the actual signed polynomial form. This is
not the divergence of a sufficient absolute-weight majorant. It proves
existence of arbitrarily large violations without naming the first
violating m. Finite scans below two remain valid in their finite scope.

These explicit carriers prove existence only; they are not usable finite witnesses at feasible degrees, as illustrated by the auditor’s MEASURED extrapolations ([audit-01, A2](../audit-01.md) and [carrier fits](../audit-01-support/subagent-f3/audit-diamond.md)); those extrapolations are not onset bounds and these carriers are unrelated to the m1600 float hit.

## Open items

Independent full-file reconstruction and Claude audit-01 are complete; see the references below.
An effective remainder and explicit first crossing are separate tasks.
Sharp growth constants of the true extrema and the odd-m branch remain
unresolved; the original all-m threshold is refuted.

## History

2026-11-05, Codex F1/F2 developer, requested gpt-6.1-sol xhigh; runtime
metadata unexposed. Opposite sample parity was isolated after the
negative carrier. The polynomial sine-product repair is explicit;
no nonpolynomial trial or floating crossing enters the proof. No Git.
