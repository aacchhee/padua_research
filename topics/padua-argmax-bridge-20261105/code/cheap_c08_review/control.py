#!/usr/bin/env python3
"""Independent bounded C08 review; no tree traversal or producer invocation."""
import ctypes, hashlib, importlib.util, json, math, os
from pathlib import Path
import resource, signal, subprocess, sys, tempfile, time
from fractions import Fraction as F
import mpmath as mp

ROOT=Path(__file__).resolve().parents[4]
TOPIC=ROOT/'topics/padua-argmax-bridge-20261105'
HERE=TOPIC/'code/cheap_C08_mpfr'
EVIDENCE=TOPIC/'evidence/c08-review-mpfr.json'
PINS={'producer.c':'bf32c04994abf53cda5aca1cc63ceb2778d6339565a8cbc7c6337d9af22dc87d',
      'c08_interval.h':'275936b502180f2d92af94eb2138815114ba75afb9c258cadffa44e580be0a03',
      'build.py':'fff281f0c765025ec182937aff38398e7eedfd11b66bfeb36f105734b730d81f'}

def ident(p):
    p=Path(p).resolve();b=p.read_bytes()
    return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())

def worker(rawpath):
    resource.setrlimit(resource.RLIMIT_CPU,(48,50))
    start=time.process_time();child=resource.getrusage(resource.RUSAGE_CHILDREN)
    report={'status':'FAIL','assertions':0,'ratios':[],'jets':[],'boxes':[],'findings':[]}
    def test(ok,label):
        report['assertions']+=1
        if not ok:raise AssertionError(label)
    try:
        sourceids=[ident(HERE/k) for k in PINS]+[ident(__file__)]
        for i,(name,sha) in enumerate(PINS.items()):test(sourceids[i]['sha256']==sha,'source pin '+name)
        spec=importlib.util.spec_from_file_location('c08_review_builder',HERE/'build.py')
        build=importlib.util.module_from_spec(spec);spec.loader.exec_module(build)
        binary,manifest=build.build();lib=ctypes.CDLL(str(binary))
        manifest['actual_loaded_mappings']=build.loaded(manifest)
        ptr=ctypes.POINTER(ctypes.c_double)
        def bind(name,args,rest=ctypes.c_int):
            f=getattr(lib,name);f.argtypes=args;f.restype=rest;return f
        ratio=bind('c08_ratio',[ctypes.c_int,ctypes.c_int,ctypes.c_double,ctypes.c_double,ptr])
        counter=bind('c08_counts',[ptr],None)
        jet=bind('n3_jet',[ctypes.c_int]+[ctypes.c_double]*4+[ptr],None)
        native=bind('n3_box',[ctypes.c_int]+[ctypes.c_double]*6+[ctypes.c_int,ptr])
        constant=bind('n3_constants',[ctypes.c_int,ptr],None)
        geometry=bind('n3_geometry',[ctypes.c_int]+[ctypes.c_double]*4)
        guard=bind('c08_guard',[ctypes.c_int]+[ctypes.c_double]*4)
        def counts():
            a=(ctypes.c_double*10)();counter(a);return list(a)
        mp.mp.dps=85
        def rd(k,z):
            frequencies=range(k-1,-k,-2)
            vals=[(mp.cos(j*z),-j*mp.sin(j*z)) for j in frequencies]
            return mp.fsum(x[0] for x in vals),mp.fsum(x[1] for x in vals)
        def point(n,u,v):
            a,ap=rd(n+1,(u+v)/2);b,bp=rd(n+1,(u-v)/2)
            c,cp=rd(n,(u+v)/2);d,dp=rd(n,(u-v)/2)
            ds=ap*b+cp*d;dt=a*bp+c*dp
            return a*b+c*d-mp.cos(n*u),((ds+dt)/2+n*mp.sin(n*u))/n,(ds-dt)/(2*(n+1))
        cases=[]
        for k in (1,2,3,32,513):
            for turn in (-3,0,2):cases.append((k,turn,-1e-6,2e-6,'pole-crossing'))
        for k in (3,32,513):
            z=float(mp.pi/k);lo=math.nextafter(z,-math.inf);hi=math.nextafter(z,math.inf)
            test(mp.mpf(lo)*k<mp.pi<mp.mpf(hi)*k,'genuine numerator-zero bracket')
            for turn in (-1,0):
                cases.extend([(k,turn,lo,hi,'numerator-zero'),
                    (k,turn,3.3/k,3.8/k,'negative-lobe-positive-residual'),
                    (k,turn,-3.8/k,-3.3/k,'negative-lobe-negative-residual')])
        cases.extend([(32,0,.125,.125,'outward-guard-boundary'),(3,0,1.4,1.5,'guard-rejected'),
                      (3,0,2.,2.1,'shifted-chart'),(513,0,-5.,5.,'global-fallback'),
                      (32,0,31/256,31/256,'interior-endpoint')])
        for k,turn,lo,hi,label in cases:
            out=(ctypes.c_double*4)();rc=ratio(k,turn,lo,hi,out);ct=counts()
            report['ratios'].append(dict(k=k,turn=turn,box=[lo,hi],label=label,status=rc,bounds=list(out),counts=ct))
            test(rc==0 and all(math.isfinite(x) for x in out),'finite ratio')
            for off in (mp.mpf(lo),(mp.mpf(lo)+mp.mpf(hi))/2,mp.mpf(hi)):
                value,derivative=rd(k,turn*mp.pi+off)
                test(mp.mpf(out[0])<=value<=mp.mpf(out[1]),'ratio value containment')
                test(mp.mpf(out[2])<=derivative<=mp.mpf(out[3]),'ratio derivative containment')
            if k==1:test(list(out)==[1,1,0,0],'exact R1')
            if 'negative-lobe' in label:
                ep=-1 if turn%2 and k%2==0 else 1
                test(ct[9]==1,'negative lobe refinement used')
                test(out[1]<0 if ep>0 else out[0]>0,'negative lobe value parity')
                test(out[3]<=0 if (lo>0)==(ep>0) else out[2]>=0,'derivative sign parity')
            if label in ('guard-rejected','outward-guard-boundary'):test(ct[9]==0,'literal rounded guard rejection')
        for args in [(1,0,math.nan,0.),(1,0,0.,math.inf),(514,0,0.,0.),(0,0,0.,0.),(2,5,0.,0.)]:
            test(ratio(*args,(ctypes.c_double*4)())!=0,'invalid scalar rejected')
        for n,b in [(2,[-.01,.02,-.03,.04]),(7,[.4,.41,-.2,-.19]),(32,[0.,0.,0.,0.]),(512,[.001,.0011,.002,.0021])]:
            out=(ctypes.c_double*6)();jet(n,*b,out);report['jets'].append(dict(n=n,box=b,bounds=list(out)))
            for t in (mp.mpf(0),mp.mpf('.5'),mp.mpf(1)):
                u=mp.mpf(b[0])+(mp.mpf(b[1])-mp.mpf(b[0]))*t;v=mp.mpf(b[2])+(mp.mpf(b[3])-mp.mpf(b[2]))*(1-t)
                for j,value in enumerate(point(n,u,v)):test(mp.mpf(out[2*j])<=value<=mp.mpf(out[2*j+1]),'kernel value/phase-gradient containment')
        counts()
        # Independent small-board value/orbit normalization, with forced profile.
        for n,aa,bb in [(2,.125,.2),(3,-.1,.15)]:
            vals={(r,s):point(n,(r*mp.pi+mp.mpf(aa))/n,(s*mp.pi+mp.mpf(bb))/(n+1))[0]
                  for r in range(2*n) for s in range(1-r%2,2*(n+1),2)}
            norm=2*n*(n+1);S=mp.fsum(abs(x) for x in vals.values())/norm
            C=mp.fsum(abs(vals[r,s]+vals[(-r)%(2*n),s]+vals[r,(-s)%(2*(n+1))]+vals[(-r)%(2*n),(-s)%(2*(n+1))]) for r,s in vals)/(4*norm)
            out=(ctypes.c_double*6)();rc=native(n,aa,aa,bb,bb,0.,0.,1,out)
            test(rc==0 and out[3]==1,'small board profile status')
            test(S<=mp.mpf(out[0]) and C<=mp.mpf(out[1]),'board/orbit normalization')
            qh=[mp.fsum(abs(x)+abs(vals[(2*j-r)%(2*n),s])-abs(x+vals[(2*j-r)%(2*n),s]) for (r,s),x in vals.items())/(2*norm) for j in range(n+1)]
            qv=[mp.fsum(abs(x)+abs(vals[r,(2*k-s)%(2*(n+1))])-abs(x+vals[r,(2*k-s)%(2*(n+1))]) for (r,s),x in vals.items())/(2*norm) for k in range(n+2)]
            admissible=[max(qh[j],qv[k]) for j in range(n+1) for k in range(1-j%2,n+2,2)
                        if 0<=j*mp.pi+aa<=n*mp.pi and 0<=k*mp.pi+bb<=(n+1)*mp.pi and not (j in (0,n) and k in (0,n+1))]
            test(mp.mpf(out[2])<=min(admissible),'projected deficit lower normalization')
            report['boxes'].append(dict(n=n,box=[aa,aa,bb,bb],label='independent-small-board',bounds=list(out),counts=counts()))
        savedpath=TOPIC/'evidence/c08-mpfr-bounded.json';saved=json.loads(savedpath.read_text());inputids=[ident(savedpath)]
        c=(ctypes.c_double*4)();constant(32,c);test(all(math.isfinite(v) for v in c),'constants finite');counts()
        for item in saved['boxes']:
            test(time.process_time()-start<40,'prospective bounded CPU')
            out=(ctypes.c_double*6)();rc=native(32,*item['box'],c[2],0.,1,out)
            test(rc==0 and list(out)==item['bounds'],'saved box exact reproduction')
            su,cu,dl=map(F,out[:3]);lc=F(c[2]);kind=item['kind']
            test(su<lc if kind=='far' else (cu<lc and su-dl<lc if kind=='corner-orbit-plus-defect' else su-dl<lc),'saved strict predicate')
            report['boxes'].append(dict(n=32,box=item['box'],root=item['root'],path=item['path'],kind=kind,bounds=list(out),counts=counts()))
        test(guard(64,0.,.25,0.,.25)==1 and guard(64,0.,math.nextafter(.25,1.),0.,.25)==0,'exact radius boundary')
        test(guard(63,0.,.25,0.,.25)==0 and guard(64,0.,math.nan,0.,.25)==0,'guard degree/nonfinite')
        broad=[-8*math.pi,8*math.pi,0.,0.];result=geometry(2,*broad)
        report['findings'].append(dict(label='geometry-wide-box-domain',n=2,box=broad,result=result,
            meaning='returns local2 outside original phase square; full-box monotonic-domain guard absent'))
        for key in ('tools','tool_runtime_closure','headers','linked_runtime_closure','actual_loaded_mappings'):build.verify(manifest[key])
        build.verify(sourceids+inputids+[manifest[k] for k in ('source','header','preprocessed','binary')])
        test(build.loaded(manifest)==manifest['actual_loaded_mappings'],'loaded mappings unchanged')
        report.update(status='PASS_WITH_DOMAIN_FINDING',build=manifest,sources=sourceids,inputs=inputids,constants=list(c))
    except Exception as exc:report['failure']=repr(exc)
    finally:
        end=resource.getrusage(resource.RUSAGE_CHILDREN)
        report.update(own_cpu=time.process_time()-start,child_cpu=end.ru_utime+end.ru_stime-child.ru_utime-child.ru_stime)
        Path(rawpath).write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    return int('failure' in report)

def main():
    if len(sys.argv)==3 and sys.argv[1]=='--worker':return worker(sys.argv[2])
    if EVIDENCE.exists():raise RuntimeError('refuse review receipt overwrite')
    start=time.process_time();wall=time.monotonic();before=resource.getrusage(resource.RUSAGE_CHILDREN)
    work=Path(tempfile.mkdtemp(prefix='c08-independent-review-'));raw=work/'raw.json'
    p=subprocess.Popen([sys.executable,__file__,'--worker',str(raw)],start_new_session=True)
    stopped=False;peak=0
    while p.poll() is None:
        ticks=0
        for path in Path('/proc').iterdir():
            if not path.name.isdecimal():continue
            try:
                f=(path/'stat').read_text().rsplit(')',1)[1].split()
                if int(f[2])==p.pid:ticks+=sum(int(f[i]) for i in (11,12,13,14))
            except (FileNotFoundError,ProcessLookupError):pass
        used=ticks/os.sysconf('SC_CLK_TCK')+time.process_time()-start;peak=max(peak,used)
        if used>=55:os.killpg(p.pid,signal.SIGKILL);stopped=True;break
        time.sleep(.1)
    rc=p.wait();after=resource.getrusage(resource.RUSAGE_CHILDREN)
    total=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime+time.process_time()-start
    r=json.loads(raw.read_text()) if raw.exists() else {}
    summary=dict(status=r.get('status','NO_REPORT'),exit_status=rc,watchdog_stopped=stopped,
       total_cpu=total,peak_group_cpu=peak,wall=time.monotonic()-wall,raw=ident(raw) if raw.exists() else None,
       control=ident(__file__),assertions=r.get('assertions'),ratio_cases=len(r.get('ratios',[])),
       jet_cases=len(r.get('jets',[])),box_cases=len(r.get('boxes',[])),findings=r.get('findings'),
       failure=r.get('failure'),sources=r.get('sources'),constants=r.get('constants'),
       full_producer_run=False,full_candidate_check=False,new_degree=False)
    with EVIDENCE.open('x') as f:json.dump(summary,f,indent=2);f.write('\n')
    print(json.dumps(summary,indent=2));return rc

if __name__=='__main__':raise SystemExit(main())
