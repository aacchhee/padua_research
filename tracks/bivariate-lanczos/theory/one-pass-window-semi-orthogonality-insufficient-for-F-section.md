# PD-N?bivariate-lanczos-claude-206 — With a one-pass CGS window, semi-orthogonality (max|Q̂ᵀQ̂ − I| ≤ √u) does not give O(u) F-sections: the window cascade loses local orthogonality

ID kind: PD-N.
Aliases: unconditional F-part of IDEA?…-203 failed; one-pass window counterexamples; local hypothesis of Theorem A is not supplied by semi-orthogonality.
Split from: PD-T?…-204 (a) and candidates.md (R01 dispositions), after reconstruction 01 finding F3.
Split into: none.

## Statement

[FP, MEASURED] BJ block window with one CGS pass, u = 2⁻⁵³, u^{3/4} = 1.1e-12. At degrees with L(n) ≤ √u the F-section error e_F = max|W_nᵀFW_{n−1} − T_F|/‖(X,Y)‖ exceeds u^{3/4}: rot0.3 plain n = 18, 20 (max 8.1e-11; oracle partial n = 18–24, max 6.9e-10), triangle n = 8, 10 (max 1.4e-10, plain and oracle), annulus plain n = 16 (4.1e-12) and oracle n = 16–30 (max 7.4e-11). In every case the local level μ (max in-window |Ω|) is ≥ 1.2e-11 and e_F ≈ 0.1–0.6 μ. With two-pass windows or CGS2 against all previous columns e_F ≤ 7.7e-15 at every semi-orthogonal degree of all 12 benchmarks (PD-T?…-204). Reconstruction 01 reproduced e_F = 2.0e-12 and 1.45e-10 (triangle n = 8, 10) and 7.9e-11 (rot0.3 n = 20) with independent code.

## Negative-result scope (PD-N only)

Attempted mechanism: IDEA?…-203 F-part in its unconditional form "semi-orthogonality √u alone ⇒ O(u) F-section" for one-pass CGS windows.
Parameter range: the 12 R01 benchmarks (failures on rot0.3, triangle, annulus), M ≤ 3000, n ≤ 47, plain and oracle-partial runs. The corrected statement (Theorem A with the local-orthogonality hypothesis, PD-T?…-201) is not affected.

## Status by part

Overall status: MEASURED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| counterexamples | MEASURED | `directions/L2/logs/r01_sections.raw.gz`, `r01_verdicts.txt`; reconstruction 01 rerun |

Candidate / claim disposition: IDEA?…-203 (one-pass F-part, unconditional form) REJECTED. Rejection reason: failed.

## Depends on

PD-T?…-201 (explains the pattern), PD-T?…-204.

## Checks

`python3 -I tracks/bivariate-lanczos/code/L2/l2_r01_sections.py`; reconstruction 01: `review_L2/rl2_thmA.py`, `rl2_sections.py`.

## Sources

Jia–Li 2021 (arXiv digest, via reconstruction 01): local orthogonality is an explicit part of the single-operator semi-orthogonality template as well; in 1D it is automatic (Paige).

## Proof or evidence

Measured.

## Scope

This is the evidence that Theorem A's extra hypothesis is needed in practice for one-pass windows; it also fires the frozen kill clause (ii) for the F-part with one-pass windows.

## Open items

None beyond PD-T?…-201.

## History

- 2026-11-01T01:29:29+01:00: created from PD-T?…-204 (a) in response to reconstruction 01 finding F3 (Claude Opus 5.5, xhigh; L2 developer).
