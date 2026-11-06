# PD-T?padua-3d-20261106-codex-T4-02 — exact height factor in the stack determinant

ID kind: PD-T. Aliases: Newton block determinant; height permutations.
Split from: none. Split into: none.

## Statement and definitions

In the setting of T4-01, let N_k=binom(n-k+2,2). For each k choose one
fixed ordering of Pad_{n-k}, and use the same monomial basis ordering for
every height permutation. Up to one fixed sign independent of the heights,

det V(X_n) = [product_{k=0}^n det V_2(Pad_{n-k})]
             product_{0<=i<j<=n}(z_j-z_i)^{N_j}.                 (1)

For the n+1 Lobatto heights h_a=cos(a*pi/n), n>=1, put

D(pi)=product_{i<j}|h_{pi(j)}-h_{pi(i)}|^{N_j},
S_n=binom(n+3,4), N=binom(n+3,3),
A_n=[(n+1)log n+(3-n^2)log2]/[n(n+1)].

Then the exact finite inequality

log Lambda(X_pi) >= max(0, [S_n A_n-log D(pi)]/N)                (2)

holds, with natural logarithms and continuous cube Lebesgue constant.

## Assumptions / status

All statements are over R; heights distinct, n>=1 in (2). Overall status:
**PROVED**, developer analytic proof, independent audit pending. Retained
standard determinant comparison specialized to the requested baseline.

## Depends on

T4-01 for stack unisolvence; elementary determinant algebra and Chebyshev
polynomial identities proved below. No numerical determinant is used.

## Proof

Use the basis x^a y^b omega_k(z), a+b<=n-k, k=0..n. Its transformation
from x^a y^b z^k is unit triangular, since omega_k is monic of degree k.
Its evaluation matrix, grouped by layers and k, is block lower triangular:
omega_k(z_l)=0 for l<k. Its kth diagonal block is omega_k(z_k) times the
planar monomial Vandermonde, of size N_k. Multiplying the diagonal block
determinants proves (1), including the stated height-independent sign.

Let ell_b be the stack's cardinal polynomials. For any other unisolvent
stack Y obtained by permuting the same heights, V(Y)=L(Y)V(X), where
L_ab=ell_b(Y_a). Each row of L has l1 norm<=Lambda(X), hence Euclidean
norm<=Lambda(X). Hadamard's determinant inequality gives

|det V(Y)/det V(X)|=|det L|<=Lambda(X)^N.

The planar factors cancel in (1). Maximizing over Y and then lower bounding
the maximum of log D by its average over all permutations gives
N log Lambda>=mean_pi log D(pi)-log D(X). The average for each fixed pair
i<j is A_n, the average log distance of two distinct Lobatto heights. Thus
mean log D=A_n sum_j j N_j=S_n A_n. The sum identity follows by counting
quadruples or by the hockey-stick identity (and also holds at n=1).

For completeness, the monic Lobatto node polynomial is
W(z)=2^{1-n}(z^2-1)U_{n-1}(z). Its derivative has magnitude
2^{1-n}n at each of the n-1 interior heights, and twice this at either
endpoint. Therefore

product_{a<b}|h_a-h_b|^2 = product_a |W'(h_a)|
                        =n^{n+1}2^{3-n^2}.

Dividing its logarithm by n(n+1) proves the displayed A_n. Finally
Lambda>=1 since constants reproduce. This proves (2).

## Checks / sources / limits

This is a hand proof, not a computer-assisted proof. Finite exact-expression
and floating regressions will be recorded separately. General determinant
domination is standard; historical source comparison is pending. Formula
(2) is valid for every permutation but may be weak for some permutations.

## Open items / history

Independent mathematical audit pending. For the asymptotic evaluation of
(2) in the monotone ordering see T4-03; no such evaluation is assumed here.
2026-11-06 Codex, assigned gpt-6.1-sol/xhigh, runtime metadata unexposed;
rules/input ccd9e905d19c0c625c196c4a3f3e707058ed042a.

## Supplementary check addendum — 2026-11-06

[Distinct Astra high check](../independent-checks-computation.md) completed
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
response dispositions, ID-kind mappings and evidence changes were covered
by [Claude audit-02](../audit-02.md); its accepted mathematical scope is
recorded there. This dated correction changes no statement or status.
