# PD-N?bivariate-lanczos-claude-201 — With the BJ selection, semi-orthogonality (and even full CGS2 reorthogonalization) does not give accurate J-sections or J-closed spans on non-product measures: the computed spaces drift from S_n

Final ID: **PD-N013** (allocated at PR preparation, 2026-11-01; the provisional ID above and in the text is retained as provenance — see ID_CROSSWALK.md).

ID kind: PD-N.
Aliases: "reorthogonalization does not cure the non-product instability"; H_drift killed; J-part of L2-Q1(b) killed; V+A-type CGS2 with the BJ selection drifts; commutator channel survives reorthogonalization.
Split from: none (J-part of the L2-Q1(b) target; positive F-part is PD-T?…-201).
Split into: none.

## Statement

[FP, MEASURED] For the BJ window recurrence (block window), u = 2^-53, on the benchmarks below:

(a) **J-section, kill test fires.** At degrees where the run is semi-orthogonal (L(n) ≤ √u), the implicit J-section error e_H(n) = max|W_nᵀJW_{n−1} − Ĥ_J|/‖(X,Y)‖ exceeds u^{3/4} on 8 of 12 benchmarks: on rot0.3, rotπ/4, disk, triangle, L-shape, annulus and the cubic-clustered checkerboard for every run type — plain CGS, CGS2 against all previous vectors ("fullcgs2", Q̂ orthonormal to ≤ 7e-15), oracle partial reorthogonalization at √u, and the two-pass-window variants — and on the square for the plain and oracle runs only (n = 32). Worst e_H with fullcgs2: 5.9e-7 (rot0.3), 2.8e-4 (rotπ/4), 5.3e-10 (disk), 8.4e-4 (triangle), 5.5e-3 (L-shape), 1.3e-2 (annulus), 9.8e-12 (cubic). The formed J-columns (t,0) are accurate with fullcgs2 (e_τ ≤ 2.9e-15) but not at semi-orthogonality level: e_τ > u^{3/4} on 9 benchmarks under oracle or two-pass-window+oracle partial reorthogonalization (e.g. rotπ/4 3.4e-9, triangle 2.7e-9, L-shape 1.0e-9, annulus 1.2e-9, cubic 2.6e-9).
(b) **Spans are not J-closed after full reorthogonalization.** With fullcgs2 the J-defect δ_J(s) gives, by PD-T?…-208 (formerly PD-T?…-202 part 5), the reference-free lower bound max(θ_s, θ_{s+1}) ≥ δ_J(s)/(2‖J‖) on the principal angles between the computed and the exact graded spaces (so the reported maxima over s < n bound max_{s≤n} θ_s, not θ_n alone): 4.4e-7 (rot0.3, n = 24), 2.8e-4 (rotπ/4, n = 24), 7.8e-4 (triangle, n = 20), 8.7e-3 (L-shape, n = 30), 1.3e-2 (annulus, n = 30); first exceeding √u at n = 24, 20, 16, 24, 24. The F-defect stays ≤ 1.5e-15 on every run.
(c) **Drift against a well-conditioned reference.** For the rotated squares, S_n is rotation invariant, so the product-Chebyshev Vandermonde in the unrotated frame is a reference with u·κ ≤ 4.2e-13 (n ≤ 24). The fullcgs2 span drifts from it by 1.9e-8 (rot0.3, n = 20), 5.2e-6 (n = 24); 7.1e-8 (rotπ/4, n = 18), 2.5e-6 (n = 20), 4.1e-3 (n = 24). The plain run has the same drift (rotπ/4: 4.5e-3 at n = 24).
(d) **Controls.** Tensor 41², Padua 48 (cubature weights) and the Chebyshev–Lobatto and equispaced checkerboards, fullcgs2: max (e_F, e_τ, e_H) = (7.7e-15, 1.9e-14, 1.9e-14), (1.7e-15, 1.7e-15, 1.7e-15), (1.4e-15, 2.0e-15, 2.0e-15), (8.9e-16, 6.5e-16, 1.8e-15); plain runs e_H ≤ 2.0e-14 except equispaced 9.8e-14; δ_J/(2‖J‖) ≤ 8.3e-15 and drift ≤ 9.2e-15 (fullcgs2; equispaced drift is reference-limited, u·κ up to 4.2e-8). The cubic-clustered checkerboard is product-type: δ_J stays ≤ 2.8e-15 there; its e_H failures are of the coefficient channel (n ≥ 16).

## Negative-result scope (PD-N only)

Attempted mechanism: IDEA?…-203 (J-part) "semi-orthogonality √u guarantees O(u) sections" for the J-section; IDEA?…-204 (H_drift) "full reorthogonalization keeps span(Q̂_n) close to S_n"; with the BJ selection rule (column (t,0) = X·(t−1,0), others Y·(t−1,j−1)), block window.
Parameter range: the 12 benchmarks of directions/L2/candidates.md (M = 496–3000, n ≤ 47), double precision, NumPy 2.5.3; reorthogonalization schemes plain CGS, two-pass window, oracle partial at √u (threshold set u^{3/4}), CGS2 against all previous columns. Not covered: other selection rules (reconstruction 01's balanced/adaptive rules), MGS/HL ORTH, M > 3000, the HL mirror ordering.

## Status by part

Overall status: MEASURED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| (a) J-section kill under semi-orthogonality | MEASURED | `logs/r01_sections.raw`, `r01_sections_w2.raw`, `r01_verdicts.txt` (IDEA-203 block) |
| (b) J-defect / reference-free drift bound | MEASURED (bound itself PROVED in PD-T?…-208, formerly PD-T?…-202 part 5) | same logs, `thetaLB` |
| (c) drift vs unrotated reference | MEASURED | same logs, `drift_unrot` |
| (d) controls | MEASURED | same logs |

Candidate / claim disposition: IDEA?…-203 J-part REJECTED (failed, scope above); IDEA?…-204 REJECTED (failed, scope above; see disclosure below).
Rejection reason: failed.

## Depends on

PD-T?…-201 (definitions), PD-T?…-202 (decomposition), PD-T?…-208 (drift bound), PD-T?…-101/-104 (CONDITIONAL inputs).

## Checks

Commands (from `tracks/bivariate-lanczos/code/L2/`): `python3 -I l2_r01_sections.py > …/L2/logs/r01_sections.raw`; `python3 -I l2_r01_sections.py --w2 > …/L2/logs/r01_sections_w2.raw`; `python3 -I l2_r01_verdicts.py …/L2/logs > …/L2/logs/r01_verdicts.txt`. Evaluation floor (pre-registered: product set, full reorthogonalization, all section errors ≤ 10²u = 1.1e-14): met on Padua 48 and the Chebyshev–Lobatto/equispaced checkerboards, missed by a factor 1.7 on tensor 41² (e_τ = e_H = 1.9e-14); no verdict is affected (a failure means e > u^{3/4} = 1.1e-12, i.e. ≥ 58× above 1.9e-14). Independent rerun: none of the R01 section suite itself. Independent confirmations: reconstruction 01 (verdict order below); Codex audit-01's new stable-reference experiment (`topics/bivariate-lanczos-20261031/audit-01/L2/independent_drift.py`, imports no developer or reviewer code; `independent-drift.log`; Python 3.12.14, NumPy 2.3.5, threads 1): BJ + two CGS passes against all earlier columns, seed-11 nodes, max Gram error 6.88e-15 in double; drift at the last degree (QR + direct residual singular values) 4.105e-3 (rotated square, n = 24; Legendre and Chebyshev product references in the inverse-rotated frame, κ = 783 and 4263, agreeing to 6.6e-13) and 1.016e-2 (triangle, n = 20; Dubiner reference, κ = 101); x87 long double (u = 2^-64): 7.69e-6 and 8.08e-6; running defect bound (PD-T?…-208) 2.82e-4 and 7.77e-4 in double.

## Sources

None (own runs). Reconstruction 01 identifies, from the ZN paper text read through a tool digest (UNVERIFIED; their code not inspected), BJ + CGS2-against-all with ZN's multivariate V+A in grevlex order (their Remark 3.2 rule); if confirmed, the drift applies to that published algorithm on these sets (ZN's reported experiments are on a tensor domain and an ellipse; no conflict). Reconstruction 01 also did not find the LIT?…-025 quotation in arXiv v2 (digest). Earlier text: Zhu–Nakatsukasa 2026 (LIT?…-024/025) use CGS2 against all previous columns; whether their selection rule coincides with BJ was not checked — no statement about their results is made.

## Proof or evidence

Measured; see logs. Disclosure: the pre-registered H_drift rule (box-frame Chebyshev reference with u·κ < 1e-11) is non-discriminating wherever the drift exceeds √u — the box reference has u·κ ≈ drift (e.g. rotπ/4 n = 16: 3.3e-8 vs 3.2e-8), so under the pre-registered rule alone H_drift is **inconclusive**. The kill rests on two criteria added after the rotπ/4 smoke test (candidates.md amendment, 00:12): the reference-free bound of PD-T?…-202 part 5 (now PD-T?…-208) and the unrotated-frame reference. Both fire on rot0.3 and rotπ/4; the reference-free bound also fires on triangle, L-shape and annulus.

**Verdict order (reconstruction 01, §5).** (1) Pre-registered H_drift rule (box-frame Chebyshev reference): inconclusive. (2) Post-hoc criteria (reference-free bound, unrotated-frame reference): killed on five sets. (3) Independent confirmation: reconstruction 01's well-conditioned extended-precision references (Legendre/Chebyshev product bases in the unrotated frame, κ ≤ 7.8e2 at n = 24; Koornwinder–Dubiner on the triangle, κ ≤ 1e2; agreement between references ≤ 2.7e-15) give drift 3.6e-3 (rotπ/4, n = 24) and 1.3e-2 (triangle, n = 20) for BJ + CGS2-against-all, scaling linearly with the working precision (long double / double ratio 6.5e-4–2.1e-3 vs u_LD/u = 4.9e-4) — the pre-registered *form* of the rule with a well-conditioned reference kills H_drift. [Wording qualified after audit-01: "scaling linearly" rests on two precisions only; the drift decreases roughly in proportion to the working precision (audit-01's rerun: ratios 1.87e-3 rotated square, 7.95e-4 triangle, vs 2^-11 = 4.88e-4), consistent with rounding excitation; this is not an exact or universal linear-u law, and operation order and rounding realization matter. (4) Codex audit-01's independent stable-reference experiment (Checks) confirms the drift on the two named sets; it does not turn the post-hoc criteria into pre-registered ones.] **Realization variance:** drift magnitudes at n = 24 vary 15–50% between implementations (BLAS path) and up to 50× between node samples at M = 1681; only orders of magnitude and verdicts are robust.

## Scope

Within the stated range: with the BJ selection no reorthogonalization scheme tested — including the O(MN²) CGS2-against-all scheme — produces an orthonormal basis of S_n on non-product measures beyond moderate degree; the orthogonality it restores is orthogonality of the wrong (drifted) spaces. The mechanism identified is the commutator/shadow recursion of PD-T?…-202, whose recursion contains no reset term; that the residual stays large under reorthogonalization is the measured content of this record, not a consequence of PD-T?…-202 (audit-01, L2-F1). This record is a measured failure of the listed schemes, not a universal impossibility theorem for reorthogonalization rules (that statement is the OPEN target PD-T?…-210). It is not a statement about reorthogonalization combined with other selection rules. Span drift (distance of the computed spaces from S_n) and the stability of fitted values or least-squares approximants computed from these bases are different targets; no claim about the latter is made here, and neither observation contradicts the other without an additional argument.

## Open items

Same test for the balanced and adaptive selections of reconstruction 01 (L2 R02); M-dependence; MGS/HL ORTH.

## History

- 2026-11-01: created (Claude Opus 5.5, xhigh; L2 R01).
- 2026-11-01T01:28:43+01:00: (reconstruction 01) F7 wording of (b); F9 ZN identification and LIT?…-025 note recorded as UNVERIFIED, original Sources sentence kept; verdict order and realization variance added (§5, §3). Original (b) phrase: "reference-free lower bound max(θ_s, θ_{s+1}) ≥ δ_J/(2‖J‖) on the principal angle between the computed and the exact graded spaces:". Status unchanged (MEASURED; CONFIRMED by reconstruction 01) (Claude Opus 5.5, xhigh; L2 developer, response to reconstruction 01, `directions/L2/response-recon-01.md`).
- 2026-11-01T08:32:22+01:00: (Codex audit-01, findings **L2-F1** (propagation) and **L2-F4** (reference to the split drift bound), plus the audit's independent stable-reference experiment and its notes on linear-u scaling and fitted-value stability; Claude Opus 5.5, xhigh; L2 developer, response `directions/L2/response-audit-01.md`; rules read at 8b61391613045f547589e48dcb8037a266bad8aa) Scope: original "The mechanism is the commutator/shadow recursion of PD-T?…-202 (not reset by reorthogonalization). It is not a statement about reorthogonalization combined with other selection rules." — replaced by the scoped mechanism sentence, the not-universal sentence (OPEN target PD-T?…-210) and the fitted-value distinction. (b) reference "by PD-T?…-202 part 5" → "by PD-T?…-208 (formerly PD-T?…-202 part 5)"; status row and Depends on likewise (original Depends on: "PD-T?…-201 (definitions), PD-T?…-202 (decomposition, drift bound), PD-T?…-101/-104 (CONDITIONAL inputs)."). Checks: original "Independent rerun: none." extended with the independent confirmations. Verdict order: bracketed qualification of "scaling linearly with the working precision" and item (4) added; original text kept. Measurements, verdicts, dispositions and status MEASURED unchanged.
