# PD-T?charter-u0audit-codex-01 — Upper bounds for two linear-code parameters over F_7

Rules/base d36722823441dc40c6e19d69a174459348dd309c. Independent U0 checker; 2026-10-31. This is a complete hand proof of two universal upper bounds for **linear** codes over F_7. It does not upgrade the finite computation of the Padua code distances. No new mechanism or novelty is claimed; projective arcs, duality and shortening are standard coding-theory arguments. This verification note supplies an explicit alternative to relying on an uninspected Ball theorem. The provisional result ID is assigned here at the orchestrator’s explicit request; final allocation and integration belong to the orchestrator.


ID kind: PD-T. Aliases: q7 Padua code optimality bounds; elementary projective arc exclusion.
Split from: supplied finite_field_padua.md §4 optimality assertions; achieved distances remain separately MEASURED in producer code-distances.md.
Split into: none.

## Statement

Every linear length-ten code C over F_7 with dimension three satisfies d(C)<=7. Every such code with dimension six satisfies d(C)<=4. Thus any linear codes attaining the respective distances seven and four are optimal among linear codes with the same length and dimension. The attainment assertion for the Padua codes is not part of this theorem.

## Definitions and assumptions

A linear [N,K] code is a K-dimensional subspace of F_q^N. Its minimum distance is the minimum Hamming weight of a nonzero element. The dual uses the ordinary coordinate dot product. Shortening at a coordinate restricts to codewords zero there and deletes that coordinate. PG(2,q) consists of one-dimensional subspaces of F_q^3; its lines are two-dimensional subspaces. An arc is a point set with no three collinear. Only q=7 and the two dimensions above are asserted.

## Status by part

Overall status: **PROVED**, by the complete elementary proofs below. This proof is independent of any execution or literature theorem. The root orchestrator separately read and checked its logic; final Claude cross-agent audit remains pending. Candidate disposition: retained verification of source upper bounds, with no novelty claim.

| Mathematical part | Status | Evidence |
|---|---|---|
| Universal d<=7 for linear [10,3]_7 | PROVED | Bound 1 below |
| Universal d<=4 for linear [10,6]_7 | PROVED | Bound 2 below |

## Depends on

Only elementary vector-space duality, projective point/line counts, and the Singleton argument explicitly proved below. No external result or producer theorem is needed. Producer code-distances.md contains separate MEASURED attainment observations, not a dependency of these upper bounds.

## Checks and sources

The independent script exact_check.py separately executed exact projective enumeration of 57 and 19,608 messages and measured Padua distances 7 and 4. Its code, output identity and execution records are in audit.md and evidence-manifest.json. Those computations are not proofs of the universal upper bounds and are not needed below. The supplied note invokes Griesmer and Ball2012; literature/records/ball-2012.md currently has publisher-abstract coverage only. Neither source theorem is inherited here. Projective arcs, MDS duality and shortening are standard prior mechanisms; this note makes no priority assertion.

## Bound 1: a linear [10,3] code over F_7 has minimum distance at most 7

Let G be a rank-three 3-by-10 generator matrix. If some three columns lie in a subspace of dimension at most two, a nonzero linear functional annihilates those columns. The resulting nonzero codeword has at least three zeros, hence weight at most 7.

Otherwise every three columns are independent. In particular they give ten distinct projective points in PG(2,7), with no three collinear. Fix one of them P. The other nine must lie on nine distinct projective lines through P. But there are exactly eight lines through P: these correspond to the one-dimensional subspaces of the two-dimensional quotient F_7^3/<P>, of which there are (7²-1)/(7-1)=8. Contradiction. Therefore d<=7. A measured [10,3,7]_7 Padua code attains the bound, conditional only on the reported finite parameter computation.

## Bound 2: a linear [10,6] code over F_7 has minimum distance at most 4

Suppose instead C has dimension six and distance at least five. Every six columns of its rank-six generator G are independent: a dependence in column rank would yield a nonzero row functional annihilating six columns, and hence a nonzero codeword of weight at most four. Every smaller subset of columns is independent as well, by extending it to six columns.

The dual D=ker(G) has dimension four. A nonzero vector in D with weight at most six would give a dependence of at most six columns of G, which is impossible. Thus D has distance at least seven. The elementary Singleton bound gives distance at most 10-4+1=7, so equality holds. Here the bound follows because puncturing d-1 positions of a distance-d linear code is injective, whence its dimension is at most its remaining length.

Choose any coordinate position and shorten D there: restrict to codewords zero at that coordinate, then delete it. The coordinate functional is nonzero on D. Otherwise deleting this identically zero position would yield dimension four, length nine and distance at least seven, contradicting Singleton. Therefore the shortened code E has dimension three, length nine and distance at least seven, with equality again by Singleton.

A generator of E has every three columns independent, by the same row-functional argument: otherwise a nonzero codeword would have at least three zero positions and weight at most six. Thus its nine columns are nine distinct points A in PG(2,7), no three collinear.

Through each P in A, the eight other points use all eight lines through P. Consequently there is no tangent line, meaning a line meeting A in exactly one point. There is an external point Q because PG(2,7) has (7³-1)/(7-1)=57 points. The eight lines through Q partition A, and each meets it in zero or two points (no tangents and no three collinear). This would make |A| even, contradicting |A|=9. The contradiction proves d<=4.

A measured [10,6,4]_7 Padua code therefore attains the universal linear-code bound, conditional only on its finite parameter computation. Neither argument asserts optimality among nonlinear codes or transfers unchanged to arbitrary prime powers/dimensions.


## Scope and open items

These are exact universal upper bounds for the stated linear-code parameters. Nonlinear codes and other field sizes/dimensions are outside scope. Attained Padua distances remain MEASURED; their optional packaging as computer-assisted proofs is not required for these upper-bound proofs. The combined source optimality assertion must cite both this bound and its separately scoped attainment evidence. Final cross-agent audit and final-ID allocation remain pending.

## History

2026-10-31: independent Codex U0 checker, requested gpt-6-astra high; actual runtime model/effort metadata not otherwise exposed. Rules/base d36722823441dc40c6e19d69a174459348dd309c. Wrote both elementary arguments independently; root subsequently read the full proof and confirmed its logic. Added the provisional PD-T ID and template fields on root’s explicit request. Original source optimality assertions were split into universal upper bounds here and measured Padua attainment in the producer record; no attainment status was silently upgraded.
