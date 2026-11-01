# PD-T027 — sharp endpoint upper spectrum

Review update, 2026-10-31: final ID allocation and scoped independent Astra review are complete; see topics/mz-constants/independent-astra-01.md and ID_CROSSWALK.md. The original development-stage pending-review wording below is historical. Required Claude audit and unresolved literature/novelty coverage remain PENDING. This administrative update changes no mathematical claim or proof.

ID kind: PD-T. Aliases: 1.004437 limit; uniform endpoint upper gap.
Split from: M1 supplied strengthened target beyond the strict threshold.
Split into: the strict threshold is separately PROVED in [PD-T014](m1-upper-bound.md), whose header links back to PD-T027. This is separation of related targets from the original M1 discussion, not decomposition of the sharp-limit/uniform-gap statement below; PD-T014 is supporting background and proves no part of that sharper statement.

## Statement

For the Lebesgue CC rule at N+1 Lobatto nodes, determine whether λ_max(G_(N,N−1)) converges, identify its exact limit if it does, and prove a uniform constant B<2 independent of N. The supplied decimal near 1.004437 is a numerical lead, not an exact proposed value.

## Definitions and assumptions

N≥2; continuous Legendre orthonormal basis through degree N−1; Gram matrix of Q_N. Measure and normalization are those of the track README.

## Status by part

Overall status: OPEN. The existence/value of the limit and uniform endpoint gap are not proved. The strict finite-N upper bound and endpoint minimum-eigenvalue order are separate PROVED results, not parts that turn this stronger target PARTIAL. Candidate disposition: deferred sharpening, not rejected.

## Depends on

No dependency establishes the target. Background: PD-T014 (strict threshold) and PD-T022 (degree-sensitive bound and endpoint corollary); finite decimal evidence: PD-T026 (MEASURED through N1280 only).

## Checks and sources

M1 four-round ledger and M0 literature baseline retain the source question and closest classical aliasing predecessor. No large run or computer proof is claimed. The supplied N20480 output remains input evidence outside the reproduced scope. Historical norm theorems remain pending-reference.

## Proof or evidence

No proof of this statement. Current analytic gaps decay like N^−1; they cannot prove eventual λ_min-side binding in eta. In particular, the complete minimum-eigenvalue order does not establish 1−eta asymp log^−2 N, since 1−eta=min(λ_min,2−λ_max).

## Scope and open items

Resume with a concrete sharper spectral comparison or an asymptotic operator model and a quantified error bound. Tolerance-dependent HSS rank alone supplies neither. No conceptual round beyond the closed strict-target rounds was launched.

## History

2026-10-31, Codex orchestrator, runtime metadata unexposed: preserves the supplied sharp strengthening as a distinct OPEN target rather than silently dropping it after the strict theorem.

2026-10-31, audit-01 P4 response, Codex gpt-6.1-sol xhigh (explicit assignment), rules `6d10a82cf6fd6f7ef6fbe76e68133ccbcbe51994`: named the reciprocal PD-T014 link and PD-T022 background by ID; clarified supporting-target separation rather than a proved portion of the present statement. The original target and OPEN status are unchanged.
