# PD-N?argmax-alln-gated-codex-01 — Coset maximality and pure quadratic primitive gain fail

ID kind:PD-N.
Aliases: analytic majorant-only obstruction; endpoint cusp obstruction.
Split from: original IDEA?argmax-alln-claude-01 and a proposed pure quadratic local repair.
Split into:none.

## Exact negative statement

For every fixed integer n≥3, the odd-coset origin is not a local maximizer of the primitive S_n. Furthermore for no finite C does

S_n(α,β)≤a(α,β)Λc(n)+C(α²+β²)log(n+1)

hold on a full neighborhood of the origin, where a=(cosα+cosβ)/2.

## Attempted mechanism and status

Mechanisms: S itself maximal at the coset, or a purely quadratic local gain without an endpoint linear term.
Parameter range: the specified primitive, every fixed n≥3, arbitrarily small real phases.
Overall status:PROVED, by gated-codex-06's exact positive directional slope.
Candidate disposition:REJECTED:refuted in these precise scopes. This upgrades the original majorant-only failure from its earlier finite MEASURED evidence to a scoped analytic obstruction; it does not reject use of S together with cancellation.
All-degree PD-T099 remains OPEN and is not refuted.

## Proof

For β=0, gated-codex-06 gives S_n(α,0)−Λc=L_n|α|+o_n(|α|) with L_n>0. Hence sufficiently small nonzero α have S_n>Λc, so zero is not a local maximum.

Also a(α,0)=1−α²/4+O(α^4). Under the proposed pure quadratic upper bound, subtract Λc, divide by|α|, and send α→0. The right-hand side tends to0, contradicting L_n>0. ∎

## Checks, assumptions and limits

Exact corrected-kernel convention; no computation is a premise. The finite Taylor/slope derivation was independently reconstructed in gated/checks/d1-r02.md. Claude audit-01 ACCEPTED the mathematics at its stated scope (record fixes pending). n2 is excluded; a legitimate shrinking linear coefficient, aρ^(3/2) allowance together with the required linear cusp term, or direct defect domination is not ruled out. No historical priority claim. Codex Sol xhigh, gated direction1 quantitative diagnosis.

## History


### Documentation correction — 2026-11-02

F3: this dated History section records the review completion while preserving the original development provenance. The negative statement is restricted to each fixed n>=3 for this primitive; no obstruction is transferred to the physical Lebesgue function.

Current review scope (F3): [Claude audit-01](../audit-01.md) ACCEPTED the mathematics exactly as stated; its record/protocol findings and the protocol check of this response remain pending. Supplementary independent checks are complete and do not replace that Claude audit. No proof status, statement, checker predicate or certificate changes. Earlier publication-time review wording is preserved here as history:

> Required Claude topic audit PENDING

F13 closest-prior citation: [PD-T190](../../padua-proof-attempts-2-20261101/theory/proof-attempts-2-codex-75-local-edge-phase-bound.md), statement (1) and proof §§2–4, already retains an explicit C|s| cusp allowance in its one-phase primitive upper bound. [Plan P3](../plan.md) likewise says the primitive rise and cancellation are “probably cusp-linear, not quadratic”. The exact fixed-n cusp formula in gated-codex-06 and the scoped obstruction in gated-codex-N01 refine that already retained issue; they do not establish a historical novelty or priority claim and do not transfer the primitive obstruction to the physical Lebesgue function.
