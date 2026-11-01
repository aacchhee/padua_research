# L2 — response to Codex audit-01

Developer: Claude Opus 5.5, effort xhigh (L2 mathematical developer; not an auditor of this work). Written 2026-11-01T08:32:22+01:00 – 09:05+01:00. Rules read at branch head `8b61391613045f547589e48dcb8037a266bad8aa` (AGENTS.md, agents/WORKFLOW.md, agents/claude/CLAUDE_ROLES.md, templates/THEORY.md; unchanged since `5f52331`). Audited candidate: `5ccfac223f466a9105450365d8c6c3781ff7d922`. Read in full: `audit-01.md`, `audit-01/L2.md`, the evidence logs of `audit-01/L2/` cited below, all L2 theory files (PD-T?…-201–207, PD-N?…-201–207), `directions/L2/` records, `l2_core.py`, the R02/R03 drivers and reconstruction 01's `review_L2/rl2_cycles.py`. Audit files were not edited. No git command that changes state was run (read-only `git rev-parse/log/show/diff/status` only; the orchestrator's WIP commits 8b61391, 11576cb, 80f4f45 picked up intermediate states of these files).

Novelty gate: not applicable — no new candidate, mechanism or IDEA record is proposed (recorded in `candidates.md`). PD-T?…-208 is a split of an existing proved bound, PD-T?…-209 a proof of an already registered open target, PD-T?…-210 the registration as OPEN of a previously asserted claim.

## Overview

| Finding | Severity | Disposition | New IDs | Status changes |
|---|---|---|---|---|
| L2-F1 | Medium | fix (accepted) | PD-T?…-210 (OPEN) | none (universal claim was never a registered part; now OPEN) |
| L2-F2 | Medium | fix (accepted) | none | none (T201 stays PROVED; corollary restated χ-explicitly) |
| L2-F3 | Medium | fix (accepted) | none | none |
| L2-F4 | Medium | fix (accepted; split) | PD-T?…-208 (PROVED), PD-T?…-209 (PROVED, new proof, pending audit) | (C) ⟹ (W): OPEN → PROVED in PD-T?…-209 with written proof |
| L2-F5 | Low | fix by rerun (accepted) | none | none |
| Claim-coverage notes C1–C12 | — | fix / no change with reason (below) | none | none |

## L2-F1 — the residual identity does not prove a universal obstruction

**Summary.** T202's Scope deduced "no reorthogonalization rule can by itself make the implicit J-section accurate or the computed spaces J-closed" from the shadow recursion, whose coefficients do change with g and which gives no lower bound on K. Accepted: the deduction does not follow.

**Disposition: fix.** T202 Scope now says what parts 1–3 prove (an additional residual R⁻ᵀKR′⁻¹ not controlled by semi-orthogonality alone; g enters only as further coefficients, no reset term; no lower bound on K, no invariance under g) and attaches the failure of the tested schemes to MEASURED PD-N?…-201 and PD-T?…-207 (b). Part 3's clause "and do not reset K" reworded likewise. The universal statement is preserved, not deleted, as the OPEN target **PD-T?…-210** with a proposed formalisation (U), the measured support (tested rules change drift/θ_LB < 2–3×) and a clearly labelled heuristic (span identity), no proof claimed. Propagated to PD-N?…-201 Scope ("not reset by reorthogonalization" → scoped mechanism sentence, not a universal theorem), PD-N?…-202 status row, PD-T?…-205 Scope, PD-T?…-207 (b) ("exactly like … as PD-N?…-201 predicts" → within ≈ 2×, consistent with the measured failure), R01 §3–4, R02 §4, STATUS, SUMMARY (rank 2 "BJ + any reorthogonalization" → "each tested scheme").

**Files changed:** `commutator-shadow-recursion-and-span-drift-bound.md` (T202), `bj-universal-reorthogonalization-obstruction-open.md` (new, T210), `reorthogonalization-does-not-restore-graded-spaces.md` (N201), `pro2d-rounding-only-trigger-fails.md` (N202), `coupled-section-residuals-general-selection.md` (T205), `pro2d-strategy-and-cost-measured.md` (T207), `R01.md`, `R02.md`, `STATUS.md`, `SUMMARY.md`, `candidates.md`, `SPLITS.md` § L2.

**New IDs:** PD-T?bivariate-lanczos-claude-210 (OPEN).

**Evidence:** audit L2.md F1 (T202:65 contains −Σ g_lK_{m,l}); the T202 History of reconstruction 01 had already conceded the distinction. Measured CGS2 span drift is unaffected (audit: "does not weaken the measured CGS2 span-drift finding").

## L2-F2 — T201 drops normalisation/near-breakdown factors outside its exact theorem

**Summary.** Corollary A′'s display retained χ = max‖Fq̂_{p(k)}‖/β_k, but its paraphrase ("O(u)‖F‖ with polynomial constants") dropped it; Remark (i) (F8 extension to the reorthogonalized step) lost the 1/β_k factor on the η³ and rounding terms. Accepted.

**Disposition: fix.** In `semi-orthogonality-implies-accurate-F-section.md`:
- χ defined precisely as χ_k = ‖B_kq̂_{p(k)}‖₂/β_k over **all** columns (F- and J-columns; the original wrote F for every k, but μ also contains the local overlaps of the J-columns, whose relations are J's); retained in the corollary and its paraphrase: max|S − T| ≤ c(N, M)u(1 + χ)(τ₁ + ‖T‖₂ + ‖F‖).
- New explicit hypothesis **(NB)** χ ≤ χ₀; only under (NB) (with χ₀ polynomially bounded) does the "O(u)‖F‖ with polynomial constants" reading hold. The one-pass sentence made quantitative (μ ≤ c_μu; then χ-free, since χ enters only via L(b)).
- Remark (i) corrected to β_k‖Q̂_Wᵀq̂_k‖ ≤ η³‖h⁽¹⁾‖ + η²‖g_k‖ + ρ′_k, i.e. local level ≤ (η³‖h⁽¹⁾‖ + η²‖g_k‖ + ρ′_k)/β_k ≤ (√(1+η)η³ + 2√(1+η)η² + cu)χ_k, with a written derivation (five passes, rounding vectors, ‖I − Q̂_ZQ̂_Zᵀ‖₂ = 1, size bounds on h⁽¹⁾ and g).
- Proof of A′ written out: local level over all columns; exact identity for the h-part of ε_c (h_l − q̂_lᵀFq̂_c = −Σ Ω_{ll′}h_{l′} − Σ Ω_{ll″}g_{l″} − q̂_lᵀf_k − β_kΩ_{lk}, in which the β-multiplied local term needs no χ); routine size bound τ₁ ≤ N((1 + η)‖F‖ + ε_c), ‖T‖₂ ≤ τ₁.
- Title shows the (1 + χ) factor; Scope/Open items mention χ; Checks record the audit's reruns and the countercheck. Theorem A, Lemmas 1–3 and Proposition L unchanged; the χ-dependent display unchanged in substance (audit: not refuted).
- Supplementary MEASURED evidence (no kill rule): new part (e) of PD-T?…-204 — χ ≤ 5.28 on all 12 benchmarks (two-pass-window and PRO-2D-J runs); so no near-breakdown occurs in the tested runs. Also recorded: in PRO-2D-J runs the Frobenius loss η at the last degree exceeds √u on rotπ/4, triangle, L-shape, annulus (3.3e-8–1.7e-7), so the corollary's hypothesis η ≤ √u is not met literally there (already disclosed as Remark (ii), entrywise ⇒ η ≤ N√u).

**Files changed:** `semi-orthogonality-implies-accurate-F-section.md` (T201), `section-accuracy-and-two-pass-window-measured.md` (T204 (e)), new `code/L2/l2_audit01_chi.py`, log `logs/audit01_chi.raw.gz`, `R01.md`, `SUMMARY.md`.

**New IDs:** none.

**Evidence:** (1) Developer rerun of the audit's countercheck `audit-01/L2/check_local_beta.py` (separate execution 2026-11-01 ≈ 09:00+01:00, Python 3.13.18, mpmath; output in the developer scratchpad, sha256 cb5eadbf2aaa5a658c548395228877d92ef7153c9e2859b683bf903015ae104b) is byte-identical to `audit-01/L2/local-beta.log`: ratios local/(η³ + u) = 2.62e5, 2.68e8, 2.75e11 at u = 2⁻⁴⁰, 2⁻⁶⁰, 2⁻⁸⁰, while the normalised bound η³‖h⁽¹⁾‖/β (1.9e-6, 1.9e-9, 1.8e-12) dominates the local overlap (2.4e-7, 2.3e-10, 2.3e-13) — consistent with the corrected Remark (i). (2) χ measurement: `cd tracks/bivariate-lanczos/code/L2 && OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 -I l2_audit01_chi.py > ../../../../topics/bivariate-lanczos-20261031/directions/L2/logs/audit01_chi.raw`, run 08:25:47–08:25:58+01:00, exit 0, Python 3.13.18, NumPy 2.5.3, 2-core VM; gzipped (`gzip -9 -n`); its PRO-2D-J losses reproduce R02 (L-shape 1.48e-8, cubic 1.97e-7). (3) Audit-01's Theorem-A stress rerun (35 instances, max LHS/RHS 0.1613) recorded in Checks.

## L2-F3 — T207 confuses its registered kill threshold with strict semi-orthogonality

**Summary.** Semi-orthogonality is defined as L ≤ √u (1.0537e-8); T207's headline "semi-orthogonal on 11 of 12" used the relaxed registered kill threshold 10√u; the L-shape reaches 1.4826e-8 = 1.407√u. Accepted.

**Disposition: fix.** T207 title and (a) now state: 11/12 pass the registered loss criterion L ≤ 10√u; strict L ≤ √u at every degree on 10/12 (L-shape exceeds √u at n = 29 (1.2076e-8) and n = 30 (1.4826e-8); cubic 18.70√u at n = 29); e_F statement refers to the strictly semi-orthogonal degrees (as registered); at L-shape n = 29–30 the logged e_F is 2e-15 but outside the registered criterion. **Failed frozen criteria preserved:** the cubic-checkerboard kill (PD-N?…-207) and the failed secondary cost criterion (≤ 30%: rotπ/4 0.33, triangle 0.42, L-shape 0.35, annulus 0.37). Original (a) text kept verbatim, followed by the threshold paragraph; Scope reworded; Checks record audit-01's independent PRO/PRO-J rerun. Propagated: N202 bracketed note on "stay", R02 §3 correction, STATUS, SUMMARY rank 6, candidates.md (IDEA?…-209's "survives on 11 of 12" refers to the registered threshold).

**Files changed:** `pro2d-strategy-and-cost-measured.md` (T207), `pro2d-rounding-only-trigger-fails.md` (N202), `R02.md`, `STATUS.md`, `SUMMARY.md`, `candidates.md`.

**New IDs:** none.

**Evidence:** per-degree maxima parsed from the stored `logs/r02_proJ.raw.gz` (sha256 4609986b6d431201cddba95c527c5ec6bb969582f116e1b9b7f0d7d33029d14c): L-shape max 1.4825593127e-8 = 1.40704√u, exactly the audit's fresh value; annulus 9.8082726784e-9 = 0.93087√u; rotπ/4 0.72299√u; triangle 0.40542√u; cubic 1.9702675094e-7 = 18.69907√u.

## L2-F4 — substantive proof and open target are not split as required

**Summary.** T202 part 5 (drift lower bound) was labelled "minor routine" although N201, T205, T206 (and N203, N204, T207) depend on it; T205 contained the explicitly OPEN target (C) ⟹ (W) inside a PROVED file. Accepted.

**Disposition: fix (split).**
- **PD-T?…-208** `reference-free-span-drift-lower-bound.md` (PROVED): T202 part 5 and the drift sentence of T205 part 4, merged (identical inequality, both operators, any computed nested spans), statement and proof unchanged in substance; states explicitly that θ_LB(n) bounds max_{s≤n} θ_s, not θ_n (audit's M = N_n example), and that (a) needs no U-hypothesis. Original wordings quoted verbatim in `Split from:`. All dependents now cite PD-T?…-208 (N201, N203, N204, T206, T207).
- **PD-T?…-209** `condition-C-staircase-selections-acyclic-sections.md`: the split-off target "(C) ⟹ (W)". In the same response I wrote a proof, so its status is **PROVED (pending audit)**: (a) Lemma S — (C) holds iff the selection is a staircase (X for j ≤ s_t, Y above, s_1 = 0, s_{t+1} − s_t ∈ {0, 1}), hence exactly 2^{n−1} (C)-selections; (b) under (P) (windows and reorthogonalization sets inside the preceding columns) every (C)-selection satisfies (W), with the explicit order (by degree; unformed Y-columns before unformed X-columns, increasing j) and a support lemma (degree-(s+1) part of supp Ĥ_Ae_{(s,j)} ⊆ {j′ ≤ j + [A = Y]}). T205 keeps the exact conditional theorem under (C) and (W), as the audit asked; it notes that PD-T?…-209 discharges (W) under (P).
- Evidence account corrected in T205 and T209: reconstruction 01's sampling at n = 6..9 contained 5, 0, 0, 0 (C)-selections out of 3000, so "well-defined ⟺ (C) in all cases" was vacuous for n = 7–9; Lemma S explains the sampling probability 2^{−(n−1)(n−2)/2}.
- T202 part 4 (two-line defect identity) proposed as minor routine (no other result cites it; T205 part 4 now carries its own one-line proof). For the auditor to check.
- `SPLITS.md` § L2: four rows (202 part 5 → 208; 205 part 4 → 208; 205 (C) ⟹ (W) → 209; 202 Scope → 210).

**Files changed:** T202, T205, new T208, new T209, N201, N203, N204, T206, T207, `SPLITS.md`, R02, STATUS, SUMMARY; new `code/L2/l2_audit01_staircase.py`, log `logs/audit01_staircase.raw`.

**New IDs:** PD-T?bivariate-lanczos-claude-208 (PROVED), PD-T?bivariate-lanczos-claude-209 (PROVED, new developer proof; requires independent audit).

**Evidence:** `cd tracks/bivariate-lanczos/code/L2 && python3 -I l2_audit01_staircase.py > ../../../../topics/bivariate-lanczos-20261031/directions/L2/logs/audit01_staircase.raw`, run 08:31:46–08:32:16+01:00, exit 0, Python 3.13.18, exact set computations: exhaustive over all selections n = 2..6 (2, 8, 64, 1024, 32768): (C) for 2, 4, 8, 16, 32, each a staircase, none cyclic, no support-lemma violation, 0 disagreements with `rl2_cycles.analyse` (n ≤ 5); all staircases n = 7..13 acyclic (block window); staircases × 3 random window/L-sets inside the preceding columns n = 2..10 (6–1536 cases) acyclic; BJ/mirror/alt n = 6, 12, 20 staircases. Finite checks supplement the proof. Audit-01 `exact-rerun.log` (80-digit part-5 inequality checks) recorded in T208.

## L2-F5 — the extended-precision experiment normalises in double

**Summary.** `l2_core.run(dots='ld')` computes product, window dots and update in long double but rounds r to double before computing β and q̂; N204 described "the whole step in x87 long double", and the pre-registration of IDEA?…-210 explicitly included the normalisation. Accepted.

**Disposition: fix by rerun** (cheap: 13 s). New script `l2_audit01_ldnorm.py` (l2_core.py unchanged) re-implements the R03 'ld' branch with two normalisation options; its 'ld' reproduces `l2_core.run(dots='ld')` **bit for bit** on all eight sets, and its double/'ld' numbers equal the R03 log. The new 'ldn' variant normalises in long double (β = ‖r_LD‖, q̂ = fl₆₄(r_LD/β), one final rounding to the stored double vector; column 0 likewise). Results (L(20), L(24) reduction double/variant): clustered checkerboards 'ld' 1.9–4.5×, 'ldn' 3.3–7.9× (quadratic 7.8/4.3, cubic 6.9/3.3, quartic 4.1/4.3, cubic m = 36 5.6/7.9) — still < 10× at both degrees; rotπ/4 'ldn' 10×/12×/11× (n = 16/20/24; 'ld' 3.3–4.5×, exact 14–19×); triangle n = 16 'ldn' 2.1× **better** (exact and 'ld' ≈ 10× worse), n = 20 saturated (L = 1); θ_LB 'ldn' rotπ/4 3.3e-4, triangle 4.5e-4 (< 2× change); controls flat (≤ 1.6e-15 CL checkerboard, 6.9e-15 tensor). Consequences recorded in N204: precise 'ld' description; new part (e); bracketed 'ldn' values in (a)–(d), Reading and Scope (originals kept); the triangle-worsening/non-monotonicity is attributed to 'exact' and double-normalised 'ld' only; the earlier 'ld' range "1.3–4.8×" corrected to 1.9–4.5× at n = 20, 24 (it was not reproducible at those degrees from the stored log); title made precise. Verdicts (P1, P2 killed; P3 survives) and disposition unchanged — the registered kill rules applied to 'exact' only; 'ld' was "Reported, no kill". The correctly-rounded-dot negative and the separate all-long-double-storage experiment (PD-T?…-115 (c)) are unaffected, as the audit stated. candidates.md and R03 record the deviation between pre-registered and implemented 'ld'.

**Files changed:** `exact-window-dots-do-not-remove-coefficient-channel.md` (N204), new `code/L2/l2_audit01_ldnorm.py`, log `logs/audit01_ldnorm.raw`, `R03.md`, `candidates.md`, STATUS, SUMMARY.

**New IDs:** none.

**Evidence:** command `cd tracks/bivariate-lanczos/code/L2 && OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 -I l2_audit01_ldnorm.py > ../../../../topics/bivariate-lanczos-20261031/directions/L2/logs/audit01_ldnorm.raw`; run 2026-11-01T08:24:29–08:24:42+01:00, exit 0; Python 3.13.18, NumPy 2.5.3, x87 long double (eps 1.0842e-19, unit roundoff 2⁻⁶⁴), 2-core VM; branch head at run time `6db79518508ae4e3153553ee4d0ffecf2f407645` plus the uncommitted script; imported `l2_core.py`, `l1_recurrence.py`, `l1_r04_checkerboard.py` byte-identical to the audited candidate; deterministic node sets (no seeds).

## Claim-coverage notes of L2.md (table and drift/cycle paragraphs)

- **C1 (T201: no-underflow model; entrywise √u ⇒ η ≤ N√u).** No change needed beyond L2-F2: both were already stated (Assumptions; Remark (ii)); Assumptions now say "diagonal F and J".
- **C2 (T202/T205: drift bound only as adjacent-stage / max-over-stages bound).** Already in that form in T202 part 5, T205, N201 (b), T206; PD-T?…-208 (c) states it with the M = N_n example. report.md:41's shorthand is outside my ownership (orchestrator).
- **C3 (T203: "factor 7" is E1's; triangle E2 overestimate 11.7147).** Fix: T203 title and (b) name E1 and give E2 11.7, E2D 13.6 (triangle), 13.4 (rotπ/4); Checks record audit-01's partial rerun. SUMMARY, STATUS, R01 corrected.
- **C4 (T204: no independent all-12 section-suite rerun).** Recorded in T204 Checks; no claim change.
- **C5 (T205: cycle evidence vacuous at n = 7–9).** Fix: see L2-F4 (evidence account corrected; PD-T?…-209).
- **C6 (T207: no fresh 10⁵/10⁶ timing).** Recorded in T207 Checks; M = 10⁶ remains under Runs needed (R02 §7).
- **C7 (N201: not a universal impossibility theorem; linear-u scaling; V+A equivalence; span drift vs fitted values).** Fix: N201 Scope (not universal → PD-T?…-210; fitted-value stability is a different target, no claim), verdict-order bracket ("scaling linearly" rests on two precisions; audit ratios 1.87e-3 and 7.95e-4 vs 2⁻¹¹; not a universal linear-u law), Checks record audit-01's independent stable-reference experiment (4.105e-3, 1.016e-2; long double 7.69e-6, 8.08e-6; running bound 2.82e-4, 7.77e-4). The ZN/V+A identification was already UNVERIFIED (unchanged).
- **C8 (N203: does not quantify over all possible selections).** Fix: N203 Scope sentence; T206 title "none of the four tested one-relation rules"; SUMMARY failed-routes wording.
- **C9 (N205: "safe" only means passing the registered underestimation tolerance).** Fix: N205 Scope; R01 correction ("safe but costly").
- **C10 (N206: no promotion to all one-pass algorithms).** No change: N206's statement is the measured refutation of the universal implication "semi-orthogonality alone ⇒ O(u) F-section" for one-pass windows by listed counterexamples (sets, degrees, values), with the parameter range stated; it makes no claim that every one-pass run fails.
- **C11 (N202, N204, N207 reruns).** Recorded in their Checks (N202 rounding-only PRO 5.0311e-7 / 2.4401e-6; N204 full R03 rerun; N207 L(29) = 18.70√u).
- **C12 (prior-art bounds; V+A-type rebuild).** No change: L2 files make no priority claim; reading limits already recorded.

## Consolidated audit-01 items concerning L2

- Item 2 (T201 pivot/amplification factors; T202 does not prove that every scheme fails): L2-F2, L2-F1.
- Item 3 (√u vs relaxed kill threshold; preserve failed frozen criterion; descriptive vs causal): L2-F3; the cubic kill and the failed ≤ 30% cost criterion are preserved; N202's "explanation" stays "MEASURED support only … not proved".
- Item 5 (splits; T202's substantive drift bound): L2-F4.
- Item 6 (literature consolidation, allocation, rehearsal): PR-preparation tasks of the orchestrator; no L2 literature statement was added in this response.

## Propagation needed in files I do not own (orchestrator)

- `report.md`: line 10 ("a proved obstruction for the y-part (the commutator residual is not reset by reorthogonalization …)") and Rank 4 lines 41–42 ("is not reset by reorthogonalization", "reference-free lower bound θ ≥ δ_J/(2‖J‖) (202)", "(C) ⇒ acyclic OPEN") → obstruction = identities + PD-T?…-208 + MEASURED failure of the tested schemes; universal claim OPEN (PD-T?…-210); drift bound is PD-T?…-208 and bounds max_{s≤n} θ_s; (C) ⟹ (W) now PD-T?…-209 (PROVED by the developer, pending audit); T201 corollary carries (1 + χ). Any "semi-orthogonal on 11/12" (PRO-2D-J) → registered 10√u criterion on 11/12, strict √u on 10/12; any "factor 7" → E1; any 'ld' = "whole step in long double" → normalised in double ('ldn' added).
- `LOG.md`, `progress.md`, `plan.md`: as the orchestrator sees fit; `ID_CROSSWALK.md`/`PROOF_STATUS.md` at PR preparation from `SPLITS.md` § L2.

## Runs

Completed in this response (all on the 2-core VM, Python 3.13.18, NumPy 2.5.3, SciPy 1.18.1): `l2_audit01_ldnorm.py` (13 s), `l2_audit01_chi.py` (11 s), `l2_audit01_staircase.py` (30 s), rerun of the audit's `check_local_beta.py` (identical output). Runs needed: none new (R02 §7 M = 10⁶ commands stand).

## Materiality to PROVED claims

- PD-T?…-201: stays PROVED. Theorem A unchanged. Corollary A′'s proved content is the χ-explicit bound (as displayed before); its former paraphrase "O(u)‖F‖ with polynomial constants" is now PROVED only under the explicit (NB) hypothesis — a correction of an overstated reading, not of a proof step. Remark (i)'s former uniform form is withdrawn and replaced by the normalised, proved form.
- PD-T?…-202: parts 1–4 PROVED, unchanged; part 5 moved unchanged to PD-T?…-208 (PROVED). Only the Scope interpretation (not a proved part) is withdrawn to PD-T?…-210 (OPEN).
- PD-T?…-205: the conditional theorem under (C) + (W) is unchanged and PROVED; its OPEN row is now PD-T?…-209, which the developer proves (OPEN → PROVED; pending audit).
- No MEASURED verdict, kill decision or REJECTED disposition changes. PD-N?…-204's verdicts stand; its description and a reported variant are corrected/extended.

## File → sha256 after changes

| File | sha256 |
|---|---|
| tracks/bivariate-lanczos/theory/semi-orthogonality-implies-accurate-F-section.md | db4812fb4318aad51e6130a0b1842f55098d927de3bab600db79adf2317853aa |
| tracks/bivariate-lanczos/theory/commutator-shadow-recursion-and-span-drift-bound.md | 7bfa20b8b8a00709e741aa333ee9fe8a8347703da7f4ed2245b015537c0f5e73 |
| tracks/bivariate-lanczos/theory/omega-estimate-tracks-loss-measured.md | 2a0cb9af3855e304b359cce2089ad00dcb8363b9d1e49deda7005f3bc7fcb8c9 |
| tracks/bivariate-lanczos/theory/section-accuracy-and-two-pass-window-measured.md | abb87e8c7ce874d7595bf6585d087de1fe1af855ee9ebc5133d4d609d1d2830c |
| tracks/bivariate-lanczos/theory/coupled-section-residuals-general-selection.md | fb2998d446b8bd75492ccd5c97352b16cd39b26dd9d0160d2dab7d327d7e3f23 |
| tracks/bivariate-lanczos/theory/selection-rules-and-span-drift-measured.md | a9d2ca39cca1731cec0df61a974291fd78b5de41aa2026aac4171d2b12d4d957 |
| tracks/bivariate-lanczos/theory/pro2d-strategy-and-cost-measured.md | 1bc0f02b4c67153371f31da879bd478583cd77f9b50e1a24a3f0c121556b82eb |
| tracks/bivariate-lanczos/theory/reorthogonalization-does-not-restore-graded-spaces.md | a0cfb918d2344b24984688174e2f398d398d1c080713883dfced8904880b8f68 |
| tracks/bivariate-lanczos/theory/pro2d-rounding-only-trigger-fails.md | fdd451d4e8c37cb8418a53356efd1ddd5bf9dbb0e389b6f41f93f5a9299532b1 |
| tracks/bivariate-lanczos/theory/one-relation-selections-do-not-keep-spans-near-Sn.md | 8e1d0c614773e87237bd3ade3f44000167726fabc7ce558e8dd8163950df8d03 |
| tracks/bivariate-lanczos/theory/exact-window-dots-do-not-remove-coefficient-channel.md | d68024f372f011937fa2264b972e034d30ffa85d5d8ce42cde37de69c164f896 |
| tracks/bivariate-lanczos/theory/omega-estimate-componentwise-in-window-sources-fail.md | f88a1b0ba065a146f42bc2e5f9c213cb3719ddf0b14340ada503e7b8a6e6b687 |
| tracks/bivariate-lanczos/theory/pro2d-j-fails-on-clustered-checkerboard.md | ef3595f73e1b53412c957c6761454402d1c6d757b8057c3a0e966741caf28f96 |
| tracks/bivariate-lanczos/theory/reference-free-span-drift-lower-bound.md (new, PD-T?…-208) | e685c442876709ad7db80cf2d379453569d16c1200318984917648c91030e23b |
| tracks/bivariate-lanczos/theory/condition-C-staircase-selections-acyclic-sections.md (new, PD-T?…-209) | 714424aefda4abc55236a2492467ff222fd736b494ddae7afb08aeef74aa3660 |
| tracks/bivariate-lanczos/theory/bj-universal-reorthogonalization-obstruction-open.md (new, PD-T?…-210) | 84a19ed6abefe138f7e113cf05ea4ece26cfcfc7ce386e75bc14ddb0fb786d99 |
| tracks/bivariate-lanczos/code/L2/l2_audit01_ldnorm.py (new) | 6e68cae5eecb93880389f281d02446131ec6d88cd1db851728416c8ed6e551d1 |
| tracks/bivariate-lanczos/code/L2/l2_audit01_chi.py (new) | ae4cba93c25f7d1545031ab2b2b7abcc844dc32d93fbc53b85cbf77d988e1945 |
| tracks/bivariate-lanczos/code/L2/l2_audit01_staircase.py (new) | e9224208348cb54f2cda7d1829e298ef6ea4160be07024b2b844be63882a18e1 |
| topics/bivariate-lanczos-20261031/directions/L2/logs/audit01_ldnorm.raw (new, 57 210 B) | 6b60fd7c972cfe64679300e24bdf35686ace357f57cb97a513ec9760f2c8e5ad |
| topics/bivariate-lanczos-20261031/directions/L2/logs/audit01_chi.raw.gz (new, 49 827 B; uncompressed 7a8f8c15cfddf89d73db6b803419c31f8d170303e8eaa69d2cfc5014aa4f9e62) | 0e0b0049e9bc3cb7084ba1d078220bc6b430c367f48b302e8cd12f1948d993b1 |
| topics/bivariate-lanczos-20261031/directions/L2/logs/audit01_staircase.raw (new, 3 096 B) | 6d0a1e28ee1cd988c7841e2cec93dc3f23327374b2087318841818c475246a02 |
| topics/bivariate-lanczos-20261031/directions/L2/SUMMARY.md | 764e9b7c15ad2f4dc557bb1b501e898c18b42596fa66bb4df25413ae7b4afdb7 |
| topics/bivariate-lanczos-20261031/directions/L2/STATUS.md | 848a5570b7842b20f09f03c22fb473f81ef38505f242b1047ae08e7516f6d791 |
| topics/bivariate-lanczos-20261031/directions/L2/R01.md | a5ca6e3cb5d33817e1495fb70e58f618fb2efbf7e544631b9b8a101c46b4e55a |
| topics/bivariate-lanczos-20261031/directions/L2/R02.md | b26817e846aac9485fcb4cc5ca0e9b448dc261d2d28dfca45be513ddad33f7af |
| topics/bivariate-lanczos-20261031/directions/L2/R03.md | e55c419535156ee5dc06fbdd9f62b999dfb91be1b9602d5508434cb0204d227b |
| topics/bivariate-lanczos-20261031/directions/L2/candidates.md | bda0de68d9e094bab19fef0b8183d27e0f06f507cb6d34b36ef3268f1e69085a |
| topics/bivariate-lanczos-20261031/SPLITS.md (whole file at the time of writing; other sections are other agents') | 9bb5b5b89837a5148ceda370dc133ac2f0dc39d501c8ab521d96a913f4842c4e |
| topics/bivariate-lanczos-20261031/directions/L2/response-audit-01.md (this file) | not self-referable; reported in the hand-back |

Unchanged L2 theory file: `one-pass-window-semi-orthogonality-insufficient-for-F-section.md` (PD-N?…-206), sha256 67126ec06209f896247ee850b8beabbd5f73bafa146681e79bcdbf0361f37c05.
