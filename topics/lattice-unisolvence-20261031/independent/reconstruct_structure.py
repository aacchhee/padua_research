#!/usr/bin/env python3
"""Independent branch-cover and symbolic mixed-dependence reconstruction."""
from functools import lru_cache
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
import sys
import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "topics/lattice-unisolvence-20261031"


def cover_exists(points, budget):
    edges = tuple(tuple((axis,index) for axis,index in enumerate(point)) for point in points)
    @lru_cache(None)
    def search(remaining, allowance):
        if not remaining:
            return True
        if allowance == 0:
            return False
        for vertex in edges[remaining[0]]:
            left = tuple(j for j in remaining if vertex not in edges[j])
            if search(left,allowance-1):
                return True
        return False
    return search(tuple(range(len(edges))),budget)


def main():
    ranks_path = TOPIC / "directions/C3/ranks.json"
    structure_path = TOPIC / "directions/C3/structure.json"
    ranks = json.loads(ranks_path.read_text())
    structure = json.loads(structure_path.read_text())
    reps = {r['id']:r for r in ranks['representatives']}
    found = 0
    for cert in structure['covers']:
        r = reps[cert['id']]
        exists = cover_exists(r['points'],r['n'])
        assert exists == (cert['layers'] is not None),cert['id']
        if exists:
            found += 1
            assert sum(map(len,cert['layers'])) == cert['degree'] <= r['n']
            assert all(any(i in chosen for i,chosen in zip(point,cert['layers'])) for point in r['points'])
    int_nonzero = 0
    for cert in structure['integer_witnesses']:
        r = reps[cert['id']]
        n = r['n']
        exps = [(a,b,d-a-b) for d in range(n+1) for a in range(d+1) for b in range(d-a+1)]
        matrix = sp.Matrix([[sp.prod(cert['axes'][j][index[j]]**exp[j] for j in range(3)) for exp in exps] for index in r['points']])
        determinant = int(matrix.det(method='domain-ge'))
        assert determinant == int(cert['determinant']),cert['id']
        int_nonzero += determinant != 0
    mixed_certificates = []
    for cert in structure['symbolic_n1']:
        axes = [[sp.Integer(0),sp.Integer(1)]+[sp.Symbol(f'{name}{j}') for j in range(2,L)] for name,L in zip('xyz',cert['lengths'])]
        matrix = sp.Matrix([[1,axes[2][k],axes[1][j],axes[0][i]] for i,j,k in cert['points']])
        determinant = sp.expand(matrix.det(method='domain-ge'))
        assert sp.expand(determinant-sp.sympify(cert['determinant'])) == 0
        multiplied = sp.sympify(cert['constant'])*sp.prod(sp.sympify(f['factor'])**f['multiplicity'] for f in cert['factors'])
        assert sp.expand(multiplied-determinant) == 0
        pair = None
        for x,y in combinations(sorted(determinant.free_symbols,key=str),2):
            if str(x)[0] == str(y)[0]:
                continue
            obstruction = sp.expand(determinant*sp.diff(determinant,x,y)-sp.diff(determinant,x)*sp.diff(determinant,y))
            if obstruction != 0:
                pair = [str(x),str(y)]
                break
        assert (pair is not None) == cert['has_mixed_factor']
        if pair is not None:
            mixed_certificates.append({'id':cert['id'],'variables':pair})
        else:
            assert all(len({str(s)[0] for s in sp.sympify(f['factor']).free_symbols}) <= 1 for f in cert['factors'])
    out = {
        'all_checks_passed':True,
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
        'input_sha256':{str(p.relative_to(ROOT)):sha256(p.read_bytes()).hexdigest() for p in (ranks_path,structure_path)},
        'cover_decisions_checked':len(structure['covers']), 'covers_found':found,
        'integer_determinants_checked':len(structure['integer_witnesses']), 'integer_nonzero':int_nonzero,
        'symbolic_determinants_checked':len(structure['symbolic_n1']),
        'mixed_dependence_certificates':mixed_certificates,
        'method':'Fresh branch-on-uncovered-point cover decision; SymPy domain determinants; mixed logarithmic derivative test avoiding irreducibility reliance.',
        'sympy':sp.__version__,
    }
    Path(sys.argv[1]).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='mixed_dependence_certificates'},sort_keys=True))


if __name__ == '__main__':
    main()
