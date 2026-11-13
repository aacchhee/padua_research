# MZ paper finalization (MZ-CC and MZ-SP): log

- Branch: `claude/padua-mz-paper-20261113` · Base: main `b5388c2` · Developer: Claude · Auditor: Codex (gpt-6-astra)
- Stage: WORK · Draft PR #35 · Next: `Claude (Opus 5.5 xhigh): Continue claude/padua-mz-paper-20261113.` · Open handoff: [handoffs/03-work.md](handoffs/03-work.md) (01, 02 superseded)
- Reserved final-ID ranges: none (no new mathematics expected).
- Decided by AC: venues (MZ-CC SINUM, MZ-SP JAT); Zenodo later; companion = AC-only reading aid, arXiv and journal versions identical (2026-11-13).

## 2026-11-13 — Claude, claude-opus-5-5 (configured; effort not exposed) — topic setup

- AC: "make a brief for a thread to finalize MZ paper".
- Rules read at `b5388c2`. Branch created from main `b5388c2`. Only BRIEF.md, handoff 01, this LOG and the results stub were added.
- BRIEF contents:
  - the manuscript today (25 pages, sections, scope);
  - the PR #31 results to integrate (PD-T522–548: π⁴/8 limit, uniform 5/3, Λ_edge operator limit, signed Padua corner-operator limits), with exact OPEN parts;
  - the literature state after PR #21;
  - AC's manuscript criteria, as recorded in the argmax-manuscript audit brief;
  - reserved decisions and pitfalls.
- No manuscript edit was made, no build run and no claim made.

## 2026-11-13 — Claude, claude-opus-5-5 (configured; effort not exposed) — split decision

- AC asked whether to split; Claude recommended it. AC: "yes let's split. call the one MZ-CC and another one MZ-SP".
- BRIEF §0 (new) and handoff 01 were amended in place before any work began:
  - **MZ-CC** (Clenshaw–Curtis) stays in `tracks/mz-constants/paper/`. It takes current §2–§5 plus PR #31's CC results (π⁴/8, 5/3, η_N, Λ_edge).
  - **MZ-SP** (signed Padua) goes in a new `tracks/mz-constants/paper-sp/`. It takes current §6 plus PR #31's corner operator results, and cites MZ-CC.
  - MZ-CC is finished first.
  - A new task 0a splits the draft with a `split-map.md` (gate W0). Correspondence, plan, notation and response files are now per paper.

## 2026-11-13 — Claude, claude-opus-5-5 (configured; effort not exposed) — venues

- AC: "let's decide on venues now. zenodo will come later."
- AC's choices, from Claude's recommended options:
  - **MZ-CC → SIAM J. Numer. Anal.** (fallback Math. Comp.);
  - **MZ-SP → J. Approx. Theory** (fallback Adv. Comput. Math.).
- BRIEF §0/§5 and handoff 01 task 0 were amended in place: journal classes `siamart` and `elsarticle`, a deposit-DOI placeholder, and only the companion question left for AC.

## 2026-11-13 — Claude, claude-opus-5-5 (configured; effort not exposed) — task 0 / 0a: baseline and split

- Rules read at branch head `c0e57a9c` (AGENTS.md, agents/WORKFLOW.md, agents/claude/CLAUDE_ROLES.md). main is still `b5388c2`; open PRs #27 and #34 are not touched. Role: orchestrator and developer (manuscript).
- **AC answers (2026-11-13):**
  - companion document: "companion document may be prepared only for my own reading, arxiv and journal should be the same". So the arXiv and journal versions of each paper are identical; long derivations go into each paper's appendices. Any companion is a private reading aid for AC, not submitted or posted;
  - then: "companion paper should follow the same rules as companion in padua argmax paper". The rules are summarized once in [BRIEF §5](BRIEF.md) item 3; one companion per paper, written after that paper's text freeze;
  - SIAM class files: "you can put them on repo". `siamart251216.cls` (v1.4.8, 2025-12-16) and `siamplain.bst` are committed in `tracks/mz-constants/paper/`. SIAM's class is not on CTAN; it was taken from public GitHub copies (dpo/latex-styles and danieleavitabile/project-starter, byte-identical class, SHA-256 `33f2eb09…a5c6f5`; bst `a5df7c48…c6ac7`). Check against SIAM's official macro download before submission.
- Toolchain installed in the sandbox: `texlive-publishers` (for `elsarticle`).
- **Baseline (task 0):** the single draft builds cleanly at 25 A4 pages, source hash equal to the 2026-11-05 record.
- **Split (task 0a):** done by script; exact changes and the statement map are in [split-map.md](split-map.md). MZ-CC post-split 16 pp., MZ-SP 11 pp., both clean. Gate W0 PASS. Class conversion follows as a separate commit.

## 2026-11-13 — Claude, claude-opus-5-5 — class conversion, plans, first MZ-CC integration

- Class conversion: a Sonnet 5.5 high worker did it; the orchestrator verified it by its own rebuild (`aed79fd`). Details are in split-map.md.
- Plans and correspondence tables written (`761e884`). Two Opus 5.5 high plan reviewers are running: review-plan-cc.md (it also independently checks the provisional corollary) and review-plan-sp.md.
- **New provisional claim:** PD-T?mz-paper-claude-01 ([theory/cc-defect-condition-corollary.md](theory/cc-defect-condition-corollary.md)). It gives the sharp defect limit (log N)²(1−η_N)→π⁴/8, κ₂(G_N)/(log N)²→8Λ_edge/π⁴, and the hyperinterpolation factor (1+√(5/3))√2. It is a two-line consequence of PD-T526/527/530/546/547/025. Flagged for the Codex audit.
- **BRIEF erratum:** BRIEF §0/§2 list PD-T544/545 among the signed Padua results. They are the CC signed-remainder and discrete-primitive lemmas behind π⁴/8 (P3), and they go to MZ-CC. MZ-SP uses PD-T534/535/536 and PD-T539–542.
- MZ-CC restructured, and PD-T526/522/523/544/545/546 integrated with Appendix A (proofs). Builds clean at 23 pp. (siamart). §5 (Λ_edge) is a stub. One proof-route change for PD-T523 is recorded in correspondence-cc.md.

## 2026-11-13 — Claude, claude-opus-5-5 — §5, reviews, session boundary

- MZ-CC §5 and Appendix B (`c41d409`): PD-T529 is stated weakened (qualitative), PD-T530 verbatim. The PD-T526 matrices H,K are renamed Y,Z. Builds clean at 28 siamart pp.
- Plan reviews: [review-plan-cc.md](review-plan-cc.md) (no BLOCKING; M1–M3 accepted) and [review-plan-sp.md](review-plan-sp.md) (F1, F2, F7, F11, F12 MAJOR; F13 blocks submission). Dispositions are at the end of each plan.
- PD-T?mz-paper-claude-01: check PASS with corrections ([check-cc-defect-corollary.md](check-cc-defect-corollary.md)). Applied: onset N≥57 via PD-T019 (exact rational check N=2…399 run by the orchestrator, proof for all N); the computer-assisted note for the numeric interval; the (c) threshold. Part (d), the interpolation norm, was added after the check and is not yet checked independently.
- Draft PR #35 opened. Tools `tools/build.sh` and `tools/split.py` committed.
- Questions pending with AC: plan-sp F2 (self-contained SP appendix vs MZ-CC on arXiv first) and F13 (public witness arrays). Defaults are in handoff 02.
- Session boundary: handoff 01 superseded by [handoff 02](handoffs/02-work.md).

## 2026-11-13 21:28 — AC answers to the handoff-02 questions

- AC: "1. mz-cc first, mz-sp cites. 2. I guess they go to zenodo".
  - plan-sp F2: MZ-CC goes out first, and MZ-SP cites it for λ₊<2 and the other CC inputs. No reproduced proof.
  - plan-sp F13: the PD-T376 witness arrays go into AC's Zenodo deposit. Prop 8.1 stays, with the deposit-DOI placeholder.
- Handoff 02 superseded by [handoff 03](handoffs/03-work.md), which carries these changes. No manuscript change.

## 2026-11-13 — Claude, claude-opus-5-5 — handoff 03: MZ-CC completed to draft

- Rules: unchanged since `c0e57a9`; main still `b5388c2`.
- MZ-CC (`34b9315`, `604e667`, `767f5d7`, then this commit) contains every result in plan-cc, with proofs:
  - PD-T547 and Appendix C (PD-T548);
  - the U lemma moved to §4.1;
  - the interpolation-norm corollary;
  - Cor 6.1 (defect, condition number, N≥57);
  - B=min{1+ρ,5/3};
  - new §9 (measurements and open problems);
  - new title, abstract and introduction with Thms 1.1–1.3 and Cor 1.4;
  - LIT-511 sentence (Mastroianni–Russo 2000, from the PR #21 reading);
  - data and code availability with placeholders for commit and DOI;
  - bibliography reading-coverage notes moved out of print (`coverage` field).

  The status box is removed, and in-heading IDs are now TeX comments. Clean build, 30 siamart pp. Statement numbering is a freeze candidate.
- Independent checks (Opus 5.5 high): [check-new-corollaries-02.md](check-new-corollaries-02.md) returns PASS with editorial corrections for PD-T?mz-paper-claude-01 (d) and PASS for PD-T?mz-paper-claude-02. Record fixes are applied: the λ₋(N,N) definition, the Π_N dependency and the J₋ pointer.
- Notation register [notation-cc.md](notation-cc.md) (Sonnet 5.5 high worker): 38 clash entries (10 H, 15 M, 13 T). The stale "H and K" at old l.571 is fixed. The other renames are left to the next session's notation pass.
- [literature-mz-paper.md](literature-mz-paper.md): coverage table drafted for MZ-CC's 26 keys; the per-sentence scope check is pending.

## Runs needed

- Remaining tasks and gates W1–W4: see handoff 02.
