# Audit 02 Part A — focused re-audit of response-01 (padua-3d-20261106)

- Auditor: Claude Opus 5.5 (`claude-opus-5-5`), xhigh; independent subagent, read-only (no Git state or repository file changed).
- Candidate `e80e000f2ba439ea62c966d255ef1b900b608b27` (head `e14ac15` adds only handoff05/status). Diff base `e5b64450fce42262dafc88ee357b72e5f203916b`.
- Read: handoffs 03/04A/05, audit-01 + novelty appendix, WORKFLOW sections, IDEA/THEORY templates, response-01, deviations, four candidates files, independent-checks-response-t8 (Part A), PR #33 body, and all e5b6445→e80e000 diffs of pre-existing T1–T6 theory/gate/literature/attempt files plus gates, rounds, plan, report, LOG, cold storage, manifest code, results; new code/receipts in full.
- Novelty scope: focused; full `state/IDEAS.md` not re-read. Spot-checked that all cited IDs exist with the stated content (IDEA-013/029/044/047/108/109/120/178/181/182/185/187/188/189/207/576; PD-N032/034/037; PD-T004/060/081/097).

## Verdict

**No BLOCKING or MAJOR findings.** All M1–M5 and m1–m15 are answered as response-01 claims. The AC-administrative items (M3 timing, unexecuted T5 probe, unused budgets) are disclosed and correctly left for AC. New issues: five MINOR, five NOTE.

## (1) No accepted T1–T6 theorem changed

A scripted comparison of all `## Statement` sections and `Overall status`/`ID kind` lines across all 21 pre-existing theory files shows no `Overall status` changed and no proof text changed. The only removed lines are those listed here; everything else is appended dated addenda. Complete list of statement/status-adjacent changes:
1. `t1-minimal-obstruction.md:11` Statement: "negation of any single torus coordinate" → "each coordinate negation R_1, R_2, R_3" (m1). This is a clarification matching the proof, the Assumptions ("full coordinate-reflection invariance") and audit-01's accepted reading; no content change.
2. `t3-short-relations.md:1-3,~55`: ID PD-N?…T3-01 → PD-T?…T3-02, kind PD-T, post hoc attempted-mechanism line removed (M5). Statement, proof, assumptions and PROVED status unchanged.
3. Split-field corrections (m9): t2-normalized-screen:3, t4-monotone-lower:3-5, t4-quality-target:3-7, t6-fourier:4-5, t6-universal:5-10. In t6-universal, the unrelated OPEN row moved out of the PROVED table.
4. Non-theory verdict/disposition changes, all listed by response-01 as material: D3 verdict (`gates.md:63,109`); T6-01 verdict to "literature duplicate, retained as local reproof"; attempts/T4 T4-02/T4-04 rows; T2-01 final disposition; n4 selected representative (1,21,29)→(1,15,19).
5. New MEASURED content only: symmetry classes; full-class D3 census; Newton-vs-direct ≤7.51e−14 (verified: max 7.505e−14 in `evidence/t4-mesh-M.json`).

## MAJOR findings M1–M5

- **M1 — fixed, no novelty asserted.**
  - novelty-gate-T1/literature-T1 M1 addenda. DMVX lies in class B=span(110,101); I verified membership (all-equal parity is closed under addition and negation).
  - novelty-gate-T5 addendum table, literature-T5 addendum; D4 attribution in the t5-validation addendum.
  - Coverage limits retained (Noskov–Schmid/Hirao–Sawa unread).
- **M2 — fixed; hygiene MINOR N1.**
  - `candidates-response-01.md` covers T2-a, phase, omit-n3, T2-02 (IDEA-182/PD-N034 at :66; T2(b) not launched :73) and T2-c (not launched :91).
  - `candidates-deferred-response-01.md` covers Haar, T5-completion, Lobatto m4/m5, T5-04 and T4-03.
  - T2-01 final disposition: `novelty-gate-T2.md:48-55`.
  - Each record has scope, mechanism, closest entries, falsifier, verdict, test/kill, results, disposition, reason and a specific resume condition.
  - T2(a): class membership is valid; the broader rank-one part is deferred to T8.
  - The T5 probe's non-execution is disclosed in `response-deviations-01.md:17-25`, the LOG link (`LOG.md:212`) and the PR body, with a resume condition. `rounds.md:44` keeps a dated in-file correction.
- **M3 — fixed; AC acceptance unresolved-disclosed.**
  - Gate qualified at `novelty-gate-T2.md:5`; canonical record `response-deviations-01.md:6-15`, linked from the LOG.
  - The permanent qualifier lives at `candidates-response-01.md:96-98`, following IDEA-576.
  - The PR #33 body's last paragraph names the T2 timing, the T5 probe and the budgets, with a link.
  - The disclose-once rule is met (LOG plus one named record). The gate (`novelty-gate-T2.md:39-46`) and attempts/T2 (`:31-42`) restate it in more than one line; the gate's restatement is its own coverage qualification and acceptable. Pointer inconsistency: N4.
- **M4 — fixed; independently reproduced** (section 3 below).
- **M5 — fixed; residual MINOR N3.**
  - Mapping recorded: `t3-short-relations.md:145-153` (no second allocation), `response-01.md:112-120`, `attempts/T3.md:85,120-123`, `report.md:214`.
  - No current record cites short relations as a PD-N, except the historical round text at `attempts/T3.md:98-99`, covered by the in-file addendum.
  - t3-degree3-extension keeps PD-N?…T3-02; T7 cites the file, not the ID.

## MINOR findings m1–m15

| ID | Verdict | Evidence / comment |
|---|---|---|
| m1 | fixed | Theory statement. The report addendum (`report.md:186`) supersedes historical :19-20. |
| m2 | fixed | t1-open-class m2 addendum. The verbatim quote matches `handoffs/01-work.md:42-46`; it adds the Gram–Schmidt vacuity and the 10-node example, labelled as audit evidence. |
| m3 | fixed, reproduced | `t2-finite-survivors.md:54-78`; see section 4. |
| m4 | fixed | t2-normalized m4 addendum, t2-finite-survivors:79-81, report addendum, omit-n3 record. |
| m5 | fixed | Addenda in all 21 theory files (counted); rounds table updated (T6 = 2); old producer's `-O` hazard documented; new producers use RuntimeError, not assert. Side effect: N2. |
| m6 | fixed; source unresolved-disclosed | `novelty-gate-T6.md:66-68`; T6 literature, theory and attempt addenda (1982/1983; Yudin unread; no second verification). |
| m7 | fixed | Re-derived: (648π³)^{1/3}≈27.19 ⇒ n≈7.2×10¹¹. |
| m8 | fixed (wording) | Producer test called tautological; audit evidence cited; no new run claimed. |
| m9 | fixed | Split fields; candidates-rejected file; t1/t4/t5 attempted-mechanism addenda; `attempts/T4.md:143,145`. |
| m10 | unresolved-disclosed | Deferred to PR-preparation crosswalk, as audit-01 allowed. M5 adds another collision (N3). |
| m11 | fixed | `plan.md:3-5`; `response-deviations-01.md:26-29`. See N5. |
| m12 | fixed | No `turn…view…` tokens remain. |
| m13 | fixed | `COLD_STORAGE.md` and `cold-storage.json` regenerate-only entry; generator sha 0cd23793… equals the current t4_stacks.py; no invented hash. |
| m14 | fixed | det −4 (`novelty-gate-T6.md:98`); t6-fourier addendum. |
| m15 | fixed | T4/T6 gate and literature addenda. |

## (3) M4 full-class enumeration

- **Cap argument: valid.** Every axis projection of X contains all of its levels:
  - active axis: B is unit-free, so B^⊥ hits both parities, and each parity reaches all q+1 Lobatto levels;
  - inactive axis: the full grid appears.
  - Hence |X|=N forces m=2q≤2N−2 on active axes and m≤2N on inactive ones (either half phase).
- **Producer logic matches the classification.**
  - It excludes unit vectors and requires even m on active axes.
  - It uses e(q)=⌊q/2⌋+1, o(q)=⌈q/2⌉, and inactive counts ⌊m/2⌋+1, m/2, (m+1)/2.
  - It partitions cases short → alias → survivor and raises on survivors; int64 is safe.
- **Independent check** (`indep_t1_points.py`, mine; imports no repository code).
  - It builds every canonical coset from the classification statement: 6 labelled unit-free codes, syndrome constraints, inactive half phases, all m∈[1,2N]³.
  - It prunes |H|>8N, which is proved: each node has ≤8 torus preimages.
  - It folds actual torus points exactly in integers (r↦min(r,2m−r)) and counts distinct nodes.
  - Every per-code count equals the receipt. Short/alias splits: 624/12, 1380/12, 756/1, 2520/0, 4800/3.

| n | N | cap | target-count | survivors |
|---|---|---|---|---|
|2|10|20|636|0|
|3|20|40|1392|0|
|4|35|70|757|0|
|5|56|112|2520|0|
|6|84|168|4803|0|

- My code also reproduces the cap-12 counts 480/708/172/162/318.
- Raising the cap above 2N (32 at n=2, 48 at n=3) adds no target cases.
- `gates.md:109` "D3(b) PASS" is supported as a finite diagnostic only; no rank computation or all-n claim is made.

## (4) m3 survivor classes

- `t2_symmetry_check.py` rerun gives an identical receipt.
- My own union-find (`indep_t2_sym.py`) over node frozensets under the 6 axis permutations gives 36/171/561 → **18/100/301** classes:
  - n=2: {(1,3,7),(1,4,6),(1,5,8)} and {(1,7,8)};
  - n=4: {(1,15,19),(1,21,29)} and {(1,11,15),(1,25,30)}.
- Lexicographic minimum of the best class: **(1,15,19)**, as `preregistration-T2.md:34` "ties lexicographic" requires.
- Mechanism: 29⁻¹=50 mod 69 sends (1,21,29) to (50,15,1), which folds to (19,15,1).

## (7) Manifest guard

- `--verify` compares two things:
  - the exact sorted identity list of `code/*.py` and `evidence/*.json`;
  - `inherited_inputs` against fresh identities of `tracks/lattice-unisolvence/code/c3_lebesgue.py` (bf9cdb7c…, 6286 B) and `c3_rank.py` (a95afbb7…, 7430 B).
- The pins equal the helper hashes in the earlier receipts.
- Mutation tests in copies of the tree:

| Mutation | Result |
|---|---|
| one byte appended to c3_rank.py | FAIL, exit 1 |
| c3_lebesgue.py deleted | FileNotFoundError, exit 1 (loud) |
| `inherited_inputs` removed from the manifest | FAIL, exit 1 |
| regenerate without `--verify` | byte-identical to the committed 13,858 B manifest |

- **Compact fallback:** generate-mode only (separators-compact JSON if indented output ≥16 KiB). Not exercised: the committed manifest is indented. Verify parses JSON, so format is irrelevant.
- **No fallback silently passes.**
- Limits (NOTE):
  - the PASS line reports only local counts, not that the inherited check ran;
  - cold-storage.json, audit-01/code, non-.py/.json files and the manifest's own recorded_commands/limits fields are unpinned, by design;
  - verify checks identities, not receipt-internal source hashes.

## New findings

- **N1 MINOR — boilerplate template fields.** Dispositions and resume conditions are specific, but some IDEA fields are copy-pasted across records.
  - `candidates-deferred-response-01.md:14,16,17` repeat verbatim at :32-35, :50-53, :68-71, :86-89 and :104-107 ("Applicable obstructions", "Cheapest decisive test", "Test discriminability").
  - That text says "support, weight, symmetry" even for the T4-03 slice witness.
  - `candidates-T5-response-01.md:13-15`: literature, obstruction and verdict text repeats in all 5 records; "(T5-01 is equivalent validation)" appears in every verdict.
  - Fix: state the obstructions and hypotheses actually escaped per record, or mark the field "not separately assessed (retrospective)".
- **N2 MINOR — new process text in theory files.** The m5 addendum in all 21 theory files (e.g. `t1-minimal-obstruction.md:196`) says the response changes "require focused re-audit". That is new process-stage text in durable records and goes stale when audit-02 completes. Pending process belongs in the LOG, handoff and PR.
- **N3 MINOR — stale label and wider suffix collision.**
  - `attempts/T3.md:98-99` still reads "PD-N T3-01" for short relations.
  - "T3-02" now names PD-T (short relations), PD-N (full M39) and IDEA (annihilator tool).
  - The PR-preparation crosswalk must use full namespaced IDs (`response-01.md:119`).
- **N4 MINOR — inconsistent canonical pointer.**
  - `attempts/T2.md:36`, `attempts/T5.md:79` and the t5-validation addendum say "LOG contains the canonical disclosure".
  - `novelty-gate-T2.md:44`, the report and the PR name `response-deviations-01.md`.
  - Use the one named record everywhere.
- **N5 MINOR — stale or unsupported prose.**
  - `response-01.md:75,128` cite "integration notes" that were never committed (`git log --all` finds no such file).
  - `response-01.md:12-15` still says Results/PR/manifest integration is pending; it is complete at e80e000.
  - `report.md:194` "not an unperformed rank computation" is garbled.
  - `LOG.md:186` and `response-deviations-01.md:28-29` assert that "AC explicitly selected/selects Astra high in this continuation" without quoting AC — the m11 pattern again. Quote AC's words or the invocation prompt.
- **N6 NOTE.** `candidates-response-01.md` and `preregistration-T8.md` first entered Git together (`1c75e1f`), so "written before T8 prereg" rests on developer attestation; the file is unchanged since.
- **N7 NOTE.** Some in-place corrections keep only a dated marker (T6-01 verdict, T3 attempted-mechanism line, attempts/T4 rows, T1 statement). Originals are in Git; acceptable for clarifications.
- **N8 NOTE — formula validation scope.** The developer's census evaluates the classification's count formulas, which were validated against actual folded points only at cap 12. My actual-point construction closes that gap at the full cap for n=2..6.
- **N9 NOTE — file sizes and links.**
  - Evidence/code all <16 KiB; prose LOG, attempts/T7, attempts/T9 and independent-checks-new-math exceed 16 KiB (not generated evidence).
  - The one broken link (LOG→handoffs/05-audit.md) resolves at e14ac15.
- **N10 NOTE.** The response worker did not read the full raw registry (`response-01.md:78-82`); its records are retrospective retention, and the T7/T8 workers owned the full pre-run read. Disclosed.

## Commands executed

Environment: Python 3.13.18, numpy 2.3.5, sympy 1.14.0; plain `python` (no `-O`). All run inside an archive copy `a2-partA/tree` made with `git archive e80e000 | tar -x`.

1. `python topics/padua-3d-20261106/code/artifact_manifest.py --verify` → `{"verdict":"PASS","artifacts":56,"bytes":309009}`, exit 0.
2. Four mutation copies; results in the table above.
3. `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/…/code/t1_full_enum.py --output a2-partA/out/t1-full-enum.json` (1.4 s) → PASS, counts [636,1392,757,2520,4803], survivors 0. My field-by-field receipt comparison: 247 fields, differing only in `.python` and `.command[3]`.
4. `python topics/…/code/t2_symmetry_check.py --output a2-partA/out/t2-symmetry-check.json` → PASS; 45 fields, same two differences.
5. `python -I a2-partA/mycode/indep_t1_points.py` (23 s) → table in section 3. `capvar.py` → cap12 [480,708,172,162,318]; n2 cap32 = 636; n3 cap48 = 1392.
6. `python -I a2-partA/mycode/indep_t2_sym.py` → 18/100/301 classes, lex (1,15,19), 29⁻¹ = 50 mod 69.
7. Read-only git/grep checks, link and size scans, PR #33 body via GitHub API.

Hashes (prefixes):
- Audited files: t1_full_enum.py bb995f1c; t1_reflection_enum.py ac4afe4c; t2_symmetry_check.py e32ed93c; t1-reflection-enum.json 6340b00f; t1-full-enum.json f2026de4; t2-symmetry-check.json 36563798; evidence-manifest.json 8db710d3; artifact_manifest.py 338fd9b9.
- Audit scripts (uncommitted): indep_t1_points c0bb4cb8, indep_t2_sym c1ee7d09, capvar 41c68c9b.

## Remaining uncertainty

- Literature comparisons were checked only against repository records; no primary source was fetched, and Subbotin remains unverified.
- Full IDEAS registry not re-read (focused scope).
- AC's decisions on the M3 timing deviation, the T5 probe omission and the old budget stops are outstanding by design.
