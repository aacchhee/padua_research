#!/usr/bin/env python3
"""Independent diagnostic arithmetic for N1/N2/N5. No proof by sampling."""
from fractions import Fraction as F
import hashlib, json, pathlib, platform
import mpmath as mp

ROOT=pathlib.Path(__file__).resolve().parents[3]
TOPIC=pathlib.Path(__file__).resolve().parents[1]
OUT=ROOT/'local-output/argmax-bridge-20261105/check-rows'
mp.mp.dps=100

def real(x): return mp.mpf(x.numerator)/x.denominator

def cheb(x,n):
    a=[mp.mpf(1),x]
    for k in range(2,n+1): a.append(2*x*a[-1]-a[-2])
    return a[:n+1]

def kernel(n,u,v):
    tx,ty=cheb(mp.cos(mp.pi*real(u)),n),cheb(mp.cos(mp.pi*real(v)),n)
    return mp.fsum((1 if a==0 else 2)*(1 if b==0 else 2)*tx[a]*ty[b]
                   for a in range(n+1) for b in range(n+1-a))-tx[n]

def W(t):
    if t==0 or t==mp.pi: return -mp.log(mp.pi)
    return mp.log(mp.sin(t)/(t*(mp.pi-t)))

def wp(t):
    if t==0 or t==mp.pi: return -mp.mpf(1)/3+1/mp.pi**2
    return -1/mp.sin(t)**2+1/t**2+1/(mp.pi-t)**2

def block_model(n,points):
    if not points: return mp.mpf(0)
    h=mp.pi/n
    points=sorted(points)
    blocks=[]
    for x in points:
        if not blocks or x-blocks[-1][-1]!=F(1,n): blocks.append([x])
        else: blocks[-1].append(x)
    ans=mp.mpf(0)
    for block in blocks:
        l=mp.pi*real(block[0])-h/2
        r=mp.pi*real(block[-1])+h/2
        pole=mp.fsum(1/(mp.pi*real(x))-1/(mp.pi*(1-real(x))) for x in block)
        ans+=pole+(W(r)-W(l))/h-h*(wp(r)-wp(l))/24
    return ans

def one_case(n,alpha,beta):
    m=n+1; A=mp.cos(mp.pi*real(alpha))+mp.cos(mp.pi*real(beta))
    p,q=mp.sin(mp.pi*real(alpha)),mp.sin(mp.pi*real(beta))
    signed=absolute=model=mp.mpf(0)
    maxrow=maxcot=maxcollision=mp.mpf(0); collisions=negcollisions=0
    for r in range(2*m):
        d=(1-r)%2; v=(F(r)+beta)/m
        us=[(F(d)+alpha)/n+F(2*k,n) for k in range(n)]
        vals=[(-1)**d*kernel(n,u,v)/2 for u in us]
        signed+=sum(vals); absolute+=sum(abs(z) for z in vals)
        if beta==0 and r==0: expected=n*(A/2-m)
        elif beta==1 and r==2*m-1: expected=n*(A/2+m)
        else: expected=n*(A/2-q*mp.cot(mp.pi*real(v)/2)/2)
        maxrow=max(maxrow,abs(sum(vals)-expected))
        if r in (0,2*m-1):
            model+=sum(abs(z) for z in vals); continue
        cm=(p-q-A*mp.cot(mp.pi*real(v)/2))/4
        cp=(p+q+A*mp.cot(mp.pi*real(v)/2))/4
        minus=[]; plus=[]; correction=mp.mpf(0)
        for u,z in zip(us,vals):
            collision=(u-v)%2==0 or (u+v)%2==0
            if collision:
                collisions+=1; correction+=2*max(-z,0)
                if z < -mp.mpf('1e-80'): negcollisions+=1
                if v%1:
                    eps=1 if (u-v)%2==0 else -1
                    c=((eps*n*p-m*q)/mp.sin(mp.pi*real(v))-mp.cos(mp.pi*real(alpha)))/2
                    maxcollision=max(maxcollision,abs(c-z))
                continue
            f=cm*mp.cot(mp.pi*real((u-v)/2))+cp*mp.cot(mp.pi*real((u+v)/2))
            maxcot=max(maxcot,abs(f-z))
            numer=A*(1+mp.cos(mp.pi*real(v)))+q*mp.sin(mp.pi*real(v))-p*mp.sin(mp.pi*real(u))
            denom=mp.cos(mp.pi*real(u))-mp.cos(mp.pi*real(v))
            if abs(z)>mp.mpf('1e-70'): assert (numer*denom<0)==(z<0)
            if z < -mp.mpf('1e-70'):
                minus.append(((u-v)/2)%1); plus.append(((u+v)/2)%1)
        model+=expected-2*cm*block_model(n,minus)-2*cp*block_model(n,plus)+correction
    bound=7*mp.pi**4/(1800*n**4)+7*mp.pi**3*mp.harmonic(n)/(900*n**4)
    err=abs(absolute-model)/(n*m)
    assert err<=bound
    assert max(maxrow,maxcot,maxcollision,abs(signed/(n*m)-mp.cos(mp.pi*real(alpha))))<mp.mpf('1e-60')
    return dict(n=n,alpha_pi=str(alpha),beta_pi=str(beta),collisions=collisions,negative_collisions=negcollisions,
                model_error=mp.nstr(err,30),bound_ratio=mp.nstr(err/bound,30),max_row_residual=mp.nstr(maxrow,10),
                max_cot_residual=mp.nstr(maxcot,10),max_collision_residual=mp.nstr(maxcollision,10))

def main():
    phases=[(F(0),F(0)),(F(1),F(0)),(F(0),F(1)),(F(1,2),F(1,2)),
            (F(0),F(1,7)),(F(1,7),F(0)),(F(1,7),F(2,7)),
            (F(1,10**20),F(1,10**20)),(F(1,3),F(2,3)-F(1,10**20))]
    rows=[]
    for n in (2,3,5,8):
        extra=[(F(k,2*n+1),1-F(k,2*n+1)) for k in range(1,2*n+1)]
        for r in range(2*(n+1)):
            v=(F(r)+F(1,7))/(n+1)
            for j in range(2*n):
                if (j+r)%2==1:
                    for eps in (-1,1):
                        alpha=(eps*n*v-j)% (2*n)
                        if 0<=alpha<=F(6,7): extra.append((alpha,F(1,7)))
        for a,b in sorted(set(phases+extra)): rows.append(one_case(n,a,b))
    quartic=F(1,80)-F(1,24)
    assert quartic==-F(7,240) # functional on t^4, fourth derivative 24
    assert quartic/24==-F(7,5760)
    # Exact mass construction, including zero sign masses.
    transport_cases=[([F(0),F(0)],[F(0)]),([F(1),F(0)],[F(1,3),F(2,3)]),
                     ([-F(2),F(3),F(0)],[-F(1,2),F(3,2)]),([-F(2)],[-F(1),F(0)])]
    for v,w in transport_cases:
        P=sum(max(x,0) for x in v); Q=sum(max(-x,0) for x in v)
        mat=[[max(y,0)/P if x>0 else max(-y,0)/Q if x<0 else F(0) for x in v] for y in w]
        assert [sum(a*x for a,x in zip(row,v)) for row in mat]==w
        assert all(sum(row[j] for row in mat)<=1 for j in range(len(v)))
    OUT.mkdir(parents=True,exist_ok=True)
    raw=OUT/'independent-high-precision.json'
    raw.write_text(json.dumps(rows,indent=2)+'\n')
    files=[TOPIC/'code/check_rows_independent.py']+sorted((TOPIC/'theory').glob('N[1245]-*.md'))
    receipt=dict(status='MEASURED independent diagnostics; written mathematical review is separate',
        rules_sha='0bca52bc1b8edf2e91d3749b710d2df285dc3e6b',python=platform.python_version(),mpmath=mp.__version__,decimal_digits=100,
        cases=len(rows),degrees=[2,3,5,8],collisions=sum(r['collisions'] for r in rows),negative_collisions=sum(r['negative_collisions'] for r in rows),
        max_model_error_ratio=max(float(r['bound_ratio']) for r in rows),exact_peano_constant='7/5760',exact_transport_cases=len(transport_cases),
        sources={str(f.relative_to(ROOT)):hashlib.sha256(f.read_bytes()).hexdigest() for f in files},
        raw=dict(path=str(raw.relative_to(ROOT)),sha256=hashlib.sha256(raw.read_bytes()).hexdigest(),bytes=raw.stat().st_size),
        limits='No outward rounding, continuum certificate, B3 pass, compact-degree model, or Claude audit.')
    target=TOPIC/'evidence/independent-rows-diagnostics.json'
    target.write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({k:receipt[k] for k in ['cases','collisions','negative_collisions','max_model_error_ratio','exact_peano_constant']}))

if __name__=='__main__': main()
