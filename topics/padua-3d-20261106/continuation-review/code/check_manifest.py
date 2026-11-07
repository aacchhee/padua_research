#!/usr/bin/env python3
"""Independently decode v6 byte layout, compare v5 records, mutate copies only."""
import argparse, base64, copy, hashlib, importlib.util, json, subprocess, zlib
from pathlib import Path
TOP=Path(__file__).resolve().parents[2]
ROOT=TOP.parents[1]
BASE='97c323bfae15cf3c76f40802c3ebabedceeb0c60'
def identity(p):
 b=Path(p).read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def decode(payload):
 raw=zlib.decompress(base64.b85decode(payload));assert raw[:5]==b'P3M6\0'
 cursor=5
 def readint():
  nonlocal cursor
  answer=0;scale=1
  while True:
   byte=raw[cursor];cursor+=1;answer+=(byte%128)*scale
   if byte<128:return answer
   scale*=128
 count=readint();rows=[];previous=b''
 for _ in range(count):
  prefix,suffix=readint(),readint();name=previous[:prefix]+raw[cursor:cursor+suffix]
  cursor+=suffix;size=readint();rows.append({'path':name.decode(),'bytes':size});previous=name
 assert len(raw)-cursor==count*32
 for row in rows:row['sha256']=raw[cursor:cursor+32].hex();cursor+=32
 return rows
def unpack(m):
 rows=[]
 for group,d in m.items():
  for k,(size,h) in d.items():
   path=k if group=='other' else group+'/'+k+('.py' if group=='code' else '.json')
   rows.append({'path':path,'bytes':size,'sha256':base64.b85decode(h).hex()})
 return sorted(rows,key=lambda r:r['path'].encode())
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
 path=TOP/'code/artifact_manifest.py';spec=importlib.util.spec_from_file_location('candidate',path)
 m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
 oldraw=subprocess.check_output(['git','show',BASE+':topics/padua-3d-20261106/evidence-manifest.json'],cwd=ROOT)
 old=json.loads(oldraw);oldmap=json.loads(zlib.decompress(base64.b85decode(old['artifacts_payload'])))
 rows=unpack(oldmap);candidate=m.make_manifest(rows,old['inherited_inputs'])
 assert decode(candidate['artifacts_payload'])==rows
 assert m.decode_manifest(candidate)==oldmap
 # Prefix sharing crosses UTF-8 byte boundaries; sizes cross varint boundaries.
 synthetic=[{'path':p,'bytes':size,'sha256':hashlib.sha256(p.encode()).hexdigest()} for p,size in [
 ('code/a.py',0),('code/a/a.py',127),('code/\u00e4.py',128),('code/\u00e5.py',16383),
 ('evidence/x.dat',16384),('evidence/\u6a21\u578b.json',2**40)]]
 s=m.make_manifest(synthetic,[]);assert decode(s['artifacts_payload'])==sorted(synthetic,key=lambda r:r['path'].encode())
 checks=['independent_v5_to_v6_identity_equality','utf8_prefix_and_varint_sizes']
 def reject(name,changed):
  try:m.verify_manifest(changed,rows,old['inherited_inputs'])
  except (ValueError,KeyError,TypeError,UnicodeError,zlib.error):checks.append(name)
  else:raise AssertionError('accepted '+name)
 def binary(name,raw):
  c=copy.deepcopy(candidate);c['artifacts_payload']=base64.b85encode(zlib.compress(raw)).decode();reject(name,c)
 raw=zlib.decompress(base64.b85decode(candidate['artifacts_payload']))
 binary('digest_bit_flip',raw[:-1]+bytes([raw[-1]^1]))
 binary('missing_digest_byte',raw[:-1]);binary('extra_digest_byte',raw+b'\0')
 binary('bad_path_utf8',b'P3M6\0\1\0\1\xff\0'+b'\0'*32)
 binary('noncanonical_count',b'P3M6\0\x81\0'+raw[6:])
 binary('oversized_count',b'P3M6\0'+b'\xff'*10+b'\0')
 binary('cache_path',b'P3M6\0\1\0\x12code/__pycache__/x\0'+b'\0'*32)
 compressed=base64.b85decode(candidate['artifacts_payload'])
 c=copy.deepcopy(candidate);c['artifacts_payload']=base64.b85encode(compressed+zlib.compress(b'junk')).decode();reject('concatenated_zlib',c)
 c=copy.deepcopy(candidate);c['inherited_inputs'][0]['sha256']='0'*64;reject('inherited_hash',c)
 # Metadata is deliberately outside the identity verifier, not authenticated.
 ignored=[]
 for key in ('rules_input_sha','generate','verify','format','artifacts_codec','limits'):
  c=copy.deepcopy(candidate);c[key]='changed metadata';m.verify_manifest(c,rows,old['inherited_inputs']);ignored.append(key)
 out={'scope':'independent identity codec check; producer verifier tested on mutated in-memory copies; no master manifest write',
  'source':identity(path),'checker':identity(Path(__file__)),'base':BASE,'base_manifest_sha256':hashlib.sha256(oldraw).hexdigest(),
  'identity_rows':len(rows),'checks':checks,'metadata_not_authenticated':ignored,
  'envelope_removed_fields':sorted(set(old)-set(candidate)),
  'envelope_changed_fields':sorted(k for k in set(old)&set(candidate) if old[k]!=candidate[k] and k!='artifacts_payload')}
 args.output.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
