# PD-T?nn-mop-stability-codex-D4-01 — finite common Christoffel transport

ID kind: PD-T (provisional allocation).
Aliases: common spectral shift; NN Darboux update; Christoffel ratio transport.
Split from: D4-C1, exact invariant supporting the unresolved stability target.
Split into: none.

## Statement

On N distinct real nodes, let two functionals have a normal mixed moment triangle through total degree N. Put F(x)=prod_l(x-x_l). For nu=(n,m), |nu|<=N, let D_nu be its moment determinant and P_nu its monic type-II polynomial; P_eta=F when |eta|=N. For c outside the nodes define Ltilde_s(f)=L_s((x-c)f). Then

    Dtilde_nu=(-1)^|nu| P_nu(c) D_nu.

Consequently the transformed full triangle is normal exactly when every P_nu(c) is nonzero. Assuming this, its NN array is obtained from the original array in O(N^2) arithmetic and storage by the formulas below. These are an exact update of known data, not an algorithm for obtaining the starting array.

## Definitions

Moment rows are ordered first (s=1,i=0..n-1), then (s=2,i=0..m-1); columns have exponents 0..|nu|-1. NN convention:

    x P_nu=P_(nu+e_j)+b_(nu,j) P_nu+sum_s a_(nu,s) P_(nu-e_s).

Absent predecessor terms are zero. The stored array has |nu|<=N-1. For these indices set R_(nu,j)=P_(nu+e_j)(c)/P_nu(c).

## Assumptions

N>=1; old and transformed normality as stated; exact field arithmetic of characteristic zero; c different from every node. Positivity is not required. To retain positive weights, one may take c below all nodes. This does not ensure transformed mixed normality (D4-02).

## Status by part

Overall status: PROVED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Determinant and polynomial identities, ratio and finite NN update | PROVED | Direct moment proof below |

Candidate / claim disposition: retained as known algebra; numerical stability remains separate and OPEN.

## Depends on

PD-T286 finite-moment definition and NN existence on the normal triangle, including h-ratio a. The identities below are rederived, rather than inherited from primary sources. PD-T288 explains the interior divisor convention of the C4 comparison.

## Proof or evidence

The bordered determinant for D_nu P_nu(c) has the |nu| moment rows with columns 0..|nu| and last row (1,c,...,c^|nu|). In decreasing order replace column j by column j minus c times column j-1, for j=|nu|,...,1. The last row becomes (1,0,...,0). Expansion on that row has sign (-1)^|nu| and remaining entries L_s(x^i(x-c)x^(j-1)); this proves the determinant identity, including the empty determinant. Normality equivalence follows because D_nu is nonzero. This proof fixes the row-order sign explicitly.

For |nu|<=N-1 and either j,

    Ptilde_nu(x)=[P_(nu+e_j)(x)-R_(nu,j)P_nu(x)]/(x-c).

The numerator vanishes at c; its quotient is monic of degree |nu|. Its transformed orthogonality follows by multiplying back by x-c and applying old orthogonality to every required row. Uniqueness proves independence of j. At degree N the transformed polynomial is F.

Evaluating the old NN recurrence at c and dividing by P_nu(c) gives the layer-ordered recursion

    R_(nu,j)=c-b_(nu,j)-sum_(s:nu_s>0) a_(nu,s)/R_(nu-e_s,s).

Every denominator is nonzero under the stated normality and support hypotheses. Define h_(nu,j)=L_j(x^nu_j P_nu). Applying L_j(x^nu_j .) to the polynomial numerator in successor direction j gives htilde_(nu,j)=-R_(nu,j)h_(nu,j), since the successor term integrates to zero. The h-ratio characterization a_(nu,j)=h_(nu,j)/h_(nu-e_j,j) now yields

    atilde_(nu,j)=a_(nu,j)R_(nu,j)/R_(nu-e_j,j),   nu_j>0.

Absent a remains zero. Write gamma_nu for the coefficient of x^(|nu|-1) in P_nu, with gamma_0=0. Comparing coefficients in the polynomial formula gives gamma_tilde_nu=gamma_(nu+e_j)-R_(nu,j)+c. Since b_(nu,j)=gamma_nu-gamma_(nu+e_j), comparison of adjacent transformed gammas gives, for |nu|<=N-2,

    btilde_(nu,j)=b_(nu+e_j,j)+R_(nu+e_j,j)-R_(nu,j).

On |nu|=N-1 the transformed successor is F, whose gamma is unchanged. Thus the finite boundary formula is

    btilde_(nu,j)=c-R_(nu,j).

It requires no degree N+1 polynomial. There are N(N+1)/2 stored vertices and a bounded number of operations per vertex. The invariant is equality to the transformed moment functionals, stronger than merely satisfying local compatibility equations.

## Checks

`code/integrable_transport.py --mode exact`: N=4 Krawtchouk and Hahn, 80 NN coefficient fields and 30 determinant identities exact over Fraction, and all polynomial identities through the boundary, passed. Frozen commands/hashes are in `attempts/D4.md`. Finite checks support implementation only; the proof above is independent of their enumeration. Independent checker replay is pending coordinator assignment.

## Sources

LIT-D4-01, Proposition 3.2 and Theorem 3.4: known common Christoffel/Geronimus polynomial formulas. LIT-D4-02, introduction and Theorem 3.2 statement: existing transformed-NN algorithm. See `literature-D4.md` for actual partial-primary reading. No novelty of the transformation is claimed.

## Scope

An exact finite update of an existing normal triangle. Its arithmetic omits C4's interior b-difference divisor, but substitutes polynomial-evaluation ratios. It makes no rounding-error or uniform positivity claim. Small ratios and cancellation in R can be arbitrarily unfavorable. The diagnostic chi=(|c|+|b|+sum|a/Rprev|)/|R| is local, and neither bounds propagation nor certifies normality in floating point.

## Open items

Input-sensitive forward/backward error bounds; a useful starting array obtainable without an ill-conditioned reconstruction; independently varied weights. D4-C1a's particular predivide-C4-restore proposal failed the benchmark gate (D4-05).

## History

2026-11-05, Codex dispatched gpt-6.1-sol xhigh; source 823cf6a4, before publication round 1. Known formula rederived with finite boundary; no theorem of numerical stability attached.
