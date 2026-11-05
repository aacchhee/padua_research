import json,sys,mpmath
from fractions import Fraction as F
sys.set_int_max_str_digits(0)
mpmath.mp.prec=400
S=sys.argv[1]; o=json.load(open(sys.argv[2]))
rows={(r[0],r[1]):r[2:] for r in o['rows']}
bad=0;n=0
for rule in ['bj','mirror','alt','pivot']:
    d=json.load(open(f'{S}/L7G1/g1/out/full-{rule}/endpoints.json'))
    runs=d['runs'] if isinstance(d,dict) else d
    for r in runs:
        s=r['degree']; L=F(r['Knode_squared']['exact']); H=F(r['KHS_squared']['exact']); R=F(r['Urow_squared']['exact']); U=F(r['upper_squared']['exact'])
        assert U==min(H,R)
        for v,(lo,hi) in ((L,rows[s,rule][0:2]),(U,rows[s,rule][2:4])):
            z=(mpmath.log(mpmath.mpf(v.numerator))-mpmath.log(mpmath.mpf(v.denominator)))/2*mpmath.mpf(10)**15
            n+=1
            # exact value must lie in [lo,hi], and floor/ceil tightness
            if not (lo< z < hi or (lo==z) or z==hi): bad+=1;print('enclosure fail',rule,s,lo,hi,z)
            if not (int(mpmath.floor(z))==lo and int(mpmath.ceil(z))==hi): print('not tight',rule,s,lo,hi,z)
print('checked',n,'bad',bad)
