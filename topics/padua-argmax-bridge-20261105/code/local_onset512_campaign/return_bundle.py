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

if sys.flags.optimize:
    raise RuntimeError("optimized Python is unsupported; use python3 -E -B")

import runner as R
from evidence import Access, identities, validate_pass, LABELS, require, safe
from common import strict as parse_strict

MANIFEST_SHA = '5b89fa66e742952497f99a49110a965ada2828b1861917268d3074af0eb22a16'
CANONICAL_ARCHIVE_SHA = 'da63280a7e4aec86fa52e3f8384620fbf07939006ab5f6f70222fa2485816e7e'
CAMPAIGN_RUNNER_SHA = '459d0728a0cb264d241bc76d270209842fc2aa55c0fadd32e23f8e3b0523af9e'

COMPARE = ('tree','S_upper_rows','lambda_upper_rows','norm','verification','floor','corner','analytic_far','origin_lower_hex')

def strict(data):
    value = parse_strict(data)
    def check(value):
        if isinstance(value, dict):
            for key, child in value.items():
                if key in {'bytes', 'n', 'observed_returncode', 'hard_aggregate_cap'}:
                    require(type(child) is int, 'integer field: ' + key)
                if key in {'ECHILD', 'quiescent', 'complete', 'terminal', 'no_live_children',
                           'input_head_equal', 'timeout', 'failed'}:
                    require(type(child) is bool, 'boolean field: ' + key)
                if key in {'total_CPU_through_summary', 'waited_child_CPU', 'absolute_self_CPU_hard'}:
                    require(type(child) in (int, float), 'numeric CPU field: ' + key)
                check(child)
        elif isinstance(value, list):
            for child in value: check(child)
    check(value)
    return value

def sha(data): return hashlib.sha256(data).hexdigest()
def encoded(value): return (json.dumps(value, indent=2, allow_nan=False)+'\n').encode()

def same_bytes(left,right):
    return type(left['bytes']) is int and type(right['bytes']) is int and all(left[k]==right[k] for k in ('bytes','sha256'))

def completed(output):
    reg = R.read(output/'preregistration.json')
    require(reg['degrees'] == list(range(320,511)) and R.pins() == reg['pins'], "required: reg['degrees'] == list(range(320,511)) and R.pins() == reg['pins']")
    rows = []
    for stage in ('pilot','remaining'):
        summary = R.read(output/(stage+'-summary.json'))
        require(summary['quiescent'] is True and summary['ECHILD'] is True and summary['failed'] is False and summary['unstarted'] == [] and summary['cleanup_killed'] == [], "required: summary['quiescent'] is True and summary['ECHILD'] is True and summary['failed'] is False and summary['unstarted'] == [] and summary['cleanup_killed'] == []")
        rows += summary['results']
    require(sorted(row['n'] for row in rows) == reg['degrees'], "required: sorted(row['n'] for row in rows) == reg['degrees']")
    require(all(row['observed_returncode'] == 0 for row in rows), "required: all(row['observed_returncode'] == 0 for row in rows)")
    helper_pins=R.read(output/'helper-source-pins.json')['files']
    for row in helper_pins:
        require(row['input_head_equal'] is True, "required: row['input_head_equal'] is True")
        expected={key:row[key] for key in ('path','bytes','sha256')}
        require(R.identity(row['path'])==expected, "required: R.identity(row['path'])==expected")
        require(same_bytes(R.identity(output/'helper-source'/Path(row['path']).name),expected), "required: same_bytes(R.identity(output/'helper-source'/Path(row['path']).name),expected)")
    evidence_pin=next(row for row in helper_pins if Path(row['path']).name=='evidence.py')
    require(same_bytes(evidence_pin,reg['compact_evidence']), "required: same_bytes(evidence_pin,reg['compact_evidence'])")
    for n in reg['degrees']:
        directory = output/'jobs'/str(n)
        attempt = R.read(directory/'attempt.json')
        require(attempt['failure'] is None and attempt['ECHILD'] is True and attempt['cleanup_killed'] == [], "required: attempt['failure'] is None and attempt['ECHILD'] is True and attempt['cleanup_killed'] == []")
        proofs = []
        for mode in ('produce','verify'):
            target = directory/mode
            validation = R.read(target/'local-validation.json')
            require(validation['receipt'] == R.identity(target/'essential-receipt.json'), "required: validation['receipt'] == R.identity(target/'essential-receipt.json')")
            require(validation['raw'] == R.identity(target/'raw-evidence.json'), "required: validation['raw'] == R.identity(target/'raw-evidence.json')")
            ex = R.read(directory/(mode+'-exit.json'))
            require(ex['observed_returncode'] == 0 and ex['ECHILD'] is True and ex['timeout'] is False and ex['cleanup_killed'] == [], "required: ex['observed_returncode'] == 0 and ex['ECHILD'] is True and ex['timeout'] is False and ex['cleanup_killed'] == []")
            account = R.read(target/'final-accounting.json')
            require(account['complete'] is True and account['first_failure'] is None, "required: account['complete'] is True and account['first_failure'] is None")
            proof = R.read(target/'essential-receipt.json')
            R.LocalAccess(R.ROOT,str(R.ROOT)).checker.verify_essential(proof, reg['pins']['freeze'])
            proofs.append(proof)
        require(all(proofs[0][key] == proofs[1][key] for key in COMPARE), 'required: all(proofs[0][key] == proofs[1][key] for key in COMPARE)')
        require((directory/'produce/essential-receipt.json').read_bytes() == (directory/'verify/original-certificate.json').read_bytes(), "required: (directory/'produce/essential-receipt.json').read_bytes() == (directory/'verify/original-certificate.json').read_bytes()")
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
    require(selection['eligible'] == reg['degrees'], "required: selection['eligible'] == reg['degrees']")
    require(selection['selected'] == random.Random(bytes.fromhex(selection['seed_hex'])).sample(reg['degrees'],2), "required: selection['selected'] == random.Random(bytes.fromhex(selection['seed_hex'])).sample(reg['degrees'],2)")
    payload = {}
    def add(path, name=None):
        path = Path(path).resolve()
        if name is None: name = path.relative_to(R.ROOT).as_posix()
        data = path.read_bytes()
        if name in payload: require(payload[name] == data, 'required: payload[name] == data')
        payload[name] = data
    for path in sorted((output/'helper-source').glob('*.py')):add(path)
    add(R.__file__);add(__file__)
    add(R.RELEASE/'runtime_manifest.json','TRUSTED_RUNTIME_MANIFEST.json')
    add(R.RELEASE/'asset_provenance.json','TRUSTED_ASSET_PROVENANCE.json')
    payload['README.txt']=('Local onset-512 compact return, provisional pending independent review.\n'
        'All 382 essential proofs and all small histories are present. Two random degrees also include complete native histories and external SHA objects; other native histories stay in the original local campaign directory.\n'
        'COMPACT.json lists every payload byte identity. The persisted compact-selection.json records the post-completion random seed, sorted population and draw; it is a transport/review sample, never a statistical proof. No archive code should be executed.\n'
        'Use the separately trusted repository code/local_onset512_campaign/return_bundle.py verify ARCHIVE.zip (invoke with python3 -E -B). That reader never extracts or executes payloads and refuses names overlapping the separately trusted release.\n'
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
                    path=Path(row['path']).resolve(); require(R.identity(path)==row, 'required: R.identity(path)==row')
                    if path.is_relative_to(R.ROOT):
                        name=path.relative_to(R.ROOT).as_posix()
                        if name in trusted:
                            require(all(trusted[name][k]==row[k] for k in ('bytes','sha256')), "required: all(trusted[name][k]==row[k] for k in ('bytes','sha256'))")
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

def exit0(record):
    require(type(record['observed_returncode']) is int and record['observed_returncode'] == 0, 'observed integer EXIT0')


def check_members(payload, prefix, degrees, selected, helpers):
    """Limit jobs and native closures to registered cases; never accept failure debris."""
    safe(prefix)
    pass_files = {'preregistration.json', 'original-certificate.json', 'tree.json',
                  'essential-receipt.json', 'raw-evidence.json', 'summary.json',
                  'final-accounting.json', 'local-validation.json', 'S-build.json',
                  'lambda-build.json', 'runtime-before.json', 'runtime-after.json',
                  'loaded-before.maps', 'loaded-after.maps', 'storage-dedup.json'}
    pass_files.update(stage + suffix for stage in ('controls', 'checker')
                      for suffix in ('-entry.json', '-checkpoint.json', '-descendants.json',
                                     '-supervisor.json', '.stdout', '.stderr'))
    top = {'preregistration.json', 'helper-source-pins.json', 'return-provenance.json',
           'compact-selection.json', 'pilot-admitted.json', 'remaining-admitted.json',
           'pilot-summary.json', 'remaining-summary.json', '.preserve.lock'}
    outside = {'README.txt', 'TRUSTED_RUNTIME_MANIFEST.json', 'TRUSTED_ASSET_PROVENANCE.json',
               Path(R.__file__).relative_to(R.ROOT).as_posix(),
               Path(__file__).resolve().relative_to(R.ROOT).as_posix()}
    helper_names = {Path(row['path']).name for row in helpers}
    for name in payload:
        require('failure' not in Path(name).name, 'unexpected failure member')
        if name in outside:
            continue
        if name.startswith('preserved-sha256/'):
            require(len(Path(name).parts) == 2 and len(Path(name).name) == 64 and
                    all(c in '0123456789abcdef' for c in Path(name).name), 'preserved object name')
            require(sha(payload[name]) == Path(name).name, 'preserved object hash')
            continue
        require(name.startswith(prefix + '/'), 'unregistered archive member: ' + name)
        parts = Path(name[len(prefix)+1:]).parts
        if len(parts) == 1:
            require(parts[0] in top, 'unregistered campaign member: ' + name)
            if parts[0] == '.preserve.lock':
                require(payload[name] == b'', 'preserve lock must be empty')
        elif parts[0] == 'helper-source':
            require(len(parts) == 2 and parts[1] in helper_names, 'unregistered helper source')
        else:
            require(parts[0] == 'jobs' and len(parts) >= 3 and
                    parts[1] in {str(n) for n in degrees}, 'unregistered job directory')
            if len(parts) == 3:
                require(parts[2] in {'admitted.json', 'attempt.json', 'wrapper-exit.json',
                        'produce-exit.json', 'verify-exit.json', 'produce.stdout', 'produce.stderr',
                        'verify.stdout', 'verify.stderr'}, 'unregistered case member')
            else:
                require(parts[2] in ('produce', 'verify'), 'unregistered pass directory')
                require(not any(p.startswith('check-') for p in parts[3:]) or
                        int(parts[1]) in selected, 'unsampled native history')
                if len(parts) == 4:
                    require(parts[3] in pass_files, 'unregistered pass member')
                    if parts[3] == 'storage-dedup.json':
                        receipt = strict(payload[name])
                        counts = ('immutable_paths_examined', 'paths_relinked', 'logical_bytes_relinked')
                        require(type(receipt) is dict and set(receipt) == {*counts, 'scope'},
                                'storage dedup receipt schema')
                        require(all(type(receipt[key]) is int and receipt[key] >= 0 for key in counts),
                                'storage dedup nonnegative integer counts')
                        require(receipt['paths_relinked'] <= receipt['immutable_paths_examined'] and
                                (receipt['paths_relinked'] != 0 or receipt['logical_bytes_relinked'] == 0),
                                'storage dedup consistent counts')
                        require(receipt['scope'] == 'identical bytes and paths retained; logs/JSON untouched',
                                'storage dedup scope')
                if len(parts) > 4:
                    require(int(parts[1]) in selected and parts[3].startswith('check-'),
                            'unregistered nested pass member')


def verify(archive, expected_archive_sha=CANONICAL_ARCHIVE_SHA):
    require(R.identity(archive)['sha256'] == expected_archive_sha, 'external archive SHA256')
    payload={}; total=0
    with zipfile.ZipFile(archive,'r') as bundle:
        for member in bundle.infolist():
            name=member.filename; path=Path(name)
            require(not path.is_absolute() and '..' not in path.parts and path.as_posix()==name and name not in payload, "required: not path.is_absolute() and '..' not in path.parts and path.as_posix()==name and name not in payload")
            require(len(payload)<200000 and member.file_size<=512*1024**2, 'required: len(payload)<200000 and member.file_size<=512*1024**2')
            require(not member.is_dir(), 'required: not member.is_dir()'); total+=member.file_size; require(total<=2*1024**3, 'required: total<=2*1024**3')
            data=bundle.read(member)
            payload[name]=data
    inventory=strict(payload.pop('COMPACT.json'))
    require(set(inventory['files'])==set(payload), "required: set(inventory['files'])==set(payload)")
    for name,row in inventory['files'].items(): require(row=={'bytes':len(payload[name]),'sha256':sha(payload[name])}, "required: row=={'bytes':len(payload[name]),'sha256':sha(payload[name])}")
    require(R.identity(R.RELEASE/'runtime_manifest.json')['sha256'] == MANIFEST_SHA, 'external trusted manifest SHA256')
    trusted=R.read(R.RELEASE/'runtime_manifest.json')['files']
    require(not set(payload)&set(trusted), 'archive shadows trusted package')
    require(same_bytes(R.identity(R.RELEASE/'runtime_manifest.json'),inventory['trusted_manifest']), "required: same_bytes(R.identity(R.RELEASE/'runtime_manifest.json'),inventory['trusted_manifest'])")
    require(payload['TRUSTED_RUNTIME_MANIFEST.json']==(R.RELEASE/'runtime_manifest.json').read_bytes(), "required: payload['TRUSTED_RUNTIME_MANIFEST.json']==(R.RELEASE/'runtime_manifest.json').read_bytes()")
    require(payload['TRUSTED_ASSET_PROVENANCE.json']==(R.RELEASE/'asset_provenance.json').read_bytes(), "required: payload['TRUSTED_ASSET_PROVENANCE.json']==(R.RELEASE/'asset_provenance.json').read_bytes()")
    def reader(name):
        if name in trusted:
            path=R.ROOT/name
            if name=='asset_provenance.json':path=R.RELEASE/name
            data=path.read_bytes(); row=trusted[name]
            require(len(data)==row['bytes'] and sha(data)==row['sha256'], "required: len(data)==row['bytes'] and sha(data)==row['sha256']")
            return data
        return payload[name]
    reader('asset_provenance.json')
    # Authenticate all checker/source/arithmetic bytes before Access imports checker.py.
    local_pins=R.pins()
    class CheckedAccess(Access):
        def json(self, name):
            return strict(self.data(name))
    access=CheckedAccess(R.ROOT,inventory['root'],read_bytes=reader)
    prefix=inventory['output']; reg=strict(payload[prefix+'/preregistration.json'])
    require(reg['degrees']==inventory['degrees']==list(range(320,511)), "required: reg['degrees']==inventory['degrees']==list(range(320,511))")
    require(reg['runner']['sha256'] == CAMPAIGN_RUNNER_SHA, 'preregistered campaign runner')
    require(reg['pins']['source']==local_pins['source'] and reg['pins']['arithmetic_files']==local_pins['arithmetic_files'], "required: reg['pins']['source']==local_pins['source'] and reg['pins']['arithmetic_files']==local_pins['arithmetic_files']")
    for key in ('freeze','asset_provenance'):require(same_bytes(reg['pins'][key],local_pins[key]), "required: same_bytes(reg['pins'][key],local_pins[key])")
    selection=inventory['selection']; require(selection['eligible']==reg['degrees'], "required: selection['eligible']==reg['degrees']")
    require(selection==access.json(prefix+'/compact-selection.json'), "required: selection==access.json(prefix+'/compact-selection.json')")
    prereg_data=payload[prefix+'/preregistration.json']
    prereg_identity={'path':inventory['root']+'/'+prefix+'/preregistration.json','bytes':len(prereg_data),'sha256':sha(prereg_data)}
    require(selection['preregistration']==prereg_identity, "required: selection['preregistration']==prereg_identity")
    require(selection['selected']==random.Random(bytes.fromhex(selection['seed_hex'])).sample(reg['degrees'],2), "required: selection['selected']==random.Random(bytes.fromhex(selection['seed_hex'])).sample(reg['degrees'],2)")
    helpers=access.json(prefix+'/helper-source-pins.json')['files']
    check_members(payload, prefix, reg['degrees'], selection['selected'], helpers)
    checked_proofs=0; checked_pairs=0
    for n in reg['degrees']:
        case=prefix+'/jobs/'+str(n); proofs=[]
        for mode in ('produce','verify'):
            target=case+'/'+mode
            proof=access.json(target+'/essential-receipt.json');proofs.append(proof)
            checked_proofs += 1
            require(proof['n']==n and proof['freeze']==reg['pins']['freeze'], "required: proof['n']==n and proof['freeze']==reg['pins']['freeze']")
            require(access.checker.verify_essential(proof,proof['freeze'])==proof['verification'], "required: access.checker.verify_essential(proof,proof['freeze'])==proof['verification']")
            ex=access.json(case+'/'+mode+'-exit.json');exit0(ex);require(ex['observed_returncode']==0 and ex['ECHILD'] is True and ex['timeout'] is False and ex['cleanup_killed'] == [], "required: ex['observed_returncode']==0 and ex['ECHILD'] is True and ex['timeout'] is False and ex['cleanup_killed'] == []")
            account=access.json(target+'/final-accounting.json'); require(account['complete'] is True and account['first_failure'] is None and account['hard_aggregate_cap']==120, "required: account['complete'] is True and account['first_failure'] is None and account['hard_aggregate_cap']==120")
            summary=access.json(target+'/summary.json')
            require(summary['result']=='PROVISIONAL_PROOF_PENDING_FINAL_ACCOUNTING' and summary['first_failure'] is None, "required: summary['result']=='PROVISIONAL_PROOF_PENDING_FINAL_ACCOUNTING' and summary['first_failure'] is None")
            require(account['engine_config']==summary['engine_config'] and account['engine_config']['n']==n and account['engine_config']['mode']==mode, "required: account['engine_config']==summary['engine_config'] and account['engine_config']['n']==n and account['engine_config']['mode']==mode")
            require(account['result']==LABELS[mode], "required: account['result']==LABELS[mode]")
            require(0<=account['total_CPU_through_summary']<120, "required: 0<=account['total_CPU_through_summary']<120")
            limit=account['final_self_limit'];require(limit['no_live_children'] is True and limit['waited_child_CPU']+limit['absolute_self_CPU_hard']<=119, "required: limit['no_live_children'] is True and limit['waited_child_CPU']+limit['absolute_self_CPU_hard']<=119")
            raw=payload[target+'/raw-evidence.json'];require(same_bytes(proof['whole_raw_evidence'],{'bytes':len(raw),'sha256':sha(raw)}), "required: same_bytes(proof['whole_raw_evidence'],{'bytes':len(raw),'sha256':sha(raw)})")
            raw_doc=strict(raw);require(reg['python'] in raw_doc['runtime_before']['all_file_mappings'], "required: reg['python'] in raw_doc['runtime_before']['all_file_mappings']")
            require(proof['CPU_stages'] == summary['stages'], 'proof stage linkage')
            require(proof['whole_raw_evidence']==summary['whole_raw_evidence'], "required: proof['whole_raw_evidence']==summary['whole_raw_evidence']")
            proof_data=payload[target+'/essential-receipt.json']
            require(summary['essential_receipt'] == {'path':inventory['root']+'/'+target+'/essential-receipt.json', 'bytes':len(proof_data), 'sha256':sha(proof_data)}, 'summary receipt identity')
            registration=access.json(target+'/preregistration.json')
            require(registration['engine_config'] == account['engine_config'] and registration['freeze'] == proof['freeze'] == summary['freeze'], 'pass preregistered inputs')
            config=account['engine_config'];require(config['output']==inventory['root']+'/'+target, "required: config['output']==inventory['root']+'/'+target")
            primary_path=inventory['root']+'/'+case+'/produce/essential-receipt.json'
            if mode == 'produce':
                require(config['certificate'] is None and config['certificate_identity'] is None, 'fresh primary')
            else:
                primary=payload[case+'/produce/essential-receipt.json']
                require(config['certificate'] == primary_path and config['certificate_identity'] == {'path':primary_path, 'bytes':len(primary), 'sha256':sha(primary)}, 'fresh input primary linkage')
            python_invocation=access.json(prefix+'/return-provenance.json')['python_invocation']
            command=[python_invocation,'-E','-S','-B',inventory['root']+'/topics/padua-argmax-bridge-20261105/code/final_hybrid_engine/engine.py','--mode',mode,'--n',str(n),'--output',config['output'],'--run-once']
            if mode=='verify':command+=['--certificate',inventory['root']+'/'+case+'/produce/essential-receipt.json']
            require(ex['command']==command, "required: ex['command']==command")
            validation=access.json(target+'/local-validation.json')
            for key,filename in [('receipt','essential-receipt.json'),('raw','raw-evidence.json')]:
                data=payload[target+'/'+filename];row=validation[key];require(row['bytes']==len(data) and row['sha256']==sha(data), "required: row['bytes']==len(data) and row['sha256']==sha(data)")
            if n in selection['selected']:validate_pass(access,target,n,mode,{'files':trusted})
        require(all(proofs[0][key]==proofs[1][key] for key in COMPARE), 'required: all(proofs[0][key]==proofs[1][key] for key in COMPARE)')
        require(payload[case+'/produce/essential-receipt.json']==payload[case+'/verify/original-certificate.json'], "required: payload[case+'/produce/essential-receipt.json']==payload[case+'/verify/original-certificate.json']")
        checked_pairs += 1
        attempt=access.json(case+'/attempt.json');
        require(attempt['status'] == 'awaits_independent_result_review', 'completed attempt status')
        require(attempt['failure'] is None and attempt['ECHILD'] is True and attempt['cleanup_killed'] == [], "required: attempt['failure'] is None and attempt['ECHILD'] is True and attempt['cleanup_killed'] == []")
        require(attempt['n']==n and attempt['terminal'] is True and attempt['passes']==[access.json(case+'/'+mode+'-exit.json') for mode in ('produce','verify')], "required: attempt['n']==n and attempt['terminal'] is True and attempt['passes']==[access.json(case+'/'+mode+'-exit.json') for mode in ('produce','verify')]")
        admission=access.json(case+'/admitted.json');require(admission['n']==n, "required: admission['n']==n")
        require(admission['preregistration']==prereg_identity, "required: admission['preregistration']==prereg_identity")
        wrapper=access.json(case+'/wrapper-exit.json');exit0(wrapper);require(wrapper['observed_returncode']==0, "required: wrapper['observed_returncode']==0")
    for stage,degrees in [('pilot',[320]),('remaining',list(range(321,511)))]:
        admission=access.json(prefix+'/'+stage+'-admitted.json');require(admission['degrees']==degrees, "required: admission['degrees']==degrees")
        require(admission['preregistration']==prereg_identity, "required: admission['preregistration']==prereg_identity")
        summary=access.json(prefix+'/'+stage+'-summary.json')
        require(summary['ECHILD'] is True and summary['quiescent'] is True and summary['failed'] is False and summary['unstarted'] == [] and summary['cleanup_killed'] == [], "required: summary['ECHILD'] is True and summary['quiescent'] is True and summary['failed'] is False and summary['unstarted'] == [] and summary['cleanup_killed'] == []")
        require(sorted(row['n'] for row in summary['results'])==degrees, "required: sorted(row['n'] for row in summary['results'])==degrees")
        for row in summary['results']:require(row==access.json(prefix+'/jobs/'+str(row['n'])+'/wrapper-exit.json'), "required: row==access.json(prefix+'/jobs/'+str(row['n'])+'/wrapper-exit.json')")
    helpers=access.json(prefix+'/helper-source-pins.json')['files']
    for row in helpers:
        data=payload[prefix+'/helper-source/'+Path(row['path']).name]
        require(row['input_head_equal'] is True and row['bytes']==len(data) and row['sha256']==sha(data), "required: row['input_head_equal'] is True and row['bytes']==len(data) and row['sha256']==sha(data)")
    evidence_pin=next(row for row in helpers if Path(row['path']).name=='evidence.py')
    require(same_bytes(evidence_pin,reg['compact_evidence']), "required: same_bytes(evidence_pin,reg['compact_evidence'])")
    print(json.dumps({'status':'accepted_pending_independent_review','pairs':checked_pairs,'proofs':checked_proofs,'reader':R.identity(__file__),'sample':selection['selected'],'archive':R.identity(archive)}))

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('action',choices=['export','verify']);ap.add_argument('archive',type=Path);ap.add_argument('--output',type=Path);ap.add_argument('--archive-sha',default=CANONICAL_ARCHIVE_SHA,help='external SHA256 pin (defaults to canonical historical return)')
    args=ap.parse_args()
    if args.action=='export':export(args.output.resolve(),args.archive.resolve())
    else:verify(args.archive.resolve(),args.archive_sha)
