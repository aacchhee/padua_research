# Independent N8 axis-root preflight

Supplementary verification record; no complete-count status or Claude audit.
Codex `/root/a5_n4_checker`, requested `gpt-6.1-sol` xhigh. Root assigned
only this new receipt and `outputs/a5_checker_n8_axis_preflight.json`.
No frozen source, producer, continuation, handoff, registry or Git mutation
was made; no search, subdivision or root isolation was run.

## Inputs and exact scope

Rules/input head `c56f3bc317c61fca4efe97d0002502ef906e22ad`; current
theory63 was read in full before execution, SHA256
`287aa76a05fad486eadc85a2abb1377b507c24ae6662cfb6fa92bb81a5446331`.
Its same-mask and convex-hull-injectivity hypotheses are applied literally.
The existing full A5 gate and reflection Candidate5 remain the scope; this
tests the already stated supporting implication and claims no novelty.

Actual supplied input `/tmp/a5-n8-candidate-v4.json.gz`,370875bytes,
SHA256 `4d0884a64cf6b41c7e9b6fadb7da56bed61a4c44e816b215a8e7ce37fdc0647c`.
Its capped spatial search is incomplete. The23 supplied root records are
data to verify, not an exhaustive count or numerical/source maximum list.

The unchanged independent verifier freshly reconstructed its formal field,
specified principal embedding,45-by45 Vandermonde inverse, all2025 cardinal
values and reproduction identities. It checked all45 exact node/reflection
identities and all45 full coefficient identities
`L_i(-x,y)=L_pi(i)(x,y)`, where pi(j,k)=(8-j,k), as in the earlier reflection
preflight. It did not import a producer or reflection helper.

## Actual observed checks

Actual exit0 in6.987978730seconds. Every one of the23 original root records
passed the frozen root predicate: Krawczyk inclusion, invertible actual C,
injectivity on R, strict cardinal signs, negative definite Hessian, open-square
containment and disjointness from all preceding original root boxes.
Exact rational rectangle inventory is20 strictly left,0 strictly right and
3 touching/crossing x=0, IDs9,10,21. The output records all23 rational R boxes.

For each of those3, the calculation permuted the exact mask, reflected R,
formed the rational matrix `D C D` with D=diag(-1,1), and checked the entire
ordinary reflected root record in a separate fresh Verifier. This avoids
trying to register two coincident roots as disjoint records in one verifier.
It then called the existing `Verifier.injection` with the SAME original
actual C on the exact convex rectangular hull `H=hull(R,T R)`.

| Original ID | Mask = reflected mask | R exactly equals T R | Reflected root predicates | Same-C injection on H |
|---|---:|---|---|---|
|9|13062369449867|yes|passed|passed|
|10|19192260774353|no|passed|passed|
|21|19990471861426|no|passed|passed|

The exact maximum row-norm bounds for `I-C Hessian(P)(H)` were:

| ID | Exact outward norm upper q |
|---|---|
|9|`36755569969410999959174941434267262946529/365375409332725729550921208179070754913983135744`|
|10|`395951703987727536951741228583463831773/45671926166590716193865151022383844364247891968`|
|21|`6905029749379531537728999285347326840885/182687704666362864775460604089535377456991567872`|

Each has the simple exact outward bound q<=1/1000000<1. Both individual row
bounds, full original/reflected R, C/reflected C and H are in the output.
No decimal sign, overlap rule or root-distance threshold was used.

The exact mask invariance and cardinal identities make each reflected witness
a witness for the SAME signed polynomial. Both root witnesses are valid and
their critical points lie in H. Existing strict gradient injectivity on H
therefore implies equality; the reflection relation then places that critical
point exactly on x=0, by the stated conditional argument in63. This supports
axis reuse for these actual3 records. It introduces no new acceptance
predicate. R9 happens already to be reflection-invariant; the full hull check
was nevertheless executed for all3, including the nonsymmetric R10 and R21.

## Sources, output and limitations

Main source before/import/after SHA256:
`a9cff5748d6c40ee41ac76e4e8a0035e0d5dab95f4de1233dfcc26902cb085a2`.
Controls source before/after SHA256:
`7f57ed9ba5ad864391aa2e309834d9b61c33f673a6854247d44594cb10ec71d2`.
Both equality guards passed. Python3.12.14, SymPy1.14.0,
python-flint0.9.0/FLINT3.6.0,160-bit outward dyadics. Trusted arithmetic is
CPython integers/Fraction and SymPy exact field/matrix/polynomial operations
with the FLINT backend. No floating proof predicate is used.

Output `outputs/a5_checker_n8_axis_preflight.json`,24615bytes, SHA256
`04b514dd497b870c7fedc038b462d2656a8f78fecdf750306addb6004f206f11`.
It explicitly records `count_certified=false`; no partition, complete cone
set, edge/corner census or global-value certificate was checked here.

Every proposed mirrored leaf/reference still must contain the selected
stored root R in its own U and satisfy the unchanged injectivity predicate
with that stored root's actual C. This root-level preflight does not grant
permission to skip those enlarged-hull checks or any compatible mask.
Complete literal count/global verification, actual different-agent full
execution, essential-evidence handling and the required Claude audit remain
separate. N8 count/global targets remain OPEN.

## Literal executed command

The following inline command actually ran from `/workspace/padua_research`:

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
out=base/'outputs/a5_checker_n8_axis_preflight.json';out.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
print(json.dumps({'original_roots':len(v.roots),'regions':result['root_rectangle_regions'],'axis':[{k:r[k]for k in('id','same_mask','R_exactly_reflection_invariant','reflected_original_root_predicates_passed','same_actual_C_hull_injection_passed','norm_upper_rounded_outward','axis_equality_conditions_verified')}for r in results],'sources_unchanged':True,'seconds':result['seconds'],'count_certified':False},sort_keys=True),flush=True)
PY
```

## Addendum: actual unchanged-checker axis-fixture integration

Root separately assigned this bounded literal integration after the exact
axis preflight. Input head `0870eb7091e199a1ad82533e86d6b4802c85d120`;
an actual read-only diff confirmed no change to the three rule files. The
new axis proposer is not a checker dependency and was not imported. No
source or acceptance predicate was changed.

Actual fixed input `/tmp/a5-n8-axis-fixture.json.gz`,146897bytes, SHA256
`00ff218c3250397922292766c207e26832208339ba792607803f80551e5b6d22`.
The raw hash was checked before execution, matched the checker's recorded
input identity, and was checked unchanged afterward. This small proposal
supplies43 root records and14 leaves, with12 pending paths and no edges;
it is explicitly incomplete and supplies no closed-square count.

The following exact command actually ran from `/workspace/padua_research`,
starting at13:53UTC, and completed with exit0 in62.546534097seconds:

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/padua2-deps python -B topics/padua-proof-attempts-2-20261101/code/a5_checker_n8.py /tmp/a5-n8-axis-fixture.json.gz --allow-partial --output topics/padua-proof-attempts-2-20261101/outputs/a5_checker_n8_axis_fixture.json > /tmp/a5_checker_n8_axis_fixture.stdout 2>/tmp/a5_checker_n8_axis_fixture.stderr
```

Every supplied predicate passed through the frozen independent checker:

| Recomputed scope | Observed result |
|---|---|
| exact node cones |45 accepted,3474 complete directional breakpoints |
| supplied distinct root records |43, all ordinary root predicates passed |
| supplied leaves |14 |
| ordinary compatible records |522: gradient320, Hessian192, root10 |
| universal-gradient leaves |2 centered,262144 compatible-pattern occurrences |
| node leaves |2, actual-cone strict containment passed |

All10 root-reference dispositions recomputed their actual stored-root mask,
U containment of both the leaf and selected original R, and the original
stored-C injectivity bound on that U. The proposer supplied axis IDs for
reuse; the verifier granted no special symmetry exception or skip. All43
root boxes separately passed disjointness, strict cardinal signs, negative
definite Hessians and Krawczyk existence/uniqueness. The all-compatible
ordering/coverage checks and direct node/universal predicates also ran
unchanged. Thus this is literal proposed-witness integration, not merely a
review of the proposer's own inequalities.

Observed output flags are `verified_supplied_witnesses=true` and
`accepted=false`, `count_certified=false`,
`complete_prefix_partition=false`, `interior_complete=false`,
`boundary_complete=false`. Exit0 with `--allow-partial` means the supplied
witnesses passed; it does not accept a maxima count.

Main source SHA256 before/import/after remained
`a9cff5748d6c40ee41ac76e4e8a0035e0d5dab95f4de1233dfcc26902cb085a2`;
the built-in `checker_source_unchanged` guard is true. Controls source was
not executed in this integration and remained, before/after,
`7f57ed9ba5ad864391aa2e309834d9b61c33f673a6854247d44594cb10ec71d2`.
Python3.12.14, SymPy1.14.0, python-flint0.9.0/FLINT3.6.0,160-bit dyadics;
trusted exact arithmetic is as stated above and recorded in the output.

Actual durable output `outputs/a5_checker_n8_axis_fixture.json`,11690bytes,
SHA256 `2df5494bd96ead2e7d23c62a5616079476942c5e2d38cabd3edced84cf11cb74`.
The temporary input/stdout/stderr are retained locally pending root's
evidence/archive handling. This addendum is append-only; the original axis
preflight and its output remain unchanged. Final full-controls execution
still awaits a complete matching count/global pair and explicit instruction.
No full count, complete partition, boundary or global assertion follows from
this fixture. N8 count/global targets and the separate Claude audit remain
OPEN/pending.
