# D4 gate — common spectral transforms and continuation

2026-11-05. Developer: Codex, dispatched gpt-6.1-sol xhigh; exact backend metadata is not independently exposed. Rules and pinned input: `823cf6a4ef7c01b4ef3d2a6fec3e9f19d4b4f6f1`; base `b4d292eea5eed373002506d5e16a3761bd7ae10e`. Scope: D4 only. No Git or shared-registry mutation.

## Coverage and predecessors

Read AGENTS, WORKFLOW, CODEX, handoff01, plan, predecessor report/gate/candidates and the formulation/interior-divisor/marginal-reconstruction theory. Scanned the complete 1016-line IDEAS registry's headings, aliases and summaries, and obstruction/disposition tables, using bounded raw reads (repeated overlapping chunks to recover truncated output). Mechanism search: Christoffel, Geronimus, Toda, qd, spectral/measure modification, nearest-neighbour, MOP and node updating. Complete shortlisted IDEA-031/090/117/193/376–379 entries and predecessor candidate records were read. No exhaustive historical novelty claim.

Closest records: IDEA-193 already classifies Toda/qd as measure modification; IDEA-379/PD-T289 give known NN reconstruction; IDEA-378 requires a concrete coupled invariant; LIT-567/568 report common Christoffel/Toda constructions. Their inherited primary-reading claims are reports by their named readers, not this worker's primary reading. New primary-source coverage will be recorded separately in `literature-D4.md`.

Applicable obstructions: equal/proportional starting measures are nonnormal at (1,1); finite common support permits a normal triangle, never a perfect N-by-N rectangle; terminal b equality is not a C4 failure; compatibility does not provide a second spectral coordinate; exact algebra alone provides no stability conclusion. Bivariate downdating/measure-modification precedents cannot supply a new MOP stability theorem.

## Prospective candidates and cheapest tests

| Local candidate | Separation from predecessor | Decisive test and kill criterion, before execution |
|---|---|---|
| D4-C1: common Christoffel transport | Explicit finite-triangle invariant, transformed-polynomial/NN map and boundary rule; algebra is known, numerical feasibility is the proposed distinction | Derive det Mtilde_nu=(-1)^k P_nu(c) det M_nu; exact Fraction check on N=4. Any formula mismatch blocks implementation. Then compare binary64 transport with direct transformed references at N=4,8,12,16. G4's both-family N16 kill applies only to this specified design. |
| D4-C2: universal easy-start common-transform solver | Reach arbitrary target pairs by common Christoffel/Geronimus/Toda steps | Test the projective pointwise weight ratio. If common multipliers preserve it, reject only this arbitrary-target claim; weight-specific transforms are outside the obstruction. |
| D4-C3: common Toda continuation | Explicit finite-triangle ODE preserving the moment/NN solution, with finite terminal closure | Derive common exponential-flow equations locally, including the degree-N boundary, and compare one small flow with directly deformed moments. A normality crossing blocks only continuation through that path. No stability claim from ODE solvability. |
| D4-C4: independently deformed weights | Changes relative weights and could reach the benchmark families | A concrete local generator/closed state and a normal path are required. If none is supplied in round 1, defer; do not mislabel common Toda equations as the independent-weight flow. |
| D4-C5: lattice Schrodinger spectral reparametrization | Must improve a defined input metric over marginal spectral data | Require an explicit invertible finite parametrization and conditioning comparison. Without it, defer; index-space spectral language is not a measured algorithm. |

## Pre-experiment implementation plan

Retain polynomial node values as an auxiliary state. Construct them at the starting normal pair by the NN recurrence in one canonical parent direction, with the degree-N support polynomial treated by its known zero values. Apply common Christoffel polynomial transport using evaluation ratios at c, then recover h-ratio a coefficients and b from subleading coefficients. Every proposed path and initial-state source must be declared; exact normality and floating denominator diagnostics remain distinct. A direct transformed moment solve is a reference, not the transport algorithm.

All candidates, including failed/deferred ones, will remain in `candidates-D4.md`. Exact and floating sanity checks are MEASURED; a separately written general proof may be PROVED without relying on those checks. Round 1 ends only when the coordinator publishes it; no second round begins silently.

## Implementation refinement and actual gate outcome

After deriving the invariant and before the floating runs, the auxiliary full polynomial state was replaced by layer-ordered evaluation ratios R: evaluating the old NN recurrence at c closes these ratios directly. This removes the need to store node values. The exact determinant/polynomial checks were run first and passed. No claim that the original plan already contained this optimization is intended.

D4-C1a initializes by binary64 C4 on w/(x+2), then restores with common c=-2; its comparison criterion is G4's two-family N16 improvement threshold.

Gate-timing disclosure and AC acceptance (without retrospective clearance): [LOG, 2026-11-06 AC decisions](LOG.md#2026-11-06-ac-decisions).

 Both N16 errors worsened, so that fixed design is failed. The transform from rounded accurate source data remains a separate isolation result. D4-C2 is analytically refuted within its common-factor scope; D4-C3 passed only its finite ODE sanity test with oracle initialization; D4-C4/C5 are deferred. Full dispositions and precise limits are retained in `candidates-D4.md`.
