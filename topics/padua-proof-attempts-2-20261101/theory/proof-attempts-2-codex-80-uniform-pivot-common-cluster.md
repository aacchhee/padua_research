# PD-T?proof-attempts-2-codex-80 — Uniform parent pivots exclude a collapsing common joint cluster

Final ID: **PD-T193**. Provisional ID `PD-T?proof-attempts-2-codex-80` is retained as an alias. Registered after accepted Claude audit-01 and response-01; historical pending-audit notes below are superseded.

Canonical Split from (registration): PD-N039 / OPEN_TARGETS B3 (computed-section extension or separate supporting route obstruction; original scope retained).

ID kind: PD-T.
Aliases: quantitative parent cyclicity; C1 common-cluster obstruction; full-residual cluster bound.
Split from: the first kill test in B3 attempt C1.
Split into: none. Related scoped failed-mechanism corollary: PD-N?proof-attempts-2-codex-02. The B3 counterexample is separate PD-N?proof-attempts-2-codex-01 and escapes this mechanism restriction.

## Statement

Let A,B be real symmetric N-by-N contractions, N>=2, with a fixed parent pattern: for each k=2,...,N one of the operators C_k in{A,B} has a parent j_k<k such that `(C_k)_(i,j_k)=0` for i>k and `(C_k)_(k,j_k)>=p>0`. Then for every a,b in[-1,1] and every unit vector v perpendicular to e_1,

`max(||(A-aI)v||_2,||(B-bI)v||_2) >= c(N,p) := 2/[(1+2/p)^(N-1)-1]`.

Consequently every subspace U of dimension at least2 obeys

`max(||(A-aI)P_U||_2,||(B-bI)P_U||_2)>=c(N,p)`.

A fixed-N family with a common at-least-two-dimensional full approximate eigenspace whose two residual norms tend to0 therefore cannot retain one uniform positive pivot lower bound p. This is a restriction on the LITERAL common shrinking-cluster route, not on every B3 family.

## Definitions

P_U is the orthogonal projector onto U. Contraction means operator2-norm<=1. The parent pattern is the column relation of the fixed graded generalized-Hessenberg basis: symmetry allows the column relation to be read as row j_k. The pivots are actual recurrence entries, not moment-matrix eigenvalues. Every positive-measure section on[-1,1]^2 is a contraction; the pattern hypothesis still must be checked for the particular fixed graded order.

## Assumptions

Exact real linear algebra; positive pivot lower bound p; centres a,b in[-1,1]; FULL residuals `(A-aI)P_U` and `(B-bI)P_U`, including their components outside U.

## Status by part

Overall status: **PROVED** (complete elementary argument). Required Claude audit PENDING.

| Mathematical part | Status | Evidence |
|---|---|---|
| vector residual lower bound | PROVED | parent recurrence and geometric sum |
| common-subspace consequence | PROVED | choose a unit v in U intersect e_1-perpendicular |

The first B3 candidate's literal common-cluster mechanism is failed under these stated assumptions. This is not a negative status for S(alpha); the full target receives a different counterexample separately.

## Depends on

The parent-column pattern in PD-T?programme-ideas-claude-01; otherwise elementary linear algebra only. The argument rechecks the needed pattern implication explicitly rather than inferring a bound from qualitative cyclicity.

## Checks

No mathematical script or unexecuted numerical test is claimed. Root proposed the recurrence bound; the developer checked it independently, and a different analytic reader checked the same parent-row/geometric-sum argument and its full-residual scope. Separate receipt `../independent-checks-b3.md` is supplementary, not the required Claude audit. Exact chronology and gate in `../attempts/T-B3.md`.

## Sources

Registered B3 route and programme finite Favard01; required LOCAL PD-T?bivariate-lanczos-claude-304(a) was read before B3 as recorded in the attempt. No external publication or novelty/priority claim is used for this elementary estimate.

## Proof or evidence

Fix v and write `eta=max(||(A-aI)v||_2,||(B-bI)v||_2)`, `T_k=sum_(i<=k)|v_i|`. Then T_1=0. For each k select C_k and its centre z_k=a or b. In row j_k of the residual, symmetry and the parent zero pattern give

`(C_k v-z_k v)_(j_k) = (C_k)_(k,j_k) v_k + sum_(i<k)(C_k)_(i,j_k)v_i-z_k v_(j_k)`.

Every matrix entry has absolute value<=1 by the contraction assumption, and |z_k|<=1. Since j_k<k, the residual component has absolute value<=eta, and therefore

`p |v_k| <= eta + T_(k-1)+|v_(j_k)| <= eta+2T_(k-1)`.

It follows that `T_k<=(1+2/p)T_(k-1)+eta/p`. Iterating from T_1=0 yields

`T_N <= (eta/p) sum_(r=0)^(N-2)(1+2/p)^r = (eta/2)[(1+2/p)^(N-1)-1]`.

The unit-vector condition gives `1=||v||_2<=||v||_1=T_N`, proving the stated bound. For dim U>=2, the kernel of the single linear functional v->e_1^T v on U is nonzero. Choose a unit v in it; P_U v=v and each full operator norm bounds the corresponding vector residual. This proves the common-subspace claim. ∎

## Scope

This excludes a two-dimensional COMMON collapsing joint cluster with both FULL residuals tending to0 at fixed N,p. A small2x2 compression alone does not meet the hypothesis: large off-U leakage may remain. Nor does the statement exclude marginal clusters in different subspaces, structured-reference distance effects, or shrinking BOX boundaries at one isolated joint node. The separate B3 negative01 uses exactly that last escape while all pivots stay bounded below. No general obstruction to B3 counterexamples or other count objects follows from this lemma.

## Open items

Required Claude audit. The common-cluster bound itself is complete and has no pending computation. Other mechanisms are not decided by this statement.

## History

2026-11-01, Codex `/root/a2_develop`, requested gpt-6.1-sol xhigh, rules b5bba7cf1328b1f207aea001a439c3fe4af0146f. C1 was registered before its analytic kill test; root and a distinct analytic reader supplied supplementary independent checks. A subsequent, separately registered C3 family escaped the exact failed hypothesis. No novelty or priority claim.
