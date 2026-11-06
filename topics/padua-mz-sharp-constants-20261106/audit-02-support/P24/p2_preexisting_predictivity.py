"""Shows P2 item-3 secant outcome was computable from S4-padua-essential.json (committed 5110954, before P2 protocol d03e74d)."""
import json,math,sys
d=json.load(open(sys.argv[1])); q={r['m']:r['minimum']['value'] for r in d['rows']}
b2=-0.0955298083997758; out={}
for lo,hi in [(1400,3000),(1800,3000),(1401,3001),(1801,3001)]:
    s=(q[hi]-q[lo])/math.log(hi/lo); out[f'{lo}-{hi}']=dict(secant=s,diff_from_b2=abs(s-b2))
for a,b,m in [(1400,1800,1600),(1401,1801,1601)]:
    t=(math.log(m)-math.log(a))/(math.log(b)-math.log(a)); out[f'interp_Qmin_{m}']=q[a]+t*(q[b]-q[a])
out['preexisting_Qmin_3000_3001']=[q[3000],q[3001]]
json.dump(out,open(sys.argv[2],'w'),indent=1); print(json.dumps(out,indent=1))
