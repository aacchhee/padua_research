import re,sys,collections
import numpy as np
# usage: f6_slopes.py log [log ...]; parses 'Padua n=.. N=M=.. order methods' lines
rows=[]
for log in sys.argv[1:]:
    for line in open(log):
        m=re.match(r"(Padua n=(\d+) N=M=(\d+)( randW)?|random M=(\d+) n=(\d+) N=(\d+)) (\S+)\s+(.*)$",line.strip())
        if not m: continue
        key=m[1]; order=m[8]; vals={}
        for t in m[9].split("  "):
            mm=re.match(r"([\w-]+):H([\d.e+-]+)/Q([\d.e+-]+)",t.strip())
            if mm: vals[mm[1]]=(float(mm[2]),float(mm[3]))
        rows.append((log.split('/')[-1],key,order,vals))
for r in rows: print(r[0][:22],r[1],r[2],{k:v[0] for k,v in r[3].items()})
# slopes on Padua uniform (no randW)
for sel in ("given","mean-all-orders"):
    data=collections.defaultdict(dict)
    for log,key,order,vals in rows:
        m=re.match(r"Padua n=(\d+) N=M=(\d+)$",key)
        if not m or log.startswith("f6_run_padua_large_20_30") and False: continue
        M=int(m[2])
        for meth,(eH,eQ) in vals.items():
            if sel=="given" and order!="given": continue
            data[meth].setdefault(M,[]).append(eH)
    print("slope selection:",sel)
    for meth,d in data.items():
        Ms=sorted(d); 
        if len(Ms)<2: continue
        e=[np.exp(np.mean(np.log(d[M]))) for M in Ms]
        sl=np.polyfit(np.log(Ms),np.log(e),1)[0]
        sl2=np.log(e[-1]/e[-2])/np.log(Ms[-1]/Ms[-2]) if len(Ms)>2 else float('nan')
        print(f"  {meth:15s} M={Ms} err={[f'{x:.1e}' for x in e]} slope(all pts)={sl:.2f} slope(last two)={sl2:.2f}")
