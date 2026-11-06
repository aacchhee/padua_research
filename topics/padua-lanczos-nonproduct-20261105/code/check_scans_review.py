#!/usr/bin/env python3
"""Supplementary checker; no P6 or inherited arithmetic module is imported.

Replays are launched separately by p6_scan.py. This checks their scientific
fields, reconstructs degree-three endpoints from direct monomial Gram-Schmidt,
and independently certifies N2 logs via rational series and signed OLS corners.
"""
import argparse, hashlib, itertools, json, math, platform, subprocess, sys, time
from fractions import Fraction as F
from pathlib import Path
sys.set_int_max_str_digits(1000000)
ROOT=Path(__file__).resolve().parents[3]
TOP=Path(__file__).resolve().parents[1]
WORK=Path('/tmp/padua-lanczos-nonproduct-20261105/scan-review')
RULES=('bj','mirror','alt','pivot')
FIELDS=('Knode_squared','KHS_squared','Urow_squared','upper_squared')

def ident(p):
    p=Path(p); b=p.read_bytes()
    return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())

def checked(rec):
    p=Path(rec['path']); a=ident(p)
    assert a['sha256']==rec['sha256'] and a['bytes']==rec['bytes']
    return p

def rows(path): return [json.loads(s) for s in Path(path).read_text().splitlines()]

def scientific(r):
    return {k:v for k,v in r.items() if k not in ('elapsed_seconds','exact_gram_pairs_checked')}

def compare_replays():
    results=[]
    for family,degree,reference in [('H24_222',16,'full16'),('D36x9',8,'benchmark8')]:
        old=TOP/'evidence'/f'p6-{reference}-{family}.json'
        new=TOP/'evidence'/f'check-scans-{family}.json'
        counts=[]
        for path in (old,new):
            r=json.loads(path.read_text()); assert r['status']=='PASS exact two-path weighted finite scan'
            assert len(r['runs'])==8
            allrows={}
            for run in r['runs']:
                data=rows(checked(run['output']))
                assert [v['degree'] for v in data]==list(range(2,degree+1))
                allrows[run['backend'],run['rule']]=data
            assert set(allrows)==set(itertools.product(('producer','checker'),RULES))
            counts.append(allrows)
        for key in counts[0]:
            for a,b in zip(counts[0][key],counts[1][key]): assert scientific(a)==scientific(b)
        for rule in RULES:
            for a,b in zip(counts[1]['producer',rule],counts[1]['checker',rule]): assert scientific(a)==scientific(b)
        results.append(dict(family=family,max_degree=degree,reference=ident(old),replay=ident(new),reference_comparisons=8*(degree-1),two_path_comparisons=4*(degree-1),status='PASS all scientific fields'))
    return results

def input_points(family):
    # Separate generators from the admission statements, not p6_families imports.
    if family in ('T24','H24_222'):
        return [(F(2*i-24,24),F(2*j-24,24),F(1,325) if family=='T24' else F((i+1)*(j+1)*(25-i-j),math.comb(29,5))) for i in range(25) for j in range(25-i)]
    directions={(F(1),F(0)),(F(-1),F(0)),(F(0),F(1)),(F(0),F(-1))}
    for a,b,c in ((3,4,5),(5,12,13),(8,15,17),(7,24,25)):
        directions.update((F(s*u,c),F(t*v,c)) for u,v in ((a,b),(b,a)) for s,t in itertools.product((-1,1),repeat=2))
    return [(F(k,9)*x,F(k,9)*y,F(1,324)) for k in range(1,10) for x,y in sorted(directions)]

def formula_checks():
    result=[]; inputs=[]
    for family in ('T24','H24_222','D36x9'):
        points=input_points(family); M=len(points); assert sum(w for x,y,w in points)==1
        pilot=TOP/'evidence'/f'p6-pilot-{family}.json'; receipt=json.loads(pilot.read_text())
        input_path=Path(receipt['runs'][0]['command'][1]); native=input_path.read_text().splitlines()
        assert ident(input_path)['sha256']==receipt['input']['native_input_sha256']
        inputs.append(dict(family=family,receipt=ident(pilot),input=ident(input_path)))
        parsed=[tuple(map(F,line.split())) for line in native[1:]]
        assert int(native[0])==M and sorted(parsed)==sorted(points)
        points=parsed # The formula is permutation invariant; use stored order to ease cross-check.
        x,y,w=zip(*points)
        def dot(a,b): return sum((wi*ai*bi for wi,ai,bi in zip(w,a,b)),F(0))
        powers=[(t-j,j) for t in range(4) for j in range(t+1)]
        index={p:k for k,p in enumerate(powers)}; B=[]; d=[]
        for a,b in powers:
            raw=[xi**a*yi**b for xi,yi in zip(x,y)]
            v=raw[:]
            for bk,dk in zip(B,d):
                coeff=dot(raw,bk)/dk
                v=[vi-coeff*bi for vi,bi in zip(v,bk)]
            assert all(dot(v,bk)==0 for bk in B)
            dk=dot(v,v); assert dk>0; B.append(v); d.append(dk)
        n=len(B); normal=[1-w[i]*sum(B[k][i]**2/d[k] for k in range(n)) for i in range(M)]
        assert sum(normal)==M-n and all(0<=r<=1 for r in normal)
        for rule in RULES:
            steps=[None]; choices=[]; ties=[]
            for k,(a,b) in enumerate(powers[1:],1):
                candidates=[]
                for axis,(pa,pb) in enumerate(((a-1,b),(a,b-1))):
                    if min(pa,pb)<0: continue
                    parent=index[pa,pb]; coord=(x,y)[axis]
                    z=[ci*bi for ci,bi in zip(coord,B[parent])]
                    sigma=dot(z,z); alpha=[dot(z,B[l])/d[l] for l in range(k)]
                    residue=[zi-sum(alpha[l]*B[l][i] for l in range(k)) for i,zi in enumerate(z)]
                    assert residue==B[k]
                    candidates.append((axis,parent,sigma,alpha))
                if rule=='pivot':
                    best=max(candidates,key=lambda v:(d[k]/v[2],-v[0]))
                    if len(candidates)==2 and candidates[0][2]==candidates[1][2]: ties.append([a+b,b])
                else:
                    axis=0 if b==0 or (a>0 and (rule=='mirror' or (rule=='alt' and 2*b<a+b))) else 1
                    best=next(v for v in candidates if v[0]==axis)
                steps.append(best); choices.append('XY'[best[0]])
            lo=F(0); hs=F(0); row=F(0)
            for i in range(M):
                # Invert the unit lower-triangular response recurrence at one node.
                G=[[F(int(k==h)) for h in range(n)] for k in range(n)]
                for k in range(1,n):
                    axis,parent,sigma,alpha=steps[k]; coord=(x,y)[axis][i]
                    for h in range(1,k):
                        G[k][h]=coord*G[parent][h]-sum(alpha[l]*G[l][h] for l in range(h,k))
                v=[steps[h][2]*sum(G[k][h]**2/d[k] for k in range(h,n)) for h in range(1,n)]
                lo=max(lo,normal[i]*max(v)); hs+=normal[i]*sum(v); row=max(row,sum(v))
            wanted=next(r for r in rows(checked(next(run['output'] for run in receipt['runs'] if run['backend']=='producer' and run['rule']==rule))) if r['degree']==3)
            assert [F(wanted[f]['exact']) for f in FIELDS]==[lo,hs,row,min(hs,row)]
            assert wanted['pivot_choices']==choices and wanted['pivot_ties']==ties
            result.append(dict(family=family,degree=3,rule=rule,point_count=M,source_count=n-1,endpoint_match=True,choice_tie_match=True))
    return dict(checks=result,inputs=inputs)

def log_series(v,terms=96):
    z=(v-1)/(v+1); square=z*z; power=z; total=F(0)
    for j in range(terms): total+=2*power/(2*j+1); power*=square
    return total,total+2*power/((2*terms+1)*(1-square))
LOG2=log_series(F(2))
def log_bounds(q):
    assert q>0
    k=q.numerator.bit_length()-q.denominator.bit_length()
    if q<F(2)**k:k-=1
    t=q/F(2)**k; assert 1<=t<2
    unit=1<<192; floor=(t.numerator*unit)//t.denominator
    low=log_series(F(floor,unit))[0]; high=log_series(F(floor+1,unit))[1]
    return low+k*LOG2[k<0],high+k*LOG2[k>=0]

def extrema(intervals,start):
    values=[sum(F(i-2,10)*intervals[start+i][bit] for i,bit in enumerate(bits)) for bits in itertools.product((0,1),repeat=5)]
    return min(values),max(values)

def rounded(v):
    a,b=v; scale=10**15
    return [str(F((a.numerator*scale)//a.denominator,scale)),str(F(-((-b.numerator*scale)//b.denominator),scale))]

def decision(windows):
    return ('PASS measured exponential screen' if all(a>F(1,10) for a,b in windows) else 'REDIRECT polynomial-bound question' if all(b<F(1,50) for a,b in windows) else 'INCONCLUSIVE')

def fit_checks():
    results=[]
    compact=ROOT/'topics/padua-lanczos-frontier-20261105/evidence/g1-compact-triangle.json'
    data=json.loads(compact.read_text()); assert ident(compact)['sha256']=='2c99758edf1888f2cdd8a0fcd7563512a1466407bb6659f630d7838abad37f38'
    table={(d,r):list(map(lambda q:F(q,data['scale']),(ll,lh,ul,uh))) for d,r,ll,lh,ul,uh in data['rows']}
    assert len(table)==76
    ratios={d:(table[d,'bj'][0]-min(table[d,r][3] for r in RULES),table[d,'bj'][3]-min(table[d,r][0] for r in RULES)) for d in range(8,17)}
    windows=[extrema(ratios,start) for start in (8,12)]
    target=TOP/'evidence/p6-n2-inherited-T24.json'; expected=json.loads(target.read_text())
    assert windows==[(F(w['lower_exact']),F(w['upper_exact'])) for w in expected['windows']]
    assert decision(windows)==expected['N2_verdict']
    provenance=[]
    for name in ('source_manifest','source_report','frozen_log_code'):
        rec=data[name]; p=Path(rec['path']); exists=p.exists()
        if exists: checked(rec)
        provenance.append(dict(kind=name,available=exists,sha256=rec['sha256']))
    results.append(dict(family='T24',source=ident(compact),target=ident(target),N2_verdict=decision(windows),windows=[rounded(v) for v in windows],provenance=provenance,scope='Inherited certified compact logs; source reconstruction only where files available'))
    for family in ('H24_222','D36x9'):
        target=TOP/'evidence'/f'p6-n2-{family}.json'
        if not target.exists(): continue
        data=json.loads(target.read_text()); receipt=json.loads(checked(data['scan_receipt']).read_text())
        assert receipt['status']=='PASS exact two-path weighted finite scan' and receipt['max_degree']>=16
        allrows={}
        for run in receipt['runs']:
            rr=rows(checked(run['output'])); assert len(rr)==receipt['max_degree']-1
            allrows[run['backend'],run['rule']]=rr
        assert len(allrows)==8
        for rule in RULES:
            for a,b in zip(allrows['producer',rule],allrows['checker',rule]): assert scientific(a)==scientific(b)
        endpoints={(rule,r['degree']):(F(r[FIELDS[0]]['exact']),F(r[FIELDS[-1]]['exact'])) for (backend,rule),rr in allrows.items() if backend=='producer' for r in rr}
        ratios={}; logcontain=0
        for degree in range(8,17):
            low=endpoints['bj',degree][0]/min(endpoints[r,degree][1] for r in RULES)
            high=endpoints['bj',degree][1]/min(endpoints[r,degree][0] for r in RULES)
            a,b=log_bounds(low),log_bounds(high)
            claim=list(map(F,data['logratio_outward'][str(degree)]))
            assert claim[0]<=a[0]/2<=a[1]/2 and b[0]/2<=b[1]/2<=claim[1]
            logcontain+=2; ratios[degree]=(a[0]/2,b[1]/2)
        windows=[extrema(ratios,start) for start in (8,12)]
        for (lo,hi),w in zip(windows,data['windows']):
            assert F(w['lower_exact'])<=lo<=hi<=F(w['upper_exact'])
            assert F(w['checker_lower_exact'])<=lo<=hi<=F(w['checker_upper_exact'])
        assert decision(windows)==data['N2_verdict']
        results.append(dict(family=family,target=ident(target),N2_verdict=decision(windows),windows=[rounded(v) for v in windows],independent_log_bounds_contained=logcontain,method='192-bit mantissa bounds; 96-term exact rational atanh series; all 32 OLS corners/window'))
    return results

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--mode',choices=('compare','formula','fits'),required=True); ap.add_argument('--output',type=Path,required=True); args=ap.parse_args()
    t=time.monotonic(); value={'compare':compare_replays,'formula':formula_checks,'fits':fit_checks}[args.mode]()
    report=dict(status='PASS supplementary '+args.mode,checker=ident(__file__),command=[sys.executable,'-B',*sys.argv],head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),python=platform.python_version(),platform=platform.platform(),elapsed_seconds=time.monotonic()-t,results=value)
    args.output.write_text(json.dumps(report,indent=2)+'\n'); print(json.dumps(report,indent=2))
if __name__=='__main__': main()
