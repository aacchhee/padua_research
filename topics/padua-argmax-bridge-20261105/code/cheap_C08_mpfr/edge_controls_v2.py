#!/usr/bin/env python3
"""Explicit numerator-zero/negative-lobe/sign controls; no box calls/build."""
import ctypes,json,math,pathlib,time
import mpmath as mp
import build

def main():
 start=time.process_time();target=build.OUT/'edge-controls-v2.json'
 if target.exists():raise RuntimeError('refuse edge receipt overwrite')
 frozen=json.loads((build.OUT/'controls.json').read_text());manifest=frozen['build'];build.verify(frozen['sources']+[manifest['binary'],manifest['preprocessed']])
 lib=ctypes.CDLL(manifest['binary']['path']);mapped=build.loaded(manifest);ptr=ctypes.POINTER(ctypes.c_double);ratio=lib.c08_ratio;ratio.argtypes=[ctypes.c_int,ctypes.c_int,ctypes.c_double,ctypes.c_double,ptr];ratio.restype=ctypes.c_int
 counts=lib.c08_counts;counts.argtypes=[ptr];mp.mp.dps=85;records=[];assertions=0;failure=None
 def test(ok,label):
  nonlocal assertions
  assertions+=1
  if not ok:raise AssertionError(label)
 try:
  cases=[(3,0,2.,2.1,'shifted-monotone-chart'),(3,0,1.4,1.5,'outside-monotone-chart'),(32,0,-.01,.02,'crossed-pole')]
  for k,turn,lo,hi,label in cases:
   out=(ctypes.c_double*4)();rc=ratio(k,turn,lo,hi,out);c=(ctypes.c_double*10)();counts(c);r=dict(k=k,turn=turn,box=[lo,hi],label=label,status=rc,bounds=list(out),counts=list(c));records.append(r);test(rc==0,'ratio status')
   epsilon=-1 if turn%2 and k%2==0 else 1
   for off in (mp.mpf(lo),(mp.mpf(lo)+mp.mpf(hi))/2,mp.mpf(hi)):
    z=turn*mp.pi+off;v=mp.fsum(mp.cos((k-1-2*j)*z) for j in range(k));d=mp.fsum(-(k-1-2*j)*mp.sin((k-1-2*j)*z) for j in range(k))
    test(mp.mpf(out[0])<=v<=mp.mpf(out[1]),'value sample');test(mp.mpf(out[2])<=d<=mp.mpf(out[3]),'derivative sample')
   if 'negative-lobe' in label:
    test(c[9]==1,'endpoint chart used on negative lobe')
    test(out[1]<0 if epsilon>0 else out[0]>0,'negative lobe retained with parity')
    sign_negative=(lo>0)==(epsilon>0);test(out[3]<=0 if sign_negative else out[2]>=0,'one-sided derivative sign')
   if label=='shifted-monotone-chart':test(c[9]==1,'correctly shifted chart admitted')
   if 'guard-reject' in label or label=='outside-monotone-chart':test(c[9]==0,'unadmitted rounded endpoint leaves base intact')
  build.verify(frozen['sources']+[manifest['binary'],manifest['preprocessed']]+mapped)
 except Exception as exc:failure=repr(exc)
 report=dict(status='FAIL' if failure else 'PASS',failure=failure,assertions=assertions,records=records,source=build.identity(pathlib.Path(__file__)),frozen_controls=build.identity(build.OUT/'controls.json'),loaded_mappings=mapped,own_cpu=time.process_time()-start)
 target.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:report[k] for k in ('status','failure','assertions','own_cpu')}));return int(failure is not None)
if __name__=='__main__':raise SystemExit(main())
