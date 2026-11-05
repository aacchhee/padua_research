# PD-T286 — finite discrete nearest-neighbour data from moment systems

Final ID: **PD-T286**. Provisional alias: `PD-T?nn-mop-iep-codex-01`.

ID kind: PD-T. Aliases: normal finite MOP triangle; direct moment baseline; C1.
Split from: none. Split into: none.

## Statement

Let x_1,...,x_N be distinct real nodes and w_{s,l}>0 for s=1,2.
Put L_s(f)=sum_l w_{s,l} f(x_l). For nu=(n,m), k=n+m,
let M_nu have rows (L_1(x^(i+j)))_{j=0}^{k-1}, i=0,...,n-1,
followed by (L_2(x^(i+j)))_{j=0}^{k-1}, i=0,...,m-1.
The empty determinant is 1. Call nu normal when det M_nu != 0.

For each normal nu there is exactly one monic degree-k polynomial P_nu
with L_1(x^i P_nu)=0 for i<n and L_2(x^i P_nu)=0 for i<m.
It is obtained by solving M_nu c = -(L_s(x^(i+k))) in the same row order.
Conversely uniqueness of this monic polynomial implies normality.

Suppose all indices of total degree <=N are normal. Then every index
nu with |nu|<=N-1 has the two nearest-neighbour identities

    x P_nu = P_(nu+e_j) + b_(nu,j) P_nu
             + a_(nu,1) P_(nu-e_1) + a_(nu,2) P_(nu-e_2), j=1,2.

Absent predecessors have coefficient zero. With h_(nu,s)=L_s(x^(nu_s)P_nu),
a_(nu,s)=h_(nu,s)/h_(nu-e_s,s) when nu_s>0.
Writing t_nu for the coefficient of x^(|nu|-1) in P_nu (t_0=0),
b_(nu,j)=t_nu-t_(nu+e_j). These coefficients are unique under this convention.
In particular the finite input determines all these arrays on |nu|<=N-1.
Strict positivity of both weight vectors alone does not ensure normality.

## Definitions and assumptions

Monic type-II MOPs; one polynomial variable x, two linear functionals.
Exact arithmetic. Normality on the stated region is an assumption, not a
consequence of positivity or a claim about all positive inputs.

## Status by part

Overall status: PROVED. Standard defining linear algebra and recurrence
derivation, with no priority or new-algorithm claim. Claude audit-01 accepted; preparation protocol check pending.

## Depends on

Elementary linear algebra only. No external theorem is used in the proof.
FHV 2015 and Van Assche 2011 are literature predecessors; see ../literature.md.

## Proof

The monic orthogonality equations are exactly the displayed square system.
An invertible matrix gives existence and uniqueness. If a singular square
system has a solution it has more than one; otherwise it has none. This proves
the equivalence with uniqueness.

For a normal nu, h_(nu,s) is nonzero whenever nu+e_s is normal: if h were
zero, the coefficient vector of P_nu, padded to degree |nu|, would be a
nonzero null vector of M_(nu+e_s). Thus every denominator in the statement
is nonzero. Fix j and subtract P_(nu+e_j) and b_(nu,j)P_nu from xP_nu.
The resulting R has degree <=k-1. It obeys the orthogonality conditions
with index (max(n-1,0),max(m-1,0)).
For n,m>0 that space, inside polynomials of degree <=k-1, has dimension two:
the k-2 constraints have independent rows, since their first k-2 columns form
the invertible predecessor moment matrix. Both P_(nu-e_1) and
P_(nu-e_2) lie in it and are independent. Indeed, if they were equal,
their monic degree k-1 common value would satisfy every constraint at nu,
contradicting invertibility of M_nu. Hence they form a basis of this space.
Applying L_s(x^(nu_s-1) .) to R gives h_(nu,s); on the predecessor in
the other direction it gives zero, and on P_(nu-e_s) it gives
h_(nu-e_s,s). This proves both coefficient ratios and shows that they do
not depend on j. On an axis, the same argument uses k-1 independent
constraints in degree <=k-1, a one-dimensional space and the sole predecessor.
At nu=0 the residual has degree <0 and is zero. Comparison of subleading
coefficients proves the b formula in all cases.

For failure of positivity alone take N>=2 and w_2=w_1. At nu=(1,1)
the two rows of M_nu coincide. For example nodes 0,1 and both weights
(1,1) give repeated row (2,1), so det M_(1,1)=0.

## Checks

Exact finite sanity checks and input specification: ../exact-runs.md and
../code/exact_nn_mop.py. These corroborate formulas; the general proof is
the argument above, not a computer-assisted proof. Supplementary independent
check and Claude audit are recorded separately when actually completed.

## Scope and open items

This is a known exact direct solver, with no floating-point stability promise.
It does not turn the two index directions into two multiplication variables.
No bijection from arbitrary coefficient arrays to positive input measures is
claimed. Conditioning, fast stable updating and incomplete normal regions
remain outside this statement.

## History

2026-11-05: Codex mathematical developer, rules/head
320fe07f5231ac7e72a4da45e64a38e5ff381b4a; actual runtime model family GPT-6,
exact backend model/effort not exposed to this orchestrator. Bounded workers
are explicitly gpt-6.1-sol xhigh (gate) and medium (code).
