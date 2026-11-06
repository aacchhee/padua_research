#!/usr/bin/env python3
"""Validate retained completed reflection outputs after interrupted harvesting.

No native process is launched. The interrupted receipt stays byte-identical.
Missing harness timings are never reconstructed from rounded native timers.
"""
import argparse
import copy
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from p6_reflection_full import identity, checked_rows, guards
from p6_rows import compare

sys.set_int_max_str_digits(1000000)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--interrupted-receipt', type=Path, required=True)
    parser.add_argument('--work-dir', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--parent-pid', type=int, default=9089)
    args = parser.parse_args()
    original = identity(args.interrupted_receipt)
    result = copy.deepcopy(json.loads(args.interrupted_receipt.read_text()))
    assert result['family'] == 'D36x9' and result['max_degree'] == 16
    assert result['status'] == 'INCOMPLETE' and len(result['runs']) == 7
    proc = Path(f'/proc/{args.parent_pid}/stat')
    observation = {'pid': args.parent_pid, 'observed_utc': datetime.now(timezone.utc).isoformat()}
    if proc.exists():
        fields = proc.read_text().rsplit(')', 1)[1].split()
        assert fields[0] == 'Z', 'original parent must have closed'
        observation.update(state='Z zombie; execution closed', linux_wait_status=int(fields[49]))
    else:
        observation['state'] = 'absent at recovery'
    assert not Path('/proc/9102').exists(), 'original PIVOT native must have closed'
    assert identity(result['runs'][0]['command'][1])['sha256'] == result['input']['native_input_sha256']
    for key in ('harness', 'row_guard', 'reflection_binary', 'producer_bundle'):
        record = result[key]
        assert identity(record['path']) == record
    for record in result['source_catalog'].values():
        assert identity(record['path']) == record
    rows = {}
    for record in result['runs']:
        assert record['status'].startswith('PASS')
        key = record['backend'], record['rule']
        assert key not in rows
        rows[key] = checked_rows(record, 'D36x9', 324)
        assert identity(record['log']['path']) == record['log']
        if 'source' in record:
            source = record.pop('source')
            assert identity(source['path']) == source
            result['source_catalog'][record['source_sha256']] = source
    assert ('checker', 'pivot') not in rows
    assert (result['runs'][-1]['backend'], result['runs'][-1]['rule']) == ('checker', 'alt')
    output = args.work_dir/'checker-pivot.jsonl'
    log = args.work_dir/'checker-pivot.log'
    record = {'backend': 'checker', 'rule': 'pivot',
              'command': [str(args.work_dir/'reflection'), result['runs'][0]['command'][1], '16', 'pivot', 'D36x9'],
              'source_sha256': result['runs'][-1]['source_sha256'],
              'implementation': 'reviewed sign-reflection scalar GMP; all-node expansion',
              'status': 'PASS recovered completed output; exact full-field match', 'rows': 15,
              'output': identity(output), 'log': identity(log),
              'harness_elapsed_seconds': None,
              'timing_limit': 'Original harness wall time was not saved. Native timer is rounded and sampled before final JSON emission; it is not substituted for harness wall time.',
              'execution_origin': 'Prior worker native PID9102; retained complete files; no recovery native execution'}
    values = checked_rows(record, 'D36x9', 324)
    record['native_reported_elapsed_seconds'] = values[-1]['elapsed_seconds']
    record['reflection_guard_records'] = guards(log, 324, 'pivot')
    assert log.read_text().splitlines()[-1].startswith('phase_finish_seconds ')
    assert [line for line in log.read_text().splitlines() if line.startswith('source ')] == [f'source {h}/152' for h in range(1, 153)]
    rows['checker', 'pivot'] = values
    result['runs'].append(record)
    assert set(rows) == {(b, r) for b in ('producer', 'checker') for r in ('bj', 'mirror', 'alt', 'pivot')}
    for rule in ('bj', 'mirror', 'alt', 'pivot'):
        for a, b in zip(rows['producer', rule], rows['checker', rule]):
            compare(a, b, 'D36x9', 324)
            assert {k: v for k, v in a.items() if k != 'elapsed_seconds'} == {k: v for k, v in b.items() if k != 'elapsed_seconds'}
    for record in result['runs']:
        assert record['source_sha256'] in result['source_catalog']
    guards(result['runs'][-2]['log']['path'], 324, 'alt')
    result.update(status='PASS exact two-path weighted finite scan', exact_rows_compared=60,
                  model='P4-02 aggregate all-source spectral-normal endpoint bounds; all324nodes retained',
                  source_provenance='Per-case source_sha256 indexes source_catalog; original scalar BJ/mirror and reflection ALT/pivot',
                  interrupted_receipt=original, recovery_code=identity(__file__),
                  parent_closure_observation=observation,
                  recovery_command=[sys.executable, '-B', *sys.argv],
                  recovery_limit='The original parent closed after saving ALT, before saving PIVOT. Its exception and PIVOT harness wall timing are unavailable; no cause is asserted. Completion here is retained-file validation, not a native rerun.')
    assert identity(args.interrupted_receipt) == original
    encoded = json.dumps(result, separators=(',', ':'))+'\n'
    assert len(encoded.encode()) < 16384
    args.output.write_text(encoded)
    print(json.dumps({'status': result['status'], 'rows': 60, 'bytes': len(encoded.encode()), 'native_reruns': 0}))


if __name__ == '__main__':
    main()
