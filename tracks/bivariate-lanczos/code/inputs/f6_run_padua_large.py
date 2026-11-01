import sys, numpy as np
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import f6_givens_vs_hl_deficit as F
rng = np.random.default_rng(2)
for n in [int(a) for a in sys.argv[1:]]:
    P = F.padua(n); N = len(P)
    F.run_case(f"Padua n={n} N=M={N}", P, np.ones(N), N, ["given", "random"], rng)
    # Padua cubature-like weights: use random positive weights as a check of weight dependence
    F.run_case(f"Padua n={n} randW", P, rng.uniform(0.1, 1, N), N, ["given"], rng)
