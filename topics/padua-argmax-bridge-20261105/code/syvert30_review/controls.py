"""Independent cgroup/guard decision fixtures; never exec systemd or a job."""
import argparse
import hashlib
import importlib
import json
from pathlib import Path
import resource
import sys
import tempfile
import time
from unittest.mock import patch
EXPECTED = 'd67a11930d74cf62f631adcdb3bb8c4a4e0d21b6fc63737c43730947da9f6a6f'
CAP = 128000000000

class Intercept(Exception):
    pass


def require(ok, message):
    if not ok: raise AssertionError(message)


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--source',type=Path,required=True);ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args(); source=args.source.resolve(); output=args.output.resolve()
    stream=output.open('x'); start=time.monotonic(); cpu=time.process_time()
    result={'candidate':EXPECTED,'checks':[],'native_executions':0,'systemd_executions':0,'subprocesses':0,'failure':None}
    try:
        resource.setrlimit(resource.RLIMIT_CPU,(10,15))
        candidate=(source/'CANDIDATE.sha256').read_bytes()
        require(hashlib.sha256(candidate).hexdigest()==EXPECTED,'candidate identity')
        for line in candidate.decode().splitlines():
            sha,name=line.split(); require(hashlib.sha256((source/name).read_bytes()).hexdigest()==sha,'candidate row '+name)
        sys.path.insert(0,str(source)); cg=importlib.import_module('cgroups'); guard=importlib.import_module('memory_guard'); pf=importlib.import_module('preflight')
        with tempfile.TemporaryDirectory(prefix='syvert30-review-') as temp:
            base=Path(temp); mount=base/'mount space'; current=mount/'team/job';current.mkdir(parents=True)
            fakeproc=base/'proc'; (fakeproc/'self').mkdir(parents=True)
            (fakeproc/'self/cgroup').write_text('0::/batch/team/job\n')
            escaped=str(mount).replace(' ','\\040')
            (fakeproc/'self/mountinfo').write_text('22 11 0:30 /batch '+escaped+' rw - cgroup2 cgroup rw\n')
            (fakeproc/'meminfo').write_text('MemTotal: 200000000 kB\nMemAvailable: 100000000 kB\n')
            for path,memory,swap,quota in [(mount,'max','max','4000000 100000'),(mount/'team','100000000000','0','max 100000'),(current,str(CAP),'max','3000000 100000')]:
                for name,value in [('memory.max',memory),('memory.current','123'),('memory.swap.max',swap),('cpu.max',quota)]: (path/name).write_text(value+'\n')
            def mapped(value):
                p=Path(value)
                return fakeproc/p.relative_to('/proc') if p.is_relative_to('/proc') else p
            with patch.object(cg,'Path',mapped):
                state=cg.snapshot()
                require(state['self_directory']==str(current) and state['mount']==str(mount),'mount root/escape resolution')
                require(state['effective_memory_max']==100000000000 and state['effective_swap_max']==0,'ancestor minimum')
                require(state['finite_cpu_quotas']==[[3000000,100000],[4000000,100000]],'CPU ancestry')
                require(len(state['visible_ancestry'])==3,'ancestry length')
                result['checks'].append('nonroot_mount_escaped_path_ancestor_memory_swap_cpu')
                # A more specific mount must win over the generic root mount.
                generic=base/'generic'; (generic/'batch/team/job').mkdir(parents=True)
                (generic/'batch/team/job/memory.max').write_text('1')
                info=(fakeproc/'self/mountinfo').read_text()
                (fakeproc/'self/mountinfo').write_text('23 11 0:31 / '+str(generic)+' rw - cgroup2 cgroup rw\n'+info)
                require(cg.snapshot()['self_directory']==str(current),'specific mount selection')
                result['checks'].append('most_specific_visible_mount')
                (fakeproc/'self/cgroup').write_text('0::/unmapped\n')
                try: cg.snapshot()
                except ValueError: pass
                else: raise AssertionError('unresolved cgroup accepted')
                result['checks'].append('unresolvable_membership_refused')
        base_state={'effective_memory_max':100000000000,'effective_swap_max':0,'swap_controller_visible':True,'finite_cpu_quotas':[[3000000,100000]],'host_MemTotal_bytes':200000000000}
        def execution(state, available='/usr/bin/systemd-run', host='syvert2'):
            calls=[]
            def intercept(path,argv): calls.append((path,argv));raise Intercept()
            with patch.object(guard,'snapshot',lambda:dict(state)),patch.object(guard.socket,'gethostname',lambda:host),patch.object(guard.shutil,'which',lambda name:available),patch.object(guard.os,'execv',intercept),patch.object(sys,'argv',['memory_guard.py','run','--resume']):
                try: guard.main()
                except Intercept: pass
            return calls
        calls=execution(base_state);require(len(calls)==1 and calls[0][0]==sys.executable and calls[0][1][-2:]==['run','--resume'],'bounded direct exec decision')
        result['checks'].append('bounded_cap_zero_swap_direct_server')
        for label,changes,swap_arg in [('unbounded',{'effective_memory_max':None},True),('oversize',{'effective_memory_max':CAP+1},True),('swap_unbounded',{'effective_swap_max':None},True),('swap_positive',{'effective_swap_max':1},True),('no_swap_controller',{'effective_memory_max':None,'swap_controller_visible':False,'effective_swap_max':None},False)]:
            calls=execution(dict(base_state,**changes));argv=calls[0][1]
            require(calls[0][0]=='/usr/bin/systemd-run' and '--scope' in argv and '--user' in argv and '--property=MemoryMax=128000000000' in argv,'scope decision '+label)
            require(('--property=MemorySwapMax=0' in argv)==swap_arg,'swap property '+label)
            result['checks'].append('scope_'+label)
        try: execution(dict(base_state,effective_memory_max=None),available=None)
        except RuntimeError: pass
        else: raise AssertionError('missing systemd fallback admitted')
        result['checks'].append('no_systemd_no_uncapped_fallback')
        try: execution(base_state,host='other')
        except ValueError: pass
        else: raise AssertionError('wrong host guard admitted')
        result['checks'].append('wrong_host_guard_refused')
        # Accepted preflight reaches tool discovery; all rejected cases stop
        # earlier. The intercept prevents even tool metadata/loader access.
        def preflight(state,workers=30,cores=30,host='syvert2'):
            def tools(name): raise Intercept('tool lookup reached')
            with patch.object(pf,'snapshot',lambda:dict(state)),patch.object(pf,'HERE',Path('/scratch/padua30')),patch.object(pf.socket,'gethostname',lambda:host),patch.object(pf.os,'sched_getaffinity',lambda pid:set(range(cores))),patch.object(pf.shutil,'which',tools):
                pf.inspect(workers,{})
        for label,state in [('bounded',base_state),('unlimited_cpu',dict(base_state,finite_cpu_quotas=[])),('swap_unavailable',dict(base_state,swap_controller_visible=False,effective_swap_max=None))]:
            try: preflight(state)
            except Intercept: pass
            else: raise AssertionError('accepted preflight did not reach gate '+label)
            result['checks'].append('preflight_accept_'+label)
        cases=[('uncapped',dict(base_state,effective_memory_max=None),{}),('over_budget',dict(base_state,effective_memory_max=CAP+1),{}),('low_floor',dict(base_state,effective_memory_max=80*1024**3-1),{}),('swap',dict(base_state,effective_swap_max=1),{}),('low_quota',dict(base_state,finite_cpu_quotas=[[2999999,100000]]),{}),('low_host_RAM',dict(base_state,host_MemTotal_bytes=80*1024**3-1),{}),('workers29',base_state,{'workers':29}),('cores29',base_state,{'cores':29}),('wrong_host',base_state,{'host':'other'})]
        for label,state,kwargs in cases:
            try: preflight(state,**kwargs)
            except ValueError: pass
            else: raise AssertionError('preflight failed to refuse '+label)
            result['checks'].append('preflight_refuse_'+label)
    except BaseException as error:
        result['failure']=repr(error)
    finally:
        result['CPU_seconds']=time.process_time()-cpu;result['wall_seconds']=time.monotonic()-start
        json.dump(result,stream,indent=2);stream.write('\n');stream.close()
    return 1 if result['failure'] else 0

if __name__=='__main__':raise SystemExit(main())
