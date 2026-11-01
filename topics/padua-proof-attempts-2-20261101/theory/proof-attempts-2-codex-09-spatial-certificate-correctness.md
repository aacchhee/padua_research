# PD-T?proof-attempts-2-codex-09 — Correctness of the spatial and edge-arrangement certificate

Current audit note, 2026-11-01: Claude audit-01 accepted this record at its stated scope. Historical audit-pending statements below describe development checkpoints.

Dated status supersession, 2026-11-01 (response to audit-01 F8): Count10 and global11 are PROVED for n=4. Claude audit-01 accepted these cases and this supporting result. Later OPEN/checks-needed lines retain the earlier development checkpoint and are superseded by this note; no mathematical status or proof changes.

ID kind: PD-T.
Aliases: A5 n4 spatial certificate reduction; complete compatible-sign trees; exact edge gap sampling.
Split from: verification obligations(3)–(5) of programme A5 for the n4 implementation.
Split into: none; actual count verification is a separate result.

## Statement

For the degree-four Padua cardinals specified in theory08, a finite certificate satisfying every predicate of `../code/a5_n4_schema.md` has exactly as many strict local maxima in the square interior as its distinct accepted interior-root ids. If its edge and corner certificates also satisfy the predicates stated below, then its number of strict relative local maxima on the closed square is the sum of the distinct interior-, edge- and corner-root ids.

This is a correctness theorem for **every finite certificate meeting the stated exact predicates**, not an assertion that a particular producer run passed the independent checker. A partial tree or an unresolved case is not accepted.

## Definitions

Let P_s=Σs_iL_i, A_s=(P_s)_x, B_s=(P_s)_y and H_s its physical Hessian. Root boxes and all other boxes are rational closed rectangles; interval operations enclose exact real values. A complete binary tree partitions [-1,1]² by splitting the widest side at its midpoint, breaking ties in x. A finite prefix-free set of binary leaf paths is complete when it covers both child subtrees at every internal path, ending at the empty root path.

On an edge, write r_i(t)=L_i|edge, E=sf(∏r_i), and q_s=Σs_ir_i. This certificate version requires every r_i nonzero as a polynomial and requires E to divide the product of all irreducible factors having multiplicity exactly1 in at least one r_i. For nonconstant q_s set D_s=q_s' and D_r=sf(D_s)/gcd(sf(D_s),E).

## Assumptions

The checker reconstructs the exact cardinals independently; verifies arithmetic enclosure, complete tree/sign lists, all algebraic identities and all root predicates; verifies complete supplied rational norm-root partitions by Sturm counts, including singleton rational roots; and rejects every unresolved case. Distinct accepted root boxes on the same stratum are disjoint. No assumption is made that the producer always terminates or that all quartic maxima have nonsingular Hessians.

## Status by part

Overall status: **PROVED** (analytic verification implication; required Claude audit pending).

| Mathematical part | Status | Evidence |
|---|---|---|
| spatial tree and universal sign-mask exclusions exhaust interior strict maxima | PROVED | comparison, compact finite partition and injectivity arguments below |
| finite edge arrangement masks and derivative-root dispositions exhaust open-edge strict maxima | PROVED | exact gap sampling and multiplicity-one crease cover below |
| root and corner witnesses give the claimed distinct strict maxima | PROVED | Krawczyk / local calculus and disjointness below |

The actual n4 count remains OPEN until full computational obligations and separate execution are recorded. This theorem has no measured count as a part.

## Depends on

The every-active-polynomial principle and regular-crease exclusion proved in `PD-T?proof-attempts-2-codex-08`; elementary interval mean-value bounds; the contraction mapping theorem / Krawczyk fixed-point argument; exact univariate Sturm root counting. No part1 result is used.

## Checks

Proposed producer: `../code/a5_n4_boxes.py`, `a5_n4_boundary.py`. Independent checker is separately owned `a5_checker_n4.py` and imports neither producer. Actual executions and hashes belong in the count/verification record; diagnostic computations do not prove this theorem. Runs needed: independent review of this implication and actual full certificate checks.

## Sources

Same pinned programme A5 and gate as theory08. This is proof completion of a registered target; no priority or novelty claim. The source MEASURED counts are not assumptions.

## Proof or evidence

### Interior coverage and verified exclusions

Every interior strict λ maximum is a strict P_s maximum for every pattern active there, by theory08. The finite complete binary tree covers its point z. A strictly positive interval lower bound for L_i forces sign+; a strictly negative upper bound forces sign−; an interval containing0 allows both. Consequently each pattern active at z occurs in the complete compatible-mask list of the containing leaf.

For each such mask, `flat` excludes strict P_s maximality because P_s is independent of a coordinate. `gradient` excludes stationarity. A positive H_xx or H_yy supplies an ascending second derivative, and det H<0 makes H indefinite; these `hessian` tests exclude a local P_s maximum. These inequalities are strict: det H=0 or H_xx=0 alone does not exclude a quartic maximum.

For `factor`, exact identities A=Ga and B=Gb and a nonzero residual component on the box imply every stationary point lies on G=0. A nonzero partial of its squarefree part F throughout the box makes every such point regular on F=0. Theory08's implicit-curve argument excludes strict P_s maxima there. No isolated-real factor zero passes this predicate.

For `regular_point`, the exact point p is stationary and is either a node (λ(p)=1≤λ everywhere, from sum L_i=1) or has a vanishing cardinal with nonzero gradient (excluded by theory08). The record supplies a convex rational rectangle U containing both the leaf Q and p, and fixed rational C with ||I−C H_s(U)||_infinity<1. For any distinct v,w in U, the segment integral gives

C(∇P_s(v)−∇P_s(w))=(I−E)(v−w), with ||E||_infinity<1.

Thus equal gradients force v=w: ∇P_s is injective on U. All stationary points in Q equal the excluded p. Mere intersection of Q with a node or crease is never sufficient.

For `root`, the referenced root record supplies R strictly inside the square, a Krawczyk inclusion and contraction, negative definite H_s throughout R, and strictly positive s_iL_i throughout R. As detailed next, this proves a unique strict λ maximum p in R. An additional injectivity witness on U containing both R and Q shows every stationary point in Q is p. Therefore any interior λ strict maximum survives only under a root id, and is exactly that certified point. Every certified root is itself a strict maximum. Pairwise disjoint R boxes prove distinctness of different ids, while repeated leaf references count only once.

### Root witness

Let c be the rational midpoint of R and C the fixed rational matrix. The map T(v)=v−C∇P_s(v) has derivative I−C H_s(v). The supplied interval Krawczyk set

c−C∇P_s(c)+(I−C H_s(R))(R−c)

contains T(R), lies strictly inside R, and its derivative norm is below1. Banach's theorem gives a unique fixed point p∈R. The norm inequality makes C H_s(c) invertible, hence C invertible; T(p)=p therefore gives ∇P_s(p)=0. Negative definiteness implies a strict P_s maximum at p, and all cardinal signs are fixed on R, so λ=P_s there. A rational Newton midpoint may select candidate data, but acceptance depends only on these verified inequalities. A failed iteration supplies no exclusion.

### All edge sign patterns from exact gaps

The exact multiplicity-one cover implies every real root of E is a simple zero of at least one r_i. Indeed any root belongs to some irreducible factor of E, which divides a multiplicity-one factor of some r_i; characteristic zero makes that factor separable. At each such root the corresponding r_i' is nonzero. Theory08 excludes every such point as an open-edge λ maximum, even at crossings.

A complete norm-root partition for E gives ordered pairwise-disjoint rational intervals, each containing one distinct real root of the norm, and accounting for every real norm root on the line. Every real chosen-embedding root of E is among them. Take one rational sample before the first interval, in every gap between consecutive intervals, and after the last interval. Each connected interval of R\{E=0} contains at least one of these samples: the extra norm roots only subdivide a component, while any consecutive actual roots are separated by a nonempty supplied gap. Thus the distinct exact sample sign masks contain every sign pattern of the edge away from E=0. This remains true when a root interval is a rational singleton. Samples lie outside all norm-root intervals, so no r_i vanishes there.

For each sampled mask, a constant q_s cannot have a strict tangent maximum. For nonconstant q_s every strict tangent maximum has D_s=0. Roots shared with E have already been excluded; all remaining distinct roots satisfy D_r=0. Complete norm-root intervals for D_r therefore cover every candidate, including repeated roots of D_s and conjugate-embedding extras. A pair is excluded only by: being outside the open edge; an interval D_r excluding0; an incompatible signed r_i; or strictly positive q_s''. Each exclusion is a valid necessary-condition failure. A quartic root with q_s''=0 is not discarded by this list and must receive a separately proved disposition or remain unresolved.

For an accepted simple `root` witness, its larger rational interval U contains the supplied norm-root interval, lies strictly inside the open edge, has all signs strict, q_s''<0, and endpoint D_s signs + then−. The intermediate value theorem gives a root, while q_s''<0 makes it unique. Strictly negative inward derivative of the full signed P_s on U proves strict relative maximality on the square: near the point, inward displacement strictly decreases P_s, while tangent displacement has a strict one-variable maximum. All cardinals are nonzero there, so the same P_s represents λ in a full relative neighbourhood. Strictly positive inward derivative instead gives an ascending feasible direction (`normal`) and excludes it. A zero inward derivative is not decided by this schema. Disjoint accepted intervals on an edge prove distinctness; different edges are disjoint strata.

### Corners

Exact node corners are excluded by λ≥1=λ(node). At every remaining accepted corner, nonzero cardinal signs are fixed and all choices for zero-cardinal signs are explicitly enumerated. Each corresponding active P_s has both exact inward partial derivatives strictly negative. Continuity and finiteness give a common small corner neighbourhood in which all these P_s decrease along every nonzero inward segment. Their finite maximum is λ there. Thus that corner is a strict relative maximum. The interior, open edges and corners exhaust S. ∎

## Scope

This is a mathematical soundness and completeness implication for an accepted finite certificate. It permits exact singular-Hessian or boundary-degenerate extensions only when their local arguments are written explicitly. It does not claim generic nonsingularity, automatic termination, a global value comparison or an executed count.

## Open items

Independent mathematical review and complete n4 producer/checker/different-agent rerun. The optional A4(d) statement must separately bound non-strict global maxima; it is not inferred from a strict-count certificate alone.

## History

2026-11-01, Codex `/root/a5_n4`, inherited gpt-6.1-sol xhigh; rules at95ca473cc21b2db6a9a46c62e86495ebe94eb397. Split from actual count evidence to preserve its correct OPEN status until independent verification.
