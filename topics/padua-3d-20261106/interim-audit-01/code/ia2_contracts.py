#!/usr/bin/env python3
"""Focused followup to finite-difference truncation; fixed-payload rejection probes."""
import argparse, base64, hashlib, json, os, platform, struct, subprocess, sys
from pathlib import Path
import numpy as np
import scipy
from scipy.linalg import solve
from scipy.special import logsumexp
import ia2_adversarial as audit

def main():
    p=argparse.ArgumentParser(); p.add_argument('--scratch',type=Path,required=True); p.add_argument('--output',type=Path,required=True); a=p.parse_args(); a.scratch.mkdir(parents=True,exist_ok=False)
    TOP=audit.TOP; receipt=TOP/'evidence/u2-admissible-holdout.json'; rec=json.loads(receipt.read_text()); raw=Path(rec['scratch']); fullpath=raw/'full-results.json'
    paths=[Path(__file__),Path(audit.__file__),receipt,fullpath,TOP/'evidence/u2-degree12-nodes.json',TOP/'code/uc12_payload_check.py']
    paths.extend(audit.ROOT/p for p in rec['sources'])
    full=json.loads(fullpath.read_text()); beta=next(r for r in full['optimizations'] if r['n']==12)['beta']
    payload=json.loads((TOP/'evidence/u2-degree12-nodes.json').read_text()); blob=base64.b85decode(payload['coordinates_base85']); x=np.frombuffer(blob,dtype='<f8').reshape(455,3)
    grid=np.array(list(audit.itertools.product(np.cos(np.linspace(0,np.pi,21)),repeat=3))); E=audit.basis(grid)/audit.SCALE
    sys.path.insert(0,str(TOP/'code')); import u2_core
    value,gradient,_=u2_core.smooth_value_gradient(x.ravel(),12,E,beta)
    def obj(x):
        c=solve((audit.basis(x)/audit.SCALE).T,E.T).T
        return float(logsumexp(beta*np.sqrt(c*c+1e-16).sum(axis=1))/beta)
    rng=np.random.default_rng(audit.SEED+4); rows=[]
    for k in range(3):
        d=rng.standard_normal(x.shape); d[abs(x)>.999]=0; d/=np.linalg.norm(d); analytic=float(gradient@d.ravel()); cases=[]
        for h in (2e-6,2e-7,2e-8,2e-9,2e-10):
            central=(obj(x+h*d)-obj(x-h*d))/(2*h)
            cases.append(dict(h=h,central=central,error=abs(central-analytic)/max(1,abs(analytic),abs(central))))
        rows.append(dict(direction=k,analytic=analytic,steps=cases))
    checker=TOP/'code/uc12_payload_check.py'; mutations=[]
    for name,mutated in [('nan_first_coordinate',struct.pack('<Q',0x7ff8000000000000)+blob[8:]),('duplicate_first_two_nodes',blob[:24]+blob[:24]+blob[48:])]:
        data=dict(payload); data['coordinates_base85']=base64.b85encode(mutated).decode(); data['coordinates_sha256']=hashlib.sha256(mutated).hexdigest(); path=a.scratch/(name+'.json'); path.write_text(json.dumps(data)+'\n')
        command=[sys.executable,str(checker),'--payload',str(path),'--output',str(a.scratch/(name+'-output.json'))]
        r=subprocess.run(command,capture_output=True,text=True); log=a.scratch/(name+'.log'); log.write_text(r.stdout+r.stderr)
        assert r.returncode!=0
        mutations.append(dict(name=name,command=command,exit=r.returncode,input=audit.identity(path),log=audit.identity(log),last_error=r.stderr.splitlines()[-1]))
    failed=[]
    pilot=TOP/'evidence/u2-pilot.json'; pilotrec=json.loads(pilot.read_text()); oldraw=Path(pilotrec['scratch']); paths.append(pilot)
    for n in (2,6,8):
        ep=oldraw/f'n{n}-optimization-events.json'; tp=oldraw/f'n{n}-optimization-trials.npz'; paths.extend([ep,tp]); events=json.loads(ep.read_text()); trials=np.load(tp)['coordinates']; points=trials[1].reshape(-1,3)
        failed.append(dict(n=n,N=len(points),first_trial_unique=len(np.unique(points,axis=0)),first_trial_error=events[1].get('failure'),returned_to_start=np.array_equal(trials[0],trials[-1]),trial_count=len(trials),producer_termination=next(r['termination'] for r in pilotrec['optimizations'] if r['n']==n)))
    pins=[audit.identity(p) for p in sorted(set(paths))]
    out=dict(status='MEASURED numerical derivative followup plus negative-input checker probes; not a new optimizer round',command=sys.argv,versions=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__),threads={k:os.getenv(k) for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS')},reason='Initial n12 h2e-6 directional errors reached8.30e-5 near epsilon1e-8 smoothing; examine truncation/cancellation without tuning nodes.',objective_independent_delta=abs(obj(x)-value),gradient=rows,payload_mutations=mutations,R1_failed_traces=failed,pins=pins,raw_policy='unique local regenerate-only, no archival delivery',scope='The checker mutations must fail; the real payload exact proof is in ia2-payload. Derivative agreement is numerical, not a proof of convergence.')
    assert pins==[audit.identity(p) for p in sorted(set(paths))]
    text=json.dumps(out,separators=(',',':'),allow_nan=False)+'\n'; assert len(text.encode())<16384; a.output.write_text(text)
    print(json.dumps(dict(gradient=rows,mutations=[dict(name=r['name'],exit=r['exit'],error=r['last_error']) for r in mutations],R1=failed)),flush=True)

if __name__=='__main__': main()
