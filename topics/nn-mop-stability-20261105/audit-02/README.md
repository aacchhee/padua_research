# Audit-02 independent checker scripts

These are Claude auditor code for [../audit-02.md](../audit-02.md). Environment: Python 3.13.18, NumPy 2.5.3, SciPy 1.18.1, mpmath 1.4.1. Run from the repository root, with a copy of the committed reference where a script asks for one. Some scripts assume the clone is at `/home/user/padua_research`. Raw outputs are not committed; they are regenerable.

## R1 (M3, MINOR 12)

- **`my_rebuild.py <reference> [cases]`** rebuilds all 12 projection witnesses exactly. It is independent Fraction code with polynomial-projection extraction. Every stored metric is reproduced with relative difference 0.
- **`my_stationarity_exact.py <reference>`** computes exact implicit-derivative stationarity. It matches all six N4 values bitwise, and Krawtchouk N8 LU. The remaining N8 runs were stopped unfinished.
- **`target_regen.py`** and **`refit_probe.py`** are platform probes that re-execute the developer's code. They are corroboration only, not independent checks.

## R2 (MINOR 11)

- **`local_lemma.py`** and **`run2.py`** test the localized NN lemma exactly. They use 19 tuned cases with a deliberately singular index, N=5..8.
- **`run3.py`** runs the certificate implication on 60 random rational inputs, N=3..7.
- **`zeros.py`** checks the exact N4 zero coefficients.

## R3 (M2, MINOR 14)

- **`numdiff.py`** is a token-level numeric diff of changed records between `4e87fc0` and `d6760d7`.
- **`zeros.py`** checks the exact N4 zero b coefficients.
