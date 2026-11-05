"""Typed proof/provenance identity controls; no mathematical acceptance."""
import argparse
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--helper',required=True)
    ap.add_argument('--input',required=True);ap.add_argument('--output',required=True)
    args=ap.parse_args();path=Path(args.helper).resolve()
    spec=importlib.util.spec_from_file_location('payload_helper',path)
    helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)
    before=helper.sha(path.read_bytes());identity,original=helper.identify(args.input)
    import gzip
    raw=Path(args.input).read_bytes();data=json.loads(gzip.decompress(raw))
    proof,removed=helper.proof_payload(data)
    assert helper.canonical(proof)==original
    controls=[]
    for key in data:
        if key=='metadata':continue
        changed=copy.deepcopy(data);changed[key]={'deliberately_changed':True}
        assert helper.canonical(helper.proof_payload(changed)[0])!=original
        controls.append('top_level_retained:'+key)
    for section in ('summary','boundary_summary'):
        if section not in data:continue
        for key in data[section]:
            changed=copy.deepcopy(data);changed[section][key]={'deliberately_changed':True}
            same=helper.canonical(helper.proof_payload(changed)[0])==original
            expected=(section,key)in(('summary','seconds'),('summary','Pcache'),('boundary_summary','seconds'))
            assert same==expected,(section,key)
            controls.append(('excluded:'if expected else'retained:')+section+'.'+key)
    changed=copy.deepcopy(data);changed['metadata']={'changed_provenance':True}
    p,r=helper.proof_payload(changed)
    assert helper.canonical(p)==original and helper.sha(helper.canonical(r))!=identity['excluded_fields_sha256']
    assert helper.canonical({'n':8})!=helper.canonical({'n':8.0})
    assert helper.canonical({'id':False})!=helper.canonical({'id':0})
    with tempfile.TemporaryDirectory(prefix='t1-independent-payload-')as directory:
        duplicate=Path(directory)/'duplicate.json';duplicate.write_text('{"n":8,"n":8}')
        try:helper.identify(duplicate)
        except ValueError:pass
        else:raise AssertionError('duplicate key accepted')
    assert helper.sha(path.read_bytes())==before
    result={'all_controls_passed':True,'count_certified':False,
            'scope':'typed full payload identity and separate excluded provenance only',
            'source_sha256':before,'source_sha256_after':helper.sha(path.read_bytes()),
            'control_sha256':helper.sha(Path(__file__).read_bytes()),'input':identity,
            'metadata_separately_bound':True,'integer_float_boolean_distinguished':True,
            'duplicate_json_rejected':True,'controls':controls}
    Path(args.output).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,sort_keys=True))
if __name__=='__main__':main()
