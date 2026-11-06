# PD-T?argmax-bridge-codex-D19-pruned2048 — A smaller self-norming degree2048 certificate

ID kind: PD-T.
Aliases: D19 one-tree2048;41S+3actual certificate; fixed-postorder
metadata coarsening; static integer geometry witness.
Split from: finite application of D19-adaptive-norm.md.
Split into: native implementation/performance remains separate.

## Statement and status

At the SAME degree n2048 already certified by D15, the new complete
61-node tree and41 independently validated S point enclosures, together
with the same3 independently validated ACTUAL lambda point enclosures,
form a self-contained certificate of

    S_2048(alpha,beta)<35 for ALL real phases,
    max_[-1,1]² lambda_2048=lambda_2048(-1,-1),
    argmax_[-1,1]² lambda_2048={(-1,-1),(1,-1)}.      (1)

The norm in(1) comes ONLY from the final tree's OWN corners using
the new leafwise norming implication. There is no hidden old full-tree,
quarter-grid, model norm42/34 or removed-point premise. This reduces
the S obligations from51 to41 and the total point obligations from54
to44, with the actual3points unchanged. The degree/equality set is
unchanged; this is not another newly certified degree.

Overall status: **PROVED developer exact metadata/computational
application**. Independent review of the NEW D19 norm/pruning proof,
source and metadata result is pending. The selected native endpoint
enclosures themselves ALREADY have the accepted D15 fresh replay;
no new native enclosure or performance benchmark is asserted here.
Final Claude audit and root adoption remain separate.

## Inputs, unchanged endpoint provenance and new evidence

D15's accepted finite result/application report is
[`independent-checks-D15-model-free-result.md`](../independent-checks-D15-model-free-result.md),
SHA256 `97044e296b48e4348326f3b354118eb2373155b2fe06f3fc19107839b7bd6ef0`.
Its51S+3actual fresh build/replay took177.049501
inclusive CPU and validated every original endpoint/radius/counter.
This application uses ONLY the selected individual outward enclosures
and their source/arithmetic trusted base, not D15's old norm or global
argmax as a proof premise. The D15 primary229.616251CPU includes
discovery54.263514 and checker175.307516; those measured historical
costs are context, not a new D19 timing or a predicted speedup.

The pinned old evidence stays whole and unchanged:

| Input | SHA256 |
|---|---|
| evidence/d15-model-free-cover.json,11491B |6be2926071f43d2a619784c16b15c980e6952eaa3cfe4bab0703c14dcc6b3481|
| evidence/d15-model-free-cover-tree.json,142B |bff8e2281d4e98f3d8a90a4a811162cbf9b275a1eda182111daac25e3033c685|
| evidence/d15-review-model-free-cover.json,11240B |7bf8fab38379a97e8e7c9bf57fca0f90510fba609ee46014d86df134b70b87a7|
| evidence/d15-model-free-cover-final-accounting.json |c826130c4dfe9b5fb737514942cae5806ed9f1057bbd39c9f7b2d0b9c4114750|

The one-shot D19 metadata helper
[`check.py`](../code/post_audit_D19_adaptive_norm/check.py),9656B,
SHA256 `b1721007323b03de815942c8d7db954a231ed733899a2540c1ca347b6973fce3`,
was prospectively frozen/inspected with those inputs before its one run.
It cross-checked all54 primary/independent native rows exactly, excluding
their different historical CPUs, before selecting any endpoint. The
literal provisional status inside the old all-row receipts is NOT
independent completion: D15's accepted result report and preserved
final-accounting/return0 records supply that already completed premise.

New complete evidence is:

| New record | Bytes | SHA256 |
|---|---:|---|
| [Self-contained bound,44 unchanged subset rows and fixed merge trace](../evidence/d19-adaptive-norm.json) |9034|4b4161b3f1eefafd8bbcd8cead2b101ea82dc156d811edd413fa46376810ed0c|
| [Complete pruned tree](../evidence/d19-pruned-tree.json) |113|5ff335b5e8c3a813b934f38b0938cf80bf29f546749651cd749e5ffc41c753d1|

The original records were NOT pruned, overwritten or split to evade
limits. This is a new reduced mathematical witness; all44 selected
rows are copied unchanged. Their CPU fields are original D15 point
costs, not D19 native measurements. The subset receipt contains every
final required S endpoint plus the3actual rows, final norm/corner/
leaf arithmetic and all38 deterministic proposal dispositions.

## Decisive initial adaptive-norm gate

Use the accepted n2048 definitions m2049,kappa2048/2049,p_hi22/7,
p_lo157/50 and the actual corner lower

    L=1222754463982439/35184372088832.

For each nonempty/tangent leaf B_i of the ORIGINAL77-node complete
tree, compute theta_i=p_hi²[width_a²+kappa² width_b²]/8 and
V_i=max of its own4actual vertex uppers. Every theta_i<1. D19's
analytic norming implication gives

    M*<=R_initial
      =1006188258610314038209293/28935301726122385866752<35.

Thus Mceil35 improves the old fixed-quarter-grid choice42 without any
new point. At35 the original tree itself passes every corner/phase
predicate, with34FAR/3NEAR/2OUTSIDE. This was the preregistered
gate allowing the single fixed pruning pass, not a tunable choice.

## Exactly one deterministic greedy pass

The source visits each of the38 original internal nodes once in fixed
left-first postorder. At each proposal it replaces that node's CURRENT
remaining subtree by its parent leaf. It first requires every parent
corner key to be available in the old51. It then recomputes FROM
SCRATCH the entire candidate's own-leaf norm, exact ceiling M, ACTUAL
three-loss criterion and ALL phase guards/inequalities. It accepts only
if those pass and the required S key count does not increase. There
is no repeated pass, alternate traversal, new coordinate, missing-key
evaluation, degree, precision, threshold or numerical rescue.

The fixed pass accepted8merges, rejected27proposals by a phase
predicate and3by theta>=1. No point query was made for a rejected
proposal. The accepted original preorder IDs were17,21,34,40,46,52,
58,69. After them the S/node counts were respectively

    (50,75),(48,73),(46,71),(45,69),
    (43,67),(42,65),(42,63),(41,61).

Mceil was recomputed and equal to35 after every accepted merge;
the underlying exact R was not carried over. In particular the final
R differs from the initial R. This finite greedy outcome is not an
optimality statement; other untested orders are not claimed better
or worse. Every proposed disposition remains in the new receipt.

The ten unused old S keys are

    (0,3/16),(0,3/8),(0,3/4),(1/64,1/16),(3/64,0),
    (3/64,1/32),(1/16,3/16),(1/8,3/8),
    (3/16,1/16),(3/8,1/8).

Notably the old quarter-grid key(0,3/4) is absent. It cannot be
replaced by(3/4,0), since these are INTERIOR phase-triangle points
and no n/m interchange is a symmetry. Thus the old15-grid norm
cannot silently supply the final proof. Only the adaptive final-tree
norm below is used.

## Final certificate, global norm and corner criterion

The113B D19-midpoint-v1 tree has exact n2048 and preorder

    abababababab..b...b..a..ba...a..ba...a..ba...a.b..bab...ab...

It is a complete binary midpoint tree rooted at[0,1]², with61nodes,
30internal nodes and31closed leaves. Subtree replacement preserves
the closed parent union, so clipping its leaves to T covers ALL of T.
The OUTSIDE test remains strictly a_l+b_l>1, retaining tangent points.
Its41canonical S vertices are exactly the S row set of the new receipt.

Compute ONLY on these final nonempty/tangent leaves:

    R_final=max_i V_i/(1-theta_i)
      =502286612131036595880045/14441481181380210589696<35,   (2)
    35-R_final
      =3165229217270774759315/14441481181380210589696>0.

Every retained theta_i<1, including any lower-dimensional clipped
patch. The adaptive norm theorem proves M*<=R_final, globally on
all real phases by compactness/period/evenness. The corner and full
signed polynomial families are therefore globally bounded by35.
No deleted point or old norm is used in(2).

The three ACTUAL upper point premises stay at physical inward turns
(1/8192,0),(0,1/10928),(1/8192,1/10928). The lower losses remain

    d_x=1169561375556747/281474976710656,
    d_y=335239824993179/140737488355328,
    d_xy=916890158846183/140737488355328.

With u'=1/32,v'=9/512, the exact current-M criterion is

    q=1169561375556747/8796093022208,
    t=(35*p_hi^4/6)*max(u',kappa^4*v')=73205/4116,
    gap=q-t=1042499158025208503/9051179719852032>0.

Hence e=gap/p_hi²=1042499158025208503/89403489477722112>0
multiplies u+v=(A²+B²)/2 in the accepted actual-cardinal theorem.
At both closed actual primary rectangles,

    lambda_2048<=Lambda_c
       -[1042499158025208503/178806978955444224]*(A²+B²).    (3)

The radial coefficient is HALF the u+v coefficient. The origin
remains symbolic Lambda_c; no rounded origin upper introduces a
positive constant error. The pi/4 by3pi/16 rectangle contains the
full closed inwardrho<=1/2 half diamond. Even-degree x reflection
supplies the second actual corner without exchanging n and m.

## Final leaf predicates and exact global classification

With M35, each final rectangle upper is

    U_B=max_(its four own vertices) U
       +(35*p_hi²/8)[width_a²+kappa² width_b²].      (4)

The independently validated ordinary Peano theorem proves this bound
throughout the enclosing rectangle. S is interpolated in ordinary
phases via its smooth signed components; its cusp is not differentiated.
Only S arguments are folded by the exact even lattice/sign orbit;
physical centers, widths, clipped sets and actual radius guards stay.

| Final predicate | Count | Minimum exact strict margin |
|---|---:|---|
| FAR: U_B<L |24|16388513452517984501/2068053441469741006848|
| NEAR: U_B-1/32<L |5|5521721808950024375/2068053441469741006848|
| OUTSIDE: a_l+b_l>1 |2|Exact empty clipped intersection|

Every NEAR leaf also passes2*p_hi*min(a_h+b_h,1)<=1, which proves
the ACTUAL signedrho<=1/2 guard on its entire clipped patch. No
SPLIT leaf occurs. FAR is a primitive exclusion and needs no lower
radius. Strict outside tests retain tangencies and shared edges.

The generic accepted D15 contract now applies with the NEW(2)--(4).
For any physical point PD-T364 supplies a physical odd-center chart
with rho<=pi and exact lambda=S-Delta,Delta>=0. There are2100225
physical odd centers; their complete closed L1-distance cover needs
no enumeration or sampled class minimum. Evenness maps the common S
value into T and the final tree supplies a containing leaf.
FAR gives lambda<=U_B<L<=Lambda_c. On NEAR at a noncorner center,
one index is interior, so C02's n>=160 actual-near projected floor
gives Delta>1/32. The maximum, never the sum, of projections is
used: lambda<=U_B-1/32<L<=Lambda_c. At the two actual even-degree
corner centers(2048,2049),(0,2049), inward admissibility and(3)
give strictness except at zero phase. At zero phase Delta=0 and
S(0)=Lambda_c, with equal corner values by x reflection. This proves
(1), including nodes, ties, axes, closed seams, tangent leaves,
initially zero cardinals and finite-polynomial collisions.

## Algorithm application and practical limits

For this SAME fixed2048 case, a future deterministic INTEGER-geometry
producer can emit the frozen61-token midpoint tree and derive its41
canonical S keys without a FLOAT search. A separate Arb verifier can
request those41 actual S enclosures and the3 actual lambda enclosures,
compute its OWN current leaf norm/ceiling, then all corner and phase
predicates exactly. It needs no preliminary quarter-grid calls or old
point receipt as a runtime premise if the44 enclosures are freshly
computed. This is a specified finite certificate algorithm, not a
claim that the existing D15 controller implements that pathway.
The D19 format and dynamic adaptive norm need separately reviewed
source integration; old literal parser/guard semantics are unchanged.

The old FLOAT discovery cost54.263514CPU would not be a required
stage of THAT static-witness design, but no such fresh native pipeline
has been built or benchmarked here. Reducing point obligations does
NOT establish a measured runtime ratio. We do not sum old per-point
CPU fields as a new benchmark, claim every point has the same cost,
or infer a uniform scaling law, actual speedup, general tree-generation
algorithm, optimal pruning or success at any other degree.

One preregistered source-frozen command ran ONCE:

    python3 topics/padua-argmax-bridge-20261105/code/post_audit_D19_adaptive_norm/check.py

It returned PASS, whole process CPU INCLUDING imports0.081474 through
the pre-serialization sample, with no children and hard RLIMIT_CPU2.
The small final receipt/tree serialization/write/print remained under
that same hard bound and the process exited0. ZERO native, phase,
kernel, board, root, quadrature, compiler or degree jobs ran. The
native/source/tail trusted base is inherited from the selected already
independently accepted D15 point enclosures; D19 only validates exact
metadata arithmetic. Distinct review must independently reconstruct
the new norm and final closed certificate, inspect the fixed pruning
source/trace and validate the copied subset/input identities.

2026-11-06, Codex gpt-6.1-sol xhigh25min; rules/input
`0768cb93c4f829faf5f38d47cdd7e33faad8bf64`, serving metadata unexposed.
Fresh gate, preexecution freeze and actual one-shot chronology are in
the D19 idea/attempt/SPEC. Only new D19 files were written; original
D15/source/evidence, shared records and mutable Git state are unchanged.
New norm/application/source/result review and final Claude audit remain
separate from root adoption. No new global degree is claimed.
