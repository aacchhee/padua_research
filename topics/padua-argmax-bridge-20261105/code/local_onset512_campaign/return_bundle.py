"""Data-only compact export/check. Never execute archive contents.

Every small history is retained; two post-validation random degrees also carry
their complete native/compiled dependency closure. Other native histories stay
in the campaign directory. Trusted frozen/package bytes are supplied separately.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import random
import zipfile
import sys
import time

import runner as R
from evidence import Access, identities, validate_pass, LABELS

COMPARE = ('tree','S_upper_rows','lambda_upper_rows','norm','verification','floor','corner','analytic_far','origin_lower_hex')

def sha(data): return hashlib.sha256(data).hexdigest()
def encoded(value): return (json.dumps(value, indent=2, allow_nan=False)+'\n').encode()

def same_bytes(left,right):
    return all(left[k]==right[k] for k in ('bytes','sha256'))

def completed(output):
    reg = R.read(output/'preregistration.json')
    assert reg['degrees'] == list(range(320,511)) and R.pins() == reg['pins']
    rows = []
    for stage in ('pilot','remaining'):
        summary = R.read(output/(stage+'-summary.json'))
        assert summary['quiescent'] and summary['ECHILD'] and not summary['failed'] and not summary['unstarted'] and not summary['cleanup_killed']
        rows += summary['results']
    assert sorted(row['n'] for row in rows) == reg['degrees']
    assert all(row['observed_returncode'] == 0 for row in rows)
    helper_pins=R.read(output/'helper-source-pins.json')['files']
    for row in helper_pins:
        assert row['input_head_equal']
        expected={key:row[key] for key in ('path','bytes','sha256')}
        assert R.identity(row['path'])==expected
        assert same_bytes(R.identity(output/'helper-source'/Path(row['path']).name),expected)
    evidence_pin=next(row for row in helper_pins if Path(row['path']).name=='evidence.py')
    assert same_bytes(evidence_pin,reg['compact_evidence'])
    for n in reg['degrees']:
        directory = output/'jobs'/str(n)
        attempt = R.read(directory/'attempt.json')
        assert attempt['failure'] is None and attempt['ECHILD'] and not attempt['cleanup_killed']
        proofs = []
        for mode in ('produce','verify'):
            target = directory/mode
            validation = R.read(target/'local-validation.json')
            assert validation['receipt'] == R.identity(target/'essential-receipt.json')
            assert validation['raw'] == R.identity(target/'raw-evidence.json')
            ex = R.read(directory/(mode+'-exit.json'))
            assert ex['observed_returncode'] == 0 and ex['ECHILD'] and not ex['timeout'] and not ex['cleanup_killed']
            account = R.read(target/'final-accounting.json')
            assert account['complete'] and account['first_failure'] is None
            proof = R.read(target/'essential-receipt.json')
            R.LocalAccess(R.ROOT,str(R.ROOT)).checker.verify_essential(proof, reg['pins']['freeze'])
            proofs.append(proof)
        assert all(proofs[0][key] == proofs[1][key] for key in COMPARE)
        assert (directory/'produce/essential-receipt.json').read_bytes() == (directory/'verify/original-certificate.json').read_bytes()
    return reg

def export(output, archive):
    reg = completed(output)
    R.save(output/'return-provenance.json', {'pins':reg['pins'],
        'trusted_manifest':R.identity(R.RELEASE/'runtime_manifest.json'),
        'runner':R.identity(R.__file__), 'return_code':R.identity(__file__),
        'python_invocation':R.read(output/'jobs/320/produce-exit.json')['command'][0],
        'regenerate':'Run runner.py preregister/pilot/remaining with a new exclusive output root; see committed preregistration-onset512-local.md',
        'retention':'All full histories remain in '+str(output)+'; this ZIP includes every small record and two complete randomly sampled native closures. Separate trusted frozen release supplies code/runtime pinned files.'})
    selection_path = output/'compact-selection.json'
    if not selection_path.exists():
        seed = os.urandom(32)
        R.save(selection_path, {'seed_hex':seed.hex(), 'eligible':reg['degrees'],
            'selected':random.Random(seed).sample(reg['degrees'],2), 'preregistration':R.identity(output/'preregistration.json'),
            'created_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),
            'method':'after completed() full coverage/quiescence checks: os.urandom(32); random.Random(seed_bytes).sample(sorted_completed_degrees,2); persisted once, never redrawn for size or result',
            'scope':'transport/review sample, not a statistical proof'})
    selection = R.read(selection_path)
    assert selection['eligible'] == reg['degrees']
    assert selection['selected'] == random.Random(bytes.fromhex(selection['seed_hex'])).sample(reg['degrees'],2)
    payload = {}
    def add(path, name=None):
        path = Path(path).resolve()
        if name is None: name = path.relative_to(R.ROOT).as_posix()
        data = path.read_bytes()
        if name in payload: assert payload[name] == data
        payload[name] = data
    for path in sorted((output/'helper-source').glob('*.py')):add(path)
    add(R.__file__);add(__file__)
    add(R.RELEASE/'runtime_manifest.json','TRUSTED_RUNTIME_MANIFEST.json')
    add(R.RELEASE/'asset_provenance.json','TRUSTED_ASSET_PROVENANCE.json')
    payload['README.txt']=('Local onset-512 compact return, provisional pending independent review.\n'
        'All 382 essential proofs and all small histories are present. Two random degrees also include complete native histories and external SHA objects; other native histories stay in the original local campaign directory.\n'
        'COMPACT.json lists every payload byte identity. The persisted compact-selection.json records the post-completion random seed, sorted population and draw; it is a transport/review sample, never a statistical proof. No archive code should be executed.\n'
        'Use the separately trusted repository code/local_onset512_campaign/return_bundle.py verify ARCHIVE.zip. That reader never extracts or executes payloads and refuses names overlapping the separately trusted release.\n'
        'Trusted source release commit: 996fedcad4ba79a28e45a3fe3678adc12f1e5358. Campaign input/rules commit: b45e29fa1fe3dbfa2517ff8043e5d9c440870530. Frozen engine sources are unchanged.\n'
        'Place the separately trusted compact release at local-output/argmax-bridge-20261105/compact-release-aea62883/padua30 relative to the repository. Its runtime_manifest.json SHA is recorded in COMPACT.json. TRUSTED_RUNTIME_MANIFEST.json and TRUSTED_ASSET_PROVENANCE.json here are data copies for inspection, not executable or self-authenticating trust roots.\n'
        'Runtime restoration: the trusted release contains all six pinned Debian packages and the resolved arithmetic headers/libraries under local-output/argmax-bridge-20261105/phase-checker/runtime/extracted/usr. Restore those bytes to the same relative repository paths, authenticating every file against the separately trusted asset_provenance.json first; no system package installation is required. Official Debian/snapshot URLs, package versions and SHA256 pins are in that provenance.\n'
        'The reader maps recorded original absolute paths through COMPACT.json root to current trusted repository or bundled payloads, and external identities to preserved-sha256 objects. New generation uses exclusive paths and records new build/runtime identities; historic timing and absolute paths need not reproduce.\n').encode()
    for path in sorted(output.iterdir()):
        if path.is_file(): add(path)
    # Small records for all cases: all proofs, raw records, logs and provenance.
    for n in reg['degrees']:
        case = output/'jobs'/str(n)
        for path in sorted(case.rglob('*')):
            if path.is_file() and not any(p.startswith('check-') for p in path.relative_to(case).parts): add(path)
    trusted = R.read(R.RELEASE/'runtime_manifest.json')['files']
    for n in selection['selected']:
        for mode in ('produce','verify'):
            target=output/'jobs'/str(n)/mode
            for path in sorted(target.rglob('*')):
                if path.is_file() and not path.is_symlink(): add(path)
            for name in ('raw-evidence.json','summary.json','final-accounting.json','preregistration.json','essential-receipt.json'):
                for row in identities(R.read(target/name)):
                    path=Path(row['path']).resolve(); assert R.identity(path)==row
                    if path.is_relative_to(R.ROOT):
                        name=path.relative_to(R.ROOT).as_posix()
                        if name in trusted:
                            assert all(trusted[name][k]==row[k] for k in ('bytes','sha256'))
                        else: add(path,name)
                    else: add(path,'preserved-sha256/'+row['sha256'])
    inventory = {'format':'PADUA-local-onset512-compact-v1','root':str(R.ROOT),
        'output':output.relative_to(R.ROOT).as_posix(),'degrees':reg['degrees'], 'selection':selection,
        'trusted_manifest':R.identity(R.RELEASE/'runtime_manifest.json'),
        'files':{name:{'bytes':len(data),'sha256':sha(data)} for name,data in sorted(payload.items())},
        'scope':'All essential certificates/small histories; full native closure for two random cases. Other full histories remain locally retained. Requires separate trusted release.'}
    with zipfile.ZipFile(archive,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as bundle:
        for name,data in sorted(payload.items()):bundle.writestr(name,data)
        bundle.writestr('COMPACT.json',encoded(inventory))
    R.save(archive.with_suffix(archive.suffix+'.receipt.json'),{'archive':R.identity(archive),'selected':selection['selected'],'degrees':reg['degrees']})
    return inventory

def verify(archive):
    payload={}; total=0
    with zipfile.ZipFile(archive,'r') as bundle:
        for member in bundle.infolist():
            name=member.filename; path=Path(name)
            assert not path.is_absolute() and '..' not in path.parts and path.as_posix()==name and name not in payload
            assert len(payload)<200000 and member.file_size<=512*1024**2
            assert not member.is_dir(); total+=member.file_size; assert total<=2*1024**3
            data=bundle.read(member)
            payload[name]=data
    inventory=json.loads(payload.pop('COMPACT.json'))
    assert set(inventory['files'])==set(payload)
    for name,row in inventory['files'].items(): assert row=={'bytes':len(payload[name]),'sha256':sha(payload[name])}
    trusted=R.read(R.RELEASE/'runtime_manifest.json')['files']
    assert not set(payload)&set(trusted), 'archive shadows trusted package'
    assert same_bytes(R.identity(R.RELEASE/'runtime_manifest.json'),inventory['trusted_manifest'])
    assert payload['TRUSTED_RUNTIME_MANIFEST.json']==(R.RELEASE/'runtime_manifest.json').read_bytes()
    assert payload['TRUSTED_ASSET_PROVENANCE.json']==(R.RELEASE/'asset_provenance.json').read_bytes()
    def reader(name):
        if name in trusted:
            path=R.ROOT/name
            if name=='asset_provenance.json':path=R.RELEASE/name
            data=path.read_bytes(); row=trusted[name]
            assert len(data)==row['bytes'] and sha(data)==row['sha256']
            return data
        return payload[name]
    access=Access(R.ROOT,inventory['root'],read_bytes=reader)
    prefix=inventory['output']; reg=json.loads(payload[prefix+'/preregistration.json'])
    assert reg['degrees']==inventory['degrees']==list(range(320,511))
    local_pins=R.pins()
    assert reg['pins']['source']==local_pins['source'] and reg['pins']['arithmetic_files']==local_pins['arithmetic_files']
    for key in ('freeze','asset_provenance'):assert same_bytes(reg['pins'][key],local_pins[key])
    selection=inventory['selection']; assert selection['eligible']==reg['degrees']
    assert selection==access.json(prefix+'/compact-selection.json')
    prereg_data=payload[prefix+'/preregistration.json']
    prereg_identity={'path':inventory['root']+'/'+prefix+'/preregistration.json','bytes':len(prereg_data),'sha256':sha(prereg_data)}
    assert selection['preregistration']==prereg_identity
    assert selection['selected']==random.Random(bytes.fromhex(selection['seed_hex'])).sample(reg['degrees'],2)
    for n in reg['degrees']:
        case=prefix+'/jobs/'+str(n); proofs=[]
        for mode in ('produce','verify'):
            target=case+'/'+mode
            proof=access.json(target+'/essential-receipt.json');proofs.append(proof)
            assert proof['n']==n and proof['freeze']==reg['pins']['freeze']
            assert access.checker.verify_essential(proof,proof['freeze'])==proof['verification']
            ex=access.json(case+'/'+mode+'-exit.json');assert ex['observed_returncode']==0 and ex['ECHILD'] and not ex['timeout'] and not ex['cleanup_killed']
            account=access.json(target+'/final-accounting.json'); assert account['complete'] and account['first_failure'] is None and account['hard_aggregate_cap']==120
            summary=access.json(target+'/summary.json')
            assert summary['result']=='PROVISIONAL_PROOF_PENDING_FINAL_ACCOUNTING' and summary['first_failure'] is None
            assert account['engine_config']==summary['engine_config'] and account['engine_config']['n']==n and account['engine_config']['mode']==mode
            assert account['result']==LABELS[mode]
            assert 0<=account['total_CPU_through_summary']<120
            limit=account['final_self_limit'];assert limit['no_live_children'] and limit['waited_child_CPU']+limit['absolute_self_CPU_hard']<=119
            raw=payload[target+'/raw-evidence.json'];assert same_bytes(proof['whole_raw_evidence'],{'bytes':len(raw),'sha256':sha(raw)})
            raw_doc=json.loads(raw);assert reg['python'] in raw_doc['runtime_before']['all_file_mappings']
            assert proof['whole_raw_evidence']==summary['whole_raw_evidence']
            config=account['engine_config'];assert config['output']==inventory['root']+'/'+target
            python_invocation=access.json(prefix+'/return-provenance.json')['python_invocation']
            command=[python_invocation,'-E','-S','-B',inventory['root']+'/topics/padua-argmax-bridge-20261105/code/final_hybrid_engine/engine.py','--mode',mode,'--n',str(n),'--output',config['output'],'--run-once']
            if mode=='verify':command+=['--certificate',inventory['root']+'/'+case+'/produce/essential-receipt.json']
            assert ex['command']==command
            validation=access.json(target+'/local-validation.json')
            for key,filename in [('receipt','essential-receipt.json'),('raw','raw-evidence.json')]:
                data=payload[target+'/'+filename];row=validation[key];assert row['bytes']==len(data) and row['sha256']==sha(data)
            if n in selection['selected']:validate_pass(access,target,n,mode,{'files':trusted})
        assert all(proofs[0][key]==proofs[1][key] for key in COMPARE)
        assert payload[case+'/produce/essential-receipt.json']==payload[case+'/verify/original-certificate.json']
        attempt=access.json(case+'/attempt.json');assert attempt['failure'] is None and attempt['ECHILD'] and not attempt['cleanup_killed']
        assert attempt['n']==n and attempt['terminal'] and attempt['passes']==[access.json(case+'/'+mode+'-exit.json') for mode in ('produce','verify')]
        admission=access.json(case+'/admitted.json');assert admission['n']==n
        assert admission['preregistration']==prereg_identity
        wrapper=access.json(case+'/wrapper-exit.json');assert wrapper['observed_returncode']==0
    for stage,degrees in [('pilot',[320]),('remaining',list(range(321,511)))]:
        admission=access.json(prefix+'/'+stage+'-admitted.json');assert admission['degrees']==degrees
        assert admission['preregistration']==prereg_identity
        summary=access.json(prefix+'/'+stage+'-summary.json')
        assert summary['ECHILD'] and summary['quiescent'] and not summary['failed'] and not summary['unstarted'] and not summary['cleanup_killed']
        assert sorted(row['n'] for row in summary['results'])==degrees
        for row in summary['results']:assert row==access.json(prefix+'/jobs/'+str(row['n'])+'/wrapper-exit.json')
    helpers=access.json(prefix+'/helper-source-pins.json')['files']
    for row in helpers:
        data=payload[prefix+'/helper-source/'+Path(row['path']).name]
        assert row['input_head_equal'] and row['bytes']==len(data) and row['sha256']==sha(data)
    evidence_pin=next(row for row in helpers if Path(row['path']).name=='evidence.py')
    assert same_bytes(evidence_pin,reg['compact_evidence'])
    print(json.dumps({'status':'accepted_pending_independent_review','pairs':191,'proofs':382,'sample':selection['selected'],'archive':R.identity(archive)}))

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('action',choices=['export','verify']);ap.add_argument('archive',type=Path);ap.add_argument('--output',type=Path)
    args=ap.parse_args()
    if args.action=='export':export(args.output.resolve(),args.archive.resolve())
    else:verify(args.archive.resolve())
