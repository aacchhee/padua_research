# P4 audit code (journal paper, audit-04)

Auditor: Claude Opus 5.5 (xhigh), read-only subagent. Sources read at branch head
70a50d7b2a72a30fd7a2af3b2ead54ae14470bf9; paper TeX/Bib unchanged since freeze
24a98db4c3c4c4d0eede2e3929532956df87911b (`git diff --stat 24a98db HEAD -- paper` touches only
README.md and BUILD.md). All scripts implement the paper's displayed formulas directly; none
imports repository or archive code. Results are MEASURED (floating mpmath at 30-50 digits) except
`exact.py` (Python Fraction, exact). Total CPU about 0.5 min.

| Script | Command | Exit | Wall | Output |
|---|---|---|---|---|
| gates.py | `PYTHONPATH=../../audit3/pylib python3 -B gates.py` | 0 | 20.8 s | gates.out |
| exact.py | `python3 -I -B exact.py` | 0 | <1 s | exact.out (38/38 PASS) |
| n2_and_kernel.py | `PYTHONPATH=../../audit3/pylib python3 -B n2_and_kernel.py` | 0 | 1.3 s | n2_and_kernel.out |
| sec3.py | `PYTHONPATH=../../audit3/pylib python3 -B sec3.py` | 0 | ~3 s | sec3.out |

mpmath 1.3.0 / sympy 1.14.0 from the audit-03 pylib; Python 3 system interpreter.
`png/` holds two 70-dpi renders (pp. 16, 48) of B4's fresh build `../build/paper/main.pdf`
(51 pages, SHA-256 ad416ae0...e21d; byte difference from the recorded 1346fc28... is expected).
