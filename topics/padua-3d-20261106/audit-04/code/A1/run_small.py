import json,sys,collections,time,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import aud_rank as R
fn,n,outfn=sys.argv[1],int(sys.argv[2]),sys.argv[3]
small=[json.loads(l) for l in open(fn) if '"small"' in l]
small=[r for r in small if r['type']=='small']
hist=collections.Counter(); recs=[]; t0=time.time()
for r in small:
    rec,X=R.certify(r['hnf'],n)
    assert rec['fold']==r['fold'] and rec['admissible'], (r,rec)
    hist[(rec['fold'],rec['rank_exact'])]+=1; recs.append(rec)
print('n',n,'cases',len(small),'hist',sorted(hist.items(), key=lambda t:(t[0][0], -1 if t[0][1] is None else t[0][1])),'unresolved',sum(1 for x in recs if x['rank_exact'] is None),'fullrank',sum(1 for x in recs if x['rank_exact']==x['N']),'sec',round(time.time()-t0,1))
json.dump(recs,open(outfn,'w'))
