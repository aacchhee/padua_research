"""Single preregistered D01 run, 300 aggregate CPU seconds; no rescue runs."""
import hashlib,json,math,os,pathlib,platform,resource,shutil,signal,subprocess,sys,time
from fractions import Fraction as F
HERE=pathlib.Path(__file__).resolve().parent
ROOT=HERE.parents[3]
OUT=ROOT/'local-output/argmax-bridge-20261105/post-audit-D01/corner'
EVIDENCE=HERE.parents[1]/'evidence/d01-corner.json'
START=time.monotonic()
def cpu():
    return sum(resource.getrusage(k).ru_utime+resource.getrusage(k).ru_stime for k in (resource.RUSAGE_SELF,resource.RUSAGE_CHILDREN))
BASE=0.0 # Include supervisor startup/import CPU from process creation.
def ident(p):
    p=pathlib.Path(p).resolve();return {'path':str(p),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def save(p,x):p.write_text(json.dumps(x,indent=2,sort_keys=True)+'\n')
def command(args,label,env=None):
    remain=295-(cpu()-BASE)
    if remain<2:raise RuntimeError('aggregate budget reserve reached')
    def limit():resource.setrlimit(resource.RLIMIT_CPU,(math.floor(remain),math.floor(remain)))
    before=cpu();p=subprocess.Popen(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE,env=env,preexec_fn=limit,start_new_session=True)
    # All preregistered commands are sequential single-worker processes.
    try:a,b=p.communicate(timeout=max(1,300-(time.monotonic()-START)))
    except subprocess.TimeoutExpired:
        os.killpg(p.pid,signal.SIGKILL);a,b=p.communicate()
    (OUT/(label+'.stdout')).write_bytes(a);(OUT/(label+'.stderr')).write_bytes(b)
    entry={'command':list(map(str,args)),'exit':p.returncode,'cpu_seconds':cpu()-before,'stdout':ident(OUT/(label+'.stdout')),'stderr':ident(OUT/(label+'.stderr'))}
    manifest['commands'].append(entry);save(OUT/'manifest.json',manifest)
    if p.returncode:raise RuntimeError('first failing command: '+label)
    if cpu()-BASE>=295:raise RuntimeError('aggregate budget reserve reached')
    return a
def envelope(row):
    n=row['n'];m=n+1;tau=m/n;L=math.log(m);H=1+math.log(2*m);pi=math.pi
    cf=30*m*m/(pi*pi*n**3)+18*m*H/(25*n**3)+3456*m*H/(25*pi*pi*n**3)+8/(n*m)
    strip=(28/5)*(n//2+1/4)/m
    def k(xs):
        sine=50*m/(9*pi*pi*n*n)*xs[3]+m/(2*n*n)*(row['B20']+row['C20'])
        leading=16*tau**3/pi**4*xs[0]+4*tau**3/pi**2*(xs[1]+xs[2])
        return {'leading':leading,'sine':sine,'remainder':cf,'strip':strip,'K':leading+sine+cf+strip-L/3}
    return {'L':L,'low':k(row['sums_low']),'upper':k([a+b for a,b in zip(row['sums_low'],row['tail_upper'])])}
def exact(n):
    sums=[F(0)]*4;b=c=F(0);cnt=0
    for j in range(n+1):
        for r in range(n+2):
            if not (j+r)%2 or (r==j+1 and 2*j>=n):continue
            s=F(j+r)-F(1,6);g=abs(F(j-r)+F(j,n))-F(1,6)
            x=[1/(s*g**3),1/(s**3*g),1/(s*s*g*g),1/g**2]
            sums=[a+v for a,v in zip(sums,x)];b+=1/s**2;c+=1/(F(2*n+1-j-r)-F(1,6))**2;cnt+=1
    return sums+[b,c],cnt
def closure():
    paths={pathlib.Path(sys.executable).resolve()}
    for mod in list(sys.modules.values()):
        p=getattr(mod,'__file__',None)
        if p and pathlib.Path(p).is_file():paths.add(pathlib.Path(p).resolve())
    maps=pathlib.Path('/proc/self/maps').read_text();(OUT/'python.maps').write_text(maps)
    for line in maps.splitlines():
        p=line.split()[-1]
        if p.startswith('/') and pathlib.Path(p).is_file():paths.add(pathlib.Path(p).resolve())
    return [ident(p) for p in sorted(paths)]
manifest={'status':'STARTED','rules_head':'4cf68980fa0538b53e2aea7174ed6e5782a34908','model':'gpt-6.1-sol; serving effort metadata unexposed','scope':'MEASURED C07 full envelope; no proof or minimum-function bracket','commands':[]}
CREATED=False
def main():
    global CREATED
    OUT.mkdir(parents=True,exist_ok=True)
    if (OUT/'preregistration.json').exists():raise RuntimeError('refuse overwrite or rescue')
    plan={'degrees':[1000,1001,10000,10001,20000,20001,100000,100001],'diagonal_cutoff':127,'full_controls':[17,1000,1001],'exact_fraction_controls':[17],'aggregate_cpu_cap':300,'source':[ident(HERE/'measure.cpp'),ident(__file__)],'spec':ident(HERE/'SPEC.md'),'no_rescue':True,'gate':'K_upper<=4 at n1000; kill K_low>=0.1*log(n+1)^2-log(n+1)/3 at n20000; overlap inconclusive'}
    save(OUT/'preregistration.json',plan);CREATED=True;manifest['preregistration']=ident(OUT/'preregistration.json')
    manifest['platform']=platform.platform();manifest['python']=sys.version
    manifest['python_closure_before']=closure()
    compiler=shutil.which('g++');manifest['compiler']=ident(compiler)
    command([compiler,'--version'],'compiler-version')
    helpers={}
    for name in ['cc1plus','collect2','as','ld']:
        p=command([compiler,'-print-prog-name='+name],'locate-'+name).decode().strip()
        helpers[name]=ident(shutil.which(p) if '/' not in p else p)
    manifest['build_helpers']=helpers
    binary=OUT/'measure'
    command([compiler,'-O2','-std=c++17','-fno-fast-math',str(HERE/'measure.cpp'),'-o',str(binary)],'build')
    manifest['binary']=ident(binary)
    rows=[]
    for n,mode in [(17,1),(1000,1),(1001,1)]+[(n,0) for n in plan['degrees']]:
        tag=f'n{n}-mode{mode}';env=dict(os.environ,D01_MAPS=str(OUT/(tag+'.maps')))
        row=json.loads(command([str(binary),str(n),'127',str(mode)],tag,env));row['envelope']=envelope(row);rows.append(row)
    rational,count=exact(17);reference=rows[0]
    values=reference['sums_low']+[reference['B20'],reference['C20']]
    controls={'exact_n17':[str(x) for x in rational],'count':count,'relative_errors':[abs(v-float(q))/max(1,abs(float(q))) for v,q in zip(values,rational)]}
    if max(controls['relative_errors'])>1e-14 or count!=reference['board']:raise RuntimeError('exact rational control failure')
    for full,trunc in [(rows[1],rows[3]),(rows[2],rows[4])]:
        if full['n']!=trunc['n']:raise RuntimeError('control identity mismatch')
        for f,a,t in zip(full['sums_low'],trunc['sums_low'],trunc['tail_upper']):
            if f<a-1e-12 or f>a+t+1e-12:raise RuntimeError('full sum outside positive-tail bracket')
    libs=set()
    for p in OUT.glob('n*.maps'):
        for line in p.read_text().splitlines():
            q=line.split()[-1]
            if q.startswith('/') and pathlib.Path(q).is_file():libs.add(pathlib.Path(q).resolve())
    manifest['native_loaded_closure']=[ident(p) for p in sorted(libs)]
    manifest['python_closure_after']=closure();manifest['rows']=rows;manifest['controls']=controls
    manifest['cpu_seconds']=cpu()-BASE;manifest['wall_seconds']=time.monotonic()-START;manifest['status']='COMPLETED'
    save(OUT/'manifest.json',manifest)
    receipt={k:manifest[k] for k in ['status','rules_head','model','scope','cpu_seconds','wall_seconds']}
    receipt.update(preregistration=manifest['preregistration'],manifest=ident(OUT/'manifest.json'),sources=plan['source'],spec=plan['spec'],rows=rows[3:],controls={'exact_fraction_n17_max_relative_error':max(controls['relative_errors']),'full_n1000_n1001_within_tail_brackets':True},binary=manifest['binary'],failures=[])
    save(EVIDENCE,receipt)
    print(json.dumps(receipt,indent=2))
try:main()
except BaseException as e:
    if CREATED:
        manifest.update(status='FAILED',failure=repr(e),cpu_seconds=cpu()-BASE);save(OUT/'manifest.json',manifest)
        save(EVIDENCE,{'status':'FAILED','failure':repr(e),'manifest':ident(OUT/'manifest.json'),'cpu_seconds':cpu()-BASE,'no_rescue':True})
    raise
