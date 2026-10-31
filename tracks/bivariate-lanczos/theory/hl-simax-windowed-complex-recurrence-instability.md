# PD-N?bivariate-lanczos-claude-102 — The windowed complex (N, N*) recurrence of HL SIMAX 2002 loses orthogonality exponentially from low degree

ID kind: PD-N.
Aliases: HL SIMAX Algorithm 1 instability; (N, N*) window instability; N*-defect growth.
Split from: none.
Split into: none.

## Statement

[FP, MEASURED] Our implementation of HL SIMAX 2002 Algorithm 1 (N = X + iY applied to every vector of cycle k−1, N* to its first vector; window as in the listing on pp. 1079–1080: first vector against cycles k−2, k−1; N-product of (k−1, s−1) against cycle k−2 from index s−1, cycle k−1, cycle k up to s−1; ORTH = MGS with a second pass when the norm drops below 0.707) loses orthogonality like roughly 3ⁿ from degree n ≈ 6 on every node set tested, including tensor Chebyshev 41², Padua with cubature weights and random squares (e.g. random square M = 1681: 2.8e-12, 1.5e-7, 1.7e-4, 0.93 at n = 12, 20, 24, 40). The N*-defect max‖(I − U_nU_n*)N*U_{n−1}‖ grows at the same rate while the N-defect stays at 1e-15; with the block window (degrees k−2..k) the growth is the same; with full orthogonalization it disappears (2.3e-15 at n = 16); in long double the loss scales with ε. The minimal Ritz residuals of its N_k coincide with ρ_Z of the real recurrence until the simax span degrades, and never predict its loss.

## Negative-result scope (PD-N only)

Attempted mechanism: "the (N, N*) window recurrence behaves like Hermitian Lanczos in finite precision, with loss tied to convergence of the Ritz values of N_k" (HL SIMAX p. 1088 observation, LIT?bivariate-lanczos-claude-119; as a quantitative predictor, plan L1-Q1's N_k object).
Parameter range: every R01 node set (random squares M = 1681, 6724; rotations; tensor 41²; Padua n = 48, 80 cubature; Padua 48 uniform; L-shape random/grid; annulus), degrees 4–40 (48 for Padua), ORTH as above. Our implementation only; HL's own code was not available.

## Statement status

Overall status: MEASURED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| exponential loss from n ≈ 6 on all sets | MEASURED | `logs/r01_*.raw` (method 'simax'); `logs/r01_verdict.txt` |
| window-size independence, full-orthogonalization control, ε-scaling | MEASURED | `code/L1/l1_simax_variants.py`, log `topics/bivariate-lanczos-20261031/directions/L1/logs/r01_simax_variants.log` (random 1681 seed 0, n ≤ 20; long double n ≤ 14) |
| structural explanation (every N-product's truncation relies on the implicit N*-relations) | CONDITIONAL reasoning, not a proof | R01 §3 M5; PD-T?…-101 (exact supports) |

Candidate / claim disposition: the mechanism "HL SIMAX window recurrence is Lanczos-like" is REJECTED: failed for our implementation within the stated range.
Rejection reason: failed (MEASURED). HL SIMAX's own examples (N ≤ 1000 with ≤ 50 stored vectors, i.e. low degree) are consistent with this measurement (measured loss ≤ 4e-14 up to degree 8, M = 1681).

## Depends on

PD-T?…-101 (window supports; Z ≅ N_k).

## Checks

`tracks/bivariate-lanczos/code/L1/l1_recurrence.py::recurrence_simax` (the implementation used in all R01 runs); `code/L1/l1_simax_variants.py` (window variants, long double): `python3 -I l1_simax_variants.py`.

## Sources

HL SIMAX 2002 pp. 1079–1080 (Algorithm 1 listing), p. 1087–1088 (ORTH, observation), fulltext read in the scratchpad.

## Proof or evidence

Measured; see the logs.

## Scope

Statement about our implementation of the published listing; it is not a statement about the exact-arithmetic algorithm (whose window is exact, Thm 3.7) nor about the real (H, K) recurrence of HL BIT, which is stable on product-aligned supports (PD-T?…-107).

## Open items

An independent implementation by the auditor.

## History

- 2026-10-31: created (Claude Opus 5.5, xhigh; L1 R01).
