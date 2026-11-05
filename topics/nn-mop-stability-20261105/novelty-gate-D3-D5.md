# D3/D5 gate — direct native formulations and joint backward geometry

2026-11-05, Codex developer, requested gpt-6.1-sol xhigh. Source/rules
`823cf6a4ef7c01b4ef3d2a6fec3e9f19d4b4f6f1`; base
`b4d292eea5eed373002506d5e16a3761bd7ae10e`. No Git authority.

## Gate before experiments

Read AGENTS, WORKFLOW, CODEX, handoff01 and the pre-existing plan. Scanned
the complete 1016-line IDEAS registry's headings, aliases and candidate
summaries, including historical and current obstruction/disposition tables.
Raw chunk reads were supplemented by filtered heading/alias/table scans;
truncated long output was repaired in bounded chunks. Shortlisted full
entries: IDEA-031, 034, 085/090/111/117, 156–164, 172, 193/194/197 and
376–379, with the complete four predecessor candidate records and gate.
Searched nearest-neighbour, mixed moments, biorthogonality, compatibility,
orthogonal basis, modified Chebyshev, backward manifold and projection.

Read predecessor report, theory records (all), baseline, exact runs, code,
literature and source recheck, audits01/02 and response01. Consulted the
required PROOF_STATUS rows and targeted INDEX rows LIT-119/347/348/562–568,
and the SINUM assessment. These are repository records of other readers'
primary reading. This worker has not freshly read the primary papers and
makes no new source assertion or novelty claim.

## Consequences and shortlist

| Predecessor / obstruction | Consequence |
|---|---|
| IDEA-376 / PD-T286 direct mixed moments | Changing polynomial basis or using QR/SVD is a known reformulation. A numerical advantage is an implementation result, not automatically a new algorithm. |
| IDEA-379 / PD-T289 FHV reconstruction | Native direct solves avoid layer propagation but do not improve exact solvability. |
| LIT-347 assessment: moment and reorthogonalized Krylov formulations | A whole-triangle solve needs primary comparison to §4.4 before any algorithmic novelty claim. |
| IDEA-378 deferred coupled updater | Neither direct solve nor a projection is called a node updater; no invariant is invented retrospectively. |
| IDEA-193/194 measure modification / modified Chebyshev | Orthogonal-basis language alone supplies no separation from existing methods. |
| PD-N100 | Both lattice directions use one spectral variable. No commuting bivariate interpretation is used. |
| IDEAS backward/cubature obstruction tables | A small compatibility or path residual is not full-data backward error. The compatible manifold below is the actual image of positive, normalized, common-support data. |
| Finite rank / positivity restrictions | Assume normality through degree N; degree-N polynomials coincide; degree N+1 systems need not be normal. Positive proportional measures are excluded. |

## Pre-registered designs and tests

1. **A, direct orthobasis mixed systems.** For every index solve its mixed
   orthogonality equations in a common uniform discrete orthonormal basis;
   extract NN coefficients by multiplication and both predecessor relations.
   LU, pivoted QR and untruncated SVD variants are retained. Kill a variant
   under inherited G4 if it is worse than frozen C4 at N16 on both families.
2. **B, node-value constrained nullspace.** At each index QR-reorthogonalize
   the constraint vectors in node space, intersect their nullspace with the
   degree-|nu| polynomial evaluation subspace, fix the monic gauge, and
   extract both recurrence relations. This is algebraically equivalent to A
   but a distinct factorization; defer implementation if A's cheap test
   settles the limited first-round question. No equivalence implies a new
   PD-N. Resume if factorization error dominates A's conditioning.
3. **C, full-data compatibility projection.** Minimize coefficient distance
   over the actual normalized positive common-node input image. Prove its
   local manifold/nearest-point meaning first. A path inverse alone fails
   its acceptance test. Global nonlinear numerical projection remains a
   separate implementation obligation.

First tests use both frozen families, N4/8/12/16, then24/32 if cheap, exact
rational input identities and 140/220-digit frozen references. Report all
variants including losses. G4 accuracy needs matching D1 kappa*u<=1e-4 and
two-digit gain plus a stated backward measurement. No stability theorem
follows from these finite measurements.

## Round2 authorized continuation

After round1 publication at929ef787c74afc2bedcc8327d44dddc2c3409f46,
coordinator authorized C's high-precision full-Jacobian fits at N4/8 both
families. No new mechanism or literature novelty claim was introduced.
Candidate C now has measured stationary fits and exact rational positive
common-data witnesses. Full-array corrections and input perturbations are
reported separately; no raw strict backward metric substitution and no
certified nearest-minimum claim. N4 passes the dated finite mixed100u
test for LU/nodeqr; N8 does not. These dispositions are retained in
the complete candidate memory and D5, with failed precision-limited
iterations preserved. A uniform algorithmic stability theorem is OPEN.
