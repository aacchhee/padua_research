# PD-T?proof-attempts-2-codex-18 — Degree-independent spatial certificate with exact node cones

ID kind: PD-T.
Aliases: A5 complete compatible-sign trees; algebraic edge arrangements; node-cone certificate extension.
Split from: verification obligations(1),(3)–(5) of programme A5 for the degree-five extension.
Split into: actual degree-five count and global value are separate results16 and17.

## Statement

Let L_0,…,L_{N−1} be polynomial cardinals for a finite interpolation set in S=[−1,1]², with ΣL_i=1, and let λ=Σ|L_i|. The polynomial degrees are arbitrary finite integers. Suppose an exact finite certificate satisfies all the predicates below, interpreted in a specified real embedding of a finite algebraic coefficient field K overQ. Then its number of strict relative local maxima on S equals the sum of its distinct accepted interior, open-edge and corner root IDs.

The interior certificate is a complete finite binary rectangle partition with either every compatible sign pattern disposed of by a stated valid predicate, or a valid whole-leaf node-cone witness from result15. Every edge has complete algebraic arrangement and derivative-root coverage, with every candidate disposed of. The four corners are checked exactly. Unresolved records, missing masks, incomplete partitions and unproved zero-curvature/boundary cases are rejected.

This is a mathematical implication for every certificate satisfying these predicates, not an execution claim. In particular it extends the explicitly n4-scoped result09 to degreefive without assuming that singular Hessians or degenerate tangent maxima can be discarded.

## Definitions

A sign mask s∈{−1,1}^N defines P_s=Σs_iL_i, A_s=(P_s)_x, B_s=(P_s)_y and H_s=HessP_s. A pattern is active at z if s_iL_i(z)=|L_i(z)| for every i. A closed rational rectangle has an inclusion-preserving polynomial interval evaluation. Its compatible masks assign the forced sign where a cardinal interval is strictly positive/negative and permit both signs when its interval contains0.

A complete tree splits the widest side at the exact midpoint, choosing x on ties. Its finite prefix-free leaf paths cover both child subtrees of every internal path and the whole root[-1,1]². On an open edge write r_i=L_i|edge. This boundary version requires every r_i to be a nonzero polynomial and every root of E=sf(∏r_i) to be a simple zero of at least one r_i, verified by the exact multiplicity-one-factor cover. For nonconstant q_s=Σs_ir_i set D_s=q_s' and D_r=sf(D_s)/gcd(sf(D_s),E).

## Assumptions

A finite algebraic coefficient field K/Q with specified real embedding, exact algebra, rational norm-polynomial Sturm counts or another proved complete root-partition verifier, inclusion-preserving intervals, and all complete mask/candidate lists. Distinct accepted root boxes/intervals on the same stratum are disjoint and have unique IDs. All referenced node cones meet result15's complete gap, geometry and strict-containment hypotheses. A specific implementation must reconstruct its board and cardinals independently in its checker.

## Status by part

Overall status: **PROVED** (written verification implication; required Claude audit pending).

| Part | Status | Evidence |
|---|---|---|
| exhaustive interior tree, all-mask predicates and node leaves | PROVED | active-polynomial comparison and result15 |
| complete exact edge arrangements and derivative candidates | PROVED | regular zeros, field norms, Sturm partitions and gap samples |
| accepted witnesses count exactly distinct strict maxima | PROVED | contraction, local calculus and disjointness |

The degree-five finite case is now separately PROVED under result16 after complete artifact and independent checks. This generic supporting theorem alone would not certify another finite case.

## Depends on

Result15 for the new node-cone exclusion. The elementary every-active-polynomial and regular-crease arguments, repeated below, hold in every degree. Contraction mapping and exact univariate Sturm root counting are used. Result09 is the predecessor implementation proof, not an inherited statement for all degrees. No cubic or quartic Taylor truncation is used.

## Checks

Degree-five serialization is `../code/a5_n5_schema.md`; new producer modules are `a5_n5_boxes.py`, `a5_n5_nodes.py`, `a5_n5_boundary.py`. Separate independently owned checker is `a5_checker_n5.py`. Actual computations and independent runs belong to result16. This theorem requires no claimed unexecuted run.

## Sources

Programme IDEA17/source06 and A5 at9bd14a6d2c4da69139a10107d8a787f2be0c5c9e; target gate in T-A5-n5.md. Same registered proof-completion target, with no novelty or priority claim. This explicitly records the changed degree scope instead of silently applying n4-scoped result09 to degreefive.

## Proof or evidence

### Active polynomials and interior coverage

Pointwise λ=max_sP_s. If λ has a strict relative maximum at z, every active P_s does too: P_s(w)≤λ(w)<λ(z)=P_s(z) locally for w≠z. At an interior maximum its gradient vanishes and Hessian is negative semidefinite. If a zero cardinal has nonzero gradient, flipping its active sign would change the stationary gradient by2∇L_i, impossible. Such regular creases and any crossings containing one are excluded exactly. The edge version uses tangential derivatives and the same comparison.

Take any interior strict maximum and any leaf containing it. Cardinal interval inclusion guarantees that every active mask occurs among that leaf's compatible masks. A valid node-cone leaf contains no strict maximum by result15. In an ordinary leaf, the following exhaustive predicates are sound:

- `flat`: one physical derivative of P_s is identicallyzero, so P_s is constant on a coordinate line and cannot have a strict interior maximum.
- `gradient`: one derivative interval excludes0, so no stationary point occurs there.
- `hessian`: H_xx or H_yy has strictlypositive lower bound, or detH has strictlynegative upper bound. These contradict negative semidefiniteness. Equality is never an exclusion, in any degree.
- `regular_point`: an exact point p is stationary and is either a node or a regular zero-cardinal point. A supplied convex rectangle U contains both the entire leaf Q and p, with ||I−C H_s(U)||∞<1 for rational C. Integrating along a segment makes ∇P_s injective on U, so every stationary candidate in Q equals the excluded p. A node is excluded because λ≥1=λ(p); an interior regular zero is excluded by the active-sign argument. If p is on the square boundary, equality with p already excludes an interior candidate, so no inappropriate full-gradient condition is imposed on a relative boundary maximum.
- `factor`: exact identities A=Ga,B=Gb, a nonzero residual component throughout Q, and a nonzero partial of F=sf(G) throughout Q imply every stationary point lies on the regular curve F=0. The implicit function theorem gives a local curve through each point, and ∇P_s=0 along it makes P_s constant there. Thus P_s cannot have a strict maximum. Singular or isolated real factor zeros fail this predicate and remain unresolved.
- `root`: a referenced accepted root box R has a certified unique smooth strict λ maximum p, and a supplied convex U containing Q and R has the same gradient injectivity test. Every stationary point in Q is p. Every possible strict maximum in the leaf is therefore the referenced root.

This list makes no nonsingular-Hessian assumption about an unclassified point. A case which does not satisfy a predicate remains unresolved rather than discarded.

### Root witnesses and distinct IDs

For an accepted root box R strictly inside S, let c be its rational midpoint and C a fixed rational matrix. The exact Krawczyk enclosure

c−C∇P_s(c)+(I−C H_s(R))(R−c)

contains T(R) for T(v)=v−C∇P_s(v). Require strict inclusion in R and ||I−C H_s(R)||∞<1. The contraction argument yields a unique fixed point in R. The norm bound makes C nonsingular, so the fixed point is a gradient zero. Require also H_xx(R)<0, detH(R)>0 and strictly positive s_iL_i throughout R. These prove negative definiteness and λ=P_s there, hence a strict λ maximum. An exactly supplied stationary point may replace Krawczyk existence only if its exact coordinates are verified to lie strictly inside R and the same whole-box injectivity and strictness predicates are verified.

Each accepted ID is a real strict maximum, independently of where its first referencing leaf lies. Conversely every strict maximum survives only as a referenced root ID by complete leaf/mask coverage. Pairwise disjoint root boxes prove that different IDs are distinct; repeated references to one ID count it once. The hull test covers the entire leaf and root box, never just a Newton seed or an outside iterate.

### Complete boundary sign patterns and roots

Every real zero of E is a simple zero of at least one restricted cardinal by the verified multiplicity-one cover and characteristic-zero separability. Its tangent derivative is nonzero, so the active-sign argument excludes that edge point, including crossings.

A complete rational partition of all distinct real roots of the squarefree norm of E includes every root in the chosen embedding. The checker verifies one root per supplied interval, exact singleton roots, ordered disjointness and equality with the total Sturm count. A rational sample before the first interval, in each consecutive gap and after the last interval supplies all actual edge sign patterns away from E=0. Extra conjugate norm roots merely subdivide actual components. Each component between consecutive actual E zeros contains one of these samples, and samples are outside every norm-root interval, so no sampled cardinal vanishes.

For every distinct sampled mask, a constant q_s cannot have a strict tangential maximum. Otherwise every strict tangent maximum solves D_s=0. Shared roots with E have already been excluded; every remaining distinct candidate is a zero of D_r. Complete supplied norm-root partitions for D_r therefore cover all candidates, including repeated derivative roots and conjugate extras. A candidate may be excluded only if it is outside the open edge, the chosen-embedding D_r interval excludes0, a signed cardinal is strictly incompatible, or q_s'' has a strictlypositive lower bound. A zero second derivative is not discarded merely because it is zero.

An accepted boundary root has a larger interval U containing the candidate interval and strictly inside the edge. Require all cardinal signs strict on U, q_s''<0 on U, and D_s(U_lo)>0>D_s(U_hi). This proves exactly one tangential critical point and a strict tangent maximum. If the physical inward derivative of the corresponding full P_s is strictlynegative there, continuity proves strict relative maximality: inward displacement decreases P_s and tangent displacement has a strict maximum. Strictlypositive inward derivative instead excludes maximality. A zero normal derivative or degenerate tangent case stays unresolved until an explicit additional proof is supplied. Disjoint accepted intervals give distinct IDs on each edge, and different open edges are disjoint strata.

### Corners and complete count

At an exact node corner, λ=1≤λ everywhere, excluding strict maximality. At an accepted non-node corner, all nonzero cardinal signs are fixed and every choice of signs for the zero cardinals is enumerated. Each active signed polynomial must have both exact inward partial derivatives strictlynegative. Continuity and finiteness give one neighbourhood where all these polynomials decrease along every nonzero inward segment. Their finite maximum is λ there, proving a strict relative corner maximum.

The interior, four open edges and four corners exhaust S. Every accepted witness is a distinct strict maximum, and complete coverage excludes all other possibilities. Their ID count is therefore exactly the strict-local-maxima count. ∎

## Scope

A generic correctness implication for accepted finite certificates, including node-cone leaves. It asserts neither automatic termination nor any unexecuted degree-five count. Global argmax conclusions require separate treatment of non-strict maxima and value bounds. Identicallyzero edge-cardinal families require a separately stated extension; they are not assumed away for a new degree without exact checking.

## Open items

The degree-five application is complete under result16, with separate exact global evidence in result17. Further degrees require their own complete artifacts and independent executions. Required Claude audit remains PENDING.

## History

2026-11-01, Codex `/root/a5_develop`, allocated gpt-6.1-sol xhigh; rules44be0080c69495cc6959e3d4c2b602fa73678d76. Written before accepting a degree-five count. Extends the mathematical predicate scope of result09 explicitly and adds result15's new exact node-cone leaf; frozen n3/n4 files are untouched.
