import sys, ctypes, json, gzip, hashlib, time, resource, pathlib
from fractions import Fraction as F
REPO=pathlib.Path('/home/user/padua_research')
T=REPO/'topics/padua-argmax-bridge-20261105'
sys.path.insert(0,str(T/'code/phase_checker'))
import check_r8 as acceptance
so, variant, outpath = sys.argv[1], int(sys.argv[2]), pathlib.Path(sys.argv[3])
assert not outpath.exists()
raw=gzip.decompress((T/'evidence/n3-phase-n32-bootstrap-r8.json.gz').read_bytes())
assert hashlib.sha256(raw).hexdigest()=='97c339181652d37e7e3c34522959f1b7157b8ea26d3f0ab83c0ebc1c3901528e'
class K:
    def __init__(self):
        self.lib=ctypes.CDLL(so); self.fn=self.lib.phase_bounds
        self.fn.argtypes=[ctypes.c_int]+[ctypes.c_double]*4+[ctypes.POINTER(ctypes.c_double)]
        self.fn.restype=ctypes.c_int
        self.has=hasattr(self.lib,'c03_variant')
        if self.has:
            self.lib.c03_variant.argtypes=[ctypes.c_int]
            assert self.lib.c03_variant(variant)==0
            self.lib.c03_counts.argtypes=[ctypes.POINTER(ctypes.c_double)]
        self.trace=[]; self.cnt=[0.]*12
    def bounds(self,n,b):
        out=(ctypes.c_double*7)()
        e=self.fn(n,*b,out)
        if self.has:
            c=(ctypes.c_double*12)(); self.lib.c03_counts(c); self.cnt=[x+y for x,y in zip(self.cnt,c)]
        if e: raise acceptance.Invalid('kernel rejected %d'%e)
        self.trace.append((list(b),list(out))); return list(out)
k=K(); data=acceptance.strict_json(raw)
t0=time.process_time(); rep=acceptance.check(data,k); t1=time.process_time()
# margins
mins={}
for r in rep['replay']:
    if r['bounds'] is None: continue
    su,cu,dl,lc=map(F,r['bounds'][:4]); kind=r['kind']
    if kind=='far': m=lc-su
    elif kind=='corner-orbit-plus-defect': m=min(lc-cu,lc-su+dl)
    else: m=lc-su+dl
    if kind not in mins or m<mins[kind][0]: mins[kind]=(m,r['root'],r['path'])
res=dict(accepted=rep['accepted'],checked=rep['checked_leaves'],failed=len(rep['failed_leaves']),
  failed_kinds=[f['kind'] for f in rep['failed_leaves']][:5], first_failed=rep['failed_leaves'][0] if rep['failed_leaves'] else None,
  check_cpu=t1-t0, proc_cpu=time.process_time(), calls=len(k.trace), counts=k.cnt,
  min_margins={kk:(str(v[0]),float(v[0]),v[1],v[2]) for kk,v in mins.items()}, constants=rep['independent_constants'])
json.dump(dict(summary=res,replay=[(r['root'],r['path'],r['kind'],r['valid'],r['bounds']) for r in rep['replay']]),open(outpath,'x'))
print(json.dumps(res,indent=1))
