# PD-T?padua-3d-codex-T6-01 — universal cube Lebesgue lower bound

ID kind: PD-T.
Aliases: explicit total-degree projection lower bound; corrected cosine
averaging; factor27 transfer.
Split from: none. Split into: none (field correction 2026-11-06, audit m9).
Source task: T6 universal Lebesgue lower bound.
Supporting dependency: PD-T?padua-3d-codex-T6-02, explicit Fourier estimate
[t6-fourier-lower-bound](t6-fourier-lower-bound.md); this is not a conjunct
split from the universal interpolation statement.

## Statement

Let `d>=1,n>=0` be integers. Let `P:C([-1,1]^d;R)->Pi_n^d` be any bounded
linear projection, where `Pi_n^d` is the real polynomial space of **total**
degree at most n. Then

\[
\|P\|\ge3^{-d}\|D_n^d\|_{L^1(\mu)}.\tag{1}
\]

Here `D_n^d=sum_{|k|_1<=n}exp(i k.t)` and mu is probability Haar measure
on the d-torus. Consequently, for every integer `n>=2` and every
`Pi_n^3`-unisolvent set `X subset [-1,1]^3` of `binom(n+3,3)` points,
its uniform Lebesgue constant satisfies

\[
\boxed{\displaystyle
\Lambda(X)\ge\max\left\{1,
 {H_{\lfloor n/2\rfloor}^{\,3}\over648\pi^3}\right\}
 \ge {\log^3(\lfloor n/2\rfloor+1)\over648\pi^3}.}
\tag{2}
\]

Thus every such family has a universal `c log^3 n` lower bound. This is an
explicit, coarse, known-mechanism result; historical novelty is not claimed.

For `d>=3,n>=d-1`, the same proof gives
`||P|| >= H_floor(n/(d-1))^d / (d*(6*pi)^d)`.

## Definitions

All operator norms are uniform norm to uniform norm. Projection means
range contained in Pi_n^d and `Pp=p` for all p in that space. For a
unisolvent set, `I_X f=sum_{x in X}f(x)ell_x`, and
`Lambda(X)=sup_z sum_x |ell_x(z)|=||I_X||`.

Let `T^d=(R/(2*pi*Z))^d`, `mu=(2*pi)^(-d)dt`, and
`e_k(theta)=exp(i k.theta)`. `s(k)` is the number of nonzero coordinates
of k. Fourier coefficients use the negative sign in the integral.

## Assumptions

No positive cubature, orthogonality of nodes, grid structure or separation
assumption. The real Banach-space convention avoids an unrecorded norm
loss from complexifying an arbitrary real operator.

## Status by part

Overall status: PROVED (complete developer proof, independent audit pending).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Every-projection comparison (1) | PROVED | Explicit corrected averaging below |
| Universal interpolation inequality (2) | PROVED | (1), split Fourier theorem and norm identity |

Candidate/claim disposition: retained known-mechanism explicit bound.
Rejection reason: none. No new Padua construction is inferred.

## Depends on

PD-T?padua-3d-codex-T6-02 for the Fourier lower estimate in (2).
The projection comparison (1) is proved independently below. No source
theorem is imported as a premise.

## Checks

Developer command:
`python topics/padua-3d-20261106/code/t6_sanity.py`.
Receipt: `evidence/t6-sanity.json`. Exact finite multiplier/support checks
and floating grid averages are sanity checks, not the universal proof.
Independent check: pending; coordinator will attach its separate record.

## Sources

[literature-T6](../literature-T6.md) records Subbotin1983 Theorem 1 and
Corollaries 1,3 (provisional LIT?padua-3d-codex-T6-02) as LITERATURE for
this same comparison and universal logarithmic order; its primary
fulltext was read. DEKL2017 Theorem2.3 supplies a precise Fourier match.
The source results are context, not premises of the local proof below.
The original Padua generating-curve introduction states its
displayed multidimensional lower bound in the tensor-product setting;
that passage is not used to assert the universal total-degree theorem.
IDEA-206's leading-constant obstruction is respected: neither (1) nor (2)
approaches a sharp interpolation coefficient.

## Proof or evidence

**1. Cosine lift and its exact total-degree range.** Define
`Jf(theta)=f(cos theta_1,...,cos theta_d)`. It is an isometric bijection
from real cube-continuous functions to continuous torus functions even
in each coordinate. To see surjectivity, restrict an even torus function
to `[0,pi]^d` and compose with coordinatewise arccos; periodicity and
evenness give agreement on all cosine fibres.

Products `product_j T_{alpha_j}(x_j)` with `alpha_j>=0,sum alpha_j<=n`
form a basis of Pi_n^d: each has a nonzero leading monomial x^alpha and
lower terms of no larger total degree. Therefore its lifted space is

\[
V_n=J\Pi_n^d=\operatorname{span}_{|\alpha|_1\le n}
 \prod_j\cos(\alpha_j\theta_j).
\tag{3}
\]

Every frequency of V_n lies in B_n^d. This assertion is about total
degree, not a rectangular tensor spectral set.

**2. Extend by reflection averaging.** On real C(T^d), let

\[
Ef(\theta)=2^{-d}\sum_{\varepsilon\in\{-1,1\}^d}
f(\varepsilon_1\theta_1,\ldots,\varepsilon_d\theta_d).
\]

E is contractive and has range equal to J's range. Thus
`Q=JPJ^{-1}E` is a bounded real operator into V_n with `||Q||<=||P||`.
It fixes V_n. All maps remain real; complex characters below are only
used to compute the algebraic multipliers of their complex-linear
extensions. No complexified norm estimate is invoked.

**3. Calculate translation averaging rather than assuming invariance.**
Write `tau_u f(theta)=f(theta+u)` and define the real operator

\[
Rf=\int_{\mathbb T^d}\tau_{-u}Q\tau_u f\,d\mu(u).
\tag{4}
\]

For each continuous f the integrand is continuous in u in uniform norm,
so this Banach-valued integral exists. Translations are isometries,
and `||R||<=||Q||<=||P||` on the real space.

For a character e_k, translation conjugation retains exactly the
coefficient at frequency k in Qe_k. Indeed, if
`Qe_k=sum_{ell in B_n^d}c_{ell,k}e_ell`, its conjugate in (4) is
`sum c_{ell,k}exp(i(k-ell).u)e_ell`; integration removes every ell!=k.
For k outside B_n^d this coefficient is absent, so Re_k=0. For k inside,

\[
Ee_k=\prod_j\cos(k_j\theta_j)\in V_n,
\qquad Qe_k=Ee_k,
\qquad Re_k=2^{-s(k)}e_k.
\tag{5}
\]

Thus R itself is generally **not** the full Fourier projection. Equation
(5) gives the exact loss at zero-coordinate strata as well as in the
interior.

**4. Correct the multiplier with bounded real operators.** Let C_j be
integration in coordinate j against probability Haar measure, leaving
the other coordinates fixed. `||C_j||=1`, and its multiplier on e_k is
1 if k_j=0 and 0 otherwise. Therefore

\[
M=\prod_{j=1}^d(2I-C_j),\qquad \|M\|\le3^d
\]

has multiplier `2^{s(k)}`. Equations (5) imply `MR=S_n` on all
trigonometric polynomials, where S_n is Fourier projection onto B_n^d.
Real sine/cosine polynomials are dense in real C(T^d); both sides are
bounded real operators, so `MR=S_n` on that space and

\[
\|S_n\|\le3^d\|P\|.\tag{6}
\]

**5. The Fourier operator norm is its kernel L1 norm over the reals.**
Since B_n^d is sign symmetric, D_n^d is real and even, and
`S_n f(theta)=integral D_n^d(theta-t)f(t)dmu(t)`.
The triangle inequality gives `||S_n||<=||D_n^d||_1`.
For epsilon>0 use the real continuous norm-at-most-one input
`f_epsilon(t)=D_n^d(-t)/sqrt(D_n^d(-t)^2+epsilon^2)` and evaluate
at theta=0. Dominated convergence gives the reverse inequality as
epsilon tends to0. Thus `||S_n||=||D_n^d||_1`, which with (6) proves (1).

**6. Interpolation and explicit constants.** The interpolation map I_X
is a projection as assumed. Its norm equals the usual Lebesgue constant:
the upper estimate is the triangle inequality; for any fixed z, the
finitely prescribed nodal signs `sign ell_x(z)` extend to a continuous
function of norm at most1, for example by disjoint continuous bumps at
the distinct nodes. This gives the opposite estimate after taking sup_z.
Constants are reproduced, so the norm is at least1. Now apply the split
Fourier theorem with d=3 to (1). Its denominator24*pi^3 times27 is
648*pi^3. Finally `H_m>=integral_1^(m+1) dt/t=log(m+1)` proves (2).

## Scope

This proves a universal obstruction to sub-logarithmic-cubed quality for
3-D total-degree interpolation, with no node-class restrictions. It does
not prove existence of a matching interpolation family, does not settle
T1's structured-class obstructions, and does not transfer lower bounds
merely from a tensor subspace. Sharp constants remain unresolved.

For the d2 sanity boundary, (1) holds but cannot exclude Padua: its known
log-squared growth is fully consistent with this coarse comparison.
The split explicit Fourier theorem is only asserted for d>=3.

## Open items

Independent review of the analytic proof and a separate replay of sanity
code. The T6 bounded target is achieved as a known-mechanism explicit
bound; a broader historical source survey and sharp constants are optional
future work, not prerequisites of this local proof.

## History

2026-11-06, Codex gpt-6.1-sol xhigh, rules/input
`ccd9e905d19c0c625c196c4a3f3e707058ed042a`: primary survey first, then
explicit developer proof. No registry edits, final-ID allocation or Git
operations by this worker.

Later source refinement: DEKL equation (3.15) led to Subbotin's exact
prior `3^-d` comparison and universal logarithmic bound. The local proof
is retained as a self-contained explicit certificate, with no novelty claim.

## Supplementary check addendum — 2026-11-06

[Distinct Astra high check](../independent-checks-math.md) completed
within its stated scope, including actual separate execution. Earlier
pending-check wording records the development state. Required Claude
substantive audit remains due; this addendum changes no mathematical claim.


## Completed-audit process addendum — 2026-11-06 — m5

[Claude audit-01](../audit-01.md) completed the substantive independent audit
of candidate f1a5b0936d8fb2b033c69af59a6366550f170999, including the recorded
independent executions, after the supplementary Astra checks. Its accepted
mathematical scopes supersede earlier “audit/replay/rerun pending” and
“planned, no run claimed” process descriptions where those refer to that
completed work. This addendum changes no mathematical statement or status;
MEASURED observations remain MEASURED and OPEN targets remain OPEN. The
new response dispositions/ID-kind/evidence changes require focused re-audit,
not another approval of the unchanged accepted mathematics.


## Audit-response limits and source qualification — 2026-11-06 — m6/m7/m8/m9

Sharp coefficients and matching interpolation upper bounds remain OPEN
outside this PROVED theorem; the unrelated OPEN row was moved out of its
status table. Its Fourier estimate is a supporting dependency, not a split
conjunct of the same target.

The harmonic term exceeds 1 only when H_floor(n/2)>(648π³)^(1/3)≈27.1858,
at roughly n=7.2×10¹¹ (using H_m≈log m+Euler's constant). At practical degrees
this explicit boxed inequality gives Λ≥1. Its asymptotic log³ order remains
valid and very coarse; it is not a useful finite-degree quality separator.

Subbotin's original Russian paper is 1982; 1983 is the English translation.
The attribution of comparison/order rests on the developer's recorded primary
read in ../literature-T6.md, not an independently verified source claim here.
That record read Theorem1, Corollary1 and Corollary3, whose Yudin input was
unread. Astra did not verify the attribution and Claude could not retrieve
Subbotin. The local proofs were independently accepted; they do not depend
on that unresolved source verification. Verdict for T6-01 is **literature
duplicate, retained as local reproof**. Dedicated source-index consolidation
is due only at PR preparation.

Producer t6_sanity.py's multiplier arithmetic is tautological: it multiplies
preset factors 2^(-s) and 2^s and never builds R from an actual projection P.
Its support/subset/harmonic checks remain diagnostics; no executed decisive
projection test is claimed for that producer. Audit-01 T5/T6 command6
independently tested a real interpolation projection and obtained multiplier
error 3.5e-16. The analytic argument, not either floating sanity run, proves
this theorem.
