# Response-02 group E1: developer report (A02-M2, A02-L1)

Developer: Claude Opus 5.5, xhigh (mathematical developer, group E1). Rules read: AGENTS.md; WORKFLOW.md, the status table, the split rules (lines 63–87) and computation/evidence (95–107); CLAUDE_ROLES.md developer items 4–5; the common brief. Rules were read at branch head 1df5f89. While I worked, the orchestrator committed other groups' work (b216cb3, 99cc9f9, a7a9b77, 20bbb65). `git diff 1df5f89 20bbb65` touches no E1 producer, no E1 evidence, no audit-01/02 check file and no E1 theory record; among the drift code it changes only README.md. I ran no state-changing git command.

Inputs read in full: handoff 07 (items 2–3); audit-02.md; checks/audit-02/E1.md; evidence/audit-02-e1-checks.json (scalar, first-principles and limits blocks); records 03, 04 and 05; directions E1.md and E2.md; ideas-e1.md; checks/audit-01/E1-records-01-05.md; first_principles.py; ind_scalar.py; the producers e1_cgs2.py, e1_cgs2_witness.py, e1_cgs2_multinode.py, e1_reproduce.py and e1_sign_check.py; evidence e1-scalar-cgs2.json, e1-multinode-certificates.json, e1-posthoc-scalar-ratios.json, e1-scalar-manifest.json, e1-reproduction-triangle.json, e1-sign-check-*.json and independent-scalar-01.json (structure and decisive fields); checks/independent-math-01.md (opening sections).

I did not read state/IDEAS.md. No new mechanism or novelty claim was introduced: record 06 is a reclassification of existing finite content.

## (a) Dispositions

| Finding | Disposition | Files / line ranges changed (current working tree) | Summary |
|---|---|---|---|
| A02-M2 (E1-R1) | FIXED (split done; I agree with it, no disagreement for AC) | **NEW** `tracks/bivariate-lanczos/theory/drift-codex-e1-06-finite-scalar-cgs2-separation.md` (whole file, 131 lines). Record 05 `drift-codex-e1-05-…md`: 1–25 (title, alias, Split into, Statement), 45–65 (Status by part, PARTIAL target classification, split paragraph, Depends on), 79–81 (Checks), 89 (Proof or evidence), 95–106 (Open items), 115 (Regeneration path), 139–140 (response-02 note), 145–147 (History). `directions/E1.md` 80–81 (ledger rows 05 and new 06) and 134–138 (Response-02 annotations). `directions/E2.md` 9–16. `ideas-e1.md` 94–96 (IDEA-05). **NEW** `tracks/bivariate-lanczos/code/drift/e1_scalar_finite_check.py`. **NEW** `topics/padua-lanczos-drift-20261101/evidence/response-02-e1-scalar-finite.json` | The finite exact inequalities move unchanged to PD-T?drift-codex-06, PROVED (finite, computer-assisted), with a written reduction via record 03, an exact checker and evidence, reused independent executions and a new developer regeneration. Record 05 stays MEASURED (experiment) with the INCONCLUSIVE both-grid test. Its factor-ten target is labelled PARTIAL: T24 conjunct PROVED in -06, rotQ24 conjunct OPEN. |
| A02-L1 (E1-R2) | FIXED, with a new degree-4 execution | Record 03 `drift-codex-e1-03-…md`: 103–107 (Checks), 146 (Open items), 157 (History). Record 05: 98–101 (Open items), 148 (History). `directions/E1.md` 79 and 140. `directions/E2.md` 7 and 20. `ideas-e1.md` 75. **NEW** `tracks/bivariate-lanczos/code/drift/e1_replay_n4.py`. **NEW** `evidence/response-02-e1-replay-n4.json` | Coverage now reads: degree 3 (audit-01; re-executed by audit-02) and degree 4 (response-02, developer execution, not independent); no degree 12. Record 04 has no replay-coverage text, so it is unchanged. |

New provisional ID: PD-T?drift-codex-06. `git grep` and a working-tree grep found no prior use of "drift-codex-06" in any namespace.

Content of record 06:

- Model: record 03's formal scalar-CGS2 l-infinity model; K_inf is the supremum of the first-order span-normal output, measured in spectral norm.
- (a) Full-graph comparator uppers: K_pivot(T24)² ≤ U_T < 2.4e10 and K_alt(rotQ24)² ≤ U_R < 1.36e10.
- (b) Explicit BJ node-sign witnesses (t=86, t=90): K_BJ(T24)² ≥ G_T > 1.57e16 and K_BJ(rotQ24)² ≥ G_R > 8.4e11.
- (c) Consequences:
  - T24: G_T/U_T = 657331.077… ∈ (657331, 657332), so K_BJ > 800 K_pivot and K_BJ > 10 min(K_alt, K_pivot).
  - rotQ24: G_R/U_R = 62.0855… ∈ (62, 63), so K_BJ > 7 K_alt ≥ 7 min.
  - The integer chains need no division by a condition number.
- (d) G_R/U_R < 100: these endpoints neither establish nor refute factor ten on rotQ24. This is labelled a minor routine fact about the certificate.
- Post-hoc provenance is stated explicitly and does not qualify the status.
- Scope: no IEEE lower bound, no implementation behaviour, no exact K, no degree other than 12, no all-degree claim.

## (b) Commands actually run (repo root; `PYTHONPATH=/workspace/padua-drift-runs/python-deps OPENBLAS_NUM_THREADS=1`; CPython 3.13.18, python-flint 0.9.0, mpmath 1.3.0)

The times are UTC on 2026-11-01. Working outputs are in `/workspace/padua-drift-runs/response-02/E1/`, outside Git.

1. `python3 tracks/bivariate-lanczos/code/drift/e1_reproduce.py --set triangle --output /workspace/padua-drift-runs/response-02/E1/reproduce-triangle.json` at 16:42:20. PASS, 2.98 s wall.
2. `python3 tracks/bivariate-lanczos/code/drift/e1_cgs2.py --set triangle --degree 12 --rule pivot --output …/cgs2-triangle-n12-pivot.json`. Exit 0, 3.59 s. The upper equals the committed U_T exactly. The record-03 hash recorded in the output is f3cea17d…, from before my edits.
3. `python3 tracks/bivariate-lanczos/code/drift/e1_reproduce.py --set rotated --output …/reproduce-rotated.json` from 16:42:42. PASS, 174.75 s wall, concurrent with run 6.
4. `python3 tracks/bivariate-lanczos/code/drift/e1_cgs2.py --set rotated --degree 12 --rule alt --output …/cgs2-rotated-n12-alt.json`, ending 16:49:50. Exit 0, 252.66 s. The upper equals the committed U_R exactly.
5. `python3 tracks/bivariate-lanczos/code/drift/e1_replay_n4.py --rules bj --output <scratchpad>/response02/replay-test-bj.json` at about 16:43. A timing test, 14 s; it wrote outside the repository and is not evidence.
6. `python3 tracks/bivariate-lanczos/code/drift/e1_replay_n4.py --output topics/…/evidence/response-02-e1-replay-n4.json`, 16:44:04–16:45:18, with code sha c3267d9c…. All pass. **This output was overwritten by run 7**, after a one-line change that added `sys.dont_write_bytecode`. Run 6 had written `checks/audit-01/scripts/E1/__pycache__/first_principles.cpython-313.pyc`, a gitignored cache file in the frozen audit-01 directory. I removed that `__pycache__` directory; it was created by my runs 5–6 and did not exist before. Its numbers were identical to run 7.
7. **Final:** `python3 tracks/bivariate-lanczos/code/drift/e1_replay_n4.py --output topics/padua-lanczos-drift-20261101/evidence/response-02-e1-replay-n4.json`, 16:51:35–16:52:47, 72.2 s, code sha `d454de30f6c4d1cda7967cb6ee4c21cd956dadd563b0e5632bed5195574cfcad`.
   - all_pass true.
   - Degree 4: 20 nodes (seed 2), bj/mirror/alt/pivot, no ties, 17710 formal operations per case. Full-replay relative error was at most 2.0027e-80, and every partC discrepancy at most 2.416e-80. Dot/norm-only errors gave a tangential part of 0.86289 with normal part ≤ 1.83e-80. Second-matvec-only errors gave ≤ 1.69e-80. θ(ε)/(ε·pred) = 1.0 at ε = 1e-20 and 1e-30.
   - The degree-4 partA outputs equal the audit-02 receipt.
   - The degree-3 control equals the audit-02 receipt field for field, including C_record03 (max 6.0012e-81).
   - Evidence: 23800 bytes, sha256 `22093d9dff7e3981182d8dbe82095bde0a5db36566b4587fa4910c483b2e870b`.
8. `python3 tracks/bivariate-lanczos/code/drift/e1_scalar_finite_check.py --output <scratchpad>/response02/finite-test.json` (test run): PASS.
9. **Final:** `python3 tracks/bivariate-lanczos/code/drift/e1_scalar_finite_check.py --regenerated /workspace/padua-drift-runs/response-02/E1 --regeneration-notes /workspace/padua-drift-runs/response-02/E1/regeneration-notes.json --output topics/padua-lanczos-drift-20261101/evidence/response-02-e1-scalar-finite.json`, code sha `422a6495caa33a275b084b7a98ab8aeaee0ee698de0d8c512a9eefaf6d2f7193`.
   - all_pass true: 31 T24 checks and 34 rotQ24 checks, plus the regeneration comparison of runs 1–4.
   - It was run twice; the second run replaced the notes' wrong "HEAD 1df5f89" statement with the actual moving-HEAD chronology.
   - Final evidence: 11339 bytes, sha256 `f4d63bac7663edee93449fc7ec4687be65ce81c0404a95742d6adcf039c02039`.

Reused, not re-executed by me: independent-scalar-01.json (Codex supplementary checker, 11:32:54Z); audit-01 `ind_scalar.py` (E1-records-01-05.md item 6); audit-02 `reaudit.py scalar`, triangle exact and rotated Arb, in audit-02-e1-checks.json.

## (c) Proposed text for files I do not own

**1. `tracks/bivariate-lanczos/code/drift/README.md`.** Anchor: line 63, the single line `` `upper_squared.exact` of each output is the comparator upper of PD-T?drift-codex-05. ``. Replace it with:

```
`upper_squared.exact` of each output is the comparator upper U_T or U_R of PD-T?drift-codex-06 (a); these inequalities were stated in PD-T?drift-codex-05 until the response-02 split.
```

Insert after line 74 (`committed producer and is not an independent reimplementation.`), before `## E4 exact closure check (response-01)`:

````
## E1 finite scalar checker and degree-4 replay (response-02)

```bash
PYTHONPATH=/workspace/padua-drift-runs/python-deps OPENBLAS_NUM_THREADS=1 python3 tracks/bivariate-lanczos/code/drift/e1_scalar_finite_check.py --output topics/padua-lanczos-drift-20261101/evidence/response-02-e1-scalar-finite.json [--regenerated DIR [--regeneration-notes FILE]]
PYTHONPATH=/workspace/padua-drift-runs/python-deps OPENBLAS_NUM_THREADS=1 python3 tracks/bivariate-lanczos/code/drift/e1_replay_n4.py --output topics/padua-lanczos-drift-20261101/evidence/response-02-e1-replay-n4.json
```

`e1_scalar_finite_check.py` (audit-02 A02-M2) uses the standard library only (exact `fractions.Fraction`) and runs in under a second. From the SHA-256-pinned committed evidence it checks every inequality of PD-T?drift-codex-06: the full-graph comparator uppers, the BJ node-sign lower witnesses, K_inf,BJ > 800 K_inf,pivot on T24, K_inf,BJ > 7 K_inf,alt on rotQ24 and the rotQ24 certificate ratio < 100. It also checks exact agreement with the reused independent evidence (`independent-scalar-01.json`, `audit-02-e1-checks.json`). It does not recompute capacities. With `--regenerated DIR` it also compares, exactly, outputs that the `e1_cgs2.py` commands above and `e1_reproduce.py --set triangle|rotated` wrote to DIR as `cgs2-<set>-n12-<rule>.json` and `reproduce-<set>.json`. The response-02 regeneration of all four took about 7 minutes, the rotated upper about 250 s.

`e1_replay_n4.py` (audit-02 A02-L1) needs mpmath and runs in about 75 seconds. It loads the unchanged audit-01 `checks/audit-01/scripts/E1/first_principles.py` by path, after checking its pinned hash and without writing bytecode there. It then runs that script's record-03 full-trajectory replay `partC` at degree 4, which the script's own loop skips (`if n == 3`), and reruns degree 3 as a harness control against the audit-02 receipt. This is a developer execution, not an independent rerun.
````

**2. `results/padua-lanczos-drift-20261101.md`.** Anchor: line 24, the row beginning `| [PD-T?drift-codex-05](…) | MEASURED experiment; finite split requested in audit-02 |`. Replace that whole row with these two rows:

```
| [PD-T?drift-codex-06](../tracks/bivariate-lanczos/theory/drift-codex-e1-06-finite-scalar-cgs2-separation.md) | PROVED, finite computer-assisted, formal scalar model (split from -05 in response-02, A02-M2; re-audit pending) | At degree 12 in record 03's formal scalar-CGS2 model (l-infinity relative operation errors), the full-graph comparator uppers and explicit BJ node-sign witnesses give K_inf,BJ > 800 K_inf,pivot on T24 (squared certificate ratio 657331.08) and K_inf,BJ > 7 K_inf,alt on rotQ24 (62.09). The thresholds were chosen post hoc. The rotQ24 certificate ratio is below 100, so it does not decide factor ten there. No IEEE or all-degree claim. |
| [PD-T?drift-codex-05](../tracks/bivariate-lanczos/theory/drift-codex-e1-05-finite-scalar-cgs2-capacities.md) | MEASURED experiment; factor-ten target PARTIAL | The exploratory scalar experiment and its both-grid factor-ten test are INCONCLUSIVE: the test passes on T24 and not on rotQ24. The factor-ten target is PARTIAL: T24 conjunct PROVED in -06, rotQ24 conjunct OPEN. |
```

Optionally, in the row at line 22 (PD-T?drift-codex-03), append before the final `|`: ` Full-trajectory replay: degree 3 independent (audits), degree 4 developer (response-02).`

**3. `topics/padua-lanczos-drift-20261101/report.md`.**

(i) Anchor lines 43–50, from `Exploratory exact finite bounds for that full graph give a triangle squared` through `hashes and a deterministic regeneration/check path.`. Replace with:

```
Exact finite bounds for that full graph, found during post-E1 exploration, are
now a separate finite computer-assisted result, PD-T?drift-codex-06 (PROVED in
the formal model; split from record05 in response-02). They give a triangle
squared BJ/pivot certificate ratio of about 657331 (K_inf,BJ > 800
K_inf,pivot) and a rotated-square BJ/alt ratio of about 62.09 (K_inf,BJ > 7
K_inf,alt). These thresholds were chosen post hoc. The rotated ratio is below
100, so the certificate neither passes nor kills factor 10 there. Record05
keeps the MEASURED exploratory experiment and the INCONCLUSIVE both-grid
factor-10 test. Its factor-10 target is PARTIAL: the T24 conjunct is PROVED in
-06, the rotQ24 conjunct OPEN. Subset-map upper bounds are not substituted for
full implementation bounds. The large raw capacity output remains outside Git,
with compact signs/gains, hashes, a deterministic regeneration path and the
exact checker e1_scalar_finite_check.py.
```

(ii) Anchor at line 169: `The scalar endpoints/capacities have now been independently regenerated; record05 remains MEASURED and its factor10 comparison remains INCONCLUSIVE.` Replace with:

```
The scalar endpoints/capacities have been independently regenerated. Their finite inequalities are PD-T?drift-codex-06 (PROVED, computer-assisted, response-02). Record05 remains the MEASURED experiment, and its both-grid factor10 test remains INCONCLUSIVE.
```

**4. `topics/padua-lanczos-drift-20261101/plan.md`, line 20 (E1 row).**

- Replace `scalar-graph finite capacities MEASURED` with `scalar-graph finite inequalities PROVED (record 06, computer-assisted); scalar experiment MEASURED (record 05)`.
- Replace `(record 05 MEASURED: factor-ten INCONCLUSIVE, >7/>800 thresholds post hoc)` with `(record 06 PROVED: >800 on T24 and >7 on rotQ24, thresholds post hoc; record 05 MEASURED: both-grid factor-ten test INCONCLUSIVE, target PARTIAL)`.
- Replace `Theory01-05` with `Theory01-06`.

**5. `topics/padua-lanczos-drift-20261101/independent-checks.md`, after line 54 (`update. Root's later receipt addition to record05 changes metadata only.`).** Append:

```
Response-02 note (A02-M2): these executions are now cited as the independent
execution references of PD-T?drift-codex-06, which holds the finite
inequalities split from record05. Record05 remains the MEASURED experiment.
"record05 remains MEASURED" above describes the file before that split.
```

**6. `topics/padua-lanczos-drift-20261101/proposed-record-changes.md`.** Insert a new section after the paragraph at line 143 (`At preparation also update the corresponding PROOF_STATUS rows, split crosswalk, …`):

```
### E1 scalar finite split (response-02, audit-02 A02-M2)

At preparation, record the split PD-T?drift-codex-05 → PD-T?drift-codex-06 in ID_CROSSWALK.md with original-to-split mappings:
- PD-T?drift-codex-05 statement table (full-graph comparator uppers, explicit BJ multinode witnesses, squared ratio lower bounds) and its post-hoc consequences K_inf,BJ > 800 K_inf,pivot (T24) and K_inf,BJ > 7 K_inf,alt (rotQ24) → PD-T?drift-codex-06, PROVED (finite computer-assisted, formal scalar-CGS2 model).
- PD-T?drift-codex-05 keeps the exploratory experiment, MEASURED, with the both-grid factor-ten test outcome INCONCLUSIVE.

Its factor-ten target, "factor ten on both sets", i.e. K_inf,BJ > 10 min(K_inf,alt, K_inf,pivot) on T24 and on rotQ24, is registered as PARTIAL: T24 conjunct PROVED under PD-T?drift-codex-06 (c), rotQ24 conjunct OPEN. Give both records PROOF_STATUS rows. If the registry needs the target as its own row, use the PARTIAL status with a dependency on PD-T?drift-codex-06. No final IDs are assigned during the response.
```

**7. `topics/padua-lanczos-drift-20261101/response-02.md`, the E1 dispositions.**

```
**A02-M2 — FIXED (split).** The finite exact scalar inequalities formerly carried in MEASURED record05 are now PD-T?drift-codex-06 (new file `tracks/bivariate-lanczos/theory/drift-codex-e1-06-finite-scalar-cgs2-separation.md`). It is a precisely scoped computer-assisted PROVED record in record03's formal model (independent formal relative operation errors |delta|<=1, l-infinity source, first-order normal map, spectral output). It contains:
- (a) full-graph comparator uppers K_pivot(T24)² ≤ U_T < 2.4e10 and K_alt(rotQ24)² ≤ U_R < 1.36e10;
- (b) explicit BJ node-sign witnesses K_BJ(T24)² ≥ G_T > 1.57e16 and K_BJ(rotQ24)² ≥ G_R > 8.4e11;
- (c) G_T/U_T = 657331.077… ⇒ K_BJ > 800 K_pivot on T24 (and factor > 10 against the better comparator), and G_R/U_R = 62.0855… ⇒ K_BJ > 7 K_alt on rotQ24;
- (d) G_R/U_R < 100, so these bounds do not settle factor ten on rotQ24.

The written reduction from record03 is: absolute-sum/Frobenius upper, and the attained target-column gain for any sign vector, so validity does not depend on the greedy rule. Thresholds, targets and comparators were chosen post hoc or exploratorily. This is stated as provenance and does not lower the status. No IEEE lower bound, implementation behaviour, exact K or all-degree claim is made.

Evidence and checks:
- Essential evidence (unchanged): e1-scalar-cgs2.json and e1-multinode-certificates.json.
- New exact checker `e1_scalar_finite_check.py` (Fraction only; pins verified; 65 checks plus agreement with the reused independent evidence), output `evidence/response-02-e1-scalar-finite.json`, all PASS.
- Reused independent executions, with their source pins: independent-scalar-01.json, the audit-01 ind_scalar.py run, and the audit-02 E1 reconstruction (audit-02-e1-checks.json).
- New in response-02 (developer execution, not independent): `e1_reproduce.py` on both sets (PASS) and `e1_cgs2.py` for both comparators (exactly equal uppers), 16:42–16:50 UTC.

Record05 keeps the MEASURED experiment, its post-hoc history and the both-grid factor-ten test outcome INCONCLUSIVE, with "Split into: PD-T?drift-codex-06". Its factor-ten target is written out as its two conjuncts and labelled PARTIAL (T24 PROVED in -06, rotQ24 OPEN); the file status stays MEASURED. Original wording is preserved in History. E1/E2 directions and IDEA?drift-codex-05 were updated. The developer agrees with the substantiveness classification, so no disagreement is recorded.

**A02-L1 — FIXED (corrected, and the missing replay executed).** The committed audit-01 `first_principles.py` replays record03's full scalar trajectory only at degree 3 (partC is guarded by `n == 3`); its degree-4 cases run records 01/02 only. Record03 Checks/Open items, record05 Open items, E1/E2 and IDEA?drift-codex-04 now read: degree 3 (audit-01; re-executed by audit-02) and degree 4 (response-02, developer execution, not independent).

The new driver `tracks/bivariate-lanczos/code/drift/e1_replay_n4.py` calls the unchanged audit-01 functions by path (hash-pinned, file not edited) with the seeds the script's loop would use. Results: 20 generic rational nodes, all four rules, 17710 formal operations per case, maximum discrepancy 2.4e-80 at 80 digits, all checks pass. The degree-3 control reproduces the audit-02 receipt field for field. Evidence: `evidence/response-02-e1-replay-n4.json`, run 2026-11-01 16:51:35–16:52:47 UTC (72 s). An earlier identical run, 16:44–16:45 UTC, was overwritten after a one-line no-bytecode change. No degree-12 replay is claimed.
```

**8. `topics/padua-lanczos-drift-20261101/LOG.md`, the response-02 entry, E1 bullet with the annotation of audit-01's summary error.**

```
- E1 (A02-M2, A02-L1; Claude Opus 5.5 xhigh developer):
  - New PD-T?drift-codex-06, PROVED (finite, computer-assisted, formal scalar model), split from record05. It carries the full-graph uppers, BJ node-sign witnesses, >800 on T24 and >7 on rotQ24 (post hoc), and the rotQ24 certificate ratio < 100.
  - Record05 is the MEASURED experiment; its both-grid factor-ten test is INCONCLUSIVE; its target is PARTIAL.
  - New exact checker e1_scalar_finite_check.py with output evidence/response-02-e1-scalar-finite.json (PASS). Reused independent executions are cited with their pins. Developer regeneration: e1_reproduce on both sets and e1_cgs2 for both comparators, PASS, about 7 minutes.
  - New degree-4 replay e1_replay_n4.py with evidence/response-02-e1-replay-n4.json (PASS; developer execution).
- Annotation (A02-L1; the audit files are unchanged): audit-01's summary states that the record-03 full normalized-trajectory replay ran "at degrees 3 and 4" (audit-01.md:67), and that it "now exists at degrees 3–4" (audit-01.md:103). Its E1 report repeats this under Remaining uncertainty ("covers degrees 3 and 4", checks/audit-01/E1-records-01-05.md:169). This is an error. The committed first_principles.py runs partC only when n == 3, and the same report's own record-03 disposition says "degree 3". Response-01 propagated the error into record03, record05, E1/E2 and ideas-e1, and into checks/response-01/E1-developer-report.md:23 ("degree 3-4"). Response-02 corrects the active files and adds an actual degree-4 replay as a new developer execution with its own chronology. The frozen audit-01 and response-01 files are not edited.
```

## (d) For the Codex re-audit

1. **New PROVED record PD-T?drift-codex-06.** Check:
   - the reduction (Proof or evidence);
   - the claim that validity of (b) needs only s ∈ {±1}^M;
   - that the integer threshold chains avoid dividing by a possibly-zero K;
   - the scope list: no IEEE, implementation, exact-K, other-degree or all-degree claim;
   - the post-hoc provenance wording;
   - the minor-routine labelling of (d).
   The display bracket "sqrt(G_T/U_T) ∈ (810, 811)" is a new, checker-verified display fact. It is not presented as a threshold claim.
2. **Record05 restructure.**
   - New title: "Exploratory formal scalar-CGS2 capacity experiment and the unresolved factor-ten comparison". The old title is in History.
   - The bounds table was removed from the Statement and quoted in History.
   - The file status stays MEASURED.
   - **Classification choice to check:** the factor-ten target is written as two explicit conjuncts and labelled **PARTIAL** (T24 PROVED in -06 (c), rotQ24 OPEN), as a separately labelled claim inside a MEASURED file. Reading the comparator as min(alt, pivot) or as E1's decisive comparator gives the same split. If the auditor prefers the target as its own registry row or file, proposed-record-changes block 6 allows that at preparation.
3. **Evidence independence.**
   - The new checker is a developer checker that reads committed rationals. It does not recompute S_t.
   - Recomputation comes from the producers: the response-02 developer regeneration, and the earlier independent producer reruns in independent-scalar-01.
   - The independent implementation is ind_scalar.py (audit-01, rerun by audit-02).
   - For rotQ24 the exact rationals are producer outputs. The independent implementation gives Arb enclosures, and its ratio enclosure alone lies in (49, 100).
4. **Degree-4 replay.**
   - Developer execution, not independent.
   - 80-digit corroboration, not an exact proof.
   - It imports the frozen audit-01 script by path without editing it.
   - One earlier identical output was overwritten (chronology in (b)).
   - A `__pycache__` that my run had created inside `checks/audit-01/scripts/E1/` was removed. It was gitignored and untracked, and no tracked file changed.
5. **Record 03.** Only coverage text and one History line changed. The record-03 hash recorded inside my e1_cgs2 regeneration outputs is the pre-edit f3cea17d….
6. **ID_CROSSWALK/PROOF_STATUS.** Not touched. The split mapping is proposed for preparation (block 6).

Nothing new for memory.
