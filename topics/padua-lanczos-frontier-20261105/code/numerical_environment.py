#!/usr/bin/env python3
"""Emit actual launch environment for future numerical receipts on stdout."""
import contextlib,datetime,hashlib,io,json,os,pathlib,platform,sys
import numpy as np
import scipy
import scipy.linalg
from threadpoolctl import threadpool_info
# Load both BLAS clients before recording actual dispatch.
np.dot(np.ones((2,2)),np.ones((2,2)))
scipy.linalg.svd(np.eye(2))
info={}
for line in pathlib.Path('/proc/cpuinfo').read_text().splitlines():
    if ':' in line:
        k,v=map(str.strip,line.split(':',1))
        if k in ('model name','flags','vendor_id') and k not in info:info[k]=v
out=io.StringIO()
with contextlib.redirect_stdout(out):np.show_runtime()
p=pathlib.Path(__file__)
receipt=dict(schema='numerical-environment-v1',observed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),scope='Actual response-session environment observation only; not a historical suite receipt or rerun',collector_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),python=sys.version,platform=platform.platform(),machine=platform.machine(),libc=platform.libc_ver(),cpu=info,numpy=np.__version__,scipy=scipy.__version__,blas_dispatch=threadpool_info(),numpy_runtime=out.getvalue(),environment={k:os.environ.get(k) for k in ['OPENBLAS_CORETYPE','OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NPY_DISABLE_CPU_FEATURES']})
print(json.dumps(receipt,indent=1))
