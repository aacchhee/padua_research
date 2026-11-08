#!/usr/bin/env bash
set -euo pipefail
python - "$@" <<'PY'
import hashlib, json, re, subprocess, sys, tarfile, zipfile
from pathlib import Path
root=Path.cwd(); topic=Path('topics/padua-argmax-bridge-20261105')
code=topic/'code/independent_phase_checker'; output=Path(sys.argv[1])
entries={}; origins={}
def sha(b): return hashlib.sha256(b).hexdigest()
def put(name,b,origin):
    if name in entries: raise ValueError('duplicate bundle member '+name)
    entries[name]=b; origins[name]=origin
def file(name,path): put(name,path.read_bytes(),str(path))
def gitbytes(name): return subprocess.check_output(['git','show','4846913:'+str(code/name)])
pins=json.loads((code/'FULL-PREREGISTRATION.json').read_text())['source_sha256']
for name,h in pins.items():
    b=(code/name).read_bytes(); assert sha(b)==h
    put('source/full/'+name,b,'executed full-run source, unchanged since preregistration')
for name in ['check.py','controls.py','run.py']:
    put('source/pilot-v2/'+name,gitbytes(name),'git commit4846913')
v1=gitbytes('check.py').decode().replace(
    'def fold(a,b): return (1-a,1-b) if a+b>1 or (a+b==1 and a>b) else (a,b)',
    'def fold(a,b): return (a,b) if a+b<=1 else (1-a,1-b)').replace(
    'grid={fold(F(i,4),F(j,4)) for i in range(5) for j in range(5-i)}',
    'grid={(F(i,4),F(j,4)) for i in range(5) for j in range(5-i)}').replace(
    "stored=read_rows(data['S_upper_rows']); need(keys<=set(stored),'missing required S keys')\n"
    "    need(all(0<=a and 0<=b and a+b<=1 for a,b in stored),'retained S key domain')\n"
    "    keys.update(stored)",
    "stored=read_rows(data['S_upper_rows']); need(set(stored)==keys,'retained S keys differ from reconstructed keys')")
cv1=gitbytes('controls.py').decode().replace('import check as c\ndef arithmetic_controls():',
    'import check as c\n\ndef arithmetic_controls():')
cv1=''.join(line for line in cv1.splitlines(True) if not line.startswith('    for p,q in [') and
            not line.startswith("        c.need(c.fold(*p)==q"))
cv1=cv1.replace('    return tests\ndef corruption_controls','    return tests\n\ndef corruption_controls')
oldpins=json.loads((code/'PILOT-PREREGISTRATION.json').read_text())['source_sha256']
for name,b in [('check.py',v1.encode()),('controls.py',cv1.encode()),('run.py',gitbytes('run.py'))]:
    assert sha(b)==oldpins[name],(name,sha(b))
    put('source/pilot-v1/'+name,b,'exact reversible reconstruction from4846913; original preregistered hash verified')
for path in sorted(code.glob('*.json')): file('records/'+path.name,path)
for path in [topic/'theory/J03-independent-phase-checker.md',code/'SECTION5-INTERFACE.md',
             topic/'independent-checks-onset512-response.md']:
    file('documentation/'+path.name,path)
base=Path('local-output/argmax-bridge-20261105')
for prefix in ['i25-pilot-v1-20261108T105100Z','i25-pilot-v2-20261108T105639Z',
               'i25-full-v1-20261108T110409Z','i25-independent-six-20261108T111930Z']:
    for path in sorted((base/prefix).rglob('*')):
        if path.is_file(): file('runs/'+prefix+'/'+str(path.relative_to(base/prefix)),path)
    for path in sorted(base.glob(prefix+'.*')):
        if path.is_file(): file('runs/'+prefix+'/'+path.name,path)
review=Path('/tmp/onset512-independent-review')
for name in ['pilot_records.py','pilot-v2-record-check.json','full-prereg-data-check.json',
             'six_runner.py','six-preregistration.json','six-wrapper.stdout','six-wrapper.stderr',
             'full_records.py','full-record-check.json','six-record-check.json','v2-seam-controls.json',
             'record-check-first-failures.json','scalar_controls.py','scalar_controls.first-failed.py',
             'scalar-controls-first-failure.json','scalar-controls.json']:
    file('independent-review/'+name,review/name)
old=base/'actual-return-20261107/return.tar.gz'
assert sha(old.read_bytes())=='b00fd57f85ce6d96a6c1fa01e2307abd815088bb8fcb28b1587657ef142b109a'
with tarfile.open(old,'r:gz') as tf:
    for m in tf:
        match=re.fullmatch(r'outputs/all/jobs/(\d+)/(produce|verify)/essential-receipt.json',m.name)
        if match:
            assert m.isfile() and 0<m.size<100000
            put('proofs/n'+match[1]+'-'+match[2]+'.json',tf.extractfile(m).read(),'data-only member '+m.name+' of pinned old tar')
inv=base/'onset512-local-20261108-essential-inventory.json'; ib=inv.read_bytes()
assert sha(ib)=='d7cea34dd64d9df329d1398c2418fbf984a9084b135cad695866a9c437551740'
put('inputs/new-inventory.json',ib,str(inv))
for row in json.loads(ib)['files']:
    p=base/'onset512-local-20261108-essential'/row['name']; b=p.read_bytes()
    assert len(b)==row['bytes'] and sha(b)==row['sha256']
    put('proofs/'+row['name'],b,str(p))
assert len([n for n in entries if n.startswith('proofs/')])==942
small=base/'onset512-certificates-20261108.zip'
assert small.stat().st_size==945235 and sha(small.read_bytes())=='c22d600cb67462918587b01f2ef5adcbf9030b825fb0f2cc79c1b9c27c7da8c8'
readme='''# I25 independent arithmetic evidence

Current outcome: all942 complete trees for471degrees41..511 accepted with
independently substituted bounds; fourworkers EXIT0;2519.420775278CPU-s and
646.839168173wall-s. Distinct reviewer accepted full records and separately
replayed bothpasses41,458,511 (six certificates, EXIT0).31 exact arithmetic
controls passed per process; pilot additionally rejected27 corruptions.
This is not universal validation of stored native upper endpoints.

The records preserve prospective pending/gated status strings and failedv1
history; these are historical, not current outcome labels. V1 conservatively
rejected seam aliases before numerical evaluation; reviewedv2 corrected only
canonical value reuse and passed. All original outputs remain unchanged.

source/full contains the executed frozen arithmetic/checker/driver. The core
is246lines. Pilotv2 sources are exact4846913 Git bytes; pilotv1 source bytes
were reversibly reconstructed and matched every original preregistered hash.
Proof inputs are942 JSON-only replicas read through trusted archive readers;
no native archive source or binary was extracted or executed. Runtime/source/
input identities, all logs, receipts, failed controls and independent scripts
are retained. The canonical review prose is a dated snapshot; its I25 outcome
is complete, though unrelated later manuscript addenda may still be appended.

For the exact registered full command use FULL-PREREGISTRATION.json plus
FULL-AMENDMENT-01.json with the public repository and these pinned returns:
old return.tar.gz,36045486B,SHA256
b00fd57f85ce6d96a6c1fa01e2307abd815088bb8fcb28b1587657ef142b109a;
new proof-only onset512-certificates-20261108.zip,945235B,SHA256
c22d600cb67462918587b01f2ef5adcbf9030b825fb0f2cc79c1b9c27c7da8c8.
Restore only verified new JSON data into the registered additional-dir and
place its authenticated INVENTORY.json at the registered sibling inventory
path. The runner reads only whitelisted JSON from the old tar; do not run
archive code. Python3.12.14 and NumPy2.3.5 identities and the explicit IEEE
round-to-nearest/gradual-underflow trusted assumptions are in the run inputs.
Analytic corner/far/floor and cover lemmas remain mathematical premises.
Public Zenodo deposit/DOI and the separate Claude audit remain pending.
'''
put('README.md',readme.encode(),'authored evidence-package README')
manifest={'format':'PADUA-I25-EVIDENCE-v1','command':'bash '+str(code/'bundle.sh')+' '+str(output),
          'proofs':942,'members':[{'path':n,'bytes':len(entries[n]),'sha256':sha(entries[n]),'origin':origins[n]} for n in sorted(entries)]}
entries['MANIFEST.json']=(json.dumps(manifest,indent=2)+'\n').encode()
with zipfile.ZipFile(output,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for name,b in sorted(entries.items()): z.writestr(name,b)
with zipfile.ZipFile(output) as z:
    assert z.testzip() is None
    for row in manifest['members']:
        b=z.read(row['path']); assert len(b)==row['bytes'] and sha(b)==row['sha256']
print(json.dumps({'path':str(output),'bytes':output.stat().st_size,'sha256':sha(output.read_bytes()),'members':len(entries),'proofs':942}))
PY
