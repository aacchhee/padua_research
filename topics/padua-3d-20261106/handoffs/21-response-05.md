# Handoff 21 — padua-3d-20261106 — focused response-05 to audit 05, then PR preparation

- Status: open
- Previous handoff: [20-final-narrowed-audit.md](20-final-narrowed-audit.md)
- Next agent / model / effort: **Codex**, coordinator gpt-6-astra high.
  - Mathematical wording for H1/H2: gpt-6.1-sol high.
  - Record work: gpt-6.1-sol medium.
- Role: developer and orchestrator.
- Branch: `codex/padua-3d-20261106`.
- Input head SHA: `23333c9946bbee02252664d358415197e1d7ab9f`. This is the audit-05 output: report `bc01a92`, then auditor fixes `23333c9`. The following commit publishes this file.
- Main / base: `f70a260e5b5f9a01209dc8a05faabdcf8db1feeb`. Fetch first.
- Stage: **WORK**.
- Written by / date: Claude, claude-opus-5-5 xhigh · 2026-11-12.

## Scope

This is a focused response only. **No new research, construction, optimization or proof campaign is authorized.** All directions are frozen, and the D1 two unused rounds stay unused.

Write `response-05.md`. Answer each of [audit-05](../audit-05.md) H1–H6 and each item that [audit-05-fixes.md](../audit-05-fixes.md) returns to the developer. Each answer is a fix, an evidence-based rejection or an explicit unresolved item.

1. **H1.** Make the hypothesis "all nodes in [−1,1]³" explicit in D1-04, D1-05 and paper Theorem A.
   - Locations: `final-d1/spectral-obstruction.md:9,19`, `weight-corollary.md:9-10,21`, `finite-frame.md:15`.
   - Rewrite line 19, "support geometry … otherwise unrestricted", so that it cannot be read as allowing nodes outside the cube.
   - No proof change is expected. This is a material statement edit and will get a focused re-audit.
   - Also decide on the two summary-scope items the fix subagent excluded, D5 F1 and F13 ("exact on Π_{2n−1}" or "through degree 2n−1" in summaries). Either apply them as accurate restatements or explain why not.
2. **H2.** Add the sphere and disk fixed-excess literature:
   - Yudin 1997 for spherical designs;
   - Lyubich, Thm 4.1, §5 and Prop. 5.1, for projective cubature (primary-read by the auditor);
   - Xu 2003 for positive interior Chebyshev-disk rules (search level).

   Use each source's actual coverage. Correct `final-d1/reconstruction.md:43-47` and the reason given there for why the sphere analogue fails (D1b-4). Correct `sources.md:27-35`, `gate.md:22,32` and `paper-note-draft.md:50`.

   Add the D1 attribution and partial-answer sentence to paper §2 (D1b-2). It should say that D1 is not stated in the checked literature; that it answers Li–Sun–Xu's question negatively for positive weights only, non-effectively, with page pins; that the mechanism credit goes to AMO Thm 14, Kolountzakis Thm 1 and Greenfeld–Lev Thm 1.1; and that Li–Sun–Xu's signed-weight question and n³/4 conjecture remain open.
3. **H3.** Cite Lyness, *Notes on lattice rules* (J. Complexity 2003), and Cools, *A Belgian view on lattice rules*, at their actual coverage.
   - Narrow "locally certified" for the lattice minima wherever the minima at n = 1, 2, 3, 6, 9, 12, 15 may already be known.
   - Add both to the gap lists: paper:104, outcome:30, report:19.
4. **H4.** Credit Wang–Wang–Wang 2014 (LIT-391) for the cube log³ hyperinterpolation order at paper:76 and novelty-gate:44, at its coverage level. This is item C8.
5. **H5.** Add D3 and D4 rows to the D5 novelty gate:
   - LIT-413 (minimal-cubature certificates);
   - classical degree-5 cube rules;
   - the T8 unisolvent 20-node sets;
   - the n = 1, 2 lattice packages;
   - IDEA-466, IDEA-609, IDEA-611.

   Fix the completeness sentence at novelty-gate:54.
6. **H6.** Final frontier dispositions:
   - C5: not subsumed by the non-effective D1. Decide, and give a resume condition.
   - C6: add a resume condition.
   - C8: add a disposition line.
7. **Returned MINOR items.**
   - Paper manuscript: separate the repository process text from the manuscript text, and add a bibliography.
   - D3 candidate: add the "Disposition reason" field.
   - `evidence/fd4-manifest.json` prose pins (A-M7): retire or disclose. Do not rewrite historical JSON silently.
   - A-M8: bring `audit-04/code/A1/aud_enum.cpp` (or a committed copy) under the master manifest, or disclose its coverage; record the g++ version if you can recover it.
   - A-M9: give the D2 quality-replay receipt a command and code identity, or disclose its absence.
   - A-M3 and A-M4: split-header pairs `t7-finite-reduction` ↔ T7-09, and full IDs in the n4..7 split headers.

## Then

- Commit the outputs.
- In a following commit, close this handoff `done in <sha>` and open handoff 22 for a **focused Claude re-audit** (Opus 5.5 high or xhigh, auditor's choice). It covers only the material changes: the H1 statement hypothesis, any H2–H6 disposition or attribution changes, and any manifest or ID changes.
- If that re-audit accepts, the step after it is **Codex PR preparation**: refreshed reservation check, final-ID and registry application, and one reviewed-diff readiness check. That freezes the direction.

## Scope limits

- Do not reopen accepted mathematics.
- Do not edit audit reports, fix notes, the frontier records or earlier handoff bodies.
- No final IDs or shared-registry edits before the PR-preparation stage.
- Do not touch other topics, main, tags, `.github/` or settings. Only AC merges.
- AC's 2026-11-08 decisions are settled. Do not present them as pending.
