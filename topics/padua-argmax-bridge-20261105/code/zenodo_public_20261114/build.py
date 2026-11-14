#!/usr/bin/env python3
"""Data-only assembly of the standalone public reproducibility package."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import tarfile
import zipfile

ROOT=Path(__file__).resolve().parents[4]
HERE=Path(__file__).resolve().parent
TOPIC=ROOT/'topics/padua-argmax-bridge-20261105'
OUTPUT=ROOT/'local-output/argmax-bridge-20261105/zenodo-public-20261114'
PACKAGE=OUTPUT/'padua-reproducibility'
SOURCES={}
SOURCE='656c15b758c3cf49782adb3af8b1bced361179e6'

def sha(b): return hashlib.sha256(b).hexdigest()
def save(name,b):
    p=PACKAGE/name; p.parent.mkdir(parents=True,exist_ok=True); p.write_bytes(b)
def copy(source,name=None):
    source=Path(source); name=name or source.relative_to(ROOT).as_posix()
    save(name,source.read_bytes())
    SOURCES[str(name)]=dict(path=source.relative_to(ROOT).as_posix())
def identity(name,b,source,**extra):
    return dict(path=name,bytes=len(b),sha256=sha(b),source=source,**extra)
def main():
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument('--source-commit',required=True); args=parser.parse_args()
    if re.fullmatch(r'[0-9a-f]{40}',args.source_commit) is None: raise ValueError('source commit must be full SHA')
    OUTPUT.mkdir(parents=True,exist_ok=True)
    if PACKAGE.exists(): raise RuntimeError('no package overwrite')
    PACKAGE.mkdir()
    phase=[]; poly=[]; origins={}
    archive=ROOT/'local-output/argmax-bridge-20261105/actual-return-20261107/return.tar.gz'
    archive_sha=sha(archive.read_bytes())
    if archive_sha!='b00fd57f85ce6d96a6c1fa01e2307abd815088bb8fcb28b1587657ef142b109a': raise ValueError('archive identity')
    with tarfile.open(archive) as t:
        for m in t:
            match=re.fullmatch(r'outputs/all/jobs/(\d+)/(produce|verify)/essential-receipt.json',m.name)
            if not match: continue
            if not m.isfile() or not 0<m.size<100000: raise ValueError('unsafe archive member')
            n=int(match[1]); mode=match[2]; key=n,mode
            if key in origins: raise ValueError('duplicate archive member')
            origins[key]=(t.extractfile(m).read(),dict(archive_sha256=archive_sha,member=m.name,origin='authenticated complete retained input'))
    inventory=json.loads((ROOT/'local-output/argmax-bridge-20261105/regeneration-20261114-direct-essentials-inventory.json').read_bytes())
    for row in inventory['files']:
        p=ROOT/'local-output/argmax-bridge-20261105/regeneration-20261114-direct-essentials'/row['name']
        b=p.read_bytes(); match=re.fullmatch(r'n(\d+)-(produce|verify).json',p.name); key=int(match[1]),match[2]
        if key in origins or sha(b)!=row['sha256'] or len(b)!=row['bytes']: raise ValueError('regenerated input identity')
        origins[key]=(b,dict(path=p.relative_to(ROOT).as_posix(),origin='regenerated complete retained input'))
    if set(origins)!={(n,m) for n in range(41,512) for m in ('produce','verify')}: raise ValueError('phase scope')
    for (n,mode),(b,source) in sorted(origins.items()):
        name=f'phase/inputs/n{n:04d}-{mode}.json'; save(name,b)
        phase.append(identity(name,b,source,n=n,**{'pass':mode}))
    for name in ('check.py','controls.py','runtime_probe.py'):
        copy(TOPIC/'code/independent_phase_checker'/name,'phase/'+name)
    results=[]
    for j in range(4):
        p=ROOT/f'local-output/argmax-bridge-20261105/i25-regeneration-20261114/full-v1/worker-{j}/observations.jsonl'
        for line in p.read_text().splitlines():
            r=json.loads(line); r.pop('CPU_seconds'); results.append(r)
    results.sort(key=lambda r:(r['n'],r['pass']))
    save('phase/expected-results.jsonl',(''.join(json.dumps(r,sort_keys=True,separators=(',',':'))+'\n' for r in results)).encode())
    full=json.loads((ROOT/'local-output/argmax-bridge-20261105/i25-regeneration-20261114/full-record-check.json').read_bytes())
    keys=['certificates','degrees','primary_fresh_scientific_pairs_equal','independent_primary_fresh_pairs_equal','minima','S_checks','distinct_S_keys','actual_lambda_checks','distinct_actual_lambda_keys','native_S_uppers_contained','native_S_uppers_total','native_lowers_contained','M_max','all_native_endpoints_validated']
    save('phase/expected-summary.json',(json.dumps({k:full[k] for k in keys},indent=2)+'\n').encode())
    freeze=json.loads((TOPIC/'code/regeneration_polynomial_20261114/frozen-inputs.json').read_bytes())
    for ns,source in sorted(freeze['certificates'].items(),key=lambda t:int(t[0])):
        n=int(ns); b=(ROOT/source).read_bytes(); name=f'polynomial/inputs/n{n:04d}.json.gz'; save(name,b); poly.append(identity(name,b,dict(path=source),n=n))
    small=TOPIC/'code/small_degree_unification'
    metadata=json.loads((small/'METADATA-FREEZE.json').read_bytes())
    closure={r['path'] for r in metadata['sources']}
    closure.add((small/'METADATA-FREEZE.json').relative_to(ROOT).as_posix())
    for name in ('finite_bernstein.py','finite_general.py','finite_general_run.py','finite_n2_exact.py'):
        closure.add('topics/padua-argmax-alln-20261101/code/part3/'+name)
    closure.add('topics/padua-proof-attempts-20261101/theory/proof-attempts-codex-01-padua-corner.md')
    for source in sorted(closure): copy(ROOT/source)
    for source,name,rowkey,columnkey,lo,hi in [(small/'checker-summary.json','polynomial/receipts/degrees-2-16.json','rows','columns',2,16),(ROOT/'topics/padua-argmax-effective-20261103/evidence/native-checker-summary.json','polynomial/receipts/degrees-17-32.json','final_rows','final_rows_columns',17,32)]:
        raw=source.read_bytes(); original=json.loads(raw)
        rows=[dict(zip(original[columnkey],row)) for row in original[rowkey] if lo<=row[0]<=hi]
        if {r['n'] for r in rows}!=set(range(lo,hi+1)): raise ValueError('accepted polynomial receipt scope')
        scientific=[{k:v for k,v in r.items() if k not in ('wall_seconds','child_cpu_seconds')} for r in rows]
        provenance=dict(path=source.relative_to(ROOT).as_posix(),sha256=sha(raw),transformation='selected accepted degree rows; CPU/wall timing omitted; scientific fields unchanged')
        save(name,(json.dumps(dict(source=provenance,accepted_rows=scientific),indent=2)+'\n').encode()); SOURCES[name]=provenance
    for n in range(33,41): copy(TOPIC/f'evidence/independent-n{n}.json',f'polynomial/receipts/n{n:04d}.json')
    for name in ('check.py','base_table.py','receipt.json'): copy(TOPIC/'code/onset512_analytic'/name,'analytic/'+name)
    for role,source in [('paper','paper'),('companion','companion-paper')]: copy(TOPIC/source/'sections/comparison-unified.tex',f'analytic/tables/{role}.tex')
    delivery=json.loads((TOPIC/'regeneration-delivery.json').read_bytes())
    for role in ('paper','companion'):
        row=delivery['manuscripts'][role]; b=Path(row['path']).read_bytes()
        if sha(b)!=row['sha256']: raise ValueError('PDF identity')
        save(f'papers/{role}.pdf',b)
        SOURCES[f'papers/{role}.pdf']=dict(path=row['path'],sha256=row['sha256'])
    copy(HERE/'verify.py','verify.py')
    for name in ('README.md','README.txt'): copy(HERE/'README.txt',name)
    payload=[identity(p.relative_to(PACKAGE).as_posix(),p.read_bytes(),SOURCES.get(p.relative_to(PACKAGE).as_posix(),dict(generated_by='code/zenodo_public_20261114/build.py'))) for p in sorted(PACKAGE.rglob('*')) if p.is_file()]
    manifest=dict(format='padua-public-reproducibility-v1',scientific_source_base_commit=SOURCE,public_adapter_source_commit=args.source_commit,public_adapter_sha256=sha((HERE/'verify.py').read_bytes()),builder_sha256=sha(Path(__file__).read_bytes()),phase_inputs=phase,polynomial_inputs=poly,payload=payload,expected_results_source='local-output/argmax-bridge-20261105/i25-regeneration-20261114/full-v1/worker-{0,1,2,3}/observations.jsonl; CPU_seconds omitted; all other fields retained',scope='finite certificate inputs 2 through 511 plus exact analytic checker for the degree >=512 reduction; premises in paired PDFs',license='No standalone license grant supplied in repository; owner publication metadata pending')
    save('MANIFEST.json',(json.dumps(manifest,indent=2,sort_keys=True)+'\n').encode())
    sums=''.join(sha(p.read_bytes())+'  '+p.relative_to(PACKAGE).as_posix()+'\n' for p in sorted(PACKAGE.rglob('*')) if p.is_file())
    save('SHA256SUMS',sums.encode())
    archive_out=OUTPUT/'padua-reproducibility-20261114.zip'
    if archive_out.exists(): raise RuntimeError('no ZIP overwrite')
    with zipfile.ZipFile(archive_out,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for p in sorted(PACKAGE.rglob('*')):
            if p.is_file(): z.write(p,p.relative_to(OUTPUT).as_posix())
    report=dict(zip_bytes=archive_out.stat().st_size,zip_sha256=sha(archive_out.read_bytes()),files=sum(p.is_file() for p in PACKAGE.rglob('*')),expanded_bytes=sum(p.stat().st_size for p in PACKAGE.rglob('*') if p.is_file()),phase_records=len(phase),polynomial_certificates=len(poly))
    (OUTPUT/'build-receipt.json').write_text(json.dumps(report,indent=2)+'\n'); print(json.dumps(report))
if __name__=='__main__': main()
