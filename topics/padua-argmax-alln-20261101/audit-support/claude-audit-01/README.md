# Claude audit-01 support evidence

This is the support evidence for [audit-01](../../audit-01.md) (handoff 05). It was audited at scientific input `c173fbf7ee66f02cc1d992e52edb43fdbd819474`, with rules read at `9fcdc2199a44393f522958b36ecadbec57e2de9b`.

## Contents

- **`subaudit-reports/A.md` … `F.md`**
  - These are the six Claude Opus 5.5 xhigh sub-auditors' returned reports.
  - The sub-agents could not write files, so the orchestrator saved condensed copies.
  - The condensing kept every finding, verdict, command and hash.
- **`orchestrator/`**
  - `run_min.sh` and its `summary.txt` and `run_min.log`: the handoff-05 minimum command set.
  - Small receipts: n8/n12/pairing/d2-symbolic/D3 check JSONs.
  - `G/`: the T1–T4 and pairing replay comparisons, with their summaries.
- **`files/<A–F>/`**
  - The sub-auditors' own scripts (independent kernels and checks) and their small outputs.
  - Inside them, absolute paths refer to the session scratch root `…/scratchpad/audit01/`.
- **`manifest.json`**
  - sha256 and size of every committed file.
  - sha256 and size of every scratch file, including those not committed. Those are the full replay JSONs that duplicate developer evidence, the 860 KB D1 screen replay, and a 200 KB tree-size listing.

## Status and limits

- These records are audit evidence. They add no mathematical claim.
- The independent kernels are unreviewed code, and they trust `mpmath.iv` and Python integers.
- The scratch-only files were ephemeral and are not archived in cold storage.
