# Handoff 05 — padua-effective-cubature-20261112 — focused Codex review of response-01

- Status: open
- Previous handoff: [04-response.md](04-response.md)
- Next agent / model / effort: **Codex, gpt-6-astra, high**. Focused review of material changes only (handoff 04, Acceptance).
- Role: independent auditor
- Branch: `claude/padua-effective-cubature-20261112`
- Input head SHA: `6c178e9d657419467c8b6eed2909ffa1347a32eb` (the response outputs; the commit publishing this file comes later)
- Main / base: `b5388c25a2a5ccb8d0faf816ab87023cf347bcd3`
- Stage: AUDIT (focused)
- Written by / date: Claude, configured `claude-opus-5-5` xhigh · 2026-11-13

## Task

Review the material changes of `response-01.md` against `audit-01.md` A1–A9, and write `audit-02.md`. Do not reopen the claims audit-01 accepted (-01 to -04, the mathematics of -06), except where a changed dependency requires it.

1. **A1, -05 compact-support witness.** Check the theorem and proof in `theory/explicit-gamma-target.md`:
   - β = (3/2)M₄ (cubic B-spline): 0 ≤ β ≤ 1, β̂ ≥ 0, 1 − β(t) ≤ (3/2)t²;
   - the product inequality 1 − g ≤ Σ(1 − β_i);
   - admissibility of ψ_R = φ·g(·/R), including ψ̂_R = φ̂ ∗ R³ĝ(R·) ≥ 0;
   - the second-moment bound and Gaussian moments m(b) = Π(2b_i − 1)!!/(2π)^{b_i};
   - the code `code/gamma_compact.py`, including how it reads γ₁'s lower end from the receipt;
   - the status history wording.
2. **A2, revised `code/gamma_certificate.py`** (SHA `52c8c9d9…c6ff`):
   - the certified coefficient-error construction (Fraction for P; 256-bit Arb abs_upper for G, rounded up) and its propagation Σ_a e_a(M+R)^a, also through the tail faces;
   - explicit-multiplication powers, and the a-priori error constant 2⁻⁴⁶ for the actual operation sequence;
   - the asserts (fl(α) ≤ α; box width ≥ 2⁻²⁴, so squares are exact);
   - the docstring argument.
   
   **Replay both certificate scripts** if the input is retrievable in your environment. A missing replay must be reported as missing, not as PASS.
3. **A6:** the appended corrected Q2 verdict in `gates.md` and its synchronisation in report, attempts/E1, rounds, results and novelty gate. Check that the pre-registrations and historical entries are kept.
4. **A3/A7:** the corrected scope (-06 covers 2–109 with M ≤ 8N only) and threshold statements (coefficient 19/108 iff γ_A = 1/18; cutoff 110 iff γ_A > 9227/166375) in report, -06 and -07.
5. **A8:** the reconstructed gate timing and the RETROSPECTIVE completion addendum in `novelty-gate-E1.md`. Check that it does not claim prospectivity and that the table list is complete.
6. **A4/A5/A9:** spot-check the wording and pointer fixes.

## Reproduction commands (cwd = topic directory unless stated)

```
curl -sS -o <scratch>/octa_double.func.cpp https://arxiv.org/src/1510.02331v3/anc/octa_double.func.cpp   # third-party; SHA-256 034a1aea4fafbf29743bded0812723ac8c9cf95274225213578145d016a7bc47; do not commit
python3 -B code/gamma_certificate.py --anc <scratch>/octa_double.func.cpp --alpha 1.001 --R 4 --RG 4 --out <scratch>/gamma-dev.json      # ~2.5 min; compare with evidence/gamma-certificate.json
python3 -I code/gamma_certificate_indep.py --input <scratch>/octa_double.func.cpp --out <scratch>/gamma-indep.json                         # ~5 s; compare with evidence/gamma-certificate-indep.json
python3 -B code/gamma_compact.py --anc <scratch>/octa_double.func.cpp --gamma-receipt evidence/gamma-certificate.json --R 100000 --out <scratch>/compact.json
python3 -B code/gamma_ft_check.py --anc <scratch>/octa_double.func.cpp
python3 -B code/lp_cube.py --q1a --out <scratch>/q1a-cube.json
cd ../.. && python3 -B topics/padua-effective-cubature-20261112/code/evidence_manifest.py --verify
```

Dependencies: Python 3.13 (3.12 also worked for the audit controls), NumPy, python-flint 0.9.0, mpmath 1.3.0, SciPy/HiGHS for lp_cube.

## Read first

- AGENTS.md, agents/WORKFLOW.md and agents/codex/CODEX.md at the branch head.
- `audit-01.md` and `audit-work/*.md`.
- `response-01.md`, LOG (the 2026-11-13 response entry), `gates.md` (appended entries) and `novelty-gate-E1.md` (the 2026-11-13 addendum).
- `theory/explicit-gamma-target.md` and `theory/explicit-gamma.md`.
- `code/gamma_certificate.py`, `code/gamma_compact.py`, `report.md` and the results file.

## Scope limits

- Review only; do not edit the development files and approve them yourself.
- No new development, ID allocation, registry edits, merges, force-pushes, tags, settings or `.github/` changes. Only AC merges.
- No third-party coefficients, PDFs or extracts in Git.

## Acceptance and outputs

- `audit-02.md` with:
  - model and effort, the audited SHA, and the commands actually run with their outputs (or the explicit reason a run was not possible);
  - findings by severity, and a verdict per finding A1–A9;
  - the overall verdict: either READY for PR preparation (IDs, registries, `RESULTS.md` section) or WORK.
- Commit the audit, then in a following commit set this handoff to `done in <sha>` and open handoff 06:
  - PR preparation, if accepted;
  - a Claude response, if there are findings.
- Keep exactly one open handoff.
