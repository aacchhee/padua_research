#!/usr/bin/env python3
"""Check v2/v3 evidence identities or atomically compact one index to v3.

No scientific checker is imported or executed. Hashes retain all32 bytes.
"""
import argparse
import base64
import binascii
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import tempfile

V2='bridge-essential-evidence-index-v2'
V3='bridge-essential-evidence-index-v3'
PREFIXES=['','evidence/','code/']
V2_COLUMNS=['path','bytes','sha256']
V3_COLUMNS=['prefix_index','suffix','bytes','sha256_base64']
LIMIT=16384
DEFAULT_ROOT=Path(__file__).resolve().parent.parent

def require(ok,message):
    if not ok:raise ValueError(message)

def strict_object(pairs):
    result={}
    for key,value in pairs:
        require(key not in result,'duplicate JSON key: '+key)
        result[key]=value
    return result

def load(raw):
    def nonfinite(value):raise ValueError('nonfinite JSON constant: '+value)
    document=json.loads(raw,object_pairs_hook=strict_object,parse_constant=nonfinite)
    require(isinstance(document,dict),'index must be an object')
    return document

def relative_path(value):
    require(isinstance(value,str) and bool(value),'empty/nonstring evidence path')
    require('\\' not in value and '\x00' not in value,'invalid path character')
    p=PurePosixPath(value)
    require(not p.is_absolute() and all(x not in ('','.','..') for x in value.split('/')),'outside/noncanonical evidence path')
    require(str(p)==value,'noncanonical evidence path')
    return value

def normalize(document):
    """Return canonical sorted[path,bytes,sha256_hex] rows for either schema."""
    schema=document.get('schema');require(schema in (V2,V3),'unknown evidence-index schema')
    require(isinstance(document.get('files'),list),'files must be a list')
    if schema==V2:
        require(document.get('columns',V2_COLUMNS)==V2_COLUMNS,'unexpected v2 columns')
        require('path_prefixes' not in document,'v2 reserved path_prefixes field')
    else:
        require(document.get('columns')==V3_COLUMNS,'unexpected/missing v3 columns')
        require(document.get('path_prefixes')==PREFIXES,'unexpected v3 path prefixes')
    rows=[];seen=set()
    for entry in document['files']:
        require(isinstance(entry,list) and len(entry)==(3 if schema==V2 else 4),'malformed evidence row')
        if schema==V2:path,n,digest=entry
        else:
            prefix,suffix,n,encoded=entry
            require(type(prefix) is int and 0<=prefix<len(PREFIXES),'invalid prefix index')
            require(isinstance(suffix,str) and bool(suffix),'invalid suffix')
            require(isinstance(encoded,str),'invalid base64 digest type')
            try:decoded=base64.b64decode(encoded,validate=True)
            except (ValueError,binascii.Error) as exc:raise ValueError('invalid standard base64 digest') from exc
            require(len(decoded)==32 and base64.b64encode(decoded).decode('ascii')==encoded,'noncanonical/incomplete base64 digest')
            path=PREFIXES[prefix]+suffix;digest=decoded.hex()
        path=relative_path(path)
        require(path not in seen,'duplicate evidence path: '+path);seen.add(path)
        require(type(n) is int and 0<=n<LIMIT,'invalid/oversize evidence byte count: '+path)
        require(isinstance(digest,str) and re.fullmatch('[0-9a-f]{64}',digest) is not None,'invalid SHA256 hex: '+path)
        rows.append([path,n,digest])
    rows.sort(key=lambda row:row[0])
    total=document.get('total_bytes')
    require(type(total) is int and total==sum(row[1] for row in rows),'total_bytes mismatch')
    return rows

def verify_files(rows,root,index):
    root=root.resolve();index=index.resolve()
    for path,n,digest in rows:
        target=(root/path).resolve()
        require(target.is_relative_to(root) and target!=index,'outside/self evidence path: '+path)
        require(target.is_file(),'missing/nonfile evidence: '+path)
        raw=target.read_bytes()
        require(len(raw)<LIMIT and len(raw)==n,'evidence byte mismatch: '+path)
        require(hashlib.sha256(raw).hexdigest()==digest,'evidence SHA256 mismatch: '+path)

def compact(document):
    """Pure lossless conversion; preserves every nonencoding metadata field."""
    before=normalize(document);result=dict(document);encoded=[]
    for path,n,digest in before:
        prefix=max((i for i,p in enumerate(PREFIXES) if path.startswith(p)),key=lambda i:len(PREFIXES[i]))
        encoded.append([prefix,path[len(PREFIXES[prefix]):],n,base64.b64encode(bytes.fromhex(digest)).decode('ascii')])
    result.update(schema=V3,columns=V3_COLUMNS,path_prefixes=list(PREFIXES),files=encoded)
    require(normalize(result)==before,'v3 roundtrip changed normalized rows')
    ignored={'schema','columns','path_prefixes','files'}
    require({k:v for k,v in result.items() if k not in ignored}=={k:v for k,v in document.items() if k not in ignored},'metadata changed')
    require(result['total_bytes']==document['total_bytes'],'total changed')
    return result

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    actions=parser.add_mutually_exclusive_group(required=True)
    actions.add_argument('--check',action='store_true');actions.add_argument('--compact',action='store_true')
    parser.add_argument('--root',type=Path,default=DEFAULT_ROOT,help='evidence path base; default: this topic root')
    parser.add_argument('index',nargs='?',type=Path,help='index path; default: ROOT/evidence-manifest.json')
    args=parser.parse_args();root=args.root.resolve();index=(args.index or root/'evidence-manifest.json').resolve()
    require(index.is_relative_to(root) and index.is_file(),'outside/missing index path')
    original=index.read_bytes();document=load(original);rows=normalize(document);verify_files(rows,root,index)
    if args.check:
        require(len(original)<LIMIT,'index reaches/exceeds16KiB')
        print(json.dumps({'status':'PASS','schema':document['schema'],'entries':len(rows),'index_bytes':len(original),'total_bytes':document['total_bytes']}))
        return
    converted=compact(document)
    candidate=(json.dumps(converted,separators=(',',':'),ensure_ascii=False,allow_nan=False)+'\n').encode('utf-8')
    require(normalize(load(candidate))==rows,'serialized roundtrip changed rows')
    require(len(candidate)<LIMIT,'compact index reaches/exceeds16KiB')
    require(len(candidate)<len(original),'refuse compaction without size improvement')
    require(index.read_bytes()==original,'index changed during validation')
    temporary=None
    try:
        with tempfile.NamedTemporaryFile(dir=index.parent,prefix=index.name+'.tmp-',delete=False) as handle:
            temporary=Path(handle.name);os.fchmod(handle.fileno(),stat.S_IMODE(index.stat().st_mode))
            handle.write(candidate);handle.flush();os.fsync(handle.fileno())
        require(index.read_bytes()==original,'index changed before atomic replacement')
        temporary.replace(index);temporary=None
    finally:
        if temporary is not None:temporary.unlink(missing_ok=True)
    print(json.dumps({'status':'COMPACTED','schema':V3,'entries':len(rows),'old_bytes':len(original),'new_bytes':len(candidate),'total_bytes':converted['total_bytes']}))

if __name__=='__main__':
    try:main()
    except (ValueError,OSError) as exc:raise SystemExit(str(exc))
