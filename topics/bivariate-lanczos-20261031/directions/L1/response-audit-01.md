# L1/L4 — Response to Codex audit-01 (`../../audit-01.md`, `../../audit-01/L1-foundations.md`, `../../audit-01/L1-later.md`)

## Header

Developer: Claude Opus 5.5, effort xhigh (L1/L4 mathematical developer). Written 2026-11-01T08:45:23+01:00; the History stamps in the edited files are 2026-11-01T08:33:59+01:00 and 08:41:34+01:00.

Rules: AGENTS.md, agents/WORKFLOW.md, agents/claude/CLAUDE_ROLES.md and templates/THEORY.md, read at branch head `5f52331`. Audited candidate: `5ccfac223f466a9105450365d8c6c3781ff7d922`. The working tree has a later WIP checkpoint `6db7951` by the orchestrator; it touches no L1/L4 file.

Process:
- I read all three audit reports in full, with their evidence folders. I did not edit any audit file.
- I performed no Git operation; the orchestrator commits.
- New computations: one exact check script and one reanalysis of stored data (both under `tracks/bivariate-lanczos/code/L1/`, logs under `logs/`). No recurrence was rerun.
- Every changed statement has a dated History line in its file that quotes the original wording.

Novelty gate: it does not apply. This response adds no new mechanism or candidate. The two new IDs are splits of existing claims, required by the split-first rule.

Finding IDs below follow the audit reports. The L1-foundations reconstruction notes and the L1-later table notes carry no IDs in the reports; I label them **RN-…** and **TN-…** so that each has a disposition.

## L1-foundations

### F1 — T108(3): the degree-only parent condition does not give a triangular selection (medium)

- **Disposition: fix.**
- File: `tracks/bivariate-lanczos/theory/window-recurrence-row-selection-of-jacobi-pencil.md` (PD-T?…-108).
- Statement, part 3: the degree-only condition is replaced by admissibility, A·lm(q_l) = lm(q_k). This is equivalent to "nonzero coefficient at π_k and no later unknown"; the equivalence is proved in the corrected proof 3.
- The mirror is now the fixed-order mirror rule, distinguished from exchanging the coordinate order (another basis, orthogonal within each degree).
- "A different propagator" becomes "its own propagator, in general different".
- Proof 3 is rewritten. Its old "(the β's)" holds only for the dev parents.
- A Remark gives two exact counterexamples to the degree-only wording:
  - the audit's sheared grid: coefficient √5/3 at the later unknown, so the system is not triangular, although it happens to be nonsingular;
  - the unsheared 4×4 product grid: the same degree-only assignment is singular (rank 5 of 6 at five points), so the solution is not unique.
- Every parent rule used in the selection experiments (dev, mirror, alt, adapt; PD-N?…-105, `l1_c01_recon_checks.py`, `review_L1/rv_core.py`) is admissible by construction, so no measured selection result is affected.
- Status: PROVED, unchanged.
- Evidence: `logs/a01_exact_checks.log`, exact Fraction arithmetic:
  - the sheared grid at n = 2 and a 40-node random rational set at n = 1–4;
  - six selections each (dev, fixed-order mirror, per-degree switch, three random admissible): all triangular with nonzero pivots, solution = p(z) at every test point;
  - x-first vs y-first overlap² = 1/5;
  - the audit's own independent value: `audit-01/L1-foundations/independent_exact.log`.

### F2 — T108(1–2): the homogeneous pencil has no left inverse; the normalisation must be included (low)

- **Disposition: fix.** Same file.
- Parts 1–2 now name the homogeneous coefficient matrix C(z) ∈ R^{2N_{n−1}×N_n}. It satisfies C(z)p(z) = 0 and rank C(z) = N_n − 1 for every z (proved: p(z) is in the kernel, and the triangular dev rows give the lower bound).
- The normalised system [e_0ᵀ; C(z)]π = [1; 0] has the unique solution p(z). It is square for n = 1 and overdetermined for n ≥ 2 (row count 2N_{n−1} + 1 − N_n = (n+1)(n−2)/2 + 1).
- L*(z) = S[e_0ᵀ; C(z)], L*(z)p(z) = e_0, and L*(z)⁻¹S is the triangular left inverse.
- The probability normalisation (p_0 = 1) is now explicit in Assumptions, and the Scope sentence is corrected.
- Evidence: in `a01_exact_checks.log`, rank C(z) = N_n − 1 and rank [e_0; C(z)] = N_n at every test point, for n = 1–4. The shapes are 2×3 / 3×3 at n = 1 (square), 6×6 / 7×6 at n = 2, 12×10 / 13×10, 20×15 / 21×15. These agree with the audit's 6×6 rank 5 and 7×6 rank 6.

### S1 — T105 part 2′ is a separate CONDITIONAL claim inside a PROVED file

- **Disposition: fix (split).**
- New ID: **PD-T?bivariate-lanczos-claude-116**, file `tracks/bivariate-lanczos/theory/product-measure-computed-propagator-transfer-conditional.md`, **CONDITIONAL**.
  - It takes part 2′ and the floating-point Assumptions sentence of T105.
  - Main statement: transfer of the factorisation to the computed propagator of a floating-point run, under the named hypothesis H_δ (κ(z_i)δ ≪ 1). This is the original hypothesis ‖L(z)⁻¹‖δ ≪ 1 restated.
  - It contains a labelled minor routine PROVED step, which is "first order in δ" written out: ΔL is independent of z, κ ≤ B (the T105 univariate bound), and the Neumann bounds.
- T105 (`product-measure-propagator-factorization.md`):
  - It keeps parts 1–3 PROVED. `Split into:` names T116, and T116 has `Split from:` T105 part 2′.
  - The 2′ row and the Assumptions sentence are removed; both originals are quoted in History.
  - Two status-table evidence cells are relabelled as cross-references. Row 3's pointer is corrected from PD-T?…-107 (f), "1–2.5", to (e), "0.3–2.5".
  - Open items (i)–(ii) now point to T110 and T113, and (iv) H_δ is added.
- SPLITS.md: row added.
- Evidence: proof in T116. Measured context, consistent with H_δ but not establishing it: tensor 41² within-degree coupling ≤ 7e-15 (PD-T?…-107 (e)). A measurement of δ·κ is listed as Runs needed.

### RN-102, RN-105, RN-106 — reconstruction notes requiring no change

- **Disposition: no change.**
- 102: the file already states first order in u (constants not optimised) and carries the two-pass correction.
- 105: the existing History extension of A′_t to 0 ≤ r < j governs part 3, as the audit says.
- 106: the existing exact-window index correction is in place.

### RN-103 — the explanatory division by ‖Bs‖ needs Bs ≠ 0

- **Disposition: fix.** File `full-operator-paige-identity-growing-blocks.md` (PD-T?…-103).
- Part 3 now reads "when Bs ≠ 0 …; when Bs = 0 only the undivided inequality is asserted". The identity, the bound and the status (PROVED) are unchanged.

### RN-108 — the two-relation completion need not give the same orthonormal basis

- **Disposition: fix.** Included in the F1 rewrite of part 3: "the particular orthonormal basis … depends on the completion".

### RN-401 — the edge case of Corollary 2 and the orthogonalised staggered starts

- **Disposition: fix (proof completion).** File `l4-band-krylov-obstruction.md` (PD-T?…-401).
- The proof of Corollary 2 now covers two points:
  - the edge case S_n = B_{0,i}, where m ≥ dim S_n ≥ n+1 directly;
  - the identification with the orthogonalised starts v_a = q_{(a,0)} of the Statement: F^b v_a has leading monomial x^a y^b, so these vectors span S_n.
- The audit's other remark ("no all-degree obstruction on an arbitrary fixed finite set is asserted") matches the file, which states U(2m+1); no change.
- The Statement and its status (PROVED) are unchanged. Exact rank checks of both points at n = 1, 2: `audit-01/L1-foundations/independent_exact.log`.

## L1-later

### LL-M1 — N101 asserts a 10²–10¹⁴ excess on sets and residuals that were not measured (medium)

- **Disposition: fix.** File `ritz-residual-governance-fails-off-product-supports.md` (PD-N?…-101). The status is unchanged (MEASURED); the scope is narrowed.
- The title is restated (original in History), and Statement (a) is rewritten as follows.
  - **Thresholds paragraph.**
    - The pre-registered kill threshold is the factor-3 band, with τ = 10³u and u := 2^-52.
    - The "/under" factor 30 and the quoted magnitudes are descriptive.
    - Ranges are given at both 2^-52 and 2^-53.
  - **(a1) The 14 R01 main non-product runs, all five objects.**
    - No informative triple lies in the band.
    - At 2^-52 the ratios lie in [1.02·10², 1.03·10¹⁴]. At 2^-53 they lie in [4.4·10¹, 2.1·10¹⁴], so the old lower end 10² holds only under the pre-registered convention.
    - The growth is 1.3–4.4 decades per 4 degrees for n = 8–24.
    - Rotation pairs: ρ_Z is equal to relative 2.3·10⁻¹² while both losses are below 10⁻⁸, and to 4 digits through n = 24.
  - **(a2) The seed-11 rotation 0.3, π/4, disk and triangle sets, Z only.** Ratios ≈ 3·10²–1.1·10¹³, computed from one-digit log values (uncertainty up to about a factor 3).
  - **(a3) The probe-only sets** (rotation 0.05, shears, rotated Beta set). They carry no Ritz claim and lie outside the negative statement. The 0.05 rotation is near the Ritz level by the auditor's independent measurement (3.72 / 3.93 / 7.16 at 2^-52), recorded as context.
- The other sections:
  - (a′) is stated with its set: the seed-11 square rotated by 0.3.
  - The parameter range, status table, disposition scope and Checks are updated. The Checks cite the audit's independent checks with their hashes.
  - The inaccurate History bullet "PC-1 … is folded in" is corrected in a new History line.
- Consistency in other files:
  - PD-T?…-107 gets a correction bullet restricting "(b) independent of Ritz convergence" to the sets with Ritz data.
  - candidates.md: PC-1 is marked applied, and A01 records the narrowed scope of IDEA?…-101/-102. Their disposition (REJECTED: failed) is unchanged.
  - SUMMARY item 1 is updated.
- Consolidated item 3 asks to distinguish the √u threshold from a relaxed kill threshold. The L1/L4 files define no √u threshold; that item concerns L2's T207 (L2-F3). The L1 analogue is the distinction between the factor-3 kill band and the descriptive factor 30 / 10² magnitudes, and between the 2^-52 and 2^-53 conventions; N101 now states it explicitly.
- New code and log:
  - `tracks/bivariate-lanczos/code/L1/l1_audit01_n101_reanalysis.py`, a reanalysis of the stored `logs/r01_{input3,rotation,irregular}.raw` and `logs/r02_node_propagator.log`. It reruns nothing.
  - Log: `logs/a01_n101_reanalysis.log`.
  - Command: `python3 -I tracks/bivariate-lanczos/code/L1/l1_audit01_n101_reanalysis.py topics/bivariate-lanczos-20261031/directions/L1/logs > topics/bivariate-lanczos-20261031/directions/L1/logs/a01_n101_reanalysis.log`; Python 3.13.18; under 1 s.

### LL-M2 — T114 has substantive PROVED and MEASURED parts under one ID; T113's Q40 condition can be discharged (medium)

- **Disposition: fix (split, and status update).**
- T114 split:
  - New ID: **PD-T?bivariate-lanczos-claude-117**, file `tracks/bivariate-lanczos/theory/coefficient-channel-gain-census-checkerboards-measured.md`, **MEASURED**.
  - T117 holds the former part 5 (gain census and first-order predictions) and its closing reading, with the former title clause "the clustered-checkerboard loss is this first-order channel" restated as a measured, scoped title.
  - It cites the audit's producer rerun (`audit-01/L1-later/gain_producer_rerun.log`, sha256 `583ca75e…169e`) and marks it as a producer rerun, not an independent implementation.
- T114 (`first-order-coefficient-channel-gains-product-type.md`):
  - It keeps parts 1–4 and is now PROVED overall, with a new title and `Split into:` T117.
  - The formula check stays as a verification record under Checks.
  - The original title, the whole original part 5 (verbatim) and every adjusted line are quoted in History.
- Dependents updated: T115 (Split from, Definitions, Depends on) and N104 (Depends on) now point to T117.
- **T113, Q_40:** CONDITIONAL → **PROVED** (finite), in `exact-certificate-propagator-growth-triangle.md`.
  - The proof (part 1 reduction plus exact orthogonality) is unchanged. The only open obligation was an independent rerun.
  - Codex audit-01 executed it: `rv2_certificate.py square 40 16`. Log `audit-01/L1-later/cert_square40_rerun.log`, sha256 `4375ae13eae79f3011c3455c09c85798bff7d810aae17ce9111afd17073005f2`; manifest `audit-01/L1-later/manifest.json`, executions[2].
  - Results: 0 off-window coefficients; 0 of 11628 off-diagonal inner products nonzero; log10 G(6) = 2.080 and G(16) = 3.088, matching the stated 2.08 / 3.09. All of n = 2…16 match the developer's log to two decimals.
  - The checker's second method (LDLᵀ) was omitted at this size; the reduction does not need it.
  - The upgrade rests on this executed audit evidence, not on new developer reasoning. Part 3 is now PROVED for all three measures; the stale open item "independent rerun" is removed.
- SPLITS.md: T114 row added. candidates.md A01, SUMMARY items 3 and 5, and §6 are updated.

### LL-L1 — T113's affine scaling sentence is false for c < 0 (low)

- **Disposition: fix.** Same file.
- Corrected statement: for scalar c ≠ 0, ((L*′(cz + d))⁻¹)_{k,s} = sign(c)^{deg k − deg s}|c|⁻¹((L*(z))⁻¹)_{k,s} for s ≥ 1. So entries scale by c⁻¹ for c > 0 (all certificate rescalings, c = 2/m), and squared entries by c⁻² for all c ≠ 0.
- A corrected proof is written: q′_k = sign(c)^{deg k}q_k and L*′ = S D L* D. The original scaling sentence of the proof is quoted.
- The impulse identity and the certificate are unaffected.
- Evidence: in `a01_exact_checks.log`, with c ∈ {−2, −1/3, 3/2} on T_6, n ≤ 4, and the transformed basis recomputed from scratch:
  - norms scale exactly as c^{2 deg k};
  - squared entries scale exactly as c⁻² (1680 entries per c);
  - signs follow sign(c)^{deg k − deg s};
  - 50-digit signed entries deviate by ≤ 1.3e-49.

### LL-L2 — "on-pattern" means structurally permitted, not nonzero (low)

- **Disposition: fix.** File: T114.
- Part 4 now reads "structurally permitted, i.e. may be nonzero (it can vanish, e.g. a^y_{j−1} = 0 for a symmetric marginal)".
- The univariate comparison names the h-coordinate perturbed and states that h- and β-coordinates are independent. A perturbation of b^y_{j−1} itself combines the two coordinate derivatives. Proof 4 is aligned.
- No number changes, since the mask is positional. Originals are in History.

### TN-T107 — finite regimes plausible; parts not freshly reproduced

- **Disposition: no change for the note itself.** The LL-M1 consistency bullet was added to T107 (see LL-M1).

### TN-T109 — P* is a high-precision reference, not exact arithmetic

- **Disposition: fix.** File `non-product-amplification-is-a-priori-measured.md`: (a) is annotated, with a pointer to T113 as the exact certificate on a different measure. MEASURED, unchanged.
- The T108 Checks wording "exact" → "reference" is aligned in the same way.

### TN-T112(e,f)/N103(a) — 27 tensor nodes, not 28; the reference coefficients are computed

- **Disposition: fix.**
- T110 (`near-product-transfer-perturbation-bound.md`): the consistency row now reads 28/28/28/27 nodes, and the coefficients are noted as computed, not certified exact. The informativeness row is relabelled as a cross-reference to T112 (f).
- T112 (e) and N103 (a) state that the "exact-coefficient" propagator uses double full-CGS2 reference coefficients. The audit's producer rerun is cited.

### TN-T112(a,b)/T114(5) — stale weight range 1.7e-33 (PC-12)

- **Disposition: fix.** File `checkerboard-and-near-product-measurements.md`: PC-12 is applied. The bivariate range is 1.8e-67…0.47, the factor ranges are given, and the open item's "33 decades" becomes 67.

### TN-T115/N104(c) and the dot64 paragraph — dot64 includes operand conversion; sufficiency only; the decision is inconclusive

- **Disposition: fix.**
- T115 (`closed-loop-dot-product-rounding-carries-coefficient-channel.md`):
  - title "is closed-loop dot-product rounding" → "closed-loop dot-product rounding … reproduces the … loss (sufficiency within the tested models)";
  - (d) describes the dot64 operation, operand conversion included, and notes that it does not validate the Gaussian term-wise model;
  - the Reading's "alone" is qualified as sufficiency within the models, not necessity or exclusive causation;
  - the audit's closed- and open-loop reruns are cited.
- N104: the stale title parenthesis is restated ("inconclusive with actual double rounding"), and (c) states the convention-free inconclusive verdict in place, with the audit rerun (21.58 / 12.95, 16.40 / 21.13).

### TN-N101

- **Disposition:** see LL-M1.

### TN-N102 — the 'full' mode is not full orthogonalisation of every product

- **Disposition: fix.** File `hl-simax-windowed-complex-recurrence-instability.md`.
- The control is described as implemented: all N-products full, the first-vector N*-products windowed.
- A transcription error is corrected: n = 16 is 3.1e-15, not 2.3e-15 (`logs/r01_simax_variants.log`, reproduced by `audit-01/L1-later/simax_producer_rerun.log`).

### TN-N103(b,c), TN-N104(a,b), TN-N105 — scoped measured observations, partly not rerun

- **Disposition: no change.** The files already state finite scopes and give no theorem.

### TN-N106 — "product support" means the sampling domain

- **Disposition: fix.** File `support-shape-does-not-classify-loss-regime.md`: clarification added; the audit's independent exp(8xy) result is cited.

### TN-near-product — "'exact' to ~1e-15" coefficients

- **Disposition: fix.** Covered by TN-T112(e,f): the transfer measurements are labelled as measurements for the computed reference coefficients.

### TN-rules — K1 inconclusive; the blanket timing sentence of candidates.md

- **Disposition: fix (candidates.md).** The header sentence "Kill criteria below were written before …" is qualified: it lists the disclosed exceptions and notes that the timestamps are self-attested.
- K1 inconclusive is already the recorded verdict; no change.

## Consolidated checklist (audit-01.md) items concerning L1/L4

- **(2)** T108: see F1 and F2.
- **(3)** N101: see LL-M1, including the √u remark.
- **(5)** Splits and status pointers:
  - T105 → T116 (S1); T114 → T117 (LL-M2); T113 Q_40 discharged (LL-M2).
  - Stale pointers fixed in T105 (107 (f) → (e)), T106 (107 (e) → (d), relabelled as cross-reference), T110 (informativeness → 112 (f)), T113 (open item) and T115 (→ T117).
  - The "64 → 67" count, the L5 N503 reference and the report wording are not in my ownership; see Unresolved.
- **(6) / protocol P2–P4:** not L1/L4 developer items.

## Other mixed-status rows reviewed (classification proposed for the auditor)

None of these needs a split:
- T101 part 6 is a minor routine lemma.
- T102 row 4's "a priori bound OPEN" is an open item, not a claim.
- T103's "sizes MEASURED in R02" is an evidence note; the claims live in T107.
- T111 row 2's numbers are a verification record; their home is T112 (a).
- T112's "mechanism … OPEN" row is an open question.
- T109's inference row and its REJECTED row were already split (N105).
- T401's transfer list is LITERATURE-as-reported plus T103.
- N102's "structural explanation" is a heuristic interpretation (labelled "CONDITIONAL reasoning, not a proof"). It names no hypothesis, is not used as a dependency and is not reported separately. I therefore classify it as non-substantive; the auditor may dispute this.
- T115 (d)'s label "REVIEWER-MEASURED" is MEASURED with reviewer provenance.

## Unresolved, and items for the orchestrator

- Shared files outside my ownership still carry the pre-audit wording, for the orchestrator or report owner to update:
  - `report.md` Rank 3: "by 10²–10¹⁴" for every residual, which is now the (a1)/(a2) scoped form;
  - the frozen `audit-handoff.md` ("-105 PROVED with IDEALIZED part"; "-114(5)").
- `directions/L1/STATUS.md` is not edited.
- No L2/L3/L5 theory file cites T108, T105 2′ or T114 part 5. L2 files cite T101/T104/T106, whose substance is unchanged.
- H_δ of T116 is unproved, and its measurement is a Runs-needed item.
- The R01 main runs behind N101 (a1) have not been re-executed independently. The audit's independent implementation covered the seed-11 sets only.

## Materiality

The changes are **material to PROVED claims** and should return to AUDIT:
- T108: the statement of parts 1–3 is corrected. The old part 3 was false as written; the proof is unchanged in substance.
- T113: the part-1 scaling sentence is corrected, and part 3 Q_40 moves from CONDITIONAL to PROVED on the audit's executed evidence.
- T401: the proof of Corollary 2 is completed.
- T114 and T105: split, with PROVED content unchanged. T114 part 4 has a wording correction.
- T103: an explanatory qualification.
- New: T116 (CONDITIONAL) and T117 (MEASURED).
- No PROVED result was downgraded.

## File → sha256 after changes

| File | sha256 after changes | sha256 at candidate 5ccfac2 |
|---|---|---|
| `tracks/bivariate-lanczos/theory/window-recurrence-row-selection-of-jacobi-pencil.md` | `81667e10def6423dd0deb139797d72734b1555aa9f126e4e22a8210ccc7c9e02` | `75c3ea0e34de612cfb17362c603a56ea4419323742538d7275a6c33026c77ecd` |
| `tracks/bivariate-lanczos/theory/product-measure-propagator-factorization.md` | `f6561373d262f4b719bde7fe79dcace72782c3b1f8755fc618eeaec2eb7350e3` | `b304e439b9aa069af3865c7efe4e4ee6209cf03227ff1dbd74f16bf39e72a2f3` |
| `tracks/bivariate-lanczos/theory/product-measure-computed-propagator-transfer-conditional.md` | `6d122bf4e03802398d72294f71b3867bb5c5a2846afff538884d8d14e7caaaaa` | (new) |
| `tracks/bivariate-lanczos/theory/first-order-coefficient-channel-gains-product-type.md` | `bc3912e13c7ee6b21fed8e9d3fa1a25427ab8c03b39c22dd7256de5e28d82b1c` | `9dbeb5f4d94745dd02fbc8e51de968a6ff1b3011f84d5766df6141c12a23e692` |
| `tracks/bivariate-lanczos/theory/coefficient-channel-gain-census-checkerboards-measured.md` | `227c30458b4bac88182ba720541a8513201b18e3dc572b46b400f269c615e699` | (new) |
| `tracks/bivariate-lanczos/theory/exact-certificate-propagator-growth-triangle.md` | `332a2e9643c28f31664c49d0858906a3606db2559ac3a8eab5ef2259ac748ab3` | `4d7f17ff8cf75726df97a7c65ad84fb3f455911cb634bd04c0e08ce2533062e7` |
| `tracks/bivariate-lanczos/theory/ritz-residual-governance-fails-off-product-supports.md` | `b1515811af69d77430dbeb6b73187f7c4771ac0df0f8b8ade5c80dcf42ef95f9` | `5388763d07fb877c4a9f04b52621a536817a2a27b802ea432f511aa19f5b27b3` |
| `tracks/bivariate-lanczos/theory/full-operator-paige-identity-growing-blocks.md` | `904cd894c93d6a297a9570279652392432a85b8a41cdf55e34e3b0dbfa0809ad` | `a2707434f266388b8d69310b71ef1921d083b8e2e11051bc8a2653bba9ae589e` |
| `tracks/bivariate-lanczos/theory/l4-band-krylov-obstruction.md` | `a9334fead2767516abd30bf8967d18394af76c489bd9bb56a4e16c200c90ec9f` | `54bf537b5178823af4dbea7ca546999588bc6124404a4d7f3ac269358014749d` |
| `tracks/bivariate-lanczos/theory/exact-omega-recurrence-window.md` | `26931230f9a9f97f46470a461f0cadcdc9fcb172d69fba50d028db416ebafa71` | `b9b984deee3dfa44ba27ab6e7c39ef7c43b98b2b5e678d20c4b6d4d2dd90eaa9` |
| `tracks/bivariate-lanczos/theory/loss-regimes-node-propagator-measured.md` | `1b20334cd1d0ca3b15e7f5565d6a01b4cb0ea5e68206206e30bdf6b182887910` | `dae0bf50b57fd6194079dc2545e64359ac316093dd1fbc2d7e0603363f59db73` |
| `tracks/bivariate-lanczos/theory/non-product-amplification-is-a-priori-measured.md` | `4c48cb5b891a5e572576f761feba545ce5beeb52faf20bcb574ca064d2b8ffb7` | `8decf8dafb97611b88a296ad0344f09e33225f7a0a26afa3cf493aa0096e6544` |
| `tracks/bivariate-lanczos/theory/near-product-transfer-perturbation-bound.md` | `398d73ed7b01bd986aaf4c4c78599b96cc3ea3077028d6c70bd1cc038e5a88e2` | `7dd02ce2455ca553b8196ee771cad25f2a0f2e57f9e3c7d3c439dc30115cff29` |
| `tracks/bivariate-lanczos/theory/checkerboard-and-near-product-measurements.md` | `39d261103e4b3fa3c8cffb5228f7201ef4bc0f3f6bb28c4796fe57855daa91ca` | `6e4ef4cdbbc63395b8ad181e464611a01bbc5ddeedb258e5132e3da151dda633` |
| `tracks/bivariate-lanczos/theory/closed-loop-dot-product-rounding-carries-coefficient-channel.md` | `7090f6e9b60c1827d7ac101f5e244d80eba9b5653ccdfd1e9a7434a9457c8367` | `aecf9975248b07f5d05d1c579b3f42201d9e3252ffc1e5daca123972c37fe0fd` |
| `tracks/bivariate-lanczos/theory/hl-simax-windowed-complex-recurrence-instability.md` | `6a323dd06ea3a80c46b8a679b40f7d254b283d0f5a25b8f41417df54cd4bfb97` | `47cd4f5b518ecba4dcf7a736293acf5f37dba31b5a6127b008fd5134df3aa1f5` |
| `tracks/bivariate-lanczos/theory/r04-failed-scaling-and-predictor-hypotheses.md` | `4956585b3509026815ca5117e4c9d1c7d4186220da026d4545eb1ae78dbc06f4` | `66623728ff6f85a269cd08032722248e016be8a470fd27f00ce8a8565169fee5` |
| `tracks/bivariate-lanczos/theory/open-loop-coefficient-noise-estimates-fail.md` | `788dfdab19558b0b2367dbde6c38df93f0a2073e7b57300454a3068e30c1b2bd` | `c6a51ae6b6862b1b5a4c81a07070ea0d21246e78e1fe4a09061d8d5cf1396bf8` |
| `tracks/bivariate-lanczos/theory/support-shape-does-not-classify-loss-regime.md` | `d7bf176b192c746573d3c94cd93daf905b0cc83f85d578b89279201754b4bc02` | `0a689dc93140d3d6bc0a5181f8f2fdabaa0a2fc83a2df7f6b84ca4e8f0e0017a` |
| `tracks/bivariate-lanczos/code/L1/l1_audit01_exact_checks.py` | `dea227ed257d96686cb9d4538e6667753b40fd3c5746947fcd7525f80440c270` | (new) |
| `tracks/bivariate-lanczos/code/L1/l1_audit01_n101_reanalysis.py` | `bb4bd526d885be7ce0544a8bf9cae51075021d2f1ec7f1a802a187b0a532e937` | (new) |
| `topics/bivariate-lanczos-20261031/directions/L1/logs/a01_exact_checks.log` | `321c114901320b242adbac9bec9d08025107a4af7ee0ea41d848fb065db4db5b` | (new) |
| `topics/bivariate-lanczos-20261031/directions/L1/logs/a01_n101_reanalysis.log` | `3b29cf2fcb1f1aec768e8fa0c7b9edc770afba717f98353ba88f6febc8bc312c` | (new) |
| `topics/bivariate-lanczos-20261031/directions/L1/candidates.md` | `b54087ae1e68984fb0fa8bc02ecc4060ed04aae22c15200cad5e0d172c3b562e` | `d633dbbe32465ec81f6a49d82e5a553cf0dfa0a8adb09b5588072f6a382d4a0d` |
| `topics/bivariate-lanczos-20261031/directions/L1/SUMMARY.md` | `ed93cc765c8b5c16abad203362a7f71f07d2bdede21732fbfeb973e9ac1e9b15` | `174661440746845a193cea9389a7566b9b607825acff7ad5781ab55c7e76c18d` |
| `topics/bivariate-lanczos-20261031/SPLITS.md` | `f6b19834bdefa16017f0e72c976311ebdb3c84d9f6579d8227f24cf519315e9f` | (new) |
| `topics/bivariate-lanczos-20261031/directions/L1/response-audit-01.md` | (this file; hash reported in the hand-off to the orchestrator) | (new) |

SPLITS.md also contains rows appended by the L3 developer in its own section; its hash is that of the file as it stood when this table was computed.
