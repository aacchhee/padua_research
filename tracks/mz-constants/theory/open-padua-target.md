# PD-T028 — two-dimensional Padua upper and endpoint targets

## Current resolution — 2026-11-05

Registry Status: **OPEN**, preserving AC's display for the historical positive formulation. Disposition: **REJECTED: refuted**, by the separate **PROVED** [PD-N105 negative carrier](../../../topics/padua-mz-2d-frontier-20261105/theory/f12-eventual-negative-carrier.md) and [PD-N106 upper carrier](../../../topics/padua-mz-2d-frontier-20261105/theory/f12-eventual-upper-carrier.md). Along even m the minimum tends to minus infinity, the maximum to plus infinity, and eta diverges; the positive endpoint orders and eta→1 are false. The earlier OPEN formulation below is historical, not an unresolved positive conjecture or usable dependency. No effective onset, odd-m classification or sharp extremal growth law is claimed. These carriers prove existence only and do not explain or certify the separate m1600 float observation.

Split into: PD-N105/106 preserve their own negative statements and proofs; supporting PD-T021 remains unchanged. [Claude audit-01](../../../topics/padua-mz-2d-frontier-20261105/audit-01.md) accepted candidate `dee638408505c9977f3febd98fdd42c9bc512c92`; [response-01](../../../topics/padua-mz-2d-frontier-20261105/response-01.md) records the permitted editorial dispositions.

## Preserved original statement and history

Review update, 2026-10-31: final ID allocation and scoped independent Astra review are complete; see topics/mz-constants/independent-astra-01.md and ID_CROSSWALK.md. The original development-stage pending-review wording below is historical. Required Claude audit and unresolved literature/novelty coverage remain PENDING. This administrative update changes no mathematical claim or proof.

ID kind: PD-T. Aliases: signed Padua weak MZ; two-dimensional log-squared endpoint.
Split from: original M4 target.
Split into: the exact marginal reduction is separately PROVED in [PD-T021](m2-padua-marginal.md), whose header links back to PD-T028. This separates supporting information from the original M4 discussion; it is not a proved part of any target below and supplies no statement decomposition that would make PD-T028 PARTIAL.

## Statement

For the interpolatory Padua rule of degree m for dx dy on [−1,1]², in total-degree Legendre products through n≤m−1, determine whether λ_max<2 and λ_min>0 for every m≥2, and whether λ_min(m,m−1) asymp (1+log m)^−2. Also determine whether eta(m,m−1) tends to one. These remain distinct questions because signed weights do not guarantee positive definiteness.

## Definitions and assumptions

The Padua node convention, interpolatory Lebesgue weights (some negative), total degree and continuous product normalization are specified in the track README and reproduction code. m is the Padua construction degree, not a generic quadrature point count.

## Status by part

Overall status: OPEN. All universal assertions in this statement are OPEN. The finite spectra are a separate MEASURED record; marginal compression is a separate PROVED dependency. Neither changes this status. Candidate disposition: deferred, not rejected.

## Depends on

Background only: PD-T021 exact compression; PD-T026 finite measurements. No classical/private theorem is imported as a proof.

## Checks and sources

Supplied F7/ASV numerical predecessor and M0 screen; reproduced spectra m10,20,30,40 only. Source statements and coverage in literature/records/mz-*.md. No universal two-dimensional Schur estimate or positivity test has been completed.

## Proof or evidence

There is no proof of these targets. PD-T021 already proves unconditionally that exact marginal compression gives eta_Padua≥eta_CC and liminf eta_Padua≥1: PD-T018 establishes λ_min(CC,N−1)→0, and eta_Padua≥1−λ_min(CC,N−1) suffices. This proved liminf supplies no limsup or 2D upper spectral bound. Negative weights require a distinct argument.

## Scope and open items

Resume with a concrete signed-form or aliasing argument controlling the complement of the univariate compression. Compare tensor-CC, Xu, Morrow–Patterson and Lissajous conventions through primary sources before claiming a general mechanism. This campaign selected CC M1/M2/M3 for substantive development and retained M4 as a scoped reduction plus open target.

## History

2026-10-31, Codex orchestrator, runtime metadata unexposed: exact supplied marginal statement split from the original stronger two-dimensional questions; source's unproved convergence implication is not inherited.

2026-10-31, audit-01 L1/P4 response, Codex gpt-6.1-sol xhigh (explicit assignment), rules `6d10a82cf6fd6f7ef6fbe76e68133ccbcbe51994`: replaced the stale phrase "once the CC endpoint convergence is established" because PD-T021 already proves the liminf from PD-T018. Named the reciprocal PD-T021 link and clarified its supporting role; all original two-dimensional targets and the OPEN status are unchanged.
