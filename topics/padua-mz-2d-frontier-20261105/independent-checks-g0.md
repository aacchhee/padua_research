# Independent G0 replay — 2026-11-05

Rules/input SHA: `83cf6f1ee244f2e72057332a7ec04ee74db1f0de`.
Worker: Codex independent replay subagent `/root/replay`; delegated model
`gpt-6.1-sol`, medium, confirmed by the orchestrator (resolved runtime
metadata is not independently exposed). The handoff's supplementary Astra
high check is a separate subsequent obligation.
Read AGENTS.md, agents/WORKFLOW.md, agents/codex/CODEX.md, handoff 01,
campaign plan, frozen code, PD-T107 and PD-T108 before execution.
No Git mutations. No novelty content: this is a bounded execution replay
of existing mechanisms, so the novelty-generation scan does not apply.

## Commands actually executed

Working directory `/workspace/padua_research`; Python without `-O`.

```sh
python -m pip install --target /tmp/padua-g0-deps python-flint==0.9.0
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python tracks/mz-constants/code/mz2d_spectra.py --m 10 20 30 40 --crosscheck 10 20 30 40 --output /tmp/padua-g0/spectra.json > /tmp/padua-g0/spectra.log 2>&1
PYTHONPATH=/tmp/padua-g0-deps OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python tracks/mz-constants/code/mz2d_exact.py --m 10 --output /tmp/padua-g0/exact.json > /tmp/padua-g0/exact.log 2>&1
PYTHONPATH=/tmp/padua-g0-deps OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-mz-2d-frontier-20261105/code/g0_replay.py --output /tmp/padua-g0/independent.json > /tmp/padua-g0/independent.log 2>&1
```

Initial pip attempt without network permission failed to reach the proxy;
the same command with tool-granted network permission succeeded. No source
change was needed. Frozen independent_check.py has no `--m` option and its
main writes into the merged topic while requiring older unarchived receipts.
The committed adapter imports its unchanged `region_checks()` and
`nodal_check(10)` instead: actual m10 exact cyclotomic nodal weights,
moments, Gram entries and symbolic continuous integrals are checked.
This intentionally omits the frozen main's stored-m30 witness and malformed
certificate checks, outside G0's m10 scope. No merged topic file is modified.

Environment: Python 3.12.14 (Clang 22.1.3); NumPy 2.3.5; SciPy 1.17.0;
SymPy 1.14.0; python-flint 0.9.0;
Linux-6.18.57-x86_64-with-glibc2.41. Float runner defaults: seed 20261101,
eigsh tolerance 2e-12, ncv 120; both Padua and tensor-CC rules.

## Input identities (SHA-256)

| Input | SHA-256 |
| --- | --- |
| mz2d_exact.py | `5d1f005e2307d3a26badc9c1a44ce313dc9126625a49fba5d59430c151cf9c70` |
| mz2d_independent_check.py | `5e455d747dc5dca84c883ed900095ff4a2bb40767f4ebcb3261d7d583df7bdfc` |
| mz2d_spectra.py | `623acdf06e4ad1c50c3c0562f47f037b8efa15fcc332c2f1ee7a7d0f88ee8b76` |
| Frozen definitions.md | `4ac0e391859a14e4d6f752f1244df0701e99d9b3d8ab8570bd632520f517c7db` |
| g0_replay.py adapter | `15dd56e439504c5834bf640ad19d6029b387115c5838fd23d3f5f5906431882c` |

## Completed results

Exact producer exit 0, m10 n9 dimension 55. Strict rational brackets equal
PD-T107 exactly: minimum `(0.356191,0.356192)` and maximum
`(1.634856,1.634857)`. Inertia counts `(negative,zero,positive)` at lower
and upper endpoints are `(0,0,55)/(1,0,54)` and
`(54,0,1)/(55,0,0)` respectively. All exact strict-dominance assertions
passed. No tolerance is used for those acceptance checks.

| m | Padua minimum | Padua maximum | tensor-CC minimum | tensor-CC maximum |
| --- | --- | --- | --- | --- |
| 10 | 0.3561913826298242 | 1.6348566147837909 | 0.39943363754825034 | 1.0055908851386626 |
| 20 | 0.27223300495805836 | 1.7233137316697678 | 0.3181387355603955 | 1.0046492551513537 |
| 30 | 0.2367055303700448 | 1.7579298559464762 | 0.28191620802341344 | 1.0045206812024878 |
| 40 | 0.21481702946731365 | 1.7780886238837528 | 0.2598490248754978 | 1.0044711207220653 |

Float producer exit 0. Comparison tolerance against the 12-decimal PD-T108
table is absolute 1e-12 (table rounding is 5e-13); all 16 values agree.
All four measured Padua pairs lie strictly inside PD-T107's stated brackets.
Maximum floating eigenpair residual is 2.15e-15. Direct-vs-matrix-free
extrema agree within 7.28e-14, below PD-T108's stated 7.3e-14 diagnostic.
Maximum direct/kernel weight discrepancy is 1.951e-15 (stated 1.96e-15);
operator-vector relative discrepancy is 2.157e-12 (stated 2.16e-12).
These remain floating diagnostics, not certified enclosures.

Independent adapter exit 0, 103.947 seconds: exact nodal m10 check used
66 nodes in the cyclotomic field of order 220 and degree 80; all 276
nodal moments and 3025 nodal-Gram/polynomial-integral pairs agreed exactly.
The separate frozen alias-region regression passed all 1221 moment checks
for m2–12, covering all six regions. These are executed independent
formulation checks, not merely an inspection of producer output.

An additional executed Python comparison parsed the PD-T108 Markdown table
and asserted all 16 values within absolute 1e-12; maximum disagreement was
4.978240042419202e-13. It also asserted exact equality of the two m10
PD-T107 bracket endpoint pairs using Fraction arithmetic. Summary is in
comparison.json below; this calculation does not introduce an additional
mathematical claim or replace the exact producer acceptance.

## Output receipts

Bulk files remain local under `/tmp/padua-g0/`; cold-storage delivery is
pending. These are regenerable outputs, not committed artifacts.

| Output | Bytes | SHA-256 |
| --- | --- | --- |
| exact.json | 3965 | `2e6ff00636922e9d53ee3703e837a61ae49c69959cb76eeef2fd29f0795a134e` |
| spectra.json | 147046 | `04b161a14ef3b690e15843981795c0da692ba374f3ec23aa89ed80658a3e936f` |
| independent.json | 983 | `30bf0ef9badbf5868363977d3dc447dd4207d024a2a4475fc4c250e61c210e9f` |
| comparison.json | 216 | `9afdf3d34bf5d1ac91201c9f53f67f1f03e6c3b2ad15c32e657ac1396587f0ef` |

## Verdict

**PASS G0.** Exact m10 producer, independent m10 nodal checker, and float
m10/20/30/40 replay agree with PD-T107/108 within the stated comparisons.
No mismatch was found. Later gates may proceed. No m>100 computation was performed.
This check adds no mathematical claim and does not replace Claude audit.
