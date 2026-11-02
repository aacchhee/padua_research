"""Auditor's exact-rational recomputation of theorem 07 / r03 bookkeeping (independent of d1_constants_r03.py)."""
from fractions import Fraction as Fr
import math, json
r = Fr(3, 2)                      # sup m/n for n>=2
zeta2_ub, zeta3_ub = 2, 2         # sum L^-2, sum L^-3 upper bounds used
# derivative coefficient constants (from hand differentiation, see report)
fi_coef = Fr(3, 2)                # |f_u|,|f_v| <= (3/2) b^-1 t^-2  (paper uses 2)
fij_coefs = (Fr(9, 4), Fr(9, 2))  # mixed: 9/4 t^-2 (<= b^-2 t^-2), 9/2 b^-1 t^-3 (paper uses 8,8)
# geometric lower bounds b>=d/(2m), t>=L/(4m); multiplicity 4 per (|L|,d); 2m pairs per L, 4m per d (paper)
S_b1t2 = 32 * 4 * zeta2_ub        # coefficient of m^3 H
S_b2t2 = 64 * 4 * zeta2_ub * 2    # coefficient of m^4 (sum d^-2<=2)
S_b1t3 = 128 * 4 * zeta3_ub       # coefficient of m^4 H
assert (S_b1t2, S_b2t2, S_b1t3) == (256, 1024, 1024)
f_grad = 2 * S_b1t2 * r**2                      # /(n^2 m) normalisation
f_hess = 8 * (S_b2t2 + S_b1t3) * r**3           # uses H>=1: 1024+1024H <= 2048H
g_val = (2 * 4 + 4 * 2) * r                     # sum t^-1+b^-1 <= (2m*4m*H + 4m*2m*H) = 16 m^2 H
g_grad = (2 * 16 * 2 + 4 * 4 * 2) * r**2        # 64+32 = 96 m^3
g_hess = (2 * 64 * 2 + 4 * 8 * 2) * r**3        # 256+64 = 320 m^4
table = dict(f_grad=f_grad, f_hess=f_hess, g_val=g_val, g_grad=g_grad, g_hess=g_hess)
assert table == dict(f_grad=1152, f_hess=55296, g_val=24, g_grad=216, g_hess=1080), table
# path second derivative with rho<=1:  rho^2[ f_hess H + rho(f_grad/2 + f_grad) H + 2*(g_val/2 rho H + g_grad + g_hess/2 rho)]
H_min = 1 + math.log(3)
coefH = f_hess + Fr(1, 2) * f_grad + f_grad + 2 * (g_val / 2)     # coefficient of H (rho<=1)
const = 2 * (g_grad + g_hess / 2)                                 # constant term
path_rho1 = float(coefH + const)       # using const <= const*H since H>=1
path_rho64 = float(f_hess + (Fr(1, 64)) * (Fr(3, 2) * f_grad + g_val)) + float(2 * (g_grad + g_hess / 128)) / H_min
regular = 2 * 59000 * 2                # two pairs, H<=2 log m for m>=3
near = 8 * (21 * 16)                   # 8 * 336 -> rho^2 H
near_lin = 8 * 16
far32 = 8 * 256
far_lin = 8 * 64
coll = 10 / math.log(3)
total = regular + 2 * near + coll
out = dict(table={k: int(v) for k, v in table.items()}, path_coefficient_rho_le_1=path_rho1,
           path_coefficient_rho_le_1_64_effective=path_rho64, regular=regular,
           near_rho2H=near, near_rho2_logm=2 * near, near_lin_rhoH_over_n=near_lin,
           far_rho32=far32, far_lin=far_lin, linear_total=near_lin + far_lin,
           collision_over_log3=coll, quadratic_total=total, below_242000=total < 242000,
           below_240000=total < 240000,
           B_family=dict(Dprime=float(Fr(1, 2) * (2 * r + Fr(5, 4) * r**2 + Fr(13, 4))), Dprime_claim=145 / 32,
                         Dsecond=float(Fr(1, 4) * (3 * r + 4 * r**2 + Fr(5, 4) * r**3 + Fr(33, 4))), Dsecond_claim=831 / 128,
                         F0_lower=4 / (3 * math.pi**2), F_lower_after_grad=4 / (3 * math.pi**2) - 3 / 64,
                         claim_lower=2 / (3 * math.pi**2), V2_at_n2=125 * 4 / 64 + 25 * 2 / 16 + 1),
           sqrt_rho_log=(1 / 8) * (1 + math.log(64)),
           scale=dict(first_term=27 * 2048**4 / (32 * (1e7**2 / 100)**3), d_delta=(1 - math.cos(math.pi / 8)) / 4096,
                      rho_delta=(1 - math.cos(math.pi / 8)) / 4, W_check=(1e7**2 / 25 - 242000 * (1e7 + .5) - 27 / 5) >= 1e7**2 / 100))
print(json.dumps(out, indent=1))
