"""Fixed final Syvert2 scope; no estimate or successful degree is inferred."""
SMALL = [41, 42, 63, 64, 159, 160, 511]
LARGE = list(range(43, 63)) + list(range(65, 159)) + list(range(161, 320))
PROFILE = {'host': 'syvert2', 'workers': 40, 'worker_as_bytes': 2 * 1024**3,
           'supervisor_soft_as_bytes': 8 * 1024**3,
           'engine_inclusive_cpu_seconds': 120, 'pass_wall_seconds': 1050,
           'case_wall_seconds': 2120, 'wrapper_cpu_seconds': 260,
           'scratch_free_floor_bytes': 128 * 1024**3, 'archive_free_floor_bytes': 64 * 1024**3}
ENGINE = 'topics/padua-argmax-bridge-20261105/code/final_hybrid_engine'
ASSET = 'local-output/argmax-bridge-20261105/phase-checker/runtime/extracted/usr'
INTERFACES = ('run', 'run_small', 'run_large', 'finished_cases', 'collect_data')

def plan(group):
    assert len(SMALL) == 7 and len(LARGE) == 273
    assert not set(SMALL) & set(LARGE)
    assert set(SMALL + LARGE) == set(range(41, 320)) | {511}
    degrees = {'small': SMALL, 'large': LARGE, 'all': SMALL + LARGE}[group]
    return {'group': group, 'degrees': sorted(degrees), 'profile': PROFILE,
            'passes': ['produce', 'verify'], 'order': 'ascending degree',
            'resume': 'only absent never-started directories; no retries',
            'estimates': None, 'scope': 'prospective proof attempts, independent result audit required'}
