# PD-T?lanczos-nonproduct-codex-P4-02 — weighted finite aggregate normal quotient

ID kind: PD-T.
Aliases: positive-weight PD-T136/137 extension; weighted source convention;
normal leverage; finite arbitrary-vector aggregate model.
Split from: P4 model/criterion target.
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

Candidate disposition: retained model lemma; no family growth law claimed.

## Depends on

PD-T136/137's elementary proof pattern; it is reconstructed for positive
weights here. No reliance on their uniform-weight statement outside scope.

## Checks

No computer-assisted proof component. A supplementary tiny rational dual
check is planned in attempts/P4.md; it has not yet executed at this file's
creation. Bulk degree12–16 structural controls remain incomplete.

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

## Scope

This is the finite M-dimensional source model. Matching polynomial moments
with an atomless measure gives the same polynomial b,alpha,d,sigma through
the needed degree; it does not identify the ambient projector, pointwise
source space, or capacity. In particular when M=N_s and U(s), R=0 and the
finite capacity is exactly zero regardless of nonzero raw responses.
M>N_s and U(s) are separate admission requirements.

## Open items

Supplementary exact derivative check; complete cross-family tests; tighter
row spectral bounds; atomless model and any rigorously justified transfer.

## History

- 2026-11-05: Codex P4 developer, gpt-6.1-sol xhigh allocation, runtime
  metadata unexposed; rules head ed5515ed84e0e7b12163175dce9f22a859c89c99.
  Written after the prospective gate. No execution claimed at creation.
