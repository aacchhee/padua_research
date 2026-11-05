"""Adversarial controls: all historical defects plus strict parser cases."""
import argparse
import copy
import json
from pathlib import Path
import subprocess
import time
import check as c


def controls(data, binary):
    started = time.monotonic()
    cache = {}
    rejected = []
    c.need(c.check(data, binary, cache)['accepted'], 'positive complete')
    bound = next(i for i,r in enumerate(data['leaves']) if r['kind']=='bound')
    corner = next(i for i,r in enumerate(data['leaves']) if r['kind']=='corner')
    def reject(name, mutate):
        d = copy.deepcopy(data)
        mutate(d)
        try:
            c.check(d, binary, cache)
        except (ValueError, KeyError, TypeError, subprocess.CalledProcessError):
            rejected.append(name)
        else:
            raise RuntimeError('defect accepted: '+name)
    cases = [
      ('missing_leaf', lambda d:d['leaves'].pop(bound)),
      ('duplicate_leaf', lambda d:d['leaves'].append(copy.deepcopy(d['leaves'][bound]))),
      ('forged_bound', lambda d:d['leaves'][bound].update(upper=0)),
      ('forged_corner', lambda d:d['leaves'][corner].update(corner=[1,1])),
      ('changed_threshold', lambda d:d['threshold_interval'].__setitem__(0,1)),
      ('changed_pi_bracket', lambda d:d['pi_interval'].__setitem__(0,'3')),
      ('changed_source', lambda d:d['source_sha256'].update({'finite_general.py':'0'*64})),
      ('changed_dependency', lambda d:d.update(dependency_sha256='0'*64)),
      ('false_complete_flag', lambda d:d.update(complete=False)),
      ('producer_self_approval', lambda d:d.update(accepted=True)),
      ('pending_leaf_overlap', lambda d:d['pending'].append(d['leaves'][bound]['path'])),
      ('ancestor_overlap', lambda d:d['pending'].append('')),
      ('invalid_path_character', lambda d:d['leaves'][bound].update(path='X')),
      ('wrong_counter', lambda d:d['statistics'].update(bound=-1)),
      ('boolean_degree', lambda d:d.update(n=True)),
      ('float_degree', lambda d:d.update(n=float(d['n']))),
      ('degree_too_small', lambda d:d.update(n=1)),
      ('degree_too_large', lambda d:d.update(n=101)),
      ('oversize_path', lambda d:d['leaves'][bound].update(path='0'*101)),
      ('nonstring_path', lambda d:d['leaves'][bound].update(path=0)),
      ('null_leaf', lambda d:d['leaves'].__setitem__(bound,None)),
      ('missing_threshold', lambda d:d.pop('threshold_interval')),
      ('boolean_complete', lambda d:d.update(complete=1)),
      ('boolean_counter', lambda d:d['statistics'].update(bound=True)),
      ('string_bound', lambda d:d['leaves'][bound].update(upper='1')),
      ('extra_leaf_field', lambda d:d['leaves'][bound].update(extra=1)),
      ('duplicate_pending', lambda d:d['pending'].extend(['0','0'])),
      ('empty_frontier', lambda d:d.update(leaves=[],pending=[])),
    ]
    for name, mutate in cases:
        reject(name,mutate)
    partial = copy.deepcopy(data)
    row = partial['leaves'].pop(bound)
    partial['pending'].append(row['path'])
    partial['statistics']['bound']-=1
    partial['complete']=False
    result = c.check(partial,binary,cache)
    c.need(not result['accepted'] and result['all_supplied_bounds_verified'], 'partial positive')
    # JSON lexical controls exercise the actual file parser rather than check().
    import tempfile
    for name,payload in [('duplicate_json_key','{"n":9,"n":10}'),
                         ('nonfinite_json','{"n":NaN}'),
                         ('truncated_json','{"n":')]:
        with tempfile.NamedTemporaryFile(mode='w',suffix='.json') as f:
            f.write(payload); f.flush()
            try:
                c.load(f.name)
            except ValueError:
                rejected.append(name)
            else:
                raise RuntimeError('parser defect accepted: '+name)
    # Exercise compiled protocol validation independently of the Python guard.
    for name, payload in [('native_invalid_path','X\n'),('native_duplicate_path','0\n0\n'),
                          ('native_prefix_overlap','-\n0\n'),('native_uncovered','0\n'),
                          ('native_empty_frontier','')]:
        p = subprocess.run([str(binary),str(data['n'])],input=payload,text=True,capture_output=True)
        c.need(p.returncode!=0, name)
        rejected.append(name)
    return dict(format='padua-native-independent-controls-v1',n=data['n'],
                negative_cases_rejected=rejected,negative_count=len(rejected),
                positive_complete_accepted=True,positive_partial_not_accepted=True,
                certificate_arithmetic_reused_only_with_identical_degree_and_frontier=True,
                seconds=time.monotonic()-started)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('certificate',type=Path);p.add_argument('--binary',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    result=controls(c.load(a.certificate),a.binary)
    result.update(certificate_sha256=c.digest(a.certificate),checker_sha256=c.digest(Path(c.__file__)),
                  kernel_sha256=c.digest(Path(__file__).with_name('kernel.cpp')),
                  controls_sha256=c.digest(__file__),binary_sha256=c.digest(a.binary))
    a.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print(json.dumps(result,sort_keys=True))
