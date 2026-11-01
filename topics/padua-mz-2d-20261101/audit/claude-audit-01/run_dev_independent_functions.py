"""Auditor driver: import mz2d_independent_check functions from the disposable
candidate worktree and write a NEW auditor receipt (does not call main())."""
import hashlib, importlib.util, json, sys, platform, time
from pathlib import Path
WT=Path(sys.argv[1]); OUT=Path(sys.argv[2])
spec=importlib.util.spec_from_file_location('ic',WT/'tracks/mz-constants/code/mz2d_independent_check.py')
ic=importlib.util.module_from_spec(spec); spec.loader.exec_module(ic)
TOP=WT/'topics/padua-mz-2d-20261101'
data=json.loads((TOP/'evidence/exact-spectra.json').read_text())
t0=time.time()
witness,bad=ic.stored_witness(data)
regions=ic.region_checks()
nodal=[ic.nodal_check(m) for m in range(1,6)]
controls=ic.rejection_controls(data,bad)
d=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
out={'auditor':'Claude Opus 5.5 xhigh','candidate_worktree_sha':'e847601c6c1f1261d4862d63360fdfdb0df8a15b',
 'python':sys.version,'platform':platform.platform(),'sympy':ic.sp.__version__,'python_flint':ic.p.flint.__version__,
 'checker_sha256':d(WT/'tracks/mz-constants/code/mz2d_independent_check.py'),'producer_sha256':d(WT/'tracks/mz-constants/code/mz2d_exact.py'),
 'stored_receipt_sha256':d(TOP/'evidence/exact-spectra.json'),
 'stored_m30_witness':witness,'region_checks':regions,'nodal_checks':nodal,'rejection_controls':controls,
 'nodal_moment_total':sum(x['exact_nodal_moment_checks'] for x in nodal),'nodal_gram_total':sum(x['direct_nodal_Gram_and_polynomial_integral_pairs'] for x in nodal),
 'seconds':time.time()-t0}
OUT.write_text(json.dumps(out,indent=1)+'\n'); print('PASS',out['nodal_moment_total'],out['nodal_gram_total'],regions['moment_checks'],len(controls))
