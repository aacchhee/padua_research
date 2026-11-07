#!/usr/bin/env python3
"""Supplementary review reruns; all generated files stay in own review directory.

Bounded diagnostics only. This is neither a full-cover producer nor a proof
checker replacing phase_checker/check.py. Rebuilds frozen bytes independently.
"""
import copy
import ctypes
import hashlib
import importlib.util
import json
import math
import pathlib
import platform
import subprocess
import time
from fractions import Fraction as F

ROOT = pathlib.Path(__file__).resolve().parents[3]
TOPIC = ROOT / 'topics/padua-argmax-bridge-20261105'
OUT = ROOT / 'local-output/argmax-bridge-20261105/phase-math-review'


def identity(path):
    data = path.read_bytes()
    return {'path': str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path),
            'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    start = time.process_time()
    files = ['code/n3_outward.c', 'code/n3_outward_interval.h',
             'code/n3_outward_run.py', 'code/phase_checker/arb_kernel.cpp',
             'code/phase_checker/check.py', 'code/phase_checker/controls.py',
             'code/phase_checker/build.sh', 'code/phase_checker/setup.py',
             'theory/phase-checker-reduction.md', 'theory/N3-enclosure-spec.md',
             'code/n5_central_edge_defect.py', 'theory/N5-central-edge-defect.md',
             'theory/N1-row-model.md']
    sources = [identity(TOPIC / name) for name in files]
    for name in files:
        dest = OUT / 'snapshot' / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes((TOPIC / name).read_bytes())
    runtime = ROOT / 'local-output/argmax-bridge-20261105/phase-checker/runtime/extracted/usr'
    mpfr_include = ROOT / 'local-output/argmax-bridge-20261105/N3/runtime/extracted/usr/include'
    commands = [
        ['c++', '-std=c++17', '-O3', '-Wall', '-Wextra', '-fPIC', '-shared',
         '-I' + str(runtime / 'include'), str(OUT / 'snapshot/code/phase_checker/arb_kernel.cpp'),
         '-L' + str(runtime / 'lib/x86_64-linux-gnu'),
         '-Wl,-rpath,' + str(runtime / 'lib/x86_64-linux-gnu'),
         '-lflint', '-lgmp', '-o', str(OUT / 'libphase_checker.so')],
        ['cc', '-std=c11', '-O3', '-Wall', '-Wextra', '-Wpedantic', '-fPIC', '-shared',
         '-I' + str(mpfr_include), str(OUT / 'snapshot/code/n3_outward.c'),
         '/lib/x86_64-linux-gnu/libmpfr.so.6', '-lm', '-o', str(OUT / 'n3_outward.so')]]
    for command in commands:
        subprocess.run(command, check=True)
    ck = module(OUT / 'snapshot/code/phase_checker/check.py', 'review_checker')
    ck.LIB = OUT / 'libphase_checker.so'
    kernel = ck.Kernel()
    samples = []
    for name in ['far', 'nonlocal-defect', 'local']:
        path = ROOT / f'local-output/argmax-bridge-20261105/N3/outward-calibration-v1/n17-sample-{name}.json'
        raw = path.read_bytes()
        data = json.loads(raw)
        result = ck.check(data, kernel)
        assert not result['accepted'] and not result['complete'] and not result['failed_leaves']
        samples.append({'input': identity(path), 'result': result})
    baseline = json.loads((ROOT / 'local-output/argmax-bridge-20261105/N3/outward-calibration-v1/n17-sample-far.json').read_bytes())
    controls = []
    mutations = [
        ('false complete', lambda x: x.update(complete=True)),
        ('remove pending', lambda x: x['pending'].pop()),
        ('duplicate leaf', lambda x: x['leaves'].append(copy.deepcopy(x['leaves'][0]))),
        ('ancestor overlap', lambda x: x['leaves'].append({'root':3,'path':'','kind':'far'})),
        ('root omission', lambda x: x['roots'].pop()),
        ('pi shrink', lambda x: x['constants'].__setitem__(1, 3.14)),
        ('inflated threshold', lambda x: x['constants'].__setitem__(2, 100.)),
        ('false outside', lambda x: x['leaves'][0].update(kind='outside')),
        ('false local', lambda x: x['leaves'][0].update(kind='local-corner-plus-defect')),
        ('unknown kind', lambda x: x['leaves'][0].update(kind='unknown'))]
    for name, mutate in mutations:
        data = copy.deepcopy(baseline)
        mutate(data)
        try:
            result = ck.check(data, kernel)
            rejected = bool(result['failed_leaves'])
            reason = 'failed leaf predicate' if rejected else 'incomplete only'
        except ck.Invalid as error:
            rejected, reason = True, str(error)
        assert rejected, name
        controls.append({'name': name, 'rejected': rejected, 'reason': reason})
    # Separately exercise exact strictness and complete/pending logic with
    # synthetic bounds. This is a control of Python logic, never real evidence.
    class Dummy:
        def __init__(self, su): self.su = su
        def bounds(self, n, b): return [self.su, self.su, 0., 2., 2., 3., 4.]
    synthetic = {'format':'n3-phase-candidate-v1','n':2,'constants':[3.,4.,2.,2.],
                 'roots':[[-4.,0.,-4.,0.],[-4.,0.,0.,4.],[0.,4.,-4.,0.],[0.,4.,0.,4.]],
                 'complete':True,'pending':[],
                 'leaves':[{'root':r,'path':'','kind':'far'} for r in range(4)]}
    assert ck.check(synthetic, Dummy(math.nextafter(2., -math.inf)))['accepted']
    assert not ck.check(synthetic, Dummy(2.))['accepted']
    assert not ck.check(synthetic, Dummy(1.), max_leaves=3)['accepted']
    # Producer jet enclosures versus an independently summed finite triangular
    # polynomial. mpmath comparisons are diagnostics, not interval proof.
    import mpmath as mp
    mp.mp.dps = 90
    lib = ctypes.CDLL(str(OUT / 'n3_outward.so'))
    fn = lib.n3_jet
    fn.argtypes = [ctypes.c_int] + [ctypes.c_double]*4 + [ctypes.POINTER(ctypes.c_double)]
    jet_checks = []
    for n, u, v, radius in [(2,0.,0.,1e-5),(3,0.,math.pi,1e-5),
                             (3,math.pi,math.pi,1e-6),(17,.1,.1,1e-6),
                             (24,math.pi,math.pi,1e-6),(32,.4,.7,1e-5)]:
        box = [u-radius,u+radius,v-radius,v+radius]
        interval = (ctypes.c_double*6)()
        fn(n,*box,interval)
        for uu in [box[0],u,box[1]]:
            for vv in [box[2],v,box[3]]:
                x,y = mp.mpf(uu),mp.mpf(vv)
                val,da,db = mp.mpf(0),mp.mpf(0),mp.mpf(0)
                for i in range(n+1):
                    for j in range(n+1-i):
                        coefficient = (1 if i==0 else 2)*(1 if j==0 else 2)-((i,j)==(n,0))
                        val += coefficient*mp.cos(i*x)*mp.cos(j*y)
                        da -= coefficient*i*mp.sin(i*x)*mp.cos(j*y)/n
                        db -= coefficient*j*mp.cos(i*x)*mp.sin(j*y)/(n+1)
                assert all(mp.mpf(interval[2*i])-mp.mpf('1e-80') <= z <=
                           mp.mpf(interval[2*i+1])+mp.mpf('1e-80')
                           for i,z in enumerate([val,da,db]))
        jet_checks.append({'n':n,'box':box,'sample_points':9,'passed':True})
    n5 = module(OUT / 'snapshot/code/n5_central_edge_defect.py', 'review_n5')
    exact = (n5.c_exact(F(1,2)) == F(1,32) and n5.c_exact(F(1,4)) == F(19,160)
             and F(25,45056)>F(1,2048) and F(475,225280)>F(1,512)
             and F(7,288)+F(112,225)<1)
    assert exact
    n5_rows = [n5.evaluate(*case) for case in [(32,1,'-0.5'),(32,-1,'0.5'),
                 (33,1,'0.5'),(33,-1,'-0.5'),(48,1,'0.25'),(64,-1,'0')]]
    binaries = [identity(OUT / name) for name in ['libphase_checker.so','n3_outward.so']]
    dependencies = [identity(runtime / 'lib/x86_64-linux-gnu/libflint.so.19.0.0'),
                    identity(pathlib.Path('/lib/x86_64-linux-gnu/libmpfr.so.6').resolve()),
                    identity(pathlib.Path('/lib/x86_64-linux-gnu/libgmp.so.10').resolve()),
                    identity(mpfr_include / 'mpfr.h')]
    assert sources == [identity(TOPIC / name) for name in files], 'developer source changed during review run'
    report = {'scope':'MEASURED independent bounded rerun; no complete cover or degree claim',
              'reviewer':'distinct Codex Astra high assignment; runtime metadata not independently exposed',
              'rules_input':'3dda890275a7599caa707b0fb8c0b6e6f6a80643',
              'command':'python topics/padua-argmax-bridge-20261105/code/review_phase_math.py',
              'sources':sources, 'review_script':identity(pathlib.Path(__file__).resolve()),
              'compile_commands':commands,'binaries':binaries,'dependencies':dependencies,
              'compiler':subprocess.check_output(['c++','--version'],text=True).splitlines()[0],
              'python':platform.python_version(),'mpmath':mp.__version__,'mpmath_digits':90,
              'samples':samples,'corruption_controls':controls,'synthetic_logic_controls':3,
              'producer_jet_checks':jet_checks,'n5_exact_constants':exact,'n5_rerun':n5_rows,
              'cpu_seconds_python_process':time.process_time()-start}
    target = OUT / 'independent-rerun.json'
    target.write_text(json.dumps(report,indent=2)+'\n')
    summary = {k:report[k] for k in ['scope','reviewer','rules_input','command','sources','review_script',
                 'binaries','dependencies','compiler','python','mpmath','mpmath_digits']}
    summary.update(bulk=identity(target), real_samples_passed=len(samples),
                   corruption_controls_rejected=len(controls),synthetic_logic_controls=3,
                   producer_jet_point_checks=9*len(jet_checks),n5_rerun_cases=len(n5_rows),
                   all_pending_guarded=True,full_cover_run=False)
    (TOPIC / 'evidence/phase-math-review-rerun.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps({k:summary[k] for k in ['bulk','real_samples_passed','corruption_controls_rejected',
                    'synthetic_logic_controls','producer_jet_point_checks','n5_rerun_cases','full_cover_run']},indent=2))


if __name__ == '__main__':
    main()
