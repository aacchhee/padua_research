# Handoff 03 — padua-literature-20261103 — independent audit of the literature campaign

- Status: open
- Previous handoff: 02-audit.md (superseded before any audit work; see LOG)

- Next agent / model / effort: Codex, gpt-6-astra, high. This is Codex auditing Claude development. Use xhigh only for a disputed priority verdict, with a written justification.
- Role: independent auditor
- Branch: claude/padua-literature-20261103
- Input head SHA: `f1007d36bc752f36d5dd969936970153509197d8` (step outputs, including the 14:50 P3 supplement). The commit that publishes this handoff comes after it.
- Main / base: `440d1079e42c3ef21c40d1cf8870f5b206410c6a`
- Stage: AUDIT
- Written by / date: Claude, claude-opus-5-5 high · 2026-11-03 (replaces 02 with the new input head)
- Draft PR: [#21](https://github.com/aacchhee/padua_research/pull/21). Reservation: LIT-482–561, first pushed in fe946c9.

## Task

Audit the literature work of handoff 01, plus the P3 supplement recorded in LOG at 14:38/14:50, at the input head and write `topics/padua-literature-20261103/audit-01.md`.

This topic makes NO mathematical claims and changes no PD statuses. Its claims are literature claims:
- citations and DOIs;
- what each source states, where, and under which hypotheses;
- one verdict per (our result, closest published statement): SUBSUMES / IMPLIES PART / RELATED, DIFFERENT SETTING / "no matching result found in the documented search";
- the proposed priority wording;
- the proposed registry corrections.

Check, in this order:

1. **Priority-critical P1 verdicts** ([p1-comparison.md](../p1-comparison.md)).
   1. Corner-argmax statement. Re-read the two primary sources at the cited locators and confirm they state the corner property as a conjecture or observation and give no proof:
      - [CDMSV 5ECM poster 2008](https://www.math.unipd.it/~marcov/pdf/poster5ecm.pdf), Conjecture box;
      - [De Marchi, CMA 5 (2022)](https://dergipark.org.tr/en/download/article-file/2240064), §3.3(2), p. 23.
   2. Search independently for any published proof of a corner argmax for Padua (or Lissajous–Chebyshev) Lebesgue functions. Use your own queries, record them, and report hits or the absence of hits within your search scope.
   3. Leading corner term. Confirm or refute the IMPLIES PART translation in the PD-T156/157 row:
      - [Kuznetsova 1995](https://doi.org/10.1007/BF01056716), Thm 1, p. 259 (Russian original free at the [UMJ archive](https://umj.imath.kiev.ua/index.php/umj/article/view/5406));
      - KL 2021 Thm 2.1, the p. 4 Padua sentence, Lemma 3.6, and §4 (4.5)–(4.6), as used for the lower bound near the corner.
   4. Confirm the "no matching result" verdicts for PD-T101 and PD-T158 against your own search.
2. **P2** ([p2-comparison.md](../p2-comparison.md)).
   - SVZ 2008 eq. (25): confirm that the journal page (p. 417, Springer [10.1007/s11075-008-9203-x](https://doi.org/10.1007/s11075-008-9203-x)) prints the misprint.
   - Rerun `python3 -I topics/padua-literature-20261103/check/svz_table1.py` independently, or write your own check, and compare with SVZ Table 1 (p. 421).
   - Check the PD-T106 IMPLIES PART split, i.e. what is published versus ours.
3. **P3** ([p3-comparison.md](../p3-comparison.md)). Spot-check at least:
   - the Greenbaum Thm 1′ two-branch resolution of LIT-213 (p. 51; AC copy `Downloads\padua\papers\1-s2.0-0024379589902851-main.pdf`, or the [DOI](https://doi.org/10.1016/0024-3795(89)90285-1));
   - the Zhu–Nakatsukasa v2 Remark 5.1(5), p. 20, which withdraws the earlier F9;
   - the PD-T057 IMPLIES PART row;
   - the reading (E) vs (G) distinction used to keep the √ε rate apart from the O(ε) 1-D rates;
   - the P3 supplement (`addenda/xu-tams-1994-operator.addendum.md`, `addenda/xu-tams-1994-blockjacobi.addendum.md`, `addenda/dunkl-xu-2014.addendum.md`, and the addendum at the end of p3-comparison.md). AC copies: `Downloads\padua\papers\S0002-9947-1994-1169912-X.pdf`, `S0002-9947-1994-1258289-7.pdf`, `general_properties_of_orthogonal_polynomials_in_several_variables.pdf`.
4. **P4** ([p4-memo.md](../p4-memo.md)).
   - Check the LIT-347/119, LIT-346, LIT-118 and LIT-420 corrections against the sources.
   - Confirm that no IDEA was registered and that the three joint questions are labelled as proposals only.
5. **Records and proposed changes.**
   - Sample at least 8 of the new or addended records (`literature/records/*.md` added on this branch; `addenda/`). Check coverage honesty: pages read, OCR-only flags, UNCONFIRMED constants (e.g. Pimenova Thm 1). Confirm there are no verbatim passages over 15 words.
   - Check that [proposed-record-changes.md](../proposed-record-changes.md) blocks are literal and apply to base `440d107` (a dry-run check is enough). Check that no shared file was edited on this branch: compare `git diff --stat 440d107..f1007d3` with the scope limits below.
6. **Links.**
   - Sample at least 10 DOIs in [DOWNLOADS.md](../DOWNLOADS.md) and the `bib/` files against Crossref.
   - Confirm no link is guessed: author and arXiv links resolve, and publisher page URLs come from Crossref.
7. **Reservation.** Recheck LIT-482–561 against current main and open PRs (#19, #20 and any new ones) under the WORKFLOW fresh-range procedure.

## Read first

- AGENTS.md, agents/WORKFLOW.md and agents/codex/CODEX.md at the input head.
- Topic files: [LOG.md](../LOG.md), [handoffs/01-work.md](01-work.md), [report.md](../report.md), the four pack memos, [DOWNLOADS.md](../DOWNLOADS.md), [ALLOCATIONS.md](../ALLOCATIONS.md), [inventory.md](../inventory.md), [check/README.md](../check/README.md).
- literature/INDEX.md and CORPUS.md. This audit carries novelty and priority verdicts, so per WORKFLOW the audit must read the complete state/IDEAS.md (no ideas were added; confirm that).
- Merged context named in handoff 01's "Read first". In particular, `topics/padua-proof-attempts-2-20261101/audit-01.md` F6 and `topics/programme-ideas-20261031/checks/adversarial-gen4-2.md`, which already met De Marchi 2022 secondarily.

## Scope limits

- Audit only.
  - Do not edit development files, records or proposed changes. Findings go into audit-01.md.
  - Do not apply proposed-record-changes and do not assign final IDs.
- Never commit third-party PDFs or extracts; the repository is public.
- Never bypass a captcha or bot check. ScienceDirect, SIAM and AMS pages may block automated access. Use AC's copies in `Downloads\padua\papers` if your environment can reach them; otherwise record the item as not rechecked.
- This topic's write scope is `topics/padua-literature-20261103/`, `results/padua-literature-20261103.md` and new topic-owned `literature/records/*.md`.
- Never commit to main, merge, force-push, create tags or touch .github/. Only AC merges.

## Acceptance and outputs

- `audit-01.md` contains:
  - auditor, model and effort;
  - the audited SHA;
  - files and novelty scope read, including the full-IDEAS read statement;
  - the searches you ran;
  - the reruns actually executed, with commands and outputs;
  - findings by severity, with file and line locations and evidence;
  - per-pack dispositions;
  - remaining uncertainty.
- Update the PR #21 body's AUDIT section from PENDING to your result, and add a LOG entry.
- Commit the audit. Then, in a following commit, set this handoff's status to `done in <audit-commit-sha>` and open handoff 03:
  - if there are findings: Claude response (`Claude (Opus 5.5 high): Continue claude/padua-literature-20261103.`), which writes response-01.md;
  - if the audit is accepted: PR preparation by Claude, which applies proposed-record-changes with the final-ID mapping into LIT-482–561, updates RESULTS.md and the ID crosswalk, and requests AC's merge decision.
