# Handoff 35: answer audit-06 (wording batch), then wait on AC's open decisions

- Status: done in 8b1a6b5301c37a9fe5cfd966454f7df4aa9600bb
- Previous handoff: 34-claude-audit-response05.md
- Next agent / model / effort: Codex, gpt-6-astra high coordinator; Sol medium for TeX edits, a distinct Astra high agent for the focused re-check.
- Role: orchestrator and developer
- Branch: codex/padua-argmax-bridge-20261105
- Input head SHA: `df5154b0799656927a4befeaab5514c459a245aa` (audit-06 outputs; MINOR addenda at `b32370e`); this handoff is the following handoff-only commit
- Main / base: `b5388c25a2a5ccb8d0faf816ab87023cf347bcd3`, merged
- Stage: WORK for the wording batch; the topic is not ready (open AC decisions below)
- Written by / date: Claude. Orchestrator `claude-sonnet-5-5`; audit work by three Claude Opus 5.5 subagents instructed at xhigh (disclosure in audit-06.md). · 2026-11-13

## Authority

Working-branch pushes stay authorized. No main push, merge, force-push, tag, settings or `.github` change, no external contact or submission, no PR readiness. Only AC merges. AI declaration,
ORCID, contributions and the draft marker are AC's. P1–P4 and the funding confirmation stand. No native campaign, regeneration of missing witnesses, retry, rescue, threshold change or final-ID
assignment. Do not remove another topic's evidence or invent a cold-storage destination.

## Read first

AGENTS.md, agents/WORKFLOW.md, agents/codex/CODEX.md at the current head (record the SHA); this handoff; [audit-06.md](../audit-06.md) and the reports in [audit-06/](../audit-06/).

## Task: one paired wording batch (new freeze), then a focused re-check

Audit-06 found no BLOCKING or MAJOR finding. The remaining items are TeX edits (a new paired TeX/Bib commit, `FINAL_BASELINE` update in a separate commit, rebuild, `check_correspondence.py`,
`--archival`, `check_baseline_controls.py`, nine mutation types and the rename-aware scanner with an updated map) or evidence-status wording, so they go together:

1. **M6-01** write w_r wherever the row half-amplitude is meant (companion comparison 2270–2274, paper 1006–1009), consistent with the companion's section 4.2 symbol table (line 1468 assigns w = r·pi + b);
   remaining local reuses (tau as Q_tau subscript, chi, bare eta, vartheta_m vs vartheta) and the paper's missing amplitude-phase reason at 588 (M6-10).
2. **M6-02** the paper points to "the expanded companion" (certification 413–416) without identifying or citing it; identify it in the data statement or bibliography and refer to it in plain text.
3. **M6-03 (material for review)** custody sentences (paper certification 505–517, companion 1624–1635): define or remove the project terms ("canonical onset-512 return archive", "evidence bundle", "data-only
   checks"); resolve the ambiguity of "the four witnesses at degrees 320, 384, 458 and 510" (two witnesses per degree) and the fact that degree 458 is listed both as re-executed and as open; say plainly that
   Proposition 5.3 at 320..510 rests on recorded runs whose outputs cannot currently be re-examined.
4. **B6-01/B6-02** the Table 2 provenance sentence (underfull badness 10000, paper `comparison-unified.tex` 1873, companion 4138; the paper's Table 2 floats to the top of p. 43 after the section 4.4 heading) and the
   companion-only "Returning to the comparison outputs" array (`localization-unified.tex` 357–366; use `l@{\quad}l@{\quad}l`); **M6-05..M6-07** the period before "where" in `ul:charts` (paper localization 35, companion 97),
   the midpoint-bound citation at companion corner 1203, the verbless sentence at paper comparison 1004–1006, the redundant "both recorded certificate records"; B6-05 optional (the white box in Figure 2 hides a short
   segment of x + y = pi); B6-08 rephrase "in/retained by the reproducibility package" when the data statement is finalised; M6-08 optionally expand the cosine-cancellation clause.
5. Optional code and recipe items: **E6-02** a subnormal-operand probe (`[2^-1074]*[2]` must be 0x2) so DAZ alone is detected, or say so in J03's scope sentence; **E6-03** state that storage receipts are checked only for
   internal consistency; **E6-04** add misplaced lock/receipt controls and a deps-branch case to the committed regression, and list the root/release/script relocation in the campaign README's adapter list; **M6-11** a committed
   command that reproduces the 60 table values (check.py returns 8 of 15 quantities). Any change to code gives a new identity: record it and re-review.
6. **E6-06 / B6-03** a careful manual pass for the dropped spaces between words and numbers or SHAs in new record text ("Code checkpoint074c7da", "at58/152pages", "is3f903e62", "alone9,733,758bytes") in
   `pr-update-20261113.md`, `response-05.md`, the results file, BUILD/README sections, handoff 34, the deposit README and the LOG; do not use an automated substitution that could corrupt SHAs.
7. Commit the one-entry incremental rename map or document how to derive it (B6-04). Write `response-06.md` with one disposition per finding; update `pr-update-20261113.md` (audit-06 result, the open items).

## Open decisions for AC (not yours to decide)

1. The global generated-output budget: union 11,734,394 B, bound 11,756,141 B against 10,000,000 B; main alone 9,733,758 B, this topic's share 2,000,636 B. Cap exception, storage destination or reducing the share.
2. The canonical `onset512-return-20261108.zip` and the I25 bundle (or confirmation that they are lost), the custody of the 632 MiB native histories, the historical PDF bytes.
3. The post-repair snapshot and the Zenodo DOI for the data statements; the AI declaration (still omits Claude Sonnet 5.5) and the draft marker.
If the canonical ZIP arrives, Claude runs the preregistered checks in audit-04/WHEN-INPUTS-ARRIVE.md after reviewing the current reader; if the I25 bundle is lost, state in the records that the 320/384/458/510 data-only checks remain OPEN.
Do not claim that a regenerated artifact is the missing historical ZIP.

## Frozen

E01–E15, J01..J03, the finite theorems and certificates, the hybrid engine freeze `0d9ce0a5…`, the compact return, the old artifacts and freezes (24a98db, ad908acb, 8937d3b in Git), all audit reports. Do not edit earlier audits.

## Publication

At the session boundary commit outputs first; then, in a separate commit, close this handoff as `done in <sha>` and open the next numbered handoff; exactly one stays open while work remains. PR 27 stays a draft;
edit its record yourself. Topic readiness is not offered while AC's decisions above are open.
