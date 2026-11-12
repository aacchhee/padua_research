#!/usr/bin/env python3
"""Check historical T8 metadata and unchanged census using isolated outputs."""
from pathlib import Path
import argparse,hashlib,importlib.util,json,platform,shutil,tempfile
parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path);args=parser.parse_args()
top=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('response02_t8_core',top/'code/t8_cyclic.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
scratch=Path(tempfile.mkdtemp(prefix='padua-3d-response02-t8-'));replay=scratch/'topic';(replay/'evidence').mkdir(parents=True)
shutil.copy(top/'evidence/t2-n3-null-cover.json',replay/'evidence')
m.TOP=replay;m.SCRATCH=scratch/'raw';m.controls();m.census(2)
old=json.loads((top/'evidence/t8-unshifted-n2.json').read_text());new=json.loads((replay/'evidence/t8-unshifted-n2.json').read_text())
skip={'source_sha256','versions','raw_path','seconds','status'}
a={k:v for k,v in old.items() if k not in skip};b={k:v for k,v in new.items() if k not in skip}
assert a==b,(a,b)
assert m.metadata('python t8_even_family.py')['preregistration_sha256']==m.PREREG_E_SHA256
assert m.metadata('python t8_phases.py')['preregistration_sha256']==m.PREREG_UOP_SHA256
out={'verdict':'PASS','source_sha256':m.sha(m.__file__),'python':platform.python_version(),'checks':['controls','n2 census scientific fields and raw hash unchanged','historical UOP and E preregistration pins'],'isolated_scratch':str(scratch),'raw_bytes':new['raw_bytes'],'raw_sha256':new['raw_sha256'],'historical_receipts_modified':False, 'command':'OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-3d-20261106/code/check_response02_t8.py --output <receipt>', 'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'rules_input_sha':'7afa6a54a4db4652267e38cd48658ba435d20481'}
text=json.dumps(out,sort_keys=True)+'\n'
if args.output is not None:
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(text)
print(text,end='')
