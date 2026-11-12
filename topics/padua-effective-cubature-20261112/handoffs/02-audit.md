# Handoff 02 — padua-effective-cubature-20261112 — Codex audit of session 1 (C0, uniform Theorem A, cap, PD-N, LP numerics)

- Status: open
- Previous handoff: [01-work.md](01-work.md) (done; see its status line)
- Next agent / model / effort: **Codex, `gpt-6-astra`, high or higher** (auditor's choice, recorded). This is the single substantive audit of Claude development (AGENTS.md: Codex audits Claude development).
- Role: independent auditor
- Branch: `claude/padua-effective-cubature-20261112`
- Input head SHA: `061b2f4a925571e444e39440979697de72d32da9` (the outputs commit; the commit that publishes this file comes later)
- Main / base: `b5388c2`
- Stage: AUDIT
- Written by / date: Claude, configured `claude-opus-5-5` xhigh · 2026-11-12

## Task

Audit every claim of session 1 and write `topics/padua-effective-cubature-20261112/audit-01.md`. The PROVED claims rest on the records below, and none rests on a measurement. For each record, check:
- the statement against the proof;
- the quantifiers and conventions (normalized product Chebyshev measure; nodes in the closed cube; positive weights; exactness 2n−2 vs 2n−1);
- the dependencies, both the local ones and the literature transcriptions;
- the status labels.

### Claims

| ID (provisional `…-claude-NN`) | Record | Claimed status | Audit focus |
|---|---|---|---|
| PD-T -01 | `theory/lebesgue-constant-corollary.md` | PROVED (assembly) | Statement vs PD-T209/162/166/169/174/177/181/214/246/229/269–271; the existential N_*; the constant c; the PR #27 disclosure (not a dependency). Already checked by Opus (`independent-checks-C0.md`) |
| PD-T -02 | `theory/delsarte-bound.md` | PROVED | (a) finite Delsarte bound; (b) periodization/transference, L = n−½; (c) supremum via ψ_R; **(d)** exactness range E, lift exact up to \|k\|₁ = E, L = (E+1)/2 |
| PD-T -03 | `theory/uniform-theorem-a.md` | PROVED with LITERATURE dependency | (i) KLM Thm 6.4 transcription, Δ(O) = int 2O, D ≥ m (KLM (6.2)); non-tiling of O via Lev–Matolcsi plus Greenfeld–Lev; **(ii′)** N ≥ (1+γ_A)n³/6; **(iv)** threshold 110 (was 138); Fisher crossover 55 |
| PD-T -04 | `theory/lp-cap.md` | PROVED | (a) the change of variables and the lattice facts (det 38/27, min ℓ₁ 2; `code/cap_critical_lattice.py`); (b) lattice-rule dual feasibility, with the exactness-E remark |
| PD-T -05 | `theory/explicit-gamma-target.md` | OPEN | The status and the sufficient-route arithmetic only |
| PD-N -06 | `theory/limitation-torus-lp-finite.md` | PROVED (exact finite check) | The reduction to -04 (b); the witness range S; rerun both checkers; the scope wording |

### Measurements and gates

- Check `gates.md`:
  - the pre-registrations are unedited (pushed at `0abf5e7`, before any run; compare with `git show 0abf5e7:topics/padua-effective-cubature-20261112/gates.md`);
  - the Q0–Q3 verdicts follow from the evidence.
- Check that every numerical statement is labelled MEASURED and that none is used as a premise of a PROVED record.
- Note the receipt caveat: `lp_torus.py` changed mid-campaign, and four script SHA-256 values occur in `evidence/lp-torus.json`.

### Novelty and mechanisms

Mechanism and novelty claims are present: IDEA?…-claude-01 is a "variant/new combination", and candidates -02 to -06 are deferred or pending. So:
- **read `state/IDEAS.md` in full**, together with `novelty-gate-E1.md` and `novelty-gate-C0.md`;
- check that no IDEA or PD entry already contains the Delsarte transference or the cube LP;
- check that the priority wording ("no priority claim"; Kuperberg/Xu LP precedent, LIT-663) is adequate;
- check `literature-effective.md` (LIT?…-claude-01, KLM 2025). Read the cited pages of arXiv:2510.10172v1: Def. 5.1 (pp. 15–16), (6.2), Thm 6.4 and the Δ(A) remark (§6.5, p. 25), and p. 2 on the Turán problem.

## Reproduction commands (from the repository root unless stated)

```
python -B topics/padua-3d-20261106/code/fd1_controls.py --output <scratch>/fd1-controls-replay.json
python -B topics/padua-3d-20261106/code/fd3_certify.py check --certificate topics/padua-3d-20261106/evidence/fd3-certificate.json --receipt <scratch>/fd3-replay.json
python -B topics/padua-effective-cubature-20261112/code/q0_d3_leverage.py --certificate topics/padua-3d-20261106/evidence/fd3-certificate.json --output <scratch>/q0c.json
python3 -B topics/padua-effective-cubature-20261112/code/cap_critical_lattice.py <scratch>/cap.json
cd topics/padua-effective-cubature-20261112 && python3 -B code/pdn_lattice_witness.py --nmin 2 --nmax 140 --extra evidence/lp-lattice.json --perturb --out <scratch>/witness-full.json   # about 13 min; then the checker about 3 min
cd topics/padua-effective-cubature-20261112 && python3 -B code/pdn_check_ball.py --full <scratch>/witness-full.json --out <scratch>/pdn-check.json   # compare with evidence/pdn-lattice-witness.json
python3 -B topics/padua-effective-cubature-20261112/code/evidence_manifest.py --verify
cd topics/padua-effective-cubature-20261112 && python3 code/lp_torus.py --q1a --out <scratch>/q1a.json && python3 code/lp_cube.py --q1a
```

Optional, with a long run time: one LP run, e.g. `python3 code/lp_torus.py --n 5 --extra 5 --out <scratch>/n5_e5.json` (cwd = topic directory), to be compared with the row in `evidence/lp-torus.json`.

Dependencies: Python 3.13, NumPy, SciPy/HiGHS (highspy), SymPy, mpmath. The fd1/fd3 replay needs SymPy only.

## Read first

- `AGENTS.md`, `agents/WORKFLOW.md`, `agents/codex/CODEX.md` at the branch head.
- `BRIEF.md`, `handoffs/01-work.md`, `LOG.md`, `report.md`, `gates.md`, `plan.md` and `rounds.md`.
- `attempts/E1–E3.md` and all of `theory/`.
- `independent-checks-C0.md`, `independent-checks-E1.md` and `independent-checks-E1b.md` (the Opus check of -02 (d), -03 (ii′) and -06, if present at the input head).
- `literature-effective.md`, `evidence-manifest.json` and `results/padua-effective-cubature-20261112.md`.
- Merged dependencies:
  - `topics/padua-3d-20261106/final-d1/` (D1-01 lift, D1-04 Theorem A, sources);
  - `theory/r08-lattice-minima.md`;
  - `paper-note-draft.md` §2 and §4.

## Scope limits

- Do not edit the development files and then approve them; return findings.
- No main mutation, merge, force-push, tag, settings or `.github/` change.
- Do not write to PR #27's branch.
- Do not commit third-party PDFs or extracts.

## Acceptance and outputs

- **Audit file.** `audit-01.md` with:
  - model and effort, the audited SHA, and the commands actually run with their outputs;
  - findings by severity (BLOCKING / MAJOR / MINOR / NOTE), each with file:line and a proposed fix;
  - per-claim verdicts and an overall verdict.
- **Commits.** Commit the audit, then in a following commit set this handoff to `done in <sha>` and open handoff 03:
  - for a Claude response if there are findings;
  - for PR readiness (ID reservation, registries, the `RESULTS.md` section) if accepted.
- **Reply to AC** with the next-prompt line only.
