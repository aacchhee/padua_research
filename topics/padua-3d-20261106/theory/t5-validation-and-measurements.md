# T5 validation and exact computational receipt

This is a verification record, not a new mechanism or a claim of historical
priority. The exact ranks and bound have their hand proof in T5-02. The
separate auxiliary numerical table below has provisional ID
**PD-T?padua-3d-20261106-codex-T5-04**, ID kind PD-T, status MEASURED pending actual
independent replay. Aliases: exact uncompleted-section norm census.
Split from: none. Split into: none.

## Statement and assumptions

For normalized product arcsine measure, the executed exact checker validates
the listed positive degree-five rules and records the listed uncompleted
section commutator norms/image dimensions for d=2,3 and q<=4. All polynomials
are of total degree. Nothing here minimizes a completed commutator norm.

## Status by part

D4 pipeline gate: PASS. Actual exact execution precedes the support
obstruction run. Exact rule validity also admits the short hand checks
below. The auxiliary finite computational census is MEASURED until the
independent actual replay; its observations do not serve as proof premises
for either T5-02 or T5-03.

## Checks and evidence

Executed command from repository root:

```
python topics/padua-3d-20261106/code/t5_exact.py --output topics/padua-3d-20261106/evidence/t5-exact.json
```

Python 3.12.14, SymPy 1.14.0; no random seed or float arithmetic.
The JSON carries the executing code's SHA-256. It records all 21 monomials
in 2D through degree five and all 56 in 3D for each rule; every residual
was exactly zero and every weight strictly positive.

| Existence control | Dimension | Nodes | Exactness checked |
|---|---|---|---|
| Three-point Gaussian product | 2 | 9 | Degree 5 |
| Three-point Gaussian product | 3 | 27 | Degree 5 |
| Axis-plus-cube symmetric rule | 3 | 14 | Degree 5 |
| Same-parity m=3 Lobatto union | 3 | 16 | Degree 5 |

The first two are the known product Gauss–Chebyshev rules required by D4.
The 14-node rule is an explicit independent moment reconstruction, without
a novelty claim or a currently verified historical attribution. It is an
off-grid counter-control to any universal reading of T5-03.

## Hand verification of the existence controls

The one-dimensional three-point rule has nodes `0,+/-sqrt(3)/2` and weights
`1/3`; its moments 0 through 5 are `1,0,1/2,0,3/8,0` as shown in T5-03.
Its products are exact on the larger coordinate-degree box and hence on
total degree five in either dimension.

The 14-node cube rule has six axis nodes `+/-sqrt(7/8) e_i`, each of weight
`4/49`, and eight cube nodes `(sign_1,sign_2,sign_3)*sqrt(7/10)`, each of
weight `25/392`. Every node lies in the cube. Independent coordinate-sign
invariance kills every monomial with an odd exponent, while permutation
invariance reduces the even total-degree-five moments to `1,x^2,x^4,x^2y^2`.
Their sums are, respectively,

`24/49+25/49=1`,

`2(4/49)(7/8)+8(25/392)(7/10)=1/2`,

`2(4/49)(7/8)^2+8(25/392)(7/10)^2=3/8`,

`8(25/392)(7/10)^2=1/4`.

For the 16-node control, take the four one-dimensional nodes
`x_i=(1,1/2,-1/2,-1)`, with weights `v_i=(1/6,1/3,1/3,1/6)`.
This full one-dimensional rule has the same six required moments.
Select triples with all indices of the same parity and assign weight
`4 v_i v_j v_k`. Put `s_i=(-1)^i`. The selection factor is
`4*1_(same parity)=1+s_i s_j+s_i s_k+s_j s_k`.
The alternating moments `sum_i v_i s_i x_i^a` vanish for `a=0,1,2`
by direct substitution. In each correction term two coordinates carry
these factors, so a nonzero correction needs degree at least `3+3=6`.
Every degree-five monomial therefore has exactly the full product-rule
moment. Positivity and sixteen distinct nodes are immediate.

## Auxiliary finite measurements

Here `F^2` is the squared Frobenius norm in the orthonormal Chebyshev basis,
the same for each coordinate pair, and `J` is the dimension of the sum
of all pair-commutator images. The code computes in the unnormalized tensor
`T` basis with exact diagonal Gram G, checking `G A=A^T G`. It evaluates
the orthonormal norm by `sum_(a,b) G_aa/G_bb * C_ab^2`.

| d | q | Pair rank | F^2 | J | Standard node lower bound |
|---|---|---|---|---|---|
| 2 | 0 | 0 | 0 | 0 | 1 |
| 2 | 1 | 2 | 1/2 | 2 | 4 |
| 2 | 2 | 2 | 1/2 | 2 | 7 |
| 2 | 3 | 4 | 5/8 | 4 | 12 |
| 2 | 4 | 4 | 3/4 | 4 | 17 |
| 3 | 0 | 0 | 0 | 0 | 1 |
| 3 | 1 | 2 | 1/2 | 3 | 5 |
| 3 | 2 | 4 | 1 | 5 | 12 |
| 3 | 3 | 8 | 13/8 | 10 | 24 |
| 3 | 4 | 12 | 19/8 | 14 | 41 |

No extension lower bound is inferred from J. The pair-rank bound is only
the known DST/Möller mechanism, and no new lower-bound strength is claimed.

## Deferred completed-section minimization

No completed-section norm minimization was executed. In an orthonormal
graded basis its natural model would extend each fixed section to
`[[A_i,B_i],[B_i^T,D_i]]`, constrain B_i to have zero rows below the top
degree, and minimize a sum of squared commutator norms over B_i and
symmetric D_i at a prescribed surplus. A nonzero local least-squares
residual proves no emptiness statement; even rank-bound attainability
would require the bottom-block and compatibility equations. This distinct
nonlinear task is deferred because the exact finite-support classification
already supplies a complete bounded result. There is no claim of
equivalence between the rank census and completion minimization.

## Sources, scope and open items

Predecessor context and reading limits are in `../literature-T5.md` and
`../novelty-gate-T5.md`. No primary-source theorem is imported here.
Independent replay and Claude audit remain pending. The universal minimal
cubature and 3D Padua targets remain OPEN.

## History

2026-11-06, Codex gpt-6.1-sol xhigh, rules at
`ccd9e905d19c0c625c196c4a3f3e707058ed042a`: actual exact validation and
census, explicit distinction from the unexecuted completion optimization.


## Audit-response attribution and deferral addendum — 2026-11-06

The same-parity four-level Lobatto 16-node D4 control above is the
De Marchi–Vianello–Xu 2009 construction (LIT-306/322), arXiv:0805.3529,
§3, eqs.(17)–(19), specialized to this small parameter. Its exact hand
moment verification is local; the construction is attributed, with the
source reading limits in ../literature-T5.md. Audit-01 independently reran
the exact controls and section census; the census remains MEASURED, and
all earlier process-pending prose is historical.

The handoff-assigned completed-section n<=4 minimization was **not executed**.
Its separate IDEA?padua-3d-20261106-codex-T5-completion record and resume condition
are in ../candidates-deferred-response-01.md. This is a disclosed scope
deviation for AC in ../response-deviations-01.md, not equivalent work
completed by the uncompleted-section census. No optimizer result is claimed.


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
