import json,sys,math,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import aud_rank as R
out=[]
def cyc(z,q):
    inv=pow(z[2],-1,q); return (1,0,(-z[0]*inv)%q,1,(-z[1]*inv)%q,q)
W=[(1,(1,1,1,2,0,2)),(3,(1,3,3,6,0,10)),(4,(4,0,5,5,5,10)),(5,(5,0,6,6,6,12)),(4,(4,0,4,4,4,8)),(5,(5,0,5,5,5,10))]
for z in [(1,3,7),(1,4,6),(1,5,8),(1,7,8)]: W.append((2,cyc(z,19)))
for n,h in W:
    rec,X=R.certify(h,n);
    if n==2:
        rec['weights']=sorted(X.values())
    print(json.dumps(rec)); out.append(rec)
json.dump(out,open('./out/aud-witnesses.json','w'))
