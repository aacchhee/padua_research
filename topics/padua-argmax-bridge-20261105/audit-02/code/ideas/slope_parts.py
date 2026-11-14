"""Split the E14 per-unit-rho slopes kNx (half-near) and kWx (wide) into their telescope sources."""
import math
for n in [320, 256, 200, 160]:
    L = math.log(n); H = 1 + L
    parts = {'ordinary rows (8H+10)/n': (8*H+10)/n,
             'retained N (3H/2+16/5+7)/n+82/n^2': (1.5*H+3.2+7)/n+82/n**2,
             'Tout near ((23/3)L+47)/n': (23/3*L+47)/n,
             'Rmesh 1/(2n)': 0.5/n}
    tot = sum(parts.values())
    print(f"n={n} kNx={tot:.4f}: " + '; '.join(f"{k}={v:.4f} ({100*v/tot:.0f}%)" for k, v in parts.items()))
    w = {'ordinary': (8*H+10)/n, 'retained W (3H/2+6+11)/n+152/n^2': (1.5*H+17)/n+152/n**2,
         'Tout wide ((23/3)L+50)/n': (23/3*L+50)/n, 'Rmesh': 0.5/n}
    tw = sum(w.values())
    print(f"      kWx={tw:.4f}: " + '; '.join(f"{k}={v:.4f} ({100*v/tw:.0f}%)" for k, v in w.items()))
