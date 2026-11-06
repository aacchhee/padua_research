#!/usr/bin/env python3
"""Authenticate AC's pin, safely extract scratch source, emit frozen inputs.

Never execute third-party source or write extracted source under the repo.
"""
import argparse,hashlib,importlib.util,json,stat,zipfile,struct
from pathlib import Path
from c4_normalization import ROOT

PIN='cdd0e98d2b411f24cfcecb49d83e16f9d50a7622a0d4f0d3eb17eb334a405145'


def require(test,message):
    if not test:raise ValueError(message)


def main():
    p=argparse.ArgumentParser();p.add_argument('--archive',type=Path,required=True)
    p.add_argument('--extract',type=Path,required=True);p.add_argument('--inputs',type=Path,required=True)
    p.add_argument('--receipt',type=Path,required=True);a=p.parse_args()
    require(a.extract.resolve().is_relative_to(Path('/tmp')),'extract third-party source only below /tmp')
    data=a.archive.read_bytes();require(hashlib.sha256(data).hexdigest()==PIN,'archive pin mismatch')
    invpath=ROOT/'topics/nn-mop-stability-20261105/audit-g5-01/source-inventory.json'
    inventory=json.loads(invpath.read_text())
    with zipfile.ZipFile(a.archive) as z:
        require({i.filename for i in z.infolist() if not i.is_dir()}=={r['path'] for r in inventory},'inventory coverage')
        for i in z.infolist():
            member=Path(i.filename)
            require(not member.is_absolute() and '..' not in member.parts and not stat.S_ISLNK(i.external_attr>>16),'unsafe ZIP member')
        for r in inventory:
            payload=z.read(r['path'])
            require(len(payload)==r['bytes'] and hashlib.sha256(payload).hexdigest()==r['sha256'],'member identity '+r['path'])
        z.extractall(a.extract)
    bp=ROOT/'topics/nn-mop-iep-20261103/code/c4_float_baseline.py'
    spec=importlib.util.spec_from_file_location('inputs_base',bp);b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)
    out=[]
    for f in ('krawtchouk','hahn'):
        for N in range(4,33):
            x,w=b.inputs(N,f)
            out.append(dict(N=N,family=f,nodes=list(map(float,x)),weights=[list(map(float,r)) for r in w],nodes_bits=''.join(struct.pack('>d',float(v)).hex() for v in x),weights_bits=[''.join(struct.pack('>d',float(v)).hex() for v in r) for r in w]))
    a.inputs.write_text(json.dumps(out))
    a.receipt.write_text(json.dumps(dict(archive_sha256=PIN,archive_bytes=len(data),member_count=len(inventory),
        inventory_sha256=hashlib.sha256(invpath.read_bytes()).hexdigest(),
        input_sha256=hashlib.sha256(a.inputs.read_bytes()).hexdigest(),input_count=len(out),
        source_revision='unknown; exact AC archive bytes pinned',source_edited=False),indent=2)+'\n')


if __name__=='__main__':main()
