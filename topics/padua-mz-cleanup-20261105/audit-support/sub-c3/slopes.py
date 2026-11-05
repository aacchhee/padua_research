import json
from math import log
d = json.load(open('/tmp/claude-0/subC3/quot.json'))
AJm, AJp = 3.75098821137025988438, 2.17372444063582269455
for par in [0,1]:
    ms = [m for m in sorted(map(int,d)) if m%2==par]
    for i in range(4):
        a,b,sg = d[str(ms[0])][i][:3]
        lim = sg*(16 if sg<0 else 8)*a*b/9
        s = []
        for m1,m2 in zip(ms,ms[1:]):
            Q1,Q2 = d[str(m1)][i][3], d[str(m2)][i][3]
            R1,R2 = Q1/d[str(m1)][i][4], Q2/d[str(m2)][i][4]
            s.append('%d-%d: dQ/dlog=%.4f dR/dlog=%.4f' % (m1,m2,(Q2-Q1)/log(m2/m1),(R2-R1)/log(m2/m1)))
        print('parity',par,'a=%.3f b=%.2f'%(a,b),'energy lim %.4f, quotient lim %.5f'%(lim, lim/(AJm if sg<0 else AJp)))
        print('   ', '; '.join(s))
