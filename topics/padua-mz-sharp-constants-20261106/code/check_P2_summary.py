import copy, hashlib, json, math, pathlib, subprocess, sys, tempfile

topic=pathlib.Path(__file__).resolve().parents[1]
code=topic/'code/P2_summary.py'
b2=-0.0955298083997758
base={'P2-b2-calibration.json': {'registered_b2': b2,'calibration_pass': True}}
for m in (1600,1601,3000,3001):
    gap=.5-.038*math.log(m//2)
    row=dict(m=m,L_low6=[-.1336,-.1336,-.0955,-.0955,-.039,-.039],
             L_at_Qmin=-.0955,doublet_weights=[.01,.95,.01],
             Q_compressed_spectra=[[gap,gap],[0,0],[0,0]],
             orthogonality_error=0,Q_checks={'residuals':[0]},
             L_checks={'residuals':[0]*6},logR=math.log(m//2),
             logm=math.log(m),Q_min=b2*math.log(m))
    base[f'P2-m{m}.json']={'row':row,'identities':{}}
def unchanged(d): pass
def weight_kill(d): d['P2-m1600.json']['row']['doublet_weights'][1]=.8
def missing(d): del d['P2-m3001.json']
def failure(d): d['P2-m3001.json']={'failure':{'type':'ArpackNoConvergence'}}
def bad_calibration(d):
    d['P2-b2-calibration.json']['calibration_pass']=False
    weight_kill(d)
def invalid_other(d):
    d['P2-m3001.json']['row']['Q_checks']['residuals']=[1]
    weight_kill(d)
def ambiguous_pair(d):
    d['P2-m1600.json']['row']['L_low6'][1]=-.12
def mid_rate(d):
    for m in (1600,1601,3000,3001):
        gap=.5-.05*math.log(m//2)
        d[f'P2-m{m}.json']['row']['Q_compressed_spectra'][0]=[gap,gap]
def rate_kill(d):
    for m in (1600,1601,3000,3001):
        gap=.5-.06*math.log(m//2)
        d[f'P2-m{m}.json']['row']['Q_compressed_spectra'][0]=[gap,gap]
def slope_kill(d):
    for m in (1600,1601,3000,3001):
        d[f'P2-m{m}.json']['row']['Q_min']=(b2+.01)*math.log(m)
cases=[('all_valid_pass',unchanged,'PASS_FINITE_TEST'),
       ('valid_weight_kill',weight_kill,'SCOPED_KILL'),
       ('missing_required_receipt',missing,'INCONCLUSIVE'),
       ('failed_producer_receipt',failure,'INCONCLUSIVE'),
       ('bad_calibration_overrides_departure',bad_calibration,'INCONCLUSIVE'),
       ('invalid_other_row_overrides_departure',invalid_other,'INCONCLUSIVE'),
       ('ambiguous_pair',ambiguous_pair,'INCONCLUSIVE'),
       ('rate_outside_target_inside_kill_band',mid_rate,'INCONCLUSIVE'),
       ('valid_rate_kill',rate_kill,'SCOPED_KILL'),
       ('valid_slope_kill',slope_kill,'SCOPED_KILL')]
results=[]
for name,mutate,expect in cases:
    data=copy.deepcopy(base);mutate(data)
    with tempfile.TemporaryDirectory(prefix='P2-summary-test-') as td:
        folder=pathlib.Path(td)
        for filename,d in data.items(): (folder/filename).write_text(json.dumps(d))
        output=folder/'summary.json'
        run=subprocess.run([sys.executable,str(code),'--directory',str(folder),'--output',str(output)],capture_output=True,text=True)
        result=json.loads(output.read_text()) if output.exists() else {}
        got=result.get('outcome')
        assert run.returncode==0 and got==expect,(name,run.returncode,got,run.stderr)
        results.append(dict(case=name,expected=expect,observed=got,exit_code=run.returncode,
                            prerequisite_failures=result.get('prerequisite_failures'),
                            valid_row_departures=result.get('valid_row_departures')))
report=dict(status='software control-flow checks on synthetic receipts; no scientific observations',
            summary_code_sha256=hashlib.sha256(code.read_bytes()).hexdigest(),
            test_script_sha256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
            command=sys.argv,python=sys.version,cases=results,all_pass=True)
output=topic/'evidence/check-P2-summary-control.json'
output.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'cases':len(results),'all_pass':True,'code_sha256':report['summary_code_sha256']}))
