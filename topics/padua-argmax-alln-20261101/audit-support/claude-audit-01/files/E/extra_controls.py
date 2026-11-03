"""Additional adversarial probes of the frozen D3 checker (read-only import; no repo writes)."""
import copy, json, sys
from fractions import Fraction as F
sys.dont_write_bytecode = True
sys.path.insert(0, '/home/user/padua_research/topics/padua-argmax-alln-20261101/code/gated')
import d3_edge_check as chk
import d3_edge_common as c
data = json.load(open('/home/user/padua_research/topics/padua-argmax-alln-20261101/outputs/gated/d3_edge_certificate.json'))
res = {}
def run(label, mutation, expect_accept):
    d = copy.deepcopy(data); mutation(d)
    try:
        chk.check(d); acc = True
    except (AssertionError, KeyError, ValueError, TypeError) as e:
        acc = False
    res[label] = {'accepted': acc, 'as_expected': acc == expect_accept}
run('baseline', lambda d: None, True)
# refine leaf '0' into '00','01' with correctly recomputed bounds: a valid deeper partition
def refine(d):
    p = d['pairs'][3]; n, j, k = p['n'], p['j'], p['source']
    left, right = c.split(c.source_bernstein(n, j, k))
    ll, lr = c.split(left)
    p['leaves'] = [{'path': '00', 'upper': c.upper(ll)}, {'path': '01', 'upper': c.upper(lr)}, p['leaves'][1]]
run('valid_deeper_partition_accepted', refine, True)
def refine_missing(d):
    p = d['pairs'][3]; n, j, k = p['n'], p['j'], p['source']
    left, right = c.split(c.source_bernstein(n, j, k)); ll, lr = c.split(left)
    p['leaves'] = [{'path': '00', 'upper': c.upper(ll)}, p['leaves'][1]]
run('deeper_partition_missing_sibling', refine_missing, False)
def overlap(d):
    p = d['pairs'][3]; n, j, k = p['n'], p['j'], p['source']
    left, right = c.split(c.source_bernstein(n, j, k)); ll, lr = c.split(left)
    p['leaves'].append({'path': '00', 'upper': c.upper(ll)})
run('overlapping_leaf_ancestor_and_descendant', overlap, False)
run('root_only_leaf', lambda d: d['pairs'][0].update(leaves=[{'path': '', 'upper': max(l['upper'] for l in d['pairs'][0]['leaves'])}]), False)
run('swap_pair_order', lambda d: d['pairs'].__setitem__(slice(2, 4), [d['pairs'][3], d['pairs'][2]]), False)
run('swap_edges_n12', lambda d: d['pairs'].__setitem__(slice(2, 10), d['pairs'][6:10] + d['pairs'][2:6]), False)
run('extra_pair_appended', lambda d: d['pairs'].append(copy.deepcopy(d['pairs'][0])), False)
run('leaf_extra_key', lambda d: d['pairs'][0]['leaves'][0].update(note='x'), False)
run('pending_nonempty', lambda d: d['pairs'][0].update(pending=['10']), False)
run('target_cosine_forged', lambda d: d['pairs'][0]['target_cosine_interval'].__setitem__(0, d['pairs'][0]['target_cosine_interval'][0] - 1), False)
run('path_too_long', lambda d: d['pairs'][0]['leaves'][0].update(path='0' * 25), False)
# a genuine but non-reversed E-P sample witness must be rejected (reversal_lower <= 0)
def nonrev(d):
    w = c.witness(7, 7, 2, 4, F(1, 2)); d['ep_exact_witnesses'].append(w)
run('nonreversed_true_witness_appended', nonrev, False)
def alt_phase_repr(d):
    d['ep_exact_witnesses'][1]['phase'] = '-2/4'
run('phase_noncanonical_repr', alt_phase_repr, False)
run('precision_changed', lambda d: d.update(precision=128), False)
run('format_changed', lambda d: d.update(format='x'), False)
run('checkpoint_changed', lambda d: d.update(source_checkpoint='0' * 40), False)
run('prereg_hash_changed_ACCEPTED_informational_only', lambda d: d.update(preregistration_note_sha256='0' * 64), True)
run('cpu_seconds_changed_accepted', lambda d: d.update(cpu_seconds=-1), True)
run('only_designated_witness_kept', lambda d: d.update(ep_exact_witnesses=[w for w in d['ep_exact_witnesses'] if (w['j'], w['source'], w['phase']) == (0, 5, '-1/2')]), True)
run('extra_key_in_pair_accepted', lambda d: d['pairs'][0].update(note='x'), True)
print(json.dumps(res, indent=1))
print('ALL_AS_EXPECTED', all(v['as_expected'] for v in res.values()))
