# PD-T?padua-3d-20261106-codex-D1-01 — finite defect and reflection lift

ID kind: PD-T. Aliases: D1-FRAME; Christoffel defect sum; sign-orbit unfolding.
Split from: C1's supporting finite identities in the frontier assessment.
Split into: none. Original asymptotic target remains OPEN in the D1 ledger until its limit proof is complete. [Superseded 2026-11-12 (audit-05): completed in D1-03/D1-04 and the R4 [reconstruction](reconstruction.md); current status in the [D1 README](README.md); this line is retained as round history.]

## Statement, definitions and assumptions

Let mu be a probability measure on R^d for which the real polynomial space V=Pi_(n-1)^d has a positive-definite L2(mu) inner product. Let distinct nodes x_i and positive weights w_i give cubature exact on Pi_(2n-2). Write D=dim V, choose a real orthonormal basis phi_1,...,phi_D, and K(x,y)=sum phi_a(x)phi_a(y). Then

    p_i=w_i K(x_i,x_i),  delta_i=1-p_i >=0,
    sum_i delta_i=N-D,
    sum_(j!=i) w_i w_j K(x_i,x_j)^2=p_i delta_i.

For normalized product Chebyshev measure on [-1,1]^d, assume all nodes x_i lie in the closed cube [-1,1]^d and replace each x_i by its distinct coordinate sign orbit of theta_i=arccos(x_i) on T^d=(R/2pi Z)^d. Give each orbit atom weight w_i/s_i, where s_i is its number of distinct elements. Different cube nodes have disjoint orbits, 1<=s_i<=2^d, so the lifted rule has M=sum s_i<=2^d N distinct positive atoms t_j of masses v_j. It is exact for every character exp(i k.t) with |k|_1<=2n-2.

Set A_n={k in Z^d: |k|_1<=n-1}, m_n=|A_n|, D_n(t)=sum_(k in A_n) exp(i k.t). Then E_(jk)=sqrt(v_j)exp(i k.t_j) satisfies E*E=I. Its rank-m_n projection P=EE* obeys

    q_j=m_n v_j<=1, eta_j=1-q_j>=0,
    sum eta_j=M-m_n,
    sum_(l!=j) v_j v_l |D_n(t_j-t_l)|^2=q_j eta_j.

If n_r tends to infinity and N_r/binom(n_r+d-1,d) tends to one, then M_r/m_(n_r) tends to one. For the Chebyshev lift this includes arbitrary support locations within the closed cube, positive weights and boundary stabilizers.

## Status and dependencies

Overall status: **PROVED** (local analytic supporting result). No external theorem is used. No rejection/negative-result claim. The general asymptotic cubature lower bound is not a conjunct of this lemma and does not become PARTIAL from it.

## Proof

For B_(ia)=sqrt(w_i)phi_a(x_i), exactness on products phi_a phi_b gives B^T B=I. Thus BB^T is an orthogonal projection. Its diagonal entries p_i lie in [0,1] and sum to D. The i-th diagonal of P^2=P says sum_j P_ij^2=p_i, proving the row formula after subtracting p_i^2. The constant basis direction shows K(x_i,x_i)>0.

On a sign orbit, independent averaging of exp(i k.theta) equals product_j cos(k_j theta_j), including theta_j=0 or pi: averaging all 2^d signs with repetitions gives the same uniform measure on the distinct orbit because every point has the same stabilizer. The product is product T_(|k_j|)(x_j), of total degree |k|_1. Chebyshev exactness therefore makes its lifted average zero for nonzero k in the stated range and one at k=0. Haar torus moments have exactly those values. Distinct orbits cannot meet since their coordinate cosines would then agree.

Differences of two members of A_n have l1 norm at most 2n-2, so lifted character exactness gives E*E=I. The complex projection identities follow by the same diagonal and trace calculation, with squared moduli.

Finally, counting orthants, their boundaries contribute O(n^(d-1)), giving

    m_n=(2^d/d!) n^d+O(n^(d-1)),
    binom(n+d-1,d)=n^d/d!+O(n^(d-1)).

The projection gives m_n<=M, and folding gives M<=2^d N. Hence

    1 <= M/m_n <= 2^d N/m_n -> 1.

In particular, boundary stabilizers cause no missing leading-order mass: this follows from the squeeze, without a separate boundary-node estimate. Exactness through 2n-1 is stronger than needed throughout. QED.

## Scope, controls and next step

The first identity works for any positive-definite polynomial measure; the reflection lift uses the exact product Chebyshev measure. It does not prove a local octahedral limit for a general doubling weight. Signed weights do not supply these positive projections.

The deterministic exact controls are `../code/fd1_controls.py` and `../evidence/fd1-controls.json`. They check finite examples only and are not premises of the proof. Independent execution is requested from root. Next unresolved D1 step: a separated high-leverage local limit with a complete exponential basis, including density/completeness rather than orthogonality alone. [Superseded 2026-11-12 (audit-05): completed in D1-03/D1-04 and the R4 [reconstruction](reconstruction.md); current status in the [D1 README](README.md); this line is retained as round history.]

## History

2026-11-12, Codex, assigned gpt-6.1-sol xhigh. R1 preregistration published at `f9ab1c6` before development; root GO received. This is a proof of the finite sketch credited to frontier S2/S4, not a priority claim.

2026-11-12, response-05, Codex assigned gpt-6.1-sol high: explicitly stated the closed-cube node hypothesis for the Chebyshev reflection lift and its squeeze conclusion (H1; audit-05 D1a-F1). The general polynomial projection identity in the opening paragraph remains valid under its original R^d assumptions; only the lift requires cube nodes. No identity, proof or status changed.
