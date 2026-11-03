# PD-T218 (PD-T?argmax-alln-gated-codex-04) — Uniform gap outside fixed corner neighborhoods

Final registration: **PD-T218**, 2026-11-03. The provisional identifier in the title remains an alias; mathematical statement and historical evidence are unchanged.

ID kind:PD-T.
Aliases: compact-complement gap; two-phase assembly; moving-strip inclusion.
Split from: PD-T099 supporting large-degree P2/P4/P5 regimes.
Split into:none. Corner dominance and an effective threshold remain distinct.

## Statement

For every fixed0<δ<π/2, let Kδ be the set of angle points(θ,φ)∈[0,π]² where θ∈[δ,π−δ] or φ∈[δ,π−δ]. Thus Kδ is the complement of the four openδ-angle corner squares. Put cδ=δ²[1−cos(δ/2)]/(16π²)>0.

Then, for the even-checkerboard Padua Lebesgue function,

sup_Kδ λ_n ≤ Λc(n)−cδ+oδ(1).

In particular there exists an integer Nδ such that λ_n≤Λc−cδ/2 everywhere on Kδ for n≥Nδ. This Nδ is not numerically explicit. The conclusion includes both orientations of all moving edge-to-interior strips in Kδ and the compact interior.

## Definitions/assumptions/status

All kernels, weights and phases are those of gated-codex-01/02/03 and PD-T101. Exact real arithmetic. Overall status:PROVED by the analytic reduction below, using its explicitly cited proved dependencies; there is no named unproved mathematical hypothesis or CONDITIONAL claim status in the statement. Supplementary independent review is complete; Claude audit-01 ACCEPTED the mathematics at its stated scope (record fixes pending). The all-degree PD-T099 target remains OPEN.

No uniform assertion asδ↓0 and no control inside the four corner squares is included. This theorem does not assert that any fixed-δ region contains a runner-up or locate its exact maximizer.

## Depends on

- gated-codex-01, exact Δ≥Qv,Qh and compact-uniform projection limits for phases tending to zero, uniform in the unused macroscopic coordinate.
- gated-codex-02, global two-phase primitive bound S≤aΛc+C log(n+1), a=(cosα+cosβ)/2 on |α|+|β|≤π.
- gated-codex-03, local primitive supremum S−Λc=O(log^-2 n).
- PD-T156 (1) / PD-T157 (1) for the explicit logarithmic corner lower bound; PD-T159 for its corner-product comparison dependency; previous codex-04/05 integral positivity.

## Proof

First every physical point has an odd-coset representation θ=Jπ/n+α/n,φ=Kπ/(n+1)+β/(n+1), with J,K physical mesh indices,J+K odd and|α|+|β|≤π. To see this, choose a physical mesh rectangle containing the point, using the adjacent interior rectangle on a boundary. In normalized fractional coordinates x,y∈[0,1], if the lower-left vertex has odd parity the odd vertices have L1 distances x+y and2−x−y, whose minimum≤1. If it has even parity the odd vertices have distances1−x+y and1+x−y, again with minimum≤1. Multiply byπ.

The full periodic kernel sum defining S is invariant under even mesh translations. Translating by this odd(J,K) sends its board to the odd board used in the primitive estimates. Therefore the same S, with these exact phases, obeys the cited global/local bounds. By the exact cardinal identity, λ≤S.

Suppose the stated uniform upper bound fails. There are ε>0, degrees tending to∞ and points z_n∈Kδ with

λ_n(z_n)>Λc(n)−cδ+ε.

The global primitive estimate then yields

(1−a_n)Λc(n)≤C log(n+1)+cδ−ε.

Since |α|,|β|≤π, 1−a≥(α²+β²)/π². The corner lower bound Λc≥(4/π²)log²n−54 forces α_n,β_n→0. The local primitive theorem gives S_n(z_n)≤Λc+o(1), uniformly along these phases.

At each z_n either its second coordinate lies in[δ,π−δ], in which case Δ≥Qv≥g_v(φ_n)+o(1)≥cδ+o(1), or its first coordinate lies there, in which case Δ≥Qh≥g_h(θ_n)+o(1)≥cδ+o(1). Both projection error bounds are uniform, so changing the case with n causes no loss. Consequently

λ_n(z_n)=S_n−Δ_n≤Λc−cδ+o(1),

contradicting the fixedε. This proves the uniform oδ(1) upper bound. Choosing n large enough that the error is<cδ/2 gives the stated existence of Nδ. ∎

## Checks and limits

This is direction1 round2's registered assembly. It uses no numerical fit or computation. Direction1 round1 source/numerical checks are supplementary. Independent assembly review is recorded separately in gated/checks/.

The existence of a threshold is not an explicit value or a finite certificate for all remaining degrees. Even an explicit compact threshold alone would leave the corner neighborhoods. This result supersedes only the earlier OPEN qualitative compact-strip/interior obligations at its stated scope; shared registries are unchanged and Claude audit-01 ACCEPTED the mathematics at its stated scope (record fixes pending).

## History

Codex gpt-6.1-sol xhigh, authorized gated direction1 round2, scientific base7d308b10d946b607ae0690454f6c0103690775a4. Closest mechanism IDEA305/fallback04, implementation/assembly variant; no novelty claim. Exact phase cover, projection uniformity and primitive identity were the pre-registered discriminating checks.


### Documentation correction — 2026-11-02

F2/F3: the original dependency text was “PD-T159 corner growth”; its direct logarithmic lower-bound source is PD-T156 (1) / PD-T157 (1), with the genuine PD-T159 corner-product comparison dependency retained. The original phrase “conditional only in the ordinary sense of its explicitly cited locally proved dependencies awaiting independent/Claude review” described review timing, not an unproved mathematical hypothesis; the current wording makes this explicit.

N4: Nδ here denotes the existential, non-effective compact-complement threshold; it is local to this file and differs from the explicit ceil(16π/δ) threshold called Nδ in gated-codex-05.

Current review scope (F3): [Claude audit-01](../audit-01.md) ACCEPTED the mathematics exactly as stated; its record/protocol findings and the protocol check of this response remain pending. Supplementary independent checks are complete and do not replace that Claude audit. No proof status, statement, checker predicate or certificate changes. Earlier publication-time review wording is preserved here as history:

> Required independent assembly check and Claude topic audit are PENDING
> required Claude audit remains pending

F13 closest-prior citation: [PD-T103](../../padua-proof-attempts-20261101/theory/proof-attempts-codex-03-degenerate-maxima.md) supplies an earlier excluded-zero-cardinal local certificate at the two degree-3 degenerate maxima: it controls a signed background and the excluded cardinal by exact Hessian bounds on fixed angle discs. It is a conceptual predecessor for retaining cancellation and zero cardinals, not a proof of this compact projection/defect result or an additional hypothesis here. No duplicate, priority or exhaustive novelty claim is made.
