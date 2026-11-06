# PD-T?lanczos-nonproduct-codex-P4-02 — weighted finite aggregate normal quotient

ID kind: PD-T.
Aliases: positive-weight PD-T136/137 extension; weighted source convention;
normal leverage; finite arbitrary-vector aggregate model.
Split from: the P4 structural-family target, which remains OPEN.
Split into: none.

## Statement

Fix distinct nodes z_i=(x_i,y_i), strictly positive weights w_i summing
to one, U(n), a graded monomial order x^(t-j)y^j and fixed admissible
coordinate parents. Represent a polynomial b by

    [b]_i=sqrt(w_i)*b(z_i).

In the monic full-projection recurrence let b_0=1,

    b_k=a_k b_parent - sum_(l<k) alpha_kl b_l,
    d_k=sum_i w_i b_k(z_i)^2,
    alpha_kl=sum_i w_i b_l(z_i)*a_k(z_i)*b_parent(z_i)/d_l.

Inject arbitrary Euclidean vectors f_h before exact full projection in
the represented monic-vector recurrence, leaving b_0 unperturbed. Set

    sigma_h^2=sum_i w_i [a_h(z_i)b_parent(h)(z_i)]^2,
    ||f||_src^2=sum_h ||f_h||_2^2/sigma_h^2.

For g_kh defined by PD-T136's scalar recursion with these alpha, let
B_ik=sqrt(w_i)b_k(z_i), D=diag(d_k), P=B D^{-1}B^T and R=I-P through a
completed degree s<=n. Then the first-order spectral span capacity is

    kappa_s=sup_(||f||src=1) || R V(f) D^{-1/2} ||_2,
    V_k(f)_i=sum_h g_kh(z_i) f_h(i).

The angle expansion is theta_s(epsilon;f)=|epsilon| times that spectral
norm plus O(epsilon^2), for each fixed finite data set and fixed f.
For all-source or any declared nonempty source subset J,

    P_ii=w_i sum_(k<N_s) b_k(z_i)^2/d_k,
    v_hi=sigma_h^2 sum_(k>=h,k<N_s) g_kh(z_i)^2/d_k,
    ell_hi=(1-P_ii)*v_hi,
    max_(h in J,i) ell_hi <= kappa_s(J)^2
      <= min(sum_(h in J,i) ell_hi, max_i sum_(h in J) v_hi).

There is **no extra w_i in v_hi**. The f_h coordinates here already are
represented Euclidean coordinates. If instead sources are function values
phi_h(z_i), their represented injections are f_h(i)=sqrt(w_i)phi_h(z_i)
and their source budget is sum_h sum_i w_i phi_h(z_i)^2/sigma_h^2.

## Definitions

All nonconstant columns through s are allowed unless J is specified. Output
is spectral norm of the normal-column matrix, not Frobenius output. The
rules use their own sigma values in the common relative-raw-product
convention. Frozen choices include a recorded tie-break if needed.

## Assumptions

Exact positive finite measure, U(n), fixed admissible parents, exact start,
exact full orthogonal projection, positive base pivots. No scalar-operation
or IEEE realization is assumed. A restricted-source upper cannot bound
the full-source capacity.

## Status by part

Overall status: PROVED (analytic weighted model extension).

| Part | Status | Evidence |
|---|---|---|
| Weighted derivative and endpoint formulas | PROVED | Written proof below |
| Routine attained terminal-degree block corollary | PROVED | Constant inverse and common normal source below; no separate ID |

Candidate disposition: retained model lemma; no family growth law claimed.

## Depends on

PD-T136/137's elementary proof pattern; it is reconstructed for positive
weights here. No reliance on their uniform-weight statement outside scope.

## Checks

No computer-assisted proof component. Supplementary exact Fraction
dual-number graph check executed:

    python3 topics/padua-lanczos-nonproduct-20261105/code/p4_weighted_check.py --output topics/padua-lanczos-nonproduct-20261105/evidence/p4-weighted-check.json

It passed all370 separate source-column/node directions for BJ/mirror at
degrees2/3 on L=n+1 triangular lattices with weights proportional to
1+i+2j. It also verified the impulse/source/leverage scaling with no extra
node weight. Code hash and Python/platform identity are in the compact
[receipt](../evidence/p4-weighted-check.json). This is the developer's
execution, not an independent rerun or a finite reduction of the analytic
theorem. Bulk degree12–16 structural controls remain incomplete.

The routine terminal-degree corollary below also has a supplementary
exact check:

    python3 topics/padua-lanczos-nonproduct-20261105/code/p4_terminal_check.py > topics/padua-lanczos-nonproduct-20261105/evidence/p4-terminal-check.json

All22 simultaneous source vectors passed on the same four n=2/3,
BJ/mirror weighted-triangle cases. Independently differentiated full
sequential projection agrees with the constant terminal block on a common
normal vector, including the generalized Rayleigh quotient and zero
earlier-degree responses. [Receipt](../evidence/p4-terminal-check.json)
pins both source files. These were developer executions. Independent
reruns are recorded in [check-math-reruns.json](../evidence/check-math-reruns.json)
and [audit 01](../audit-01.md#independent-reruns-actually-executed). No
spectral maximum computation or cross-family gate pass is claimed.

## Sources

PD-T136/137 read fully; weighted normalized PD-T324 read fully. No new
external source or historical novelty claim.

## Proof or evidence

Weighted polynomial inner products are ordinary Euclidean inner products
of represented vectors. Coordinate multiplication remains the real diagonal
operator A=diag(a(z_i)), commuting with diag(sqrt(w_i)). The triangular
leading-monomial induction in PD-T136 therefore applies verbatim to
represented vectors, with the weighted alpha,d above: b_k is the unique
monic polynomial orthogonal to all earlier monomials. U(n) gives d_k>0.

Differentiate the perturbed represented recursion. Its derivative is

    dot b_k=A_k dot b_parent - sum alpha_kl dot b_l + f_k
             -sum dot alpha_kl [b_l].

The frozen response V satisfies the same recurrence without the last sum.
Induction makes dot b_k-V_k a represented polynomial of degree<=deg(k):
coordinate multiplication raises degree by at most one, and every earlier
term has at most the target degree. R annihilates it at every completed
degree s containing the column. The normal derivative is thus RV D^{-1/2}.
The graph-over-the-base-subspace argument in PD-T136 proves the angle
expansion; it uses orthonormality of BD^{-1/2}, now already in Euclidean
represented coordinates. All differentiations are finite and smooth near
the positive base pivots.

The displayed P_ii is direct matrix multiplication. Write f_h=sigma_h u_h.
A unit source coordinate u_h=e_i produces the rank-one output

    sigma_h R e_i [g_kh(z_i)/sqrt(d_k)]_k^T.

Its squared spectral norm is ell_hi since ||R e_i||^2=R_ii=1-P_ii. Taking
the maximum gives the lower. Summing these squared Frobenius norms over
an orthonormal source-coordinate basis gives the Hilbert–Schmidt upper.
For the row upper, the unprojected output row at node i is C_i u_i, with

    (C_i)_(k,h)=sigma_h*g_kh(z_i)/sqrt(d_k).

Cauchy–Schwarz and spectral<=Frobenius give
||RV D^{-1/2}||_2<=max_i||C_i||_F times ||u||, whose square is max_i sum_h v_hi.
Weights enter d,sigma and P; the source coordinate e_i is Euclidean unit
length and contributes no additional w_i. This completes the proof.

## Routine corollary: attained terminal-degree block

This is a PROVED corollary of the displayed normal quotient, consolidated
with PD-T324's common-normal-source construction. It has no new theorem
ID or historical-mechanism claim. The same statement holds in the compact
L2 model of [PD-T?lanczos-nonproduct-codex-P4-03](p4-continuous-capacity.md), without requiring atomlessness,
provided the polynomial normal space is nonzero.

Fix s>=1 and let T={N_(s-1),...,N_s-1} be exactly the s+1 final-degree
columns. Define square matrices indexed by T:

    A_kk=1, A_kl=alpha_kl for l<k, A_kl=0 for l>k,
    G=A^(-1), D_T=diag(d_k), S_T=diag(sigma_h^2),
    M_T=D_T^(-1/2) G S_T^(1/2).

If ran(R_s) is nonzero, the **restricted** capacity is exactly

    kappa_s(T)=||M_T||_2.                                  (3)

In particular (3) is a lower bound for the all-source capacity. For finite
positive measures U(s) and M>N_s ensure the required nonzero normal space.
For atomless compact measures it follows from infinite-dimensional L2
and the finite dimension of Pi_s. If ran(R_s)=0 the restricted capacity
is zero instead; the positive matrix norm in (3) must not be used.

To prove (3), set all earlier sources to zero. Causality makes every
frozen response before T zero. Each terminal parent has degree s-1,
so its response is zero as well. The frozen terminal recurrence becomes

    V_k+sum_(l in T,l<k)alpha_kl V_l=f_k.

Thus V=Gf, with constant coefficients and no coordinate dependence.
Write f_h=sigma_h u_h and let U:R^(s+1)->H have columns u_h. Its
Hilbert–Schmidt norm equals the source norm. The normalized output is

    W=R_s U M_T^T,

so ||W||_2<=||U||_HS||M_T||_2. Conversely choose a unit e in ran(R_s)
and a unit right singular vector v for the largest singular value of
M_T. Put u_h=v_h e. The source norm is one, and W=e(M_T v)^T has
spectral norm exactly ||M_T||_2. This proves (3), with attainment.

Equivalently, its squared norm is the largest generalized Rayleigh
quotient

    max_(r!=0) [r^T G^T D_T^(-1) G r]/[r^T S_T^(-1) r].    (4)

The two matrices in (4) are rational for rational nodes/weights. Their
maximum need not be rational. Formula (4) fixes the source and output
gauges explicitly; it does not identify a raw unscaled inverse norm.

Unlike a single-node impulse, the maximizing sources share a normal
vector across the ambient coordinates. Unlike PD-T142/143's inverse
upper score, (3) is an attained capacity for this declared restricted
source set. These are routine consequences of the already available
quotient and normal-source argument, not a new growth mechanism. The
SH topchain of PD-T324 is a one-source subchannel of this block; its
proved lower need not equal the entire block norm. No bound for earlier
sources or polynomial all-source comparator follows from (3).

## Scope

This is the finite M-dimensional source model. Matching polynomial moments
with an atomless measure gives the same polynomial b,alpha,d,sigma through
the needed degree; it does not identify the ambient projector, pointwise
source space, or capacity. In particular when M=N_s and U(s), R=0 and the
finite capacity is exactly zero regardless of nonzero raw responses.
M>N_s and U(s) are separate admission requirements.

## Open items

Complete cross-family tests. Tighter row spectral
bounds and atomless model are proved separately in
[p4-continuous-capacity.md](p4-continuous-capacity.md); moment transfer in
[p4-moment-capacity-transfer.md](p4-moment-capacity-transfer.md).

## History

- 2026-11-05: Codex P4 developer, gpt-6.1-sol xhigh allocation, runtime
  metadata unexposed; rules head ed5515ed84e0e7b12163175dce9f22a859c89c99.
  Written after the prospective gate. No execution claimed at creation.
- 2026-11-05 round3: after boundary dbe5c81 and the prospective terminal
  delta gate, appended the routine attained-block corollary and executed
  its tiny exact check. No new ID, growth criterion or independent audit.
