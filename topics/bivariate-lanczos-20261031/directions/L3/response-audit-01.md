# L3 developer response to Codex audit-01

Developer: L3, Claude Opus 5.5 (xhigh, requested; runtime effort not exposed). Written 2026-11-01T08:46:07+01:00; all edits stamped 2026-11-01T08:33:39+01:00 (`date -Iseconds`). Branch claude/bivariate-lanczos-20261031, head 5f52331 (audited candidate 5ccfac2). Read: AGENTS.md, agents/WORKFLOW.md, templates/THEORY.md, audit-01.md, audit-01/L3-framework.md, audit-01/L3-certificates.md, audit-01/protocol.md (P3–P4), all L3 theory files and records. Audit files not edited. No Git operations. Novelty gate: not applicable (no new mechanism or candidate; 318 is a new proved formula about an existing object, 316/319 are open questions split from existing claims). Executed: the auditor's `exact_framework_checks.py` (identical output) and two new developer scripts (below).

## LF-M1 — T302(b) normalised residual threshold

Summary: the full-ball inradius theorem and exact representation are correct; the threshold (1−θ)ε with the mass-normalised L̂ and factor 1 is false (auditor's exact counterexample, rerun by the developer).
Disposition: **fixed.** 302(b) restated as (b1)–(b4) with three consistent residual conventions, each proved: (R1) unnormalised reference L_μ + E, threshold r(δ) ≥ (1−θ)ε exact in both directions; (R2) mass-preserving E ∈ H_0 with fixed-mass approximants, exact threshold r₀(δ) ≥ (1−θ)ε with the quotient seminorm |p|₀ = min_t ‖p − t‖_*, and r₀/(A + Br₀) ≤ r ≤ r₀; (R3) mass-normalised section data, factor s_E = m/(m + E(1)) carried; (b4) section norms with constants only. Old variant recorded as refuted (PD-N, WORKFLOW L5 rule: refuted claim with a scoped negative statement and exact evidence). Propagated: 303 (pointer, Scope transfers), N301/N303 (residual convention named, factor s_E), N302 (residual scope restated and its residual variant proved for (R1)–(R3)), candidates, SUMMARY. Rate exponents, exact-representation results and sign-separation obstructions unaffected.
Files: 302, N309 (new), 303, N301, N302, N303, candidates.md, SUMMARY.md. New IDs: PD-N?bivariate-lanczos-claude-309.
Evidence: `python3 -I tracks/bivariate-lanczos/code/L3/t302b_conventions_check.py` → `directions/L3/logs/t302b_conventions_check.log` (Fraction arithmetic, independent of audit code): counterexample reproduced; explicit radius δ′ = 10⁻⁸ for the positive-δ gap (gradient bound G = 120); (b2) threshold checked against an exact projection onto the fixed-mass simplex in both directions; the same E with free-mass approximants has residual ≤ θε, showing why (b2)(ii) needs fixed mass.

## LF-M2 — T304 isomorphism inside a PROVED file

Disposition: **fixed (split).** 304 keeps (a), (b) and the factorisation of (c), PROVED. The isomorphism clause → PD-T?…-316 (OPEN, original wording in Split from); the rank observation → PD-T?…-317 (MEASURED: reviewer's Padua n = 2, 3 plus a new developer run). New PD-T?…-318 (PROVED): κ(Φ(L))_ab = L(R^y_aR^x_b − R^x_aR^y_b) for every L; at a square-case measure dκ(E)_ab = E(s_ab), s_ab ∈ S₁, span{s_ab} = {p_C : C ⊥ Hankel}; hence 316 ⟺ (independent jets, C ↦ p_C injective, S₁ = {p_C}) — the open conjunct of 309. The isomorphism itself is not proved.
Files: 304, 316, 317, 318 (new), SPLITS.md (§L3). Evidence: `t318_dkappa_formula_check.py` → `logs/t318_dkappa_formula_check.log`: central differences vs formula ≤ 2.7e-8 relative (Padua n = 1..4, equispaced n = 3, random n = 3); identity (a) at a non-measure L ≤ 1.4e-10; rank dκ = dim{p_C} = n(n+1)/2 in all six sets (MEASURED verification record).

## LF-R1 — report-level: reading (E) presented as ruling out a Greenbaum model (report.md:23; protocol P4; consolidated item 4)

Disposition: **fixed in L3 records; report.md is orchestrator-owned (not edited).** Titles/headlines of N301, N303 restricted to reading (E) with (G) OPEN; same qualifier in N304, 308, 300, IDEA 307, OBST?…-L3-b, SUMMARY. Suggested report wording: Rank 1 brief — "…the striking instance: in reading (E) — exact representation (or a sufficiently smaller residual) of specified consistent perturbations given as data — Padua sections of every degree n ≥ 3 admit no positive backward measure with δ(ε) → 0; the finite-precision Greenbaum reading (G) remains OPEN." Rank 1 statement: "for every ε ∈ (0, ε₁]" (not "every ε > 0"), and "a per-degree radius δ₀(n) > 0".

## LF-R2 — report-level: rate trichotomy paraphrased as nonnegative-annihilator conditions (report.md:27; consolidated item 5)

Disposition: **fixed in SUMMARY (§1, §2 item 2); report.md orchestrator-owned.** Suggested report wording: "trichotomy (303), with S₀/S₁ the polynomials of degree ≤ 2n+1 vanishing (to first order) at the nodes and (H) = no nonzero p ∈ S₁ with all node Hessians PSD: S₀ = {0} → δ = 0; S₀ ≠ {0}, S₁ = {0} → δ ≍ ε; S₁ ≠ {0} → δ ≳ √ε, and δ ≍ √ε under (H); some p ∈ S₁ with all node Hessians PD → obstruction; the remaining PSD-singular case OPEN." Also replace "(inradius criterion r(δ) ≥ ε, c = 1)" by "(inradius criterion r(δ) ≥ ε; residual thresholds per convention, 302(b1)–(b3); the factor-1 normalised threshold is refuted, N309)" and "304(c) isomorphism part MEASURED" by "304(c) isomorphism: 316 OPEN (reduced to 309 by 318), 317 MEASURED". Counterexample to the paraphrase: any triangle (305).

## LF-S — stale labels in T300/T307/T310/N306 (L3-framework, summary-level note)

Disposition: **fixed.** 300 split list and rows synchronised (310, 313, N303 PROVED; Padua n = 4..7 MEASURED row replaced; random-set wording aligned with 307; Open items (2), (6)); 307 rerun record (recon-01 reproductions; audit did not rerun the survey); 310 n = 8 scope and the audit's fresh n = 1..7 rerun; N306 parameter range. Also current-evidence pointers in 301, 314, 315, N307, N308 (audit's fresh runs).

## LC-M1 — no-uniform-radius inference

Disposition: **fixed (withdrawn) + OPEN record.** Removed "δ₀(n) → 0 … no radius uniform in n" (313), "the obstruction is per degree, not uniform in n" (N303), "δ_0(n) → 0" (300 row), "δ₀(n) → 0 as n grows" (SUMMARY). Replacement: chosen radius δ₀(n) (may be taken nonincreasing); certified lower bounds for the positivity radius of P_n decrease over n = 4..12; no uniform-in-n radius established. New PD-T?…-319 (OPEN) distinguishes chosen radius, ρ_n (positivity radius of P_n) and δ_obs(n) (maximal obstruction radius) and records (U1) ρ_n → 0?, (U2) inf_n δ_obs(n) > 0? with the evidence; the earlier "roughly n⁻³" is not supported (descriptive log–log slope ≈ −4.1). This also records the disposition of reconstruction-02's L7 recommendation (its acceptance in response-recon-02 is corrected).
Files: 313, N303, 300, 319 (new), SUMMARY.md, SPLITS.md. New IDs: PD-T?bivariate-lanczos-claude-319.

## LC-L1 — stale status pointers

Disposition: **fixed.** N303 status row (CONDITIONAL → PROVED, citing 313 and its independent checks); candidates.md OBST?…-L3-b (l.139), IDEA 312 (l.145), IDEA 313 (l.159) with bracketed original wording; 311 ("7 values" → 8 values; prior independent computations vs the audit's log review vs the audit's fresh execution distinguished); 300 split list. No status upgrades.

## Consolidated checklist items for L3

1 → LF-M1. 2, 3 → not L3. 4 → LC-M1, LF-R1. 5 → LF-M2 (T304 split), LF-R2 (rate wording), LC-L1/LF-S (stale pointers); the theory count 64 → 67 and N503 are orchestrator/L5 items (not in L3 files). 6 → **unresolved here (orchestrator, PR preparation):** canonical literature records for the L3 prior-art statements (Di Dio–Schmüdgen, Blekherman 2012, Tchakaloff, DST, Passer–Shalit–Solel); final ID allocation.

## Status changes and materiality

No status upgrade. Material changes to PROVED claims: 302(b) statement (corrected; old variant REJECTED: refuted, N309); 304 statement narrowed (isomorphism moved out; PROVED parts unchanged); new PROVED 318 and N309; new OPEN 316, 319; new MEASURED 317. Per-degree obstruction theorems (N301, N303, 313), rate theorem 303, 305/306/310 unchanged in substance. All material changes return to AUDIT. Runs needed: independent checks of the two new scripts and of 302(b2)/(b3), 318 and N309 (Codex re-audit); `review_L3/indep_generator_cert.py` rerun (for a Padua n ≤ 3 corollary of 316 via 318); items in SUMMARY §6. SUMMARY.md: the Write tool blocked this developer's write; full text handed back for the orchestrator to save.

## File → sha256 after changes

| File | sha256 |
|---|---|
| tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-300-l3q1-backward-interpretation-target.md | a1157022d0750fe6f64eb5bfc6a6c7f0182d8f68840f9069f73f8c96461e0143 |
| …-301-truncated-favard-sections.md | 6362f6ff465ab4d8d93e2cdb0fd49989e0faed93430edbfccc9bcdc63b4a03c8 |
| …-302-backward-reduction-moment-cone.md | fd21c38c54355f9951dbc4281fb6cb79377d66541d6ffb272c2b895ba20a5d93 |
| …-303-moment-cone-rate-theorem.md | e2cebac0f5f6181d75a412ef815f8c11f2e788ce21d90cf3dff1c940c619c7f9 |
| …-304-square-case-commutator-bounds.md | efbf1ab4adb34eda1ad0006e30eb2a22ef387e5235986ac5498d2e539f35781b |
| …-307-square-case-hessian-condition-measurements.md | 683ad23074cc20ae56126bed032efc9bcd77f211922a24f142617365b5b3691b |
| …-308-compression-model-no-obstruction.md | 88bc0093ab89d29be72e06fc8c66114b9a4eb86c2c9fb9eb8fb71dd80c8e990d |
| …-310-equispaced-checkerboard-condition-H.md | c2848bc6f183718d9ffa02f12e1f7c6b91274495977edf20c9902640f72cbcea |
| …-311-equispaced-certificate-margins.md | 34a5c33ced7f222705a05df6b62dd42f7bc1624223d12caf329f920c9e876652 |
| …-313-padua-turan-certificate-all-n.md | 8c85a85617469b5b329a826482d78369c7bdff2447e86d4659129b1450299474 |
| …-314-computed-data-consistency-symmetry.md | 5ba1c0bc7493f949cacfb8d76cf740876a249440ebd890611dc5a1ebc42b5557 |
| …-315-consistency-defect-measurements.md | c0bf408f1c0b36c98d34975122afea635b19cc89406333b6676942a968f82fd1 |
| …-316-square-case-first-order-commutator-isomorphism.md (new) | 8a149eaf2ac262824b82b31147042663420ebab68c79d38d0f447b291d2f7e55 |
| …-317-first-order-commutator-rank-measurements.md (new) | 49cf947440ca9e08f3422d563dc47eef836d3649f5dd798505956433f7888bdc |
| …-318-first-order-commutator-formula.md (new) | f293c642ff08dd8677a85dc9582daeb07f0f92a391bacab295d9dd4840f56e19 |
| …-319-padua-obstruction-radius-uniformity.md (new) | 955dbfa15ad4c29d963586ef254bbc75e20d2af6ab8a4cad200264c93d4aaad7 |
| …-N301-padua-n3-exact-backward-obstruction.md | 1c3ef581874c134d14c00b8a4aca1b3039bceadbb5a43728e25ef5d44ae817f1 |
| …-N302-square-case-linear-rate-refuted.md | 7104f281107a413cea3b9509497561fd53b536f94152bce1e7629b2feec8dc26 |
| …-N303-padua-all-n-exact-backward-obstruction.md | 6ef1bbfbcfa818d33626e4435c12e8d2a12d5297463795dccb4a400696b087ed |
| …-N304-compression-model-insufficient.md | 1494e3bad7ddb6b4160c863353ac75f8cadc126162ffdba7f0058edebbde272b |
| …-N306-H-not-decided-by-count.md | 6f4eb65688d9cbf8123b37e54a9e47d4d33a8669385ef40eb848b49b623dc412 |
| …-N307-consistency-survives-loss-refuted.md | c9ef44696d5820b9a48efc8dfa1c29ce2837a27aac271c9d0e5a05f9b8cc552a |
| …-N308-weight-only-greenbaum-fit-refuted.md | 056f450111eece41d0cd6426570776c9ee564a77b319c807e016dd17b7d7de4f |
| …-N309-normalized-residual-threshold-refuted.md (new) | 67ccce2680cba0f303e4db8fd0a3d9762868422539cb4d16554a7116066ba7f2 |
| tracks/bivariate-lanczos/code/L3/t302b_conventions_check.py (new) | f8ad12db997a6c597bf3efd21bf4a1785e30ba29b63a582dbd01e9790f2c0d50 |
| tracks/bivariate-lanczos/code/L3/t318_dkappa_formula_check.py (new) | 8ade3424969a22c2aca1744ce5d8e612117a8c138ddeff9b2e17609d74ce0ea1 |
| topics/bivariate-lanczos-20261031/directions/L3/logs/t302b_conventions_check.log (new) | b829dd853361bf2af7c3bbb9d60b5f31c991bcd6a3fd161cba26eec5419c2039 |
| topics/bivariate-lanczos-20261031/directions/L3/logs/t318_dkappa_formula_check.log (new) | fcc4cc02799253d15a96c531bf93798725e46b3363befa91aaff30839c885e08 |
| topics/bivariate-lanczos-20261031/directions/L3/candidates.md | 55cfbf8ee57f4ce5d5f1e291ea681a8e942a30adb679ce28a540e691306018e0 |
| topics/bivariate-lanczos-20261031/SPLITS.md (L3 section appended; file also holds other sections) | f6b19834bdefa16017f0e72c976311ebdb3c84d9f6579d8227f24cf519315e9f |
| topics/bivariate-lanczos-20261031/directions/L3/SUMMARY.md | pending: saved by the orchestrator from the handed-back text |
| this file | not self-hashed |
