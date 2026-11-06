<a id="pd-tlanczos-nonproduct-codex-p3-03--non-affine-product-measures-moment-equivalent-to-sh_n-through-degree-2n1-with-an-n-dependent-weight-mode"></a>

# PD-T480 — non-affine-product measures moment-equivalent to SH_n through degree 2n+1, with an n-dependent weight mode

Provisional alias: `PD-T?lanczos-nonproduct-codex-P3-03`.

ID kind: PD-T.
Aliases: unchanged SH constants on rank-two weights; uniform eta certificate.
Split from: IDEA-576 combined target.
Split into: none. Supporting admission and moments/creators were recorded
separately as P3-01 and P3-02.

## Statement

For every n>=2 and every real eta with 0<|eta|<1, use the explicit
mu_(n,eta) of [P3-01](p3-01-high-mode-weight-admission.md), physical
operators X=S,Y=2S+T, order and fixed BJ/mirror rules of
[P3-02](p3-02-exact-moments-creators.md). In the normalized aggregate
model defined below, the first-order spectral span capacities satisfy

    kappa_BJ(n,eta)>=sqrt(2*(4^(n+1)-1)/3)>=sqrt(2)*2^n,     (1)
    0<kappa_mirror(n,eta)
      <=2*sqrt(6)*(n+1)^2*(N_n-1), N_n=(n+1)(n+2)/2.         (2)

Consequently

    kappa_BJ/kappa_mirror
      >=2^n/[2*sqrt(3)*(n+1)^2*(N_n-1)].                     (3)

Thus one fixed nonzero eta in this interval gives an all-degree family
of non-affine-product measures with an exponential BJ lower and a
polynomial full-source mirror upper. The constants are the original
PD-T324 constants, with no density-comparison loss. A sufficient uniform
radius certificate is eta_0(n)=1/2 for every n>=2; the larger open range
0<|eta|<1 is also proved. This certificate preserves (1)–(3), rather than
asserting strict BJ>mirror at every small degree or a maximal radius.

## Definitions

Represent a function p by (sqrt(w_eta,kl)*p(z_kl))_kl. Start from the
exact q_00 and leave it unperturbed. At each subsequent column h form

    raw_h(epsilon)=A_h q_parent(h)(epsilon)+epsilon*f_h,

project exactly against all earlier perturbed columns and normalize with
positive residual norm. Sources f_h are arbitrary Euclidean M-vectors.
Let sigma_h=||A_h q_parent(h)(0)||_2 for the chosen rule and define

    ||f||_src^2=sum_(h!=00) ||f_h||_2^2/sigma_h^2.

Let P_n^eta be the exact orthogonal projector onto represented Pi_n and
P_n^eta(epsilon;f) the computed-column projector. The capacity is

    kappa_R=sup_(||f||src=1) lim_(epsilon->0+)
      ||(I-P_n^eta)P_n^eta(epsilon;f)||_2/epsilon.

Output norm is spectral. The source domain contains every column through
n for either rule, with each rule's own relative raw-product scales.

## Assumptions

n finite, n>=2, 0<|eta|<1; exact real operators, full exact projection,
positive normalization, fixed prescribed parents, exact start, and fixed
f when taking epsilon to zero. No scalar-operation or IEEE model is used.

## Status by part

Overall status: PROVED (analytic; accepted at stated scope in [audit 01](../audit-01.md)).

| Mathematical part | Status | Evidence |
|---|---|---|
| Normalized source/quotient application | PROVED | Exact differentiated recurrence below |
| BJ normal lower and all-source mirror upper | PROVED | Preserved unit normal witness and explicit U solutions |
| Degree-uniform sufficient eta range and n 2–10 certificate | PROVED | Bounds hold throughout 0<|eta|<1 |

Candidate disposition: retained successful weight variant. N2 measured
growth screen remains UNRUN/INCONCLUSIVE and is not promoted by this proof.

## Depends on

[P3-01](p3-01-high-mode-weight-admission.md) and
[P3-02](p3-02-exact-moments-creators.md). PD-T324's frozen-response
identities are extended to these weights explicitly below. P4's
[weighted quotient](p4-weighted-normal-quotient.md) and
[moment-preserving transfer](p4-moment-capacity-transfer.md) provide
the common framework and a separate, weaker comparison route; no equality
of projectors, or generic equality of finite capacities, is assumed.

## Checks

Written analytic proof only. No new numerical, symbolic or exact scan is a
premise; no N2 execution is reported. Distinct independent mathematical
review of this proof and its dependencies was accepted in
[audit 01](../audit-01.md), which also records the auditor's separate
finite algebraic checks and their exact scope.

## Sources

PD-T324 and P4 records above; all were read in full. No new external
literature theorem or historical-priority assertion.

## Proof or evidence

### Normalized quotient and source factors

Write c_hl for the exact coefficients in the normalized creator relation

    beta_h q_h=A_h q_parent-sum_(l<h)c_hl q_l, beta_h=1/2.

P3-02 proves these coefficients and sigma_h are independent of eta.
At each fixed n,eta,f, positive base pivots imply smooth full projection
and normalization in a neighborhood of zero. Let V_00=0 and define the
frozen responses by

    beta_h V_h=A_h V_parent-sum_(l<h)c_hl V_l+f_h.           (4)

Differentiate the perturbed normalized relation. In addition to the
terms on the right of (4) it contains only
-sum_l dot(c_hl)q_l-dot(beta_h)q_h. Induction therefore proves
dot(q_h)-V_h belongs to represented Pi_(deg h): multiplying a parent's
polynomial error by one physical coordinate raises degree by at most one,
and every other error/base column has degree at most deg(h). With
R_n=I-P_n^eta, R_n dot Q_n=R_n[V_h]. Because Q_n(epsilon) has exactly
orthonormal columns,

    ||R_n P_n(epsilon;f)||_2
      =||R_n Q_n(epsilon;f)||_2
      =|epsilon|*||R_n[V_h]||_2+O(epsilon^2).                (5)

The first equality follows also by multiplying R_n Q_n Q_n^T by Q_n;
the remainder is only for fixed finite data and f. Hence the capacity is
exactly sup_(||f||src=1)||R_n[V_h]||_2.

For completeness the convention matches P4's monic quotient. At degree
d the represented monic column is b_h=2^(-d)q_h, of norm 2^(-d).
Its raw-product source is f_h^mon=2^(-(d-1))f_h and its source scale is
sigma_h^mon=2^(-(d-1))sigma_h. These factors cancel in the source norm.
The monic frozen response is W_h=2^(-d)V_h: inserting the scaled exact
creator coefficients into its recursion verifies this identity. Dividing
W_h by sqrt(d_h)=2^(-d) gives V_h, exactly the output in (5). This
accounts for Gram, creator and source factors; no norm-equivalence
shortcut or projector identity is used.

### A complete normal BJ witness

P3-02 proves e=q_(n+1,0)^eta is unit length and normal to Pi_n. Put
f_(n,0)=e/sqrt(2) and all other sources zero. The source scale at this
position is 1/sqrt(2), so the source budget is one. All responses before
degree n vanish. The first degree-n column has V_(n,0)=2f_(n,0).
At each next degree-n BJ column (r,j)=(n-j,j), the only earlier term of
degree n in its Y creator has coefficient 1 at (r+1,j-1); every other
term and the parent have vanishing response. Equation (4) gives

    V_(n-j,j)=-2 V_(n-j+1,j-1)=2*(-2)^j*f_(n,0).            (6)

All these columns are normal multiples of e. Their rank-one matrix has
squared spectral norm

    4*||f_(n,0)||^2*sum_(j=0)^n 4^j=2*(4^(n+1)-1)/3.

This proves (1), after the actual perturbed-weight normal projection.

### Mirror upper for every allowed aggregate source

Negative indices denote zero. P3-02's creators and (4) give

    V_rj=2S V_(r-1,j)-V_(r-2,j)+2 f_rj, r>=1,
    V_0j=2Y V_(0,j-1)-2V_(1,j-1)-V_(0,j-2)+2 f_0j.

Substitute V_(1,j-1)=2S V_(0,j-1)+2 f_(1,j-1), and use Y-2S=T.
The boundary recurrence is

    V_0j=2T V_(0,j-1)-V_(0,j-2)+2f_0j-4f_(1,j-1).

The U recurrence solves these identities, by induction, as

    V_0j=sum_(b=1)^j U_(j-b)(T)(2f_0b-4f_(1,b-1)),
    V_rj=U_r(S)V_0j+2 sum_(a=1)^r U_(r-a)(S) f_aj.         (7)

Every source used has degree <=r+j and is available in the ordered run.
The case j=0 uses the empty boundary sum. Both S and T are diagonal
with spectrum inside [-1,1], independently of the weights. The sine
formula for U, or its finite exponential sum, gives |U_a(z)|<=a+1 there.
Every individual source coefficient in (7), for r+j<=n, therefore has
operator norm at most C_n=4(n+1)^2. The possible boundary occurrences
f_(1,b-1) have second index at most j-1, whereas a direct source has
second index j, so no source coefficient has been counted twice in this
bound. The other source indices are distinct as well.

Let H=N_n-1 and u_h=f_h/sigma_h. For a source budget one,
sum||u_h||^2=1, while P3-02 gives sigma_h<=sqrt(3/2) for mirror. For
each output column the triangle inequality and Cauchy–Schwarz give

    ||V_rj||<=C_n*sqrt(3/2)*sum_h||u_h||
             <=C_n*sqrt(3H/2).

There are H nonconstant output columns. Projection is contractive, so

    ||R_n[V_h]||_2<=||[V_h]||_F
      <=C_n*sqrt(3/2)*H=2*sqrt(6)*(n+1)^2*(N_n-1).

This bounds the entire source sphere, proving (2)'s upper. Positivity
follows by injecting sigma_(0,n)*e at the last mirror column: only the
last response is nonzero and equals 2 sigma_(0,n)e. Dividing the BJ
lower by the positive mirror upper proves (3).

### Uniform radius certificate and its meaning

None of these estimates loses a factor as eta varies inside 0<|eta|<1.
Every choice 0<eta_0<1 certifies the closed sufficient range
0<|eta|<=eta_0 for all n>=2; eta_0(n)=1/2 is one such choice.
At |eta|=1 some weights vanish, so |eta|=1 lies outside the admitted positive full-support family. No endpoint claim is made.
In particular the requested finite table is an analytic certificate:

| n | Certified sufficient eta_0(n) |
|---|---|
| 2 | 1/2 |
| 3 | 1/2 |
| 4 | 1/2 |
| 5 | 1/2 |
| 6 | 1/2 |
| 7 | 1/2 |
| 8 | 1/2 |
| 9 | 1/2 |
| 10 | 1/2 |

This proves the bounded-decay sufficient-radius property with c=1/2,k=0
for preservation of the all-degree inequalities (1)–(3). It is neither
a numerical growth scan nor a computation of a maximal radius. The
conservative ratio lower in (3) is below one for 2<=n<=17 and exceeds
one for every n>=18. Thus the n=2–10 certificate preserves (1)–(3)
without proving BJ>mirror there; strict capacity ordering is certified
for n>=18 by this bound. No necessity or upper-radius theorem is
claimed by this table.

## Scope

The result concerns non-affine-product measures moment-equivalent to SH_n
through degree 2n+1, with an n-dependent weight mode. At fixed n,
mu_(n,eta) agrees with SH_n on all moments through degree 2n+1.
Consequently the Gram matrices, monic polynomial basis, creators, pivots,
source scales and frozen-response map f->V are eta-independent; only the
ambient normal projector changes in the capacity formula. Represented
weighted basis vectors themselves vary with eta. The two finite capacities
are not asserted equal to those at eta=0.

One may fix eta!=0 once for all degrees, but the weight mode
U_(n+1)(s)U_(n+1)(t) changes with n. This is the weaker variant accepted
in [AC's Q2 decision](../LOG.md#2026-11-06--claude-audit-01).
It does not prove robustness under one fixed smooth density or nonlinear
node geometry. It is a worst-case aggregate first-order statement with
degree-dependent sources. It supplies no finite-epsilon uniform remainder,
IEEE/scalar realization, every-error lower bound, closure theorem, or
comparison with every possible rule.

## Open items

The [completed Claude audit](../audit-01.md#accepted-claims-audit-scope)
accepts P3-01/02/03 at their stated scope. The n-independent perturbation
remains OPEN and [deferred to a follow-up topic](../ideas/P3.md),
not a precondition for this PR. No P3 scan is required; see
[AC's Q3 decision](../LOG.md#2026-11-06--claude-audit-01).

## History

- 2026-11-05: Codex P3, assigned gpt-6.1-sol xhigh; rules/input
  ed5515ed84e0e7b12163175dce9f22a859c89c99. Round2 after pushed
  checkpoint 6988024. Routine PD-T324 extension required no hard-step
  escalation. Gate followed initial proposal; [canonical protocol disclosure](../LOG.md#canonical-protocol-disclosure--p3-gate-timing).

- 2026-11-06: audit-response wording for A1 and MINOR 1/18; title and Scope
  carry the moment-equivalence limitation, and the radius discussion states
  the threshold and open endpoints. The theorem Statement and proof arguments
  are unchanged; the certificate discussion adds the audited clarifications.
