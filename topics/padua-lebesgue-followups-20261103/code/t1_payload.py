"""Canonical identity of every frozen-checker proof input, minus diagnostics.

Only top-level metadata (unused by frozen Verifier.run), summary.seconds,
summary.Pcache and boundary_summary.seconds are removed. No polynomial, interval,
root, leaf, node, partition, boundary or checker-validated count is omitted.
Raw/source identities and omitted provenance remain separately bound in receipts.
"""
if not __debug__:
    raise RuntimeError('optimized Python disables T1 integrity guards')
import argparse,copy,gzip,hashlib,json,lzma
from pathlib import Path

def sha(raw):return hashlib.sha256(raw).hexdigest()

def unique(pairs):
    out={}
    for key,value in pairs:
        if key in out:raise ValueError('duplicate JSON key: '+key)
        out[key]=value
    return out

def canonical(data):return json.dumps(data,sort_keys=True,separators=(',',':'),allow_nan=False).encode()

def proof_payload(data):
    data=copy.deepcopy(data);removed={}
    if 'metadata'in data:removed['metadata']=data.pop('metadata')
    for section,key in(('summary','seconds'),('summary','Pcache'),('boundary_summary','seconds')):
        if section in data and key in data[section]:removed[section+'.'+key]=data[section].pop(key)
    return data,removed

def identify(path):
    raw=Path(path).read_bytes();payload=gzip.decompress(raw)if raw[:2]==b'\x1f\x8b'else lzma.decompress(raw)if raw[:6]==b'\xfd7zXZ\x00'else raw
    data=json.loads(payload,object_pairs_hook=unique);proof,removed=proof_payload(data);proof=canonical(proof)
    assert sha(Path(path).read_bytes())==sha(raw),'input changed'
    return dict(path=str(path),raw_sha256=sha(raw),raw_bytes=len(raw),mathematical_payload_sha256=sha(proof),mathematical_payload_bytes=len(proof),excluded_fields=sorted(removed),excluded_fields_sha256=sha(canonical(removed))),proof

def main():
    ap=argparse.ArgumentParser();ap.add_argument('input');ap.add_argument('--compare');ap.add_argument('--output',required=True);a=ap.parse_args()
    own=sha(Path(__file__).read_bytes());first,proof=identify(a.input);result=dict(primary=first,source_sha256=own,count_certified=False,scope='exact complete proof-input identity only; full mathematical replay still required')
    if a.compare:
        second,other=identify(a.compare);result.update(comparison=second,mathematical_payload_identical=proof==other)
    assert own==sha(Path(__file__).read_bytes())
    output=Path(a.output)
    assert all(output.resolve()!=Path(p).resolve()for p in(a.input,a.compare)if p),'receipt must not overwrite input'
    value=json.dumps(result,indent=2,sort_keys=True)+'\n'
    if output.exists():assert output.read_text()==value,'refusing to overwrite differing receipt'
    else:output.write_text(value)
    print(json.dumps(result,sort_keys=True),flush=True)
if __name__=='__main__':main()
