# PD-T?mz-paper-claude-02 — analytic lower bounds for the corner-operator extrema

ID kind: PD-T (provisional; final ID at PR preparation).
Aliases: ‖B‖ ≥ c_new; corner norm carrier bound; combined corner enclosure.
Split from: none. Combines PD-T533/PD-T379 (carrier bounds) with PD-T536/PD-T540 (limits are the spectral extrema of B; c₋=−‖B‖). Suggested by the MZ-SP plan review, finding F7.
Split into: none.

## Statement

Let B be the compact selfadjoint corner operator of PD-T536, with c₋ = inf σ(B) and c₊ = sup σ(B). Let c_new be the constant of PD-T533, c_new = 16(51/200)(49/200)/[9 A J(51/200)] with A = 4 log 2 and J as in PD-T533/PD-T537. Let c₊^(379) = 1/[36 A J₊(1/8)] be the positive constant of PD-T379. Then

(a) ‖B‖ = −c₋ ≥ c_new (c_new = 0.0296417…, rounded orientation; exact closed form above);

(b) c₊ ≥ c₊^(379) > 0.

In particular, the analytic lower bound in (a) exceeds the rectangle certificate's lower bound 0.013164… of PD-T542 for ‖B‖.

## Definitions and assumptions

Exactly those of PD-T536, PD-T540, PD-T533 and PD-T379: the signed Lebesgue Padua rule of mass four, total degree Π_{m−1}, extremal Rayleigh quotients λ±(m,m−1), natural logarithm.

## Status by part

Overall status: **PROVED** (developer: Claude; independent check pending, flagged for the Codex audit).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| (a) | PROVED | Proof below; independent check pending |
| (b) | PROVED | Proof below; independent check pending |

## Depends on

PD-T536 (λ±(m,m−1)/log m → c± over all integers m), PD-T540 (c₋ = −‖B‖), PD-T533 (limsup λ₋(m,m−1)/log m ≤ −c_new over all integers m), PD-T379 (liminf λ₊(m,m−1)/log m ≥ c₊^(379) over all integers m), PD-T542 (the certified rectangle enclosure, used for comparison only).

## Checks

Analytic. Floating evaluation of c_new = 0.029641768762… (Python, double precision, orchestrator, 2026-11-13) is orientation only; the inequality c_new > 0.013165 is clear from it, and PD-T533 itself gives c_new > 1/[9A J(1/4)] (≈ 0.02962). No proof step depends on a floating value except the comparison sentence after the statement, which is not part of (a) or (b).

## Proof

(a) By PD-T536, λ₋(m,m−1)/log m → c₋. By PD-T533, the upper limit of the same sequence is at most −c_new. Hence c₋ ≤ −c_new, and PD-T540 gives ‖B‖ = −c₋ ≥ c_new.

(b) By PD-T536, λ₊(m,m−1)/log m → c₊; by PD-T379, its lower limit is at least c₊^(379). Hence c₊ ≥ c₊^(379).

## Scope

One-sided lower bounds only. No upper bound on ‖B‖ beyond PD-T542's 0.47781…, no two-sided decimal of c₋ or c₊, and no optimality claim for the carrier constants. PD-T381's decimal conjunct stays OPEN.

## Open items

Independent check; Codex audit of the topic.

## History

2026-11-13: created in topic padua-mz-paper-20261113 during the MZ-SP plan dispositions (review F7).
