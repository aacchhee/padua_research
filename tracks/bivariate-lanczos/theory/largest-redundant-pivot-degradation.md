# PD-N?bivariate-lanczos-claude-506 — The 'larger redundant pivot' rule degrades point-by-point Givens updating on Padua points, with and without non-unisolvent prefixes

ID kind: PD-N.
Aliases: 'largest' pivot catastrophe; Humet/ETNA max-norm pivot as used in Algorithm 1; seed p. 395 pivot remark; OBST?bivariate-lanczos-claude-08; IDEA?bivariate-lanczos-claude-502 (prefix mechanism, refuted in the 'only' form), 013, 016.
Split from: none.
Split into: none.

## Statement

[FP, MEASURED; scope = Parameter range below.] Let Algorithm G (`givens-updating-rotation-count-backward-bound.md`) use, for each doubly-parented monomial j (one with an x-parent and a y-parent), the rule 'largest': form the rotation from whichever of the two pivot entries V(j)[j,p(j)], V'(j)[j,p'(j)] has the larger modulus, instead of the fixed primary ('scheme', y-parent first) pivot. Then:

(N1) *Degradation with n.* On Padua first-family sets Pad_n the relative Frobenius error of (H_x, H_y) with 'largest' is at the level of 'scheme' at n = 10 (ratio 0.8..1.3 for all 9 orders and both weight types), is up to 5 times 'scheme' for the random and constructed orders at n = 15..20, and grows to ratios of 1e3..1e5 at n = 50 (gepp, rpiv1-3, rand1-3; see N2). On the natural (`given`) order with cubature weights: 8.7e-9 (n = 30), 1.5e-7 (n = 40), 3.4e-4 (n = 50), 7.1e-4 (n = 62); with U(0.1,1) weights 6.1e-3 (n = 30), 2.1e-4 (n = 50), 1.9e-1 (n = 62); with unit weights 2.0e-9 (n = 30), 6.5e-5 (n = 40); against 'scheme' errors <= 1.1e-13 on the same streams; on a random order at n = 60 (unit weights, `default_rng(2)`) 2.1e-4 against 'scheme' 2.0e-12 (`logs/r03_x60.log`). The exceptions at small n are the `given` order with U(0.1,1) weights (1.1e-2 at n = 15, 1.4e-3 at n = 20, both with 'scheme' at 1e-14), so there is no 'safe n' threshold for 'largest' that holds for all weights.

(N2) *Non-unisolvence is not necessary.* On orders whose every prefix is unisolvent with min prefix sigma_min >= 4.7e-4 (gepp and rpiv1-3, `unisolvent-prefix-extension-lemma.md`), 'largest' reaches (cubature weights) 4.2e-13..1.5e-12 (n = 30), 1.8e-11..5.7e-11 (n = 40) and 9.3e-10..3.1e-9 (n = 50) against 'scheme' 3.8e-14..4.5e-14, 6.0e-14..7.8e-14 and 1.1e-13..1.2e-13: ratios 11..33, 250..720 and 8.6e3..2.8e4; the U(0.1,1)-weight values are similar (within a factor 2.5). The error grows by a factor 15..50 per Delta n = 10 (gepp: 2.8e-14, 4.2e-13, 1.8e-11, 9.3e-10 for n = 20, 30, 40, 50). Under the operational definition of candidates.md (catastrophe = error ratio >= 1e3 and 'largest' error >= 1e-10), 16 of the 54 (weights, n, order) cases with n >= 20 and all prefixes unisolvent are catastrophic: the 14 cases at n = 50 (gepp, rand1-3, rpiv1-3, for each of the two weight types) plus n = 40 rand3 for both weight types (listing in `logs/analysis_r01b.txt`). Hence the kill test of plan L5-Q1 for the prefix mechanism *fires*: 'the catastrophe occurs only on orders with non-unisolvent intermediate prefixes' is false in this scope. 14 of the 16 have min sigma_min >= 1e-8 (the pre-registered tolerance); the two with 3.0e-9 are n = 50 rand3 (both weight types). The 8 cases of gepp and rpiv1-3 at n = 50 (4 per weight type) (min sigma_min >= 4.7e-4) are unaffected by any tolerance choice.

*Scope of the kill (reconstruction finding M4).* The kill of the binary prefix mechanism rests on the **operational catastrophe threshold** (ratio >= 1e3 and error >= 1e-10), not on the seed's magnitude of about 7e-4. On the well-conditioned unisolvent orders the 'largest' error stays <= 3.1e-9 up to n = 50; errors of 1e-4 or more occur only on non-unisolvent orders (given/sortx: 3.4e-4 at n = 50, 7.1e-4 at n = 62) or on the near-singular REPRO order (min prefix sigma_min 9.7e-10: 2.1e-4), and the largest error on an all-unisolvent order in the developer data is 5.9e-7 (n = 50 rand3, sigma_min 3.0e-9). The data fit a **graded prefix-conditioning effect** rather than a binary one: 'largest' degrades on every order at about x15-50 per Delta n = 10, and reaches >= 1e-6 only on singular or near-singular (sigma_min <~ 1e-9) prefix sequences in the tested range. This last statement is a description of the data, neither tested nor refuted by the kill. The classification itself is fragile (n = 40 rand2 counts as non-unisolvent only through a K = 2 prefix with two equal x-coordinates, yet behaves like rand1/rand3). The independent reconstruction confirmed the kill with its own code and orders (geppR1, geppR2 with random row scalings; certified min sigma_min >= 4.3e-6 at n = 50; 'largest' 2.1e-9, 1.8e-9, ratios 1.6e4, 1.8e4).

(N3) *Non-unisolvence aggravates it.* Median 'largest'/'scheme' ratio over the two weight types, by order class: `given` 1e9..1e12 at n = 30, 40, 50 (also 8e11 at n = 15 and 5e10 at n = 20, driven by the random-weight stream); `sortx` 5e4 (n = 30), 1.6e7 (n = 40), 7e9 (n = 50); random orders (all prefixes unisolvent except n = 15, 40 rand2) 33, 1.2e3, 1e5; gepp/rpiv 30, 460, 1.2e4. So the singular-prefix streams are 3..10 orders of magnitude worse than the unisolvent ones at the same n (3 for `sortx` n = 30 against random orders, 10 for `given` n = 30 against gepp/rpiv). Singular prefixes are not sufficient for a large 'largest' error (cubature weights, n = 15 and 20, `given` and `sortx`: ratio 1.1..1.4; random weights n = 20 `sortx`: 2.7) and not necessary (N2).

(N4) *Magnitude-threshold variants are separate records.* The variants that take the alternative pivot only when it is kappa times larger (pivk10, pivk100, the reading of VB-C p. 395 'if two pivots differ in some orders of magnitude') or compare pair norms (pairnorm1, pairnorm100) are recorded, with their own scoped negative statement, in `magnitude-threshold-pivot-rules-failure.md` (PD-N?bivariate-lanczos-claude-507); the detector-threshold deferral rules in `fifo-threshold-deferral-failure.md` (PD-N?bivariate-lanczos-claude-508). Not repeated here (reconstruction finding L9). The only fact used here: 'pairnorm1' coincides with 'largest' within 15% on rand1-3 and gepp (n = 20, 30), so 'largest' is the kappa = 1 member of that family.

(N5) *Random nodes differ.* For random nodes with M/N approximately 3 and uniform density, 'largest' is not worse than 'scheme' (M = 2016: 1.45e-12 versus 5.6e-11; slopes 1.84 versus 2.87); for arcsine-density random nodes, 'largest' is worse and steeper (slope 2.10 versus 1.28 for M = 66..1326; 1.1e-12 versus 6.4e-14 at M = 1326, ratio 17).

(N6) *What fails is the zero pattern, not the backward error (REVIEWER-MEASURED, reconstruction 01, `b_kill.jsonl`; not rerun by me).* On all-prefix-unisolvent orders 'scheme' and 'largest' have the same orthogonal-similarity residual (2.7e-15 at n = 30, 4.4e-15 at n = 50) and the same first-column residual, while the structure defect (largest entry below the candidate pivots, relative to ||H||_F/sqrt(M)) tracks the forward error (n = 50 gepp: 8.4e-10 for 'largest' versus 6.8e-14 for 'scheme'; forward error 9.3e-10 versus 1.2e-13).

## Definitions

'scheme', 'largest': `givens_core.c` rule codes 0 and 1 (bit-identical to the inputs' `givens(pivot=…)` at n = 6, 10, 14). Catastrophe, unisolvent order, σ_min: as in PD-T?bivariate-lanczos-claude-503.

## Assumptions

IEEE double; real nodes; the tables of parents of Algorithm 1 ('downside-up', y-parent primary); no skip threshold (b = 0 test only).

## Status by part

Overall status: MEASURED (the status of the negative statement; dispositions below).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| N1–N3 | MEASURED | `logs/r01_padua_cub.jsonl`, `r01_padua_rand.jsonl`, `r01_prefix_a.jsonl`, `r01_prefix_b.jsonl`; `analyze_r01b.py` output in `logs/analysis_r01b.txt` |
| N4 | pointer | PD-N?bivariate-lanczos-claude-507, -508 |
| N6 | REVIEWER-MEASURED | reconstruction 01 `b_kill.jsonl` |
| N5 | MEASURED | `logs/r01_random.jsonl`, `logs/r01_random_cheb.jsonl` |
| a mechanism (why larger pivot degrades) | OPEN | see Open items |

Candidate / claim disposition (wording corrected after reconstruction findings L7, L8):
- Claim 'the "largest" catastrophe occurs only on orders with a non-unisolvent intermediate prefix' (IDEA?bivariate-lanczos-claude-502): REJECTED: refuted (the negation is established within the scope below; MEASURED, operational threshold, see the N2 scope paragraph).
- Mechanism 'choose the larger redundant pivot (kappa = 1) as a stabilising rule in point-by-point Givens updating': REJECTED: failed (it does not achieve its stability aim in the scope below).
- The VB-C p. 395 suggestion proper ('if two pivots differ in some orders of magnitude' = the kappa >> 1 rule) is **not** the 'largest' rule; its rejection rests on PD-N?bivariate-lanczos-claude-507, not on the 'largest' data here.

## Negative-result scope

Attempted mechanism: IDEA?bivariate-lanczos-claude-013/016/502 — choose the larger redundant pivot (kappa = 1); and the diagnostic claim that its failures occur only on non-unisolvent prefixes.
Parameter range: Algorithm 1, real nodes, IEEE double, Padua first-family n = 10, 15, 20, 30, 40, 50, 62 (cubature weights; U(0.1,1) weights; unit weights up to n = 40 in `r01_padua_unif.jsonl`), orders given, sortx, rand1–3, gepp, rpiv1–3 (the last two only up to n = 50), and random nodes M ≤ 2016. The data support 'no catastrophe at n <= 10' (ratios 0.8-1.3 for all 9 orders and both weight types) and nothing stronger: a catastrophe occurs at n = 15 (`given` order, U(0.1,1) weights, 1.1e-2, ratio 1.6e12; reconstruction finding M5). Magnitude-threshold and deferral variants: see PD-N?bivariate-lanczos-claude-507 and -508.

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

2026-10-31T23:00Z, Claude Sonnet 5.5 (high), response to L5 reconstruction 01: M1 (N6 added: zero pattern, not backward error), M4 (kill scope, graded statement), M5 (scope n <= 10), L7 (p. 395 is the kappa rule; rejection moved to 507), L8 (refuted/failed wording), L9 (N4 split into PD-N 507 and 508).
