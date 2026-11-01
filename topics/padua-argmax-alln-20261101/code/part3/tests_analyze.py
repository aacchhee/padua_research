"""Summarize saved T1--T4 measurements and split T1 evidence below 1 MB.

This is postprocessing only. It does not rerun or certify any maximum.
"""
import json, sys
from pathlib import Path
import numpy as np


if __name__=='__main__':
    root=Path(sys.argv[1]);summary={'status':'MEASURED','interpretation_date':'2026-11-01'}
    d=json.loads((root/'tests_T2.json').read_text())
    fit=[]
    for a in range(1,10):
        for b in range(1,10):
            rr=[r for r in d['rows'] if (r['a'],r['b'])==(a,b)]
            n=np.array([r['n'] for r in rr]);y=np.array([r['gap'] for r in rr])
            fits={}
            for law,x in [('1/n',1/n),('log(n)/n',np.log(n)/n),('log(n)',np.log(n))]:
                design=np.column_stack((np.ones(3),x));coef=np.linalg.lstsq(design,y,rcond=None)[0]
                fits[law]={'intercept':float(coef[0]),'coefficient':float(coef[1]),'max_residual':float(max(abs(design@coef-y)))}
            fit.append({'a':a,'b':b,'fits':fits})
    summary['T2']={'criterion':'abs(gap128-gap64)>.05 at any fixed macro position',
      'verdict':'KILL under documented complementary-cell convention',
      'exceedances':len(d['criterion_exceedances']),'max_change':d['max_change_64_128'],'fits':fit}
    d=json.loads((root/'tests_T3.json').read_text())
    rows=[]
    for xy in [(0,0),(.25,0),(.5,.5),(1,1),(2,2),(0,2)]:
        rows.append({'xi':xy[0],'eta':xy[1],'lambda_minus_corner':[r['lambda_minus_corner'] for r in d['rows'] if (r['xi'],r['eta'])==xy]})
    summary['T3']={'verdict':'KILL measured n-independent raw angular profile; convergence itself not decidable from three degrees',
      'selected_rows':rows,'near_zero_threshold_dated':1e-6,
      'off_origin_near_zero_count':sum(abs(r['lambda_minus_corner'])<1e-6 and (r['xi'],r['eta'])!=(0,0) for r in d['rows'])}
    d=json.loads((root/'tests_T4.json').read_text())
    summary['T4']={'verdict':'KILL literal existing localization assembly; INCONCLUSIVE for unspecified improved asymptotic strategy',
      'literal_projection':d['literal_proof_projection'],'optimistic_central_only':d['optimistic_projections']}
    summary['T5']={'verdict':'PASS via separate finite developer exact proof; replay/audit owned by that record',
      'record':'theory/argmax-alln-codex-02-degree-two-global-argmax.md',
      'checker':'code/part3/finite_n2_exact.py','test_owner_executed_checker':False}
    t1=root/'tests_T1.json'
    if t1.exists():
        d=json.loads(t1.read_text())
        # Idempotent split: original complete profiles become per-degree files.
        ns=sorted(set(r['n'] for r in d['profiles']))
        for n in ns:
            rr=[r for r in d['profiles'] if r['n']==n]
            name=f'tests_T1_n{n}.json'
            if 'cells' in rr[0]:
                (root/name).write_text(json.dumps({'status':'MEASURED','n':n,'profiles':rr},indent=2)+'\n')
                for r in rr:
                    r['cell_count']=len(r.pop('cells'));r['cell_evidence']=name
        # Compare the positive-defect integral at each fixed macro ordinate to
        # the nearest interior cell's measured max; compare VERTICAL edges only.
        comparisons=[]
        for n in (100,200,400):
            raw=json.loads((root/f'tests_T1_n{n}.json').read_text())
            for edge in ('v+','v-'):
                rr=next(r['cells'] for r in raw['profiles'] if r['edge']==edge)
                for g in d['gbeta_integral']:
                    r=min(rr[1:-1],key=lambda z:abs(z['beta_over_pi']-g['beta_over_pi']))
                    comparisons.append({'n':n,'edge':edge,'beta_over_pi':g['beta_over_pi'],
                       'sampled_beta_over_pi':r['beta_over_pi'],'cell_gap':r['gap'],
                       'integral':g['gap_integral'],'error':r['gap']-g['gap_integral']})
        d['vertical_integral_comparisons']=comparisons
        t1.write_text(json.dumps(d,indent=2)+'\n')
        threshold=.5485148423995541-.01
        tested=[r for r in d['profiles'] if r['n']>=100]
        summary['T1']={'literal_verdict':'TRIVIAL KILL when cells containing maximal corners are included; criterion ill-posed',
          'dated_noncorner_cell_verdict':'RETAIN at sampled degrees and search resolution',
          'minimum_noncorner_cell':min(tested,key=lambda r:r['minimum_noncorner_cell']['gap']),
          'threshold':threshold,'breaches':sum(r['minimum_noncorner_cell']['gap']<threshold for r in tested),
          'series_requirement':'NOT DONE: beta-general PD-T188 series not derived; positive integral compared instead',
          'integral_comparison_max_abs_error_by_n':{str(n):max(abs(r['error']) for r in comparisons if r['n']==n) for n in (100,200,400)}}
    (root/'tests_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps({k:{a:b for a,b in v.items() if a!='fits'} if isinstance(v,dict) else v for k,v in summary.items()},indent=2))
