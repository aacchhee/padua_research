"""C/GMP exact producer, emitting the unchanged reference v1 certificate schema."""
import argparse
import gzip
import json
from pathlib import Path
import hashlib
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
REFERENCE = REPO / 'topics/padua-argmax-alln-20261101/code/part3'
sys.path.insert(0, str(REFERENCE))
import finite_general as g
import finite_bernstein as b
import finite_general_run as reference_run


def run(n, output, work, seconds=600, boxes=200000, depth=48):
    assert 2 <= n <= 100 and seconds > 0 and boxes > 0 and 0 < depth <= 100
    started = time.monotonic()
    work.mkdir(parents=True, exist_ok=True)
    binary = work / 'native-producer'
    source_bytes = (HERE/'producer.c').read_bytes()
    source_hash = hashlib.sha256(source_bytes).hexdigest()
    driver_hash = b.digest(HERE/'run.py')
    snapshot = work / 'producer-build.c'
    snapshot.write_bytes(source_bytes)
    subprocess.run(['gcc', '-O3', '-Wall', '-Wextra', '-Werror', str(snapshot), '-lgmp', '-o', str(binary)], check=True)
    binary_hash = b.digest(binary)
    xv, xs = g.cosine_axis(n)
    yv, ys = g.cosine_axis(n+1)
    cp = g.chebyshev_polynomials(n)
    inputs = [str(n)]
    inputs.extend(f'{a} {z}' for a, z in xv+yv)
    inputs.extend(str(cp[i].get(k, 0)) for i in range(n+1) for k in range(n+1))
    inputs.extend(str(b.monomial_to_bernstein(n, i, k)) for i in range(n+1) for k in range(n+1))
    input_file = work / f'n{n}-input.txt'
    input_file.write_text('\n'.join(inputs)+'\n')
    proc = subprocess.run([str(binary), str(seconds), str(boxes), str(depth), str(input_file)], check=True, text=True, capture_output=True)
    (work/f'n{n}-native.txt').write_text(proc.stdout)
    leaves, pending = [], []
    corners = [[-1,-1], [1,-1] if n%2==0 else [-1,1]]
    for line in proc.stdout.splitlines():
        fields = line.split()
        if fields[0] == 'THRESHOLD':
            threshold = list(map(int, fields[1:]))
        elif fields[0] == 'SETUP_SECONDS':
            setup = float(fields[1])
        elif fields[0] in ('BOUND', 'CORNER', 'PENDING'):
            path = '' if fields[1] == '-' else fields[1]
            if fields[0]=='BOUND':
                leaves.append(dict(path=path, kind='bound', upper=int(fields[2])))
            elif fields[0]=='CORNER':
                leaves.append(dict(path=path,kind='corner',corner=corners[int(fields[2])],upper_away_from_vertex=int(fields[3])))
            else:
                pending.append(path)
        elif fields[0] == 'STATS':
            visited, splits, bound, corner, maximum_depth, limited = map(int, fields[1:7])
            search = float(fields[7])
    assert g.S < threshold[0] <= threshold[1], 'precision insufficient for corner threshold'
    pi, counts = g.pi_bounds()
    data = dict(format='padua-part3-general-certificate-v1', source_head=b.PINNED_HEAD,
                source_sha256=reference_run.sources(), setup_seconds=setup, search_seconds=search,
                total_seconds=time.monotonic()-started, limits=dict(seconds=seconds,boxes=boxes,depth=depth),
                statistics=dict(visited=visited,splits=splits,bound=bound,corner=corner,maximum_depth=maximum_depth),
                leaves=leaves,pending=pending,depth_limited=bool(limited and maximum_depth>=depth),
                complete=not pending,accepted=False,n=n,precision=g.PRECISION,scale=g.S,
                threshold_interval=threshold,corners=corners,
                cardinal_constructor='PD-T101 corrected kernel; rigorous rational cosine intervals',
                cardinals=(n+1)*(n+2)//2,pi_interval=list(map(str,pi)),machin_terms=list(counts),
                dependency_sha256=b.digest(g.DEPENDENCY),x_cosine_seed=list(xs),y_cosine_seed=list(ys),
                producer_provenance=dict(kind='C/GMP native exact hot path',source_sha256=source_hash,
                                        driver_sha256=driver_hash,binary_sha256=binary_hash,
                                        input_sha256=b.digest(input_file),reference_sources_are_schema_dependencies=True))
    payload = (json.dumps(data,sort_keys=True,separators=(',',':'))+'\n').encode()
    if output.suffix=='.gz': payload=gzip.compress(payload,mtime=0)
    output.write_bytes(payload)
    return dict(n=n,complete=data['complete'],leaves=len(leaves),setup_seconds=setup,search_seconds=search,
                total_seconds=data['total_seconds'],certificate_sha256=b.digest(output),bytes=len(payload))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--n',type=int,required=True)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--work',type=Path,default=Path('/workspace/padua-work/producer'))
    parser.add_argument('--seconds',type=float,default=600)
    parser.add_argument('--boxes',type=int,default=200000)
    parser.add_argument('--depth',type=int,default=48)
    a=parser.parse_args()
    print(json.dumps(run(a.n,a.output,a.work,a.seconds,a.boxes,a.depth),sort_keys=True))
