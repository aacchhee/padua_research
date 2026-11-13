import json,sys,re,math
from fractions import Fraction as F
D,S=sys.argv[1],sys.argv[2]
qr=json.load(open(S+'/evidence/fd4-qr.json'))
prod={r['n']:r for r in qr['rows']}
# table from lebesgue-intervals.md
tab={}
for line in open(S+'/final-d4/lebesgue-intervals.md'):
    m=re.match(r'\|(\d+)\|(\d+)\|([\d.]+)\|([\d.]+)\|(\d+)\|',line)
    if m: tab[int(m[1])]=(int(m[2]),F(m[3]),F(m[4]),int(m[5]))
allok=True
def check(label,mine,pl,pu,pmax_int,pe,prho,pcm,dlo=None,dhi=None):
    global allok
    ml=F(mine['lambda_lower']); mu=F(mine['lambda_upper']); mmu=F(mine['mesh_upper'])
    # (1) my rigorous enclosure inside producer's: confirms producer's interval independently
    inside = pl<=ml and mu<=pu
    # (2) producer's mesh-level enclosure of the TRUE mesh max must meet mine
    p_mesh_lo=pl; p_mesh_hi=(F(pmax_int,2**48)+pe)/(1-prho)
    meet = p_mesh_lo<=mmu and ml<=p_mesh_hi
    ok=inside and meet
    if dlo is not None: ok &= dlo<=ml and mu<=dhi and dlo<=pl and pu<=dhi and pl-dlo<F(1,10**6) and dhi-pu<F(1,10**6)
    allok&=ok
    print(label,'mine[%.6f,%.6f]'%(ml,mu),'prod[%.6f,%.6f]'%(pl,pu),'inside',inside,'meshmeet',meet,'ok',ok)
for n in range(4,17):
    mine=json.load(open(f'{D}/out_qrm2_{n}.json')); c=prod[n]['certificate']
    assert mine['sha']==prod[n]['coordinates_sha256'] and mine['N']==c['N']==tab[n][0]==math.comb(n+3,3) and c['evaluated']==tab[n][3]==mine['meshes'][0]['points']==(2*n+1)**3
    check(f'QR n{n} m2',mine['meshes'][0],F(c['lower_fraction']),F(c['upper_fraction']),c['mesh_max_integer'],F(c['mesh_error_fraction']),F(c['rho_fraction']),F(c['mesh_constant_upper_fraction']),tab[n][1],tab[n][2])
o=json.load(open(f'{D}/out_opt12.json'))
for m,f in [(2,'fd4-payload-m2.json'),(3,'fd4-payload-m3.json')]:
    c=json.load(open(S+'/evidence/'+f))['rows'][0]['certificate']; assert json.load(open(S+'/evidence/'+f))['rows'][0]['coordinates_sha256']==o['sha']
    mm=[x for x in o['meshes'] if x['m']==m][0]; assert mm['points']==c['evaluated']==(12*m+1)**3
    check(f'opt n12 m{m}',mm,F(c['lower_fraction']),F(c['upper_fraction']),c['mesh_max_integer'],F(c['mesh_error_fraction']),F(c['rho_fraction']),F(c['mesh_constant_upper_fraction']))
    print('   producer arg',c['mesh_arg_dyadic'],' mine arg idx',mm['arg_index'],[math.cos(j*math.pi/(12*m)) for j in mm['arg_index']])
m2=json.load(open(S+'/evidence/fd4-payload-m2.json'))['rows'][0]['certificate']; m3=json.load(open(S+'/evidence/fd4-payload-m3.json'))['rows'][0]['certificate']
lo=F(m2['lower_fraction']); hi=F(m3['upper_fraction'])
print('intersection exact', float(lo), float(hi), 'decimals outward:', F('25.961333')<=lo, hi<=F('29.062900'), 'tight to 1e-6:', lo-F('25.961333')<F(1,10**6), F('29.062900')-hi<F(1,10**6))
mylo=F([x for x in o['meshes'] if x['m']==2][0]['lambda_lower']); myhi=F([x for x in o['meshes'] if x['m']==3][0]['lambda_upper'])
print('my independent enclosure', float(mylo), float(myhi), 'confirms claim:', F('25.961333')<=mylo and myhi<=F('29.062900'))
print('ALL_OK' if allok else 'FAIL')
