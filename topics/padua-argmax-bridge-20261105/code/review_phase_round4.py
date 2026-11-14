#!/usr/bin/env python3
"""Independent bounded diagnostics of frozen hybrid source; no full replay.

Complex-exponential and triangular-polynomial samples are MEASURED checks,
not a replacement for the interval argument or complete certificate replay.
"""
import ctypes as C
import hashlib
import json
import math
import pathlib
import platform
import resource
import subprocess
import time
import mpmath as mp

ROOT = pathlib.Path(__file__).resolve().parents[3]
TOPIC = ROOT / 'topics/padua-argmax-bridge-20261105'
SOURCE = TOPIC / 'code/phase_checker'
OUT = ROOT / 'local-output/argmax-bridge-20261105/phase-round4-review'


def ident(path):
    data = path.read_bytes()
    return {'path': str(path), 'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest()}


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--source-sha', required=True)
    args = ap.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    source = SOURCE / 'hybrid_kernel.cpp'
    assert ident(source)['sha256'] == args.source_sha
    paths = [source, SOURCE/'arb_kernel.cpp', SOURCE/'check.py', SOURCE/'build_snapshot.py']
    before = [ident(p) for p in paths]
    for p in paths[:2]:
        (OUT/p.name).write_bytes(p.read_bytes())
    runtime = ROOT/'local-output/argmax-bridge-20261105/phase-checker/runtime/extracted/usr'
    binary = OUT/'libindependent_round4.so'
    command = ['c++', '-std=c++17', '-O3', '-Wall', '-Wextra', '-fPIC', '-shared',
               '-I'+str(runtime/'include'), str(OUT/source.name),
               '-L'+str(runtime/'lib/x86_64-linux-gnu'),
               '-Wl,-rpath,'+str(runtime/'lib/x86_64-linux-gnu'),
               '-l:libflint.so.19', '-lgmp', '-o', str(binary)]
    ct0 = resource.getrusage(resource.RUSAGE_CHILDREN)
    subprocess.run(command, check=True)
    ct1 = resource.getrusage(resource.RUSAGE_CHILDREN)
    start = time.process_time()
    lib = C.CDLL(str(binary))
    ptr = C.POINTER(C.c_double)
    ratio = lib.phase_ratio
    ratio.argtypes = [C.c_int, C.c_int, C.c_double, C.c_double, ptr, C.POINTER(C.c_int)]
    ratio.restype = C.c_int
    term = lib.phase_term
    term.argtypes = [C.c_int]*3+[C.c_double]*2+[ptr]
    term.restype = C.c_int
    mp.mp.dps = 120
    tol = mp.mpf('1e-100')

    def contained(out, values):
        return all(mp.mpf(out[2*i])-tol <= value <= mp.mpf(out[2*i+1])+tol
                   for i, value in enumerate(values))

    ratio_cases = []
    intervals = [(0.,0.), (-1e-12,1e-12), (-.25,.125),
                 (1e-30,2e-30), (.125,.375), (-.375,-.125)]
    for k in (1,2,3,17,18):
        for turn in (-2,-1,0,1,2):
            for lo,hi in intervals:
                out = (C.c_double*8)(); used = C.c_int(-1)
                assert ratio(k,turn,lo,hi,out,C.byref(used)) == 0
                if lo <= 0 <= hi:
                    assert used.value == 0, 'collision must use finite fallback'
                for q in (0,1,2,3,4):
                    z = turn*mp.pi + mp.mpf(lo)+(mp.mpf(hi)-mp.mpf(lo))*q/4
                    frequencies = range(k-1,-k,-2)
                    value = mp.re(mp.fsum(mp.exp(1j*j*z) for j in frequencies))
                    derivative = mp.re(mp.fsum(1j*j*mp.exp(1j*j*z) for j in frequencies))
                    assert contained(out[:4], [value,derivative])
                    if not contained(out[4:], [value,derivative]):
                        report = {
                            'scope':'MEASURED independent bounded failure; stopped at first finding',
                            'rules_sha':'bda45a4c1392bea87de0841b6b23e5c35b2a694b',
                            'sources':before,'script':ident(pathlib.Path(__file__).resolve()),
                            'command':'python '+str(pathlib.Path(__file__).relative_to(ROOT))+' --source-sha '+args.source_sha,
                            'compile_command':command,'binary':ident(binary),
                            'python':platform.python_version(),'mpmath':mp.__version__,
                            'mpmath_digits':120,'tolerance':'1e-100, numerical diagnostics only',
                            'passed':False,'finding':'phase_ratio returns success with NaN hybrid derivative bounds',
                            'case':{'k':k,'turn':turn,'lo':lo,'hi':hi,'sample_index':q,
                                    'quotient_used':bool(used.value),
                                    'output':[v if math.isfinite(v) else str(v) for v in out],
                                    'reference_value':str(value),'reference_derivative':str(derivative)},
                            'completed_ratio_cases':len(ratio_cases),
                            'completed_ratio_points':5*len(ratio_cases),
                            'jet_cases':0,'full_cover_run':False,
                            'compiler_child_cpu_seconds':ct1.ru_utime+ct1.ru_stime-ct0.ru_utime-ct0.ru_stime,
                            'diagnostic_process_cpu_seconds':time.process_time()-start,
                            'source_stable':before == [ident(p) for p in paths]}
                        target = TOPIC/'evidence/phase-round4-review.json'
                        target.write_text(json.dumps(report,indent=2)+'\n')
                        print(json.dumps(report['case']))
                        raise SystemExit(1)
                ratio_cases.append({'k':k,'turn':turn,'interval':[lo,hi],
                                    'quotient':bool(used.value)})
    assert lib.phase_disjoint_intersection_control() == 3
    jet_cases = []
    for n in (2,3,17,24,32):
        for r,s in ((0,0),(n,n+1),(0,n+1),(n,0),(1,1),(n-1,n)):
            for a,b in ((0.,0.),(1e-12,-1e-12),(.2,-.3)):
                out = (C.c_double*6)()
                assert term(n,r,s,a,b,out) == 0
                u = (r*mp.pi+mp.mpf(a))/n
                v = (s*mp.pi+mp.mpf(b))/(n+1)
                value = da = db = mp.mpf(0)
                for i in range(n+1):
                    for j in range(n+1-i):
                        coefficient = (1 if i==0 else 2)*(1 if j==0 else 2)-int((i,j)==(n,0))
                        value += coefficient*mp.cos(i*u)*mp.cos(j*v)
                        da -= coefficient*i*mp.sin(i*u)*mp.cos(j*v)/n
                        db -= coefficient*j*mp.cos(i*u)*mp.sin(j*v)/(n+1)
                assert contained(out, [value,da,db]), (n,r,s,a,b,list(out))
                jet_cases.append({'n':n,'r':r,'s':s,'a':a,'b':b})
    assert before == [ident(p) for p in paths], 'reviewed source changed during run'
    dependencies = [ident((runtime/'lib/x86_64-linux-gnu/libflint.so.19').resolve()),
                    ident(pathlib.Path('/lib/x86_64-linux-gnu/libgmp.so.10').resolve()),
                    ident(pathlib.Path('/lib/x86_64-linux-gnu/libmpfr.so.6').resolve())]
    report = {'scope':'MEASURED independent bounded diagnostics; no full-cover replay',
              'rules_sha':'bda45a4c1392bea87de0841b6b23e5c35b2a694b',
              'sources':before, 'script':ident(pathlib.Path(__file__).resolve()),
              'command':'python '+str(pathlib.Path(__file__).relative_to(ROOT))+' --source-sha '+args.source_sha,
              'compile_command':command, 'binary':ident(binary),'dependencies':dependencies,
              'compiler':subprocess.check_output(['c++','--version'],text=True).splitlines()[0],
              'python':platform.python_version(),'mpmath':mp.__version__, 'mpmath_digits':120,
              'tolerance':'1e-100, numerical diagnostics only',
              'ratio_cases':len(ratio_cases),'ratio_points':5*len(ratio_cases),
              'quotient_cases':sum(x['quotient'] for x in ratio_cases),
              'fallback_cases':sum(not x['quotient'] for x in ratio_cases),
              'jet_cases':len(jet_cases),'disjoint_intersection_rejected':True,
              'full_cover_run':False,'passed':True,
              'compiler_child_cpu_seconds':ct1.ru_utime+ct1.ru_stime-ct0.ru_utime-ct0.ru_stime,
              'diagnostic_process_cpu_seconds':time.process_time()-start}
    target = TOPIC/'evidence/phase-round4-review.json'
    target.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ['ratio_cases','ratio_points','quotient_cases',
          'fallback_cases','jet_cases','passed','compiler_child_cpu_seconds',
          'diagnostic_process_cpu_seconds']}))


if __name__ == '__main__':
    main()
