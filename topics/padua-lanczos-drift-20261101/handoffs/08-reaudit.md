# Handoff 08 — padua-lanczos-drift-20261101 — Codex re-audit of response-02

- Status: open
- Previous handoff: 07-response-02.md

- Next agent / model / effort: Codex, `gpt-6-astra` xhigh (independent auditor; Codex audits Claude development)
- Role: independent auditor
- Branch: codex/padua-lanczos-drift-20261101
- Input head SHA (candidate): `ea829d92d509f79326a1cc037844a1bac3b4de13`. The commit publishing this file changes only handoff statuses.
- Previous audited candidate: `cef79d66321a93d93d53e53efcb7e6744c387481` (audit-02)
- Main / base: `28aaa20861d08074b77efc74eaef75cdcb36234d` (PR14 and PR16 merged)
- Stage: AUDIT; PR15 remains draft
- Written by / date: Claude, configured `claude-opus-5-5` xhigh · 2026-11-01

## Task

Re-audit Claude's response-02, the changes `1df5f89..ea829d92d509f79326a1cc037844a1bac3b4de13`, and write `topics/padua-lanczos-drift-20261101/audit-03.md`. Give the exact pins, the model/effort actually used, read coverage, executed commands, severity-ranked findings, a disposition for each of A02-M1, A02-M2 and A02-L1…L8, and the remaining uncertainty.

Material items (see the end of response-02.md):

1. **Record 15.** Display (13): δ_A(t)/u = κ_A‖v_m‖/√(b²+u²‖v_m‖²) → (κ_A/b)‖v_m‖, with equality for the forming operator iff κ = b. Check the general form and run `e4_response02_check.py` (25 instances). Also check IDEA?drift-claude-17's R17a/R17b repair definitions.
2. **New record 06,** `drift-codex-e1-06-finite-scalar-cgs2-separation.md` (PROVED, computer-assisted, formal scalar model):
   - the reduction from record 03; exact statements; the evidence pins;
   - the distinction between reused independent executions (independent-scalar-01, audit-01 `ind_scalar.py`, audit-02 E1) and the new developer regeneration;
   - run `e1_scalar_finite_check.py`, optionally with `--regenerated`.

   Also decide on **record 05's factor-ten target label PARTIAL**: T24 conjunct PROVED in -06, rotQ24 conjunct OPEN. The test outcome stays INCONCLUSIVE and the file status stays MEASURED. If you prefer OPEN, say so.
3. **Record 30.** The a₋/a₊ labels and the eventual-only a ≤ 0 scope. Run `e5_response02_check.py` (Arb-384, P₄(ζ₄(a*)) < 0 at a* = 20π³/9 − 512π).
4. **Record 50 and E6.** The midpoint-law wording; rerun equality via `e6_offsample_compare.py`; the `numpy==2.3.5` pin; the IDEA57 kill direction.
5. **Degree-4 replay** (`e1_replay_n4.py`, which calls the unchanged audit-01 `first_principles.py` by hashed path) and the corrected coverage text. Audit-01's summary error is annotated in LOG; audit-01 itself is unchanged.
6. **L8.** Repository-only results wording in plan, report, proposals and COLD_STORAGE; `results/padua-lanczos-drift-20261101.md` accuracy.
7. **Integration.** Refresh main and the open PRs (at writing, only PR12 `146babe`) and rerun `integration_check.py`. The receipt at `b94e5a1` is `evidence/response-02-integration-20261101.json`, PASS.

Commands and pins are in each developer report under `checks/response-02/` and in `tracks/bivariate-lanczos/code/drift/README.md`. Use the pinned environment: numpy 2.3.5, python-flint 0.9.0, SymPy 1.14.0, mpmath 1.3.0, `OPENBLAS_NUM_THREADS=1`.

## Read first

- `AGENTS.md`, `agents/WORKFLOW.md`, `agents/codex/CODEX.md` at the branch head.
- LOG (the last entry), audit-02.md, response-02.md and `checks/response-02/*`.
- For the IDEA-17 change, the complete `state/IDEAS.md`.

## Scope limits

- Do not edit audits, responses or developer reports.
- No final IDs. No registry edits until preparation.
- No main commits or pushes, no merges, no force pushes, no tags, no `.github/`. PR15 stays draft. Only AC merges.

## Acceptance and outputs

- `audit-03.md` and a LOG entry; PR #15 AUDIT updated.
- If you accept, open a PR-preparation handoff covering:
  - final IDs from PD-T136–155, PD-N062–071, IDEA-246–285 and LIT-445–459 (record 14 withdrawn; record 06 added);
  - applying the literal proposals;
  - removing the record-14 tombstone;
  - the registry rows (PROOF_STATUS, IDEAS, CROSSWALK);
  - this topic's root RESULTS.md section;
  - a fresh union scan and readiness.
- If you find problems, open a response handoff.
- Commit outputs, then in a following commit set this handoff to `done in <sha>` and add the next handoff. Keep exactly one open handoff.
