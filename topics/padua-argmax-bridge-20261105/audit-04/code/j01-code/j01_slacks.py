import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as F
import j01_own as J
def d20(iv):
    s=10**20; lo=iv.lo.numerator*s//iv.lo.denominator; hi=-((-iv.hi).numerator*s//(-iv.hi).denominator)
    f=lambda k:('-' if k<0 else '')+str(abs(k)//s)+'.'+str(abs(k)%s).zfill(20)
    return f'[{f(lo)}, {f(hi)}]'
r=J.relative(512)
print('slack 41/1000-maxP512   ', d20(F(41,1000)-r['peak_b']))
print('slack -1/7-P512(1/2)    ', d20(-F(1,7)-r['half']))
print('slack 1/2-vertex512     ', d20(F(1,2)-r['vert_b']))
print('slack d1(512)-1         ', d20(r['d1']-1))
print('slack 5/48-db(512)      ', d20(F(5,48)-r['db']))
g1=J.gate(512,J.sin_q(F(1,2)),J.cos_q(F(1,2)))
print('slack G(512,1)-1/2      ', d20(g1['Glin']-F(1,2)))
print('slack tan(1/2)-C/Theta  ', d20(J.sin_q(F(1,2))/J.cos_q(F(1,2))-g1['ratio']))
c=J.consts(192); Th=c['T']+J.J0; C=J.T0+2*c['KD']; rh=F(707107,10**6)
g2=Th*(1-rh)-C*rh-J.T0**2*rh/(2*Th)-c['CE']-c['ebar']
print('slack G192 (707107 subst)-3/100', d20(g2-F(3,100)))
g2e=J.gate(192,J.INV_SQRT2,J.INV_SQRT2)
print('slack G192 (exact 1/sqrt2)-3/100', d20(g2e['Glin']-F(3,100)))
print('slack 1-C/Theta(192)    ', d20(1-g2e['ratio']))
fl=J.floor_band(295)[0]; print('slack Fh(295)-1/20 exact', fl-F(1,20), float(fl-F(1,20)))
fl4=J.floor_band(294)[0]; print('Fh(294)-1/20 exact', fl4-F(1,20), float(fl4-F(1,20)))
