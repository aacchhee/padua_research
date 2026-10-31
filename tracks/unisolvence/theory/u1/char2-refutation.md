# PD-N001 — Characteristic-two refutation of the supplied quasi-definiteness iff

ID kind: PD-N. Aliases: U1a refutation; loss of parity in alternation weights.
Split from: supplied U1a conjecture, unchanged scope: for every field and every m, a labelled checkerboard S_e(X,Y) is unisolvent iff both alternation functionals have all leading Hankel minors of orders 1,…,|H|−1 nonzero.
Split into: odd-characteristic restriction in `odd-characteristic-criterion.md`; corrected all-characteristic statement in `all-characteristic-criterion.md`.

## Statement

The quoted arbitrary-field iff is false, for m=1 over F4 and also for m=2 over F8, both parity choices. More generally, for m=1 over every field with at least three elements both checkerboards are unisolvent for Π_1; in characteristic 2 the required first minor for X is zero.

## Definitions and assumptions

Let K have characteristic 2 and an element a∉{0,1}, e.g. K=F_2[a]/(a²+a+1). Take X=(0,1), Y=(0,1,a). Distinctness within both axes holds; shared axis coordinates are allowed by the original conjecture. Use alternation weights and cutoff exactly as in the supplied statement, with no normalization change.

## Status by part

Overall status: PROVED (elementary explicit proof; supplementary Astra check complete; Claude audit-01 accepted the mathematics).
Candidate / claim disposition: REJECTED: refuted, for the exact arbitrary-field iff. The characteristic≠2 restriction is a separately preserved result, not a silent narrowing.

## Negative-result scope

Attempted mechanism: infer checkerboard unisolvence exactly from finite-support alternation quasi-definiteness, U1a.
Parameter range covered by refutation: characteristic 2, m=1, any distinct X of length 2 and Y of length 3; explicit F4 example and explicit m=2 F8 example below. An additional m=0 edge is recorded but not needed.

## Proof

For S_0 the three nodes are (0,0),(0,a),(1,1). In columns (1,x,y), the evaluation determinant is a, nonzero. For S_1 the nodes are (0,1),(1,0),(1,a); its determinant is also a in characteristic 2. Equivalently, any affine linear polynomial vanishing at the two distinct y-values in one vertical line has zero y-coefficient, and the remaining two distinct x-values force both other coefficients to vanish. This latter proof works for all fields and all labelled lists of lengths 2 and 3.

But in characteristic 2, (-1)^i=1. The first alternation moment of any support of length L≥2 is the ordinary barycentric sum Σ1/ω′(h_i)=0, by the leading-coefficient Lagrange identity. In particular Δ_1(X)=0, while its prescribed cutoff includes r=1. Thus both boards are unisolvent and the proposed necessary condition fails.

For an example inside the supplied script's m≥2 range, take K=F2[a]/(a³+a+1), X=(0,1,a), Y=(0,1,a,a²), m=2. In the checker's bit encoding these are X=[0,1,2], Y=[0,1,2,4], modulus 0b1011; the encoding b0+2b1+4b2 represents b0+b1a+b2a². In graded columns (1,x,y,x²,xy,y²) and lexicographic (i,j) row order, the exact determinants are a²+a (encoding 6) for e=0 and a² (encoding 4) for e=1, both nonzero, while Δ1(X)=0. These determinants can be verified by ordinary Gaussian elimination in this explicitly presented field; the committed checker performs that exact arithmetic. Equivalently the fully symbolic m=2 determinant factorizations in directions/U1/symbolic-factors.md specialize directly to these nonzero values.

If m=0 is included, X has one entry and each board is a single point, always unisolvent for constants; Y has two entries and Δ_1(Y)=0 in characteristic 2. This independently refutes that edge. No assertion of universal singularity in characteristic 2 follows.

## Depends on / checks / sources

No imported mathematical dependency. Exact F4 implementation and both determinants are included in directions/U1/exact_checker.py; actual run identity and evidence are recorded separately. Closest source is the supplied `finite_field_padua.md` conjecture and hs_ff.py; their odd-prime sampling does not cover characteristic 2. Harris–Simanek ordered-real result is not contradicted.

## Scope and open items

This refutes necessity in the exact arbitrary-field claim. Its sufficiency direction remains true over every field: it is proved in characteristic≠2 in the separate theorem, and in characteristic 2 its antecedent is false because Y has length≥2 and Δ1(Y)=0. It does not refute a criterion using divided-alternation/even-index barycentric moments. Supplementary Astra reconstruction complete; Claude audit-01 accepted the mathematics.

## History

2026-10-31, Codex `gpt-6.1-sol` xhigh, rules/base d36722823441dc40c6e19d69a174459348dd309c. Original field scope preserved explicitly on refutation.

2026-10-31, Codex response-01 A2: updated completed handoff references and Claude audit-01 acceptance metadata only; mathematical statements, proofs and epistemic statuses unchanged.
