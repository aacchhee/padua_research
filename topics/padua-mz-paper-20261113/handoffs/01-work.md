# Handoff 01 — padua-mz-paper-20261113 — finalize the MZ manuscript

- Status: open
- Previous handoff: none (new topic)

- Next agent / model / effort: **Claude** (a new Claude thread).
  - Orchestrator and mathematical writing: Opus 5.5 xhigh.
  - LaTeX mechanics, build, bibliography and correspondence tooling: Sonnet 5.5 high.
  - Mechanical edits: Sonnet 5.5 medium.
  - Internal referee reviews: separate Opus 5.5 instances that did not write the section they review.
  - This follows AC's standing preference: development subagents on Sonnet, reviews on Opus.
- Role: orchestrator and developer (manuscript)
- Branch: claude/padua-mz-paper-20261113
- Input head SHA: `b5388c2` (main; this branch adds only BRIEF.md, this handoff, LOG and the results stub)
- Main / base: `b5388c2` (PR #29 rules)
- Stage: WORK
- Written by / date: Claude, claude-opus-5-5 · 2026-11-13

## Goal

Turn `tracks/mz-constants/paper/manuscript.tex` into a **submission-ready manuscript for AC's decision**:
- integrate the PR #31 sharp-constant results at their exact scopes;
- restructure around the new headline results;
- resolve the literature placeholders that predate PR #21;
- meet AC's manuscript criteria.

Read [BRIEF.md](../BRIEF.md) first. It holds the current state (§1), what to integrate (§2), the literature status (§3), the criteria (§4), the decisions reserved for AC (§5) and the pitfalls (§6).

## Tasks, in order (parallel where marked)

0. **Setup.**
   - Read the rules at the branch head and record the SHA.
   - Build the current manuscript (pdfLaTeX, BibTeX, pdfLaTeX twice) in scratch and record pages, warnings and hashes.
   - **Send AC the BRIEF §5 questions in one short message.** Continue on the defaults; do not wait.
1. **Correspondence table**, `correspondence.md`. For every theorem, lemma, proposition and corollary that is or will be in the paper, record:
   - the label;
   - the final PD ID;
   - the record's status and exact scope;
   - "in paper: verbatim / weakened / omitted".

   Every PROVED statement in the text must match its record. Nothing OPEN or MEASURED may appear as proved.
2. **Restructuring plan**, `plan.md`. Write the new outline (abstract, introduction with the main theorems stated up front, then the sections and appendices), with the target length and the location of each result. Get it reviewed by one Opus reviewer before large edits.
3. **Integration**, in parallel by section, with disjoint section ownership:
   - **§2:** add the uniform 5/3 theorem (PD-T526), the η_N bounds (PD-T527), and the CC upper limit with its operator identification and finite brackets (PD-T530/531, with the definition material of PD-T528/529/548 and the one-sided PD-T547).
   - **§3:** culminate in the sharp limit π⁴/8 (PD-T546/523/522). Keep the existing PD-T017/018 bounds as the explicit finite results.
   - **§6:** add the corner operator B and the signed logarithmic limits (PD-T534/535/536/540/544/545), the certified enclosure with its honest "no useful digits" caveat (PD-T541/542), and the carrier improvements (PD-T533/537).
   - **§7:** rewrite as "Open problems". It covers the decimal values of Λ_edge and of spec(B)'s extremes; effective onsets; anything else genuinely open. Optionally add measured tables, clearly labelled.
   - Move long proofs to appendices where that helps the line of argument. Keep the derivations and worked examples.
4. **Abstract, introduction and conclusion.** Rewrite them around the exact constants. State the main theorems in the introduction, with their scope.
5. **Literature pass.**
   - Resolve every pre-PR #21 hedge using `p2-comparison.md` and the LIT records. Cite only what has fulltext-read LIT coverage at the cited scope.
   - Update `refs.bib`, using the MathSciNet citation-check note as a starting point.
   - Give AC clickable links for any unread item the text needs.
6. **Notation register** (`notation.md`) and a consistency pass. Every symbol must be defined before use, with one meaning, matching between text, appendices and tables.
7. **Data and code availability.** Write an accurate statement naming the committed checkers and receipts for every computer-assisted part, at the actual commit. Make no deposit claim unless AC creates one.
8. **Internal referee round.** Two distinct Opus reviewers:
   - **(a) mathematics:** re-derive or spot-check every changed statement and proof against its record;
   - **(b) exposition and notation:** check against AC's criteria.

   Answer their findings in `response-internal.md`.
9. **Final build and records.**
   - A clean build: zero errors, warnings or undefined references, and no unexplained overfull boxes.
   - Record pages, source and PDF hashes in the M7 manuscript record (append only).
   - Update the paper README scope table.
   - Prepare the PAPER_MAP and state/CURRENT.md updates for PR preparation. Fix PAPER_MAP's stale "No manuscript has been drafted" header.

## Gates

If a criterion proves ill-posed, record why and add a new criterion as a separate dated entry.

- **W0, baseline.** The current manuscript builds cleanly and matches its last recorded page count, 25 ± 1 pages. **Kill:** a broken baseline must be fixed first and recorded.
- **W1, correspondence.** Before the final build, every numbered statement has a correspondence row. Each PROVED row is verbatim or explicitly weakened. No OPEN or MEASURED item is stated as proved. **Kill:** any mismatch blocks the final build.
- **W2, scope.** The decimal values of PD-T027 and PD-T381 appear only as OPEN. The first-crossing language follows PD-T376. Fits are labelled MEASURED.
- **W3, citations.** Every `\cite` resolves to a refs.bib entry with LIT coverage at the cited scope, or carries an explicit coverage note in `literature-mz-paper.md`.
- **W4, build.** A clean final build, and an independent rebuild by a different subagent with the same page count.

## Read first

- AGENTS.md, agents/WORKFLOW.md, agents/claude/CLAUDE_ROLES.md at the branch head.
- [BRIEF.md](../BRIEF.md).
- `tracks/mz-constants/paper/`: manuscript.tex, refs.bib, README.md.
- `topics/mz-constants/directions/M7/manuscript-record.md`.
- `topics/padua-mz-sharp-constants-20261106/`: report.md, manuscript-insert.md, theory/ (all records behind PD-T522–548), the audits and responses.
- `topics/padua-mz-cleanup-20261105/` and `topics/padua-mz-2d-frontier-20261105/`, for the signed-Padua records already in the paper.
- `tracks/mz-constants/theory/` (the PD-T013–027 records).
- `topics/padua-literature-20261103/`: p2-comparison.md, notes/mathscinet-citation-check-2026-11-05.md. Also `topics/mz-constants/literature-search.md`, `literature-response-01.md` and `literature/INDEX.md`.
- PROOF_STATUS rows PD-T013–028, PD-T106–117, PD-T294–300, PD-T376–381, PD-T522–548 and PD-N004, N044–053, N104–107.

## Scope limits

- **Where to write.**
  - Inside `topics/padua-mz-paper-20261113/` and `results/padua-mz-paper-20261113.md`.
  - `tracks/mz-constants/paper/manuscript.tex`, `refs.bib` and `README.md`.
  - `topics/mz-constants/directions/M7/manuscript-record.md` (append only).
  - Shared registries (PAPER_MAP, state/CURRENT.md) only at PR preparation, edited directly and reviewed by diff.
  - Do not write to any other open branch: PR #27, PR #34.
- **New mathematics.** None is expected. If a gap needs a new lemma, record it as its own theory file with a provisional ID `PD-T?mz-paper-claude-NN`, get an independent check, and flag it for the Codex audit. Never silently strengthen a statement in the text.
- **No PDFs, extracts or bulk data committed.** Build outputs stay in scratch or `local-output/`, which is ignored. The repo is public: never commit third-party fulltexts.
- **Literature.** Open any legally accessible literature without asking per link (AC standing authorization). Cite only after a fulltext read. Do not bypass captchas or bot checks.
- **Reserved to AC.** The AI declaration, ORCID, contributions, funding text, cover letter, venue, submission and any external contact. Do not create a Zenodo deposit.
- **Compute.** Sandbox only. No new numerics are expected beyond rebuilding and reproducing table entries from committed receipts.
- **Commits** are authored as Andrey Chesnokov <aacchhee@gmail.com>, with trailers `Agent: Claude` and `Model: <exact model and effort>`, plus the session's Co-Authored-By and Claude-Session lines. Never commit to main, merge, force-push, create tags or touch .github/. Only AC merges.

## Acceptance and outputs

- **Files.**
  - The revised `manuscript.tex` and `refs.bib`.
  - `correspondence.md`, `plan.md`, `notation.md`, `literature-mz-paper.md` and `response-internal.md`.
  - LOG.md, `results/padua-mz-paper-20261113.md` and `report.md`.
  - The `report.md` contains:
    - the new outline;
    - page count and hashes;
    - the correspondence summary;
    - what is OPEN in the paper;
    - AC's answers or the defaults used;
    - the list of items reserved for AC.
- **Pushes and PR.** Push at every task boundary, and at least every ~10 minutes while something has changed. Open a draft PR early.
- **Closing.** When done, commit the outputs. Then, in a following commit, set this status to `done in <sha>` and open handoff 02 for the single substantive audit by **Codex, gpt-6-astra high or higher at its choice**: Codex audits Claude development. That audit covers the mathematics-to-text correspondence, exposition against AC's criteria, citations and the build. Novelty: not applicable unless new lemmas or priority claims were added. Reply to AC only with `Codex (gpt-6-astra high): Continue claude/padua-mz-paper-20261113.`
