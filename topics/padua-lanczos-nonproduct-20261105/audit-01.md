# Audit 01 — padua-lanczos-nonproduct-20261105 — substantive independent audit

- Auditor: Claude, independent of the Codex developer. Orchestrator and lead auditor: configured `claude-opus-5-5`, xhigh, as handoff 02 specifies. Five independent Claude Opus subagents were each given a disjoint scope:
  - P3: xhigh;
  - P5: xhigh;
  - P4 with P1/P2: high/xhigh;
  - P6 scans with reruns: high;
  - novelty and protocol: high.

  Serving metadata for the subagents is not separately exposed. Opus xhigh was chosen because the batch carries a new all-degree mechanism, negative results and novelty content (WORKFLOW allocation table, adversarial or novel-mechanism row). The lead auditor checked the central P3 proof line by line independently of the subagent.
- Date: 2026-11-06.
- Rules read: `b5d2d5de5395889e98443fc0aa4776982c41617a`. AGENTS.md, WORKFLOW and the role files there are byte-identical to main `be9a831`.
- Audited input: `38237fecb45f672f20a25d9989a90c31f3ff02a6`, against base main `be9a8318150204711d5446d2ea26284cf1ed0819`.
  - The checked-out head `b5d2d5d` differs only in handoff status lines.
  - Every theory file read matches the snapshot hashes recorded in `independent-checks-math.md`.
- Round: 1. No auditor fixes were made: the third-round MINOR-fix exception does not apply.
- Verdict: **WORK, returned to Codex.**
  - No BLOCKING finding.
  - Every PROVED claim in scope was reconstructed and accepted at its stated scope.
  - All consequential computations rerun by the audit agree.
  - Three MAJOR findings need a response before PR. They concern framing, a protocol record and one claim-statement qualifier; none concerns a proof's correctness.

## Scope and read coverage

Handoff 02 items 1–7 were all audited.

**Read in full:**
- AGENTS.md, WORKFLOW and the Claude role file.
- The topic records: handoffs 01–02, LOG, plan, report, gates, rounds, the results file, and every `ideas/`, `attempts/` and `novelty-gate-P*.md` record.
- Every topic `theory/` record.
- The method and notes records: `p6-reflection-methods.md`, scan methods, the FLINT, reflection and speed notes, `COLD_STORAGE.md`, and both supplementary independent-check records.
- **The complete `state/IDEAS.md` (lines 1–1031)**, including every obstruction and disposition table. This read is required because the batch has mechanism, negative and novelty content.

**Read for predecessors:**
- PD-T324 (`l1-01-sheared-U-aggregate-separation.md`), the PD-T136/137 model records, and the PD-T039 record.
- The PROOF_STATUS rows PD-T039/040/324 and PD-N012/062/063/116–118.
- The precedent `gate-timing-response-01.md` from the frontier topic.

`literature/INDEX.md` was read in targeted rows, not exhaustively. The supplementary Astra reviews were read as history; they are not adopted as audit results.

## Independent reruns actually executed

Everything ran in this cloud session: Python 3.13.18, sympy 1.14, python-flint 0.9.0 (FLINT 3), mpmath, g++ 13.3 and libgmp-dev. All outputs went to session scratch, outside Git, and no repository file was changed by a check. These reruns are review evidence. None is a proof premise.

**P3.** The developer committed no P3 code. The auditor wrote its own exact checker: computation in Q(ζ) with the weighted inner product, sha256 `661687fc…09bfe`. It covered n=2,3,4,5 at η ∈ {1/2, −1/3, 9/10}, with η=0 as a control (5 min 56 s). All exact tests pass:
- positivity, marginals and signs;
- every physical moment through degree 2n+2, with the cutoff exact at 2n+1;
- the nonzero rank minor;
- exact Gram–Schmidt for both rules on the reweighted measure, not assuming the U-form, including β=1/2 and the σ formulas;
- the unit normal witness;
- a full sequential projection in dual numbers, which gives exactly 2(4^(n+1)−1)/3 for the BJ witness;
- equality of the projection and the frozen response modulo Π_n;
- the mirror positivity witness.

The η=0 controls fail only the moment and rank tests, as they must. Float64 local maximisation (not certified) gave BJ ≈ 17.6, 127, 1025, 8768 against proved lowers 6.5, 13.0, 26.1, 52.2. It gave mirror ≈ 7.7, 13.4, 28.6, 38.0 against proved uppers of 220 to 3527.

**P4, P1 and P2.**
- The developer's checks were rerun to scratch, and all matched the committed receipts:
  - `p4_weighted_check.py --output`: 370 directions, rows identical;
  - `p4_annulus_check.py`: 8 rows identical;
  - `p4_terminal_check.py`: 22 rows identical;
  - `p1_moment_probe.py`: agrees to 3.4e-16;
  - `p2_disk_probe.py`: report byte-identical, sha256 `6909c27f…`.
- The auditor's own exact ring-grid check covered:
  - counts and hull;
  - an exhaustive affine self-map search, which finds exactly the 8 signed permutations on both D36x9 and D65x9;
  - mod-p ranks 153, 171 and 188;
  - LCDs 49,725 and 585;
  - grid hashes that reproduce the developer's identities.
- Further auditor checks:
  - exact triangle moments, norms and creators;
  - symbolic annulus identities;
  - complex-step finite-capacity checks on 10 cases;
  - 708 impulse tests of the weighted quotient.
- One combined invocation was stopped after about 22 minutes with no output, cause not diagnosed. The per-family reruns completed.

**P5.**
- The developer's checker, `python -I -B code/p5_exact_checks.py --output <scratch>/p5.json`, exits 0 with PASS (1.62 s wall). Its output equals the committed receipt in every field except elapsed time.
- The auditor's own exact cyclotomic code checks m=1..7 (441 moments, 2.3 s, all PASS):
  - cutoff failure patterns;
  - hull vertex counts 3, 5, 6, 6, 6, 6, 6;
  - the exact Gram identity at s=m−1, with exactly one mismatch at s=m;
  - T_m normal to Π_s;
  - the readouts.
- The auditor's own forward-mode Jacobian of the actual normalized algorithm covers m=2..7, every s≤m, BJ and mirror: 54 rows, 1054 s. The float64 brackets are not certified, but:
  - every lower bracket is ≥ √⌈s/2⌉ and every upper bracket is ≤ the claimed upper;
  - the brackets are within 3.3% of each other;
  - κ(m;m) ≤ 5e-14;
  - 20 random admissible rules have floor √2 or √3.
- A 90-digit finite-ε check (ε=1e-30) matches the frozen closed form to 7e-31 relative error.
- An earlier, larger Jacobian run was stopped and its output is unused. The harness errors in the first finite-ε script were the auditor's own and do not indicate a mathematical discrepancy.

**P6.**
- `p6_scan.py --family H24_222 --max-degree 16 --seconds 600` with a fresh work directory: PASS in 30.6 s. The input sha256 matches, and all 8 case digests equal the committed ones, so all 60 rows match in every field except elapsed time.
- D36x9 degrees 2–8, four rules on both paths: PASS in 28.2 s; all 56 endpoint logs fall inside the committed table.
- **Fresh D36x9 degree-16 producers**, all four rules: BJ 266.6 s, mirror 296.7 s, alternating 1091.3 s, pivot 892.8 s, the last two under four-process load. The digests equal the committed producer and checker digests for all 60 rows.
- Reflection checker against the original scalar checker at degree 8: all four rules equal in every field, including Gram count 990 and pivot ties.
- Fresh reflection pivot at degree 16: 1291 s; the digest matches, and the guards match the recorded values.
- The N2 interval slopes were recomputed with the auditor's own exact-Fraction signed OLS over the committed compact tables, cross-checked against all 32 corners. The compact log tables were independently certified with arb at 300 bits (120 entries each). The results equal the committed receipts:

| Family | 8–12 | 12–16 | Verdict |
|---|---|---|---|
| T24 | [0.13737, 1.80236] | [−0.21648, 1.82281] | INCONCLUSIVE |
| H24_222 | [0.05531, 1.53950] | [−0.22020, 1.65120] | INCONCLUSIVE |
| D36x9 | [−0.50785, 1.06105] | [−0.88737, 1.16246] | INCONCLUSIVE |

**Auditor check code.** Committed as code only under [`audit-01-checks/`](audit-01-checks/). Outputs stay in session scratch and are regenerable; they are not committed. sha256 prefixes:

| Check | Files |
|---|---|
| P3 | `p3_audit_check.py` `661687fcdbe8c139` |
| P4/P1/P2 | `rings_check.py` `8f46f895d4997db2`, `exact_checks.py` `0d475fb17fe642a9`, `finite_capacity_check.py` `9ac376f1416e9dd0`, `impulse_check.py` `0c13fc51e249e861` |
| P5 | `exact_cyclo.py` `b9672b2d58131945`, `capacity_num.py` `380a109402fff55f`, `fd_mpmath_v2.py` `fd11937e040c6aa7` |
| P6 | `n2.py` `3aceac3668cd6ad9`, `n2contain.py` `551b4641a3ec0245`, `cmp_rows.py` `e2241d4e9fb03dfe`, `cmp8.py` `48befb5785ba949e` |

**Not executed by this audit:**
- the degree-16 scalar BJ/mirror checkers (about 2000 s each), which are confirmed only through matching producer digests;
- reflection alternating at degree 16;
- any D65x9 case;
- the FLINT paths;
- native T24 scans or log regeneration, which remain inherited.

## Findings

### BLOCKING

None.

### MAJOR

**A1 — P3 headline framing: moment-equivalent to SH_n through degree 2n+1, with an n-dependent mode that the coordinator, not AC, put in scope.**
- Where: `report.md:11-19` and `:211-219`, `gates.md` (N4 row), `theory/p3-03-uniform-capacity-radius.md` (Statement and Scope), and PR body.
- The mathematics is correct (see accepted claims). But μ_(n,η) agrees with the affine-product SH_n on every moment through degree 2n+1. As a result the following are all independent of η, and only the ambient normal projector changes:
  - the Gram matrices;
  - the monic basis, creators, pivots and source scales;
  - the frozen-response map f↦V.

  Non-productness first appears in moments of degree 2n+2, which the degree-n process never uses. The auditor rerun confirms that the row-level mirror bounds are identical at η = 0, 1/2, −1/3 and 9/10.
- The report does say "invisible to polynomial moments through degree 2n+1" (`report.md:32-33`). However, the headline ("the requested existence goal is proved"), the N4 row and the paper-consequence paragraph ("can now say non-affine-product positive measures") do not carry that caveat. So handoff 01's question whether drift is a property of geometry rather than of coordinates is answered only in a moment-invisible sense.
- Separately, handoff 01's P3 reads "with a fixed polynomial or trigonometric φ, or perturb the weights non-multiplicatively". The reading that the weight mode may change with n was a Codex-coordinator decision (`attempts/P3.md:14-16`). It is not recorded in LOG as such, and it is not AC's decision.
- Required:
  - State the moment-equivalence and η-independence in the P3-03 Scope, the report headline, the N4 row, the paper paragraph and the PR body.
  - Record the coordinator's scope reading once, in LOG.
  - Refer it to AC (question Q2 below).

  This wording does not change the theorem statement.

**A2 — The canonical P3 gate-timing disclosure is accurate but incomplete.**
- Where: `LOG.md:60-71` (commit `2ebea9a`).
- The disclosure was written before any P3 file existed. The gate record, `ideas/P3.md` and the P3-01 admission first enter Git together in `6988024`. The disclosure omits:
  - (a) when the proposal was made and what it contained;
  - (b) which required reads were incomplete at that moment;
  - (c) whether the gated candidate (weight formula, η range, target) is identical to the proposal;
  - (d) that "gate completed before admission" rests on the worker's self-report, since both entered Git in one commit.
- The central P3-02 lemma, moment cancellation through degree 2n+1, predates the gate.
- This audit's own post-hoc gate covered the full IDEAS read and synonym searches. It confirms the verdict "variant of IDEA-137/PD-T039 and IDEA-414/PD-T324", with no essentially identical prior entry found. That supports the record but does not substitute for a prospective gate.
- Proposed disposition (auditor's proposal; AC decides): the deviation stands as disclosed, not waived and not cured. Mathematical acceptance is unaffected. The P3 IDEA record should carry a qualifier: "not prospectively gated: candidate and moment-cancellation observation proposed before completing the required reads (`2ebea9a`); gate and admission first committed together (`6988024`); disclosed, not waived, not cured; AC decision <date>".
- Required: complete (a)–(d) in the canonical LOG paragraph, which is the one place this is disclosed, and add the qualifier. Then refer it to AC (Q1).

**A3 — The P1 continuous-triangle chain is stated without its rule.**
- Where: `theory/p1-continuous-creator-probe.md:31-37` and `:132-134`; `ideas/P1.md:192-194` and `:210`.
- The MEASURED identity g_j = 1/binom(2j,j) for a source at (8,0) is stated in a record that compares three rules, without naming a rule. The auditor's recomputation (sympy moments, LDL^T) shows it holds under BJ only; mirror and alternating give (1,0,…,0). The code checks only BJ (`p1_moment_probe.py:153`).
- Required: qualify the statement "under BJ". This changes a recorded claim's statement, so it is a material change; a focused diff re-audit follows.

### MINOR

1. **Ratio threshold.** Bound (3) of P3-03 is below 1 for every n ≤ 17 (0.026 at n=2, 0.038 at n=10, 0.687 at n=17) and first exceeds 1 at n=18 (1.109). At the N4 degrees 2–10 the certificate preserves the inequalities but proves no BJ>mirror ordering. State n ≥ 18 explicitly at `p3-03:204-226` and `report.md:38-43`. Also, η_0=1/2 is one choice: every η_0<1 is certified, and |η|=1 leaves the admitted family (zero weights).
2. **N2 screen not run before the P3/P5 proofs.**
   - Handoff 01 N2 says "For each admitted family … Pass: proceed to a proof attempt", and handoff 01 P6 asked for scans of perturbed SH_n and Padua. Both families went straight to analytic all-degree proofs, and the report lists their scans as UNRUN.
   - The proofs do not depend on a screen, so no claim is affected. But no dated entry records the decision to skip the screen.
   - Add one canonical LOG paragraph and refer it to AC (Q3).
3. **Missing P3 predecessors** in `novelty-gate-P3.md` and `ideas/P3.md`. The verdict is unchanged.
   - PD-N012(a): product supports with non-product weights.
   - IDEA-415's discrete highest-U sign channel. The P3 weight mode is the tensor square of PD-T324's own normal witness.
   - PD-T039 part 2's sign-indicator mechanism. μ_(n,η) is the mixture (1−|η|)·SH_n + 2|η|·(a parity sub-measure).
4. **Missing P5 predecessors:** the P5 gate omits PD-T040(a) and PD-N063.
5. **Chronology wording.**
   - **D65x9 motive:** `report.md:140` says D65x9 was motivated "before observing a high-degree capacity result". D36x9 BJ/mirror/pivot degree-16 producers had completed before the D65 admission (22:33–22:35 UTC). Correct the wording; the N2 thresholds were indeed unchanged.
   - **P2 probe:** LOG calls the P2 0.154 s probe "preregistered", but `attempts/P2.md:31-38` records that its IDEA entry was written after the run. Reconcile the wording.
   - **P1 round 3:** it is called "productive", but it was a literature read only. This is moot because P1 paused.
6. **Dispositions:**
   - `ideas/P3.md` says "retained for scoped development", and its "Actual results" were overwritten without a dated line.
   - D65 (IDEA P2-03) is still "retained for scan"; record it as `deferred`, with a resume condition.
   - "Not pursued" entries at `ideas/P2.md:90` and `novelty-gate-P6.md:36` lack an allowed disposition word.
   - `ideas/P2.md:91` is deferred without a resume condition.
7. **Provisional labels collide across namespaces.**
   - Bare "P4-01" names the PD-T definition, an IDEA and the PD-N annulus record; "P4-04" names the transfer PD-T and an IDEA. In the PD-N file, line 61 ("P4-04 REJECTED: refuted") can be misread as rejecting the transfer theorem.
   - The same pattern occurs at P2-03/P2-04, and P5 labels mix upper and lower case.
   - Use full namespace prefixes and disambiguate them in the crosswalk at preparation.
8. **Split from/into fields disagree** between `nonproduct-definition.md:7-9` and P4-02/03/04 lines 6–7. P4-03 says it was split into P4-04, but P4-04 says it was split from P4-02.
9. **Admission wording.** `nonproduct-definition.md:36-37`, "a positive finite measure on {(i,j)…}", should say positive weight at every node. Read alone it fails (weights only on {0,1}² give an affine product). The Definitions line, the proof and P1-01 already assume full support.
10. **Status structure.** `p2-03-finite-recurrence-probe.md:66` lists an OPEN all-source recursion/rate "part" inside a MEASURED record. That is the parent target; link it rather than listing it as a part.
11. **P6 provenance.**
    - The H24/D36 full16 and benchmark8 receipts record head `6988024`, but their harness hash `cbb3314d` is the `p6_scan.py` first committed in `dbe5c81`. They ran from a dirty tree; the harness is recoverable and results are unaffected.
    - The N0 `original_harness` `18981aa5` is in no commit.
    - Add one disclosure line.
12. **Rounding.** `report.md:162-165` rounds the four-decimal slope intervals to nearest, sometimes inward (for example 0.13737→.1374). No verdict changes; display them outward.
13. **Supplementary replay wording.** `report.md:175-177`: the Astra degree-16 alternating/pivot replay used the same reflection source and binary, so it is a repeatability rerun, not a distinct implementation. Its collector receipt is INCOMPLETE, and alternating has no saved exit code. Say so.
14. **Gates and results.**
    - The `gates.md` N1 row ("all used finite families") omits the D65x9 admission (`p2-04`).
    - The results file omits the PROVED covariance PD-N and the MEASURED P1/P2 probes.
15. **Literature cross-reference.** The P1 literature checkpoint does not cross-reference the existing LIT-292 addendum (Dunkl–Xu Chapter 3, read from an AC-supplied PDF). AC may be able to supply Chapter 5 the same way. The provisional LIT for Xu 2015 is not a duplicate.
16. **Unproved "only D4 symmetry".** `report.md:128-129` and `LOG.md:93-94` say "only D4 symmetry", but `p2-01:40-41` proves only D4 invariance and non-invariance under all rotations. The statement is true: the auditor's exhaustive exact search finds exactly 8 affine self-maps (the signed permutations) on both D36x9 and D65x9. The short proof is that an affine bijection fixes the centroid and the 36 hull vertices on one circle force an orthogonal map, followed by a finite check. Weaken the wording to "D4-invariant, not rotation-invariant". Adding the proof instead would be a material addition and needs a focused re-audit.
17. **P5 checker hygiene.**
    - `code/p5_exact_checks.py:159` hard-codes `lower_capacity_squared=(s+1)//2` next to computed fields; annotate it in a later revision, leaving the frozen receipt unchanged.
    - The P5 receipt and `attempts/P5.md:57` record SymPy only, without the Python version or platform.
18. **Stale text and spacing.**
    - `p4-weighted-normal-quotient.md:106-107` and `attempts/P4.md:93-94` still say "no independent rerun". The Astra rerun exists (`evidence/check-math-reruns.json`), and this audit adds another.
    - Missing spaces: "through2n+1" (`p3-02:58,60`), "n2–10" and "coefficient1" (`p3-03:70,146`), "and0<|eta|<1" (`LOG.md:139`), and similar elsewhere.

### NOTE

1. **Atomless capacity (P4-03, `:157-161`).** The step to a countable dense set uses continuity of a↦K_a (Lipschitz with constant sup‖C‖), and ess sup ≤ max over the support is used too; both are unstated but routine. The claim "ess sup = attained maximum" is correct, by continuity, compact support and positive mass near every support point. Finite atoms are correctly excluded.
2. **Transfer (P4-04 (2)).** "More generally" is loose, since (2) keeps the moment-matching hypothesis. The directions and constants are right (κ within √(a/b)…√(b/a); ratio loss at most b/a), and (3) is correctly one-sided.
3. **Reflection guards.** They are sufficient but partly redundant, so "needed as stated" (`independent-checks-math.md:458`) overstates. The proof, review, code and pilots all first appear in `697863b`, so Git cannot order them; this rests on the coordinator's record.
4. **N2 criteria.**
   - The T24 screen is retrospective, because PD-T338 predates the plan; this is disclosed.
   - The plan's "both upper slopes <0.02" refines the handoff's kill wording. That is immaterial here, since every upper slope is ≥1.06.
   - A single 8–16 window would give positive lowers (0.380 for T24, 0.305 for H24). Only the preregistered both-halves rule yields INCONCLUSIVE, and this audit does not reinterpret it.
5. **Gate legitimacy.**
   - N4 legitimately passes as an analytic certificate under the frozen plan.
   - Handoff 01's body is unchanged, and `gates.md` changes are verdicts only.
   - The following are allowed and recorded:
     - the 600 s → 3600 s resource extension;
     - the reflection method as a new dated variant;
     - the single PD-N, for the covariance obstruction;
     - the round budgets (P1 3, P2 3, P3 2, P4 4, P5 1, P6 6).
   - Each novelty gate was committed together with its first candidate ("before or with"). Ordering within a commit rests on worker self-reports.
6. **Literature.** No theorem is imported from an unread source, and no priority claim is made. A complete read of a 22-page preprint inside a ten-minute window cannot be verified, but nothing depends on it.
7. **Checker hygiene.**
   - The checkers use bare `assert`, which `python -O` would disable; the recorded commands do not use `-O`.
   - `exact_gram_pairs_checked` is a whole-run count repeated on each row.
   - The recovered pivot and the Astra alternating outputs have no saved exit codes. They rest on complete outputs, and this audit's fresh reruns reproduce both scientific outputs.
8. **P5 details.**
   - The developer's checker covers only s=m−1, with derivative directions only at m=2,3; the records state this scope correctly.
   - "Precisely six vertices" (`p5-01:145-147,156`) could use one sentence of justification.
   - "Admissible" at `p5-02:43` should cross-reference PD-T136.
   - The upper bound is loose by more than 11× in the measured range (2√2·s would suffice).
   - All P5 files first appear together in `13c3146`; no P5-specific deviation was found.
9. **Storage (handoff item 7).**
   - Committed JSON and compressed data repository-wide total 5,489,510 bytes in 1,087 files; this topic contributes 661,295 bytes, including 232,786 bytes of inventory chunks. All tracked data-like files, including `.out`/`.log`/`.txt`, total 5,868,931 bytes.
   - **AC decided on 2026-11-06** that storage belongs to a separate cleanup topic and that no cleaning action is taken while everything stays under 10 MB (recorded in [LOG](LOG.md#2026-11-06--claude-audit-01)). The total is under that limit, so this item needs no action here.
   - Every committed file is ≤16 KiB except three prose records (LOG, and the two independent-check records at 28–33 KB). The size limit concerns generated outputs, so these are not an issue.
   - The `/tmp/padua-lanczos-nonproduct-20261105/` raw artifacts that the inventory indexes do not exist in this session. As recorded, retrieval now means regeneration; the audit's reruns show that regeneration reproduces the scientific digests.
   - No prose is hash-pinned; records only link to prose.

## Accepted claims (audit scope)

The following are accepted at their stated scope, after independent reconstruction.

**P3-01, P3-02, P3-03** hold for every n≥2 and real 0<|η|<1. Covered:
- non-affine-productness against all invertible affine maps, by hull rigidity forcing axis-preserving maps plus the nonzero minor 4η·v_k v_k′ v_l v_l′;
- positivity and normalization;
- the exact moment cutoff 2n+1;
- the unit normal witness in the actual reweighted space;
- the frozen-response reduction and monic/source scaling;
- the BJ lower √(2(4^(n+1)−1)/3) and the full-source mirror upper 2√6(n+1)²(N_n−1);
- the quantifiers, and N4 as a sufficient certificate only.

The lead auditor's line-by-line check and the subagent's reconstruction agree.

**P4.** Accepted:
- the definition and admission lemmas;
- the weighted finite quotient and the terminal-block corollary (all-source lower only);
- the atomless capacity identity;
- the transfer theorems;
- the annulus obstruction, PD-N PROVED with the candidate REJECTED: refuted, correctly scoped to absolute degree-two capacity and explicitly not a refutation of the BJ/best ratio criterion.

**P1/P2.** Accepted:
- the triangle admission;
- the D36x9 and D65x9 admissions;
- rotation covariance and the degree-two basis-mixing obstruction (swap coefficients −1/3 and 2√2/3);
- the probes, correctly labelled MEASURED/restricted;
- N3, recorded as a redirect only.

No cubature equivalence between the continuous disk and the ring grids is claimed.

**P5-01 and P5-02** are accepted for all m>s≥1:
- the continuous cutoff 2m−1 is sharp, with (2m,0) the only failure at degree 2m;
- agreement with the discrete Lobatto product holds through degree 2m, first failing at (m,m+1);
- the hull vertex counts are 3, 5 and 6 for m = 1, 2 and ≥3, so no invertible affine image of a product support (a four-vertex rectangle) can match;
- the full-source upper is valid for unrestricted node sources: moments fix only the base coefficients, and the frozen recurrence then acts through diagonal operators with values in [−1,1];
- T_m is a unit normal witness, since m+s ≤ 2m−1;
- the floor κ ≥ 1 for every admissible rule (σ_last ≥ β_last);
- no all-rule upper, sharp exponent, alternating/pivot upper or IEEE claim is made;
- s=m is correctly excluded: there κ=0.

**P6.** Accepted:
- the reflection method's reduction (the 90 representatives share energies only; all 324 nodes and every source are retained, and the seven guards fail closed);
- the coverage as reported;
- per-case source identities at D36 degree 16 (producer `41c11190`, scalar BJ/mirror `58480a86`, reflection alternating/pivot `09d524f9`);
- that no FLINT or speed variant appears at degree 16;
- incomplete, cancelled and timeout receipts committed once and never relabelled;
- the three INCONCLUSIVE N2 verdicts.

## Questions for AC (after the response)

- **Q1.** P3 gate timing: accept the disclosed deviation with the A2 qualifier, or require further remediation?
- **Q2.** P3 scope: the family is non-affine-product but moment-equivalent to SH_n through degree 2n+1, with a weight mode that changes with n, put in scope by the Codex coordinator. Does this satisfy the P3/N4 and topic intent? Or should the fixed-φ / fixed-density route remain the stated target, with this result reported as a weaker variant?
- **Q3.** Accept that the P3 and P5 proofs went ahead without the N2 screen, and that the perturbed-SH and Padua bulk scans requested in handoff 01 P6 remain unrun?

## Remaining uncertainty

- The P3 finite checks cover n=2..5 and three nonzero η values; the all-degree claims rest on the analytic reconstruction.
- The capacity maximisations are float lower estimates and are not certified.
- The degree-16 scalar BJ/mirror checkers and reflection alternating were not rerun; their values are confirmed through producer digests and committed artifacts.
- Ordering within commits rests on self-reports, and no worker transcripts exist.
- `literature/INDEX.md` was not read exhaustively.

Only AC merges.
