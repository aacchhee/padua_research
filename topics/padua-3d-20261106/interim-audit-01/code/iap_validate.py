#!/usr/bin/env python3
"""Validate interim audit artifact identities and n7 scientific digest."""
import argparse
import hashlib
import json
from pathlib import Path
import platform
import sys

ROOT=Path(__file__).resolve().parents[1]
TOPIC=ROOT.parent

def identity(path):
    data=Path(path).read_bytes()
    return {'path':str(path),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}

def records(value):
    if isinstance(value,dict):
        if {'path','bytes','sha256'}<=value.keys():yield value
        for nested in value.values():yield from records(nested)
    elif isinstance(value,list):
        for nested in value:yield from records(nested)

def main():
    p=argparse.ArgumentParser();p.add_argument('--receipt',type=Path,required=True);a=p.parse_args()
    sources=['iap-lattice-enumeration.json','iap-lattice-alternate.json','iap-t8.json','iap-boundaries.json']
    checked=0;inputs=[]
    for name in sources:
        path=ROOT/'evidence'/name
        assert path.stat().st_size<16384
        payload=json.loads(path.read_text());inputs.append(identity(path))
        for item in records(payload):
            actual=identity(item['path'])
            assert all(actual[key]==item[key] for key in ('bytes','sha256')),item['path']
            checked+=1
    data=json.loads((ROOT/'evidence/iap-lattice-enumeration.json').read_text())
    first=[]
    for entry in data['rows']:
        rows=[json.loads(line) for line in Path(entry['raw']['path']).read_text().splitlines()]
        firstq=next(r for r in rows if r['type']=='q' and r['admissible'])
        first.append({'n':entry['n'],'first_admissible_q':firstq['q'],'minimizers':firstq['admissible']})
        if entry['n']==7:
            keys=['q','hnf_total','after_axis_pair_prune','admissible','small']
            scientific=[{k:r[k] for k in keys} for r in rows if r['type']=='q']
    digest=hashlib.sha256(json.dumps(scientific,separators=(',',':')).encode()).hexdigest()
    reference=TOPIC/'evidence/r08-lattice-n7finish.json'
    assert digest==json.loads(reference.read_text())['scientific_per_q_sha256']
    out={'audit_pin':'5440555cf326afdbd66b75bed195802013901c2d','command':sys.argv,
         'python':platform.python_version(),'code':identity(__file__),'inputs':inputs,
         'identity_records_verified':checked,'first_admissible_determinants':first,
         'n7_reference':identity(reference),'n7_scientific_per_q_sha256':digest,
         'n7_all_960_scientific_rows_match':True}
    encoded=json.dumps(out,separators=(',',':'))+'\n';assert len(encoded.encode())<16384
    a.receipt.write_text(encoded);print(json.dumps(identity(a.receipt)))

if __name__=='__main__':main()
