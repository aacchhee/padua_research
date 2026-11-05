# Claude audit-01 support files

All executions are by the Claude auditor on 2026-11-05 (Python 3.13.18, SymPy 1.14.0, python-flint 0.9.0 / FLINT 3.6.0, mpmath 1.3.0, NumPy 2.5.3, SciPy 1.18.1). `<deps>` was a pip `--target` prefix holding sympy==1.14.0, python-flint==0.9.0 and mpmath. The repository clone was at `407fe83` (topic theory/code/evidence identical to `5b2e367`).

| # | Command (from repo root unless noted) | Exit | Output |
|---|---|---|---|
| 1 | `git cat-file blob 3f65a77df46ed9ba3c665fd80cd8509fefefaa17 > audit/t1/archived-interior.json.gz` | 0 | SHA-256 a3b4f278…, 637163 B |
| 2 | proof payload of 1 via committed `code/t1_payload.proof_payload` | 0 | 18969878 B, e22a9b55… (matches developer) |
| 3 | `PYTHONPATH=<deps> timeout 9000 python3 -B topics/padua-lebesgue-followups-20261103/code/t1_boundary.py --output audit/t1/boundary-claude.json` | 0 | 2250.7 s; raw cf141bab…, 4822048 B; [log](boundary-regeneration.log) |
| 4 | proof payload of 3 via `t1_payload.proof_payload` | 0 | 4821831 B, 1316b929… = developer adfe1107… payload |
| 5 | `claude_monolithic_n8.py` (see audit-01 §T1.4) | 0 | [monolithic-receipt.json](monolithic-receipt.json), [facts comparison](monolithic-facts-comparison.json) |
| 6 | `PYTHONPATH=<deps> python3 -B claude_analytic_checks.py` (from this dir) | 0 | [claude_analytic_checks.json](claude_analytic_checks.json), 11.2 s |
| 7 | `python3 -B topics/…/code/t3_series.py --terms 72 --digits 16 --output reruns/t3-series-claude.json` | 0 | rows identical to developer |
| 8 | `python3 -B topics/…/code/t3_quadrature.py --series-receipt reruns/t3-series-claude.json --output reruns/t3-quadrature-claude.json` | 0 | identical except python/receipt hash |
| 9 | `PYTHONPATH=<deps> python3 -B topics/…/code/t4_constant.py --order 64 --bits 320` and `--order 96 --bits 448` | 0, 0 | reruns/t4-constant-claude-*.json |
| 10 | `frozen_boundary_ast()` under Python 3.13.18 | 0 | aad6c3e2… ≠ pinned 73fc0216… (finding F6) |

Sub-auditor reports and their scripts: [subreports/](subreports/), [subreport-scripts/](subreport-scripts/). Bulk T1 artifacts (regenerated boundary, joined certificate, full checker output) remain in the auditor's cloud sandbox and are not committed; identities are in the receipts. Physical delivery to AC cold storage is pending.
