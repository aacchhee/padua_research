# E1 audit findings — load-bearing questions 1–4 (records drift-codex-e1-01…05)

Auditor: Claude Opus 5.5, xhigh (independent auditor E1; not the developer). No file inside the repository was modified, and no state-changing git command was run. Read-only git (`log`, `show`, `status`, `diff --stat`, `rev-parse`) was used for provenance only.

Candidate: branch `codex/padua-lanczos-drift-20261101` at `36c93794ce02f92c76c89e5a9ec8095eb238d91d`, with a clean working tree. Between the scientific source `b09e1db` and HEAD, the only change under `tracks/` and the topic `evidence/` and `directions/` is `evidence/archive-receipt.json`.

Audited content (SHA-256 at HEAD):

| File | SHA-256 | Note |
|---|---|---|
| record 01 | `757cf4ba…` | |
| record 02 | `4651684a…` | |
| record 03 | `38a58ef2…` | equals the independent checker's pin |
| record 04 | `622e76b5…` | equals the pin |
| record 05 | `a2ea9a62…` | |
| e1-full-sweep.json | `0d9c236f…` | equals the manifest |
| e1-freeze.json | `66313783…` | equals the manifest |
| e1-multinode-certificates.json | `fae9c874…` | |
| e1-scalar-cgs2.json | `e215556a…` | |

All E1 code hashes equal the manifest entries: e1_exact `19ce7b77…`, e1_cgs2 `426630eb…`, multinode `32b9e827…`.

## (a) Files read

**Rules and handoffs.** AGENTS.md; agents/claude/CLAUDE_ROLES.md (Independent audit); the agents/WORKFLOW.md status table (lines 65–107); handoffs/02-audit.md.

**Topic documents.** LOG.md, plan.md, report.md, local-results-entry.md, proposed-record-changes.md (it contains no E1 blocks), independent-checks.md, checks/independent-math-01.md, directions/E1.md, directions/E2.md, ideas-e1.md.

**Evidence.**
- Read in full: e1-summary.md, e1-freeze.json (HEAD version and the original at 6920ba6), e1-manifest.json.
- Inspected structure and key fields: e1-scalar-manifest.json, e1-full-sweep.json (all 88 records), e1-scalar-cgs2.json, e1-multinode-certificates.json, e1-posthoc-scalar-ratios.json, e1-sign-check-rotated.json, e1-reproduction-triangle.json, independent-math-01.json (decision and identity fields).

**Theory.** All five E1 records. Predecessors: PD-T041 (exact-certificate-propagator-growth-triangle.md, full); the PD-T051, PD-T053 and PD-T055 statements; the PD-T050 and PD-T054 headers. state/IDEAS.md was grepped for sensitivity, condition, first-order, drift and quotient, and the IDEA-130–159 and IDEA-088 rows were read. The literature INDEX was grepped for Krylov conditioning; the full IDEAS read belongs to the other auditor.

**Code.** e1_exact.py, e1_check.py, e1_verify.py, e1_scalar.py, e1_cgs2.py, e1_cgs2_verify.py, e1_cgs2_witness.py, e1_cgs2_multinode.py, e1_sign_check.py, e1_reproduce.py, check_independent_math.py, README.md.

## (b) Commands executed and results

Scratch directory: `/tmp/claude-0/-home-claude/86053f32-48fa-5413-a794-72c84a52bfb6/scratchpad/audit/E1/`. All runs used `PYTHONPATH=/workspace/padua-drift-runs/python-deps OPENBLAS_NUM_THREADS=1`, Python 3.13.18 and python-flint 0.9.0. My own code (`ind_basis.py`, `ind_aggregate.py`, `ind_scalar.py`, `first_principles.py`) imports no producer code. The producer is imported only in `compare_small.py`, for comparison.

1. **Independent degree-12 aggregate bounds** (`ind_aggregate.py`). The method differs from the producer at every step:
   - the canonical monomial basis comes from an exact Gram LDLᵀ, not parent Gram–Schmidt;
   - α_kl comes from that basis, with the identity a_k b_p − Σα b_l = b_k checked exactly at every node;
   - the response g is a column of Λ_i⁻¹ per node, rather than a per-source vector recursion;
   - exact BᵀB = D is checked (T24 0.2 s, rotQ24 5 s).

   T24 used exact rationals for all four rules: Knode², KHS², Urow², choices and maximizing witness all **exactly equal** the committed sweep. rotQ24 bj and alt used rigorous arb balls at 512 bits: every committed rational lies inside a ball of relative width about 1e-147, and choices and witnesses are equal. From my own balls alone:
   - L_BJ²(lower)/U_alt²(upper) = 137.3648 (> 121, > 11.72²; L_BJ² > 8.8e10; U_alt² < 6.42e8);
   - the KHS-only ratio is 62.1636 < 100.
2. **Whole 88-case sweep** (`sweep_check.py`). T24 matches in 44/44 cases (exact equality). rotQ24 matches in 44/44 cases: rigorous balls contain every committed Knode², KHS² and Urow² rational, and the choices are equal (degrees 2–11 all rules, plus degree 12 for all four rules).
3. **Pivot ties.** I detect ties exactly (T24 from exact rationals; rotQ24 from the exact basis, before the ball stage).
   - T24 has no ties at any degree; the minimum relative margin |σ_X−σ_Y|/(σ_X+σ_Y) is 0.0084 at degree 12.
   - rotQ24 has an **exact tie at column (2,1)** at every degree 2–12. Both candidates give the same product x∘y, because the grid is invariant under rotation by 90°.
   - With the tie resolved to Y (`ind-rot-pivotY-arb.json`), only that choice changes. At degree 12, Knode² is unchanged (1.487755e9), KHS² goes from 3.581e10 to 4.026e10 and Urow² from 1.897e10 to 1.969e10.
4. **Small-case first principles** (`first_principles.py`). Generic rational sets: 14 nodes at degree 3 and 20 nodes at degree 4, all four rules, no ties, exact Fractions.
   - *Record 01.* The exact dual-number derivative of the full exact-projection recursion (all α and d differentiated) satisfies R_s ḃ = R_s V exactly. The unprojected difference ḃ − V is nonzero (max |·| about 6–9), and ‖V D^-1/2‖ is 1.15–2.77× ‖T(f)‖. With exact rational ε, θ(ε)/(ε‖T(f)‖) − 1 equals 4.7e-6, 4.7e-9 and 4.7e-12 for ε = 1e-6, 1e-9 and 1e-12, i.e. it is O(ε).
   - *Record 02.* L ≤ κ_est (alternating maximization of the spectral output) ≤ κ_F (2→F operator norm) ≤ min(KHS, Urow) holds in all 8 cases.
   - *Record 03.* I ran a **full normalized-trajectory replay** of the declared CGS2 graph, with a formal δ on every scalar operation (5454 per case: products, sums, dots, squares, sqrt, divisions) in 80-digit dual numbers.
     - R_s q̇ agrees with the amplitude-table prediction R_s V D^-1/2 to relative error ≤ 1.3e-80, both overall and separately for each class (mul, mv1p, mv1s, sub1, sub2, div).
     - Dot and norm δ's alone give a normal part ≤ 6e-81 while the tangential part is 1.27, so they lie in the polynomial kernel without being zero.
     - Second-matvec δ's alone give a zero derivative.
     - At ε = 1e-20 and 1e-30, θ(ε)/(ε·predicted) = 1.0.
5. **Producer against my implementation on the same small sets** (`compare_small.py`, producer functions `e1_exact.bounds` and `e1_cgs2.run`). Knode², KHS², Urow², choices and the full-graph U_inf² are all exactly equal in 8/8 cases.
6. **Independent record-05 check** (`ind_scalar.py`). I implemented ρ_hi, U_inf² and S_ti myself and recomputed greedy signs.
   - T24 (exact): U_inf²(pivot), the BJ greedy lower bound (with committed signs and with my own signs), and the expected random-sign gain all **exactly equal** the committed values. My greedy signs equal the committed ones.
   - rotQ24 (arb): balls contain U_inf²(alt), the greedy lower bound and the expected gain. My greedy signs equal all 625 committed signs, with 0 ambiguous sign decisions.
   - Ratios: T24 657331.077 (> 640000, > 100). rotQ24 62.0855 (> 49, < 100).
7. **History check** (`dead_all_degrees.py`, exact). The original freeze's DEAD clause (6920ba6: "on either set", any degree, KHS) **never fires** at degrees 2–12 on either set. The same inequality with the sharpened U_BJ = min(KHS, Urow) holds at T24 degrees 2–4 and rotQ24 degrees 2–6; BJ coincides with alt at degree 2. SURVIVES-original holds at T24 degrees 8–12 only. SURVIVES-sharpened holds at T24 degrees 7–12 and rotQ24 degree 12 only.
8. **Decisive inequalities from the committed rationals** (`compare.py`, Fraction). All 20 checks are True, including:
   - the six inequalities stated in record 04;
   - T24 ratio² ∈ (1269287, 1269288), and κ ratio ∈ (1126, 1127);
   - rotQ24 sharpened ratio² ∈ (137.36, 137.37), κ ratio > 11.72;
   - rotQ24 KHS ratio² ∈ (62.16, 62.17) < 100;
   - the best comparator is pivot (via KHS) on T24 and alt (via Urow) on rotQ24.
9. `python3 tracks/…/e1_check.py --evidence …/e1-full-sweep.json --output <scratch>/own-e1-check.json`: the output is **byte-identical** to the committed e1-exact-check.json.

**Orchestrator reruns compared.** Files under `scratchpad/runs/`, compared by exact Fraction equality of every exact field plus string equality of the sqrt intervals, choices, witness and counts:
- audit-T24-bj, audit-T24-pivot, audit-rotQ24-bj and audit-rotQ24-alt.json are **identical** to the committed degree-12 records in all mathematical fields (the producer hash is the same; only the Python version and timings differ).
- audit-e1-check.json is byte-identical to e1-exact-check.json. The first orchestrator attempt failed on a missing `/usr/bin/time`, and the later run succeeded.
- audit-e1-derivative-check.json has checks identical to e1-derivative-verification.json (360 and 800).
- audit-scalar-rotated.json and audit-scalar-triangle.json (`e1_reproduce`) both PASS.

## (c) Dispositions

| Record | Claimed | Disposition | Reason |
|---|---|---|---|
| 01 span derivative | PROVED | **CONFIRMED** | Proof reconstructed (the induction keeps E_k ∈ S_deg k; graph sine = ‖Z‖/√(1+‖Z‖²)). Exact derivative and FD checks pass; gauge statement f_k/‖b_p‖ is correct; remainder is fixed-data only. Editorial only (F9). |
| 02 rational bounds | PROVED | **CONFIRMED** | Rank-one Knode, HS and row bounds reconstructed for spectral output; restricted-J upper ≠ full upper is stated correctly. L ≤ κ ≤ κ_F ≤ min(H,U) holds numerically. |
| 03 scalar CGS2 bridge | PROVED (formal model) | **CONFIRMED** | Amplitude table and kernel claims reconstructed. My full normalized-trajectory replay (degree 3) agrees to 1e-80. No IEEE lower-bound claim and no promotion of the local-primitive checks. Wording only (F8). |
| 04 finite aggregate separation | PROVED (computer-assisted) | **CONFIRMED-WITH-CORRECTIONS** | The reduction, exact arithmetic, committed producer/evidence and actual reruns all hold. My implementation-independent recomputation reproduces all 88 cases and the decisive inequalities. Corrections needed: rotQ24 pivot tie not disclosed (F1); tautological trace check described as verification (F2); statement thresholds not in a committed checker (F3); freeze provenance wording (F4). |
| 05 finite scalar capacities | MEASURED; factor-10 INCONCLUSIVE; >7/>800 post-hoc | **CONFIRMED-WITH-CORRECTIONS** | Endpoints, signs and ratios are independently reproduced; the INCONCLUSIVE and post-hoc labels are correct. Corrections needed: stale "pending" text contradicting the record's own receipt, and an unexplained retention of MEASURED (F5); reproduction path for the uppers (F6). |

## (d) Findings

Counts: high 0, medium 2, low 7.

**E1-F1 — medium — exact pivot tie on rotQ24 is undisclosed and undetected.**
- Locations: `tracks/bivariate-lanczos/code/drift/e1_exact.py:77-78` (the max key resolves ties silently and records nothing); `drift-codex-e1-04…md:15`; `directions/E1.md:32`; `report.md:18` ("exact pivot-adaptive selections"); `evidence/e1-summary.md` table row "rotated Q24 pivot"; `checks/independent-math-01.md:23,52` (rotQ24 BJ/pivot 4.648).
- Evidence (item 3 above): an exact tie σ_X = σ_Y occurs at column (2,1) of rotQ24 at every degree. Neither the documents nor the code detect or report it. The Y tie-break changes the rotQ24 pivot KHS² by +12% and Urow² by +3.8%. At this data the adaptive pivot rule has no derivative; only each frozen tie-break does. Record 01:39 correctly excludes ties.
- Impact: no decisive claim changes. rotQ24 uses alt, and T24 pivot has no tie (margin 0.0084), so on T24 the frozen and adaptive derivatives coincide locally. The rotQ24 pivot rows of the 88-case sweep and the descriptive tables are, however, X-tie-break values.
- Required:
  - make the producer record ties;
  - disclose the (2,1) tie and its symmetry cause in record 04, E1.md and e1-summary;
  - label the rotQ24 pivot values "X-tie-broken frozen sequence";
  - state the T24 no-tie fact explicitly.

**E1-F2 — low — "exact projector trace" check is tautological.**
- Locations: `e1_check.py:21`; `e1_exact.py:94,121`; `drift-codex-e1-04…md:65,69`; `e1-summary.md:47`; `checks/independent-math-01.md:11`.
- Evidence: Σ_i(1−Σ_k b_k(i)²/d_k) = M − N holds identically whenever d_k := ‖b_k‖², for any nonzero vectors, so the check verifies neither orthogonality nor the projector property. At degree 12 the producer's orthogonality is "by construction" only; e1_verify checks pairwise orthogonality at degree 3 only. The decisive values are nonetheless confirmed by my implementation-independent recomputation, including exact BᵀB = D at degree 12 on both grids.
- Required: replace the trace check with an exact BᵀB = D check in the producer or checker (cheap), or describe the trace check as a consistency identity and not a verification.

**E1-F3 — low — record 04's stated inequalities are not checked by committed code.**
- Locations: `drift-codex-e1-04…md:17-25,67,79`; `e1_check.py:39-42` (it tests only the factor-100 criterion).
- Evidence: the four absolute thresholds and the >1000 and >11 ratios were checked ad hoc by the developer (record 04:67); the independent JSON records only >100. I verified all six from the committed rationals (item 8). The rotQ24 margin U_alt² < 6.42e8 is 0.02%, which is exact but tight.
- Required: add the six inequalities to e1_check.py or a small committed checker, and commit its output, as the computer-proof rule requires.

**E1-F4 — low — freeze provenance wording is overstated or inconsistent; the substance is disclosed.**
- Locations: `evidence/e1-freeze.json:2,12,16,19-27`; `directions/E1.md:53,67`; `drift-codex-e1-02…md:90`; `ideas-e1.md:22`.
- Evidence:
  - The earliest committed freeze (6920ba6, 11:12:02 UTC) already contains the Urow addition, under `"frozen_before_run": true`. No committed KHS-only pre-run snapshot exists.
  - The `dead` field was edited in place at c89eb6a to add the final-degree scope.
  - The amendment note (11:13:25 UTC) says T24 degree-12 full results for all four rules and rotQ24 alt had already been inspected on the code side.
  - E1.md:53 ("sent before receiving numerical comparison results") and record02:90 ("before receiving results") differ from freeze:12 ("after initial n2 restricted-source run"). E1.md:67 ("before receiving the final full-map result") differs from freeze:26 ("received after full T24 final and standalone rotated alt were known").
  - My exact check shows the original any-degree KHS DEAD never fires, so both corrections are immaterial to the original test. The analogous sharpened-U DEAD inequality would fire at low degrees (T24 2–4, rotQ24 2–6), so the final-degree scope matters for the tightened certificate; this is undisclosed.
  - The chronology rests on unlogged messages, which the independent checker also noted.
- Impact: the report conservatively keeps the original test INCONCLUSIVE, and Urow is a proved bound, so no claim depends on timing.
- Required: per-field frozen flags; a note that 6920ba6 already includes Urow; reconciled wording in E1.md:53/67 and record02:90; a one-line note of the low-degree sharpened-DEAD fact.

**E1-F5 — low — stale "pending" text, and the record-05 status rationale.**
- Locations: `drift-codex-e1-05…md:67` ("remaining consequential independent execution"), `:77` ("Independent full finite reproduction is required before upgrading…"), `:85` (Open items); `directions/E2.md:9` ("MEASURED pending independent full finite reproduction") and `:13`; `ideas-e1.md:95-96`; `plan.md:20` ("finish scalar graph evidence"); `evidence/e1-scalar-manifest.json` actual_execution; `e1-scalar-cgs2.json` developer_checks.
- Evidence: all of these contradict record 05's own receipt (lines 91–103), LOG:66-77 and report.md:154. Record 05:77 names an upgrade condition (independent full finite reproduction) that the receipt says is now met, yet the status stays MEASURED with no reason given. MEASURED is not an overclaim. The finite exact inequalities (>800 on T24, >7 on rotQ24, ratio of bounds <100 on rotQ24) meet the computer-proof requirements: record 03 reduction, exact arithmetic, committed code and evidence, independent reruns.
- Required: reconcile the stale lines, and either upgrade record 05 to a finite computer-assisted PROVED (keeping the factor-10 INCONCLUSIVE verdict and the post-hoc labels) or state why MEASURED is retained. The evidence JSON snapshots may stay immutable, with an annotation in the manifest.

**E1-F6 — low — the record-05 regeneration path covers only the BJ lower bound.**
- Locations: `code/drift/README.md:37-49`; `e1-scalar-manifest.json` reproduction_commands; `drift-codex-e1-05…md:67`.
- Evidence: e1_reproduce regenerates the BJ capacities, signs and gain, and the explicit projection (both sets PASS in the orchestrator rerun). The comparator full-graph uppers U_inf need `e1_cgs2.py` commands, which appear only inside the e1-scalar-cgs2.json records; I recomputed them independently and they match. Separately, e1_reproduce's output field `input_sha256` hashes a temporary JSON that contains timings and paths, so it is not reproducible: committed `c0ad…` against rerun `a182…`.
- Required: list the e1_cgs2.py commands for both comparators in the README and manifest, and drop or explain the nonreproducible hash field.

**E1-F7 — low — novelty-gate shortlist omissions (no novelty is claimed).**
- Location: `directions/E1.md:7`; `ideas-e1.md:11,13`.
- Evidence: IDEA-088, a bivariate Fischer-type first-order condition number (settled background), matches E1's own search terms "condition" and "first order" but is not listed. LIT-114 (Kuznetsov 1997; Carpraux–Godunov–Kuznetsov 1996, Krylov–Hessenberg sensitivity) and LIT-255 (condition number of Krylov bases and subspaces, unread) are the closest literature pins, but only "classical Krylov-subspace conditioning" is cited.
- Required: add these with a one-line separation each. The separations are: node/weight-perturbation input versus residual injection, and a single-operator Krylov space versus two-operator graded selection.

**E1-F8 — low (editorial) — record 03 wording is stronger than the formal model.**
- Location: `drift-codex-e1-03…md:4`, alias "vector arithmetic controls first-order span drift"; the title says "rounding map".
- Evidence: the body correctly restricts everything to the formal relative-error model and says no IEEE lower bound or activation follows (lines 18, 82, 134-136). The alias reads as a causal or IEEE claim.
- Required: reword, e.g. "vector-operation amplitudes determine the first-order normal map in the formal relative-error model".

**E1-F9 — low (editorial) — record 01 degree symbols.**
- Location: `drift-codex-e1-01…md:10` versus `:19-33`.
- Evidence: injectivity is assumed "through degree n" but the statement uses stage s, and s ≤ n is never stated.
- Required: add "for s ≤ n".

**Items checked with no finding.**
- The normal-quotient derivative was distinguished from the raw PD-T041 entry, both in the proof and numerically.
- The source scaling ‖f_h‖/‖A_h b_p‖ is gauge-invariant.
- Restricted (degree-2) uppers are never used for full decisions: e1_check filters `sources=='all'`.
- Spectral and Frobenius output are kept distinct.
- The fixed-data remainder is stated with no uniform claim (record 01:33, record 04:79).
- The aggregate Hilbert norm and the scalar l-infinity norm stay separate (record 04:85, record 05:10).
- Decisive comparisons use no floats (Fraction, fmpq and isqrt only).
- No PD-N is created for an inconclusive result.
- report.md and local-results-entry.md agree with the records on all E1 numbers and verdicts. I checked κ ratio > 1126 and > 11.72, KHS² ratio 62.16, row ratio 137.36, scalar 657331 and 62.09.

## (e) Remaining uncertainty

- **Trusted dependencies.** All exact results trust CPython, python-flint (fmpq, fmpq_mat, arb) and mpmath. My rotQ24 recomputation relies on arb ball soundness, though the inputs are converted from exact rationals and the balls are about 1e-147 wide.
- **Independence.** My code is independent of the producer in algorithm and in code, but was written by one auditor in one session.
- **Replay depth.** The full normalized-trajectory replay of record 03 covers degrees 3 and 4 (14 and 20 generic nodes) only. No degree-12 trajectory replay was run, and no actual IEEE realization was tested; none is claimed in the records.
- **Chronology.** The relative order of the Urow addition, the initial degree-2 run and the degree-12 inspections cannot be verified from durable records (F4).
- **Not audited here.** E3–E6 records, the complete IDEAS read and the cold-storage ZIP are outside E1 scope. e1_fp.py and e1-n12-directional-snapshot.json were not re-executed; both are descriptive.
