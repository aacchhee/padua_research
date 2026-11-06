# PD-T?padua-3d-codex-T4-03 — explicit recursive Lebesgue upper majorant

ID kind: PD-T. Aliases: Newton residual norm bound; greedy-height bound.
Split from: none. Split into: none.

## Statement and definitions

For T4-01's stack, set B_0=1 and B_m=sqrt(2m(m+1)) for m>=1. With the
same omega_k and distinct heights, define the positive numbers

b_k = B_{n-k}/|omega_k(z_k)| *
      (1+sum_{i<k}|omega_i(z_k)|b_i).

Then the continuous cube Lebesgue constant satisfies

Lambda(X_n) <= sum_{k=0}^n 2^k b_k.                             (1)

For exact greedy discrete-Leja ordering of the n+1 Lobatto heights, n>=1,
a simpler bound is

Lambda(X_n) <= sqrt(2n) [product_{m=0}^n(1+B_m)-1].              (2)

Thus this ordering has a rigorous, coarse exp(O(n log(n+1))) upper bound.
No polynomial or polylogarithmic upper bound is claimed.

## Assumptions / status

Same planar Padua convention as T4-01; arbitrary distinct heights in (1).
Greedy in (2) means an exact maximizer of the absolute Newton product over
the unused Lobatto heights at every step, with any exact tie resolution.
Overall status: **PROVED**, developer analytic proof; independent audit
pending. These are standard norm estimates, with no priority claim.

## Depends on / proof

T4-01's Newton formula and PD-T004's positive real Padua Gram identity.
The latter gives cardinal functions ell_xi(u)=w_xi K_m(u,xi), with kernel
K_m(u,v)=sum_phi phi(u)phi(v)/D_phi. Cauchy-Schwarz and discrete reproducing
orthogonality give

sum_xi |ell_xi(u)| <= sqrt(sum_xi w_xi)*
                       sqrt(sum_xi w_xi K_m(u,xi)^2)
                    = sqrt(K_m(u,u)).

Here sum w=1. Since every Chebyshev product has magnitude<=1 on the square,
K_m(u,u)<=sum_phi 1/D_phi=2m(m+1) for m>=1. Indeed the ordinary product
norms give 2m(m-1) from a,b>0, 4m from the two axes and1 from the constant,
and the exceptional (m,0) norm subtracts1. For m=0 the norm is1. Thus the
planar interpolation norm is at most B_m.

For node data of supremum norm<=1, inductively the Newton coefficients in
T4-01 satisfy ||q_k||_square<=b_k. Also |omega_k(z)|<=2^k for z in [-1,1].
Triangle inequality proves (1), uniformly over all node data. The operator
norm on arbitrary node data equals the Lebesgue constant (choose the signs
of the cardinals at a maximizing point), so this is a true continuous bound.

For the greedy case set t_k=|omega_k(z_k)| ||q_k||. By greedy maximization,
|omega_i(z_k)|<=|omega_i(z_i)| for k>i, so
t_k<=B_{n-k}(1+sum_{i<k}t_i). Consequently
sum_k t_k <= product_{m=0}^n(1+B_m)-1.
The degree-k polynomial omega_k vanishes at the previous heights, and its
maximum on the complete Lobatto grid is |omega_k(z_k)|. Degree-n univariate
interpolation on that grid therefore implies
||omega_k||_interval<=Lambda_Lobatto(n)|omega_k(z_k)|.
The same positive Gram/Cauchy-Schwarz argument in one dimension bounds
Lambda_Lobatto(n)<=sqrt(2n): endpoint-half Lobatto weights have sum1,
Chebyshev squared norms1 for degrees0,n and1/2 for1,...,n-1. Their inverse
sum is2n. Combining the last three inequalities proves (2). Finally
B_m<=sqrt(2)(n+1), so its logarithm is O(n log(n+1)).

## Checks / sources / limits

Hand proof only; no computer proof or numerical upper certificate. PD-T004
was read in full. Historical Radon/Berzolari comparison remains pending.
The bounds are deliberately coarse; they do not imply BRIEF E2's polynomial
expectation. Floating greedy permutations in the bounded screen are stored;
that numerical ordering calculation is not a dependency of this exact-greedy
theorem. Its small numerical tie tolerance is disclosed in code.

## Open items / history

Sharper all-n upper bounds remain OPEN. Independent audit pending.
2026-11-06 Codex, assigned gpt-6.1-sol/xhigh, runtime model metadata unexposed;
rules/input ccd9e905d19c0c625c196c4a3f3e707058ed042a.
