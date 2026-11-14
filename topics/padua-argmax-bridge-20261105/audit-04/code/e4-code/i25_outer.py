"""Outer-accounting consistency of committed I25 records only (bundle absent). Data only."""
import json, sys, hashlib
from pathlib import Path
d = Path(sys.argv[1]); R = json.loads((d/'RESULTS.json').read_text()); P = json.loads((d/'FULL-PREREGISTRATION.json').read_text())
groups = [list(range(41+j, 512, 4)) for j in range(4)]
u = [n for g in groups for n in g]
chk = {
 'group_sizes': [len(g) for g in groups], 'groups_disjoint': len(u) == len(set(u)), 'union_is_41_511': sorted(u) == list(range(41, 512)),
 'certs_eq_2x_degrees': R['full']['certificates'] == 2*R['full']['degrees'] == 942, 'old_plus_new': R['full']['old_certificates'] + R['full']['new_certificates'] == 942,
 'old_560_is_41_319_511': 2*len(list(range(41, 320)) + [511]) == 560, 'new_382_is_320_510': 2*len(range(320, 511)) == 382,
 'four_zero_exits': R['full']['worker_exits'] == [0, 0, 0, 0] and R['full']['observed_outer_exit'] == 0,
 'cpu_below_10800': R['full']['CPU_seconds_inclusive'] < P['resources']['global_CPU_seconds_cap'], 'wall_below_7200': R['full']['wall_seconds'] < P['resources']['worker_wall_timeout_seconds'],
 'S_distinct_half': R['premises']['S_checks'] == 2*R['premises']['distinct_S_keys'], 'lambda_distinct_half': R['premises']['actual_lambda_checks'] == 2*R['premises']['distinct_actual_lambda_keys'],
 'lambda_keys_3_per_degree_below_256': R['premises']['distinct_actual_lambda_keys'] == 3*len(range(41, 256)),
 'S_partition': R['premises']['old_S_uppers_proved_by_new_upper_le_old'] + R['premises']['old_S_uppers_not_proved_by_that_test'] == R['premises']['S_checks'],
 'not_proved_equals_one_per_certificate': R['premises']['old_S_uppers_not_proved_by_that_test'] == 942,
 'source_pins_equal_prereg': R['source_sha256'] == P['source_sha256'],
 'source_pins_equal_head_files': all(hashlib.sha256((d/k).read_bytes()).hexdigest() == v for k, v in R['source_sha256'].items()),
 'assignment_text_matches': 'range(41+j,512,4)' in P['assignment'] and '118/118/118/117' in P['assignment'],
}
print(json.dumps(chk, indent=1)); sys.exit(0 if all(v if isinstance(v, bool) else True for v in chk.values()) else 1)
