#!/usr/bin/env python3
"""Verify metadata-only envelope change against original v6 and current map."""
import argparse,ast,hashlib,importlib.util,json,subprocess
from pathlib import Path
import check_manifest as independent
TOP=Path(__file__).resolve().parents[2];ROOT=TOP.parents[1]
OLD='d826a0fd0df617b7d0c36e782607c2b979a26048'
def identity(p,relative=None):
 p=Path(p);b=p.read_bytes();return {'path':p.relative_to(relative).as_posix() if relative else str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
 path=TOP/'code/artifact_manifest.py';oldtext=subprocess.check_output(['git','show',OLD+':topics/padua-3d-20261106/code/artifact_manifest.py'],cwd=ROOT).decode();newtext=path.read_text()
 def without_envelope(text):
  tree=ast.parse(text);tree.body=[n for n in tree.body if not isinstance(n,ast.FunctionDef) or n.name!='make_manifest'];return ast.dump(tree,include_attributes=False)
 assert without_envelope(oldtext)==without_envelope(newtext)
 old={'__file__':str(path),'__name__':'old_manifest'};exec(compile(oldtext,str(path),'exec'),old)
 spec=importlib.util.spec_from_file_location('new_manifest',path);new=importlib.util.module_from_spec(spec);spec.loader.exec_module(new)
 rows=sorted([identity(p,TOP) for d in ('code','evidence') for p in (TOP/d).rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc'],key=lambda r:r['path'].encode())
 inherited=[identity(ROOT/'tracks/lattice-unisolvence/code'/name,ROOT) for name in ('c3_lebesgue.py','c3_rank.py')]
 before=old['make_manifest'](rows,inherited);after=new.make_manifest(rows,inherited)
 different=sorted(k for k in before if before[k]!=after[k]);assert different==['artifacts_codec','format','limits']
 assert independent.decode(after['artifacts_payload'])==rows
 assert old['encode_rows'](rows)==new.encode_rows(rows)
 new.verify_manifest(after,rows,inherited)
 oldbytes=len((json.dumps(before,separators=(',',':'))+'\n').encode());newbytes=len((json.dumps(after,separators=(',',':'))+'\n').encode())
 out={'scope':'AST equality outside make_manifest; only3 informational fields change inside it; exact old/new current identity payload and independent decode equality',
  'old_commit':OLD,'old_code_sha256':hashlib.sha256(oldtext.encode()).hexdigest(),'source':identity(path),'checker':identity(Path(__file__)),
  'independent_decoder':identity(Path(independent.__file__)),'artifact_count':len(rows),'artifact_bytes':sum(r['bytes'] for r in rows),
  'map_sha256':hashlib.sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest(),
  'changed_fields':different,'old_compact_bytes':oldbytes,'new_compact_bytes':newbytes,'saved_bytes':oldbytes-newbytes,'same_identity_payload':True}
 a.output.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
