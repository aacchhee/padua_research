import json
R='/home/user/padua_research/topics/padua-lanczos-frontier-20261105/evidence/'
rep=json.load(open(R+'g4-replay.json'))
ind=json.load(open(R+'g4-independent.json'))
old={}
for c in rep['cases']:
    for m,v in c['checks']['methods'].items():
        old[(c['name'],m)]=(v['old_gap'],v['new_gap'])
print(f"{'case':9s}{'method':13s}{'hist':>12s}{'curHas':>12s}{'curNeh':>12s}{'|dHist|':>11s}{'kernSpan':>11s}{'ratio':>8s}{'maxF/u_op':>9s}{'amp_rel':>10s}{'recon/err':>10s}")
for c in ind['cases']:
    for m in c['methods']:
        meth=m['method']; key=meth if meth!='upstream_yx' else 'upstream_yx'
        h,cur=old[(c['name'],key)]
        ctrl=m['controls']
        has=[x for x in ctrl if x['core']=='Haswell'][0]['normal_Q']; neh=[x for x in ctrl if x['core']=='Nehalem'][0]['normal_Q']
        dh=min(abs(h-has),abs(h-neh)); ks=m['kernel_normal_difference']
        mo=max(x['max_local_over_u_operation_sum'] for x in ctrl)
        rq=max(m['reconstruction_quality_ratios'])
        print(f"{c['name']:9s}{meth:13s}{h:12.4e}{has:12.4e}{neh:12.4e}{dh:11.3e}{ks:11.3e}{dh/ks:8.3f}{mo:9.3f}{'':>10s}{rq:10.2e}")
