# Independent recomputation of uc:base-values from the paper's formulas, using decimal (80 digits).
import re, sys
from decimal import Decimal as D, getcontext
getcontext().prec = 80
def pi():
    # Machin
    def arctan_inv(x):
        x=D(x); s=D(0); t=1/x; k=0; x2=x*x
        while True:
            term=t/(2*k+1)
            if term < D(10)**-78: break
            s += term if k%2==0 else -term
            t/=x2; k+=1
        return s
    return 16*arctan_inv(5)-4*arctan_inv(239)
PI=pi()
def vals(n):
    n=D(n); m=n+1; L=n.ln(); Lb=1+L
    T=(4*L*L-3*L)/PI**2; b0=4/PI**2; r0=D('2.5').ln()+D(1)/18
    Dd=((52/PI**2)*Lb+7)/n+10/n**2+20*Lb/(PI*n**2)
    Mm=b0*(2*L+2*r0)/n+(4+b0*(L+1/n))/(4*n**2-1)+b0/(2*n-1)**2+(5+b0*((n+D('0.5')).ln()+2))/(4*(n-D('0.5'))**2)
    eb=Dd+Mm+1/n
    KD=((6+16/(3*PI))*Lb+2/PI)/n
    A4=4/n+40*Lb/(PI*n**2); C4=A4+20/n**2; db=(17*L+27)/n**2
    kWx=((D(19)/2)*Lb+(D(23)/3)*L+D(155)/2)/n+152/n**2; kWy=kWx+db
    Wn=(3*m.ln()+D(2).ln()+2*PI.ln()+2)/(PI*m)
    gn=1+(2+8*m/(3*PI)).ln(); MA=1/PI+4/PI**2
    Gg=(7*MA*L+D(111)/2+(63+D(2).ln()+4*PI.ln()+7*m.ln())/PI+(16*(2*m).ln()+D(3)/2*gn)/PI)/m
    CE=Dd+Gg+(64+16*L)/n+318/n**2+Mm+Wn
    Mn=(4*L*L+D(79)/5*L)/PI**2+D(9)/4+CE+2*KD
    U=T-eb+A4+D(23)/250
    return {'L':L,r'\mathfrak T':T,r'\bar e':eb,'K_D':KD,r'\overline C_E':CE,'C_4':C4,'k_{Wx}':kWx,'k_{Wy}':kWy,r'd_\beta':db,'M(n)':Mn,'U_*':U,'d_x':11*U/48-D(5)/12,'d_y':11*U/48,r'\ell_x':kWx+D(5)/48,r'\ell_y':kWy}
src=open(sys.argv[1]).read().split(r'\label{uc:base-values}')[1].split(r'\end{tabular}')[0]
cols=None; ok=bad=0
for row in src.split(r'\\'):
    cells=[c.strip() for c in row.replace(r'\midrule','').replace(r'\toprule','').replace(r'\bottomrule','').split('&')]
    if len(cells)!=3: continue
    if cells[0].endswith('Quantity'): cols=[int(c.strip('$')) for c in cells[1:]]; continue
    sym=cells[0].strip('$')
    for n,c in zip(cols,cells[1:]):
        lo,hi=re.fullmatch(r'\$\[(.*),(.*)\]\$',c).groups(); v=vals(n)[sym]
        tight = (D(hi)-D(lo))==D('0.000001')
        if D(lo)<=v<=D(hi) and tight: ok+=1
        else: bad+=1; print('MISMATCH',n,sym,lo,hi,v)
print('entries ok',ok,'bad',bad)
for n in (192,512): print(n, {k:str(+v)[:12] for k,v in list(vals(n).items())[:4]})
