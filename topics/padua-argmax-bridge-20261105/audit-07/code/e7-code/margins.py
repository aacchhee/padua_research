import json,sys
from fractions import Fraction as F
r=json.load(open(sys.argv[1]))
m=r['exact_minima'];b=r['strict_bounds_greater_than']
for k in ['near_min','far_min','corner_gap']:
    v=F(m[k]['exact']); lb=F(b[k])
    print(k, float(v), v>lb, float(v-lb), m[k]['degrees'])
    # tightest 'nice' check: lb+? 
    print('  next denominators: v>', lb, ' v-lb=',float(v-lb))
print(m['floor_min'], m['M'], r['M_max'])
p=r['premises']; print(p, p['S_checks']==2*p['distinct_S_keys'], p['actual_lambda_checks']==2*p['distinct_actual_lambda_keys'], p['native_S_uppers_total']-p['native_S_uppers_contained'])
f=r['full'];print(f['certificates']==2*f['degrees'], f['degree_range'][1]-f['degree_range'][0]+1)
print(r['inputs']['old_certificates']+r['inputs']['new_certificates'], 2*(319-41+1+1), 2*(510-320+1))
