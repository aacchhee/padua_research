#!/usr/bin/env python3
"""Adversarial basis-certificate controls for the FLINT path; no developer edits."""
import copy,hashlib,json,subprocess,sys
from pathlib import Path
from flint_disk_check import verify_basis,parse_input,identity
TOP=Path(__file__).resolve().parents[1]
WORK=Path('/tmp/padua-lanczos-nonproduct-20261105/scan-review')
def main():
 wd=WORK/'flint-negative-controls-v2';wd.mkdir(exist_ok=False)
 exe=WORK/'flint-D36x9-d8/exporter';inp=WORK/'D36x9/input.txt';basis=wd/'pivot4.json'
 cmd=[str(exe),str(inp),'4','pivot','D36x9']
 with basis.open('w') as out,(wd/'export.log').open('w') as err:subprocess.run(cmd,stdout=out,stderr=err,check=True,timeout=30)
 points=parse_input(inp);doc=json.loads(basis.read_text());verify_basis(doc,points)
 controls=[]
 mutations=[
 ('basis value',lambda d:d['B'][3].__setitem__(0,'999')),
 ('pivot norm',lambda d:d['d'].__setitem__(3,'999')),
 ('constant start',lambda d:d['B'][0].__setitem__(0,'2')),
 ('input coordinate',lambda d:d['points'][0].__setitem__(0,'999')),
 ('input weight',lambda d:d['points'][0].__setitem__(2,'1')),
 ('wrong parent',lambda d:d['steps'][3].update(parent=0)),
 ('inadmissible axis',lambda d:d['steps'][1].update(axis=1)),
 ('alpha coefficient',lambda d:d['steps'][3]['alpha'].__setitem__(0,'999')),
 ('source scale',lambda d:d['steps'][3].update(sigma_squared='999')),
 ('wrong grading',lambda d:d['meta'][3].__setitem__(1,1)),
 ('wrong prefix',lambda d:d['ends'].__setitem__(2,5)),
 ('choice metadata',lambda d:d['choices'].__setitem__(0,'Y')),
 ('tie metadata',lambda d:d.update(ties=[[2,1],[2,1]])),
 ('wrong fixed rule',lambda d:d.update(rule='bj'))]
 for name,change in mutations:
  changed=copy.deepcopy(doc);change(changed)
  try:verify_basis(changed,points)
  except (ValueError,KeyError,IndexError) as exc:controls.append(dict(control=name,rejected=True,diagnostic=str(exc)));continue
  raise AssertionError('accepted malformed basis: '+name)
 # Coherently rescale a basis vector and its norm: Gram alone would accept,
 # but creator identity must reject because it fixes the monic normalization.
 changed=copy.deepcopy(doc)
 from flint import fmpq
 changed['B'][3]=[str(2*fmpq(v)) for v in changed['B'][3]];changed['d'][3]=str(4*fmpq(changed['d'][3]))
 try:verify_basis(changed,points)
 except ValueError as exc:controls.append(dict(control='Gram-preserving column rescale',rejected=True,diagnostic=str(exc)))
 else:raise AssertionError('monic normalization not enforced')
 d65=Path('/tmp/padua-lanczos-nonproduct-20261105/p6/pilot8-D65x9/input.txt')
 from fractions import Fraction as F
 dirs={(65,0),(-65,0),(0,65),(0,-65)}
 for a,b in ((16,63),(25,60),(33,56),(39,52)):
  for u,v in ((a,b),(b,a)):
   for sx in (-1,1):
    for sy in (-1,1):dirs.add((sx*u,sy*v))
 expected={(F(k*a,585),F(k*b,585),F(1,324)) for k in range(1,10) for a,b in dirs}
 raw=d65.read_text().splitlines();actual={tuple(map(F,line.split())) for line in raw[1:]}
 assert int(raw[0])==len(actual)==len(expected)==324 and actual==expected
 report=dict(d65_input=identity(d65),d65_exact_admission_input_match=True,status='PASS 15 malicious basis-export rejection controls',command=[sys.executable,'-B',*sys.argv],code=identity(__file__),checked_code=identity(TOP/'code/flint_disk_check.py'),export_command=cmd,basis=identity(basis),input=identity(inp),export_binary=identity(exe),controls=controls)
 (TOP/'evidence/check-scans-flint-guards.json').write_text(json.dumps(report,indent=2)+'\n');print(report['status'])
if __name__=='__main__':main()
