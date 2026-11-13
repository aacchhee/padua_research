# Handoff 02 — padua-mz-paper-20261113 — continue finalizing MZ-CC and MZ-SP

- Status: superseded by 03: AC answered the pending questions (F2: MZ-CC first, MZ-SP cites; F13: the witness arrays go to Zenodo)
- Previous handoff: [01-work.md](01-work.md) (superseded at the session boundary; its task list and gates remain the reference)

- Next agent / model / effort: **Claude**, a new session.
  - Orchestrator and mathematical writing: Opus 5.5 xhigh.
  - LaTeX mechanics, build and tooling: Sonnet 5.5 high. Mechanical edits: Sonnet 5.5 medium.
  - Internal referee reviews: separate Opus 5.5 instances (high or xhigh) that did not write the section they review.
- Role: orchestrator and developer (manuscripts)
- Branch: claude/padua-mz-paper-20261113 · Draft PR #35
- Input head SHA: `c41d409` (the commit that publishes this file comes later)
- Main / base: `b5388c2`
- Stage: WORK
- Written by / date: Claude, claude-opus-5-5 · 2026-11-13

## State at handoff

Read the [LOG](../LOG.md) entries of 2026-11-13 first.

- **Done:**
  - task 0 (baseline) and task 0a (split, [split-map.md](../split-map.md), gate W0 PASS);
  - journal classes: MZ-CC `siamart251216`, MZ-SP `elsarticle`;
  - task 1 correspondence tables and task 2 plans, both reviewed by Opus, with dispositions at the end of [plan-cc.md](../plan-cc.md) and [plan-sp.md](../plan-sp.md).
- **MZ-CC** (`tracks/mz-constants/paper/manuscript.tex`, 28 siamart pp., clean build). Sections:
  - §1 old intro, not yet rewritten;
  - §2 preliminaries;
  - §3 upper spectrum, incl. Thm `thm:five-thirds` (PD-T526);
  - §4 endpoint minimum, incl. §4.2 sharp π⁴/8 (PD-T522/523/544/545/546);
  - §5 Λ_edge (PD-T529 weakened, PD-T530);
  - §6 consequences (old Cor/Remark, not yet updated);
  - §7 fixed ratio; §8 hyperinterpolation; §9 finite/open (old text);
  - Appendix A (proofs for §4.2) and Appendix B (proofs for §5).
- **MZ-SP** (`tracks/mz-constants/paper-sp/manuscript.tex`, 15 pp., clean): the post-split text in `elsarticle`; nothing integrated yet.
- **New provisional claim** PD-T?mz-paper-claude-01: [theory/cc-defect-condition-corollary.md](../theory/cc-defect-condition-corollary.md). Parts (a)–(c) were checked independently ([check-cc-defect-corollary.md](../check-cc-defect-corollary.md), PASS with corrections, applied). Part (d) has no independent check yet.
- **Tools:** [tools/build.sh](../tools/build.sh) `<paper-dir> <scratch-out-dir>` runs pdflatex, bibtex, pdflatex, pdflatex and reports pages, log issues and hashes. [tools/split.py](../tools/split.py) is the split script (provenance only). The sandbox needs `texlive-publishers` for `elsarticle`: `apt-get update && apt-get install -y --no-install-recommends texlive-publishers`.

## Task, in order

1. **MZ-CC remaining integration** (plan-cc and its dispositions):
   1. PD-T547 Prop 5.4: certified Λ_edge ≥ 1.0044369, computer-assisted, one-sided. Add Appendix C with PD-T548's closed-form Gram entries (as Lemma C.1) and the certificate reduction (exact trial, outward arithmetic, scalar remainders, the committed checker named precisely, the independent rerun). Read `topics/padua-mz-sharp-constants-20261106/theory/P4-certified-lower.md`, `P4-denominator-closed-form.md` and `independent-checks-P4*.md`.
   2. §4.1: turn the exact U_{N−1} formulas into a lemma (plan-cc disposition a1). §8 keeps the N=512 certificate and the An–Wu discussion.
   3. §4: add the interpolation-norm corollary, ‖𝓘_N‖_{ℓ²_w→L²}/log N → 2√2/π² (PD-T?mz-paper-claude-01 (d)).
   4. §6: Cor 6.1 (PD-T527 + PD-T?mz-paper-claude-01 (a)(b), with N≥57, and the computer-free interval [8/π⁴,12/π⁴] beside the certified one). Replace `cor:endpoint` and rewrite `rem:rate`: what remains open is only a convergence rate usable at computable N, and the decimal value of Λ_edge.
   5. §8: Cor 8.3 with B=min{1+ρ,5/3} (PD-T?mz-paper-claude-01 (c), with the n/N>0.908 note).
   6. §9: MEASURED material per disposition b2; open problems per M1/M2. Delete the old "PD-T020 open" sentences.
   7. Task 4: title (working: *Marcinkiewicz–Zygmund constants of Clenshaw–Curtis quadrature beyond half-exactness*), abstract and introduction with Thms 1.1–1.3 and Cor 1.4 stated up front; remove the status box and the in-heading `\id{…}`, keeping the IDs as TeX comments. Then **freeze MZ-CC numbering**.
2. **Independent check** (a separate Opus agent) of PD-T?mz-paper-claude-01 (d). Write a record for PD-T?mz-paper-claude-02 (‖B‖ ≥ c_new, plan-sp F7) and have it checked independently in the same way.
3. **MZ-SP integration** (plan-sp and its dispositions):
   1. notation-sp.md first (F12);
   2. CC-weight lemma inside SP (F1);
   3. the F2 choice: default is an appendix with the λ₊<2 proof, unless AC answers otherwise;
   4. PD-T533/537 in §5;
   5. §6 corner operator: PD-T534/535/536/539/540/541/542 with Appendices A–B, the F7 corollary and the F8 remark;
   6. §7 with the reproduction remark;
   7. §8 finite results (PD-T107 if its scope fits; F9 measured labels);
   8. §9 open problems;
   9. task 4 for SP.
4. **Tasks 5–7, both papers:** literature pass (`literature-mz-paper.md`; resolve pre-PR #21 hedges, especially the Mastroianni–Russo 2000 sentence, using `topics/padua-literature-20261103/p2-comparison.md`; the SP list in review-plan-sp (g)/F11; clickable DOI links for AC for unread items); notation-cc.md and notation-sp.md with a consistency pass; data and code availability statements naming the committed checkers (PD-T298/299/376/541/542/547) at the actual commit, with a deposit-DOI placeholder.
5. **Task 8:** internal referee round per paper (two distinct Opus reviewers each: mathematics; exposition and notation), answered in `response-internal-cc.md` and `response-internal-sp.md`.
6. **Task 9:** final builds, an independent rebuild by a different subagent, M7 manuscript-record append, README scope tables for both papers, `report.md`, results file. Prepare PAPER_MAP/state/CURRENT.md diffs for PR preparation, and reserve a final-ID range for the provisional claims by the WORKFLOW reservation procedure.
7. **Companions** (AC's rules, BRIEF §5 item 3): only after each paper's text freeze. They may be left to a later handoff if the session runs out; say so in the log.

Push at every task boundary. When development is complete, open handoff NN for the single substantive Codex audit (gpt-6-astra high or higher). It covers the mathematics-to-text correspondence, both new provisional claims, the proof-route change for PD-T523 (correspondence-cc changes log), exposition, citations and builds.

## Questions pending with AC (asked 2026-11-13; continue on the defaults)

- MZ-SP's dependence on MZ-CC's λ₊<2 (plan-sp F2). Default: (a), a self-contained appendix in MZ-SP.
- PD-T376 witness arrays for the public record (plan-sp F13). Default: keep Prop 8.1, with a deposit-DOI placeholder; the Zenodo deposit is AC's.
- MZ-CC length is now about 37–42 SIAM pages including appendices (plan-cc M3); for information.

## Read first

AGENTS.md, agents/WORKFLOW.md and agents/claude/CLAUDE_ROLES.md at the branch head; BRIEF.md; the LOG; plan-cc.md and plan-sp.md with the reviews and dispositions; correspondence-cc.md and correspondence-sp.md (including the changes log); split-map.md; the theory records named above.

## Scope limits

As handoff 01: write only in this topic directory, `results/padua-mz-paper-20261113.md`, both paper directories and the M7 record (append only). Shared registries only at PR preparation. Do not write to other open branches (PR #27, PR #34). Never strengthen a statement silently: any new mathematical statement gets a provisional record and an independent check, and is flagged for the audit. No PDFs or bulk data in Git. AI declaration, ORCID, contributions, funding, cover letter, venue, submission and deposits are reserved to AC. Commits are authored by Andrey Chesnokov <aacchhee@gmail.com>, with Agent/Model trailers. Only AC merges.

## Acceptance and outputs

As handoff 01, *Acceptance and outputs*, and gates W1–W4. Reply to AC only with the `Continue` prompt for the next step.
