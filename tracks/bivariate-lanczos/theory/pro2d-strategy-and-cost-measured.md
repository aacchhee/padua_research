# PD-T?bivariate-lanczos-claude-207 — Measured behaviour of PRO-2D-J (two-pass window + ω-triggered partial reorthogonalization with measured J-rows; IDEA?…-209, REJECTED on the cubic checkerboard, PD-N?…-207): passes the registered loss criterion L ≤ 10√u on 11 of 12 benchmarks (strictly semi-orthogonal, L ≤ √u at every degree, on 10 of them; L-shape reaches 1.41√u), with O(u) F-sections at every strictly semi-orthogonal degree, at 16–71% of the dot products of CGS2-against-all; costs and M-scaling to M = 10⁵

ID kind: PD-T.
Aliases: IDEA?…-209 results; L2 strategy; cost comparison vs full reorthogonalization / V+A-type CGS2; M-scaling.
Split from: none.
Split into: PD-N?…-207 (cubic-checkerboard failure of (a)). Negative parts: PD-N?…-202 (rounding-only trigger), PD-N?…-201 (no repair of the drift).

## Statement

[FP, MEASURED] u = 2^-53.

(a) **Benchmark set (M ≤ 3000; IDEA?…-209, pre-registered kill: L > 10√u, or e_F > u^{3/4} at L ≤ √u).** PRO-2D-J keeps max L ≤ 1.5e-8 on 11 benchmarks (≤ 7.6e-9 on rotπ/4, 4.3e-9 triangle, 1.5e-8 L-shape, 9.8e-9 annulus) and e_F ≤ 7.7e-15 at every semi-orthogonal degree of all 12; it is **killed on the cubic-clustered checkerboard** (L(29) = 2.0e-7 at the last degree, M − N_29 = 31). **Thresholds distinguished (audit-01, L2-F3).** Semi-orthogonality is defined in this campaign as L(n) ≤ √u = 1.0537e-8 (candidates.md conventions; IDEA?…-203); the registered kill threshold of IDEA?…-209 is the relaxed L(n) > 10√u = 1.0537e-7. Hence: 11 of 12 benchmarks pass the registered loss criterion L ≤ 10√u; **strict semi-orthogonality L ≤ √u at every degree holds on 10 of 12** — the L-shape exceeds √u at n = 29 (L = 1.2076e-8) and n = 30 (L = 1.4825593127e-8 = 1.407√u; identical in Codex audit-01's fresh execution), and the cubic checkerboard exceeds it at n = 29 (1.9702675e-7 = 18.70√u, also above 10√u: the registered kill); the annulus maximum is 9.8083e-9 = 0.931√u, rotπ/4 7.618e-9 = 0.723√u, triangle 4.272e-9 = 0.405√u (values from `logs/r02_proJ.raw.gz`). The e_F statement refers to the strictly semi-orthogonal degrees (L ≤ √u), as registered; at the L-shape degrees 29–30 (√u < L ≤ 10√u) the logged e_F is 2e-15 as well, but those degrees are outside the registered e_F criterion. The registered verdicts are unchanged: the kill on the cubic checkerboard and the failure of the secondary cost criterion below are preserved. Dot products (window + reorthogonalization + J-row measurement) / CGS2-against-all: 0.50 (rot0.3), 0.57 (rotπ/4), 0.29 (disk), 0.71 (triangle), 0.55 (L-shape), 0.57 (annulus), 0.22 (square), 0.19 (tensor), 0.16 (Padua 48), 0.24 (checkerboards), 0.31 (cubic). On product-type sets no column is reorthogonalized; the cost is the two-pass window plus the J-row measurement (2.5–3.8% of CGS2-against-all). The pre-registered secondary criterion "(reorthogonalization + measurement) ≤ 30% of CGS2-against-all" fails on rotπ/4 (0.33), triangle (0.42), L-shape (0.35), annulus (0.37).
(b) **What it does not repair.** On the non-product sets the PRO-2D-J spans drift like BJ with CGS2-against-all, within a factor ≈ 2 at the last degree (rotπ/4 θ_LB 3.8e-4, drift 5.5e-3 at n = 24; triangle θ_LB 2.7e-3, drift 2.9e-2 at n = 20; implicit J-section errors up to 1.2e-3–5.2e-3), consistent with the measured failure of the other tested schemes (PD-N?…-201).
(c) **M-scaling and wall time (rotπ/4 n = 24, N = 325; triangle n = 20, N = 231; unit weights; 2-core VM, OMP/OpenBLAS threads 2; times noisy).**

| method | dots / CGS2-all (rotπ/4) | rotπ/4 L, drift at M = 1681 / 10⁴ / 10⁵ | triangle L, drift at M = 1681 / 10⁴ / 10⁵ | time M = 10⁵ (rotπ/4, triangle) |
|---|---|---|---|---|
| BJ one pass | 0.12 | 4.2e-3, 4.5e-3 / 3.3e-4, 1.2e-3 / 6.7e-5, 6.5e-4 | 1.0, 1.9e-2 / 1.0, 1.1e-2 / 1.0, 1.7e-2 | 12.8 s, 3.8 s |
| BJ two-pass window | 0.24 | 2.5e-4, 5.5e-3 / 4.3e-5, 1.3e-3 / 2.0e-5, 6.7e-4 | 1.9e-3, 2.9e-2 / 4.8e-5, 1.3e-2 / 9.2e-5, 1.8e-2 | 29.7 s, 4.3 s |
| PRO-2D-J | 0.49–0.57 | 7.6e-9, 5.5e-3 / 4.4e-9, 1.3e-3 / 4.5e-10, 6.7e-4 | 1.0e-8, 2.9e-2 / 8.4e-9, 1.3e-2 / 1.1e-8, 1.8e-2 | 15.7 s, 9.4 s |
| adapt + two-pass window | 0.35 | 2.9e-7, 2.0e-6 / 1.3e-6, 1.4e-5 / 2.8e-7, 3.3e-5 | 4.4e-11, 2.0e-10 / 1.9e-11, 1.4e-9 / 5.3e-12, 1.8e-9 | 18.7 s, 10.1 s |
| CGS2 against all (V+A type) | 1 | 6.9e-15, 4.1e-3 / 2.2e-15, 1.4e-3 / 4.4e-15, 7.1e-4 | 6.9e-15, 2.4e-2 / 2.2e-15, 1.3e-2 / 4.4e-15, 1.9e-2 | 13.3 s, 7.9 s |
| two-relation, 2 passes | ≈ 0.36 + SVD (BLAS-3) | 6.9e-15, 6.5e-13 / 3.7e-15, 3.9e-14 / 4.4e-15, 4.3e-14 | 5.5e-13, 7.4e-12 / 7.5e-13, 5.7e-12 / 1.1e-13, 8.8e-12 | 4.9 s, 2.8 s |

(reference bound u·κ ≤ 4e-13 for every drift entry). Readings: the BJ drift does not decay towards √u with M: on rotπ/4 at n = 24 it falls by ≈ 6× from M = 1681 to 10⁵ in this sample and is ≈ 6–7e-4 at M = 10⁵ (reconstruction 01: two seeds 6.3e-4–7.2e-4; seed spread 50× at M = 1681; M-independent at n ≤ 16); flat on the triangle; partial or full reorthogonalization changes L by up to 12 decades and the drift by less than a factor 2; the dot-product ratio of PRO-2D-J is M-independent (51 901–59 783 of 105 300 on rotπ/4; 33 754–38 195 of 53 130 on the triangle).
(d) **Operation-count model (exact counts from the runs, n = degree, N = N_n).** One window pass: Σ_k |W_k| (block window ≈ n³ dot products; 12 676 at n = 24); two-pass window: twice that; CGS2-against-all: N(N − 1) ≈ n⁴/4 (105 300); ratio window/full ≈ 4/n. J-row measurement: Σ_t N_{t−1} ≈ n³/6 (4 624 at n = 24). Two-relation block (2 passes): Σ_n 4n(2n−1) ≈ (8/3)n³ dot products (38 000 at n = 24) plus a thin SVD of an M × 2n block per degree (≈ (8/3)n³ further dot-equivalents) — O(M n³) = O(M N^{3/2}), the same order as the window recurrence, against O(M N²) for CGS2-against-all. The ω-estimate costs O(N³) flops per run as coded (dense), independent of M. The J-rows are measured twice (provisional r/β₀ and final q̂_k); the provisional pass is redundant when nothing triggers, ≈ n³/6 extra dot products (≈ 2% of CGS2-against-all), counted in the ratios above (reconstruction 01).

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

PD-T?…-201 (why e_F stays O(u)), -202/-205 (identities of the residual that stays), -208 (θ_LB), -203 (estimate).

## Checks

`python3 -I l2_r02_pro.py --jmeasure > …/logs/r02_proJ.raw`; `OMP_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2 python3 -I l2_r02_cost.py --sets rotpi4,triangle --M 1681,10000,100000 > …/logs/r02_cost.jsonl` (≈ 6 min). Independent rerun: Codex audit-01 (Python 3.12.14, NumPy 2.3.5, threads 1; `topics/bivariate-lanczos-20261031/audit-01/L2/proJ-rerun.log`, `pro-rerun.log`) reproduced the rounding-only trigger failure, the PRO-2D-J improvement and the cubic degree-29 kill; max L/√u = 0.7230 (rotπ/4), 0.4054 (triangle), 1.4070 (L-shape), 18.699 (cubic); total-dot/full ratios 0.567740, 0.705496, 0.549890, 0.312662. No fresh M = 10⁵/10⁶ timing or scaling run. The developer's own rerun of PRO-2D-J (in `l2_audit01_chi.py`, same environment as R02) gives the same L-shape and cubic maxima (1.48e-8, 1.97e-7).

## Sources

Zhu–Nakatsukasa 2026 (LIT?…-024/025): CGS2 against all previous columns, O(MN²) — the cost comparator; reconstruction 01 identifies, from the paper text read through a tool digest (UNVERIFIED against their code), ZN's Remark 3.2 rule in grevlex order with the BJ selection, so (c)'s "V+A type" row would be their multivariate V+A in grevlex order up to scaling; our row is our implementation, not their code. Simon 1984 (LIT?…-212): about 20% of full reorthogonalization for moderately conditioned single-operator problems (as digested) — the 2D figure here is 50–70% on hard non-product sets because nearly every column of the top degrees needs reorthogonalization.

## Proof or evidence

Measured.

## Scope

PRO-2D-J is a strategy for loss of orthogonality of the BJ recurrence; within the tested range it keeps the loss within the registered level 10√u — strictly within √u except on the L-shape at n = 29–30 (1.41√u) — with O(u) F-sections, cheaply on product-type and mildly non-product sets and at about half the cost of full reorthogonalization on hard ones; on the cubic checkerboard it fails (PD-N?…-207). It does not deliver a basis of S_n on non-product measures (b); for that the selection or the relation count must change (PD-T?…-206).

## Open items

M = 10⁶ (Runs needed); the cubic-checkerboard last-degree failure; a PRO variant for the adaptive selection (needs an ω-estimate with both sections partly implicit, PD-T?…-205).

## History

- 2026-11-01: created (Claude Opus 5.5, xhigh; L2 R02). IDEA?…-209 written after the -208 failure and before its own run (disclosed in candidates.md).
- 2026-11-01T01:28:43+01:00: (reconstruction 01 F3/F6) title states that IDEA?…-209 is REJECTED on the cubic checkerboard (PD-N?…-207) and corrects the range; original title: "PD-T?bivariate-lanczos-claude-207 — PRO-2D-J (two-pass window + ω-triggered partial reorthogonalization with measured J-rows) keeps the BJ recurrence semi-orthogonal with O(u) F-sections on 11 of 12 benchmarks at 13–70% of the dot products of CGS2-against-all; costs and M-scaling to M = 10⁵". (F4) M-scaling sentence corrected; original: "the BJ drift does not decrease with M beyond a factor ≈ 7 (rotπ/4) and is flat on the triangle;". (§4) estimate cost and double J-row measurement noted; original: "The ω-estimate costs O(N²n) flops independent of M.". (F9) ZN identification recorded as UNVERIFIED; original: "their selection rule was not checked against BJ, so (c)'s "V+A type" row is our BJ-selection implementation, not their code.". Measurements unchanged (Claude Opus 5.5, xhigh; L2 developer, response to reconstruction 01, `directions/L2/response-recon-01.md`).
- 2026-11-01T01:29:55+01:00: Split into updated (original: "Split into: none."), reconstruction 01 F3 (Claude Opus 5.5, xhigh; L2 developer, response to reconstruction 01).
- 2026-11-01T08:32:22+01:00: (Codex audit-01, finding **L2-F3**; Claude Opus 5.5, xhigh; L2 developer, response `directions/L2/response-audit-01.md`; rules read at 8b61391613045f547589e48dcb8037a266bad8aa) The registered kill threshold (L ≤ 10√u) and the campaign's definition of semi-orthogonality (L ≤ √u) are now distinguished: 11/12 pass the registered criterion, 10/12 are strictly semi-orthogonal at every degree (L-shape 1.407√u at n = 30). Original title: "PD-T?bivariate-lanczos-claude-207 — Measured behaviour of PRO-2D-J (two-pass window + ω-triggered partial reorthogonalization with measured J-rows; IDEA?…-209, REJECTED on the cubic checkerboard, PD-N?…-207): semi-orthogonal with O(u) F-sections on 11 of 12 benchmarks at 16–71% of the dot products of CGS2-against-all; costs and M-scaling to M = 10⁵". The original (a) sentence is kept verbatim and followed by the threshold paragraph. Original Scope sentence: "PRO-2D-J is a strategy for loss of orthogonality of the BJ recurrence; within the tested range it delivers semi-orthogonality and O(u) F-sections cheaply on product-type and mildly non-product sets and at about half the cost of full reorthogonalization on hard ones." (b) wording (audit-01 L2-F1 propagation): original "On the non-product sets the PRO-2D-J spans drift exactly like BJ with CGS2-against-all (" and "), as PD-N?…-201 predicts." Original Depends on: "PD-T?…-201 (why e_F stays O(u)), -202/-205 (why the drift stays), -203 (estimate)." Original Checks ended "Independent rerun: none." Failed frozen criteria preserved unchanged: the cubic-checkerboard kill (PD-N?…-207) and the failed secondary cost criterion (≤ 30%) on rotπ/4, triangle, L-shape, annulus. Measurements, verdicts and status MEASURED unchanged.
