import json,sys
from fractions import Fraction as F
D=sys.argv[1]; cc=json.load(open(sys.argv[2]))
fa=json.load(open(D+'/evidence/g1-fit-actual.json'))
for c in cc['checks']:
    g=c['grid']; r=fa['grid_results'][g]
    si=[F(x) for x in r['signed_interval']]; m=[F(x) for x in c['late_minus_half_early']]
    ei=[F(x) for x in r['early_minimum_interval']]; me=[F(x) for x in c['early_minimum']]
    print(g, r['status'], r['witness_tau']==c['tau'], 'receipt late',[float(x) for x in si],'compact',[float(x) for x in m],
      'overlap', max(si[0],m[0])<=min(si[1],m[1]), 'early overlap', max(ei[0],me[0])<=min(ei[1],me[1]), r['SSE_clause'])
    # midpoint late-half-early from receipt diagnostics
    md=r['midpoint_ratio_descriptive_diagnostics']
    es=[F(x) for x in md['early_slope']]; ls=[F(x) for x in md['late_slope']]
    v=[ls[0]-es[1]/2, ls[1]-es[0]/2]; print('  receipt midpoint late-half early',[float(x) for x in v],'compact',[float(F(x)) for x in c['midpoint_late_minus_half_early']])
    E=[F(x) for x in md['E']['holdout_15_20_SSE']]; P=[F(x) for x in md['P']['holdout_15_20_SSE']]
    print('  midpoint 2SSE_P-SSE_E in',[float(2*P[0]-E[1]),float(2*P[1]-E[0])])
