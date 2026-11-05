# Claude audit-02 — focused re-audit of Codex response-01

2026-11-05. **Verdict: RESPONSE ACCEPTED, WITH MINOR FINDINGS.**

- Every audit-01 finding (A-M1, A-M2, A-P1 R1–R4, A-m1–A-m8) and every family NOTE disposition is resolved against the exact response bytes.
- No proof, formula, theorem statement or status changed beyond what audit-01 required.
- There is no BLOCKING or MAJOR finding. The eight MINOR record fixes and the NOTEs below can be made as the first part of audited PR preparation.
- **Stage → PR (audited preparation).**
- **AC's decision on A-P1 remains PENDING.** This audit does not and cannot accept the gate-timing deviation on AC's behalf. Neither merge readiness nor final IDs are implied. Only AC merges.

## Identity, inputs and rules

- **Auditor:** Claude, the cross-family independent auditor for handoff08. The orchestrator ran Claude Opus 5.5 (`claude-opus-5-5`) at effort **high**, as AC requested ("Claude (Opus5.5 high): Continue …") and as handoff08 assigns.
- **Why high, not xhigh:** handoff08 allows xhigh if a material mathematical statement or proof changed. The TXT family verified that every Proof section and every fenced formula block in all 17 modified theory files is byte-identical. The one exception is two L5-1 wording sentences in l5-03, so high was retained.
- **Subagents:** three Claude Opus 5.5 high subagents (TXT, EVD, GATE). They had no Git authority and returned their reports to this orchestrator.
- **Developer:** Codex (gpt-6.1-sol high, with medium workers and a supplementary gpt-6-astra check). No developer or supplementary conclusion was inherited.
- **Audited head:** response output `6a9a54a6af287a317e572c53de2ff9a851edb232`, fix checkpoint `a64b866e25a3b117c9ce87410e9b511f428881da`.
  - Files were read at publication head `2473ab5111ae6f20a5e5c346cec00d1eab56c679`. It differs from the output only by handoff07's status line and the new handoff08.
  - Per-file SHA-256 prefixes are in the family reports.
- **Rules:** AGENTS.md, agents/WORKFLOW.md and agents/claude/CLAUDE_ROLES.md, read at `2473ab5`. They are byte-identical to audit-01's rules (`3f1e74c`) and to current main.
- **Base:**
  - Branch merge `7f50cae` incorporates main `330fab8`.
  - main has since advanced to `9322fba` (PR25 merged). PR25 is not merged into this branch and changes no rules or Lanczos sources.
  - All 22 non-append literal OLD blocks in the registry proposals still match `9322fba` byte for byte.
  - PR25's assignments (T364–370, N132, IDEA454–461) do not overlap this topic's ranges.
- **Reading depth:**
  - This is a bounded response and impact audit. It adds no new candidate, mechanism, novelty verdict or negative claim, so the full IDEAS.md re-read required by the novelty gate was not repeated. audit-01's full read stands.
  - The R3 predecessor reconciliation was done substantively. The GATE report read IDEA-130/134/148/151 and the full PD-T035/037/041 and PD-N013/015 records, and ran a recorded bounded search of IDEAS.md for closer entries; none was found.

## Family reports (preserved as written)

| Family | Scope (handoff08 items) | Verdict | Report |
|---|---|---|---|
| TXT | 1 (A-M1), 4 (A-m1–A-m6, L2 chronology), 5 (frozen inputs), theory part of 8 | ACCEPT WITH MINOR FINDINGS | [TXT.md](audit-02/TXT.md) |
| EVD | 2 (A-M2), 6–7 (A-m7: compact G1, n1 recipe, storage), 8 (A-m8), PROT-1 notes | ACCEPT WITH MINOR FINDINGS | [EVD.md](audit-02/EVD.md) |
| GATE | 3 (A-P1 R1–R4, R3 reconciliation, AC question) | ACCEPT WITH MINOR FINDINGS | [GATE.md](audit-02/GATE.md) |

Auditor scripts and small receipts are in [audit-02/code/](audit-02/code/).

## Finding-by-finding disposition

| Audit-01 finding | Disposition | Key verification |
|---|---|---|
| A-M1 broader L3 PARTIAL | **RESOLVED** | Broader L3 is OPEN everywhere; L3-01 is a separate PROVED supporting result; Proof and all 18 formula blocks are byte-identical. The audit-attributed radius ceiling and the λ₁=0 qualification are correct (own derivation plus a 60-digit check). |
| A-M2 L7 kernel dependence | **RESOLVED** | Haswell/single-thread pinned before import; 18/9 vs 20/6 disclosed; MEASURED kept; no historical CPU invented. **Fresh rerun under the new recipe reproduces 20/6 with a byte-identical comparison** (EVD). |
| A-P1 gate timing R1–R4 | **RESOLVED technically**; AC acceptance PENDING | 14 candidates (16 rows), 18 descendant qualifiers, R3 separations independently confirmed, R4 forward-only. One wrong SHA (R2-GATE-1), one over-hedge (R2-GATE-2), one stale owner line (R2-GATE-3). |
| A-m1 small-n/affine wording | **RESOLVED** | n ≥ 18 threshold recomputed (0.79 at n=17, 1.28 at n=18). |
| A-m2 IDs and aliases | **RESOLVED** | Canonical agent-qualified numeric IDs with aliases; L4 split graph crisp. Residue: R2-TXT-4, R2-TXT-6. |
| A-m3 stale records | **RESOLVED** | Additive dated updates; frozen files untouched. Residue: R2-TXT-3, R2-TXT-5. |
| A-m4 wording | **RESOLVED** | Every listed fix verified at its location. Residue: R2-TXT-1, R2-TXT-2. |
| A-m5 literal proposals | **RESOLVED** | Every OLD block occurs exactly once in the registries at `330fab8`, `9322fba` and HEAD. No NEW block is applied. No final number. L4b is an IDEA-250 variant; L6-02 is IDEA-262's contract; 19+19 rows reconcile the "about 22" without invented IDs. |
| A-m6 priority wording | **RESOLVED** | Memo blob `4741c389` exists on the PR21 branch and is absent from main. Rows 14/15 and group C are cited correctly per statement. |
| A-m7 retrievability | **RESOLVED** (bounded) | Compact G1 tables: 152/152 T24 values enclosed and tight. The implication is valid because the counterchoice is certified at an **original-box** point, never an enlarged-box corner. n1 recipe rerun gives PASS/367/INCONSISTENT/5 controls with identical output hashes, writing only to scratch. Raw archival delivery remains OPEN, as disclosed. |
| A-m8 manifest | **RESOLVED** | Verify mode PASS for 330 files, including all 82 tracked audit-01 files. Independent `git ls-files` count agrees. JSON, size, link and whitespace checks pass. |
| PROT-1 G0/G4 notes | **RESOLVED** | Additive, accurate and scoped. Haswell relative differences of 7.9e-8 and 6.6e-5 were recomputed. |
| Family NOTE dispositions | **Accepted** | Deferrals (L1-5, L4-7, L5-9, L6-5, L7G1-9) are recorded as deferred, not done. No NOTE is used to support a stronger claim. |

Corrections to audit-01 recorded here, without editing audit-01:
- audit-01's "≥ 93.81" midpoint SSE bound was imprecise. The receipt lower bound is 93.8078…, so Codex's ">93.80" is the correct strict statement.
- See also the audit-01 log defect below.

## New findings

### MINOR (fix at the start of PR preparation; no science change)

**R2-1 — non-inclusion clause missing from "stronger" (R2-TXT-1).**
- **Where:** registry-proposals rows (PD-T143 NEW :64, IDEA-251 NEW :162, and :5, :340, :376, :404, :444, :463), attempts/L3.md :9/:234, ideas-l3-continuation.md :123/:135, LOG :246.
- **Problem:** these call the L3-01 model a "stronger per-column budget than Hres" without saying that neither class contains the other.
- **Remedy:** add that clause.

**R2-2 — PD-T143 cross-reference not tracked (R2-TXT-2).** L3-5 asked for a cross-reference from PD-T143's "excludes the pivot-adaptive rule" text (drift-codex-e3-11…md:91) to L3-01's adaptive corollary (9). Add a literal additive block scoped to model (1), or a tracked checklist item.

**R2-3 — G5 receipt SHA wrong (R2-GATE-1).**
- **Correct values:** the gate receipt was first preserved at `844e812` (blob `6b811daa…`), not `b6bf1f6`. The orchestrator confirmed the first-add commit and the heading at `844e812:5`.
- **Remedy:** add a dated erratum in gate-timing-response-01 (G5 bullet and rows :38–40), response-01 and LOG, with a same-commit caveat for L5a.

**R2-4 — L3 "survived unchanged" hedge misplaced (R2-GATE-2).**
- **Problem:** the hedge cites the unretained intermediate draft `cdcf…`. The pre-gate draft is committed at `0574c47:attempts/L3.md`, and its constants match theory (2)–(5) and (7) verbatim up to notation.
- **Remedy:** state the verifiable fact with its locator, and limit the `cdcf` caveat to the intermediate draft.

**R2-5 — stale decision owner (R2-GATE-3 = R2-TXT-3).** results/padua-lanczos-frontier-20261105.md:12 still says the deviation "remains for Claude disposition". It should say AC's decision is pending; the deviation is disclosed, not waived and not cured. Refresh the ROOT RESULTS proposal block to match.

**R2-6 — LOG header IDs (R2-TXT-4).** LOG.md:6 should read "PD-T L4-01 (alias L4a) … PD-N L4-01". Complete the list of checked claims, or point to the crosswalk.

**R2-7 — "not executed" wording beside the root's actual run (R2-TXT-5 = R2-EVD-2).** Add dated pointers in l6-n1-methods.md:52, l6-02-execution-metadata-20261105.md:13 and evidence-response-01.md:19 to the root execution and `evidence/response-n1-recheck.json` (`c683aaf8…`).

**R2-8 — audit-01 log files missing from Git** (R2-EVD-1; a **Claude audit-01 defect**, not Codex's).
- **Problem:** the repository `.gitignore` rule `*.log` kept 16 audit-01 auditor logs (25,193 B) out of every commit. Five of them are linked from audit-01/L2.md and audit-01/L7G1.md.
- **Orchestrator action (done):** commit `71131b2` preserves byte-identical copies under [audit-02/preserved-audit-01-logs/](audit-02/preserved-audit-01-logs/), with a `.txt` suffix and a SHA256SUMS file. audit-01 itself is not edited.
- **Codex action:** none, beyond including these files in the next inventory refresh. Whether `.gitignore` should change is outside this topic's scope and would be for AC.

### NOTEs (optional; record a disposition at preparation)

- **CURRENT label and main refresh** (R2-TXT-7): the CURRENT block's "old line103" label is now line 108. Include merged PR25 in the mandatory reservation and main refresh.
- **Working aliases** (R2-TXT-6): `…-codex-G1-fit` and `…-codex-L7` appear only in their own headers. Drop them or add them to the crosswalk.
- **Optional shifted ceiling** (R2-TXT-8): r_R ≤ 5^{−(N−2−j)/2}/(4√2λ_j) at the first positive λ_j.
- **Shared-commit order** (GATE N1): a per-line "reported, same commit" caveat would make the order claims consistent where a gate receipt shares its first commit with descendants (`b81c374`, `844e812`, `6012600`).
- **SH_n mirror context** (GATE N2): note PD-N011 and PD-N015, so the formal mirror upper bound is not read as a general rule ordering. Put the IDEA-130/134 separation in the l1-02 registry row.
- **W/R vs PD-N013 precision** (GATE N3): first-order invariance is universal within R_smooth. The "neither universalize" caveat applies to IEEE and unrestricted PD-T055(U). Avoid "actual" wording that could suggest IEEE runs.
- **Qualifier harmonization** (GATE N4): "not waived, not cured, AC pending" in all addenda, and name parent candidates in L4/L5 qualifiers.
- **R4 scope** (GATE N5): R4 is topic-level. A cross-topic rule would need an AC change to WORKFLOW.
- **Receipt dispatch** (R2-EVD-3): the environment receipt was collected with Haswell forced. Future receipts could record both default and forced dispatch.
- **Builder behaviour** (R2-EVD-4): `storage_response_inventory.py` without `--check` rewrites the committed index. State this near the recipe.

## Independent executions actually performed

All runs were in this cloud session: Linux, Intel Xeon with AVX-512F, single-threaded, on `git archive` copies or scratch.

**EVD family**
- `g1_compact_check.py`: PASS, both grids INCONCLUSIVE, 0.04 s.
- Own 400-bit mpmath enclosure of all 152 T24 compact values against the audit-01 regenerated endpoints, whose hashes equal the source pins: all tight.
- `response_evidence_check.py`, scratch copy: checks identical to the committed receipt. The vanished four-file packaging replay was not reconfirmed.
- n1 recipe verbatim: PASS, 0.109 s, output hashes identical.
- `check_manifest.py` verify: PASS for 330 files.
- **L7 triangle under the new Haswell recipe:** 37.3 s; 20 loss cells and 6 paired directions; comparison byte-identical to audit-01's Haswell run; all 43 arrays per seed equal.
- JSON, link, `git diff --check` and literal-OLD checks.

**TXT family**
- Hashes of the frozen files.
- audit-01's `section_hash.py` reproduces the L1 seven-section digest `13325943…`.
- Own 60-digit L3 radius and ceiling check for s = 2, 3, 4, across five budget patterns including λ₁ = 0 and λ ≡ 0.
- Byte-exact OLD/NEW search across five registries at three commits.
- Section and fence comparison of all modified theory files.

**GATE family:** read-only Git provenance only: 13 SHAs, first-add history, 21 `-S` searches, blob comparisons. Plus GitHub reads of PR24 (body and comments).

**Orchestrator**
- audit-01 and prior-handoff preservation diffs.
- Branch-only registry, rules and `.github` diff against main (empty).
- Confirmation of the G5 first-add commit.
- Ignored-file listing and log preservation (`71131b2`).

Failed or corrected attempts are recorded in the family reports: a wrong `--external` path, missing PYTHONPATH and an absent `time` binary.

**Not rerun:**
- the full G1 scan or fit;
- rotQ24 raw endpoint regeneration (the compact rotQ24 intervals enclose the receipt intervals);
- the non-triangle L7 cross-group recomputation (raw workers absent);
- the four-file packaging byte replay.

## Trusted dependencies and remaining limitations

- **Trusted:** CPython integers, Fraction, JSON and SHA-256; mpmath for enclosure confirmation; NumPy 2.3.5, SciPy 1.17.0 and OpenBLAS (Haswell) with polyrat `6903d7a` for the L7 rerun.
- **What the compact G1 check covers:** it proves the downstream finite implication from committed, pinned, outward-rounded tables. It does not authenticate arbitrary supplied tables or regenerate rotQ24 endpoints.
- **Disclosed, unresolved limits** (none is a finding against the response):
  - historical CPU/ISA for the original L7 run;
  - physical cold-storage delivery;
  - vanished `/tmp` inventories;
  - the uncommitted intermediate drafts (`9f59…`, `cdcf…`).

## AC decision status

The question in response-01.md:35 and the PR24 body is unchanged and **unanswered**: *Do you accept the permanently disclosed pre-gate drafting deviation after R1–R4 remediation, as audit-01 recommends?*
- Technically, R1–R4 now pass (subject to errata R2-3 and R2-4).
- Acceptance is not inferred from this audit, from elapsed time, or from the mathematics having been accepted.

## Stage and next step

- **Stage → PR**, for audited preparation by Codex under handoff09: first the R2-1–R2-7 fixes and NOTE dispositions, then the PR-preparation steps.
  - Merge current main (`9322fba` or newer).
  - Refresh the full active and retired reservation union.
  - Assign final IDs from the permanent ranges.
  - Apply the literal registry blocks.
  - Run the integration checks.
- **Re-audit required:** registry application and final-ID assignment are material registry changes under WORKFLOW, so they come back for a Claude preparation audit before readiness.
- **Open frontier:** all original unresolved research remains OPEN, as recorded.
- **AC decides** A-P1 and the merge.
