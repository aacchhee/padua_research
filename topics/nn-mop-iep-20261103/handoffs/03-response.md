# Handoff 03 — nearest-neighbour MOP IEP — Codex response-01 to Claude audit-01

- Status: done in 5b36f8f8ac5b3c9a426d22a9375155a2b4d86e1b
- Previous handoff: 02-audit.md
- Next agent / model / effort: Codex.
  - Mathematics and record corrections (F1, F2): gpt-6.1-sol, xhigh.
  - F3 baseline run, if executed, and F4 receipts: gpt-6.1-sol, medium.
  - Optional supplementary check: gpt-6-astra, high.
- Role: orchestrator and developer (response to audit).
- Branch: codex/nn-mop-iep-20261103
- Input head SHA: `48f7479700cfe3966c4e3fe4bf72122a30ddb6e6` (audit-01 output commit). Audited candidate: `ae7e6187e8731b6f83aa444d4d702a0ef779c564`.
- Main / base: `440d1079e42c3ef21c40d1cf8870f5b206410c6a` (refetch and record; merge `origin/main` if it moved).
- Stage: WORK (audit findings)
- Written by / date: Claude, claude-opus-5-5 xhigh (independent auditor), 2026-11-05.

## Task

Write `topics/nn-mop-iep-20261103/response-01.md`. Answer every finding of [audit-01.md](../audit-01.md) (F1–F4, N1, N2) with one of:
- a fix,
- an evidence-based rejection, or
- an explicitly unresolved item preserved for AC.

Never edit audit-01.md. Read the rules at the branch head first and record the SHA.

1. **F1 (major).**
   - Obtain the primary text of FHV 2015 §3.1/§3.3 (Thm 3.3, eqs. (3.11)–(3.14), pp. 19–21) and Van Assche 2011 Thm 3.1. Quote, in faithful paraphrase with page, which layer's divisors b_{ν,k} − b_{ν,j} are used to compute each layer of NN coefficients from marginal data.
   - Then confirm or refute the auditor's claim. The claim: under normality through degree N, reconstruction on |ν| ≤ N−1 uses divisors only at |ν| ≤ N−2, which are nonzero by the interior part of PD-N?nn-mop-iep-codex-01. The auditor's relations (A), (B1) and (B2) and the checker `audit-01/claude_layer_recursion_check.py` are inputs to check, not results to inherit.
   - If confirmed, three things follow:
     - Rescope PD-N?nn-mop-iep-codex-01 to propagation to degree-N coefficients. Decide under WORKFLOW L5 whether that scoped negative still records a failed mechanism, or whether the record should be reworked: for example, the terminal equality kept as a final boundary condition inside a positive record. Preserve the original wording in History.
     - Correct gate.md (Decision; "Correcting C4"), report.md, candidates.md (C4), exact-runs.md (final-layer sentence) and results so that C4 on the normal finite triangle is not described as needing a boundary modification.
     - Apply split-by-default. If a positive statement depends on the interior d ≠ 0 lemma, propose a PROVED record for it (provisional `PD-T?nn-mop-iep-codex-03` or the next free local number) with a full written proof. Possible content: "marginal-data NN reconstruction is well defined on the normal common-support triangle; the terminal b-equality is a necessary final boundary condition". Include the Kozhan–Vaktnäs Thm 3.6 comparison. The auditor's checker counts only as MEASURED support.
   - If refuted, state the exact FHV step that needs the terminal divisor for a coefficient with |ν| ≤ N−1.
2. **F2 (minor).**
   - Reword report.md "Precise objects", PD-N?nn-mop-iep-codex-02 and C2. Fixed-site noncommutation kills only the literal identification. PD-T057's block form (Xu commuting conditions) also couples adjacent levels.
   - State the decisive mismatch as one spectral variable: both NN difference operators H_1, H_2 have eigenvalue x on the MOP vector, versus independent joint eigenvalues (x_l, y_l). Statuses unchanged.
   - Optionally list the H_1/H_2 full-lattice encoding as tested (auditor's 255-site count, MEASURED) or as not excluded.
3. **F3 (minor).**
   - Correct the LOG sentence "No expensive numerical run is pending…".
   - Add to Runs needed a C4-only floating-point baseline:
     - method: floating-point marginal Jacobi data, then the (A)/(B) layer recursion;
     - comparison: against exact or high-precision ground truth on the Kravchuk/Hahn families of SINUM / arXiv 2608.25758;
     - metric: digits lost versus N;
     - include the planned command.
   - You may execute it at medium effort with a full run receipt (MEASURED). Never report a run that did not execute.
4. **F4 (minor).** Note in exact-runs.md and independent-check.md that the output SHA-256 values depend on the embedded `python`/`sympy` version fields. Cross-environment identity requires normalising those fields; the auditor reproduced both recorded hashes that way.
5. **N1/N2.**
   - Record in literature.md which primary locators were rechecked in this round.
   - Add IDEA-197 to the gate's closest-entries table with its non-applicability reason.

## Do not reopen

- PD-T?nn-mop-iep-codex-01 (PROVED, accepted).
- The finite counts of PD-T?nn-mop-iep-codex-02 and PD-N?nn-mop-iep-codex-02 (MEASURED, accepted).
- C1/C2/C3 dispositions (except F2 wording and any F1 consequence for C4).
- The permanent reservation T286–293, N100–103, IDEA376–383, LIT562–573 (first pushed `a0abe8b`).

No new novelty claims beyond what F1 requires; any new candidate goes through the gate.

## Scope limits

- Write only inside `topics/nn-mop-iep-20261103/`, `results/nn-mop-iep-20261103.md` and new topic-owned theory/literature records.
- No shared registry edits, no final-ID assignment, no merge, no force-push, no tags, nothing under `.github/`. Only AC merges.
- Raw outputs stay local and regenerable; commit code and short receipts only.
- Do not contact Leuven or any external person.
- List any unreachable primary source for AC with a verified DOI or arXiv link.

## Acceptance and outputs

- response-01.md with a disposition for every finding.
- Updated records consistent with those dispositions.
- Any new theory record follows templates/THEORY.md with explicit status.
- Run receipts for anything executed.
- LOG, results file and PR22 WORK/AUDIT sections updated (AUDIT: audit-01 findings, response pending re-audit).
- Commit the outputs first. In a following commit, set this handoff's status to `done in <output-sha>` and add handoff 04.
- F1 changes a claim's scope and possibly its records, so handoff 04 is a **Claude re-audit (Opus 5.5 xhigh)** of response-01. If every finding were resolved without material change, Codex may argue in response-01 for direct PR preparation; the re-audit decides.
- Push before replying. The reply ends only with `Claude (Opus 5.5 xhigh): Continue codex/nn-mop-iep-20261103.`
