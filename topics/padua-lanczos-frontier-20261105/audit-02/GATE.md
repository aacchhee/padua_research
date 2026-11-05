# Audit-02 family report — GATE (A-P1 R1–R4, R3 predecessor reconciliation, AC decision)

**Auditor.** A subagent auditor, Claude Opus 5.5, at effort high, working under the Claude audit-02 orchestrator. The orchestrator saved this report from the subagent's returned text. All work was read-only inspection, and no scripts were retained.

- **HEAD:** `2473ab5`. `6a9a54a..2473ab5` only changes handoff07's status and adds handoff08.
- **Git and repository:** no changes and no writes.

**Verdict: ACCEPT WITH MINOR FINDINGS.** Three MINOR findings, five NOTEs, nothing BLOCKING or MAJOR. No novelty or status verdict changes.

## Scope (D = `topics/padua-lanczos-frontier-20261105`)

**Read in full**
- gate-timing-response-01.md (`bd2a85b0…`)
- response-01.md (`025330ae…`)
- handoffs/08-reaudit.md
- the three companions (l1-01 `dacdf1aa`, l2-01 `ff3ad75d`, l6-02 `a1ca8d19`)

**Read in part**
- audit-01.md A-P1, and audit-01/PROT.md §2.1/§2.2, PROT-2 and PROT-4.
- Family slices: L1-8, L2 protocol and L2-5, L3-7/L3-9, L4-9, L5 §5, L6-9.
- All seven ideas files: ideas-l1-l2 `25e1ed84…`, ideas-l2-continuation, ideas-l3-l4, ideas-l3-continuation, ideas-l5-l6, ideas-l5-continuation, ideas-l6-continuation.
- registry-proposals-response-01.md: the candidate and addendum rows.
- theory/l3-finite-u-selection.md: displays (2)–(7), Checks and History.
- The History qualifier lines of all 18 descendants.
- independent-checks-response-01.md: the A-P1 paragraph.
- report.md:96 and the results file.

**Predecessor records**
- state/IDEAS.md (`4c119736…`): rows IDEA-120–155, 246–267 and 286, plus the search hits below.
- PD-T035 (`6f54865c`), PD-T037 (`8d8cd658`), PD-T041 (`7b9e88fc`), PD-N013 (`64cbceb7`) and PD-N015 (`2202f19a`) in full; the PD-N011 statement.
- Old L1 candidates -106 and -110 with corrections PC-5…PC-10; IDEA-286's registration.
- Historical blobs at `0574c47`, `684849d`, `aab7bbe`, `b81c374`, `844e812`, `b6bf1f6` and `6012600`.

**Frozen pins** confirmed unchanged: l1-01 `f27a22c4`, l2-smooth `44498c62`, n1 contract `9d857e30`.

**Not read**
- WORKFLOW/CLAUDE_ROLES (the orchestrator read them).
- The old L2 candidates -204/-207 in full; the IDEAS rows plus the complete PD-N013/015 records carry their dispositions.
- PD-T156–159, which are unrelated.
- Proof bodies: unchanged in this scope.

## Items

### R1 — dated table (gate-timing-response-01.md:7–46): RESOLVED, with R2-GATE-1

**Commit facts**
- `40b3eb6` (09:54:24Z) is the direct parent of `0574c47` (10:05:00Z). `git grep` finds no candidate text in `40b3eb6`'s topic files.
- The three ideas files and attempts/L1–L6 are first added in `0574c47`.

**Candidate count**
- Candidate headings at `0574c47` number 5 + 4 + 5 = 14.
- The table has 16 rows: those 14 plus 2 retained non-candidate rows.

**Content and missing reads**
- `git log --all -S` puts 18 distinctive strings first in `0574c47`. Among them: `y=2*s_k+s_l`, `C_n >= 2^(n-4)`, `E_n >= 2^(n-8)`, `R_smooth`, `e/6`, and every candidate title. The L6 draft writes `e<=48c u`.
- Missing-read codes A/B/C match ideas-l1-l2.md:9–22, ideas-l3-l4.md:7–52 and 163–174, and ideas-l5-l6.md:5–7 at `0574c47`.

**Input SHAs**
- `684849d`: checkpoint 4, "Rules reread in full at 684849d".
- `f85c7b5`: the L3/L4 continuation, which still withholds gate completion.
- `0e493be`: the b81c374 delta gate.
- `bb67c1e`: the L3 and L5 continuations.
- `9825d18`: the L6 continuation.

**Gate-receipt blobs**
- `aab7bbe`: ideas-l1-l2 is `bbafcdd`, and ideas-l3-l4 is `7600595`.
- `b81c374`: `5b37a7b`.
- `844e812`: ideas-l3-continuation is `c0801a0`.
- `6012600`: ideas-l6-continuation is `8a59ee1`.
- The `684849d` ideas-l1-l2 blob equals `0574c47`'s (`034fe18`) and ends with the stop.

**Verdicts and wording**
- The post-gate verdicts and claims match PROT §2.1/§2.2.
- "Not waived and not cured" appears at :5 and :103.
- The G34 same-commit caveat and a general co-publication caveat (:107) are present.

### R2 — qualifiers: RESOLVED, with R2-GATE-2

**IDEA records**
- ideas-l1-l2 table: 6 rows, with l1-03 correctly post-gate.
- ideas-l2-continuation: W/R/F.
- ideas-l3-l4: L3-01/02 and L4-01/02.
- ideas-l3-continuation.
- ideas-l5-l6.md:67 and ideas-l5-continuation.
- ideas-l6-continuation.md:95.
- Registry proposals: 15 candidate rows, continuation addenda for IDEA-248/250/251/255/262, and inherited addenda for IDEA-158/160/162/253.

**Descendants: all 18 present.**
- 16 in-file History qualifiers: g1, l2-g2, l2-pos, l2-sh-wc, l2-sh-rand, l3, l4, l4-N01, l5-01…04, l6-01, l6-N01, l6-03 and l6-N02.
- 2 via companions, l1-01 and l2-smooth.
- Contract chronology: l6-02-execution-metadata:11.

**L6.** The identity, e/6 and e≤48cu are stated as pre-gate. The sharpening is "verification-only" and "sharpened to 24√3cu" (l6-01 History:162; gate-timing:41).

### R3 — closest-entry omissions (substantive): RESOLVED

**Source records match the response's descriptions:**
- PD-T035: includes sheared squares (loss data only), with selection and support-classifier corrections.
- PD-T037(a): M = 1681, n ≤ 20, dev rule; P* uses a long-double reference; the old Consequence sentence is refuted by PD-N011.
- PD-T041: exact dev-rule, degree-2 impulse, finite T24/Q24 through n = 12 plus T40/Q40/rotQ24; asymptotics OPEN.
- PD-N013: 12 benchmarks, M = 496–3000, n ≤ 47. The preregistered H_drift rule was inconclusive; the kill is post hoc on five sets, with later independent confirmation.
- PD-N015: dev/mirror/alt/adapt, six sets, M = 1681–3000, n ≤ 30.

**SH_n versus IDEA-130/134: the objects really differ.**
- L1-01 is an all-degree analytic bound on a normal-projected span derivative, with aggregate first-order sources and exact projection.
- It concerns one explicit weighted Gauss–U product grid mapped affinely by x = s, y = 2s + t, which is non-product in recurrence coordinates.
- IDEA-130/134 concern measured loss of orthogonality and raw propagator growth (P*, ‖L*⁻¹‖) on other sets.
- L1-01 does not settle IDEA-134's "general a priori lower bound" or PD-T041's triangle asymptotics.
- The separation correctly concedes that shears and affine-product grids were already probed: PD-T035(b) sheared squares, PD-T041 rotQ24, ideas-l1-l2.md:176.

**W/R versus IDEA-148/PD-N013 and IDEA-151/PD-N015: correct.** W/R are formal first-order statements over R_smooth with fixed BJ parents (worst-case C_n and independent-sign Frobenius expectation E_n). PD-N013/015 are IEEE measurements on other sets and rules.

**No verdict changes.** SH_n stays an IDEA-248 instantiation, W/R stay formalization variants of IDEA-255, and PD-T055 stays OPEN.

**Bounded search of state/IDEAS.md** (case-insensitive; hits per term):

| Term | Hits |
|---|---|
| shear/sheared | 1 (IDEA-286) |
| affine | 7 (IDEA-010/015/347/348, PD-N051/085) |
| "product grid" | 1 |
| "affine image" | 0 |
| closure | 4 (IDEA-150/254/337/466) |
| X-closure | 0 |
| J-closed | 0 |
| commutator | 23 |
| reorthogonal | 10 |
| selection | 7 (IDEA-130/134/135/151/181/251/266) |
| Gauss | 4 |
| U-grid | 0 |
| Chebyshev U | 0 |
| mirror | 0 |
| normal.quotient | 0 |

None of these hits is closer than the cited entries. IDEA-135/PD-N011 adds information (N2). IDEA-286 "sheared product-U" is a terminology coincidence, as the L1 gate already says.

### R4 — process control: RESOLVED

- **Where:** gate-timing-response-01.md:103, restated in response-01.md:33 and LOG:247.
- **What it requires:**
  - a worker records its gate, sends it to the orchestrator, waits for the commit and cites the returned SHA;
  - pre-gate notes are labelled "non-candidate brainstorming" and not pursued.
- **Wording:** explicitly "a future control, not a cure for 0574c47".
- **Limit:** it is a topic-level control only (N5).

### AC decision: RESOLVED, with R2-GATE-3

- The explicit question appears in response-01.md:35 and in the PR24 body ("Explicit AC decision — A-P1", read through `mcp__github__pull_request_read`).
- LOG.md:7 and report.md:96 reserve the decision for AC.
- PR24 has no comments.
- Acceptance is not inferred anywhere.

## Executions (own, read-only, each exit 0 within seconds)

- `git rev-parse` and `git show -s` on the 13 cited SHAs.
- `git log --diff-filter=A` on the ideas, attempts and theory files.
- `git log --all --reverse -S'<string>'` for 21 strings: 20 resolved to `0574c47` or later. `48cu` gave `6f10e90` (a later spelling), and `48*c*u` gave nothing.
- `git show <sha>:<path>`, plus `git diff` for `0574c47→684849d`, `684849d→aab7bbe`, `844e812→b6bf1f6`, `aab7bbe→b81c374` and `45646d7→6a9a54a`.
- `git grep` on `40b3eb6`; `sha256sum`; `grep` over IDEAS.md and the topic files.
- GitHub MCP reads of PR24 (`get`, `get_comments`).

## Findings

**R2-GATE-1 (MINOR) — wrong first-preserved SHA for the G5 receipt.**
- *Location:* gate-timing-response-01.md:22 (G5 bullet) and :38–40 (L5-01/02/03 rows). response-01.md:30 and LOG:247 summarize it.
- *Evidence:*
  - The record says the receipt was first preserved at `b6bf1f6` (15:43:13Z), blob `b29d2de`.
  - In fact ideas-l5-continuation.md was first added at `844e812` (15:30:34Z), blob `6b811daa2449644dcf81a5ca822f88e8e5f5cfa3`. That version already contains the complete "Completed pertinent gate before new development" section, and `844e812→b6bf1f6` only appends "Actual n3 outcome".
  - `844e812` also first adds theory/l5-01-finite-optimal-radius-certificates.md, so Git cannot order the receipt against L5a.
  - The error is conservative: it places the receipt later than it was. But R1 requires exact SHAs.
  - The orchestrator confirmed the first-add commit and the heading at `844e812:5`.
- *Remedy:* a dated additive erratum giving `844e812`/`6b811da` for G5, with a same-commit caveat like G34's.

**R2-GATE-2 (MINOR) — L3 "survived unchanged" hedged against the wrong draft.**
- *Location:* theory/l3-finite-u-selection.md:444–450; ideas-l3-continuation.md audit-response paragraph; ideas-l3-l4.md "Timing qualifier for each IDEA L3-01…".
- *Evidence:*
  - These say the constants survived "according to the developer's account; the unretained draft limits byte verification". That limitation (L3-7) concerns the uncommitted intermediate Astra-reviewed draft `cdcf…`.
  - The pre-gate draft itself is committed at `0574c47:attempts/L3.md`. Its constants match theory (2)–(5) and (7) verbatim up to notation (d = KΔ, h_p(k), α_ki for A_k(i)): H, C_k, h_k, b, D_kl, T_kl, Δ, F, J, r_R, B_R and θ_s ≤ uKF + 4u²K[J+F(b+KΔ)].
  - The hedge contradicts the plain wording at gate-timing:34 and registry-proposals :9, :162, :340.
- *Remedy:* state the verifiable fact with the `0574c47` locator, and limit the `cdcf` caveat to the intermediate draft.

**R2-GATE-3 (MINOR) — stale decision owner in results.**
- *Location:* results/padua-lanczos-frontier-20261105.md:12, unchanged by the response.
- *Evidence:* it still says "remains for Claude disposition". Claude gave its disposition in audit-01, and acceptance now rests with AC. (Same as R2-TXT-3.)
- *Remedy:* "A-P1: AC decision pending; disclosed, not waived or cured."

**N1 (NOTE) — order inside shared commits.**
- These gate receipts share their first commit with descendants:
  - G12 delta `b81c374`, with L1-01/L2-01;
  - G3 `844e812`, with L3-01;
  - G6 `6012600`, with L6-01, N01 and the contract.
- Some qualifiers state the order as fact rather than "reported": the L1 companion, "Later completed gates preceded the proof" for L3, and L6.
- This matches audit-01's accepted fact statement and the general caveat at :107. A per-line caveat like G34's would be more consistent.

**N2 (NOTE) — selection context for the SH_n mirror result.**
- L1-01's polynomial mirror upper bound is formal and holds for one family.
- PD-N011 measured that the dev/mirror ordering depends on the set; mirror is worse on rotπ/4 (3.4e-1 vs 4.2e-3). PD-N015 measured that mirror is not uniformly safe.
- Suggest adding these as context, with "no general rule ordering".
- The l1-02 registry row cites IDEA-130/134 without its one-line separation, which lives in ideas-l1-l2.md:247–255.

**N3 (NOTE) — sharper W/R wording relative to PD-N013.**
- R_smooth with fixed BJ parents formally contains exact-base first-order analogues of PD-N013's plain, CGS2 and partial schemes, so L2-01's rule invariance is universal within R_smooth.
- "Neither universalize … to every rule" is right for IEEE and unrestricted PD-T055(U), and could say so explicitly.
- "Prove actual first-order closure" (ideas-l1-l2.md:257–260) could be misread as meaning a real IEEE run.

**N4 (NOTE) — qualifier wording varies.**
- Registry continuation and inherited addenda say "does not cure" without "not waived" or "AC pending".
- The L4/L5 descendant qualifiers do not name their parent candidate.
- The retained IDEA-253 reading in ideas-l1-l2 has no local qualifier; its registry addendum does.
- Harmonization is optional.

**N5 (NOTE) — R4 is topic-level only.** Making it a cross-topic rule would require AC to amend WORKFLOW.
