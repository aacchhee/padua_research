#!/usr/bin/env python3
"""Orchestrate independent GMP port. No mathematical producer imports."""
import argparse, concurrent.futures, copy, hashlib, json, os, subprocess, sys, time
from fractions import Fraction
from pathlib import Path
sys.set_int_max_str_digits(1000000)
FIELDS=('Knode_squared','KHS_squared','Urow_squared','upper_squared')
def cross(a,b):
    a,b=Fraction(a),Fraction(b)
    return (a.numerator*b.denominator>b.numerator*a.denominator)-(a.numerator*b.denominator<b.numerator*a.denominator)
def validate(r):
    s=r['degree'];n=(s+1)*(s+2)//2
    assert r['sources']=='all' and r['source_count']==n-1 and r['basis_count']==n
    assert r['point_count']=={'triangle':325,'rotated':625}[r['set']] and n<r['point_count']
    assert len(r['pivot_choices'])==n-1 and set(r['pivot_choices'])<=set('XY')
    vals=[r[f]['exact'] for f in FIELDS]
    assert all(cross(v,0)>0 for v in vals)
    assert cross(vals[3],min(map(Fraction,vals[1:3])))==0 and cross(vals[0],vals[3])<=0
    assert Fraction(r['normal_trace_exact'])==r['point_count']-n
    assert r['exact_gram_pairs_checked']>=n*(n-1)//2
    expected=[[2,1]] if r['rule']=='pivot' and r['set']=='rotated' else []
    if s<=12: assert r['pivot_ties']==expected
    assert r['rule']=='pivot' or r['pivot_ties']==[]
    for t,j in r['pivot_ties']:
        assert 1<=t<=s and 0<j<t
        assert r['pivot_choices'][t*(t+1)//2+j-1]=='X'
def equal(a,b):
    validate(a)
    for f in ('degree','rule','set','sources','source_count','point_count','basis_count','pivot_choices'):
        assert a[f]==b[f],f
    for f in FIELDS: assert cross(a[f]['exact'],b[f]['exact'])==0,f
    assert a['normal_trace_exact']==b['normal_trace_exact']
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--old',required=True);ap.add_argument('--out',required=True);ap.add_argument('--degree',type=int,default=12);ap.add_argument('--workers',type=int,default=4);ap.add_argument('--timeout',type=int,default=1800);ap.add_argument('--receipt',required=True);ap.add_argument('--validated-overlap');args=ap.parse_args()
    if args.degree>12:
        assert args.validated_overlap, 'higher runs require successful old-overlap receipt'
        gate=json.loads(Path(args.validated_overlap).read_text())
        assert gate['status']=='PASS finite independent exact endpoint rerun'
        assert sum(r['case'][2]==12 and r['status']=='PASS' for r in gate['runs'])==8
    out=Path(args.out);out.mkdir(parents=True,exist_ok=True);src=Path(__file__).with_name('g1_independent.cpp');exe=out/'g1_independent'
    subprocess.run(['g++','-O3','-std=c++17',str(src),'-lgmpxx','-lgmp','-o',str(exe)],check=True)
    oldbytes=Path(args.old).read_bytes();assert hashlib.sha256(oldbytes).hexdigest()=='0d9c236fe879879b7f546596c554d213b7b8c408d31dec08dd79146c7d629344'
    old={(r['set'],r['rule'],r['degree']):r for r in json.loads(oldbytes)['runs']}
    def run(case):
        grid,rule,degree=case;stem=f'{grid}-{rule}-d{degree}';raw=out/(stem+'.jsonl');log=out/(stem+'.log');start=time.monotonic()
        cmd=[str(exe),grid,str(degree),rule]
        try:
            with raw.open('w') as f,log.open('w') as e: p=subprocess.run(cmd,stdout=f,stderr=e,timeout=args.timeout)
            assert p.returncode==0,f'returncode {p.returncode}'
            rows=[json.loads(l) for l in raw.read_text().splitlines()];assert len(rows)==degree-1
            for r in rows:
                validate(r)
                if r['degree']<=12:equal(r,old[grid,rule,r['degree']])
            return {'case':case,'status':'PASS','elapsed_seconds':time.monotonic()-start,'rows':len(rows),'path':str(raw),'sha256':hashlib.sha256(raw.read_bytes()).hexdigest(),'bytes':raw.stat().st_size}
        except Exception as e:return {'case':case,'status':'FAIL_OR_INCOMPLETE','elapsed_seconds':time.monotonic()-start,'error':repr(e),'path':str(raw)}
    # Small independent degree builds first; these must agree with frozen old rows.
    cases=[(g,r,d) for d in (2,3,4) for g in ('triangle','rotated') for r in ('bj','mirror','alt','pivot')]
    receipt={'status':'INCOMPLETE','implementation':'independent C++ GMP mpq_class; no producer imports','code_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'old_sha256':hashlib.sha256(oldbytes).hexdigest(),'command':sys.argv,'rules_sha':'0e493be7f9883e00e6260cf6b081c607a230177f','harness_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'compiler':subprocess.check_output(['g++','--version'],text=True).splitlines()[0],'gmp_linkage':'system GMP C++ and GMP shared libraries','runs':[]}
    def save():Path(args.receipt).write_text(json.dumps(receipt,indent=2)+'\n')
    for batch in (cases,[(g,r,args.degree) for g in ('triangle','rotated') for r in ('bj','mirror','alt','pivot')]):
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
            for r in pool.map(run,batch):
                receipt['runs'].append(r);save();print(json.dumps(r),flush=True)
        if any(r['status']!='PASS' for r in receipt['runs']):save();return 1
    # Compare independent small-degree construction to the higher-prefix construction.
    for g in ('triangle','rotated'):
        for rule in ('bj','mirror','alt','pivot'):
            high=[json.loads(l) for l in (out/f'{g}-{rule}-d{args.degree}.jsonl').read_text().splitlines()]
            for d in (2,3,4):
                low=json.loads((out/f'{g}-{rule}-d{d}.jsonl').read_text().splitlines()[-1]);equal(low,high[d-2])
    good=json.loads((out/'rotated-pivot-d4.jsonl').read_text().splitlines()[-1]);controls=[]
    for label,edit in [('omitted source',lambda r:r.update(source_count=r['source_count']-1)),('wrong point count',lambda r:r.update(point_count=624)),('wrong basis dimension',lambda r:r.update(basis_count=14)),('negative endpoint',lambda r:r['Knode_squared'].update(exact='-1')),('bad upper minimum',lambda r:r['upper_squared'].update(exact='1')),('missing pivot tie',lambda r:r.update(pivot_ties=[])),('Y tie break',lambda r:r['pivot_choices'].__setitem__(3,'Y')),('wrong trace',lambda r:r.update(normal_trace_exact='0')),('no Gram checks',lambda r:r.update(exact_gram_pairs_checked=0))]:
        bad=copy.deepcopy(good);edit(bad)
        try:validate(bad)
        except (AssertionError,ValueError):controls.append({'control':label,'rejected':True})
        else:raise AssertionError('accepted malformed '+label)
    for argv in [('triangle','21','bj'),('triangle','2','bad'),('bad','2','bj')]:
        p=subprocess.run([str(exe),*argv],capture_output=True);assert p.returncode!=0;controls.append({'control':'invalid native arguments '+str(argv),'rejected':True})
    receipt.update(status='PASS finite independent exact endpoint rerun',prefix_checks=24,malformed_controls=controls);save()
if __name__=='__main__':sys.exit(main())
