# Claude audit 01 — independent check code

Independent check scripts written by the Claude audit workers for [audit-01](../../audit-01.md). They import no topic producer code, except where a row below says otherwise. Outputs are regenerable and were not committed. SHA-256 prefixes of the audit-run outputs are recorded below. Environment: Python 3.13.18, mpmath 1.3.0, SymPy 1.14.0, NumPy 2.5.3, SciPy 1.18.1, scipy-openblas 0.3.34, glibc 2.39, single-threaded BLAS. Script paths are relative to this directory; some scripts locate repository files at the checkout path `/workspace/padua_research` used by the audit. `OUT` is any fresh output directory.

| Script | Scope | Command | Result (output prefix) |
|---|---|---|---|
| A/c2_hard_check.py | Byte-exact extraction of the only python block in attempts/C2-hard.md (sha256 452d72d7…) | `python3 -I A/c2_hard_check.py` | PASS: 50 polys, 735 jets, 1050 a rows, 330 support coords (65c1427d…) |
| A/kappa_exact.py | Exact-Fraction Krawtchouk κ_N from the PD-T432 definition, x variable, all 3N columns | `python3 -I A/kappa_exact.py 2 18` | PD-T437 lower ≤ κ_N ≤ 3·10⁶N¹³ρ^M at every N=2..18 (f8c40db1…) |
| A/lemmas.py | Exact k-variable lemmas (3),(12),(19)–(21), support successor, majorant ratios | `python3 -I A/lemmas.py 2 16` | every identity exact; every actual/claimed ratio < 1 (36e4158e…) |
| A/contours_formula8.py | Formula (8) with the stated source split and contours, 45 dps | `python3 -I A/contours_formula8.py > OUT/f8.jsonl` | max relative error 2.8e-45 for N≤5 (stopped before N6) (80e8c549…) |
| A/contours_pointwise.py | Pointwise majorants (5),(11),(14) | `python3 -I A/contours_pointwise.py > OUT/pw.jsonl` | (5),(11) ratio 1 up to rounding, attained at u=c; (14) ≤ 0.222 (6d2cead6…) |
| B/audit_exact_nn.py | Exact Hahn NN data and κ_N, normality, formulas (1)(2), witnesses | `python3 -I B/audit_exact_nn.py 16` | all checks pass N=2..16; κ_N equals predecessor table N4–16 (1a803491…) |
| B/audit_rate.py | Terminal row M=2..24, generating function to M=80, saddle, envelope | `python3 -I B/audit_rate.py OUT` | D_M exact; H/r = ρ_H to 45 digits (0f55a7d0…) |
| B/audit_sympy.py | Kernel determinant constants, identity (4), quartic/minimal polynomial | `python3 -I B/audit_sympy.py` | all symbolic identities hold (b8134159…) |
| B/compare.py | Compares rerun Hahn checker payloads with committed JSON | `python3 B/compare.py OUT` | four payloads identical apart from timing/version |
| C/indep_nn.py, C/t1–t8 | Independent moment-solve NN/step-line, finite differences at 70–80 dps; gauge, matrix, scalar, parameter-lower tests | `python3 -I C/t2_param_lower.py` etc. (each writes its JSON beside its CWD) | 56 parameter-lower cases pass; gauge/matrix/scalar inequalities hold (t2 84998f97…, t3 34df7252…, t4 09e4ffc4…, t5 bf60c450…) |
| D/c3_rank.py | Exact residual-dimension ranks d_c, rank M, rank H, N=3..5 | `python3 -I D/c3_rank.py` | d_c = rank M > rank H as the record states |
| D/mkext.py | Builds a synthetic external-input file to exercise c4_compare.py's native path (imports predecessor c4_float_baseline.py) | `python3 D/mkext.py OUT/ext.json` | native C4 tables reproduce; hahn-C4.csv byte-identical |

The topic producers rerun by the audit (c1_metrics.py/c1_summarize.py full grid, c2_rate_checks.py, c2_hahn_*.py, independent_hahn_rate.py, c3_grid.py full grid, c4_normalization.py, c4_lift.py, verify_evidence.py) use the commands in audit-01.md. The rerun c1-grid.csv is byte-identical to the committed file (aa3a6e19…). The rerun c3 summary prefix is 4eee4169… and the rerun c1-summary prefix is 8e305606…; audit-01.md lists their differences from the committed files.
