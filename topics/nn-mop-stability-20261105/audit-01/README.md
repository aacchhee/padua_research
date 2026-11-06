# Audit-01 independent checker scripts

These are Claude auditor code for [../audit-01.md](../audit-01.md), written independently of the developer's code from the PD-T286 definitions. Exceptions are stated per script: some import a developer module only to score that method, or only to compare against it.

Environment: Python 3.13.18, NumPy 2.5.3, SciPy 1.18.1, mpmath 1.4.1. Run from the repository root. Several scripts assume the clone is at `/home/user/padua_research` (variables `ROOT`/`REPO`); edit that path if it is elsewhere. Scripts in B/ write or read outputs in the directory given by `AUDIT_OUT` (default: the script's own directory).

Raw outputs are not committed. They are regenerable from these commands and stayed in local scratch storage; no archival is claimed.

## claude/ (orchestrator, priority 1)

**`kraw_exact.py 12`**: all checks pass for M = 1..12 (about 3 minutes).
- Formula (5) for four (p1,p2) pairs.
- The terminal derivative (4) and the sign (11).
- The bound (13).
- The proximity derivative, ‖b2‖∞, d_min and the κ bound, for δ ∈ {1/10, 1/37, 1/1000}.

**`kappa_exact.py N`**: the exact mixed-input condition for Krawtchouk.
- N=4..7 gives 4126/25, 77996/45, 307633/25 and 151421899/1250.

## A/ (priority 2)

- **`indep_hahn.py modp|moment|recur <sizes>`** gives exact Hahn normality by three methods.
  - modp: all 61 sizes N=4..64.
  - moment: N=4..32, 40, 48, 63, 64.
  - recur: all 61 sizes.
  - Input and payload fingerprints match the committed receipt.
- **`indep_identity.py`** checks the determinant–divisor identity at 146 sites and a planted zero.
- **`indep_krawtchouk.py`** checks the D1-02 lemmas and gives the exact κ (Krawtchouk N=2..7, Hahn N=4..6).

## B/ (priorities 3–4)

- **`exact_jacobian.py 3 4 5 6 7 8`** gives the exact NN and step-line Jacobians, the induced norms and the mass-null checks.
- **`compare_small.py`** and **`compare_table.py`** compare these against `conditioning.py` and against the committed 61-row table. Result: 0 of 244 cells differ.
- **`chain.sh <family>`** runs the developer producer through the timing wrapper at 260 and then 180 dps, for N=4..64.
- **`trap.py`** checks the path-plus-anchor traps.
- **`d2_compare.py`** gives G0/G1/G2.
- **`marginal_rel.py`** gives the componentwise marginal errors.

## C/ (priorities 5–7)

- **`native_exact_ref.py <sizes>`**: an exact Fraction NN reference that scores the developer's native and C4 outputs.
- **`dyadic_check.py`**: the exact dyadic residual, which is 25700541873527631/2^109.
- **`rank_check.py`**: exact Jacobian rank 3N−2 at N=4 and N=6.
- **`witness_spotcheck.py [all8]`**: exact rebuild of the projection witnesses.
  - It reads `/tmp/backward-projection-{family}-r2-160.json`. Regenerate those first with the 160-dps commands in attempts/D5.md.

## D/ (priorities 8–9)

- **`exact_core.py`**: an exact PD-T286 library.
- **`check_integrable.py`**: Christoffel (40 cases), Toda (25 cases), the counterexample, the exponential path and the cross-ratio check.
- **`check_predivide.py <repo-root> 4 6 8 10 12 14 16`**: the predivide-C4-restore check against an exact reference.
- **`check_dictionary.py`**: the D6 graph identity and the obstructions.

## E/ (records)

- **`verify.py`**: recomputes SHA-256, Git blob and bytes for every evidence-manifest row. All 49 match.
