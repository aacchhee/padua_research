# Audit-02 family report — TXT (statuses, wording, IDs, proposals, frozen inputs)

**Auditor.** A subagent auditor, Claude Opus 5.5 (`claude-opus-5-5`), running at effort high as AC requested; runtime effort is not independently exposed. It worked under the Claude audit-02 orchestrator. The orchestrator saved this report from the subagent's returned text. Scripts are in [code/R-TXT/](code/R-TXT/).

- **HEAD:** `2473ab5`; response input head `6a9a54a`.
- **Git:** no state changes and no repository writes.

**Verdict: ACCEPT WITH MINOR FINDINGS.**
- Handoff08 item 1 (A-M1), item 4 (A-m1–A-m6 and the L2 chronology corrections) and item 5 (frozen inputs) are resolved, together with the theory-file part of item 8.
- Five MINOR record-wording fixes (R2-TXT-1…5) and three NOTEs. None touches a proof, formula or status.

## Scope (D = `topics/padua-lanczos-frontier-20261105`)

**Read at HEAD (sha256 prefix):**

| File | sha256 |
|---|---|
| handoffs/08-reaudit.md | `4541b9d2` |
| audit-01.md | `63b3ed82` |
| audit-01/L3.md | `ec5ec066` |
| response-01.md | `025330ae` |
| registry-proposals-response-01.md | `1b1c910b` |
| independent-checks-response-01.md | `59d14564` |
| theory/l3-finite-u-selection.md | `703c3414` |
| theory/l1-01-audit-response-20261105.md | `dacdf1aa` |
| theory/l2-01-audit-response-20261105.md | `ff3ad75d` |
| theory/l6-02-execution-metadata-20261105.md | `a1ca8d19` |
| attempts/L3.md | `57e1d3d1` |
| ideas-l3-continuation.md | `0eab4e31` |
| ideas-l3-l4.md | `203d241d` |
| ideas-l1-l2.md | `25e1ed84` |
| report.md | `fd0dcf72` |
| results/padua-lanczos-frontier-20261105.md | `1403c92f` |
| LOG.md | `bb964995` |
| l6-n1-methods.md | `b7270b21` |

**Also read:**
- The finding texts in audit-01/L1, L2, L4, L5, L6 and PROT.
- Diffs `45646d7..6a9a54a` of every modified theory, attempt and ideas file in scope.
- The PD-T143 record.
- handoff01 lines 35 and 81.
- The P3 memo blob `4741c389`.
- The five registries at `330fab8`, origin/main `9322fba` and HEAD.

**Not read:**
- The full IDEAS.md: no novelty verdict is in this scope.
- The L7/G1, storage and manifest material: covered by the EVD report.
- The full gate-timing table: covered by the GATE report.

## Items

### Item 1 / A-M1 — RESOLVED

**What changed**
- The broader L3 target is OPEN everywhere outside quoted, superseded History: attempts/L3.md:3–11 and History :230–246; ideas-l3-continuation.md:121–142; theory header :7–15; report.md:33, :86; results:16; proposal rows.
- L3-01 is a separate PROVED supporting result.

**Proof unchanged.** The l3 file at `45646d7` (`d42f4e89…`, the bytes audit-01 accepted) was compared with HEAD (`703c3414…`):
- the `## Proof` section is byte-identical;
- all 18 fenced formula blocks are identical;
- the Statement and Finite-selection sections changed only in prose (the model comparison and the routine monotonicity sentence answering L3-8).

**The added prose checks out**
- *Monotonicity.* The sentence is correct: B_R(u) = uK(F+uJ)/[(1−ub)(1−ud)] is nondecreasing in b, d, K, F and J while the denominators are positive.
- *Covering cost.* "Covering every Hres direction forces λ_k v_k/β_k* ≥ C_loc√(N−1)χ_R" is correct to first order, giving F ≥ C_loc(N−1)χ_R. "Neither class contains the other" is correct.
- *Radius ceiling.* The audit-attributed ceiling is correctly derived. h_1 = 2λ_1v_1/β_1* ≥ 2λ_1, and H_k² ≥ 5H_{k−1}², so b ≥ 2λ_1·5^{(N−3)/2}. With d ≥ √2·b this gives r_R ≤ 5^{−(N−3)/2}/(4√2λ_1). For λ ≡ 1 the ceiling is ≈1.2e−19 at s=9 and ≈3.7e−16 at s=8, so "below 2^−53 for s≥9" is right.
- *λ_1 = 0.* The qualification is correct and conservative:
  - with λ_1 = 0 the λ_1-based bound is vacuous (+∞);
  - a shifted ceiling r_R ≤ 5^{−(N−2−j)/2}/(4√2λ_j) holds at the first index j with λ_j > 0;
  - λ ≡ 0 gives r_R = 1.
- *Split from.* The quotes are verbatim: PD-T143 record line 103 and handoff01:81.

**No new theorem was registered from audit observations.** The ceiling appears only in the dated, attributed note.

### Item 4

**A-m1 — RESOLVED.**
- The n≥18 qualifier and the affine-product wording appear in the L1 companion :15–17, ideas-l1-l2, results:9, the IDEA-248 NEW block, the PD-T L1-01 row and the CURRENT NEW block.
- Recomputed ratio: 0.79 at n=17 and 1.28 at n=18. The weaker form (3) gives 0.69 and 1.11.

**A-m2 — RESOLVED** (residue in R2-TXT-4 and R2-TXT-6).
- Canonical theory IDs: L3-01, L4-01, L5-01…04, G1-01, L7-01. The frozen L1 header is historical; its companion gives L1-01.
- Canonical IDEA headings: L3-01/02, L4-01/02, L7-01…04, with aliases.
- Old aliases now appear only in labelled alias, History, checkpoint or superseded contexts.
- L4 dispositions are crisp:
  - IDEA L4-01 is REJECTED: failed only for 100U<G_R with the fixed old lower;
  - IDEA L4-02 is retained as an IDEA-250 variant;
  - PD-N L4-01 splits from the failed subroute only.

**A-m3 — RESOLVED** (one residual stale line, R2-TXT-3). Each listed record has a dated additive update:

| Finding | Update |
|---|---|
| L2-1 | companion |
| L2-3 | dated disposition table |
| L4-5 | pointers in l4-N01 and attempts |
| L5-2 | attempts and continuation checkpoint |
| L5-3 | l5-01 Open items; historical NOT RUN label |
| L6-1 | forward pointers and companion |
| L7G1-3 | ideas-l7 addendum and external-code addendum, including the backports.cached_property correction |
| PROT-6, PROT-8 | LOG header and Runs needed; exact upstream_xy command; no invented commands |

**A-m4 — RESOLVED.** Each fix was verified at its location:

| Finding | Verified fix |
|---|---|
| L2-2 | L2-04:73 and L2-05:63 cite `f27a22c4…` |
| L2-4 | results:10 |
| L4-1 | status table now says "distinct re-execution of the pinned S/V producer" |
| L4-3 | results:5 |
| L4-6 | 217.2247 s at theory:183, methods:194 and attempts:193 |
| L5-1 | l5-03:44 ("saved dyadic"); l5-03:46 separates source `335bb5c3` from input `ee25f934` |
| L5-5 | b₄ and b₅ cited at l5-03:56 and l5-04:54 |
| L6-3 | scoped REJECTED objects |
| L6-4 | l6-03:108 uses the frozen 64u, ε/6, ε/12 rules |
| L7G1-2 | l7:93 |
| L7G1-7 | g1:106 ">93.80/>50.35" |

The only Proof section touched is l5-03's "Proof and finite evidence", by the two L5-1 sentences.

**A-m5 — RESOLVED.**
- Every OLD block was extracted and searched byte-exactly in PROOF_STATUS.md, state/IDEAS.md, state/CURRENT.md, ID_CROSSWALK.md and RESULTS.md. Each occurs exactly once at `330fab8`, at current origin/main `9322fba` and at HEAD.
- No NEW block occurs in any registry, and the registries are byte-identical between `330fab8` and HEAD, so nothing has been applied.
- Every NEW block is purely additive except the audit-accepted PD-T140 target change PARTIAL→PROVED and the matching CURRENT/crosswalk wording.
- No final number appears anywhere in the response diff.
- L4b is registered as an IDEA-250 variant, and L6-02 as IDEA-262's contract with no PD-T row.
- Counts reconcile audit-01's "about 22" without invented IDs:
  - 19 candidate rows;
  - 19 mathematical rows (16 PD-T and 3 PD-N);
  - the 3 abandoned L6 inferences mapped to IDEA-262, IDEA-158/160 and IDEA-162;
  - IDEA-253 cross-referenced separately.

**A-m6 — RESOLVED.**
- Blob `4741c389…` exists and equals `topics/padua-literature-20261103/p3-comparison.md` on origin/claude/padua-literature-20261103. It is absent from main, so "PR21 (unmerged)" is correct.
- Row 14 (PD-T136/137/141, "no matching result found in the documented search") and group C (PD-T053, PD-T136–143) are cited correctly.
- Row 15 (PD-T142/143, "RELATED, DIFFERENT SETTING", Barrio–Peña–Sauer Remark 9) is cited correctly; the addendum says "Row 15: unaffected".
- report.md:102–115 matches per statement and states the coverage limits.

**L2 chronology corrections (RC-01) — RESOLVED.**
- All five passages say "first preserved at aab7bbe (684849d worker input/rules SHA)".
- Git confirms aab7bbe (11:22:15Z) with blobs `bbafcdd1…` and `76005951…`.
- 684849d still ends with the incomplete-gate stop.

### Item 5 — RESOLVED

- The three frozen files have SHA-256 `f27a22c4…` (L1), `44498c62…` (L2-01) and `9d857e30…` (n1 contract). None changed since `45646d7`; they were last touched at `b81c374`, `b81c374` and `6012600`.
- Their checker pins match: sh_independent.py, g2_screen.py, and l6_n1_independent.py:228.
- All three companions exist and are additive.
- `git diff --diff-filter=MDR 45646d7 HEAD -- D/code D/evidence` is empty; there are only additions (4 code files, 7 evidence files).
- Checker-pinned l7-preregistration.md and g1-fit-spec.md are unchanged.
- OPEN targets are intact: PD-T055/F, PD-T056(G), U2/G3 (n4/5 uppers, n6–8, handoff01 n3–10), broader L3, and scalar/IEEE.

### Theory files (item 8 part)

Across all 17 modified theory files, every fenced block is identical and every Proof section is byte-identical, except l5-03 (the L5-1 sentences).

## Executions (own; nothing run in the repository)

1. `sha256sum` of the three frozen files at HEAD.
2. `python3 -B audit-01/code/L1/section_hash.py theory/l1-01-…md` on a `git archive HEAD` copy: exit 0, 0.018 s. It printed "MATCH seven" and reproduced the companion digest `13325943…`.
3. Inline computation of the L1 ratio threshold for n = 15..19.
4. Own checker [l3ceil.py](code/R-TXT/l3ceil.py) (`3edbc9d5…`), in 60-digit mpmath on random rational triangle nodes, run for s = 2, 3, 4 (exit 0; 0.13, 0.39 and 1.33 s).
   - Budgets tested: λ≡1, λ_1=0, λ_1..3=0, only the last λ positive, and λ≡0.
   - Results: d ≥ √2·b always held, and r_R stayed below the original or shifted ceiling. λ_1=0 gives +∞ for the original formula, and λ≡0 gives r_R = 1. For example, s=4 with λ≡1 gives r_R = 1.70e−14 against a ceiling of 1.13e−5. MEASURED only.
5. Literal OLD/NEW checks, [oldcheck.py](code/R-TXT/oldcheck.py) and [olddel.py](code/R-TXT/olddel.py), against `330fab8`, `9322fba` and HEAD.
6. Section and fence comparison scripts for l3 and all modified theory files.
7. `git cat-file`/`ls-tree` checks on the memo blob, and `git log`/`rev-parse` on aab7bbe and 684849d.

Failed attempts: one missing-mpmath error before PYTHONPATH was set, and the absent `/usr/bin/env time`.

## Findings

**R2-TXT-1 (MINOR) — "stronger" budget wording lacks the non-inclusion clause.**
- *Location:* registry-proposals-response-01.md :5, :64 (PD-T143 NEW), :162 (IDEA-251 NEW), :340, :376, :404, :444, :463; attempts/L3.md :9, :234; ideas-l3-continuation.md :123, :135; LOG.md :246.
- *Evidence:* these say "stronger per-column (finite-error) budget than Hres". The theory (:107–113), report:33 and response-01:18 say neither class contains the other. Read alone, the durable registry rows suggest (1) is a sub-hypothesis of Hres, which is exactly what L3-3 asked to avoid.
- *Remedy:* add the clause "a different per-column zeroth-order finite-error budget, neither containing nor contained in Hres".

**R2-TXT-2 (MINOR) — L3-5's cross-reference into PD-T143 is not tracked.**
- *Location:* registry-proposals :64; tracks/bivariate-lanczos/theory/drift-codex-e3-11-selection-criterion.md :91 ("excludes the pivot-adaptive rule").
- *Evidence:* L3-5 asked that this text cross-reference L3-01's adaptive corollary (9) at registry time. No literal block or tracked obligation exists for it.
- *Remedy:* add a literal additive block, or a checklist item, scoped to model (1) only, not Hres.

**R2-TXT-3 (MINOR) — stale, contradictory results line, also copied into the ROOT RESULTS proposal.**
- *Location:* results/padua-lanczos-frontier-20261105.md:12, and the ROOT RESULTS NEW block in registry-proposals.
- *Evidence:* line 12 says the timing deviation "remains for Claude disposition", while line 14 says acceptance is AC's decision. (Same as R2-GATE-3.)
- *Remedy:* say "AC decision pending; disclosed, not waived or cured", and refresh the ROOT block.

**R2-TXT-4 (MINOR) — LOG header ID usage.**
- *Location:* LOG.md:6.
- *Evidence:* it says "L4a … and L4-01 scoped … obstruction". Under the new scheme PD-T L4-01 is the positive theorem and PD-N L4-01 the negative. The list also omits L3-01, L5-01..04, the L6 records, G1-01 and L7-01.
- *Remedy:* write "PD-T L4-01 (alias L4a) … PD-N L4-01 …", and complete the list or point to the crosswalk.

**R2-TXT-5 (MINOR; cross-scope with EVD) — "not executed" wording in the same commit that records the root's execution.**
- *Location:* l6-n1-methods.md:52; l6-02-execution-metadata-20261105.md:13; evidence-response-01.md:19.
- *Evidence:* all three are at `a64b866`, which also adds evidence/response-n1-recheck.json. LOG:249 and response-01 say the root executed the recipe once. (Same as R2-EVD-2.)
- *Remedy:* add a dated pointer naming the root execution and the receipt (`c683aaf8…`).

**R2-TXT-6 (NOTE).** The "response working aliases" `PD-T?lanczos-frontier-codex-G1-fit` and `PD-T?lanczos-frontier-codex-L7` (g1:4, l7:4) appear nowhere else and are missing from the crosswalk alias lists. Drop them, or add them at preparation.

**R2-TXT-7 (NOTE).** The CURRENT block is labelled "old line103"; at `330fab8`/`9322fba` the paragraph is at line 108. The OLD text still matches exactly. origin/main has since merged PR25 (PD-T364–370, PD-N132, IDEA-454–458). Every OLD block still matches at `9322fba`, and nothing overlaps T324–363/N116–131/IDEA414–453/LIT582–593. Refresh the label and include PR25 in the reservation refresh.

**R2-TXT-8 (NOTE, optional).** The shifted ceiling r_R ≤ 5^{−(N−2−j)/2}/(4√2λ_j) could be added. The current non-assertion is correct.
