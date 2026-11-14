"""J3-04 positive substitution controls on the authenticated old n=41 witness.

No native engine is run. Frozen checker code and archived inputs are unchanged.
"""
import copy
import hashlib
import json
from pathlib import Path
import resource
import sys
import tarfile

import check

OLD_RETURN = 'b00fd57f85ce6d96a6c1fa01e2307abd815088bb8fcb28b1587657ef142b109a'


def main():
    if sys.flags.optimize:
        raise SystemExit('optimization is not permitted')
    resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
    archive = Path(sys.argv[1])
    h = hashlib.sha256()
    with archive.open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            h.update(block)
    if h.hexdigest() != OLD_RETURN:
        raise ValueError('old return identity')
    suffix = '/jobs/41/produce/essential-receipt.json'
    proofs = []
    with tarfile.open(archive, 'r|gz') as tar:
        for member in tar:
            if member.name.endswith(suffix):
                if not member.isfile() or not 0 < member.size < 16384:
                    raise ValueError('witness member kind/size')
                proofs.append(json.loads(tar.extractfile(member).read()))
    if len(proofs) != 1:
        raise ValueError('unique n41 witness')
    base = proofs[0]
    cache = {}
    expected = check.check(base, cache)
    cases = []
    for field in ('S_upper_rows', 'lambda_upper_rows'):
        changed = copy.deepcopy(base)
        for row in changed[field]:
            row[2] = (float.fromhex(row[2]) + 1.0).hex()
        cases.append(('raise ' + field, changed))
    changed = copy.deepcopy(base)
    changed['origin_lower_hex'] = '0x0p+0'
    cases.append(('lower stored origin', changed))
    names = []
    # Endpoint-containment diagnostics may change; mathematical output must not.
    diagnostics = {'native_S_upper_contained', 'native_lower_contained'}
    for name, data in cases:
        actual = check.check(data, cache)
        if {k: v for k, v in actual.items() if k not in diagnostics} != {
                k: v for k, v in expected.items() if k not in diagnostics}:
            raise ValueError('mathematical result changed: ' + name)
        names.append(name)
    print(json.dumps({'n': 41, 'positive_controls': names,
                      'archive_sha256': OLD_RETURN,
                      'scope': 'stored endpoint substitution; one old-return tree'}, indent=2))


if __name__ == '__main__':
    main()
