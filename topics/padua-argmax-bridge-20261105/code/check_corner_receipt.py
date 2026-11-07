#!/usr/bin/env python3
"""Collect independent exact corner replay; --run rebuilds and executes the checker."""
from pathlib import Path
from fractions import Fraction as Q
import argparse, ctypes, datetime, hashlib, json, platform, subprocess
ROOT=Path(__file__).resolve().parents[3]
TOPIC=Path(__file__).resolve().parents[1]
OUT=ROOT/'local-output/argmax-bridge-20261105/check-corner'
SOURCE=TOPIC/'code/check_corner_exact.cpp'
BINARY=OUT/'check_corner_exact'
HISTORY=OUT/'initial-withdrawn'
BUILD=['g++','-O2','-std=c++17','-Wall','-Wextra','-Werror',str(SOURCE),'-lgmpxx','-lgmp','-o',str(BINARY)]
PINS={
 'theory/N3-corner-radius-reduction.md':'8cf89c491a4d82df81a69bd1024139d1224bd1f43fd91b1d1fe58a1dd519aee4',
 'theory/N3-corner-bounds.md':'7241cd4221643473cf34c9a36e502d1095a916a0b2f67075d2fb4093d2142fe6',
 'evidence/n3-corner-bounds.json':'fe843711ff66e4a89f7856fc952441537a69d2907a5c78a6a844d61fec3e9c46',
 'code/n3_corner_bounds.c':'a0497ca1219850e28f2bf51e72cb4fc8f78cde238b81fd678262d646511402bd',
}
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def ident(p): return dict(path=str(p.relative_to(ROOT)),sha256=sha(p),bytes=p.stat().st_size)
def cheb(x,n):
    a=[Q(1),x]
    for k in range(2,n+1): a.append(2*x*a[-1]-a[-2])
    return a[:n+1]
def rational_n2_control():
    # Direct coefficient polynomial and endpoint derivatives, unrelated to quotient brackets.
    n=2; m=3; xs=[Q(1),Q(0),Q(-1)]; ys=[Q(1),Q(1,2),Q(-1,2),Q(-1)]
    mass=energy=Q(0); zeros=0
    for j,x in enumerate(xs):
        for k,y in enumerate(ys):
            if (j+k)%2: continue
            w=Q(2,n*m)
            if j in (0,n): w/=2
            if k in (0,m): w/=2
            tx,ty=cheb(x,n),cheb(y,n)
            ell=gx=gy=Q(0)
            for a in range(n+1):
                for b in range(n+1-a):
                    coeff=(1 if a==0 else 2)*(1 if b==0 else 2)
                    if (a,b)==(n,0): coeff=1
                    t=w*coeff*tx[a]*ty[b]*(-1)**(a+b)
                    ell+=t; gx-=a*a*t; gy-=b*b*t
            mass+=abs(ell)
            if ell: energy+=(gx*gx+gy*gy)/abs(ell)
            else: zeros+=1
    return mass,energy,zeros

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--run',action='store_true'); args=ap.parse_args()
    if not args.run: ap.error('Corrected receipt requires --run: rebuild and actual replay are mandatory')
    started=datetime.datetime.now(datetime.timezone.utc).isoformat()
    for path,h in PINS.items(): assert sha(TOPIC/path)==h,(path,'changed frozen input')
    OUT.mkdir(parents=True,exist_ok=True)
    if args.run:
        subprocess.run(BUILD,check=True,cwd=ROOT)
        for n in [2,33,64,128]:
            path=OUT/('n2-control.json' if n==2 else f'n{n}.json')
            with path.open('w') as f: subprocess.run([str(BINARY),str(n)],stdout=f,check=True,cwd=ROOT)
    original=json.loads((TOPIC/'evidence/n3-corner-bounds.json').read_text())
    rows=[]
    for run in original['runs']:
        d=run['certificate']; n=d['degree']; path=OUT/f'n{n}.json'; a=json.loads(path.read_text())
        assert a['degree']==n and a['precision_bits']==512
        contained={k:Q(d[k])<=Q(a[k]) if k.endswith('lower') else Q(d[k])>=Q(a[k]) for k in ['corner_lower','corner_upper','energy_lower','energy_upper']}
        assert all(contained.values())
        ell,E,u=map(Q,(a['corner_lower'],a['energy_upper'],a['global_norm_upper']))
        kap=min(Q(1),1/(8*(E/(n**4*ell)+3*u/ell)))
        assert kap==Q(a['kappa']) and kap>Q(1,12500)
        phase=Q(1,128**2)*(1+Q(n*n,(n+1)**2))/2
        assert phase==Q(a['scaled_phase_requirement']) and phase<=Q(1,12500)
        c=n.bit_length(); assert 2**c>=n+1 and 2**(c-1)<n+1
        assert u==110*(1+c)**2
        dell,dE,du=map(Q,(d['corner_lower'],d['energy_upper'],d['global_norm_upper']))
        dkap=min(Q(1),1/(8*(dE/(n**4*dell)+3*du/dell)))
        assert dkap==Q(d['kappa']) and dkap>Q(1,12500) and du==u
        assert Q(d['physical_H_radius'])==dkap/(n*n)
        r=Q(d['symmetric_scaled_phase_radius']);assert r*r*(1+Q(n*n,(n+1)**2))/2<=dkap
        assert a['nonzero_cardinals']==d['nonzero_cardinals']==(n+1)*(n+2)//2-n//2
        assert a['zero_cardinals_omitted']==d['zero_cardinals_omitted']==n//2
        rows.append(dict(degree=n,own_interval_inside_producer=contained,nonzero_cardinals=a['nonzero_cardinals'],zero_cardinals_omitted=a['zero_cardinals_omitted'],kappa_approx_diagnostic=float(kap),certified_common_kappa='1/12500',certified_scaled_phase_box='1/128',exact_assembly_pass=True,raw=ident(path)))
    mass,energy,zeros=rational_n2_control(); c=json.loads((OUT/'n2-control.json').read_text())
    assert Q(c['corner_lower'])<=mass<=Q(c['corner_upper'])
    assert Q(c['energy_lower'])<=energy<=Q(c['energy_upper']) and zeros==1
    comparisons=[]
    for name in ['n2-control.json','n33.json','n64.json','n128.json']:
        old,new=HISTORY/name,OUT/name
        comparisons.append(dict(file=name,initial_sha256=sha(old) if old.exists() else None,corrected_sha256=sha(new),byte_identical=old.read_bytes()==new.read_bytes() if old.exists() else None))
    for path,h in PINS.items(): assert sha(TOPIC/path)==h,(path,'changed during replay')
    gmp=ctypes.CDLL('libgmp.so.10')
    result=dict(schema='independent-corner-replay-v2',status='PASS independent exact finite replay; analytic local reduction separately reviewed',rules_sha='3dda890275a7599caa707b0fb8c0b6e6f6a80643',reviewer='Distinct Codex /root/check_rows; assigned gpt-6-astra high; serving metadata not independently exposed',
      arithmetic='GMP exact integers with directed dyadic quantization at512bits; exact Machin arctangent rationals and Taylor cosine remainder; no MPFR or developer kernel',
      build_command=BUILD,compiler=subprocess.check_output(['g++','--version'],text=True).splitlines()[0],python=platform.python_version(),platform=platform.platform(),
      command='python topics/padua-argmax-bridge-20261105/code/check_corner_receipt.py --run',
      execution_started_utc=started,execution_finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
      execution_commands=[[str(BINARY),str(n)] for n in [2,33,64,128]],
      gmp_runtime_version=ctypes.c_char_p.in_dll(gmp,'__gmp_version').value.decode(),
      linked_runtime=subprocess.check_output(['ldd',str(BINARY)],text=True),
      supersedes=dict(receipt_sha256='28050ad27ecccb011faf0df4958744041e3843e3cd1581ca921b830e1504983f',source_sha256='84cbbe858b52711c99713b05f6b538eb352efb73aa41c2c1eac715288362bfa6',status='initial PASS withdrawn',reason='two_w divided by 2 before canonicalization, violating GMP canonical-operand contract',correction='canonicalize immediately after two_w construction, before any arithmetic',historical_archive=str(HISTORY.relative_to(ROOT))),
      comparison_with_withdrawn_outputs=comparisons,
      sources=[ident(SOURCE),ident(Path(__file__).resolve())]+[ident(TOPIC/p) for p in PINS],binary=ident(BINARY),rows=rows,
      rational_control=dict(degree=2,corner=str(mass),energy=str(energy),zero_cardinals=1,method='independent direct rational coefficient kernel and physical endpoint derivatives',raw=ident(OUT/'n2-control.json')),
      limits='Only the three finite local radii. No full-degree cover, B2/B3 pass, global argmax extension, external novelty or required Claude audit. Raw output off Git; archival pending, all regenerating source included.')
    target=TOPIC/'evidence/independent-corner-replay.json';target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(status='PASS',degrees=[r['degree'] for r in rows],control=result['rational_control'],receipt=ident(target)),indent=2))
if __name__=='__main__':main()
