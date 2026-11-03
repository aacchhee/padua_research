# Handoff 01 — padua-literature-20261103 — literature campaign for the new Padua results and related papers

- Status: open
- Previous handoff: none

- Next agent / model / effort:
  - orchestrator: Claude, Opus 5.5 high (xhigh for priority or novelty verdicts);
  - development subagents (inventory, DOI and link verification, bibliography, record drafting): Claude Sonnet 5.5, medium or high;
  - independent verdict reviews: Opus.
- Role: orchestrator and developer (literature)
- Branch: claude/padua-literature-20261103
- Input head SHA: the first topic commit on this branch, which adds this handoff, LOG, results stub and the SINUM assessment note (parent `440d107`; see LOG)
- Main / base: `440d107`
- Stage: WORK
- Written by / date: Claude, claude-opus-5-5 · 2026-11-03

## Task

**Goal.** Give the recent Padua results (PRs #9–#17) a documented literature footing for three paper drafts: the Padua Lebesgue function, Clenshaw–Curtis/Padua MZ constants (1-D + 2-D), and the bivariate Lanczos / V+A note. Close the open fulltext gaps, and check priority and novelty claims against what is actually published.

- This campaign is **literature only**. It makes no new mathematical claims and no PD status changes.
- A source that subsumes a result changes only the attribution and the scope of the novelty claim.

### AC's hard requirement: clickable download links

For every source whose fulltext is needed and not already available, AC must get links that open the paper directly, with no searching:
- the DOI as a clickable `https://doi.org/...` link;
- the journal's article page;
- any free version (arXiv abstract or PDF, author page, institutional repository).

Rules for the links:
- Verify each DOI resolves to the right paper (title, authors, year), for example through doi.org or the Crossref API, and record the check.
- Never give a bare DOI, a search-engine URL or a guessed URL. If no DOI exists (thesis, proceedings, old C. R. note), give the best direct page plus the full citation, and say that no DOI exists.
- In every message to AC, write links as markdown links, e.g. `[Brutman 1997](https://doi.org/...)`.

### Steps

0. **Setup.**
   - Read AGENTS.md, agents/WORKFLOW.md and agents/claude/CLAUDE_ROLES.md at the branch head, and record the SHA. Fetch main and merge it if it moved.
   - Read literature/INDEX.md, CORPUS.md and the records named below.
   - Read this topic's [SINUM assessment note](../notes/faghih-sinum-2026-assessment.md) (already done by Claude: the AC-supplied Faghih et al. SINUM 2026 PDF, read and assessed for the IEP plans).
1. **Inventory first** (Sonnet). List AC's local folders through the link to AC's computer: `~/Downloads/padua/papers` and `~/Downloads/bttb/papers`. Match each PDF to its citation (filenames are often DOIs), and cross-check with CORPUS.md and the existing records. Already-available items are never requested again.
   - If the computer is not linked, say so and ask AC to link it or attach files; continue with open-access sources meanwhile.
2. **Search and verify** (Sonnet subagents, Opus spot checks). For each pack below, find the primary sources, check access, and resolve and verify DOIs.
3. **Deliver the download list early.** As soon as steps 1–2 are done for packs P1 and P2, and before the long reading:
   - write `topics/padua-literature-20261103/DOWNLOADS.md`;
   - send AC the same table with SendUserMessage, in priority order.

   Columns:
   - priority;
   - full citation;
   - DOI (clickable);
   - journal article page (clickable);
   - free version (clickable, or "none found");
   - which repository claims it bears on;
   - exactly which sections or pages are needed;
   - local status ("have: `<filename>`" or "need").

   Update the table and resend it when it changes. Tell AC to drop PDFs into `Downloads\padua\papers` under any name, and re-inventory when AC says files have arrived.
4. **Read and record** (Opus for the verdicts). Read the fulltexts that are available or supplied. For each source:
   - write or update its `literature/records/<key>.md` entry, giving coverage (exact pages read), the statements with their full hypotheses, and page/theorem locators;
   - stay paraphrase-only: never commit third-party PDFs or extracts, since the repo is public.

   For each pack, write a comparison memo `topics/padua-literature-20261103/<pack>-comparison.md`, with one row per (our result, closest published statement). Each row gets one verdict:
   - SUBSUMES (with the translation written out);
   - IMPLIES PART;
   - RELATED, DIFFERENT SETTING (with the mismatch named);
   - no matching result found in the documented search (the only admissible negative).

   Also write a short "priority wording for the paper" paragraph per result.
5. **Bibliography.** For each paper, give BibTeX fragments with verified DOIs in `topics/padua-literature-20261103/bib/<paper>.bib`. These are fragments only; do not edit merged manuscripts.

## Packs, in priority order

### P1 — Padua Lebesgue-function paper (highest)

Our results:
- PD-T101: exact corner formula.
- PD-T156–159: corner asymptotics with explicit O(1), including the b-term and the comparison with L_n².
- PD-T161–177, PD-T183, PD-T209, PD-T214: certified maxima counts n = 3–7 and global argmax n = 2–16.
- PD-T185–192 and PD-T211/212/230: edge formula, edge envelopes and the constant g.
- PD-T229: eventual exact corner argmax.

Sources to cover:
- Padua basics: LIT-301/312/330/366; Bos–Caliari–De Marchi–Vianello–Xu 2006 and Bos–De Marchi–Vianello–Xu 2007.
- Any published statement or observation that the Padua Lebesgue function attains its maximum at a corner (numerical papers by Caliari–De Marchi–Vianello and the Padova group, Vianello's surveys).
- Kolomoitsev–Lomako 2021 (LIT-379): confirm the theorem and page locators that part 2's audit F6 flagged as unconfirmed.
- Białas-Cież–De Marchi–Suder, arXiv 2605.23299 (LIT-388): full read, plus any newer version.
- Dencker–Erb and Erb on Lissajous–Chebyshev Lebesgue constants.
- **The 1-D literature on where the Lebesgue function attains its maximum**: Brutman 1978 (SIAM J. Numer. Anal.), Brutman's 1997 survey, Günttner, Ehlich–Zeller, Rivlin, the midpoint maximality of trigonometric interpolation, and the Chebyshev-extrema case. All citations are to be verified; none has been read in this repository yet.

Coordinate: the parallel Codex campaign `codex/padua-argmax-effective-20261103` needs these 1-D sources (its gate G8). Do not write to its branch. Note in this topic's report which LIT records it can reuse after merge.

### P2 — MZ papers (1-D CC and 2-D signed Padua)

Our results: PD-T013–028, PD-N004, and PD-T106–117 with PD-N044–053.

Open gaps named in the merged reports:
- Mastroianni–Russo 2000 (Hadronic Press);
- Della Vecchia–Mastroianni–Vértesi 1995 (IDOMAT proceedings);
- Wu, Appl. Math. Lett. 182 (2026);
- the journal versions of König–Nielsen and Don–Gottlieb;
- Feldheim, C. R. 203 (1936), p. 650;
- the final journal bodies flagged in PR #14's report: Sommariva–Vianello–Zanovello (doi 10.1007/s11075-008-9203-x), Dencker–Erb (10.1016/j.jat.2017.03.003), Kolomoitsev–Lomako (10.1016/j.amc.2021.126192), Xu 1996 (10.1006/jath.1996.0102), ASV published body (10.1016/j.matcom.2026.10.001), and KLP2018 (10.1016/j.jat.2018.02.005).

Verify each DOI rather than trusting these strings.

Plus: signed-Padua cubature and hyperinterpolation sources (Caliari–De Marchi–Vianello hyperinterpolation on the square, LIT-428), and any 2-D MZ results for Chebyshev-type rules beyond half-exactness.

### P3 — Bivariate Lanczos / V+A / backward stability

Our results:
- PD-T029–080, with PD-T069 (Padua backward obstruction), PD-T058–060 (rate theorem) and PD-T075;
- PR #15's drift results: PD-T136–155 range; check PROOF_STATUS for exact IDs, including ρ_n = O(n⁻⁵) and the polyrat measurements.

Sources:
- Zhu–Nakatsukasa (LIT-361), Hokanson (LIT-360), Brubeck–Nakatsukasa–Trefethen, polyrat;
- Barrio–Peña–Sauer 2010, Liu–Narayan 2023, Huhtanen–Larsen, Xu's block-Jacobi theory;
- Greenbaum 1989 and any multivariate backward-stability or "Greenbaum-type" results.

Upgrade the many UNVERIFIED and "reported" LIT entries from PR #10 that the papers will cite.

### P4 — Leuven IEP / MOP line (for AC's IEP plans)

- Start from the [assessment note](../notes/faghih-sinum-2026-assessment.md). The SINUM 2026 paper is read; carry its record corrections for LIT-347/119 into the records at PR preparation.
- Cover the companion arXiv 2608.25758 (LIT-348; is there a published version?), Van Barel–Van Buggenhout–Vandebril 2023 (arXiv 2302.00355; resolve its author list), Faghih et al. on Sobolev ORFs (Numer. Algorithms 2025, NLAA 2025), Laudadio–Mastronardi–Van Assche–Van Dooren 2024/2025 (simultaneous Gaussian quadrature), and Filipuk–Haneczok–Van Assche 2015.
- Produce a one-page memo for AC: what the Leuven group has done since 2024 that bears on bivariate IEPs, what they list as future work, and where a contact or joint question makes sense (the assessment's points 3–4). Do not register new ideas here; propose them for a later topic.

## Read first

- Rules files at the branch head.
- literature/INDEX.md, CORPUS.md, and the records cited above.
- The merged reports:
  - `topics/mz-prior-art-20261101/report.md` and comparison.md;
  - `topics/padua-mz-2d-20261101/report.md` and literature.md;
  - `topics/padua-argmax-alln-20261101/report.md`;
  - `topics/padua-proof-attempts-2-20261101/report.md` and audit-01.md (F6);
  - `topics/bivariate-lanczos-20261031/report.md`, lit/ and reviews/;
  - `topics/padua-lanczos-drift-20261101/report.md`.
- PAPER_MAP.md.

## Scope limits

- Write only inside `topics/padua-literature-20261103/`, `results/padua-literature-20261103.md`, and new or updated `literature/records/<key>.md` files that this topic owns.
- Put changes to shared files (`literature/INDEX.md`, `CORPUS.md`, existing records owned by merged topics, PROOF_STATUS/IDEAS, PAPER_MAP, manuscripts) as literal old→new blocks in `proposed-record-changes.md`. Apply them only at PR preparation, per WORKFLOW.
- LIT IDs: provisional `LIT?padua-literature-claude-NN`. Reserve final ranges at draft PR by the fresh-range procedure, including the two open Codex branches (`codex/padua-argmax-effective-20261103`, `codex/padua-lebesgue-followups-20261103`) and their PRs.
- Novelty: this branch carries novelty and priority verdicts. Run the relaxed registry scan before each pack, and the audit must read the complete state/IDEAS.md.
- Access: AC authorizes opening any legally accessible publication page without asking each time. Do not bypass paywalls or bot checks. If ScienceDirect, SIAM or Springer blocks automated access, list the item for AC with its links instead.
- Never cite a source as establishing something unless its relevant pages were read. Otherwise it stays UNVERIFIED or pending.
- Commits are authored as Andrey Chesnokov <aacchhee@gmail.com>, with the trailers `Agent: Claude` and `Model: <exact model and effort>`. Never commit to main, merge, force-push, create tags or touch .github/. Only AC merges.

## Acceptance and outputs

- DOWNLOADS.md with verified clickable links, sent to AC early and kept current.
- Records with locators; per-pack comparison memos with verdicts and priority wording; the P4 memo for AC; BibTeX fragments; proposed-record-changes.md.
- LOG.md entries at each step; results/padua-literature-20261103.md kept current.
- A final report.md: what was verified; what each fulltext changed (per pack); what remains missing (with the same clickable links); and which merged claims need narrower wording.
- Open a draft PR to main early, with WORK / AUDIT (PENDING) / PR sections and the ID reservation.
- When done, commit the outputs. Then, in a following commit, set this status to `done in <sha>` and open handoff 02 for the audit: Codex, gpt-6-astra high, since Codex audits Claude development. Reply to AC with only `Codex (gpt-6-astra high): Continue claude/padua-literature-20261103.`
