# PD-N004 — the endpoint eta≤3/4 mechanism fails at N=512

Review update, 2026-10-31: final ID allocation and scoped independent Astra review are complete; see topics/mz-constants/independent-astra-01.md and ID_CROSSWALK.md. The original development-stage pending-review wording below is historical. Required Claude audit and unresolved literature/novelty coverage remain PENDING. This administrative update changes no mathematical claim or proof.

ID kind: PD-N.
Aliases: exact U witness counterexample to a uniform three-quarter endpoint bound.
Split from: the original combined M2 evidence discussion.
Split into: none; exact U norm identity is PD-T019.

## Statement

At N=512 nodes convention N+1=513, degree n=N−1=511, the CC Gram deviation η_N=||I−G_N||₂ satisfies η_512>3/4. Thus a proposed uniform bound η_N≤3/4 that includes this endpoint case is false.

## Definitions

G_N is the CC Gram matrix in any Lebesgue-orthonormal polynomial basis of Π_(N−1). Equivalently its smallest eigenvalue is λ_min(CC,N−1) from PD-T017. Operator norm is Euclidean spectral norm.

## Assumptions

The exact node, degree, weight and measure conventions above. No assertion about the wording or validity of any source's conditional theorem is part of this statement.

## Status by part

Overall status: PROVED (development; independent acceptance pending).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Strict finite counterexample | PROVED | Analytic rational/logarithmic inequalities below |

Candidate / claim disposition: the uniform endpoint bound is REJECTED: refuted within any claimed range containing N=512,n=511.
Rejection reason: refuted; precise finite scope only.

## Negative-result scope (PD-N only)

Attempted mechanism: treating η≤3/4 as uniform through degree N−1, candidate IDEA-068.
Parameter range: the single exact endpoint case N=512,n=511. This refutes any uniform assertion covering this case; it does not refute a conditional MZ theorem or any smaller parameter range.

## Depends on

PD-T019, the exact U quotient. No floating eigenvalue or M1 theorem.

## Checks

`python tracks/mz-constants/code/m2_endpoint.py --exact 512` executed 2026-10-31; exact Fraction arithmetic returned `RQ_lt_1_4: true`, alongside `Hodd8_gt_201_100: true` and `exp4_bound: true`. The proof below is an independent symbolic certificate, not a computer-assisted claim. Base/rules SHA, code hash, environment and replay in M2 log.

## Sources

The supplied F7 report suggests a failure of a uniform bound, but its attribution and exact applicability remain FULLTEXT UNVERIFIED here. This file states only the local mathematical counterexample.

## Proof or evidence

Let S_N=Σ_(j=1)^N1/(2j−1). Direct addition gives S_8>201/100. Since t↦1/(2t−1) decreases,

    S_512 ≥S_8+∫_9^513 dt/(2t−1)
           =S_8+(1/2)log(1025/17).

The elementary series bound e<11/4 follows, for example, by bounding the factorial-series tail from 1/4! onward by (1/24)/(1−1/5), giving e≤87/32<11/4. Exact rational arithmetic shows (11/4)^4<1025/17. Hence log(1025/17)>4 and S_512>401/100. Also

    4·512²/(512²−1)<401/100.

The U quotient from PD-T019 is therefore

    R=512²/[(512²−1)S_512]<1/4.

The variational principle gives λ_min≤R<1/4, and η_N≥1−λ_min>3/4, as claimed.

## Scope

An exact finite counterexample with explicit degree and node convention. No asymptotic eta convergence or attribution claim.

## Open items

Independent acceptance. Literature worker must separately verify the precise source assumptions before connecting this counterexample to a named application.

## History

2026-10-31, Codex subagent, gpt-6.1-sol xhigh (explicit orchestrator assignment), rules/base d36722823441dc40c6e19d69a174459348dd309c. Split from the supporting U formula so the negative statement retains its exact scope.
