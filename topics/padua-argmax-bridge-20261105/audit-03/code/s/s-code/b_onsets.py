# ENCLOSED (arb) first closing integer n for each simplified gate, scanning n upward (base check only).
from b_arch_arb import consts, wide_poly, closed_gate, tail_floors, F, j, t0, arb, A
import flint
def first(pred, lo, hi):
    for n in range(lo, hi):
        if pred(n): return n
def near_uniform(n):
    c = consts(n); e, f, g = wide_poly(c); return (F(1, 20) - (c['C4'] + g + f**2/(4*e))).lower() > 0
def wide_neg(n):
    c = consts(n); e, f, g = wide_poly(c); return (-(c['C4'] + g + f/2 - e/4)).lower() > 0 and (f/(2*e)).upper() < F(1, 2)
def outer_crude(n):
    c = consts(n); return (F(47, 384)*(c['T'] + j) - t0 - c['CE'] - 2*c['KD'] - c['ebar']).lower() > 0
def outer_closed(n):
    return closed_gate(consts(n), A(1)).lower() > 0
def floor20(n):
    c = consts(n); return all((x - F(1, 20)).lower() > 0 for x in tail_floors(c, F(1, 2)))
def far_closed(n):
    from b_arch_arb import pi
    return (closed_gate(consts(n), pi/2) - F(3, 100)).lower() > 0
print('uniform 1/20 floor from (ul:tail-floors) at r=1/2 holds from n =', first(floor20, 64, 2000))
print('near gate  max P(rho<=1/2) < 1/20 (wide column, relaxed) from n =', first(near_uniform, 300, 2000))
print('wide gate  P(1/2)<0 and vertex<1/2 from n =', first(wide_neg, 300, 2000))
print('outer crude (u1(T+j)-t0-CE-2KD-ebar>0) from n =', first(outer_crude, 300, 2000))
print('outer closed form G(n,1)>0 from n =', first(outer_closed, 300, 2000))
print('far closed form G(n,pi/2)>3/100 from n =', first(far_closed, 100, 400))
