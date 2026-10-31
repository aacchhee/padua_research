# PD-N?bivariate-lanczos-claude-501 — The 'larger redundant pivot' rule degrades point-by-point Givens updating on Padua points, with and without non-unisolvent prefixes

ID kind: PD-N.
Aliases: 'largest' pivot catastrophe; Humet/ETNA max-norm pivot as used in Algorithm 1; seed p. 395 pivot remark; OBST?bivariate-lanczos-claude-08; IDEA?bivariate-lanczos-claude-502 (prefix mechanism, refuted in the 'only' form), 013, 016.
Split from: none.
Split into: none.

## Statement

[FP, MEASURED; scope = Parameter range below.] Let Algorithm G (`givens-updating-rotation-count-backward-bound.md`) use, for each doubly-parented monomial j (one with an x-parent and a y-parent), the rule 'largest': form the rotation from whichever of the two pivot entries V(j)[j,p(j)], V'(j)[j,p'(j)] has the larger modulus, instead of the fixed primary ('scheme', y-parent first) pivot. Then:

(N1) *Degradation with n.* On Padua first-family sets Pad_n the relative Frobenius error of (H_x, H_y) with 'largest' is at the level of 'scheme' at n = 10 (ratio 0.8..1.3 for all 9 orders and both weight types), is up to 5 times 'scheme' for the random and constructed orders at n = 15..20, and grows to ratios of 1e3..1e5 at n = 50 (gepp, rpiv1-3, rand1-3; see N2). On the natural (`given`) order with cubature weights: 8.7e-9 (n = 30), 1.5e-7 (n = 40), 3.4e-4 (n = 50), 7.1e-4 (n = 62); with U(0.1,1) weights 6.1e-3 (n = 30), 2.1e-4 (n = 50), 1.9e-1 (n = 62); with unit weights 2.0e-9 (n = 30), 6.5e-5 (n = 40); against 'scheme' errors <= 1.1e-13 on the same streams. The exceptions at small n are the `given` order with U(0.1,1) weights (1.1e-2 at n = 15, 1.4e-3 at n = 20, both with 'scheme' at 1e-14), so there is no 'safe n' threshold for 'largest' that holds for all weights.

(N2) *Non-unisolvence is not necessary.* On orders whose every prefix is unisolvent with min prefix sigma_min >= 4.7e-4 (gepp and rpiv1-3, `unisolvent-prefix-extension-lemma.md`), 'largest' reaches (cubature weights) 4.2e-13..1.5e-12 (n = 30), 1.8e-11..5.7e-11 (n = 40) and 9.3e-10..3.1e-9 (n = 50) against 'scheme' 3.8e-14..4.5e-14, 6.0e-14..7.8e-14 and 1.1e-13..1.2e-13: ratios 11..33, 250..720 and 8.6e3..2.8e4; the U(0.1,1)-weight values are similar (within a factor 2.5). The error grows by a factor 15..50 per Delta n = 10 (gepp: 2.8e-14, 4.2e-13, 1.8e-11, 9.3e-10 for n = 20, 30, 40, 50). Under the operational definition of candidates.md (catastrophe = error ratio >= 1e3 and 'largest' error >= 1e-10), 16 of the 54 (weights, n, order) cases with n >= 20 and all prefixes unisolvent are catastrophic: the 14 cases at n = 50 (gepp, rand1-3, rpiv1-3, for each of the two weight types) plus n = 40 rand3 for both weight types (listing in `logs/analysis_r01b.txt`). Hence the kill test of plan L5-Q1 for the prefix mechanism *fires*: 'the catastrophe occurs only on orders with non-unisolvent intermediate prefixes' is false in this scope. 14 of the 16 have min sigma_min >= 1e-8 (the pre-registered tolerance); the two with 3.0e-9 are n = 50 rand3 (both weight types). The 8 cases of gepp and rpiv1-3 at n = 50 (4 per weight type) (min sigma_min >= 4.7e-4) are unaffected by any tolerance choice.

(N3) *Non-unisolvence aggravates it.* Median 'largest'/'scheme' ratio over the two weight types, by order class: `given` 1e9..1e12 at n = 30, 40, 50 (also 8e11 at n = 15 and 5e10 at n = 20, driven by the random-weight stream); `sortx` 5e4 (n = 30), 1.6e7 (n = 40), 7e9 (n = 50); random orders (all prefixes unisolvent except n = 15, 40 rand2) 33, 1.2e3, 1e5; gepp/rpiv 30, 460, 1.2e4. So the singular-prefix streams are 3..10 orders of magnitude worse than the unisolvent ones at the same n (3 for `sortx` n = 30 against random orders, 10 for `given` n = 30 against gepp/rpiv). Singular prefixes are not sufficient for a large 'largest' error (cubature weights, n = 15 and 20, `given` and `sortx`: ratio 1.1..1.4; random weights n = 20 `sortx`: 2.7) and not necessary (N2).

(N4) *Magnitude-based variants (R03).* Only-if-larger-by-kappa pivot rules ('pivk10', 'pivk100') and pair-norm rules ('pairnorm1', 'pairnorm100') on n = 20, 30 (cubature and random weights; `logs/r03_rules.jsonl`): on gepp and rand1-3 'pivk10', 'pivk100' and 'pairnorm100' equal 'scheme' to the printed digits (the alternative is not taken) and 'pairnorm1' equals 'largest' within 15%; on the structured streams at n = 30 (`given`, cubature weights, scheme 2.3e-14): pivk10 8.6e-9, pivk100 5.9e-12, pairnorm1 4.0e-12, pairnorm100 2.2e-14 (= scheme); random weights `given`: pivk10 and pivk100 4.3e-3, pairnorm1 1.6e-13, pairnorm100 5.9e-14. No variant beats 'scheme' anywhere. (Disposition of these rules: R03.md.)

(N5) *Random nodes differ.* For random nodes with M/N approximately 3 and uniform density, 'largest' is not worse than 'scheme' (M = 2016: 1.45e-12 versus 5.6e-11; slopes 1.84 versus 2.87); for arcsine-density random nodes, 'largest' is worse and steeper (slope 2.10 versus 1.28 for M = 66..1326; 1.1e-12 versus 6.4e-14 at M = 1326, ratio 17).

## Definitions

'scheme', 'largest': `givens_core.c` rule codes 0 and 1 (bit-identical to the inputs' `givens(pivot=…)` at n = 6, 10, 14). Catastrophe, unisolvent order, σ_min: as in PD-T?bivariate-lanczos-claude-503.

## Assumptions

IEEE double; real nodes; the tables of parents of Algorithm 1 ('downside-up', y-parent primary); no skip threshold (b = 0 test only).

## Status by part

Overall status: MEASURED (the status of the negative statement; the candidate 'larger pivot is a stabilising heuristic' carries the disposition REJECTED: failed, scope above).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| N1–N3 | MEASURED | `logs/r01_padua_cub.jsonl`, `r01_padua_rand.jsonl`, `r01_prefix_a.jsonl`, `r01_prefix_b.jsonl`; `analyze_r01b.py` output in `logs/analysis_r01b.txt` |
| N4 | MEASURED | `logs/r03_rules.jsonl`, `r03_rules.log` |
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
