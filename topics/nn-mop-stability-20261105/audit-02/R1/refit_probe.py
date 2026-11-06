# Developer-code re-execution (NOT independent): feed the COMMITTED raw target to backward_projection.fit
# on this platform and compare the returned rational witness hash with the committed one.
import sys, json, time
from pathlib import Path
CODE=Path('/home/user/padua_research/topics/nn-mop-stability-20261105/code')
sys.path.insert(0,str(CODE))
import backward_projection as dev
ref=json.load(open(sys.argv[1])); want=set(sys.argv[2:])
for c in ref['cases']:
    key='%d:%s:%s'%(c['N'],c['family'],c['method'])
    if key not in want: continue
    raw={tuple(r['nu']):{f:float.fromhex(r[f]) for f in dev.FIELDS} for r in c['raw_coefficients']}
    t=time.time(); fit=dev.fit(raw,c['N'],c['family'],dps=160)
    print(key,'witness_equal=',fit['rational_input_sha256']==c['rational_input_sha256'],
          'eta_d_u=%.9g eta_c_u=%.9g'%(fit['input_in_units_u'],fit['correction_in_units_u']),
          'ref %.9g %.9g'%(c['metrics']['input_in_units_u'],c['metrics']['correction_in_units_u']),
          'conv=',fit.get('optimizer_stationarity_converged'),fit.get('optimizer_stop_reason'),'%.1fs'%(time.time()-t),flush=True)
