# U1 development plan and rounds

Rules/base: `d36722823441dc40c6e19d69a174459348dd309c`. Assigned developer: Codex, inherited `gpt-6.1-sol` xhigh allocation. No Git operations or shared registry edits. Baseline-ready authorization received from orchestrator before mathematical exploration. All imported results remain reports, not proof dependencies.

Read: AGENTS.md, agents/WORKFLOW.md, agents/codex/CODEX.md, templates/THEORY.md and IDEA.md, state/CURRENT.md, complete state/IDEAS.md (empty), literature/INDEX.md, Harris record, complete baseline-candidates.md, frozen campaign plan, source hs_ff.py and relevant supplied-note passages. Mechanism search: `quasi|hankel|alternation|checkerboard|unisolven|determinant` across theory and topics. No pre-existing theory directory at launch. Step0 override permits exploration; prior-art comparison and independent adversarial reconstruction still precede acceptance. De Marchi–Usevich (2014) and related determinant-factorization overlap is being checked by orchestrator's literature agent.

## Frozen first test

For m=2,3,4, factor checkerboard determinants and compare leading alternation Hankel minors, both parity choices; also inspect m=0,1 and characteristic 2 before any kernel proof. Distinctness is required only within each axis, never across the axes. Indeterminate nodes are idealized scaffolding; any resulting identity must have denominators that are products of within-axis node differences.

## Round ledger (maximum 10, no extension used)

| Round | Frozen question / kill criterion | Result / next opening |
|---|---|---|
| 1 | Does the exact arbitrary-field iff survive characteristic 2 and m=0,1? Kill with one unisolvent board and zero required minor. | Exact refutation: characteristic 2, m=1, X=(0,1), Y=(0,1,a), a≠0,1. Both boards are unisolvent while Δ1(X)=0. m=0 is an additional edge; later exact m=2 F8 example also lies inside source script range. Full record in negative theory. |
| 2 | Can a parity-weighted Gram identity replace HS positivity for char≠2? Kill if barycentric twist does not vanish on Πm×Πm. | Degree counting proves vanishing. Tensor triangular moment determinant factors as product of leading Hankel minors. Complete char≠2 iff and determinant-square identity. |
| 3 | Can complementary-minor symmetry cancel all powers of 2 and give a char2-valid replacement? Kill if Δr≠ΔL−r or residual factor 2 survives. | Cauchy–Binet complements give equality; total 2-exponent equals N. Corrected all-characteristic criterion in even-index barycentric Hankel minors. Final exact checker passed 1100 random axis pairs/2200 boards and exhaustive 288 F4 m1 pairs/576 boards. |
| 4 | What are exact full-symbolic m=2,3,4 factors and their multiplicities? Kill any formula differing from direct determinant or specialization. | Six exact factor records passed. Fully multivariate direct determinant computed for m2; m3/4 full factors obtained from proved square identity with direct one-variable slices fixing global signs. Multiplicity/scope record in symbolic-factors.md. Two costly rational-expansion routes retained there. |
| 5 | Does the same Gram identity give an explicit Lagrange kernel without square roots and degree-2m discrete-product cubature? Kill if norms need an unproved nonzero condition or the evaluation identity fails. | Derivation below in separate kernel theory; char≠2 and quasi-definiteness explicitly retained for interpolation, while cubature needs no quasi-definiteness. Classical direct consequence, not a new direction/mechanism. |

Rounds 6–10 remain unused; no extension used. Assigned U1 criterion, characteristic edge, multiplicities and direct classical kernel/cubature consequence are complete. No unresolved concrete U1 proof opening remains; broad U2 questions are not activated. No new substantive direction is activated here.

## Source replay coordination

U0 actually reran unchanged `run_all.py`, including hs_ff.py, in a byte-identical cold copy; log `/workspace/padua-cold/charter-unisolvence-20261031/U0/source-copy/hs_ff.log`. Actual scope: 14 (p,m) settings, 600 labelled samples each, two parities = 16,800 parity checks, seed 1; agreement 1.0000 in every setting. This is measured source reproduction; no general proof is inherited. Source sampling artificially required X and Y disjoint; this U1 theory/checker does not.

## Evidence paths

Generated results: `/workspace/padua-cold/charter-unisolvence-20261031/U1/`. Delivery to AC's Windows cold-storage destination remains pending orchestrator handoff. Independent adversarial reconstruction/rerun is arranged separately by the orchestrator; developer checks do not count as that audit.
