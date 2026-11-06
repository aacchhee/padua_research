import json,copy,sys,subprocess,os,csv
S=os.environ.get('AUDIT_SCRATCH', '.')  # holds D/c3-raw.json (c3_grid.py --raw output) and K/ext.json
K=S+'/K'
d=json.load(open(S+'/D/c3-raw.json'))
def idx(f,N):
    return [i for i,c in enumerate(d['cases']) if c['family']==f and c['N']==N][0]
variants={}
def mk(name,fn):
    x=copy.deepcopy(d); fn(x); variants[name]=x
H=idx('hahn',10);Kr=idx('krawtchouk',12)
mk('nocoef',lambda x:x['cases'][H]['A-QR'].pop('coefficients'))
mk('absent',lambda x:x['cases'][H].pop('A-LU'))
mk('nostatus',lambda x:x['cases'][H]['measurement']['C4'].pop('status'))
mk('meas_method_absent',lambda x:x['cases'][H]['measurement'].pop('B-nodeqr'))
mk('badnum',lambda x:x['cases'][H]['A-QR']['coefficients'][3][1].__setitem__('a1','abc'))
mk('missingfield',lambda x:x['cases'][H]['A-QR']['coefficients'][3][1].pop('a2'))
mk('missingnu',lambda x:x['cases'][H]['A-QR']['coefficients'].pop(3))
mk('nu_int',lambda x:x['cases'][H]['A-QR']['coefficients'][3].__setitem__(0,5))
mk('r_list',lambda x:x['cases'][H]['A-QR']['coefficients'][3].__setitem__(1,[1,2]))
mk('r_none_val',lambda x:x['cases'][H]['A-QR']['coefficients'][3][1].__setitem__('a1',None))
mk('coef_empty',lambda x:x['cases'][H]['A-QR'].__setitem__('coefficients',[]))
mk('coef_notlist',lambda x:x['cases'][H]['A-QR'].__setitem__('coefficients',5))
mk('src_int',lambda x:x['cases'][H].__setitem__('A-QR',5))
mk('src_list',lambda x:x['cases'][H].__setitem__('A-QR',[]))
mk('meas_str',lambda x:x['cases'][H]['measurement'].__setitem__('A-QR','completed'))
mk('nan',lambda x:x['cases'][H]['A-QR']['coefficients'][3][1].__setitem__('a1','nan'))
mk('inf',lambda x:x['cases'][H]['A-QR']['coefficients'][3][1].__setitem__('a1','inf'))
mk('bool_ok_no_measurement',lambda x:x['cases'][H].pop('measurement'))
mk('breakdown_no_reason',lambda x:x['cases'][H]['measurement'].__setitem__('A-QR',{'status':'breakdown'}))
os.environ['OPENBLAS_NUM_THREADS']='1'
for n,x in variants.items():
    p=f'{K}/mal/{n}';os.makedirs(p,exist_ok=True)
    json.dump(x,open(p+'/native.json','w'))
    r=subprocess.run(['python3','/workspace/padua_research/topics/nn-mop-conditioning-20261106/code/c4_compare.py','--external',K+'/ext.json','--native',p+'/native.json','--raw',p+'/raw.json','--evidence',p+'/tables'],capture_output=True,text=True,cwd='/tmp')
    line=r.stderr.strip().splitlines()[-1] if r.stderr.strip() else ''
    out=''
    if r.returncode==0:
        rows=[l for l in open(p+'/tables/hahn-A-QR.csv') if l.startswith('10,')]
        out=rows[0].strip() if rows else ''
        for m in ('A-LU','C4','B-nodeqr'):
            rr=[l for l in open(p+f'/tables/hahn-{m}.csv') if l.startswith('10,')]
            out+=' | '+m+':'+(rr[0].strip()[:60] if rr else '')
    print(f'{n}: rc={r.returncode} {line[:120]} {out}')
