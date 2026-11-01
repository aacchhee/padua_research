# PD-N?bivariate-lanczos-claude-204 — Correctly rounded window dot products (and long-double window steps with double storage, normalised in double or in long double) do not remove the clustered-checkerboard coefficient channel; exact dots reduce the rotπ/4 loss 14–19× and make the triangle 10× worse at n = 16; the drift is unchanged

ID kind: PD-N.
Aliases: IDEA?…-210 killed (P1, P2); L1 hand-off "compensated/extra-precision window dot products" tested; dot rounding is not the special driver.
Split from: none.
Split into: none.

## Statement

[FP, MEASURED] BJ block window, one CGS pass, u = 2^-53; window coefficients computed in double (BLAS), correctly rounded ('exact': Dekker products + math.fsum, verified against exact rational arithmetic), or with the whole step in x87 long double and the vectors stored in double ('ld'). **Precise description of 'ld' (corrected after audit-01, L2-F5):** the product B·q̂_p, the window dot products and the update are computed in x87 long double (unit roundoff 2^-64) from the double-stored vectors, but the residual r is rounded to double **before** the normalisation, so β = ‖r‖ and q̂ = r/β are computed in double (`l2_core.py` lines 165–172 and 205–206); 'ld' therefore does not remove the double rounding of the normalisation. **New variant 'ldn' (audit-01 response):** as 'ld' but with the normalisation in long double, β = ‖r_LD‖ and q̂ = fl₆₄(r_LD/β) (one final rounding to the stored double vector; column 0 likewise); see (e).

(a) **Clustered checkerboards (P1 killed on all four).** L(20), L(24) double → exact: quadratic m = 30 1.17e-11 → 5.11e-12, 1.43e-10 → 1.08e-10 (2.3×, 1.3×); cubic m = 30 6.67e-9 → 1.65e-9, 6.31e-7 → 2.57e-7 (4.0×, 2.5×); quartic m = 30 1.44e-6 → 8.26e-7, 1.78e-3 → 1.00e-3 (1.7×, 1.8×); cubic m = 36 9.79e-9 → 1.78e-9, 5.53e-6 → 6.48e-7 (5.5×, 8.5×). 'ld' gives 1.3–4.8×. The pre-registered requirement (≥ 100×; kill if < 10× at both degrees) fails on every clustered set. [Corrected range, audit-01 response: recomputed from the stored log at the pre-registered degrees n = 20, 24, 'ld' gives 1.9–4.5× (quadratic 4.2, 2.8; cubic 2.8, 2.0; quartic 2.2, 1.9; cubic m = 36 1.9, 4.5); 'ldn' gives 3.3–7.9× (quadratic 7.8, 4.3; cubic 6.9, 3.3; quartic 4.1, 4.3; cubic m = 36 5.6, 7.9) — below 10× at both degrees on every clustered set, like 'exact'.]
(b) **Vector channel (P2 killed).** rotπ/4: L(16), L(20), L(24) double 1.62e-9, 2.27e-6, 4.17e-3 → exact 1.15e-10, 1.20e-7, 2.37e-4 (14×, 19×, 18×); 'ld' 3.3–4.5×. Triangle: L(16) 4.88e-4 → 4.91e-3 (exact, 10× worse), 'ld' 5.19e-3; L(20) = 1 in all three. So the effect of removing one rounding source is set-dependent and not monotone. ['ldn', audit-01 response: rotπ/4 1.61e-10, 1.85e-7, 3.90e-4 (10×, 12×, 11×); triangle L(16) 2.38e-4 (2.1× better than double), L(20) = 1. The triangle worsening at n = 16 is therefore a property of 'exact' and of the double-normalised 'ld', not of extra precision as such; with the normalisation also in long double the triangle improves 2×.]
(c) **Drift (P3 survives).** θ_LB at the last degree: rotπ/4 3.1e-4 / 3.2e-4 / 1.6e-4, triangle 7.8e-4 / 6.1e-4 / 3.3e-4 (double / exact / ld): changes < 10×. ['ldn': rotπ/4 3.3e-4, triangle 4.5e-4; changes < 2×.]
(d) **Controls.** Chebyshev–Lobatto checkerboard and tensor 41² flat in all variants (≤ 4.1e-15, ≤ 1.9e-14). PRO-2D-J with exact dots on the cubic checkerboard: L(29) = 7.5e-7 (double 2.0e-7) — the R02 last-degree failure is not repaired. ['ldn': ≤ 1.6e-15, ≤ 6.9e-15.]
(e) **Long-double normalisation rerun (audit-01, L2-F5).** `l2_audit01_ldnorm.py` re-implements the 'ld' branch for this setting with both normalisation options; its 'ld' reproduces `l2_core.run(dots='ld')` bit for bit on all eight sets (control printed in the log), and its double baseline and 'ld' values equal the R03 log. Results as bracketed in (a)–(d). The registered kill rules applied to 'exact' only and are unchanged; 'ld' and 'ldn' are reported variants (as pre-registered: "Reported, no kill").

Reading: on the clustered product-type checkerboards the closed loop of PD-T?…-115 is fed at comparable strength by the rounding of the stored vectors and of the vector operations, not specifically by the dot products; removing ρ leaves the loss within 1.3–8.5×. The hand-off speculation "compensated or extra-precision window dot products would shrink ρ, which drives the closed loop" is refuted in this scope. [Audit-01 response: with the whole step including the normalisation in long double ('ldn'), so that only the rounding of the stored double vectors remains, the clustered-checkerboard loss still drops only 3.3–7.9× at n = 20, 24 — consistent with the storage rounding feeding the closed loop at comparable strength (cf. PD-T?…-115 (c): long-double storage scales the loss with the storage precision).]

## Negative-result scope (PD-N only)

Attempted mechanism: IDEA?…-210 (correctly rounded / extended-precision window dot products as a remedy for the coefficient channel, and as a channel separator).
Parameter range: Harris–Simanek checkerboards with gradings s|s|, s|s|², s|s|³ (m = 30) and s|s|² (m = 36), weights |1/ω′_X||1/ω′_Y|, n ≤ 35; controls as listed; one machine, NumPy 2.5.3, x87 long double; variants double / exact / 'ld' (step in long double, normalisation in double) / 'ldn' (step and normalisation in long double), vectors stored in double in all. Not covered: storing vectors in extended precision (L1 PD-T?…-115 (c): a long-double run with long-double storage scales with u), compensated vector updates, MGS.

## Status by part

Overall status: MEASURED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| (a)–(d) | MEASURED | `logs/r03_dots.raw.gz`; bracketed 'ldn' values `logs/audit01_ldnorm.raw` |
| (e) long-double normalisation rerun | MEASURED | `logs/audit01_ldnorm.raw` (control: bitwise reproduction of the R03 'ld' variant) |
| exact-dot implementation | checked against exact rational arithmetic on 3 random dot products of length 500 (difference 0) | R03 §2 |

Candidate / claim disposition: IDEA?…-210 REJECTED (failed: P1 on all four clustered sets, P2 on rotπ/4); P3 (drift insensitive to dot precision) survives.
Rejection reason: failed.

## Depends on

PD-T?…-115 (closed-loop reading, CONDITIONAL input), PD-T?…-208 (θ_LB; formerly cited as PD-T?…-202 part 5 / -205).

## Checks

`python3 -I tracks/bivariate-lanczos/code/L2/l2_r03_dots.py > …/L2/logs/r03_dots.raw` (≈ 40 s). Independent rerun: Codex audit-01 reran the complete R03 suite (Python 3.12.14, NumPy 2.3.5, threads 1; `topics/bivariate-lanczos-20261031/audit-01/L2/dots-rerun.log`): double/exact/ld values reproduced to the printed digits; clustered-set exact-dot improvement at n = 20/24 1.3153–8.5334×, rotπ/4 ≈ 18–19×, triangle n = 16 ≈ 10× worse.
Long-double normalisation rerun (audit-01 response, L2-F5): `cd tracks/bivariate-lanczos/code/L2 && OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 -I l2_audit01_ldnorm.py > ../../../../topics/bivariate-lanczos-20261031/directions/L2/logs/audit01_ldnorm.raw` — run 2026-11-01T08:24:29+01:00 to 08:24:42 (13 s), exit 0; Python 3.13.18, NumPy 2.5.3, x87 long double eps 1.0842e-19 (unit roundoff 2^-64), 2-core VM; branch head at run time 6db79518508ae4e3153553ee4d0ffecf2f407645 plus this response's uncommitted new script (the imported `l2_core.py`, `code/L1/l1_recurrence.py` and `code/L1/l1_r04_checkerboard.py` are byte-identical to the audited candidate 5ccfac223f466a9105450365d8c6c3781ff7d922; l2_core.py sha256 e8c8fa3378b3531f4fc13faac9902757b97c92c281b2bcd2c02875e0b1c5638d); script sha256 6e68cae5eecb93880389f281d02446131ec6d88cd1db851728416c8ed6e551d1, output sha256 6b60fd7c972cfe64679300e24bdf35686ace357f57cb97a513ec9760f2c8e5ad (57 210 bytes). No seeds (deterministic node sets of candidates.md).

## Sources

None (L1 hand-off text only).

## Proof or evidence

Measured.

## Scope

Within the stated range, extra-precision dot products are a weak remedy (≤ 8.5×) for the coefficient channel and a moderate one (≈ 18×) for the rotπ/4 vector channel; they do nothing for the space channel. Doing the whole step including the normalisation in long double while storing in double ('ldn') is likewise weak on the coefficient channel (≤ 7.9×), gives ≈ 11–12× on the rotπ/4 vector channel and 2× on the triangle at n = 16, and leaves θ_LB unchanged (< 2×).

## Open items

Extended-precision storage of the basis (expected to scale the loss with the storage precision, PD-T?…-115 (c)) at the cost of doubling memory traffic; whether any double-storage scheme removes the coefficient channel.

## History

- 2026-11-01: created (Claude Opus 5.5, xhigh; L2 R03). Kill rules pre-registered 00:44:13 (candidates.md).
- 2026-11-01T01:28:43+01:00: (reconstruction 01 F6) title range corrected from "17–19×" to "14–19×" to match (b) (Claude Opus 5.5, xhigh; L2 developer, response to reconstruction 01, `directions/L2/response-recon-01.md`).
- 2026-11-01T08:32:22+01:00: (Codex audit-01, finding **L2-F5**; Claude Opus 5.5, xhigh; L2 developer, response `directions/L2/response-audit-01.md`; rules read at 8b61391613045f547589e48dcb8037a266bad8aa) Disposition: fix by rerun. The 'ld' description was imprecise — the implementation normalises in double. Original wording: "or with the whole step in x87 long double and the vectors stored in double ('ld')." (kept; the precise description follows it). Rerun with a long-double normalisation ('ldn', new script, l2_core.py unchanged) added as part (e) and as bracketed values in (a)–(d), Reading and Scope; original texts of (a)–(d) and Reading kept verbatim. The 'ld' range "1.3–4.8×" in (a) is not reproduced at n = 20, 24 by the stored log (recomputed: 1.9–4.5×) and is corrected in brackets. Title made precise; original title: "PD-N?bivariate-lanczos-claude-204 — Correctly rounded (or long-double) window dot products do not remove the clustered-checkerboard coefficient channel; they reduce the rotπ/4 loss 14–19×, make the triangle worse at n = 16, and leave the drift unchanged". The triangle-worsening statement is now attributed to 'exact' and the double-normalised 'ld' only ('ldn' improves the triangle 2× at n = 16). Original Parameter range ended "…; one machine, NumPy 2.5.3, x87 long double. Not covered: …"; original status row "| (a)–(d) | MEASURED | `logs/r03_dots.raw.gz` |"; original Depends on "PD-T?…-115 (closed-loop reading, CONDITIONAL input), PD-T?…-202 part 5 / -205 (θ_LB)."; original Checks ended "Independent rerun: none." Verdicts (P1, P2 killed; P3 survives), disposition and status MEASURED unchanged.
