# Sub-audit: novelty gate, literature wording, proposed records, write scope

Auditor: Claude Opus 5.5 (high), read-only sub-auditor for audit-01 of `padua-lebesgue-followups-20261103`.
Clone: /home/claude/padua_research, head 407fe83; audited dev SHA 5b2e367; base 440d107. History fetched (depth 300). No repo file edited; only read-only git commands.

## Verdict summary

- No BLOCKER and no MAJOR finding.
- T2, T3 and T4 are **not duplicates**. No record at base states any of the following: centre-minimality of g_v/g_h, g_h(pi/2)=1, a general-beta series, or a kappa formula. Every relevant base record says the opposite (OPEN, excluded, or explicitly not claimed).
- The T2/T3 protocol deviation is **confirmed and not cured**. I read the later-read sources myself. Their actual impact on candidates, verdicts, obstructions and kill tests is **minor**: one closest-entry omission (F1), with no change to any verdict or kill test.
- Literature wording is correctly bounded.
- The proposed statuses are right. Four MINOR record-hygiene items are listed below.
- Write scope is clean.

## Findings

**F1 — MINOR (protocol impact).**
- Where: topics/padua-lebesgue-followups-20261103/gate-t2-t3.md:41-43.
- Evidence: "Closest entries: IDEA-304 (central integration), IDEA-326/332".
- Problem: the closest entries for T2 are IDEA-318 (Brutman-type ordering umbrella) and IDEA-324 (E-C centreward edge order). The gate shortlists both (line 25) but leaves them out of the candidate's closest-entry field.
  - IDEA-318's original record (topics/padua-argmax-alln-20261101/ideas.md:74) says the measured vertical gap profile "is smallest at the centre ... compatible with an along-edge monotonicity toward the centre". That is the measured motivation for exactly this target.
  - PD-T207 and PD-T208 (MEASURED) are also not named as the measured predecessors. PD-T208 explicitly says "The requested general-β PD-T188 series has not been derived", which is the closest record to T3.
- Why it is only MINOR: these are finite-n cell orderings and finite measurements, while T2/T3 are limiting-integral statements. The "variant with difference" verdict, the separation criterion and the kill test do not change.
- Fix: add IDEA-318/324 and PD-T207/208 to the T2 and T3 closest-entry fields, and to the proposed IDEAS rows at preparation/proposed-registry-additions.md:78-79. Add one sentence that finite-n ordering is a different object.

**F2 — NOTE (protocol disposition).**
- Where: gate-t2-t3.md:10-13 and 87-96. The initial gate text at commit 4cfad03, lines 20-21, read "Shortlist read: ... full registered records and inherited attempts P1-P2-edges/T-A4a".
- Problem: that pushed claim was inaccurate. The full T-A4a read happened later. b721709 added the qualification but left the shortlist sentence in place.
- Disposition: this is a prospective-gate deviation against WORKFLOW.md:55-57 ("Then read the full shortlisted entries ... Generate candidates only after that gate"). Later reading does not cure it.
- Impact assessment, from my own reading of each later-read source:
  - IDEA-303-305 registration paragraphs (preparation/ideas-registration.md:175-203) are boilerplate pointers. Nil.
  - The full T-A4a attempt (98 lines) defines R_cen and the central routes. It has no centre-minimality, general-beta or monotonicity content. Nil.
  - The full IDEA-206 record (programme-ideas candidates.md:473-494) covers the corner expansion, counts and Fekete. Its only edge item is the runner-up "G(n)≈0.5483+0.839/n". Nil.
  - FINAL_CANDIDATES IDEA-318/324/325/326/327/332 each say "No center-minimality" or point to finite orderings. Their linked original IDEA-318 note is the only content of relevance, and it gives F1.
  - Overall impact: minor. No candidate, verdict, obstruction or kill test would change.
- Recommended disposition: deviation ACKNOWLEDGED, not waived. Readiness should not be blocked once F1 is fixed. Rewording gate line 25 to separate "read before derivation" from "read at reconciliation" would make the record self-consistent.

**F3 — NOTE (timing evidence).**
- Where: all three gate files contain no timestamps.
- Evidence: in the git history, the plan was committed at 11:18:49 (514e376). The gates gate-t1/t2-t3/t4 and the full 258-line t2-01 proof were all first committed together in 4cfad03 at 11:22:59. T4 records its start at 11:07, before the plan commit. T2.md:26 says derivation began at 11:18.
- Consequence: gate-before-mechanism ordering is plausible but rests on self-report; git cannot confirm it.
- T1 is completion of an existing target with no new mechanism. Its gate (gate-t1.md:5) correctly says so.
- Fix: none required. Future gates should carry UTC timestamps.

**F4 — MINOR (closest predecessor).**
- Where: theory/t4-02-one-dimensional-remainder.md:1-48 (Depends on / Sources). The string "158" appears 0 times in the file.
- Evidence: alias "local proof of the classical endpoint constant".
- Problem: t4-02 sharpens PD-T158's proved estimate |L_n−A_n|<2/n (T-A2.md:42; proof-attempts-2-codex-03) to 1/(4n²). It does not name PD-T158 as the closest predecessor. Gate-t4 does read PD-T156-159 in full.
- Fix: add "sharpens PD-T158's 2/n one-dimensional estimate" to t4-02 Sources or History, and to the proposed PROOF_STATUS row.

**F5 — MINOR (silent rewording).**
- Where: proposed-record-changes.md:55 (PD-T211) and :69 (PD-T230).
- Evidence: the old "center-minimality remains OPEN/excluded" text is replaced, not appended to.
- Problem: WORKFLOW.md:85 says "Do not narrow or reword an original claim silently". By contrast, the PD-T098, PD-T100, IDEA-206/299 and crosswalk proposals preserve the old text as a prefix (I checked this mechanically).
- Fix: keep the old Disposition cell verbatim and append "Dated 2026-11-03: the excluded limiting-integral centre-minimality is proved separately in t2-01 (endpoint behaviour in t2-02)".
- Also to resolve at preparation: PD-T212 gets no row annotation even though t2-01 says it is "Split from" PD-T212's exclusion. Decide whether PD-T212 needs one.

**F6 — MINOR (audit-link history).**
- Where: proposed-record-changes.md:27 (PD-T184) and proposed-t1-record-updates.md:41 (PD-T180).
- Problem: the new rows replace all old cells. That drops the old status text "OPEN, not rejected; deadline failures are not passes" and the existing [Claude audit-01]/[response-01] links. The status change to PROVED is correct, and both theory records preserve the history.
- Fix: keep the prior audit links in the Evidence/audit cell and add "earlier OPEN/deadline history preserved in the original record", matching the PD-T181 precedent row.

**F7 — NOTE (stale frontier clauses).**
- Where: state/CURRENT.md:82 and RESULTS.md:111 (base) both say "center-minimality ... remain OPEN" and "General-beta series, center-minimality ... OPEN". PD-T208's record says the general-β series "has not been derived".
- Problem: the proposed T2-T4 CURRENT paragraph (proposed-registry-additions.md:134) appends new text but does not mark those clauses as superseded at the proved limiting-integral scope. The T1 paragraph does mark its superseded clauses.
- Fix: add one sentence to the T2-T4 CURRENT paragraph stating which clauses are superseded.

**F8 — NOTE (results wording).**
- Where: results/padua-lebesgue-followups-20261103.md:9.
- Evidence: "PROVED 44/16/2 = 62 against the numerical source 38/56".
- Assessment: not an overreach. For consistency it could say "certified candidate correction of LIT-388 v1 Table 3".

## Item checks that passed

**(a) Gates present before mechanism.**
- Gates exist for T1, T2/T3 and T4.
- Each records closest entries, obstructions, verdict, cheapest test and kill criterion. Kill criteria are in the attempts/T2.md, T3.md and T4.md pre-run plans.
- Timing caveats are in F2 and F3.

**(b) Routes retained.**
- T2/T3 routes: gate-t2-t3.md:98-104 and T3.md:62-73. These cover PD-T188's alternating Taylor series, the single K chart, and the unused interval mesh.
- T4: the PSLQ search is labelled MEASURED, and the sharp-remainder goals are deferred (gate-t4.md:27-29).
- T1: the unused resume contingency, the symbolic-corner interrupt and the baseline interrupt are retained (T1.md:71; evidence receipts).
- I found no silently dropped route.

**(c) Duplicate check.** All grep searches were run over base 440d107, excluding this topic.
- Centre-minimality: always stated as OPEN or excluded. Locations: PD-T211 record :87, P1-P2-edges.md:46/58, PD-T230 record :53/217, FINAL_CANDIDATES IDEA-332, CURRENT:82.
- g_h(pi/2)=1: explicitly not claimed (argmax-alln-codex-05:100; gated-codex-16:53/217). The value appears only as a MEASURED ≈1.0000 note in an audit-support subreport (B-8), which itself says "no record claims it".
- General-beta series: "not derived" (PD-T208 record :31-32).
- Kappa: PD-T098 has only a MEASURED fit, κ=0.9197101183886, with identification OPEN. T-A2.md:44 says "κ ... remain OPEN". No integral or series formula for kappa exists. The only arsinh/artanh formulas are PD-T188's central g.
- Conclusion: none of T2, T3 or T4 duplicates an existing record.

**Literature.**
- literature-comparison.md, report.md:27-33, t1-closed-count.md:36 and the proposed LIT-388 addendum (proposed-t1-record-updates.md:139) all word 44/62 vs 38/56 as a "certified candidate correction" of the inspected v1 table only.
- They explicitly deny an accepted erratum, author contact, later-version coverage, and any Morrow–Patterson correction.
- The old LIT-388 2026-11-01 addendum is preserved verbatim.
- No external theorem is imported as a proof. LIT-379 is used only as baseline context in gate-t4.md:17. T4-02 proves the 1D estimate locally (lines 46-48, 78: "without an imported Euler–Maclaurin expansion").
- Every theory file says "no historical novelty claim".
- A scan of T/ for erratum, priority, novel, first, Morrow and correction wording found no overreach.

**Statuses.**
- PD-T184 and PD-T180: PROVED, reusing the existing IDs and IDEA-299.
- Six analytic records: PROVED, under provisional IDs.
- PD-T098: stays OPEN. This is correct: the A3 done criterion (OPEN_TARGETS.md:105-107) requires -1/N, O(log N/N²), and a closed form or exclusion for κ.
- PSLQ: MEASURED.
- PD-T100: kept MEASURED, with its "not a certified correction" text preserved.
- Split-from/into fields are consistent with the original codex-61 and codex-65 records.

**Old blocks literal.** I checked all 12 old→new Old blocks mechanically. Each occurs verbatim in the base file:
- PROOF_STATUS rows PD-T098/100/180/184/211/230
- IDEAS rows IDEA-206/299
- two ID_CROSSWALK rows
- the LIT-388 addendum
- the IDEA-299 disposition line, which occurs twice in ideas-registration.md. Preparation must target the IDEA-299 section, as the proposal says.

**Final IDs.**
- No final ID in the reserved ranges (PD-T266-285, PD-N092-099, IDEA356-375, LIT474-481) appears anywhere except as range statements in LOG.md:5, ALLOCATIONS.md and handoff 02.
- The crosswalk uses "unassigned" markers.

## Write scope

- `git diff --name-only 440d107 5b2e367`: every path is under topics/padua-lebesgue-followups-20261103/ except results/padua-lebesgue-followups-20261103.md (146 files, additions only).
- 5b2e367..407fe83 touches only LOG.md and handoffs/01-work.md, and adds handoffs/02-audit.md.
- No shared registry, frozen source or merged theory file changed.

## Read coverage

- state/IDEAS.md lines 440-889: read in full.
- Topic files read in full:
  - gate-t1.md, gate-t2-t3.md, gate-t4.md, plan.md, LOG.md, report.md, literature-comparison.md
  - attempts/T2.md, T3.md, T4.md
  - proposed-record-changes.md, preparation/proposed-registry-additions.md, preparation/proposed-t1-record-updates.md, ALLOCATIONS.md
  - theory/t1-closed-count.md
  - results/padua-lebesgue-followups-20261103.md
- Topic files read in part:
  - theory/t2-01 lines 1-12, 74-108, 255-262
  - t2-02 lines 1-12, 155-167
  - t3-01 lines 1-12, 108-120, 270-279
  - t4-01 lines 1-12, 75-85, 200-210
  - t4-02 lines 1-60
  - t4-03 lines 1-12, 60-70, 90-96
  - t1-interior-count headers and Sources
  - handoffs/01-work.md lines 40-50, 78-111
  - independent-checks-analytic.md lines 195-225
- Git: early versions of gate-t2-t3.md and T2.md at 4cfad03; diffs 4cfad03→b604f0d and b604f0d→5b2e367 (gate-t2-t3); 4cfad03→34150d0 (gate-t4); commit timestamps.
- Later-read sources, re-read by me:
  - padua-proof-attempts-2-20261101/preparation/ideas-registration.md lines 1-44 and 175-204
  - attempts/T-A4a.md: full
  - programme-ideas-20261031/ideas/candidates.md lines 473-494 (full IDEA-206)
  - padua-argmax-alln-20261101/FINAL_CANDIDATES.md lines 1-25, 56-70, 146-205, 266-280
  - padua-argmax-alln-20261101/ideas.md lines 39-52, 72-76
- Other predecessor records:
  - attempts/P1-P2-edges.md lines 35-81
  - attempts/T-A2.md lines 1-60
  - PD-T188 record lines 1-40
  - PD-T180/184 original record headers
  - PD-T207 record lines 1-30
  - PD-T208 record lines 25-40, 92-100
  - gated-codex-16 lines 45-56, 210-220
  - OPEN_TARGETS A3
  - PD-T098 record lines 60-70
- Shared files at base:
  - PROOF_STATUS rows PD-T098/100/159/180/181/183/184/187/188/211/212/230 and the PD-T208 row
  - literature/INDEX.md rows 206 and 215 and lines 500-525
  - WORKFLOW.md lines 53-92, plus a status/ID-rule grep
  - CURRENT.md lines 78-84
- Grep searches over base 440d107: centre-minimality, g_h(pi/2), general beta, kappa/κ, 0.9197 and 1.84616, arsinh/artanh, odd-offset integrals.
- Not checked: the mathematics (out of scope), the LIT-388 primary PDF (not re-fetched), and the PD-T212 theory body.
