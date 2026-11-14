"""Prepare explicit input/source freeze after successful new campaign; no numerical work."""
import argparse
import hashlib
import json
from pathlib import Path
from runtime_identity import identity

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--additional-dir',required=True)
    p.add_argument('--output',required=True)
    args=p.parse_args()
    root=Path(args.additional_dir)
    inventory=root.with_name(root.name+'-inventory.json')
    code=Path(__file__).parent
    core=code.parent/'independent_phase_checker'
    sources=[core/'check.py',core/'controls.py',core/'runtime_probe.py',core/'accept_controls.py',code/'worker.py',code/'launch.py',code/'freeze.py',code/'runtime_identity.py',code/'records.py',code.parent.parent/'compact_pack/process_guard.py']
    freeze={'runtime':identity(),'additional_dir':str(root),'inventory':str(inventory),'inventory_sha256':sha(inventory),
            'sources':{str(q):sha(q) for q in sources},
            'old_archive_sha256':'b00fd57f85ce6d96a6c1fa01e2307abd815088bb8fcb28b1587657ef142b109a'}
    with Path(args.output).open('x') as f: json.dump(freeze,f,indent=2); f.write('\n')
    print(json.dumps(freeze,indent=2))
if __name__=='__main__': main()
