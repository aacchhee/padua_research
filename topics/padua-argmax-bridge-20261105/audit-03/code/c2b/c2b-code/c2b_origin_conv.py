import numpy as np, importlib.util, sys
spec = importlib.util.spec_from_file_location("rows", "c2b_rows.py")
src = open("c2b_rows.py").read().split("# --- 1.")[0]
exec(src)
for n in (32, 161):
    for eps in (1e-3, 1e-4, 1e-5, 1e-6):
        for (x, y) in ((eps, eps), (eps, 0.3*eps), (0.2*eps, eps)):
            S = setup(n, x, y); m = S["m"]
            Jc = (row_sum(S, m-1)[0] + row_sum(S, m)[0])/(n*m)
            print(f"n={n} x={x:.1e} y={y:.1e}  m*J_cen-2 = {m*Jc-2:+.3e}")
