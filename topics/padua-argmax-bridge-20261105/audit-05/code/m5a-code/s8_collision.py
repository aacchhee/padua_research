# M5A s8: does an endpoint-row collision force |x-y| >= pi - v (text), or only rho >= pi - v?
# Construct rho = pi - v with x = y on the s = -y/pi side and test the actual row for cos u = cos v.
import numpy as np
for n in (32, 192, 512):
    m = n + 1
    for j in (2, 3):
        y = 0.4
        s = -y / np.pi; nu = j + s; v = np.pi * nu / m
        x = np.pi - v - y            # rho = x + y = pi - v
        r = 2 * m - j                # actual row with v_r = 2*pi - v
        vr = (r * np.pi + y) / m
        dr = (1 - r) % 2
        u = (dr * np.pi + x + 2 * np.arange(n) * np.pi) / n
        gap = np.min(np.abs(np.cos(u) - np.cos(vr)))
        etap = (0.5 + (x + y - vr) / (2 * np.pi)) % 1.0
        print(f"n={n} j={j}: |x-y|={abs(x-y):.4f}  pi-v={np.pi-v:.4f}  rho={x+y:.4f}  "
              f"eta_+ frac={min(etap,1-etap):.2e}  min|cos u - cos v_r|={gap:.2e}  a={(np.cos(x)+np.cos(y))/2:.4f} <= Pv/2={(np.sin(x)+np.sin(y))*v/2:.4f}")
