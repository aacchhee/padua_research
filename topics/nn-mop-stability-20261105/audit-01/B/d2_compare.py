# Auditor B: compare D2 reruns with committed attempts/D2.md tables; recompute G0/G1/G2
import json, re, sys
import mpmath as mp
import os
B = os.environ.get('AUDIT_OUT', os.path.dirname(os.path.abspath(__file__)))  # auditor output directory
T=os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../../')+'topics/nn-mop-stability-20261105/attempts/D2.md'
d2=open(T).read()
sections=re.split(r'\n## ',d2)
def table(title_start):
    sec=[s for s in sections if s.startswith(title_start)][0]
    out={}
    for m in re.finditer(r'^\| (krawtchouk|hahn),(\d+) \|(.*)\|$',sec,re.M):
        cells=[c.strip().strip('`') for c in m.group(3).split('|')]
        out[(m.group(1),int(m.group(2)))]=cells
    return out
Et=table('G0 and exact'); Rt=table('Conditioning comparison'); It=table('Input rounding'); Bt=table('Fixed-path'); Mt=table('Mixed-input')
frozen={('krawtchouk',4):1.0090076922134965e-13,('krawtchouk',8):1.8705702304571456e-9,('krawtchouk',12):1.6124888672742654e-6,('krawtchouk',16):0.09666944831233441,('krawtchouk',24):72940.5982327841,('krawtchouk',32):5022.381465152575,
        ('hahn',4):1.3412313841971528e-12,('hahn',8):2.614295169950109e-7,('hahn',12):0.0024598366717086153,('hahn',16):70.31384815587052,('hahn',24):310.52010170669297,('hahn',32):677581.5807967706}
g0={f:json.load(open(f'{B}/d2/d2-g0-{f}-final.json')) for f in ('krawtchouk','hahn')}
g0pass=0
for f,d in g0.items():
    for r in d['cases']:
        e=r['max_field_relative_error']; ok=(e==frozen[(f,r['N'])]); g0pass+=ok
        print('G0',f,r['N'],repr(e),'exact-equal' if ok else 'DIFF %.3e'%(abs(e/frozen[(f,r['N'])]-1)), 'refagree',r['reference_relative_agreement'], 'N4exact',r.get('exact_moment_check',{}).get('passed'), 'inhash==D2', r['input_sha256']==It[(f,r['N'])][1])
print('G0 PASS count',g0pass,'/12')
kap={}
for f in ('krawtchouk','hahn'):
    for r in json.load(open(f'{B}/runs/conditioning-full-{f}260.json'))['cases']: kap[(f,r['N'])]=mp.mpf(r['NN']['mixed']['kappa'])
u=mp.mpf(2)**-53
names=['c4_stieltjes','c4_lanczos','c4_oracle_exact','c4_oracle_rounded']
for fn in sys.argv[1:]:
    st=json.load(open(fn)); print('==',fn,'python',st['python'],'mpmath',st['mpmath'],'hashes',{k:v[:12] for k,v in st['hashes'].items()})
    worst=dict(E=0,ratio=0,inp=0,B=0,Bmix=0); g1=[]; g2=[]
    for c in st['cases']:
        key=(c['family'],c['N']); ku=kap[key]*u
        E=[c['methods'][n]['forward_exact'] for n in names]
        worst['E']=max(worst['E'],max(abs(a/float(b)-1) for a,b in zip(E,Et[key])))
        rat=[mp.mpf(e)/ku for e in E]
        worst['ratio']=max(worst['ratio'],max(float(abs(a/mp.mpf(b)-1)) for a,b in zip(rat,Rt[key][1:])))
        worst['inp']=max(worst['inp'],abs(c['input_rounding_forward_effect']/float(It[key][0])-1))
        assert c['input_rounding_forward_effect']<=float(ku), ('input rounding effect exceeds kappa*u',key)
        if 'path' in c['methods'][names[0]]:
            Bv=[c['methods'][n]['path']['diagnostic_max'] for n in names]
            worst['B']=max(worst['B'],max(abs(a/float(b)-1) for a,b in zip(Bv,Bt[key])))
            Mv=[c['methods'][n]['path']['mixed_input_diagnostic'] for n in names]
            worst['Bmix']=max(worst['Bmix'],max(abs(a/float(b)-1) for a,b in zip(Mv,Mt[key])))
        if rat[0]>10: g1.append((key,float(rat[0])))
        if rat[0]>100: g2.append((key,float(rat[0]),float(rat[1]),'FAIL' if rat[1]>=10 else 'pass'))
        print(key,'kappa*u %.6e'%float(ku),'ratios S/L/O/R',['%.7g'%float(r) for r in rat],'eps-ratio S %.4g'%float(rat[0]/2),'inputround/(kappa u) %.3g'%float(c['input_rounding_forward_effect']/ku),
              'lanczos marg err',max(c['methods']['c4_lanczos']['marginal_error'],0),'stieltjes marg err',c['methods']['c4_stieltjes']['marginal_error'])
    print('max rel deviations from committed D2 tables (committed tables are rounded):',worst)
    print('G1 failures (S ratio>10):',g1)
    print('G2 antecedent (S ratio>100) and Lanczos:',g2)
