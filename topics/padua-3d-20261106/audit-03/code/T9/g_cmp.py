import json,sys
for fam,mine,theirs in [('qr',sys.argv[1],sys.argv[2]),('localdet',sys.argv[3],sys.argv[4])]:
    a=json.load(open(mine));b=json.load(open(theirs))
    bb={r['n']:r for r in b['rows']}
    mx=0
    for r in a['rows']:
        o=bb[r['n']]
        d={k:abs(r[k]-o[k]) for k in ('mesh21','mesh41','local') if k in r}
        same=r['node_sha256']==o['node_sha256']
        mx=max(mx,max(d.values()))
        print(fam,r['n'],'local',round(r['local'],9),'receipt',round(o['local'],9),'maxdiff',max(d.values()),'node_hash_equal',same,'cond',f"{r['cond']:.3g}",'resid',f"{r['resid']:.2g}",'success',r['success'])
    print(fam,'max abs diff',mx,'cpu',a['cpu_seconds'],'receipt cpu',b['cpu_seconds'])
    print(fam,'fits mine',json.dumps(a['fits'])[:300])
    print(fam,'fits rcpt',json.dumps(b['fits'])[:300])
