"""Exact-rational and interval re-checks of the two scoped negative
allocation statements (E08-allocation-obstruction, E12-assembly256-
obstruction) plus I4 bounds.  Auditor m3, Claude Opus 5.5 xhigh.
Run: PYTHONPATH=<audit2>/pylib python3 -P obstructions.py
"""
from fractions import Fraction as Fr
from mpmath import iv, mp, quad, sqrt as msqrt
iv.prec = 200; mp.prec = 200
ok = True
def chk(name, c):
    global ok; ok &= bool(c); print(('PASS ' if c else 'FAIL ') + name)
PI = iv.pi
def I(q): return iv.mpf(q.numerator) / iv.mpf(q.denominator)
# --- E08 near witness at n=384
s = Fr(1, 96) + Fr(1379, 6912) + Fr(1, 32) + Fr(11, 324) + Fr(13, 1296) - Fr(3, 16)
chk('E08 P384 rational sum %s == 25/256' % s, s == Fr(25, 256))
chk('E08 25/256-9/100 == 49/6400', Fr(25, 256) - Fr(9, 100) == Fr(49, 6400))
chk('E08 Fh numerator (2303/5000)(35/36)-(471/1250)/3 == 57997/180000', Fr(2303, 5000) * Fr(35, 36) - Fr(471, 1250) / 3 == Fr(57997, 180000))
chk('E08 (539/1936)*57997/180000 == 31260383/348480000 < 9/100', Fr(539, 1936) * Fr(57997, 180000) == Fr(31260383, 348480000) and Fr(31260383, 348480000) < Fr(9, 100))
chk('E08 GO384 bound 611/384-461/250 == -12137/48000', Fr(611, 384) - Fr(461, 250) == Fr(-12137, 48000))
chk('E08 461/250 == 101/250+97/100+13/100+17/50', Fr(101, 250) + Fr(97, 100) + Fr(13, 100) + Fr(17, 50) == Fr(461, 250))
# interval: actual R(1/6,1/6) of D10 majorant vs written lower
x = iv.mpf(1) / 6
R = I(Fr(15, 32)) * x**iv.mpf(1.5) + I(Fr(4, 9)) * x**2 * (1 + iv.log(1 / x)) + I(Fr(1, 9)) * x**2 * (I(Fr(3, 2)) + iv.log(1 / x))
chk('E08 R(1/6,1/6) > 1/32+11/324+13/1296 (interval)', R.a > I(Fr(1, 32) + Fr(11, 324) + Fr(13, 1296)).b)
# n=384 kNx lower and T upper
n = iv.mpf(384); L = iv.log(n); H = 1 + L
kNx = ((I(Fr(19, 2))) * H + I(Fr(29, 2)) * L + I(Fr(1163, 15))) / n + 82 / n**2
chk('E08 kNx(384) > 1379/2304 (interval)', kNx.a > I(Fr(1379, 2304)).b)
T = (4 * L**2 - 3 * L) / PI**2
chk('E08 T(384) < 13 (interval)', T.b < 13)
# --- E12 near witness at n=256
s2 = Fr(1, 64) + Fr(10297, 46080) + Fr(1, 50) - Fr(1, 100) - Fr(5, 32)
chk('E12 P256 rational sum %s == 21389/230400' % s2, s2 == Fr(21389, 230400))
chk('E12 21389/230400 == 9/100+653/230400', Fr(21389, 230400) == Fr(9, 100) + Fr(653, 230400))
chk('E12 Bbeta product (1/36)(72/71)(20/197)(661/200)<1/100', Fr(1, 36) * Fr(72, 71) * Fr(20, 197) * Fr(661, 200) < Fr(1, 100))
n = iv.mpf(256); L = iv.log(n); H = 1 + L
kNx = ((I(Fr(19, 2))) * H + I(Fr(23, 3)) * L + I(Fr(677, 10))) / n + 82 / n**2
chk('E12 kNx(256) > 10297/15360 (interval)', kNx.a > I(Fr(10297, 15360)).b)
T = (4 * L**2 - 3 * L) / PI**2
chk('E12 T(256) < 271/25 (interval)', T.b < I(Fr(271, 25)).a)
t = iv.mpf(1) / 6; a = iv.cos(t); p = iv.sin(t); u = 1 - a
chk('E12 u=1-cos(1/6) < 1/72', u.b < I(Fr(1, 72)).a)
c0 = p / a
chk('E12 c0=tan(1/6) in (1/6, 12/71)', c0.a > I(Fr(1, 6)).b and c0.b < I(Fr(12, 71)).a)
# actual Bbeta integral (measurement: mp quad), compared with the written bound
mp.dps = 40
af = mp.cos(mp.mpf(1) / 6); pf = mp.sin(mp.mpf(1) / 6)
b = 2 * mp.atan(pf / (2 * af))
Bb = 4 / mp.pi**2 * quad(lambda e: (pf / 2 - af * mp.tan(e / 2)) * (-mp.log(mp.sin(e))), [0, b])
print('measurement: Bbeta(1/6,1/6) quad =', mp.nstr(Bb, 12), '(written upper 1/100)')
chk('E12 Bbeta quad < 1/100 (measurement)', Bb < mp.mpf(1) / 100)
# --- I4
I4 = quad(lambda z: msqrt(1 - z**4), [0, 1])
print('measurement: I4 =', mp.nstr(I4, 15))
chk('I4 in (4/5, 319/360) (measurement)', mp.mpf(4) / 5 < I4 < mp.mpf(319) / 360)
print('ALL PASS' if ok else 'SOME FAIL')
raise SystemExit(0 if ok else 1)
