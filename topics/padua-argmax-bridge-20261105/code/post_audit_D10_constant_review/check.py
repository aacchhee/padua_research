"""Preregistered D10 exact rational controls; no author imports."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import resource
import time

resource.setrlimit(resource.RLIMIT_CPU, (1, 2))
start = time.process_time()


def add(p, q):
    out = [F(0)]*max(len(p), len(q))
    for i, x in enumerate(p): out[i] += x
    for i, x in enumerate(q): out[i] += x
    return out


def mul(p, q):
    out = [F(0)]*(len(p)+len(q)-1)
    for i, x in enumerate(p):
        for j, y in enumerate(q): out[i+j] += x*y
    return out


def val(p, x):
    return sum((a*x**i for i, a in enumerate(p)), F(0))


p, y = [F(0), F(0), F(40, 9)], F(1, 3)
derivatives = []
for j in range(5):
    derivatives.append(val(p, y)/(1-y*y)**(j+1)/3**j)
    dp = [i*a for i, a in enumerate(p)][1:]
    p = add(mul(dp, [F(1), F(0), F(-1)]),
            mul(p, [F(0), F(2*(j+1))]))
assert derivatives == [F(5,9), F(5,4), F(15,8), F(75,32), F(165,32)]
fourth = (derivatives[4]+2*derivatives[3]+F(3,2)*derivatives[2]
          +derivatives[1]/2+(2+derivatives[0])/16)/3
assert fourth == F(3871,864)
controls = {
    'fourth_derivative':F(9,2)-fourth,
    'H_increment':F(1,3)-F(7050,29791)-F(5805,63488),
    'weighted_square':F(49,100)**2-F(23,125)**2-F(9,20)**2,
    'global_8over3':F(8,3)-F(320,197)-F(66,125)-F(49,100),
    'c_minus_one_third':F(1,2)-F(4,9)*(F(6,5)**2-F(69,100)**2),
    'near_linear':F(4,3)-F(1501,1152),
    'far_constant':F(8,15)-(F(320,197)+F(89,125)-F(4383,2420)),
    'far_phase_floor':F(191,6144)-F(31,1000),
    'far_square_floor':F(31,1000)-F(7,40)**2,
    'far_22':F(22)-(F(8000,465)+F(36,7)-F(46,125)),
}
assert all(v>0 for v in controls.values())
assert F(15,32)*F(3,4)+F(113,72)/2+F(4,9)*F(3,8)==F(1501,1152)
assert F(2,3)+F(1,8)==F(19,24)
assert F(19,24)+F(7,9)==F(113,72)
result = {'status':'PASS_EXACT_FRACTION_CONTROLS',
          'majorant_derivatives':[str(v) for v in derivatives],
          'positive_slacks':{k:str(v) for k,v in controls.items()},
          'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'cpu_seconds':time.process_time()-start}
dest = Path(__file__).resolve().parents[2]/'evidence/post_audit_D10_constant_review/scalars.json'
dest.parent.mkdir(parents=True,exist_ok=True)
assert not dest.exists()
dest.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
print(json.dumps({'status':result['status'], 'cpu_seconds':result['cpu_seconds'],
                  'bytes':dest.stat().st_size,
                  'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()}))
