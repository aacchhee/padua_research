import sys,json,struct,importlib.util
from pathlib import Path
ROOT=Path('/workspace/padua_research')
spec=importlib.util.spec_from_file_location('b',ROOT/'topics/nn-mop-iep-20261103/code/c4_float_baseline.py');b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)
hx=lambda v:''.join(struct.pack('>d',float(x)).hex() for x in v)
out=[]
for f in ('krawtchouk','hahn'):
    for N in range(4,33):
        x,w=b.inputs(N,f)
        out.append(dict(N=N,family=f,input_kind='shared_normalized',nodes_bits=hx(x),weights1_bits=hx(w[0]),weights2_bits=hx(w[1]),exact=[],algorithms={}))
Path(sys.argv[1]).write_text(json.dumps(out))
