# Audit 01 — substantive Claude audit of the NN MOP conditioning round

- **Auditor:** Claude, Opus 5.5 xhigh. I was the orchestrator and the independent auditor (handoff [02](handoffs/02-audit.md)). Five Claude audit workers ran in parallel:
  - A (Krawtchouk upper, Opus 5.5 xhigh);
  - B (Hahn, Opus 5.5 xhigh);
  - C (C1 metric and the general-parameter lower, Opus 5.5 xhigh);
  - D (C3/C4, Opus 5.5 high);
  - E (novelty gate and records, Opus 5.5 high).

  I chose xhigh for the mathematics because the work is a new quantitative mechanism and a decisive hard step, and high for the technical and protocol scopes. Workers made no Git or repository changes. I also reconstructed the headline proof myself.
- **Audited candidate:** `cc1edd20a27f955f2f028e988e525889ddfbc805`. The checkout head `64a45b3ec018898fb21ad1bccbc18de2d781ba7f` differs from it only in handoffs 01 and 02, per `git diff --stat`. Base/main is `76ba4214b100c86a44941f5e9a662ce9ce48efb8`, unchanged at audit time.
- **Rules:** I read the rules at `64a45b3`. AGENTS.md, agents/ and state/IDEAS.md are unchanged from `76ba421`.
- **Verdict:**
  - No BLOCKING findings. Every claimed PROVED result is accepted as PROVED, and every MEASURED record as MEASURED, within its stated scope.
  - Three MAJOR findings concern classification, attribution and candidate records. No theorem needs to change.
  - **Stage returns to WORK** for a bounded Codex response ([handoff 03](handoffs/03-response.md)).

## Coverage

- **Rules and handoffs:** AGENTS.md, agents/WORKFLOW.md, agents/claude/CLAUDE_ROLES.md, handoffs 01–02.
- **Topic records:** LOG, plan, rounds, gates, report, note-material, COLD_STORAGE, input-snapshot, evidence-manifest, external-code.md.
- **Gates and attempts:** novelty-gate-C1 to C4, and attempts C1, C2, C2-hard, C3, C4.
- **Theory and checks:** all 18 theory files (the PROVED ones in full); receipts and the 14 c4-tables CSVs; independent-checks-01/02, used as supplementary only; the results file; the PR #32 body.
- **Predecessor dependencies (nn-mop-stability-20261105):** PD-T432, PD-T433, PD-T435, PD-T436, PD-T437, PD-T440, PD-T448, PD-T449. Also PD-T290's input definition (nn-mop-iep-20261103) and the predecessor conditioning.py and native_mixed.py.
- **state/IDEAS.md:** read completely by worker E, lines 1–1112 in ten sequential chunks. That includes every alias, obstruction table and disposition table. Targeted searches: gauge, diagonal scaling, norm balancing, Fischer, weak stability, conditioning, Krawtchouk, Hahn.
- **literature/INDEX.md:** rows read in full for LIT-112/113/114, 119, 347, 348, 365, 502/503, 562–568, 614 and 630, plus the NN MOP conditioning section. The index was searched for Krawtchouk/Kravchuk, Hahn, conditioning, inverse eigenvalue, weak stability and AT/Angelesco/perfect systems.
- **Blocked in this runtime:**
  - `IEP-MOP-main.zip` is absent and Octave is not installed. So M2, M4, the 348 external calls and the Octave-side bit transport were **not rerun**. They were reviewed from receipts and code only.
  - No cold-storage destination is attached.

## Independent reconstruction and reruns

All of the following was actually executed in this session. Independent scripts are committed under [audit-01/claude](audit-01/claude/README.md), with their commands and output hashes.

### 1. Krawtchouk sharp upper bound (c2-sharp-upper.md): accepted as PROVED

- **Reconstruction.** I re-derived the proof by hand, and worker A did so independently. Every step holds:
  - the Bernstein normalization (3)–(5);
  - the differentiated jets (6), including moving nodes;
  - the source split (7) and the Hermite kernel formula (8), with (9) |h₂| ≤ 9+3N/2+N²/8 ≤ 16N²;
  - the separating rectangles (10): the ratios decrease in |y| on the shared side and equal 5+2√6 at u=c;
  - (11), the lengths 14/2π < 3, the grid-differentiation identity (12) and column sums ≤ 3H_M;
  - the Γ₀ bounds (14);
  - the constant sum N²(24M²+80M+48) ≤ 200N⁴;
  - the transfer (16)–(18), the terminal support successor, the recurrence comparison (19)–(21) with gap −(M−t+2)/10, the derivative bounds, the field normalization and 3000N⁴C = 3·10⁶N¹³ρ^M.
- **Other checks:**
  - No step needs N ≥ N₀. N=2 and N=3 were traced by hand.
  - The common source G is integrated only on Γ₀, whose closed disk avoids the branch points 0 and 1. Γ₁ contains 0 and Γ₂ contains 1, so only the polynomial sources use the rectangles. The proof does this correctly but does not say why (MINOR-11).
  - The limit (2) and the gauge squeeze in c1-gauge-sharp-rate.md are valid. B_j = b_j holds under every gauge, κ_monic(six fields) = κ_N(four fields) because the u fields are identically 1, and the parity witness lies in every input variant.
- **Executed checks:**
  - `python3 -I A/c2_hard_check.py`: the byte-exact extraction of the C2-hard block (sha256 452d72d7…, matching the record). PASS, with counts 50/735/1050/330 matching the record.
  - `A/kappa_exact.py 2 18`: exact-Fraction κ_N from the PD-T432 definition. PD-T437 lower ≤ κ_N ≤ claimed upper at every N=2..18; for example κ₁₀ = 7.838e7 against an upper of 10^28.4. From N=4 on, the maximizing row is a₁ at the terminal layer.
  - Predecessor conditioning.py at 80 dps agrees with this exactly for N=3..18.
  - `A/lemmas.py 2 16`: every k-variable identity is exact, and every actual/claimed majorant ratio is below 1. The largest are (13) 0.667, the terminal bound 0.94 and (18) 0.22.
  - `A/contours_formula8.py`: formula (8) with the stated split and contours reproduces the exact top coefficients of R to 2.8e-45 relative, for N ≤ 5 in random mixed directions.
  - `A/contours_pointwise.py`: bounds (5) and (11) are attained at u=c, so the contour bound is sharp there.

### 2. Hahn results: all accepted as PROVED, and the PD-N negative statement accepted as PROVED

Worker B reconstructed every step, and I reviewed that reconstruction.

- **c2-hahn-normality.md:**
  - identity (4), including symbolically in α;
  - the kernel determinant (5) with constant ∏_{r=1}^t r!, symbolically for t ≤ 4 and at random rationals for t = 5..7;
  - the residue formulas (7)–(8);
  - the field scale ≤ 2M+3.
- **c2-hahn-lower.md:**
  - formulas (2)–(5);
  - the M-th difference and the central-binomial bound;
  - witness admissibility, zero mass and no node change.
- **c2-hahn-terminal-rate.md:**
  - the half-grid sign coherence and the hockey-stick identity;
  - the dual (6) and the polynomial comparison A_M/54 ≤ D_M ≤ 3(M+1)²A_M;
  - the generating function (8)/(9) for both parities;
  - the saddle upper bound and the finite-type entropy lower bound;
  - the sextic factorization 2(w−1)²(2w⁴+4w³−2w−1) and the quartic r⁴−14r³+24r²−14r+1;
  - the step to the full-map liminf, including fixed mass.
- **c1-hahn-gauge-lower.md:** the transfer is valid.
- **c2-hahn-upper-envelope.md:** β = 12.449 > 12.2 > ρ_H. It is a correctly scoped PD-N: its negative statement is PROVED, its disposition is REJECTED: failed, and it does not refute the full target.
- **Executed checks:**
  - c2_hahn_checks.py, c2_hahn_terminal.py --max-m 10, independent_hahn_rate.py and c2_hahn_upper_search.py --max-m 6: scientific payloads are identical to the committed JSON.
  - Independent `B/audit_exact_nn.py 16`: exact Hahn κ_N for N=2..16 equals every printed digit of the predecessor PD-T434 table at N4–16 (κ₄ = 49126640/31213), and all lower bounds hold.
  - `B/audit_rate.py`:
    - D_M equals (7) exactly for M=2..24 (the committed checks stop at 11);
    - the generating identity holds exactly for M=2..80;
    - the Richardson-extrapolated ratio is 12.113595, and H/r equals ρ_H = 12.1136005841302404957… to 45 digits.
  - `B/audit_sympy.py`: all symbolic identities hold.
  - Against the predecessor table at N4–64, both lower bounds stay below κ_N.

### 3. C1 metric results and the general-parameter lower bound: accepted

These are accepted as PROVED or MEASURED, as each record labels them. Worker C reconstructed them; I reviewed that reconstruction.

- **c1-gauge-invariants.md:**
  - B_j = b_j identically, and the chain κ_b ≤ K_dep ≤ K_fix ≤ κ_monic.
  - Bounds (2) and (3), with b₁ and b₂ re-derived, the central-index Vandermonde bound, and the M=2, 3 cases.
- **c1-scalar-derivative.md:** the α̇ and β̇ formulas, the weighted-median dual (attainment and weak duality), and the exact-zero convention on Fraction inputs.
- **c1-matrix-metric.md:** (1)–(4).
- **c2-krawtchouk-parameter-lower.md:**
  - the symmetries, the terminal derivative, the summation (9)–(13) and the fixed-mass factor;
  - the specialization ρ(2/5,1/2) = 5+2√6, which with the symmetric orientation recovers PD-T437(13) exactly;
  - it covers every distinct p₁, p₂ in (0,1), and is a lower base only.
- **C1 producer, full grid:** c1_metrics.py scalar and terminal modes, both families, 180 and 260 dps, N4–64, eight runs, all exit 0. Then c1_summarize.py:
  - **c1-grid.csv is byte-identical** (aa3a6e19…).
  - Every scientific field of c1-summary.json is identical: the 16 gauge-fit intervals, the scalar values and fits, and the precision differences.
  - The exceptions are 19 binary64 matrix-endpoint values that differ in the last digit (NumPy 2-norm version) and the version strings.
- **Other topic code:** c2_rate_checks.py gives 42 identical records, and was extended to N ≤ 12. The c1_error_diagnostic copy (paths changed only) matches its 348 rows to ≤ 5e-16.
- **Independent scripts (moment solves, coefficient matching, finite differences at 70–80 dps, no topic AD):**
  - t2: the parameter lower bound in 56 cases, 8 pairs at N=2..8. κ_N reproduces PD-T434 at N4–8.
  - t3: successive growth just below ρ(p₁,p₂) up to N36 for six pairs.
  - t4: B rows equal b rows exactly under random frozen and input-dependent gauges.
  - t5: exact K₂ by enumerating box vertices for N3–6; matrix inequalities (1)–(3) hold.
  - t6: 352 scalar values match to 8.6e-48, and the median dual equals a HiGHS LP in 400 cases.
  - t7 and t8: the step-line witness and the lower envelope.
- **M1 wording:** the verdict is consistently MEASURED and stated as fits of the unknown infimum, with no exact optimizer or outward certificate claimed.

### 4. C3 weak stability: OPEN target confirmed; grid accepted as MEASURED

- **Reduction, checked by worker D:**
  - The chain rule DF = Q − L M⁻¹H includes the direct terminal-input term Q, the degree-N support successor.
  - Exact `D/c3_rank.py` for N=3..5, both families: d_c = 8, 20, 40 equals rank M; rank H = 6, 10, 13; both mass-scaling directions lie in ker H.
  - The record draws only the limited consequence that follows, and its nearby-input caveat (frozen grid, P_(n,N−n) set to zero) is correct.
  - It makes no constant claim, does not activate M3 and does not assert PARTIAL.
  - PD-T449 is untouched.
- **Grid rerun:** `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python code/c3_grid.py`, the full 58 inputs × 4 methods. Python 3.13.18 / NumPy 2.5.3 here, against 3.12.14 / 2.3.5 for the developer.
  - **Identical:** all C4 values, including Hahn N14 at 40533.1034; Hahn A-LU .469316; the warning counts and first-warning indices; and both N4 exact checks.
  - **Platform-dependent:**
    - Krawtchouk A-LU on κu ≤ 1 is .809084 (N17), against .809315.
    - The full-grid Krawtchouk A-LU maximum is 1.609547 at N21, against 1.132694 at N19.
    - **Krawtchouk N32 A-LU breaks down here** with a singular matrix, so 231 of 232 solves complete (MINOR-3).

### 5. C4 comparison: accepted as MEASURED, with source replay blocked here

- **Finite checks:** c4_normalization.py and c4_lift.py give payloads identical to the committed receipts. Recomputing c4-shared-input.json gives SHA 4a1f4ea5…, matching the source and runtime receipts.
- **Native path of c4_compare.py**, run with a synthetic external file (`D/mkext.py`): hahn-C4.csv is byte-identical and all 28 Krawtchouk C4 rows are identical.
- **Table consistency:**
  - 8 native tables × 29 rows = 232; 6 external tables × 58 rows = 348; 116 configurations.
  - Every row is `ok`, and E_NN equals the maximum of the field errors in every row.
  - The maximum lift disagreement is 1.698e-107. All table hashes match the receipt.
- **Labelling:** external NN errors are labelled as including the H+d0 lift. The decimal-transport records are labelled exploratory and rejected, and no final evidence uses them.
- **Files and provenance:** c4_external.m is the developer's own wrapper. No committed generated file exceeds 16 KiB. No third-party code or data is committed.
- **Not rerun here:** M2, M4 and the 348 external calls. Their PASS rests on the developer's receipts and on the supplementary Codex-side replay in independent-checks-01.

### 6. Evidence

- `python3 code/verify_evidence.py`: PASS, 58 committed identities. No raw artifacts exist in this runtime.

## Findings

### BLOCKING

None.

### MAJOR

**MAJOR-1: PD-T448's classification after the Krawtchouk rate theorem has not been decided, and the split wording is inconsistent.**
- PD-T448's statement asks, for the exact Krawtchouk and Hahn families, to "determine liminf and limsup of kappa_N^(1/N), whether they are equal and finite, and the required subexponential factors", with useful constants and a finite radius. See topics/nn-mop-stability-20261105/theory/conditioning-growth-target.md:11–18.
- Its OPEN status rested on "not a decomposition into solved target cases" (:5–7, :28–33).
- The Krawtchouk liminf = limsup conjunct is now PROVED, and the topic labels it as split from PD-T448:
  - c2-sharp-upper.md:5–7 and :356–357 ("closes the stated fixed-pair case");
  - report.md:21.
- What remains open includes the Krawtchouk subexponential factors (the gap between 5/(2M²) and 3·10⁶N¹³), the constants and radius, and every Hahn conjunct.
- Under WORKFLOW **Split results**, the developer must explicitly propose one of:
  - **PARTIAL**, with the decomposition into conjuncts and cases, the split mapping, the original wording preserved and a dated History entry;
  - **OPEN**, with a reason that addresses the PARTIAL criterion.
- Align "Split from: PD-T448" on the supporting lemmas with that decision (see MINOR-6).
- This is a status decision, so it is material and needs a focused re-audit. Disputes go to AC.

**MAJOR-2: the closest literature for the central gauge question and for the scalar controls is not cited.**
- **LIT-502** (literature/INDEX.md row 574, Faghih–Van Barel–Vandebril, the same group as LIT-348): a diagonal scaling that balances the column norms of W and V keeps about 5 recurrence-residual digits at N=100 for multiple Kravchuk/Hahn MOPs, where the monic unscaled variant loses all digits by N≈20–25.
  - The topic never mentions it; a grep of all topic .md files finds nothing.
  - novelty-gate-C1.md:16–19 searched "diagonal scaling" in IDEAS and predecessor records only.
  - Nothing is contradicted: LIT-502 is about an algorithm's residual under basis scaling, while C1 is about the forward-map condition in the fieldwise metric.
  - But report.md:3 and note-material.md:5 say the exponential "survives fixed and differentiable gauges", in material destined for that group. Without the distinction, a reader would see an apparent contradiction.
- **Fischer 1998** (LIT-113 row 312, with LIT-112 and LIT-365, and IDEA-087/088): node and weight derivatives of the scalar α and β, and a condition number with O(N²) for regular discretizations. This is the closest predecessor of c1-scalar-derivative.md and of the "slow growth" scalar controls (report.md:9, note-material.md:6).
  - c1-scalar-derivative.md:41–45 and novelty-gate-C1.md:63–67 cite neither.
  - The predecessor audit already raised this exact omission (nn-mop-stability-20261105/audit-01.md:321, finding 5).
- **Fix:** a dated C1 gate addendum, attribution lines with LITERATURE qualifiers in c1-scalar-derivative.md, and one distinguishing sentence each in report.md and note-material.md. No claim changes.

**MAJOR-3: the failed C2 upper subroutes lack candidate records, and two evidenced failures have no negative-result home.**
- **Rounds 4–6** carry REJECTED: failed (novelty-gate-C2.md:145–170; attempts/C2.md:38–40 and :140–169). None has a provisional IDEA record per templates/IDEA.md, or is registered as a subform of C2-03. So the envelope PD-N's candidate disposition (c2-hahn-upper-envelope.md:40) attaches to an unnumbered subroute.
- **Rounds 5 and 6** contain proved scoped negatives:
  - the exact positivity counterexample ΔU(0) = −6 at M=3, t=1 (c2-hahn-upper-search.md:46–62);
  - the unweighted differentiation loss ‖D‖∞ ≥ 2^M/[M(M+1)] (:84–104).
- **Missing header:** c2-hahn-upper-search.md has no ID kind and no status header (:1–7).
- **Rules:** WORKFLOW (L5) says an evidenced mechanism failure gets its own PD-N; round 4 got one, rounds 5–6 did not, and no reason is recorded. The predecessor audit treated the analogous omission as MAJOR (its M4).
- **Fix:** add provisional IDEA records, or registered subforms, for rounds 4–6. For rounds 5–6, add either PD-N records with their status and scope, or a written justification that they are minor routine route notes. Add a status header or attempt-record label to c2-hahn-upper-search.md.
- The mathematics is already correctly scoped; this is about the records.

### MINOR

1. **Results file stale.**
   - results/nn-mop-conditioning-20261106.md:4 lists only the Hahn "nonsharp exponential lower base2". It omits:
     - the PROVED terminal rate ρ_H ≈ 12.1136 and the full-map liminf;
     - the gauge-infimum ρ_H corollary (c1-hahn-gauge-lower.md:24–48);
     - the envelope PD-N;
     - the matrix-metric theorem;
     - provisional IDs.
   - LOG.md:182–183 says "Report/results/note material now cite this stronger bound"; only the report and note material do.
   - novelty-gate-C1.md:50–52 and attempts/C1.md:116–118 also describe only the base-2 gauge lower bound.
2. **Hash chain.**
   - c1-error-comparison.json pins c4-comparison-receipt.json as `6795570d…`. The committed receipt, also pinned in evidence-manifest.json, is `92ace13e…`; both enter in commit 505e6cf. Table hashes match, so the payload is unaffected.
   - The raw artifact c1-matrix-all.json (b4e53167…) is pinned in c1-summary.json and c1-error-comparison.json but is missing from the manifest's raw_working_artifacts.
   - Fix: rerun c1_error_diagnostic.py against the final receipt, or record the revision used, and add the raw pin.
3. **C3 platform dependence.**
   - theory/c3-grid-measurements.md:8–10 and :32–37, report.md:29 and the results file state "232 completed" and the attained maxima without qualification.
   - The record does note that results depend on the numerical stack (:79–81).
   - The audit rerun differs as described in section 4, including the breakdown at Krawtchouk N32 A-LU.
   - Fix: state that completion of every solve and the κu > 1 maxima are platform-specific, and record the rerun outcome. The C4 values and Hahn A-LU were stable across platforms.
4. **c4_compare.py crashes on a native breakdown.** code/c4_compare.py:79–80 reads `['coefficients']` without checking status; c3_grid.py:121–124 writes none for a breakdown. Result: `KeyError: 'A-LU'`. Fix: record the status instead.
5. **The M2 replay command does not regenerate the committed bit-exact M2 receipt.**
   - external-code.md:59–60 runs c4_external in `m2` mode. That mode keeps only Krawtchouk N6 (c4_external.m:7).
   - c4-m2-bits-receipt.json covers both families and pins the full-grid output efc7fd… as its input.
   - Fix: document the actual command and the ordering. The pre-grid gate was c4-m2-receipt.json (8.66e-17).
6. **"Split from: PD-T448" appears on supporting lemmas:** c2-hahn-lower.md:5, c2-hahn-terminal-rate.md:5 and c2-krawtchouk-parameter-lower.md:6, while c2-hahn-normality.md says "Split from: none". Use Dependencies, consistent with MAJOR-1.
7. **Stale process text:**
   - c2-sharp-upper.md:38–39 ("independent checking and the required Claude audit are pending") and :337–339 ("requested");
   - attempts/C2-hard.md:24–25;
   - attempts/C2.md:99 ("is rerunning separately");
   - LOG.md:6 ("Claims: none yet");
   - LOG.md:20–22, where Runs needed holds only the setup items. Add the unrun Advanpix experiments and the undelivered cold storage.
   - c4-interface-validation.md:41 still says M2/M4 are BLOCKED above its superseding section.
   - The 1-ulp transport failure is described three ways: report.md:35 ("one node"), c4-measurements.md:25 ("some N12 nodes"), attempts/C4.md:45 ("several").
8. **Durable records without IDs:**
   - c3-weak-stability-open.md:3–6 says "ID kind: PD-T" but has no provisional ID. It states a forward weak-stability target, E ≤ C_N κu + O(u²), that differs from PD-T449's strict and correction/data models, yet calls itself a "PD-T449 continuation". Give it its own OPEN provisional ID with its relation to PD-T449 stated, or label it an attempt record.
   - c4-measurements.md:3 is a distinct MEASURED claim with no ID.
9. **C3 gate coverage limitation undisclosed.**
   - novelty-gate-C3.md:7–11 relied on bounded table-summary views.
   - Its list of tables read omits PR15/17/22/23/25, the cleanup and frontier tables, the nonproduct tables and the unnumbered subroutes.
   - There is no impact, since C3 produced no new mechanism. Disclose it once in LOG, as C1's timing qualification is.
10. **Record hygiene:**
    - *Numbering:* local numbers collide across namespaces. C2-01 names an IDEA candidate (the upper) and a PD-T result (the parameter lower), and C2-02 and C2-03 collide the same way. "PD-T?…-31" is ad hoc. Add a candidate-to-result mapping table before final IDs.
    - *C2-hard script:* the check is embedded only in prose (attempts/C2-hard.md:87–196). Move it to code/ and pin it in the manifest.
    - *IDEA fields:* C1-01 to C1-03 and C3-01 to C3-04 lack literature baseline, applicable obstructions, a pre-test kill criterion and discriminability; C3-02 to C3-04 also lack a verdict.
    - *M1 row:* gates.md's M1 row omits the pre-registered LIT-347-normalized and 1-D monic ratios (handoff 01:90).
11. **Proof clarity.** c2-sharp-upper.md:126–129 and :141–142: add one sentence saying that G cannot use the rectangles because Γ₁ ∋ 0 and Γ₂ ∋ 1 are branch points of ℓ. The proof as written is correct.

### NOTE

1. **The gauge infimum is essentially the b-field condition (worker C, t4).**
   - Under the frozen gauge s_(0,0)=1, s_ν = t^(|ν|−1), the rows of A of degree ≥ 2 shrink by the factor t. As t → 0,
     κ_s → max(κ_b1, κ_b2, rc(a1_(1,0)), rc(a2_(0,1))),
     where rc is the relative condition of the two degree-one entries.
   - The value is attained exactly at Krawtchouk and Hahn N4 and N6; for example Krawtchouk N6 gives 5570.73, against monic 12305.32.
   - So K_dep = K_fix = max(κ_b1, κ_b2) whenever the b fields dominate those two entries.
   - The records are not wrong: they say the infimum "need not be attained" and leave exact minimizers OPEN.
   - Two consequences:
     - the "exact gauge optimizer OPEN" item could likely be closed;
     - the M1 "intrinsic" verdict amounts to gauge invariance of the b fields, while all off-diagonal a-sensitivity is gauge-removable except two scalar entries.

   Stating this explicitly would sharpen the note to AC. It is optional for this round.
2. **Possible classical predecessor for all-N normality.** Multiple Hahn with α₁−α₂ ∉ ℤ and multiple Krawtchouk with distinct p are AT systems; to worker E's background knowledge this is in Arvesú–Coussement–Van Assche 2003. It has no INDEX entry and was not verified. No priority is claimed (c2-hahn-normality.md:54–57). Do a bounded literature check, or add a qualifier, before note-material.md:8 is used externally.
3. **Measured base against proved rate.** The predecessor's finite Hahn fit (about 11.8 for N48–64) and the step-line interval [11.69, 11.77] lie below the proved liminf ρ_H ≈ 12.11. This is consistent, given polynomial prefactors. One sentence in the report would prevent misreading.
4. **Expository gaps in c2-hahn-terminal-rate.md**, each verified:
   - :222–223: the mean tends to ∞ because H′ ~ δ^(−3/2) while H ~ δ^(−1/2);
   - :274–275: "ρ > 12" excludes 1/ρ_H because r < R;
   - :278: positivity bounds, with 2w²−1 > 0.18 and 1−2w³ > 0.07.

   Also, c2-hahn-normality.md:15–16 calls the normalized weights the PD-T290 weights, but PD-T290 uses the unnormalized W. κ is invariant under scaling each weight vector, so one sentence would remove the ambiguity.
5. **Notation and wording:**
   - c1-gauge-invariants.md:37–39 reuses K_dep for the step-line infimum; use K^SL.
   - c2-krawtchouk-parameter-lower.md:231–233 uses the reflection for p₁ > 1/2 implicitly.
   - :239–240 overstates what c2_rate_checks.py checks; the audit's t2/t7 check PD-T437(13) directly.
   - report.md:3 says "differentiable input-dependent polynomial gauges", which could be misread as gauges polynomial in the input.
6. **C4 records:**
   - The CSV header (c4_compare.py:121) does not mark that external E_NN includes the lift.
   - c4-exploratory-receipt.json keeps top-level `M2: PASS`/`M4: PASS` keys next to its hand-added rejected disposition.
   - M2 holds under either reading of handoff 01:97: receipts give returned-H errors below 1e-12 for CORE and REORTH at N6. This is receipt-backed only.
7. **Loose but valid constants** in c2-sharp-upper.md: |ℓ| ≤ 2.944 is used as < 7, and S ≤ 3.65 as < 5. Bounds (5) and (11) are attained at u=c on terminal sites, which matches the PD-T437 lower bound.

## Dispositions and status summary

| Record | Claimed | Audit |
|---|---|---|
| c2-sharp-upper (Krawtchouk upper and limit) | PROVED | accepted |
| c1-gauge-sharp-rate | PROVED | accepted |
| c1-gauge-invariants, c1-scalar-derivative, c1-matrix-metric | PROVED | accepted (MAJOR-2 attribution only) |
| c2-krawtchouk-parameter-lower | PROVED | accepted |
| c2-hahn-normality, c2-hahn-lower, c2-hahn-terminal-rate, c1-hahn-gauge-lower | PROVED | accepted |
| c2-hahn-upper-envelope (PD-N, failed mechanism) | negative statement PROVED; REJECTED: failed | accepted |
| c2-hahn-upper-search | attempt record | label and records needed (MAJOR-3) |
| c1-measurements, c1-error-measurements, c3-grid-measurements, c4-measurements, c4-interface-validation | MEASURED | accepted (MINOR-2, -3, -8) |
| c3-weak-stability-open | OPEN | accepted (MINOR-8 ID) |
| PD-T448 | OPEN, unchanged | classification required (MAJOR-1) |
| PD-T449 | OPEN, unchanged | accepted |
| M0 original / M0a / M1 / M2 / M3 / M4 | UNASSESSABLE / PASS / MEASURED intrinsic / PASS / unactivated / PASS | accepted. M2 and M4 are receipt-backed only in this audit. |

## Remaining uncertainty

- The all-N theorems rest on written analytic arguments, reconstructed by hand. The finite checks corroborate them; they are not premises.
- My numerical checks are exact for small N:
  - Krawtchouk κ_N to N18;
  - Hahn κ_N to N16;
  - the Krawtchouk lemmas to N16;
  - quadrature for formula (8) to N5;
  - floating point at 45–80 dps elsewhere.
- No outward enclosures were made.
- External source execution (M2, M4, the 348 calls, the 1-ulp transport failure) was not rerun here.
- Committed native LU/QR/nodeqr values beyond small N reproduce only on the recorded numerical stack.
- NOTE-2's literature lead is unverified.
- No reservation or readiness check was done, because no final IDs exist and the topic is not at PR stage.

## Required next step

The stage is WORK. Codex answers every MAJOR and MINOR finding in `response-01.md`, under [handoff 03](handoffs/03-response.md). The MAJOR fixes change classification, dispositions and records, so they are material and return the topic to AUDIT for a focused re-audit of those changes only. The MINOR fixes are confirmed by diff. Only AC merges.
