# PD-N?bivariate-lanczos-claude-501 — The 'larger redundant pivot' rule degrades point-by-point Givens updating on Padua points, with and without non-unisolvent prefixes

ID kind: PD-N.
Aliases: 'largest' pivot catastrophe; Humet/ETNA max-norm pivot as used in Algorithm 1; seed p. 395 pivot remark; OBST?bivariate-lanczos-claude-08; IDEA?bivariate-lanczos-claude-502 (prefix mechanism, refuted in the 'only' form), 013, 016.
Split from: none.
Split into: none.

## Statement

[FP, MEASURED; scope = Parameter range below.] Let Algorithm G (`givens-updating-rotation-count-backward-bound.md`) use, for each doubly-parented monomial j (one with an x-parent and a y-parent), the rule 'largest': form the rotation from whichever of the two pivot entries V(j)[j,p(j)], V'(j)[j,p'(j)] has the larger modulus, instead of the fixed primary ('scheme', y-parent first) pivot. Then:

(N1) *Degradation.* On Padua first-family sets Pad_n, the relative Frobenius error of (H_x, H_y) with 'largest' grows with n on every node order tested, from the level of 'scheme' (n ≤ 15: ≤ 1.5× scheme) to values far above it: on the natural (`given`) order with cubature weights 8.7e-9 (n = 30), 1.5e-7 (n = 40), 3.4e-4 (n = 50), 7.1e-4 (n = 62), and with U(0.1,1) weights 6.1e-3 (n = 30), 2.1e-4 (n = 50), 1.9e-1 (n = 62), against 'scheme' errors ≤ 1.0e-13 on the same streams.

(N2) *Non-unisolvence is not necessary.* On orders whose every prefix is unisolvent with min prefix σ_min ≥ 4.7e-4 (gepp and rpiv1–3, `unisolvent-prefix-extension-lemma.md`), 'largest' reaches 4.2e-13..1.5e-12 (n = 30), 1.8e-11..7.3e-11 (n = 40) and 3.6e-10..3.1e-9 (n = 50) against 'scheme' 3.8e-14..7.8e-14, 6e-14..9e-14 and 1.1e-13..1.3e-13: ratios 10..40, 250..900 and 3e3..3e4, i.e. the growth factor per Δn = 10 is ≈ 30–50. Under the operational definition of candidates.md (catastrophe = ratio ≥ 1e3 and error ≥ 1e-10) 16 of the 54 (family, n, order) cases with n ≥ 20 and all prefixes unisolvent are catastrophic (all at n = 50 except n = 40 rand3 in both weight sets); hence the kill test of plan L5-Q1 for the prefix mechanism *fires*: 'the catastrophe occurs only on orders with non-unisolvent intermediate prefixes' is false in this scope. (14 of these 16 have min σ_min ≥ 1e-8, the pre-registered tolerance; the other two (n = 40 rand3) have 7.1e-8 and are above it too — the count 14 is for cases where the minimum was exact-refined ≥ 1e-8 and the join used the refined minimum; see R01.md.)

(N3) *Non-unisolvence aggravates it.* On `given` and `sortx` orders (almost all prefixes singular) the ratio 'largest'/'scheme' is 1e9..1e11 at n = 30–50 (median of the classes in R01.md), 3–7 orders of magnitude above the unisolvent orders of the same n; at n = 15 and 20 the structured orders are sometimes harmless (`given`, cubature weights: 8.5e-15 vs 7.9e-15, 1.4e-14 vs 9.9e-15) and sometimes not (random weights n = 20: 1.4e-3 vs 1.4e-14), so singular prefixes are neither sufficient nor necessary for large 'largest' errors.

(N4) *Magnitude-based alternatives fail the same way* (n = 30, `given`, cubature weights; errors vs 'scheme' 2.3e-14): alternative pivot only if its modulus exceeds 10× the primary one: 8.6e-9; exceeds 100×: 5.9e-12; alternative pair (pivot, entry below) chosen by larger hypot: 4.0e-12; pair-norm with factor 100 equals 'scheme'. On `rand1–3` and `gepp` at n = 20, 30 the pivot-only factor rules 10/100 and pair-norm 100 coincide with 'scheme' (the alternative is almost never taken), and pair-norm 1 coincides with 'largest'.

(N5) *Random nodes are different.* For M = N-free random nodes (M/N ≈ 3) 'largest' is not worse than 'scheme': uniform nodes, M = 2016: 1.45e-12 vs 5.6e-11; but with the arcsine-density random nodes it is worse with a larger slope (2.10 vs 1.28; 1.1e-12 vs 6.4e-14 at M = 1326).

## Definitions

'scheme', 'largest': `givens_core.c` rule codes 0 and 1 (bit-identical to the inputs' `givens(pivot=…)` at n = 6, 10, 14). Catastrophe, unisolvent order, σ_min: as in PD-T?bivariate-lanczos-claude-503.

## Assumptions

IEEE double; real nodes; the tables of parents of Algorithm 1 ('downside-up', y-parent primary); no skip threshold (b = 0 test only).

## Status by part

Overall status: MEASURED (the status of the negative statement; the candidate 'larger pivot is a stabilising heuristic' carries the disposition REJECTED: failed, scope above).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| N1–N3 | MEASURED | `logs/r01_padua_cub.jsonl`, `r01_padua_rand.jsonl`, `r01_prefix_a.jsonl`, `r01_prefix_b.jsonl`; `analyze_r01b.py` output in `logs/analysis_r01b.txt` |
| N4 | MEASURED | `logs/r03_rules.jsonl` |
| N5 | MEASURED | `logs/r01_random.jsonl`, `logs/r01_random_cheb.jsonl` |
| a mechanism (why larger pivot degrades) | OPEN | see Open items |

Candidate / claim disposition: REJECTED (the seed-p. 395 suggestion and the Humet-type max-norm pivot as a stability enhancement in point-by-point Givens updating on Padua points; and the prefix mechanism in the 'only' form).
Rejection reason: failed (mechanism does not achieve its stability aim in the stated range); the 'only on non-unisolvent prefixes' conjecture is refuted (MEASURED) in the stated range.

## Negative-result scope

Attempted mechanism: IDEA?bivariate-lanczos-claude-013/016/502 — choose the larger redundant pivot (and variants by magnitude); and the diagnostic claim that its failures occur only on non-unisolvent prefixes.
Parameter range: Algorithm 1, real nodes, IEEE double, Padua first-family n = 10, 15, 20, 30, 40, 50, 62 (cubature weights; U(0.1,1) weights; unit weights up to n = 40 in `r01_padua_unif.jsonl`), orders given, sortx, rand1–3, gepp, rpiv1–3 (the last two only up to n = 50), and random nodes M ≤ 2016. 'No catastrophe at n ≤ 15' is part of the scope.

## Depends on

`unisolvent-prefix-extension-lemma.md` (orders), `prefix-unisolvence-order-statistics-measured.md` (prefix tests), input `f6_givens_vs_hl_deficit.py` (unchanged, via bit-identical C port). The reproduction agent's independent reproduction of the seed numbers (`repro/REPRO.md`: n = 20 random weights 7.2e-4, n = 30 uniform 2.0e-9/3.3e-12) is supporting evidence from another agent, not used as a dependency.

## Checks

`exp_r01.py padua_cub|padua_rand`, `exp_r01b.py`, `analyze_r01b.py`, `exp_r03.py`; see R01.md/R03.md for the command lines. Independent rerun of these numbers on AC's servers: not done (Runs needed). The two skip-threshold claims of the input (thresholds 1e-14, 1e-12 do not cure 'largest') are *not* re-tested here; the reproduction agent's run 9 (REPRO.md) reports them (R: no threshold cures 'largest').

## Sources

VB–C 2010 p. 395 (fulltext read): 'if two pivots differ in some orders of magnitude, then choosing the larger one may enhance the numerical stability' (a suggestion, no data); Table 1 uses n ≤ 15 Padua points. `vanbarel-humet-sorber-2014` (record only, not re-read).

## Proof or evidence

Measured; see Checks.

## Scope

Exactly the range above. This does not show that every stability heuristic based on pivot size fails, that 'largest' fails for other pivot-chain structures, or that it fails in exact arithmetic (in exact arithmetic with unisolvent prefixes both pivots are equivalent).

## Open items

(1) A mechanism: why does 'largest' degrade with n on well-conditioned unisolvent orders at a growth of ≈ ×40 per Δn = 10? (The redundant-pivot residual is not zeroed; its amplification along the chase is the natural suspect; not analysed.) (2) A test on the Harris–Simanek checkerboard orders (plan Benchmarks) as an independent family. (3) n = 62 for unisolvent orders (Runs needed).

## History

2026-10-31, Claude Sonnet 5.5 (high), L5 R03: created.
