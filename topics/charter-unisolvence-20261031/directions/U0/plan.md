# U0 frozen verification plan

- Rules/base SHA: `d36722823441dc40c6e19d69a174459348dd309c` (provided by orchestrator; rules read locally).
- Branch: `codex/charter-unisolvence-20261031`.
- Role: bounded U0 verification developer, Codex; assigned model/effort `gpt-6.1-sol xhigh`. Only the orchestrator changes Git state.
- Ownership: this directory and `theory/unisolvence/u0/` only. Generated evidence: `/workspace/padua-cold/charter-unisolvence-20261031/U0`.
- Stage: WORK; independent adversarial acceptance pending.
- Frozen before the first scientific execution: 2026-10-31.

## Exact first question

For the canonical checkerboard set
`Pad_n = {((zeta^j+zeta^-j)/2,(eta^k+eta^-k)/2): 0<=j<=n, 0<=k<=n+1, j+k even}`,
where `n>=1`, the characteristic `p` does not divide `2n(n+1)`, and `zeta,eta` have exact orders `2n,2(n+1)` in the algebraic closure, do the supplied implementations reproduce their stated finite checks, and which of the following source statements survive explicit assumption and edge-case checking?

1. `|Pad_n|=(n+1)(n+2)/2` and unisolvence for total degree at most `n` over its coordinate field.
2. All nodes are `F_q`-rational exactly when `q=+/-1 mod 2n` and `q=+/-1 mod 2(n+1)`; classify the four sign combinations, including degeneracy at `n=1`.
3. For Dickson coordinates `(X,Y)=(2x,2y)`, the square of the total-degree monomial Vandermonde determinant is `2^((n^2+3n+6)/2) [n(n+1)]^N`, `N=(n+1)(n+2)/2`.
4. At the odd prime power `q=2n+1`, the supplied quadratic-character formulas describe the canonical set, including `-1` endpoints.
5. The small evaluation-code distances claimed in the source match exhaustive finite calculations, with scope separated from general distance, duality and optimality claims.

This is source verification and quick registration, not a novelty claim or a new mechanism. Source headings saying "proved" convey no inherited proof. All supplied numerical statements start MEASURED after local reproduction; all universal targets start OPEN unless a complete independent derivation is written. Claimed finite results not actually rerun remain OPEN/unverified source reports.

## Before-run kill and scope criteria

- Reproduce the unmodified `code/ff_padua/run_all.py` in a byte-identical cold-storage copy so the supplied source tree stays untouched. Inspect every child log and process outcome: the driver itself does not propagate child failures.
- If isolated imports fail, preserve the original failed execution and fix only the local execution wrapper/path handling; do not edit the source copy. Record precisely whether any repair was needed.
- Kill an exact stated formula only by an exact counterexample or written negation under its own hypotheses; label a missing hypothesis separately. A failed proof route does not refute the target.
- The first cheap mathematical check is to reconstruct the character-sum Gram identity and count boundary weights; then compare the determinant exponents. Check `n=1`, endpoint parity, the distinction between prime and prime-power implementations, and `k=n` in any code-duality claim.
- Preserve all considered candidates and up to ten conceptual-round records. Stop after exact U0 scope and concrete unresolved proof obligations are registered. Do not generate new mechanisms before the orchestrator confirms that the literature baseline is ready.

## Planned executions (not yet run when frozen)

1. Capture Python/platform/dependency versions, source/copy SHA-256 identities and deterministic seeds appearing in the scripts.
2. `python3 -I /workspace/padua-cold/charter-unisolvence-20261031/U0/source-copy/run_all.py` and per-child log inspection.
3. A small exact independent checker, if needed, for exposed endpoint/quantifier issues and selected code distances. Its checked scope and limitations must be frozen in code and outputs.

## Gate coverage before generating any candidate

Read complete current `state/IDEAS.md` (empty registry, obstruction and disposition tables empty) and `literature/INDEX.md` (no extracted statements). No shortlisted entries exist. Source mechanisms and prior-art assertions have been read as unverified supplied material. The orchestrator is producing the external baseline; no priority or novelty conclusions are authorized here.

## Runs needed

All scientific executions above; independent adversarial rerun/audit arranged by orchestrator.
