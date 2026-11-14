#!/usr/bin/env python3
"""Collect full-run closure and frozen candidate identities, without arithmetic."""
import hashlib
import json
from pathlib import Path
from n3_native_receipt import identity

ROOT=Path(__file__).resolve().parents[3]
TOPIC=Path(__file__).resolve().parents[1]
OUT=ROOT/'local-output/argmax-bridge-20261105/N3/outward-full-n17-r3'

def verify(item):
    p=Path(item['path']);p=p if p.is_absolute() else ROOT/p
    raw=p.read_bytes()
    assert len(raw)==item['bytes'] and hashlib.sha256(raw).hexdigest()==item['sha256'],item['path']

def main():
    producer=json.loads((OUT/'n17-producer-receipt.json').read_text())
    projection=json.loads((OUT/'compact-receipt.json').read_text())
    manifest_path=OUT/'build/build-manifest.json';raw_manifest=manifest_path.read_bytes()
    manifest=json.loads(raw_manifest)
    records=manifest['dependencies']+manifest['linked_runtimes']+manifest['snapshots']+[manifest['compiler']]
    for item in records:verify(item)
    for item in producer['original_sources_before_and_after']:verify(item)
    for key in ['candidate','compressed_candidate','build_manifest','binary_before_and_after']:verify(producer[key])
    for key in ['original_candidate','compact_candidate','compressed_compact']:verify(projection[key])
    assert producer['complete'] is True and producer['accepted'] is False and producer['pending']==0
    preserved=TOPIC/'evidence/n3-full-n17-build.json'
    assert len(raw_manifest)<16384
    preserved.write_bytes(raw_manifest)
    receipt={'status':'Complete outward producer candidate; independent whole-tree replay and source review own acceptance',
             'rules_input':'c000899f3fb10d6ba0f1725341a045fe11ec943a',
             'command':'python topics/padua-argmax-bridge-20261105/code/n3_outward_full.py --degrees 17 --seconds 600 --work local-output/argmax-bridge-20261105/N3/outward-full-n17-r3 --execute',
             'collector_command':'python topics/padua-argmax-bridge-20261105/code/n3_full_receipt.py',
             'collector_source':identity(Path(__file__).resolve()),
             'producer_receipt':identity(OUT/'n17-producer-receipt.json'),
             'producer_original_statistics':producer['statistics'],'corner_patch':producer['corner_patch'],
             'original_candidate':producer['candidate'],'original_gzip':producer['compressed_candidate'],
             'compact_projection':projection,'projection_source':identity(TOPIC/'code/n3_compact_candidate.py'),
             'projection_identity_helper':identity(TOPIC/'code/n3_native_receipt.py'),
             'build_manifest_original':identity(manifest_path),'build_manifest_preserved':identity(preserved),
             'closure_after_run':{'verified_file_identities':len(records),'all_match':True,
                                  'loaded_binary':producer['binary_before_and_after'],
                                  'scope':'Compiler, actual discovered headers, snapshot sources and linked runtime files; checked against pre-run manifest.'},
             'complete':True,'accepted_by_producer':False,
             'limits':['Only overlap n17; no extension of the accepted finite range.',
                       'Compact candidate omits only numeric leaf diagnostics ignored by the independent checker; it requires its own exact-byte replay.',
                       'Full original diagnostics remain local; essential compact gzip and manifest fit individual evidence size limits.',
                       'The independent checker and mathematical/source review must accept before proof promotion.']}
    text=json.dumps(receipt,indent=2)+'\n';assert len(text.encode())<16384
    (TOPIC/'evidence/n3-full-n17-producer.json').write_text(text)
    print(json.dumps({'closure_identities_checked':len(records),'receipt_bytes':len(text),'manifest_bytes':len(raw_manifest)}))

if __name__=='__main__':main()
