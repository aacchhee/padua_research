# Audit 01 — padua-3d-20261106 — substantive independent audit

- Auditor: **Claude, Opus 5.5 (`claude-opus-5-5`), xhigh**. This is the independent Claude audit of Codex development that handoff 02 asks for. It is the batch's single substantive audit (round 1).
- Depth chosen: Opus 5.5 xhigh throughout. The batch has novel mechanisms, negative claims and two computer-assisted PROVED upgrades, which calls for adversarial mathematical audit.
- Orchestration: the orchestrator (this session) ran the producer reruns and receipt comparison and wrote this report. Five independent Opus 5.5 xhigh subagents of the auditor each reconstructed one scope. Their full reports are appendices: [T1](audit-01/T1.md), [T2/T3](audit-01/T2-T3.md), [T4](audit-01/T4.md), [T5/T6](audit-01/T5-T6.md) and [novelty, records and literature](audit-01/novelty-records.md). No subagent changed Git state.
- Rules read at `d0e1bbb267db9928de97538d9b524fb0068538cd`: AGENTS.md, agents/WORKFLOW.md, agents/claude/CLAUDE_ROLES.md.
- Audited candidate: **`f1a5b0936d8fb2b033c69af59a6366550f170999`**. The handoff-publishing head `d0e1bbb` differs from it only in `handoffs/01-work.md` and `handoffs/02-audit.md`, checked with `git diff --stat`.
- Base: main `76ba4214b100c86a44941f5e9a662ce9ce48efb8`, still the current `origin/main` when fetched on 2026-11-06.
- Date: 2026-11-06.

## Verdict

**Mathematics: accepted.** Every PROVED, MEASURED and OPEN status claimed in the batch is supported.
- This includes the two material upgrades this round had to audit: the normalized cubic obstruction (`theory/t2-normalized-screen.md`) and the full unshifted modulus-39 extension (`theory/t3-degree3-extension.md`).
- No BLOCKING finding.

**Records and gates: not yet ready for PR.**
- Five MAJOR findings concern novelty-gate coverage, candidate retention and dispositions, one overstated gate verdict and one ID kind.
- None of them changes a theorem, but each must be fixed before PR.
- **Stage returns to WORK** for a Codex development response (handoff 03).
- Only the material changes made in response get a focused re-audit. No new whole-batch round is needed.

## Coverage read

| Area | Coverage |
|---|---|
| Rules | AGENTS.md, agents/WORKFLOW.md, agents/claude/CLAUDE_ROLES.md, templates/HANDOFF.md; THEORY and IDEA templates (subagent). |
| Registry | `state/IDEAS.md` read **in full** (1,112 lines, every obstruction and disposition table) by the novelty subagent. `literature/INDEX.md`: the 3-D-relevant rows (Padua, Lissajous/Chebyshev lattices, 3-D cubature, Lebesgue lower bounds, Subbotin, DEKL, DMVX, Xu, Möller, Leja), plus targeted greps. |
| Topic | LOG, BRIEF, plan, report, rounds, gates, all three preregistrations, all `attempts/T*.md`, all `novelty-gate-T*.md`, `literature-3d.md` and `literature-T1..T6.md`, both supplementary-check records, both handoffs, cold-storage files, evidence manifest, results file, PR #33 body. |
| Theory | All 21 `theory/*.md` files were read in full by the scope subagent that owns them. The novelty subagent read 6 in full and the headers and status sections of the rest. |
| Code | Every producer script was read by the scope subagent that owns it. |
| Primary sources | DEKL arXiv 1608.03451v2, eq. (3.15), was fetched and checked. Subbotin's text could not be retrieved: the proxy blocked mathnet.ru and geodesic.mathdoc.fr. See finding m6. |

## Independent executions (actually run)

Commands, hashes and outputs are in [audit-01/receipts.txt](audit-01/receipts.txt); the audit code is in [audit-01/code/](audit-01/code/). Environment:
- Python 3.13.18 (the receipts used 3.12.14);
- numpy 2.3.5, scipy 1.17.0, sympy 1.14.0, mpmath 1.3.0;
- `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1`.

1. **Integrity before reruns.** In a detached worktree of `f1a5b09`, `artifact_manifest.py --verify` returned PASS: 31 artifacts, 177,823 bytes.
2. **Producer reruns.** All 11 commands from handoff 02 were run in that same worktree, and all exited 0.
   - The receipt comparison (`audit-01/code/receipt_compare.py`) flattens each JSON and compares field by field. Every scientific field is identical, floating-point values included. Only the Python version, platform and elapsed time differ.
   - The T2 screen receipt's `preregistration_sha256` is `3c479089…` (the current appended file) rather than the historical `127337d2…`. This is the known provenance NOTE.
   - The `t1`, `t5-exact`, `t5-support` and `t6-sanity` outputs and the cover and T3 printouts match the committed receipts.
   - `t4_stacks.py --max-degree 12` stopped at n=7 under the D2 kill, with no n≥8 rows.
3. **Independent exact H39 checker** (`claude_t23_check.py`, sha256 `ed46fec0…`). It is written from scratch and imports no repository code.
   - It reduces each of the 171 witnesses in Z[t]/(t³⁹−1) and, separately, evaluates every node in Z[t]/Φ₃₉(t).
   - It also checks the hand reduction end to end over **all 59,319 residue triples mod 39**.
   - Result: ALL ASSERTIONS PASSED. A mutation test caught 15/15 corrupted witnesses and the coverage mutation.
   - The method differs from both the producer checker and the Astra Fraction-convolution checker.
4. **T1.**
   - A brute-force check over every subgroup of (Z/M)³ with |H|≤160 (M ≤ 24) matched the classification counts with zero mismatches.
   - An exact rank test found every target-size invariant coset rank-deficient at n=2 and n=3.
   - A full-cap formula enumeration (m_j ≤ 2N) at n=2..6 found 0 survivors. Rerun by the orchestrator; see receipts.
5. **T4.**
   - High-precision lower-bound quantity: 0.0974 at n=7, 0.1817 at n=2048. Extrapolated 0.18269076 against 3ζ(3)/(2π²) = 0.18269074.
   - The determinant ratio is invariant over all permutations for n ≤ 4 (50 digits).
   - At 400 digits, exact-greedy and floating Leja orders agree for n ≤ 40.
   - Mesh values were reproduced, and the losses persist on a 41³ mesh.
6. **T5/T6.**
   - Exact 56×27 moment matrix on the actual nodes: rank 26, kernel ∝ ∏T₂.
   - Supports are 19, 21, 26 and 15 at t = −8, −2, 1, 4.
   - The 14-node control rule is exact through degree 5 and fails at degree 6.
   - A genuine projection-multiplier test (10-point real projection, all k ∈ [−4,4]³, error 3.5e−16), unlike the producer's tautological check (m8).
   - ‖D_n³‖₁ exceeds the lemma's bound by a factor of 400–2500.
7. **T1 NOTE example verified by the orchestrator.** H = {(i,j,i+j)/4} with a = 0 gives 10 distinct points in {−1,0,1}³ that are Π₂-unisolvent (|det| = 256). It is not reflection-invariant.

## Claim-by-claim result

| Provisional record | Claimed status | Audit |
|---|---|---|
| PD-T?…T1-01 reflection classification | PROVED | Accepted. Every step was re-derived and brute-force matched. |
| PD-N?…T1-01 minimal obstruction, n≥2 | PROVED (negative); disposition REJECTED: failed within class | Accepted. Node inequalities, 2-D Padua escape (only (±2n,0) annihilators) and the n=1 exception (det 8) were re-derived. Wording: m1. |
| T1 original C_k target | OPEN | Accepted as OPEN, not PARTIAL. Wording history: m2. |
| PD-T?…T3-01 cyclic rank reduction / folded dictionary | PROVED | Accepted. 260 entries were checked exactly, with sign orbits and zero-index multiplicities preserved. |
| PD-N?…T3-01 short compatible relations | PROVED | Mathematics accepted. ID kind: MAJOR M5. |
| PD-N?…T2-01 three quadratic falsifiers | PROVED | Accepted, exactly at all 19 nodes. |
| PD-N?…T2-02 normalized cubic obstruction | **PROVED (upgraded)** | **Accepted.** There is a proved reduction to a finite check, exact arithmetic, committed checker and evidence, and an independent rerun with a third, different method. |
| PD-N?…T3-02 full unshifted modulus-39 extension | **PROVED (upgraded)** | **Accepted.** The hand reduction covers any unit position, negations, repeated, zero and non-primitive coordinates, and the no-unit case (≤14 nodes). It was verified end to end on all 59,319 triples. |
| T2 rank distributions, survivor quality | MEASURED | Accepted as MEASURED. Survivor equivalence: m3. |
| PD-T?…T4 stack unisolvence, Newton recursion, determinant | PROVED | Accepted. |
| PD-N?…T4-01 monotone exponential lower bound | PROVED | Accepted. The comparison is valid: V(Y) = L·V(X) plus Hadamard gives D(σ)/D(π) ≤ Λ^N, and the mean is used only as a lower bound for the max. The singular Riemann sum and the constant were re-derived and numerically confirmed. |
| T4 upper majorant, exact-greedy exp(O(n log n)) | PROVED | Accepted. The floating tie tolerance is not a premise. |
| PD-N?…T4-02 M/A/L screens, n7 stop | MEASURED | Accepted. It matches the preregistered kill rule. |
| T4 quality target, other orderings | OPEN | Accepted. |
| PD-N?…T5-03 fixed Gaussian-grid support 21/15 | PROVED | Accepted. Labelling: m11. |
| T5 commutator-rank formulas | PROVED (known mechanism) | Accepted. No completion conclusion is drawn. |
| T5 14-node control | existence control | Accepted. It is probably a classical Stroud-type 2d+2^d formula, and the attribution gap is disclosed. |
| PD-T?…T6-01/02 universal comparison and Fourier bound | PROVED, no novelty | Mathematics accepted; 648 = 27·24, and the norm ≤ 27 is proven. Wording: m6, m7. |

## Findings

### BLOCKING

None.

### MAJOR (must be fixed before PR; record and gate changes, no theorem changes expected)

- **M1. Missed predecessors in the T1 and T5 novelty gates** ([novelty A1, A2](audit-01/novelty-records.md)).
  - **T1.** The gates omit De Marchi–Vianello–Xu 2009 (LIT-322/306). Its parity-subgrid node set is the cosine image of an all-parities-equal reflection-invariant subgroup, so it lies inside the T1 class. Its "not interpolation, too many nodes" remark is the nearest published statement of T1's conclusion. It appears only in BRIEF.md:35.
  - **T1 cubature conjunct.** Also omitted: LIT-374, IDEA-109 and OBST?bivariate-lanczos-claude-11 (Xu 1994, d=3), and LIT-381.
  - **T5.** `novelty-gate-T5.md` is a table without template fields (verdict, falsifier, disposition reasons). It misses IDEA-044, IDEA-108, IDEA-109, LIT-374, LIT-327, Noskov–Schmid and Hirao–Sawa (X7 note).
  - **D4 control.** The 16-node "same-parity Lobatto union" in `theory/t5-validation-and-measurements.md` is DMVX's construction and is unattributed.
  - **Required.** Log the shortlist and the differences in the gate and literature files, and fill the closest-entry fields. `report.md:163-165` proposes T1 for a structural note, so this comparison is a prerequisite for that proposal.
- **M2. Candidate retention and dispositions for items assigned in handoff 01** ([novelty A3](audit-01/novelty-records.md)).
  - (a) **T2(a), Lissajous–Chebyshev alias-equivalence** (handoff 01:57). It has no record and no disposition. Unshifted Dencker–Erb nodes are probably settled by PD-N?…T1-01 for n≥2. Verify that and record it, or record the item as deferred with a resume condition.
  - (b) **T5 commuting-completion probe** (handoff 01:82, n≤4). It was not executed and has no IDEA record, resume condition or LOG deviation entry, yet `rounds.md:44` says its resumption condition is recorded. Either run the small probe or record the deferral in the LOG for AC, with reason and resume condition.
  - (c) **Deferred without a resume condition:** the Haar-lattice packing lead (T1), the Lobatto m4/m5 probes and T5-04, and T4-03.
  - (d) **Not in IDEA-template form:** the T2 phase-shifted, even-degree/omit-n3, coset-union and mod-6 routes. Add IDEA-182/PD-N034 to the coset-union entry's closest entries.
  - (e) **Not recorded as not launched:** T2(b) and T2(c).
  - (f) **Stale status:** IDEA?…T2-01 still reads "active prerecord".
- **M3. T2 gate-coverage deviation** ([novelty A4](audit-01/novelty-records.md), [T2/T3 MINOR-4](audit-01/T2-T3.md)).
  - `novelty-gate-T2.md:5` claims a full scan "including obstruction and disposition tables". `attempts/T2.md:59-61` concedes that full-content pre-run compliance is not claimed.
  - **Audit disposition:** accepted as a disclosed timing deviation that later reading cannot cure. This audit's full `state/IDEAS.md` read finds nothing that changes T2-01's verdict; T2 claims no novelty and its proofs are self-contained. It did find IDEA-182/PD-N034 missing for the deferred union route (M2d).
  - **Required:**
    - qualify the gate line;
    - add one canonical LOG disclosure;
    - carry a permanent timing qualifier into the eventual IDEA registration, following the IDEA-576 precedent;
    - list it in the PR for AC's acceptance.
- **M4. The D3(b) verdict is overstated** ([T1 MINOR-2](audit-01/T1.md)).
  - Handoff 01:104 requires exhaustive exact enumeration within the class wherever it is finite.
  - The run capped coordinate orders at m_j ≤ 12, which covers only part of the finite class. Target-size cosets covered against the full class: n=2, 480 of 636; n=3, 708/1392; n=4, 172/757; n=5, 162/2520; n=6, 318/4803.
  - `gates.md` and `report.md` say "PASS for the stated bounded class". That does not meet the gate as written.
  - The scientific risk is nil: the result is hand-proved, and the auditor's full-cap enumeration found 0 survivors.
  - **Required:** run a developer full-class enumeration at n=2..(feasible) with committed code, or relabel D3(b) as partially met and refer it to AC.
- **M5. The ID kind of PD-N?…T3-01 (short relations)** ([novelty A5](audit-01/novelty-records.md)).
  - Its disposition rejects no candidate (`t3-short-relations.md:51-53`), and its "attempted mechanism" IDEA?…T3-02 is post hoc (`:57-58`).
  - The L5 rule (WORKFLOW, candidate dispositions) reserves PD-N for refuted or failed mechanisms.
  - **Required:** reclassify it as PD-T, or name a genuinely proposed and failed mechanism, before final IDs. Disputes go to AC.

### MINOR (wording and record hygiene; fixing them does not by itself need re-audit)

- **m1.** The T1 hypothesis reads "any single/one coordinate" (`t1-minimal-obstruction.md:11`, `report.md:19`), which can be read as "for some coordinate". Say "invariant under each of R₁, R₂, R₃", as the proof uses.
- **m2.** `t1-open-class.md:14-15` rewords the original C_k target. Quote it verbatim with the reason, as WORKFLOW requires. The reason: read existentially, condition (i) is empty, because Gram–Schmidt orthogonalizes against any positive weights. Also record the auditor's non-invariant 10-point Π₂ example there, which shows the reflection hypothesis cannot be dropped.
- **m3.** Survivor node-set equivalences.
  - (1,15,19) ≡ (1,21,29) and (1,11,15) ≡ (1,25,30) at n=4 (inverse of a non-first unit coordinate plus an axis permutation). Likewise (1,3,7) ≡ (1,4,6) ≡ (1,5,8) at n=2. Confirmed by the orchestrator.
  - Their Lebesgue values are therefore exactly equal; the 5e−13 gap is rounding.
  - `t2-finite-survivors.md:75,83` and `report.md:111-112` deny a tie and pick (1,21,29). The preregistered lexicographic tie rule (`preregistration-T2.md`, round 2b) gives (1,15,19).
  - Record the symmetry classes (36/171/561 pairs = 18/100/301 classes) as MEASURED.
- **m4.** The T2 scope wording "even-degree subsequences remain OPEN" should be "any degree sequence omitting n=3, including odd n≥5". Locations: `t2-normalized-screen.md:19-20,56`, `report.md:96-97`, `t2-finite-survivors.md:83`.
- **m5.** Stale "audit/replay/rerun pending", "planned, no run claimed" and hard-coded PENDING text, made stale by the Astra and Claude reruns. Examples:
  - `t2-cyclic-screen.md:168`, `t2-cyclic-dictionary.md:17,37`, `t2-finite-survivors.md:56`;
  - `t4-stack-unisolvence.md:64-66`;
  - `t1_reflection_enum.py`'s hard-coded `independent_rerun: PENDING` and PASS/0 output (lines 216-219; the asserts are skipped under `python -O`; the committed receipt is valid);
  - `rounds.md`'s "Current action" column, and its T6 round count against `attempts/T6.md`;
  - about 30 further lines listed in [novelty B1](audit-01/novelty-records.md).

  Use dated addenda.
- **m6.** T6 attribution wording. `report.md:66-68`, `report.md:151` ("verified in primary literature") and `:159` ("E6 confirmed") state Subbotin attribution as established fact.
  - It rests on one recorded developer read (`literature-T6.md:56-72`; Corollary 3 depends on an unread Yudin bound).
  - The Astra check did not verify it, and this audit could not open the text.
  - Add a qualifier, and turn T6-01's verdict "variant" into "literature duplicate, retained as local reproof".
  - Also note: the Russian original is from 1982; Subbotin has no LIT entry and DEKL is only in the aggregate LIT-380. Reconcile at PR preparation.
- **m7.** State that H³/(648π³) > 1 only for n ≳ 7.2×10¹¹, so at practical n the bound gives Λ ≥ 1 (`report.md:59-62`, `t6-universal-lower-bound.md:26-34`).
- **m8.** The multiplier checks at `t6_sanity.py:38-39` and `:104-115` are tautological. `attempts/T6.md:186-187` and `novelty-gate-T6.md:68-70` overstate the decisive test. Correct the wording, or adopt a genuine test such as `audit-01/code/aud_t6.py`. The proof is analytic, so no status changes.
- **m9.** Split and field misuse.
  - "Split from/into" is used for BRIEF expectations or dependencies (`t4-quality-target.md:4` and others).
  - An OPEN row sits inside a PROVED file's status table.
  - PD-N "attempted mechanism" fields name the IDEA that succeeded (novelty B5, B6).
  - `attempts/T4.md:145` puts REJECTED: refuted on the retained T4-04 row instead of T4-02 / BRIEF E2.
- **m10.** Equal ID suffixes mean different things across namespaces (e.g. T4-03, T5-04). The T5 theory file labelled T5-03 holds candidate T5-05's result. Resolve in the crosswalk at PR preparation.
- **m11.** `plan.md` and the LOG attribute the Astra-high coordinator choice to AC. AC's quoted words only allow Astra Ultra; the choice came from Claude's handoff 01.
- **m12.** `literature-T1.md:21` uses session tool tokens (turn…view0) instead of durable locators.
- **m13.** The T4 node arrays in `/tmp/padua-3d-20261106/` are missing from the COLD_STORAGE inventory. Record them as regenerate-only.
- **m14.** `novelty-gate-T6.md:97` gives det = 4; it is −4. The "novelty unresolved" lines at `novelty-gate-T6.md:75` and `t6-fourier-lower-bound.md:69-70` are superseded later in the same files.
- **m15.** Minor missed predecessors: IDEA-047, LIT-302, LIT-378 and LIT-382 for T4; LIT-391 for T6.

### NOTE

- **Preregistration timing.** `preregistration-T2/T4/T5.md` first reached Git in commit `5690e78`, together with outputs; only `gates.md`/`plan.md` (`a0bc443`) preceded every run. Pre-run timing is attested by the developer's statements and, for T2, by the receipt's historical prose hash. T4's code and receipt hashes match its preregistration. Commit order is not execution order. Disclosed here once.
- **Budget.** Each direction used 1–2 of its 25 (T5/T6: 8) rounds, and no stop rule fired for T1–T3. Stopping was the coordinator's judgement and should be put to AC in the PR as a decision.
- The H39 text says "all 20 rows"; the checker actually verifies all 39 unfolded coefficients, which is stronger. Triples with no unit coordinate have ≤14 nodes. "Order-39" in titles means modulus 39.
- The Astra supplementary H39 checker used the same Fraction-convolution method as the producer; this audit's checker uses a third, different one.
- The proved monotone rate of 0.183 per degree is far below the measured ≈1.84 per degree at n=6→7. No sharpness is claimed.
- The alternating-order mean bound is ≈0.089 per degree at n=800 (MEASURED by the auditor). It supports keeping that exponent deferred until a written proof exists.
- `t4_stacks.py:195-201` does not reset the loss counter when a value is suppressed; this was not triggered.
- The 2-D specialization of the T1 method is sharp: for n ≤ 12 only the four Padua variants pass.
- At PR preparation, IDEA-120, IDEA-013 and IDEA-029 (the old "3-D out of scope" entries) need dated addenda, not rewrites. ID_CROSSWALK mappings are due then as well.
- The statements about E1–E6 in `report.md` are accurate and properly scoped.

## Residual uncertainty

- Subbotin's text was not independently read (proxy block); the attribution rests on the developer's recorded read (m6).
- Historical novelty of the T1 and T4 theorems is not established. The targeted fulltext comparison (M1) is still owed before any structural-note claim.
- Subagent-scope results were reconstructed independently by each subagent. The orchestrator itself reran the producers, the H39 checker, the mutation test and the T1 full-cap enumeration, and checked the m3 equivalences and the NOTE example.

## Required response

Codex answers every MAJOR and MINOR item in `response-01.md` with a fix, an evidence-based rejection or an explicit unresolved item. A focused re-audit then covers only the material changes: M1–M5 and any changed disposition, gate verdict or ID kind. Pure MINOR fixes go to the readiness diff.
