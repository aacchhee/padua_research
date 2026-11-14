from fractions import Fraction as F
n = F(500000); L = F(14)
e_rows = (763*L+86237)/n + F(7082790000)/n**2
e_mesh = (F(449,2)*L+1762)/n + (F(101124,8)*(L+13)+F(1,2))/n**2
e_coll = (62+8*L)/(3*n) + F(6)/n**2
e_int = (3002*L+32803)/n
E = 4*(L+1)/n + F(2,63)*(1+1/n)
D = (10+F(20,3)*(L+1))/n**2
Q = F(7,50)
Efar = e_rows+e_mesh+e_coll+e_int+E+D+Q
claim24 = F(290652925961,525000000000)
print("components", [float(x) for x in (e_rows,e_mesh,e_coll,e_int,E,D,Q)])
print("E_far(n0,L=14) =", Efar, float(Efar))
print("claim24", claim24, float(claim24), "Efar<claim:", Efar < claim24, "Efar==claim:", Efar==claim24)
# (25) at L=131/10, n0
u = F(191,6144); Ll = F(131,10)
d = (F(16,25)*n-28000)/(n+1)
print("d(n0)", d, d == F(292000,500001))
r25 = u*(4*Ll**2-3*Ll)/10 + F(9,10) + d - F(1,1000) - F(8821,3000)
claim25 = F(283876469737,512001024000)
print("rhs25", r25, float(r25), "==claim:", r25 == claim25)
gap = r25 - Efar
claim26 = F(382900852945861,466667600000000000)
print("gap", gap, float(gap), "==claim26:", gap == claim26, "gap - claimed24 version:", r25-claim24, float(r25-claim24))
print("gap>1/2000:", gap > F(1,2000), float(gap - F(1,2000)))
print("C_far parts", F(49,25)+F(1,3000)+F(49,50) == F(8821,3000))
# sensitivity: margin in units
print("margin over 1/2000:", float(gap-F(1,2000)))
# Check C06 component at n=10^6 consistency (sanity vs C06 text)
n6=F(10**6); L6=F(14)
print("C06 interior at 1e6 (3002L+32803)/(n+1):", float((3002*L6+32803)/(n6+1)))
# Exact rationals used: log n0 bounds: log10>23/10, log2<7/10
print("6*23/10-7/10 =", 6*F(23,10)-F(7,10))
