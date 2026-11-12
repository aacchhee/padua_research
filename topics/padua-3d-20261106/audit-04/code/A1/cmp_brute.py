import json,sys,subprocess
n,qmax,cap=map(int,sys.argv[1:4]); S=sys.argv[4]
b=subprocess.run([S+'/mine/aud_brute',str(n),str(qmax),str(cap)],capture_output=True,text=True,check=True).stdout.split('\n')
bq={};bs=set()
for l in b:
    t=l.split()
    if not t: continue
    if t[0]=='Q': bq[int(t[1])]=tuple(map(int,t[2:5]))
    else: bs.add(tuple(map(int,t[1:])))
out=S+f'/out/mine-brutecmp-n{n}.jsonl'
subprocess.run([S+'/mine/aud_enum','fold',str(n),'1',str(qmax),str(cap),out],check=True)
mq={};ms=set()
for l in open(out):
    r=json.loads(l)
    if r['type']=='q': mq[r['q']]=(r['hnf_total'],r['admissible'],r['small'])
    elif r['type']=='small': ms.add((r['q'],r['fold'],*r['hnf']))
print('n',n,'qmax',qmax,'per-q equal',bq==mq,'small sets equal',bs==ms,'#small',len(ms),'adm total',sum(v[1] for v in mq.values()),'hnf total',sum(v[0] for v in mq.values()))
