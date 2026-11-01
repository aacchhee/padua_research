# PD-N?proof-attempts-2-codex-02 — A common collapsing cluster cannot retain uniform parent pivots

Final ID: **PD-N073**. Provisional ID `PD-N?proof-attempts-2-codex-02` is retained as an alias. Registered after accepted Claude audit-01 and response-01; historical pending-audit notes below are superseded.

Canonical Split from (registration): PD-N039 / OPEN_TARGETS B3 (computed-section extension or separate supporting route obstruction; original scope retained).

ID kind: PD-N.
Aliases: B3-C1 literal cluster implantation failure; shared two-dimensional full-residual obstruction; fixed-degree uniform-pivot limitation.
Split from: attempted mechanism B3-C1 in attempts/T-B3.md.
Split into: none. Positive quantitative estimate is retained separately as PD-T?proof-attempts-2-codex-80. The successful computed-section count counterexample is separate PD-N?proof-attempts-2-codex-01.

## Statement

Fix an integer N>=2, p>0 and a fixed parent pattern as in80. There does NOT exist a sequence of real symmetric contraction pairs(A_m,B_m), each with every prescribed parent pivot>=p, together with centres(a_m,b_m) in[-1,1]^2 and subspaces U_m of dimension>=2, for which

`epsilon_m := max(||(A_m-a_m I)P_(U_m)||_2,||(B_m-b_m I)P_(U_m)||_2) -> 0`.

In fact EVERY member necessarily satisfies

`epsilon_m >= 2/[(1+2/p)^(N-1)-1] > 0`.

Thus the specific attempt to implant the old common shrinking two-dimensional x/y cluster (including a45-degree rotation inside it) into fixed-degree positive-pivot computed sections, with BOTH full residuals tending to0 and one uniform p, fails. This does not prohibit two close SUPPORT atoms in an overdetermined measure; the claim concerns the alleged cluster INHERITED BY ITS SECTIONS.

## Definitions

For each k=2,...,N the fixed parent pattern prescribes one C_k in{A,B} and j_k<k, with `(C_k)_(i,j_k)=0` for i>k and `(C_k)_(k,j_k)>=p`. P_U is the orthogonal projector. Full residual includes the component outside U; a bound on only `P_U(A-aI)P_U` or `P_U(B-bI)P_U` is insufficient. Symmetric contraction means operator2-norm<=1.

## Assumptions

Fixed N,p,centre bounds and fixed recurrence/parent order; exact real linear algebra; full residuals. These assumptions hold for the literal mechanism being tested only if its actual positive square-supported section matrices and all selected recurrence pivots have been verified. No commutator-size assumption is needed for the obstruction.

## Status by part

Overall status: **PROVED**, by the quantitative80 corollary below. Required Claude audit PENDING.

Candidate / claim disposition: B3-C1 is **REJECTED: failed** for the precise shared-cluster implantation mechanism under these hypotheses. This disposition concerns a mechanism, not B3's robustness statement S(alpha); the latter has a different successful counterexample in negative01.

## Negative-result scope

Attempted mechanism: preserve a shrinking, common, at-least-two-dimensional approximate joint eigenspace of BOTH computed sections at fixed degree while keeping one positive pivot lower bound. The source-inspired45-degree rotation is included only when its full off-subspace leakage also tends to0.
Parameter range: any FIXED N>=2 and p>0 with the prescribed parent pattern and bounded centres; in B3, N=dim Pi_n and n is fixed. The number M of positive support atoms need not be fixed, but that does not relax the hypotheses on the N-by-N sections.

## Depends on

PD-T?proof-attempts-2-codex-80, whose full-residual quantitative cyclicity estimate is retained PROVED in its own file. No new numerical or symbolic obligation.

## Checks

80's parent-row induction was independently reconstructed by root and a different analytic reader. This scoped negative is precisely its corollary, not an administrative negative record or a claim of an unexecuted test. The full final-file readings are recorded in `../independent-checks-b3.md`. Required Claude audit remains separate.

## Sources

B3's registered common-cluster route and the closest general symmetric-pair cluster in PD-N?programme-ideas-claude-01. The full relaxed registry and linked-record gate is recorded in `../attempts/T-B3.md`. Required LOCAL PD-T?bivariate-lanczos-claude-304(a) was read, but its support-radius estimate is not used as the residual bound here. No novelty/priority claim.

## Proof or evidence

For each U_m, choose a unit vector v_m in `U_m intersect e_1-perpendicular`, which exists because dim U_m>=2. Result80 gives

`max(||(A_m-a_m I)v_m||_2,||(B_m-b_m I)v_m||_2)>=c(N,p)`.

Since P_(U_m)v_m=v_m, this quantity is at most epsilon_m. The fixed number c(N,p)>0 cannot tend to0. This proves the negative statement and its explicit quantitative bound. ∎

## Scope

ONLY the stated common-cluster/full-residual mechanism fails. Small compressions with large external leakage, separate marginal clusters, a varying p tending to0, growing N, or centres outside the stated range are not ruled out. In particular shrinking test BOXES around one isolated joint node evade the failed hypothesis: negative01 exploits exactly that different configuration and retains uniform positive pivots. This record is not an impossibility theorem for B3 counterexamples, for other count objects, or for structured nearby commuting references.

## Open items

Required Claude audit. No further mathematical run is needed for this corollary. Any relaxed cluster mechanism needs a new precise hypothesis/test and cannot inherit this negative result outside its scope.

## History

2026-11-01, Codex `/root/a2_develop`, requested gpt-6.1-sol xhigh, rules b5bba7cf1328b1f207aea001a439c3fe4af0146f. C1 was registered and analytically killed before the successful C3 route. Root requested this separate scoped failed-mechanism record after reading positive80, to preserve both the positive estimate and the exact negative disposition. No new mathematics or computation was introduced by this classification.
