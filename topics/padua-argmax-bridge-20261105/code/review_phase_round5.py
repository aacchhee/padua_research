#!/usr/bin/env python3
"""Focused independent R4-1 response checks; never replays a complete tree."""
import ctypes as C
import hashlib
import importlib.util
import json
import math
import pathlib
import platform
import resource
import subprocess
import sys
import time
import mpmath as mp

ROOT = pathlib.Path(__file__).resolve().parents[3]
TOPIC = ROOT/'topics/padua-argmax-bridge-20261105'
SOURCE = TOPIC/'code/phase_checker'
OUT = ROOT/'local-output/argmax-bridge-20261105/phase-round5-review'
PINS = {
    'hybrid_kernel_v2.cpp':'17fea91d4fa02e4183823e5d70b44705e96da7acfd26b04a0f3ed1cac443d9a2',
    'build_snapshot.py':'19a5a7c2296768853b94672b9b5dc4cf16c9ae87c37abbcde073ffaf89246bfb',
    'check.py':'88dde644a77a286e547679b0547c4d35814a4dda7373575208246882d9a26820',
    'hybrid_kernel.cpp':'9a976e77d861c291468d6bfa4d2104c6c42ace953781ce1c5ff1a43073505d7d',
    'arb_kernel.cpp':'236116452dc7aae66e39cbf8800fe847cffe931ac0ce8a9682397313de7c43a6'}


def identity(path):
    data = path.read_bytes()
    return {'path':str(path),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    sources = [identity(SOURCE/name) for name in PINS]
    assert all(row['sha256']==PINS[pathlib.Path(row['path']).name] for row in sources)
    sys.path.insert(0,str(SOURCE))
    spec = importlib.util.spec_from_file_location('independent_round5_checker',SOURCE/'check.py')
    ck = importlib.util.module_from_spec(spec); spec.loader.exec_module(ck)
    start = time.process_time(); child0 = resource.getrusage(resource.RUSAGE_CHILDREN)
    kernel = ck.Kernel('round5')
    assert kernel.provenance['source_snapshot']['sha256']==PINS['hybrid_kernel_v2.cpp']
    assert kernel.provenance['kernel_variant']=='round5'
    mp.mp.dps = 120; tolerance = mp.mpf('1e-100')
    ptr = C.POINTER(C.c_double)
    ratio = kernel.lib.phase_ratio
    ratio.argtypes = [C.c_int,C.c_int,C.c_double,C.c_double,ptr,C.POINTER(C.c_int)]
    ratio.restype = C.c_int
    rows = []
    cases = [(-2,.125,.375),(-1,-.375,-.125),(1,-1e-12,1e-12),
             (0,1e-30,2e-30),(2,.2,.2),(0,-4.,4.)]
    for k in (1,2,3,17,18):
        for turn,lo,hi in cases+([(-2,0.,0.)] if k==1 else []):
            out = (C.c_double*8)(); used = C.c_int(-1)
            assert ratio(k,turn,lo,hi,out,C.byref(used))==0
            assert all(math.isfinite(v) for v in out)
            assert used.value in (0,1)
            if lo<=0<=hi: assert used.value==0
            if k==1: assert list(out)==[1.,1.,0.,0.,1.,1.,0.,0.]
            for i in range(3):
                z = turn*mp.pi+mp.mpf(lo)+(mp.mpf(hi)-mp.mpf(lo))*i/2
                freq = range(k-1,-k,-2)
                value = mp.re(mp.fsum(mp.exp(1j*j*z) for j in freq))
                derivative = mp.re(mp.fsum(1j*j*mp.exp(1j*j*z) for j in freq))
                for offset in (0,4):
                    assert mp.mpf(out[offset])-tolerance<=value<=mp.mpf(out[offset+1])+tolerance
                    assert mp.mpf(out[offset+2])-tolerance<=derivative<=mp.mpf(out[offset+3])+tolerance
            rows.append({'k':k,'turn':turn,'offsets':[lo,hi],
                         'quotient':bool(used.value),'hybrid_bounds':list(out[4:])})
    nonfinite = kernel.lib.phase_nonfinite_refinement_control
    nonfinite.argtypes = [C.c_int,ptr]; nonfinite.restype = C.c_int
    for which in (0,1):
        out = (C.c_double*4)()
        assert nonfinite(which,out)==0 and list(out)==[1.,1.,0.,0.]
    assert nonfinite(2,(C.c_double*4)())==3
    assert kernel.lib.phase_disjoint_intersection_control()==3
    term = kernel.lib.phase_term
    term.argtypes = [C.c_int]*3+[C.c_double]*2+[ptr]; term.restype = C.c_int
    jets = []
    for n in (2,17,32):
        for r,s,a,b in ((0,0,0.,0.),(n,n+1,0.,0.),(n,n+1,1e-12,-1e-12),(1,2,.2,-.3)):
            out = (C.c_double*6)(); assert term(n,r,s,a,b,out)==0
            assert all(math.isfinite(v) for v in out)
            u=(r*mp.pi+mp.mpf(a))/n; v=(s*mp.pi+mp.mpf(b))/(n+1)
            value=da=db=mp.mpf(0)
            for i in range(n+1):
                for j in range(n+1-i):
                    coefficient=(1 if i==0 else 2)*(1 if j==0 else 2)-int((i,j)==(n,0))
                    value+=coefficient*mp.cos(i*u)*mp.cos(j*v)
                    da-=coefficient*i*mp.sin(i*u)*mp.cos(j*v)/n
                    db-=coefficient*j*mp.cos(i*u)*mp.sin(j*v)/(n+1)
            assert all(mp.mpf(out[2*i])-tolerance<=x<=mp.mpf(out[2*i+1])+tolerance
                       for i,x in enumerate((value,da,db)))
            jets.append({'n':n,'r':r,'s':s,'a':a,'b':b})
    # Exercise the changed default and fixed selector independently of the
    # developer's build. No candidate tree is supplied or checked.
    baseline=ck.Kernel()
    assert baseline.provenance['kernel_variant']=='baseline'
    assert baseline.provenance['source_snapshot']['sha256']==PINS['arb_kernel.cpp']
    assert baseline.provenance['workdir']!=kernel.provenance['workdir']
    box=[.1,math.nextafter(.1,math.inf),.3,math.nextafter(.3,math.inf)]
    base_bounds=baseline.bounds(3,box); new_bounds=kernel.bounds(3,box)
    assert all(math.isfinite(v) for v in base_bounds+new_bounds)
    assert new_bounds[0]<=base_bounds[0] and new_bounds[1]<=base_bounds[1] and new_bounds[2]>=base_bounds[2]
    rejected=[]
    for variant in ('','../hybrid_kernel_v2.cpp','arbitrary-source.cpp'):
        try: ck.build_snapshot.build(variant)
        except ValueError: rejected.append(variant)
        else: raise AssertionError('invalid variant accepted')
    badcli=subprocess.run([sys.executable,str(SOURCE/'check.py'),'unused-candidate',
                           '--kernel','../hybrid_kernel_v2.cpp'],capture_output=True,text=True)
    assert badcli.returncode==2 and 'invalid choice' in badcli.stderr
    assert sources==[identity(SOURCE/name) for name in PINS]
    child1=resource.getrusage(resource.RUSAGE_CHILDREN)
    builds={'round5':kernel.provenance,'baseline':baseline.provenance}
    manifest=OUT/'build-provenance.json';manifest.write_text(json.dumps(builds,indent=2)+'\n')
    receipt={'scope':'MEASURED focused independent response checks; no complete candidate replay',
             'rules_sha':'3888dd37c362a0689943f33e6b7e44c1dd1c3050',
             'command':'python topics/padua-argmax-bridge-20261105/code/review_phase_round5.py',
             'script':identity(pathlib.Path(__file__).resolve()),'sources':sources,
             'python':platform.python_version(),'mpmath':mp.__version__,'mpmath_digits':120,
             'tolerance':'1e-100, point comparisons diagnostic only',
             'ratio_cases':rows,'ratio_point_checks':3*len(rows),'primitive_cases':jets,
             'R4_1_exact_reproducer_closed':True,'nonfinite_candidate_fallbacks':2,
             'finite_contradiction_rejections':2,'invalid_selector_rejections':rejected,
             'invalid_cli_selector_rejected':True,'baseline_default_verified':True,
             'asymmetric_box':box,'baseline_bounds':base_bounds,'round5_bounds':new_bounds,
             'build_manifest':identity(manifest),'passed':True,'full_cover_run':False,
             'degree_certificate_accepted':False,
             'process_cpu_seconds':time.process_time()-start,
             'child_cpu_seconds':child1.ru_utime+child1.ru_stime-child0.ru_utime-child0.ru_stime}
    path=TOPIC/'evidence/phase-round5-review.json';path.write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({'passed':True,'ratio_cases':len(rows),'ratio_points':3*len(rows),
                      'primitive_cases':len(jets),'full_cover_run':False,
                      'process_cpu_seconds':receipt['process_cpu_seconds'],
                      'child_cpu_seconds':receipt['child_cpu_seconds']}))


if __name__=='__main__':
    main()
