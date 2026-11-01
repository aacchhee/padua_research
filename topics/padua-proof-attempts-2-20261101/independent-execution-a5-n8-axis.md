# Actual independent n=8 axis preflight replay

Date: 2026-11-01. Executor: Codex subagent `/root/input_manifest`, separately
assigned mechanical replay, requested gpt-6.1-sol medium. Serving-model metadata
is not separately exposed. This is supplementary independent execution, not the
required Claude audit or a mathematical audit of theory 63.

Read the complete `independent-checks-a5-n8-axis.md` and its entire literal
executed command. Ran that exact frozen inline command in a fresh process,
changing only the output filename from
`outputs/a5_checker_n8_axis_preflight.json` to
`outputs/a5_independent_n8_axis_preflight.json`. The command was extracted from
its single bash block, the one literal replacement was asserted and reversed
to check identity, and `bash -c` executed the resulting block from
`/workspace/padua_research`. Actual inner command and wrapper both exited 0.
No search, subdivision, root isolation, source/proof/manifest edit, Git action,
or n=7 file change was performed.

## Frozen inputs and environment

- Supplied candidate: `/tmp/a5-n8-candidate-v4.json.gz`, 370875 bytes, SHA-256
  `4d0884a64cf6b41c7e9b6fadb7da56bed61a4c44e816b215a8e7ce37fdc0647c`.
- Main checker before/import/after:
  `a9cff5748d6c40ee41ac76e4e8a0035e0d5dab95f4de1233dfcc26902cb085a2`.
- Controls before/after:
  `7f57ed9ba5ad864391aa2e309834d9b61c33f673a6854247d44594cb10ec71d2`.

All literal source/input guards passed. The two source hashes were additionally
read after the actual process exit and still matched. Actual output records
Python 3.12.14, SymPy 1.14.0, python-flint 0.9.0 / FLINT 3.6.0 and 160-bit outward
dyadics. The requested FLINT dependency path was supplied in the literal
command below. No random seed or floating proof predicate applies.

## Actual result and equality check

The independent execution recorded 8.9753372640007 seconds. It freshly
reconstructed the formal field/principal embedding and cardinal system, then
verified all 23 supplied original root records and all 45 exact node and 45 full
coefficient cardinal reflection identities. The exact rectangle inventory is
20 strictly left, zero strictly right and 3 touching/crossing the axis.

For IDs 9, 10, 21, all three reflected-root predicates, exact same-mask identities
and same-original-C injectivity tests on the full convex rectangular hull
passed. R9 is exactly reflection invariant; R10 and R21 are not, and their
nontrivial hull tests were actually executed. Every outward q bound is at most
1/1000000, strictly below1. The output preserves both row bounds, exact q,
original/reflected R, original/reflected C and each hull.

Parsed JSON was compared to the original checker output after removing ONLY
`seconds` from each object. All remaining fields are exactly equal, including
versions, source/input hashes and all rational q/R/C/hull data. The original
run recorded 6.987978730001487 seconds; no other field was dropped or normalized.

Independent output: `outputs/a5_independent_n8_axis_preflight.json`,
24613 bytes, SHA-256 `a1b210518708eeec30c06b1a214e9da201298d7e4ea5b53aed167c9dfbe859f3`.
The complete source receipt read above has SHA-256
`52a651a62619c9c4da5649724e9bbf477081c5e40645eb05dd8ccb352764cdba`.
The exact executed inline block below, after the sole filename replacement,
has UTF-8 SHA-256 `4e32bc583b052cab42f9bb136ba0bb86d9cc15580392c8dc97df122e7cf346e2`.

## Literal command actually executed

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/padua2-deps python -B - <<'PY'
import sys,json,hashlib,time
from fractions import Fraction
from pathlib import Path
started=time.monotonic()
base=Path('/workspace/padua_research/topics/padua-proof-attempts-2-20261101')
source=base/'code/a5_checker_n8.py';control=base/'code/a5_checker_n8_controls.py'
before=hashlib.sha256(source.read_bytes()).hexdigest();control_before=hashlib.sha256(control.read_bytes()).hexdigest()
assert before=='a9cff5748d6c40ee41ac76e4e8a0035e0d5dab95f4de1233dfcc26902cb085a2'
assert control_before=='7f57ed9ba5ad864391aa2e309834d9b61c33f673a6854247d44594cb10ec71d2'
sys.path.insert(0,str(base/'code'))
import a5_checker_n8 as check
artifact=Path('/tmp/a5-n8-candidate-v4.json.gz');raw=artifact.read_bytes()
check.require(len(raw)==370875 and hashlib.sha256(raw).hexdigest()=='4d0884a64cf6b41c7e9b6fadb7da56bed61a4c44e816b215a8e7ce37fdc0647c','wrong actual V4 input')
data=json.loads(check.decode_payload(raw),object_pairs_hook=check.unique_object)
v=check.Verifier(data['field_embedding'])
labels=[(j,k)for j in range(9)for k in range(10)if(j+k)%2==0]
permutation=[labels.index((8-j,k))for j,k in labels]
check.require(sorted(permutation)==list(range(45))and all(permutation[permutation[i]]==i for i in range(45)),'node permutation not involutive bijection')
for i,j in enumerate(permutation):
    check.require(v.nodes[j][0]==-v.nodes[i][0] and v.nodes[j][1]==v.nodes[i][1],'exact node identity failed')
    reflected=check.sp.Poly.from_dict({(a,b):(-c if a%2 else c)for(a,b),c in v.cardinals[i].rep.to_dict().items()},check.x,check.y,domain=check.FIELD)
    check.require(reflected==v.cardinals[j],'exact full cardinal identity failed')
for row in data['interior_roots']:
    v.root(row)
axis=[];inventory=[]
for row in data['interior_roots']:
    low,high=v.roots[row['id']]['bounds'][0]
    region='strict_left'if high<0 else'strict_right'if low>0 else'sects_axis'
    inventory.append({'id':row['id'],'R':row['R'],'region':region})
    if region=='sects_axis':axis.append(row)
refv=check.Verifier(data['field_embedding'])
results=[]
for row in axis:
    root=v.roots[row['id']];bounds=root['bounds'];low,high=bounds[0]
    permuted_mask=sum(1<<permutation[i]for i in range(45)if row['mask']&(1<<i))
    rbounds=((-high,-low),bounds[1]);hull=((min(low,-high),max(high,-low)),bounds[1])
    d=(-1,1);cm=tuple(tuple(map(check.rational,r))for r in row['C'])
    candidate={'id':row['id'],'mask':permuted_mask,'R':[[str(a),str(b)]for a,b in rbounds],'C':[[str(d[i]*d[j]*cm[i][j])for j in range(2)]for i in range(2)]}
    entry={'id':row['id'],'mask':row['mask'],'reflected_mask':permuted_mask,'same_mask':permuted_mask==row['mask'],'R':row['R'],'reflected_R':candidate['R'],'R_exactly_reflection_invariant':bounds==rbounds,'C':row['C'],'reflected_C':candidate['C'],'hull':[[str(a),str(b)]for a,b in hull]}
    try:
        refv.root(candidate);entry['reflected_original_root_predicates_passed']=True
    except check.Rejected as error:
        entry['reflected_original_root_predicates_passed']=False;entry['reflected_root_failure']=str(error)
    try:
        error=v.injection(row['mask'],root['C'],tuple(check.Interval.bounds(a,b)for a,b in hull))
        norms=[Fraction(sum(max(abs(z.lo),abs(z.hi))for z in r),check.UNIT)for r in error]
        entry['same_actual_C_hull_injection_passed']=True
        entry['row_norm_upper']=list(map(str,norms));q=max(norms)
        entry['norm_upper']=str(q)
        coarse=Fraction(-((-q.numerator*1000000)//q.denominator),1000000)
        entry['norm_upper_rounded_outward']=str(coarse)
    except check.Rejected as error:
        entry['same_actual_C_hull_injection_passed']=False;entry['injection_failure']=str(error)
    entry['axis_equality_conditions_verified']=entry['same_mask'] and entry['reflected_original_root_predicates_passed'] and entry['same_actual_C_hull_injection_passed']
    results.append(entry)
after=hashlib.sha256(source.read_bytes()).hexdigest();control_after=hashlib.sha256(control.read_bytes()).hexdigest()
check.require(before==check.SOURCE_SHA_AT_IMPORT==after and control_before==control_after,'source changed during axis preflight')
result={'format':'a5-checker-n8-axis-preflight-v1','scope':'fresh supplied-root verification and exact same-mask reflection-hull uniqueness conditions; no full tree, boundary or maxima count acceptance','count_certified':False,'field_embedding_verified':v.embedding_result,'exact_node_reflection_identities':45,'exact_cardinal_reflection_identities':45,'permutation_involutive_bijective':True,'verified_original_root_records':len(v.roots),'root_rectangle_inventory':inventory,'root_rectangle_regions':{key:sum(r['region']==key for r in inventory)for key in('strict_left','strict_right','sects_axis')},'axis_records':results,'axis_root_ids':[r['id']for r in results],'all_axis_equality_conditions_verified':all(r['axis_equality_conditions_verified']for r in results),'reflected_root_records_verified':len(refv.roots),'input_path':str(artifact),'input_sha256':hashlib.sha256(raw).hexdigest(),'input_bytes':len(raw),'checker_sha256':before,'checker_sha256_after':after,'controls_sha256':control_before,'controls_sha256_after':control_after,'sources_unchanged':True,'precision':check.PRECISION,'python':check.platform.python_version(),'sympy':check.sp.__version__,'python_flint':check.flint.__version__,'FLINT':check.flint.__FLINT_VERSION__,'seconds':time.monotonic()-started}
out=base/'outputs/a5_independent_n8_axis_preflight.json';out.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
print(json.dumps({'original_roots':len(v.roots),'regions':result['root_rectangle_regions'],'axis':[{k:r[k]for k in('id','same_mask','R_exactly_reflection_invariant','reflected_original_root_predicates_passed','same_actual_C_hull_injection_passed','norm_upper_rounded_outward','axis_equality_conditions_verified')}for r in results],'sources_unchanged':True,'seconds':result['seconds'],'count_certified':False},sort_keys=True),flush=True)
PY
```

## Scope limits

The output explicitly has `count_certified: false`. It does not accept a full
partition, complete cone set, edge/corner census, total maxima count or global
maximum. The input spatial search is incomplete. These are 23 supplied root
witnesses and 3 exact axis-uniqueness condition checks, not an exhaustive list.
Every later mirrored leaf/reference must still satisfy the unchanged whole-hull
injectivity test using the selected stored root and its actual C, and must
cover every compatible mask. This replay neither introduces a new predicate
nor upgrades any mathematical theory status. N8 count/global targets and the
required Claude audit remain separate and OPEN/pending respectively.
