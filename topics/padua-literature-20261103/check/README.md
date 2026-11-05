# Consistency checks (not registered claims)

- `svz_table1.py`, by the P2 reader (Claude Opus 5.5 high). It computes the signed Padua cubature weights in double precision for m = 5, 10, …, 40. It compares the correct normalisation 2/(m(m+1)) with the denominator printed in Sommariva–Vianello–Zanovello 2008, eq. (25), which is 1/((n+2)(n+3)) with n = m−1. It also lists the negative weights.
  - Rerun by the orchestrator, 2026-11-03: `python3 -I topics/padua-literature-20261103/check/svz_table1.py`, with numpy, in the cloud workspace.
  - Output: the weights sum to 4 (to 1e-15) under the correct denominator, and to 4·m/(m+2) under the printed one. For m = 3, 4, 5, 10 and 40 the only negative weights sit at two corners.
  - This is a floating-point consistency check only, MEASURED-level evidence for a literature locator (a typographical error in the source). It is not a mathematical claim of this topic. The comparison with SVZ Table 1 digits was made by the P2 reader against the journal page.
