# PD-T?lanczos-frontier-codex-L2-01 — finite first-order rule invariance and exact aggregate X-closure certificates

ID kind: PD-T.
Aliases: smooth exact-base rule quotient; nested-projector closure derivative;
worst-case closure capacity; independent-sign closure trace.
Split from: the finite reduction obligation of the saved W/R readings in
attempts/L2.md. Original working-precision PD-T055 stays OPEN.
Split into: none. Degree12 G2 outcomes require separate computation/evidence.

## Statement

Fix a finite degree n>=1, a uniform positive measure on distinct real
nodes, injectivity through degree n, fixed admissible BJ parents and
coordinates, and exactly the saved class R_smooth from attempts/L2.md.
Its members have exact starting vector and relations

    beta_hat_k q_hat_k = A_k q_hat_p + epsilon f_k
                        - sum_(l<k) c_hat_kl q_hat_l.          (1)

For each fixed source f, coefficients and normalizations are differentiable
at epsilon=0, beta_hat_k(0)>0, and every column at zero is the exact
positive-leading orthonormal graded column q_k. No parent revision,
reference injection, extra product or outside vector is permitted. No
uniform neighborhood or second derivative is assumed.

Then, for every fixed f, the first derivatives of all completed-degree
span projectors are identical for every member of R_smooth. The actual
X-closure derivative has the following rule-independent monic formula:

    D_X,s(F) = R_(s+1) [X V_s(F)-V_(s+1)(F) C_X,s] D_s^(-1/2),
                 0<=s<n,                                   (2)

where F_k=sqrt(d_p(k)) f_k and all quantities are defined below. In
particular, with the original unit source budget and X-norm normalization,

    C_n = max_(s<n) sup_(||F||_mon=1) ||D_X,s(F)||_2 / ||X||_2, (3)

so the saved infimum over R_smooth is eliminated by proof, rather than
assumed absent. The saved random-source quantity is exactly

    E_n = sum_(s<n) H_s^2 / [(N_n-1) M ||X||_2^2],            (4)

with rational H_s^2 on rational nodes. The computable endpoints below
bound C_n itself; they concern X-closure, not a span angle.

This is a finite analytic reduction. It supplies no degree12 truth value
and no all-degree growth statement. Saved G2 thresholds remain
`C_12>=256` and `E_12>=16`, separately on T24 and rotQ24.

## Definitions

N_s=(s+1)(s+2)/2. The graded monic basis and frozen recurrence are those
of PD-T136, using uniform Euclidean sums:

    b_0=1, d_k=b_k^T b_k, q_k=b_k/sqrt(d_k),
    b_k=A_k b_p-sum_(l<k) alpha_kl b_l.

B_s=[b_0,...,b_(N_s-1)], D_s=diag(d_0,...,d_(N_s-1)),
Q_s=B_s D_s^(-1/2), P_s=Q_s Q_s^T, R_s=I-P_s. Thus D_s in (2)
is the basis norm diagonal, whereas D_X,s denotes the closure derivative.
The perturbed projector P_hat_s projects onto the actual stored-column
span; orthogonality at nonzero epsilon is not required.

For the source h let

    tau_h^2=||A_h b_p(h)||_2^2,
    sigma_h^2=||A_h q_p(h)||_2^2=tau_h^2/d_p(h).

The unchanged original source norm is

    ||f||_src^2=sum_h ||f_h||_2^2/sigma_h^2
              =sum_h ||F_h||_2^2/tau_h^2=:||F||_mon^2.        (5)

All h run1,...,N_n-1, with no starting-vector source. Admissibility and
injectivity imply d_k,tau_h^2>0. Write F_h=tau_h u_h, so u has joint
Euclidean norm one.

Let g_kh(i) be the exact frozen monic responses of PD-T136, with
g_kh=0 for k<h, g_hh=1, and its stated recurrence for k>h. Put

    V_k(F)=sum_h diag(g_kh(i)) F_h,
    V_s(F)=[V_0,...,V_(N_s-1)], V_0=0.

C_X,s is the rational N_(s+1)-by-N_s coordinate expansion matrix

    (C_X,s)_lj = b_l^T X b_j/d_l,
    X B_s=B_(s+1) C_X,s.                                   (6)

This is the full exact multiplication expansion, including its top
degree, rather than an implicit computed section. Define rational responses

    omega_s,j,h(i)=x_i g_jh(i)
                   -sum_(l<N_(s+1)) (C_X,s)_lj g_lh(i),     (7)

for j<N_s and1<=h<N_(s+1). Later source columns have zero response at
this stage. Finally put

    ell_s,h,i = tau_h^2 R_(s+1),ii
                *sum_(j<N_s) omega_s,j,h(i)^2/d_j,
    L_s^2=max_(h,i) ell_s,h,i,
    H_s^2=sum_(h,i) ell_s,h,i,
    U_s^2=max_i sum_(h,j) tau_h^2 omega_s,j,h(i)^2/d_j.       (8)

All these are rational for rational nodes. The normal diagonal is
`R_(s+1),ii=1-sum_(l<N_(s+1))b_l(i)^2/d_l`. Full global source
coverage is retained even though later sources are zero columns at earlier
stages.

## Assumptions

Exactly the saved smooth exact-base class and source budgets above;
positive pivots at zero; no data or initial-column perturbation. The
sources f are fixed while epsilon tends to zero. Differentiability is
only pointwise for each fixed rule and f. Uniform finite-epsilon bounds,
actual working-precision storage, scalar-operation realizability and
arbitrary nonsmooth rules are outside this statement.

The statements dividing by ||X|| require ||X||>0; this holds on both
frozen grids. T24 has M=325 and ||X||^2=1. RotQ24 has M=625 and
||X||^2=49/25. Both have N_12=91 and the exact point/weight conventions
of the inherited producer. No SH_n hypothesis or asymptotic estimate is used.

## Status by part

Overall status: PROVED, analytic finite reduction; distinct mathematical
reconstruction and required later Claude scientific/protocol audit pending.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Rule-independent completed-level first derivative | PROVED, analytic | Polynomial-error induction below, including normalization terms |
| Actual nested-projector/frame closure derivative (2) | PROVED, analytic | Both projector terms retained and simplified below |
| Saved inf-rule W/R reductions (3)–(4) | PROVED, analytic | Pointwise equality; no infimum/limit interchange or uniform radius |
| Exact endpoints (8) and finite variational characterization | PROVED, analytic | Source impulses, Hilbert–Schmidt and row bounds below |

The degree12 predicates remain OPEN/G2 NOT RUN at this record's creation.
They are not parts of this analytic theorem's status and require separate
finite computer-assisted records. PD-T055 in its original scope remains OPEN.

## Depends on

PD-T136 for the monic recurrence/g convention and exact-base polynomial
triangularity; its original full-projection hypothesis is not silently
extended. The extension to (1) is proved here. PD-T137 supplies the
source-impulse/trace/row-certificate template, applied to the different
response (7). PD-T053 defines closure versus drift and its one-way bound;
no converse is used. PD-N062 and PD-T055 are closest predecessors, not
an assumption of multi-degree rule invariance.

## Checks

No code was executed by this mathematics worker and no numerical result
is claimed. A medium producer and distinct independent implementation/
execution must use the frozen specification below before G2 is decided.
Full-source exact Gram, coordinate-expansion and closure-derivative controls
are required. The trace formula cannot be validated by Monte Carlo alone.

## Sources

Full closest records PD-T055/136/137/053, PD-N062 and IDEA253–255;
PD-T042/043 separate coefficient/Gram perturbations from this observable.
Current registry delta and exact search/coverage are in
ideas-l2-continuation.md. No new original fulltext or historical-priority
claim. Earlier campaign timing deviation remains for Claude disposition.

## Proof or evidence

**1. Exact baseline coefficients are forced.** At zero every q_k is the
exact orthonormal column. Take inner products of (1) at zero with q_l,
l<k, and with q_k. Uniqueness of the orthogonal expansion gives

    beta_k=sqrt(d_k/d_p),
    c_kl=alpha_kl sqrt(d_l/d_p).                             (9)

The class is nonempty: exact full orthogonal projection and normalization
of the sourced raw product supplies a differentiable member near zero
for each fixed f. Every finite prefix has full rank near zero by continuity
from its orthonormal baseline.

**2. The coefficient and normalization derivatives are polynomial.**
Differentiate (1) at zero. With w_k=sqrt(d_k) dot(q_hat_k), using fixed
baseline d_k, multiply by sqrt(d_p) and use (9):

    w_k=A_k w_p-sum_(l<k)alpha_kl w_l+F_k+h_k,
    h_k=-sqrt(d_p)sum_(l<k)dot(c_hat_kl)q_l
        -sqrt(d_p)dot(beta_hat_k)q_k.                       (10)

Every h_k belongs to S_deg(k), regardless of how its scalar derivatives
depend on the data or on f. Subtract the frozen recurrence for V_k(F).
E_k=w_k-V_k satisfies E_0=0 and

    E_k=A_k E_p-sum_(l<k)alpha_kl E_l+h_k.

Induct on the column index. The parent has degree deg(k)-1, so A_k E_p
has degree at most deg(k); every earlier E_l has degree no greater than
deg(k), and so does h_k. Thus E_k is a polynomial evaluation vector in
S_deg(k). This argument includes earlier sources and changing parent
vectors: it does not freeze a sourced prefix or drop A_k E_p. Consequently

    Z_s:=R_s dot(Q_hat_s)=R_s V_s(F) D_s^(-1/2)              (11)

for every rule. The individual derivative columns need not agree inside
S_s, and no exact finite-epsilon span invariance is asserted.

**3. Nested-projector derivative and actual closure.** Differentiating the
full-rank projector formula
`P_hat=Q_hat(Q_hat^T Q_hat)^(-1)Q_hat^T` at an orthonormal baseline gives

    dot(P_hat_s)=Z_s Q_s^T+Q_s Z_s^T.                        (12)

This proves the stated first-order projector invariance. Let
`H_X,s=Q_(s+1)^T X Q_s`, so XQ_s=Q_(s+1)H_X,s exactly.
For the frame observable in the saved R definition, differentiating gives

    D_X,s=R_(s+1)X dot(Q_hat_s)-dot(P_hat_(s+1))XQ_s
          =R_(s+1)X Z_s-Z_(s+1)H_X,s.                       (13)

Indeed the tangential part of dot(Q_hat_s) lies in S_s, whose X-image
is in S_(s+1), and the Q_(s+1)Z_(s+1)^T term in (12) annihilates XQ_s.
Both moving-span effects are present in (13).

For the actual operator `(I-P_hat_(s+1))X P_hat_s`, (12) similarly gives
derivative `D_X,s Q_s^T`. The other term from dot(P_hat_s) vanishes
because `R_(s+1)XQ_s=0`. Right multiplication by Q_s^T preserves both
the spectral and Frobenius norms of D_X,s. Therefore, for each fixed R,f,

    delta_X(s;epsilon f)=|epsilon| ||D_X,s(F)||_2+o(|epsilon|). (14)

If the observed perturbed frame is subsequently orthonormalized by a
differentiable change of basis equal to identity at zero, its closure
derivative is unchanged: the extra derivative multiplies the zero exact
closure matrix. Thus the saved orthonormal exact-base gauge is well defined
even though class (1) does not require orthogonal stored columns away
from zero.

Use (11) in (13). Since X maps S_s into S_(s+1),
`R_(s+1)X R_s V_s=R_(s+1)X V_s`. Moreover (6) gives
`H_X,s=D_(s+1)^(1/2) C_X,s D_s^(-1/2)`. These identities give (2)
and its entrywise response (7).

**4. Eliminating the infimum without a uniform-radius assertion.** For
each fixed f, finitely many expansions (14) give the limit of the saved
maximum-over-stages quotient as
`max_(s<n)||D_X,s(F)||_2/||X||`. It is the same for every rule by (10)–(13).
The source sphere (5) is also the same for every rule because its sigma
uses the common exact baseline. Take the supremum over that sphere and
then the infimum over the nonempty rule class; the value is unchanged.
There is no exchange of an infimum with a limit, nor any common finite-
epsilon neighborhood assumption. Finally, for a finite set of stages,
`sup_F max_s a_s(F)=max_s sup_F a_s(F)`. This proves (3).

**5. Rational W certificates.** The joint unit source coordinate
u_h=e_i (all other sources zero) gives the rank-one frame output

    tau_h (R_(s+1)e_i)
      [omega_s,0,h(i)/sqrt(d_0),...,omega_s,N_s-1,h(i)/sqrt(d_N_s-1)].

Its squared spectral and Frobenius norms both equal ell_s,h,i. This
proves the lower L_s. Summing these squared Frobenius gains over all
orthonormal source coordinates gives H_s^2, the Hilbert–Schmidt squared
norm of the stage map into Frobenius output. It upper-bounds its spectral-
output operator norm. Before projection, the node-i row depends only on
(u_hi)_h, with entries tau_h omega_s,j,h(i)/sqrt(d_j). Its Frobenius
squared row-map norm is the corresponding sum in U_s^2. Projection
contracts, giving the same rowwise argument as PD-T137. Hence

    max_s L_s^2/||X||^2 <= C_n^2
        <= max_s min(H_s^2,U_s^2)/||X||^2.                  (15)

All decisions use squared rational quantities, not approximate square
roots or a ratio of two lower bounds.

For completeness the exact finite worst-case value also has a rational
variational description. For nonzero monic output vector t and nonzero
node vector r put

    a_i(t)=sum_h tau_h^2 [sum_(j<N_s)omega_s,j,h(i)t_j]^2,
    J_s(t,r)=sum_i (R_(s+1)r)_i^2 a_i(t)
              /[(sum_j d_j t_j^2)(sum_i r_i^2)].             (16)

Then the stage squared capacity is `max_(t!=0,r!=0) J_s(t,r)`.
To see this, test the output in the unit directions
`D_s^(1/2)t/sqrt(t^T D_s t)` and `r/||r||`, then maximize the resulting
linear functional over the unit source sphere. Its squared coefficient
norm is (16). Supremums over source and these two test directions commute;
on normalized compact spheres maxima exist. Any rational t,r give an exact
lower certificate. An exact upper lambda can equivalently be certified by

    lambda(t^T D_s t) I_M - R_(s+1)diag(a_i(t))R_(s+1) >= 0
                        for every real t.                 (17)

This is a finite rational semialgebraic predicate; no efficient quantifier-
elimination implementation or cost bound is asserted. It identifies the
missing inequality if simpler endpoints overlap, without declaring a
false G2 failure.

**6. Exact R expectation.** The saved sign law gives
`u_hi=xi_hi/sqrt((N_n-1)M)`, with independent zero-mean unit signs. Its
covariance is diagonal with entries1/((N_n-1)M), and it has joint norm
one in every realization. The rule-independent map (2) is linear in u.
All cross-source terms in each Frobenius square have zero expectation,
so its expected value is H_s^2/((N_n-1)M). Summing over s and dividing
by ||X||^2 proves (4). This is an exact finite expectation, not a
probability bound or a deterministic lower for every sign realization.

## Frozen finite computation specification

Use T24 and rotQ24 exactly as in the inherited rational producer, BJ only,
n=12, all90 source columns, stages0,...,11. Build exact b,d,alpha,g;
form the complete C_X,s in (6), and compute every omega and ell in
(7)–(8), including j=0 and h in the next-degree block.

Required controls: exact full basis Gram diagonal; positive d,tau^2;
exact coordinate expansion (6) with top degree retained; R-diagonal
within[0,1]; source/stage/dimension coverage; small-degree comparison
against independently differentiated complete projector formulas,
including both terms of (13) and an alternative coefficient/normalization
derivative inside (1). A source pulse's direct projected Frobenius norm
must agree with ell. Expected trace is not checked with Monte Carlo.

For W compare the rational lower/upper in (15) with65536. PASS if the
lower is at least65536, FAIL only if the upper is strictly below65536;
otherwise INCONCLUSIVE with the exact interval/missing inequality. A
later rational witness from (16) or PSD certificate gets a separate
prospective specification before its search. For R compute (4) exactly
and compare with16, with equality counted as PASS. The common denominator
uses90*M, namely29250 on T24 and56250 on rotQ24. Preserve the source
laws and original thresholds without change.

Commit medium-effort producer/checker and small essential receipts with
exact witness/endpoint identities; keep bulk responses outside Git with
regeneration commands and hashes. Obtain distinct independent execution.
No all-degree proof attempt for a reading before its degree12 G2 decision;
an inconclusive decision keeps that attempt blocked.

## Scope

The exact-base smooth restriction is essential. This theorem does not say
that arbitrary prior-vector rules have exactly equal finite-error spans,
that arbitrary rules reproduce this zero-order basis, or that derivatives
of non-smooth/adaptive implementations exist. It does not resolve original
PD-T055 working-precision quantifiers. Coefficients can vary; their first
derivatives vanish only in the completed-degree normal quotient proved
above. Closure and span sensitivity are different maps, and no reverse
use of PD-T053 occurs. No actual IEEE source activation, high-probability
statement, uniform finite-u radius, or all-degree exponential lower follows.

## Open items

Independent mathematical reconstruction; certified degree12 W/R predicates
and their separate finite records; required later Claude audit. Original
PD-T055 and the saved all-degree W/R growth targets remain OPEN. F remains
deferred until a complete actual implementation is frozen. Storage and
publication are root-owned.

## History

- 2026-11-05: Codex mathematics developer, configured gpt-6.1-sol xhigh,
  rules0e493be. Written after the completed delta/source gate in
  ideas-l2-continuation.md and explicit handoff03 finite-development START.
  No G2 run or all-degree L2 proof attempt. Saved class, source laws,
  constants and predicates are preserved. The older campaign-wide
  prospective reading-gate timing deviation remains for Claude disposition.
