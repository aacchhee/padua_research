# Claude audit-01 supporting checks

Auditor-written checkers (not developer code), run 2026-11-01, Python 3.13.18,
SymPy 1.14.0, mpmath 1.3.0, from any directory with `python3 -I <script>`.

| Script | Output | Scope |
|---|---|---|
| aud_a1.py | outputs/aud_a1.json | A1 cardinal-level check, monomial Vandermonde, mpmath 80 dps, n=1..10 (MEASURED) |
| aud_b5.py | outputs/aud_b5.out | B5 exact QQ nullity of the full patterned commutator system; witnesses, random, Padua n=2 control |
| aud_a5.py | outputs/aud_a5.json | A5 local certificate, mpmath iv intervals directly in angle variables on l_inf box 0.0022 |

See ../../audit-01.md for interpretation. SHA-256 in SHA256SUMS.txt.
