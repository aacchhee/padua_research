# Handoff 03 — padua-effective-cubature-20261112 — Codex audit of session 1 and the explicit-γ campaign (C0, uniform Theorem A, cap, PD-N, explicit γ ≥ 1/36)

- Status: open
- Previous handoff: [02-audit.md](02-audit.md) (superseded by this one before any audit was written; it covered session 1 only)
- Next agent / model / effort: **Codex, `gpt-6-astra`, high or higher** (auditor's choice, recorded). This is the single substantive audit of Claude development (AGENTS.md: Codex audits Claude development).
- Role: independent auditor
- Branch: `claude/padua-effective-cubature-20261112`
- Input head SHA: `895d85fdd995e9f227dabaf8a212ba4d3b188db0` (the outputs commit; the commit that publishes this file comes later)
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
| PD-N -06 | `theory/limitation-torus-lp-finite.md` | PROVED (exact finite check) | The reduction to -04 (b′); the witness range S; rerun both checkers; the scope wording |
| PD-T -07 | `theory/explicit-gamma.md` | PROVED, computer-assisted (local) | The transcription of DGOV's normalisation (K−K = {\|x\|₁ ≤ 1}, vol K = 1/6). Part (L): the exact transform G; the rigour of `code/gamma_certificate.py` (Taylor-shift enclosure, the a-priori float error bound 2^−46, exact dyadic y-boxes, the ℓ₁-region discard rule, the tail shift test from \|x\|_∞ ≥ 4). Rerun it, and read the independent rerun `independent-checks-gamma.md` with `code/gamma_certificate_indep.py`. The arithmetic of (b)–(d): 37n³/216, 218, 109, n₀(1/72) = 220 |

### Measurements and gates

- Check `gates.md`:
  - the pre-registrations are unedited (pushed at `0abf5e7`, before any run; compare with `git show 0abf5e7:topics/padua-effective-cubature-20261112/gates.md`);
  - the Q0–Q3 verdicts follow from the evidence.
- Check that every numerical statement is labelled MEASURED and that none is used as a premise of a PROVED record.
- Note the receipt caveat: `lp_torus.py` changed mid-campaign, and four script SHA-256 values occur in `evidence/lp-torus.json`.

### Novelty and mechanisms

Mechanism and novelty claims are present: IDEA?…-claude-01 and -07 are "variant/new combination", and candidates -02 to -06 are deferred or pending. So:
- **read `state/IDEAS.md` in full**, together with `novelty-gate-E1.md` and `novelty-gate-C0.md`;
- check that no IDEA or PD entry already contains the Delsarte transference or the cube LP;
- check that the priority wording ("no priority claim"; Kuperberg/Xu LP precedent, LIT-663) is adequate;
- check `literature-effective.md`: LIT?…-claude-01 (KLM 2025) and LIT?…-claude-02 (DGOV 2017, arXiv:1510.02331v3: Theorem 1.1, Table 6, §6, ancillary `README_SOSChecking`); Read the cited pages of arXiv:2510.10172v1: Def. 5.1 (pp. 15–16), (6.2), Thm 6.4 and the Δ(A) remark (§6.5, p. 25), and p. 2 on the Turán problem.

## Reproduction commands (from the repository root unless stated)

```
python -B topics/padua-3d-20261106/code/fd1_controls.py --output <scratch>/fd1-controls-replay.json
python -B topics/padua-3d-20261106/code/fd3_certify.py check --certificate topics/padua-3d-20261106/evidence/fd3-certificate.json --receipt <scratch>/fd3-replay.json
python -B topics/padua-effective-cubature-20261112/code/q0_d3_leverage.py --certificate topics/padua-3d-20261106/evidence/fd3-certificate.json --output <scratch>/q0c.json
python3 -B topics/padua-effective-cubature-20261112/code/cap_critical_lattice.py <scratch>/cap.json
cd topics/padua-effective-cubature-20261112 && python3 -B code/pdn_lattice_witness.py --nmin 2 --nmax 140 --extra evidence/lp-lattice.json --perturb --out <scratch>/witness-full.json   # about 13 min; then the checker about 3 min
cd topics/padua-effective-cubature-20261112 && python3 -B code/pdn_check_ball.py --full <scratch>/witness-full.json --out <scratch>/pdn-check.json   # compare with evidence/pdn-lattice-witness.json
curl -sSL -o <scratch>/octa_double.func.cpp https://arxiv.org/src/1510.02331v3/anc/octa_double.func.cpp   # third-party input, SHA-256 034a1aea…7bc47; do not commit
cd topics/padua-effective-cubature-20261112 && python3 -B code/gamma_certificate.py --anc <scratch>/octa_double.func.cpp --alpha 1.001 --R 4 --RG 4 --out <scratch>/gamma.json   # about 2 min; compare with evidence/gamma-certificate.json
cd topics/padua-effective-cubature-20261112 && python3 -B code/gamma_ft_check.py --anc <scratch>/octa_double.func.cpp
python3 -B topics/padua-effective-cubature-20261112/code/evidence_manifest.py --verify
cd topics/padua-effective-cubature-20261112 && python3 code/lp_torus.py --q1a --out <scratch>/q1a.json && python3 code/lp_cube.py --q1a
```

Optional, with a long run time: one LP run, e.g. `python3 code/lp_torus.py --n 5 --extra 5 --out <scratch>/n5_e5.json` (cwd = topic directory), to be compared with the row in `evidence/lp-torus.json`.

Dependencies: Python 3.13, NumPy, SciPy/HiGHS (highspy), SymPy, mpmath, python-flint (arb). The fd1/fd3 replay needs SymPy only.

## Read first

- `AGENTS.md`, `agents/WORKFLOW.md`, `agents/codex/CODEX.md` at the branch head.
- `BRIEF.md`, `handoffs/01-work.md`, `LOG.md`, `report.md`, `gates.md`, `plan.md` and `rounds.md`.
- `attempts/E1–E3.md` and all of `theory/`.
- `independent-checks-C0.md`, `independent-checks-E1.md`, `independent-checks-E1b.md` (the Opus check of -02 (d), -03 (ii′) and -06) and `independent-checks-gamma.md` (the independent rerun of the γ certificate).
- `attempts/E1-gamma.md` and gates addendum G.
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
- **Commits.** Commit the audit, then in a following commit set this handoff to `done in <sha>` and open handoff 04:
  - for a Claude response if there are findings;
  - for PR readiness (ID reservation, registries, the `RESULTS.md` section) if accepted.
- **Reply to AC** with the next-prompt line only.
