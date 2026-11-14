#!/usr/bin/env python3
"""Remove untrusted diagnostic leaf numbers; perform no numeric computation.

The exact resulting plain bytes, not merely the original, require independent
whole-leaf replay. Root/path/kind and every non-leaf field are preserved.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
from n3_native_receipt import identity

def unique_object(pairs):
    result={}
    for key,value in pairs:
        if key in result:raise ValueError('duplicate JSON key')
        result[key]=value
    return result

def reject_constant(value):
    raise ValueError('nonfinite JSON constant: '+value)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('candidate',type=Path);ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();source=args.candidate.resolve();target=args.output.resolve()
    if target.exists() or target.with_suffix(target.suffix+'.gz').exists():raise RuntimeError('Refusing to overwrite candidate')
    raw=source.read_bytes()
    data=json.loads(raw,object_pairs_hook=unique_object,parse_constant=reject_constant)
    assert data['format']=='n3-phase-candidate-v1' and data['complete'] is True
    assert data['accepted'] is False and data['pending']==[]
    omitted={'S_upper','corner_upper','defect_lower'}
    original_leaves=data['leaves']
    compact_leaves=[{key:value for key,value in leaf.items() if key not in omitted} for leaf in original_leaves]
    assert all(set(leaf)=={'root','path','kind'} for leaf in compact_leaves)
    data['leaves']=compact_leaves
    source_identity={'path':identity(source)['path'],'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
    data['projection']={'operation':'omit diagnostic numeric leaf fields only','omitted_fields':sorted(omitted),
                        'original_candidate':source_identity,'projection_source':identity(Path(__file__).resolve()),
                        'leaf_count':len(compact_leaves),'arithmetic_executed':False}
    payload=(json.dumps(data,separators=(',',':'))+'\n').encode()
    compressed=gzip.compress(payload,mtime=0)
    target.write_bytes(payload);gz=target.with_suffix(target.suffix+'.gz');gz.write_bytes(compressed)
    target.chmod(0o444);gz.chmod(0o444)
    print(json.dumps({'original_candidate':source_identity,'compact_candidate':identity(target),
                      'compressed_compact':identity(gz),'compression_decompressed_sha256':hashlib.sha256(gzip.decompress(compressed)).hexdigest(),
                      'complete':True,'accepted':False,'leaves':len(compact_leaves)}))

if __name__=='__main__':main()
