# PD-T002 — A characteristic-free checkerboard criterion using even-index barycentric minors

ID kind: PD-T. Aliases: U1c; divided-alternation Hankel criterion; complementary-minor repair.
Split from: none; this is a changed statement following the explicitly retained refuted U1a, not a relabeling of it.
Split into: none.

## Statement

Let K be any field, m≥0, X and Y have lengths m+1,m+2 with distinct entries within each list, and S_e,V_e,N be as in `odd-characteristic-criterion.md`. No cross-axis distinctness is required. For any length-L list H define

`B_H(f)=Σ_(i even) f(h_i)/ω′_H(h_i),   H_r(H)=det[B_H(t^(a+b))]_(a,b=0)^(r−1).`

Then, for either parity e, S_e is unisolvent for Π_m(K) if and only if

`H_r(X)≠0 and H_r(Y)≠0 for every respective r=1,…,floor((L−2)/2).` (1)

The two ranges are taken separately with their respective lengths L; a negative or zero upper bound is empty. This statement includes characteristic 2 and m=0,1.

An explicit determinant-square identity, also valid in every characteristic, is as follows. Put R(2k)={1,…,k−1}, R(2k+1)={1,…,k}; put Q=∏_(H=X,Y)∏_(r∈R(|H|)) H_r(H). Let E be the unique even-length axis, |E|=2k, and let

`A_E=det[B_E(t^(a+b))]_(a,b=0)^(k−1) = Vand(E_even)^2 ∏_(i even) 1/ω′_E(e_i).`

Let w_i(H)=(-1)^i/ω′_H(h_i) and W_e=∏_(i+j≡e)w_i(X)w_j(Y). Then

`det(V_e)^2 W_e = A_E Q^2.` (2)

In particular A_E and W_e are always nonzero. Every denominator in (2) is a product of within-axis node differences. Formula (2), not division by 2 after specialization, supplies the characteristic-2 claim.

## Status and dependencies

Overall status: PROVED (developer proof; supplementary Astra reconstruction complete; required Claude audit pending). Both (1) and (2) have complete algebraic proofs below. Mechanism classification: reformulation/direct corollary of known Padua-like axis determinant factorization, with locally proved characteristic transfer and cutoff bookkeeping; see literature/U1-COMPARISON.md, read in full by this developer. No novelty claim.

Depends on: `PD-T001`, only its rational-function identity proved in characteristic zero, and elementary Cauchy–Binet/field arithmetic. The specialization argument is proved below and does not assume the characteristic≠2 theorem in characteristic 2.

## Proof

Write s_i=(-1)^i. For the original alternation minors Δ_r(H), Cauchy–Binet gives

`Δ_r=Σ_(I⊆{0,…,L−1}, |I|=r) (∏_(i∈I)w_i) Vand(H_I)^2.` (3)

For I of size r and complementary J of size L−r, the I summand equals

`(-1)^(r(r−1)/2) (∏_(i∈I)s_i) / ∏_(i∈I,j∈J)(h_i−h_j).`

The corresponding J summand is the same. Their ratio is the sign with exponent L(L−1)/2+Σ_(i=0)^(L−1)i−r(r−1), which is even. Thus

`Δ_(L−r)=Δ_r,   Δ_0=Δ_L=1.` (4)

This proof is valid over every field, including characteristic 2; all signs remain formal integer signs before specialization.

By the leading-coefficient identity (2) in the odd-characteristic file, on degrees a<L−1 the original alternation functional equals 2B_H: the ordinary barycentric even-plus-odd sum is zero. Consequently

`Δ_r=2^r H_r for r≤floor(L/2).` (5)

Here 2r−2≤L−2 ensures that every entry is in that degree range. This is an identity over the ring of indeterminate nodes localized at their differences; no division by 2 has occurred.

If L=2k, the even support has exactly k nodes, so its k×k Gram determinant is A_H=Vand(H_even)^2∏even1/ω′_H(h_i)≠0. Equations (4)–(5) give

`∏_(r=1)^L Δ_r = 2^(k²) A_H ∏_(r=1)^(k−1) H_r².` (6)

If L=2k+1, they give

`∏_(r=1)^L Δ_r = 2^(k(k+1)) ∏_(r=1)^k H_r².` (7)

For this odd length, H_k is always nonzero when k≥1: on all entries needed, B_even=−B_odd, and the odd support has exactly k nodes, hence

`H_k=(-1)^k Vand(H_odd)^2 ∏_(i odd)1/ω′_H(h_i)≠0.` (8)

For k=0 no minor is present. The full minors Δ_|X| and Δ_|Y| are 1, so one may include them in the odd-characteristic product identity. If m=2a, the 2-exponent in (6)–(7) is a(a+1)+(a+1)²=(a+1)(2a+1)=N. If m=2a+1, it is (a+1)²+(a+1)(a+2)=(a+1)(2a+3)=N. Substitution in that identity, over Q in independent indeterminate nodes, cancels precisely 2^N and proves (2).

To justify every characteristic, let R be Z[all node indeterminates] localized at the product of all within-axis differences. This is a domain and embeds in its characteristic-zero fraction field. Every expression in (2), including A_E,Q,W_e and V_e, belongs to R. The equality just proved in the fraction field is therefore an equality in R. For any field K and any within-axis distinct specialization, the homomorphism R→K exists and preserves that equality. This proves (2) without any characteristic assumption or hidden denominator 2.

Because A_E,W_e are nonzero in every such specialization, (2) gives det(V_e)≠0 iff Q≠0. In the odd-length axis the terminal minor H_k is nonzero by (8), while the even-axis central minor was absorbed in A_E. Omitting those automatic factors leaves exactly the ranges floor((L−2)/2) in (1). This proves the criterion and parity-independence for all m and every field.

## Checks and sources

`directions/U1/exact_checker.py` checks all displayed identities over odd prime fields and binary extension fields and produces explicit characteristic-2 examples; scope and outputs are separately recorded. The proof is algebraic, not inferred from that finite sample. Symbolic indeterminate nodes above are explicitly proof scaffolding; distinctness suffices at specialization because all denominators are tracked.

Closest literature: source alternation-minor conjecture; Harris–Simanek; De Marchi–Usevich (2014) Padua-like Vandermonde factorization. Literature/U1-COMPARISON.md proves the conversion of predecessor axis factors to these barycentric Hankel minors; classify this as an established-axis-factor rewrite. Exact printed all-characteristic coverage remains unverified. No theorem from an unread source is used as a proof dependency.

## Open items and history

Supplementary Astra reconstruction/rerun and bounded prior-art comparison are complete; required Claude audit remains pending. Full-symbolic m=2,3,4 factor records and exact numeric slices are verification records, not limitations on the proved quantifiers.

2026-10-31, Codex `gpt-6.1-sol` xhigh, rules/base d36722823441dc40c6e19d69a174459348dd309c. Changed functional B_H explicitly replaces the refuted characteristic-2 alternation functional; original claim remains preserved in its negative file.
