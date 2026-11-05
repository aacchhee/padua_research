# Padua literature campaign (P1–P4): log

- Branch: `claude/padua-literature-20261103` · Base: main `440d107` · Developer: Claude · Auditor: Codex (gpt-6-astra high)
- Stage: WORK · Next: `Claude (Opus 5.5 high): Continue claude/padua-literature-20261103.` · Next handoff: [handoffs/05-response.md](handoffs/05-response.md)
- Reserved final-ID ranges: LIT-482–561 (80); no PD-T, PD-N or IDEA range. See [ALLOCATIONS.md](ALLOCATIONS.md).
- Claims: none (literature topic). Note: [SINUM 2026 assessment](notes/faghih-sinum-2026-assessment.md).
- Open for AC: the remaining PDFs in DOWNLOADS.md v5 (A9 print-only, interlibrary loan; A10, A15, A19 low priority).

## 2026-11-03 — Claude, claude-opus-5-5 (configured; effort not exposed) — topic setup

- AC's requests:
  - "Now one more handoff for Claude, to do literature campaigns on new results and related papers. I also added one recent PDF on IEP done by Van Barel group, check whether it is of interest for IEP plans."
  - Then: "that literature campaign should give me clickable links to journals and/or dois to download fulltexts without searching".
- Rules read at `440d107`. Branch created from main `440d107`.
- New PDF: `Downloads\padua\papers\25m1770965.pdf` (staged; 27 pp.). It is Faghih–Rinelli–Van Barel–Vandebril–Vermeiren, SINUM 64(4) (2026) 1190–1216, DOI 10.1137/25M1770965, the published version of arXiv 2506.19796 (existing LIT-347/LIT-119, until now UNVERIFIED).
  - Read with pdftotext: §1, §3.2, §4.2–4.4, §5 opening with Alg. 5.1, §6.2–6.3, §7 and the references.
  - Assessment and record corrections: [note](notes/faghih-sinum-2026-assessment.md). Verdict: moderate interest (related work, a test-methodology template, the open IEP-conditioning question matching our sensitivity tools, and the analogy between multi-index paths and selection rules). Not a campaign by itself.
- Wrote handoff 01 (packs P1–P4, with clickable-link download lists as AC's hard requirement), this LOG and the results stub. No records or registries edited.

## 2026-11-05 — Claude, claude-opus-5-5 (configured; effort not exposed) — pass 2 ingest

- AC: "some papers have arrived. ingest, update the literature branch", then "I authorize all branch updates related to literature".
- Re-inventory of `Downloads\padua\papers` (44 files) through the link to AC's computer. New: A4 (Mastroianni–Russo 2000) and A11–A14 (journal versions); see [inventory.md](inventory.md).
- A4 read by the orchestrator: text layer for §1 and §3, page images of copy pp. 22–23 for the Theorem 11 hypotheses. New record `literature/records/mastroianni-russo-2000.md`; P2 comparison row added; report "Pass 2".
- A11–A14: a Sonnet 5.5 subagent mapped every cited locator onto journal pages (read-only, no git). The orchestrator spot-checked Xu 1996 Thm 3.3 (rendered p. 231), CDMV (13) p. 80, and BCDMVX Thm 1 p. 19 / Thm 2 p. 20. Results are in [addenda/journal-versions-2026-11-05.addendum.md](addenda/journal-versions-2026-11-05.addendum.md); the KLP record (topic-owned) gained a journal-version section; bib notes were updated.
- proposed-record-changes.md: "Pass 2" blocks, each old block verified to occur exactly once in the current files.
- DOWNLOADS v5. Checkpoint commit `f47b6a5`.
- Handoff 03 had not started (the branch had no audit commits), so it is superseded by handoff 04, which keeps the same audit task and adds the pass-2 scope at the new input head.

## Runs needed

- Steps 0–5 of handoff 01.

## 2026-11-03 — Claude, claude-opus-5-5 (configured; effort high per handoff, runtime effort not exposed) — handoff 01 steps 0–2

- Rules read at branch head `0a173a29ec938c47f8a5a1942208edf03ab2f767` (AGENTS.md, agents/WORKFLOW.md, agents/claude/CLAUDE_ROLES.md). Role: topic orchestrator and literature developer. `origin/main` = `440d1079e42c` (unchanged since the branch was cut; no merge needed).
- Step 1 inventory: AC granted access to `Downloads\padua` and `Downloads\bttb` (an earlier automatic request was refused; AC then authorised it in chat at 13:28). Listed `Downloads\padua\papers` (24 PDFs) and `Downloads\bttb\papers` (≈230 files). Filenames only are recorded in [inventory.md](inventory.md); citation matching is delegated (Sonnet 5.5 medium).
- Step 2 search and verify: delegated per pack to Sonnet 5.5 high subagents (P1, P2, P3, P4), with Crossref (`api.crossref.org/works/<doi>` via WebFetch) as the DOI check. The shell cannot reach doi.org, Crossref or arXiv (proxy refuses); WebFetch can.
- Steps 1–3 done (2026-11-03, about 13:30–14:25 local):
  - Inventory: all 24 `Downloads\padua\papers` files matched to citations (21 Crossref-confirmed, 1 partial, 2 offline-only: TW629, Humet thesis).
  - Link verification: four Sonnet 5.5 high subagents, one per pack. Claude spot-checked the load-bearing items and read the key ones itself (see step-4 notes below).
  - [DOWNLOADS.md](DOWNLOADS.md) v1 written and sent to AC.
- Access method: text extraction with pdf.js in the built-in browser on AC's computer.
  - Works: arXiv, Springer (NTNU), Math-Net.ru, UMJ, DergiPark, author pages.
  - ScienceDirect and SIAM stop at a bot check, which is not bypassed. Those items are in DOWNLOADS Part A.
  - Browser downloads do not land in a connected folder, so no PDFs were saved on AC's machine.
- Step-4 readings so far, by Claude (opus); paraphrase notes are kept off-repo until the records are written:
  - Białas-Cież–De Marchi–Suder arXiv 2605.23299v1: complete.
  - Kolomoitsev–Lomako arXiv 2009.07114v1: locator check for audit F6. Thm 2.1 p. 4; Lemma 3.5/(3.20) pp. 10–11; Lemma 3.6/(3.29) pp. 11–12. Confirmed against the printed running heads. (3.27)–(3.30) are imported from Kuznetsova 1995.
  - Kuznetsova, Ukrainian Math. J. 47 (1995): complete; Thm 1 checked on the page image.
  - Pimenova, Dokl. 249 (1979): OCR text only.
  - Corner statements: CDMSV 5ECM poster 2008 (Conjecture); De Marchi, CMA 5(1) 2022 §3.3(2) p. 23; BCDMV, Computing 76 (2006) pp. 318–319 (Xu points).
- 2026-11-03 ~14:00: AC supplied 10 PDFs (DOWNLOADS v2), staged into the cloud workspace and read with pdftotext.
  - P1 (Claude): Brutman 1978 complete; Günttner 1980/1988 statements; published KL AMC numbering identical to arXiv v1.
  - P2 and P3 files were passed to their reader subagents.
- Step 4 for P1 is done:
  - records (new): kuznetsova-1995, pimenova-1979, ehlich-zeller-1966, cdmsv-poster-2008, bcdmv-computing-2006, kolomoitsev-lomako-2021, bialas-ciez-demarchi-suder-2026, brutman-1978, guenttner-1980-1988;
  - [p1-comparison.md](p1-comparison.md);
  - P1 blocks in [proposed-record-changes.md](proposed-record-changes.md).
- P2, P3 and P4 reading runs as three Opus 5.5 high subagents (one browser tab each). Their outputs go to scratch first; the orchestrator integrates them.
- 2026-11-03 ~14:10: P4 integrated, from the P4 reader subagent (Claude Opus 5.5 high).
  - [p4-memo.md](p4-memo.md) for AC.
  - 8 new records in literature/records/ (provisional LIT?padua-literature-claude-70…84).
  - 4 addenda for existing records in [addenda/](addenda/).
  - P4 blocks in proposed-record-changes.md; [bib/leuven-iep.bib](bib/leuven-iep.bib).
  - Orchestrator check: memo and records spot-read; no verbatim third-party passages beyond titles. Keyword search of all P4 sources for bivariate/multivariate/Padua/Chesnokov: zero hits.
- 2026-11-03 ~14:15: P2 integrated, from the P2 reader subagent (Claude Opus 5.5 high).
  - [p2-comparison.md](p2-comparison.md); 5 new records (LIT?padua-literature-claude-20…24); 5 addenda; P2 blocks in proposed-record-changes.md; [bib/padua-mz.bib](bib/padua-mz.bib); [check/](check/).
  - Main findings:
    - the SVZ eq. (25) denominator misprint is also in the journal version (p. 417, page image), and Table 1 confirms the correct form;
    - PD-T106 is now IMPLIES PART;
    - Wu AML 2026, Don–Gottlieb journal and Dencker–Erb journal gaps are closed;
    - König–Nielsen journal body: De Gruyter showed "Unlicensed", so it is still unread.
  - Orchestrator rerun of check/svz_table1.py: reproduced (see check/README.md). PDF text extracts are kept off-repo.
- 2026-11-03 ~14:25: draft [PR #21](https://github.com/aacchhee/padua_research/pull/21) opened, with WORK, AUDIT (PENDING) and PR sections and the reservation (fe946c9). Results file updated.
- 2026-11-03 ~14:40: P3 integrated, from the P3 reader subagent (Claude Opus 5.5 high).
  - [p3-comparison.md](p3-comparison.md); 1 new record (xu-sima-1993); 11 addenda; P3 blocks in proposed-record-changes.md; [bib/bivariate-lanczos.bib](bib/bivariate-lanczos.bib).
  - Xu Trans. AMS 343/342 were blocked by the AMS bot check and moved to DOWNLOADS v3 (A16–A19).
  - Extracted PDF text is kept off-repo. The shared browser tab was closed after all readers finished.
- [report.md](report.md) written. Step outputs complete; handoff 01 is closed in the next commit, which opens handoff 02 (Codex audit).
- Handoff 01 closed (done in 821a03e). [Handoff 02](handoffs/02-audit.md) opened: Codex gpt-6-astra high audit. Stage → AUDIT.
- 2026-11-03 14:38: AC supplied Xu, Trans. AMS 343 and 342, and Dunkl–Xu Ch. 3 (DOWNLOADS v4).
  - The audit had not started, so Claude read them before the audit (pdftotext). 3 addenda; P3 memo supplement (PD-T057 verdict unchanged, IMPLIES PART, now with primary locators; priority wording D revised); registry blocks; report updated.
  - Handoff 02 is superseded by handoff 03, which carries the new input head.
- [Handoff 02](handoffs/02-audit.md) superseded by [handoff 03](handoffs/03-audit.md): Codex gpt-6-astra high audit at input head f1007d3.

## 2026-11-05 — Codex — audit 01 of handoff 04

- Requested model/effort gpt-6-astra high; serving identity/effective effort not independently exposed. Role: independent auditor of Claude development. Rules read at full head `890f56ccde35431b70b43141c224b0b8817fea7f`; scientific input `a6302fb59f7b24242ca3b850fdd78c15753878b6`; original base `440d1079e42c3ef21c40d1cf8870f5b206410c6a`.
- [audit-01.md](audit-01.md): CHANGES REQUESTED, six P2 findings (corner attribution bridge, Theorem9 powered hypothesis, scoped rates wording, Möller dimension term, bivariate-downdating absence scope, Laurie/version reconciliation). Findings are recorded without editing developer files.
- Bounded primary-source review by four inherited-configuration readers; full state/IDEAS.md read across P1/P3 readers. Detailed sources, queries and coverage in audit-support/. Mandatory unavailable journal/theorem/image/Crossref checks remain explicitly incomplete. No substitute acceptance claimed.
- Independently reran SVZ floating-point checker (Python3.12.14/NumPy2.3.5); values reproduced and agree with the author preprint Table1. Literal checker:60 Old blocks, zero missing at base440d107; appends/full application not certified. Small receipts and complete fetched-file identities in check/audit-*.json; checker code committed. No third-party PDFs/text extracts committed.
- Shell Git fetch failed connecting to configured proxy8080; used GitHub connector pinned reads/publication. Current main refreshed to `21dbfc90257b952d8923f6d01739d12aa8d6e0a1`, three commits beyond the audit base; reconcile in the developer response before further development/preparation. Audit remains pinned to unchanged source head.
- Fresh main/open-PR21/22/24 registry/ledger scan: unchanged LIT482–561 remains disjoint through593; all returned closed PRs merged. No range or final ID assigned; scientific registries unchanged.
- Stage → WORK. [Handoff05](handoffs/05-response.md): Claude response, propagation fixes, current-main reconciliation and return to independent Codex review after material edits.
