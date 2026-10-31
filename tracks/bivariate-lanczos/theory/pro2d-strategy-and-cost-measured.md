# PD-T?bivariate-lanczos-claude-207 — PRO-2D-J (two-pass window + ω-triggered partial reorthogonalization with measured J-rows) keeps the BJ recurrence semi-orthogonal with O(u) F-sections on 11 of 12 benchmarks at 13–70% of the dot products of CGS2-against-all; costs and M-scaling to M = 10⁵

ID kind: PD-T.
Aliases: IDEA?…-209 results; L2 strategy; cost comparison vs full reorthogonalization / V+A-type CGS2; M-scaling.
Split from: none.
Split into: none. Negative parts: PD-N?…-202 (rounding-only trigger), PD-N?…-201 (no repair of the drift).

## Statement

[FP, MEASURED] u = 2^-53.

(a) **Benchmark set (M ≤ 3000; IDEA?…-209, pre-registered kill: L > 10√u, or e_F > u^{3/4} at L ≤ √u).** PRO-2D-J keeps max L ≤ 1.5e-8 on 11 benchmarks (≤ 7.6e-9 on rotπ/4, 4.3e-9 triangle, 1.5e-8 L-shape, 9.8e-9 annulus) and e_F ≤ 7.7e-15 at every semi-orthogonal degree of all 12; it is **killed on the cubic-clustered checkerboard** (L(29) = 2.0e-7 at the last degree, M − N_29 = 31). Dot products (window + reorthogonalization + J-row measurement) / CGS2-against-all: 0.50 (rot0.3), 0.57 (rotπ/4), 0.29 (disk), 0.71 (triangle), 0.55 (L-shape), 0.57 (annulus), 0.22 (square), 0.19 (tensor), 0.16 (Padua 48), 0.24 (checkerboards), 0.31 (cubic). On product-type sets no column is reorthogonalized; the cost is the two-pass window plus the J-row measurement (2.5–3.8% of CGS2-against-all). The pre-registered secondary criterion "(reorthogonalization + measurement) ≤ 30% of CGS2-against-all" fails on rotπ/4 (0.33), triangle (0.42), L-shape (0.35), annulus (0.37).
(b) **What it does not repair.** On the non-product sets the PRO-2D-J spans drift exactly like BJ with CGS2-against-all (rotπ/4 θ_LB 3.8e-4, drift 5.5e-3 at n = 24; triangle θ_LB 2.7e-3, drift 2.9e-2 at n = 20; implicit J-section errors up to 1.2e-3–5.2e-3), as PD-N?…-201 predicts.
(c) **M-scaling and wall time (rotπ/4 n = 24, N = 325; triangle n = 20, N = 231; unit weights; 2-core VM, OMP/OpenBLAS threads 2; times noisy).**

| method | dots / CGS2-all (rotπ/4) | rotπ/4 L, drift at M = 1681 / 10⁴ / 10⁵ | triangle L, drift at M = 1681 / 10⁴ / 10⁵ | time M = 10⁵ (rotπ/4, triangle) |
|---|---|---|---|---|
| BJ one pass | 0.12 | 4.2e-3, 4.5e-3 / 3.3e-4, 1.2e-3 / 6.7e-5, 6.5e-4 | 1.0, 1.9e-2 / 1.0, 1.1e-2 / 1.0, 1.7e-2 | 12.8 s, 3.8 s |
| BJ two-pass window | 0.24 | 2.5e-4, 5.5e-3 / 4.3e-5, 1.3e-3 / 2.0e-5, 6.7e-4 | 1.9e-3, 2.9e-2 / 4.8e-5, 1.3e-2 / 9.2e-5, 1.8e-2 | 29.7 s, 4.3 s |
| PRO-2D-J | 0.49–0.57 | 7.6e-9, 5.5e-3 / 4.4e-9, 1.3e-3 / 4.5e-10, 6.7e-4 | 1.0e-8, 2.9e-2 / 8.4e-9, 1.3e-2 / 1.1e-8, 1.8e-2 | 15.7 s, 9.4 s |
| adapt + two-pass window | 0.35 | 2.9e-7, 2.0e-6 / 1.3e-6, 1.4e-5 / 2.8e-7, 3.3e-5 | 4.4e-11, 2.0e-10 / 1.9e-11, 1.4e-9 / 5.3e-12, 1.8e-9 | 18.7 s, 10.1 s |
| CGS2 against all (V+A type) | 1 | 6.9e-15, 4.1e-3 / 2.2e-15, 1.4e-3 / 4.4e-15, 7.1e-4 | 6.9e-15, 2.4e-2 / 2.2e-15, 1.3e-2 / 4.4e-15, 1.9e-2 | 13.3 s, 7.9 s |
| two-relation, 2 passes | ≈ 0.36 + SVD (BLAS-3) | 6.9e-15, 6.5e-13 / 3.7e-15, 3.9e-14 / 4.4e-15, 4.3e-14 | 5.5e-13, 7.4e-12 / 7.5e-13, 5.7e-12 / 1.1e-13, 8.8e-12 | 4.9 s, 2.8 s |

(reference bound u·κ ≤ 4e-13 for every drift entry). Readings: the BJ drift does not decrease with M beyond a factor ≈ 7 (rotπ/4) and is flat on the triangle; partial or full reorthogonalization changes L by up to 12 decades and the drift by less than a factor 2; the dot-product ratio of PRO-2D-J is M-independent (51 901–59 783 of 105 300 on rotπ/4; 33 754–38 195 of 53 130 on the triangle).
(d) **Operation-count model (exact counts from the runs, n = degree, N = N_n).** One window pass: Σ_k |W_k| (block window ≈ n³ dot products; 12 676 at n = 24); two-pass window: twice that; CGS2-against-all: N(N − 1) ≈ n⁴/4 (105 300); ratio window/full ≈ 4/n. J-row measurement: Σ_t N_{t−1} ≈ n³/6 (4 624 at n = 24). Two-relation block (2 passes): Σ_n 4n(2n−1) ≈ (8/3)n³ dot products (38 000 at n = 24) plus a thin SVD of an M × 2n block per degree (≈ (8/3)n³ further dot-equivalents) — O(M n³) = O(M N^{3/2}), the same order as the window recurrence, against O(M N²) for CGS2-against-all. The ω-estimate costs O(N²n) flops independent of M.

## Definitions

As in candidates.md (IDEA?…-209, cost protocol) and PD-T?…-201/-206. "Dots" = inner products of length M.

## Assumptions

Double precision; NumPy 2.5.3 / OpenBLAS, 2 threads; single VM (timings indicative only).

## Status by part

Overall status: MEASURED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| (a) | MEASURED | `logs/r02_proJ.raw.gz`, `logs/r02_verdicts.txt` |
| (b) | MEASURED | same, and `logs/r02_cost.jsonl` |
| (c) | MEASURED | `logs/r02_cost.jsonl` |
| (d) counts | exact counts of the implemented algorithms (routine) | |

## Depends on

PD-T?…-201 (why e_F stays O(u)), -202/-205 (why the drift stays), -203 (estimate).

## Checks

`python3 -I l2_r02_pro.py --jmeasure > …/logs/r02_proJ.raw`; `OMP_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2 python3 -I l2_r02_cost.py --sets rotpi4,triangle --M 1681,10000,100000 > …/logs/r02_cost.jsonl` (≈ 6 min). Independent rerun: none.

## Sources

Zhu–Nakatsukasa 2026 (LIT?…-024/025): CGS2 against all previous columns, O(MN²) — the cost comparator; their selection rule was not checked against BJ, so (c)'s "V+A type" row is our BJ-selection implementation, not their code. Simon 1984 (LIT?…-212): about 20% of full reorthogonalization for moderately conditioned single-operator problems (as digested) — the 2D figure here is 50–70% on hard non-product sets because nearly every column of the top degrees needs reorthogonalization.

## Proof or evidence

Measured.

## Scope

PRO-2D-J is a strategy for loss of orthogonality of the BJ recurrence; within the tested range it delivers semi-orthogonality and O(u) F-sections cheaply on product-type and mildly non-product sets and at about half the cost of full reorthogonalization on hard ones. It does not deliver a basis of S_n on non-product measures (b); for that the selection or the relation count must change (PD-T?…-206).

## Open items

M = 10⁶ (Runs needed); the cubic-checkerboard last-degree failure; a PRO variant for the adaptive selection (needs an ω-estimate with both sections partly implicit, PD-T?…-205).

## History

- 2026-11-01: created (Claude Opus 5.5, xhigh; L2 R02). IDEA?…-209 written after the -208 failure and before its own run (disclosed in candidates.md).
