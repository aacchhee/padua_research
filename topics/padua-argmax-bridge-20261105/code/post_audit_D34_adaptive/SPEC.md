# D34 first exact adaptive41 prototype — prospective frozen contract

Status **UNEXECUTED**. Requested developer Codex gpt-6.1-sol medium;
serving metadata independently unexposed. This is source preparation ONLY.
D32's generic mathematical contract is accepted by distinct review82a4a38e;
D29 floors are accepted by review84fbde47. The D34 executable source still
requires distinct source/math matching audit, publication and root release
before ANY control/compiler/native
execution. No new degree claim is permitted before independent FRESH replay
of ALL retained proof points and all final predicates after a successful
primary. Root alone controls Git/shared records and release.

## One command, one case

The only future command, from repository root after explicit release:

```sh
python3 topics/padua-argmax-bridge-20261105/code/post_audit_D34_adaptive/controller.py --run-once
```

The one attempt directory is
`local-output/argmax-bridge-20261105/post-audit-D34/adaptive`.
Exclusive mkdir consumes the attempt even on registration failure. Never
remove/reuse it to retry. Degree is STRICTLY n41,m42,kappa41/42; no second
seed/case/degree, source, precision, order, cap, phase, geometry or rescue.
There is no guarantee that a certificate exists or fits these budgets.

## Exact point sources and cache

Freshly build TWO isolated libraries using the accepted builder lineage:

- S source: unchanged `post_audit_D23_backend/point.cpp` and local partial,
  J2,K8,LH4,WD16,P160,CP640,MP640. Its full returned ball, including all
  lower-degree truncation and numerical uncertainty, is retained. D23's
  specially small160-and-above corollary is NOT imported at41.
- ACTUAL lambda source: unchanged `post_audit_D07_fourcopy_point/point.cpp`,
  which includes ORIGINAL C11 point/partial arithmetic with J16,K32,LH16,
  WD96. Never route cheap S tails into the actual-lambda API. Its literal
  n<=2048 guard admits41 unchanged; C23's n<=2147483647 is unchanged.

Only `c07_point` from the S library and `d07_point` from the actual library
are bound/called. No FLOAT, model, producer approximation or reference API.
Arb/LP64, C++ compiler and system/runtime identity checks remain trusted
numerical dependencies, not a hermetic/formally verified machine claim.
Tools/headers/preprocessed TUs/source snapshots, linked/loaded closures,
all mappings and before/after identities are recorded/rechecked. Missing
package setup is frozen and inside budget; read its cloud-runtime guidance
before release.

All arguments are exact canonical Fractions. For raw vertices in[0,1]^2,
fold(a,b)->(1-a,1-b) only above a+b=1; reverse coordinates only ON that
hypotenuse, choosing the lexicographic minimum. Never swap interior phases
or unequal n,m meshes. A new S key is called once, only if absent from the
in-memory source/degree-scoped cache; no on-disk/old-degree cache input.
At most256 unique S calls TOTAL including grid, intermediate parents and
final corners. Before a257th call fail; duplicates use the same complete
validated enclosure. All calls retain API,n,key, raw lower/upper/radius hex,
complete counters and inclusive point CPU before any acceptance check.
Nonfinite/inverted endpoints, nonnegative-radius/lower or counter failures
end the attempt. Diagnostic mag_get_d is never a narrowness predicate.

For S require retained4n and ordinary2(n+1)-4 except the exact S=1 endpoint
with all-zero counters; maxdirect<=5,maxblocks<=24 and total bounds. All13
actual counters must be nonnegative,43 actual rows, no node/corner shortcut,
applicable row/fallback bounds and maxdirect<=40. D07's existing internal
row recovery is unchanged, retained/charged and is not an external retry.

## Coarse grid, actual corner and deterministic producer

First query the SORTED canonical union of
E={(i/4,j/4):i,j>=0,i+j<=4}. There are13 distinct keys after the accepted
hypotenuse identifications. All fresh upper endpoints establish

    Mcoarse=ceil((784/663)*max_grid_upper),
    L=fresh LOWER S(0,0)>0.

D14's GLOBAL norming proof establishes Mcoarse, not a sampled-maximum
assumption. Then make exactly THREE fresh actual-lambda calls in this order:

    (xi/pi,zeta/pi)=(1/164,0),(0,1/224),(1/164,1/224).

These are inward PHYSICAL angles, corresponding to(A,B)=(pi/4,0),
(0,3pi/16),(pi/4,3pi/16). Never pass phase turns1/4,3/16 to d07_point.
Let their uppers be Wx,Wy,Wxy. For any final global norm M use EXACT D32:

    u'=1/32, v'=9/512,
    q=min((L-Wx)/u',(L-Wy)/v',(L-Wxy)/(u'+v')),
    t=M*(22/7)^4*max(u',kappa^4*v')/6 = M*(22/7)^4/192.

Require q>t and the proved actual-corner radial coefficient lower is
(q-t)/(2*(22/7)^2). The pi^4 factor and symbolic true corner origin are
essential. D08/D32 then covers both parity-correct inward half diamonds;
n41 is odd and the candidate equality corners would be(-1,-1),(-1,1).
No analytic D17 corner substitution at41. A preliminary coarse-M corner
calculation is recorded without acceptance/stop; the predeclared FINAL M
is used once at final verification. This is not a retry after a failed
final criterion.

Start the exact producer at[0,1]^2 and use Mcoarse throughout discovery.
For each node, lower-child-first depth-first traversal:

1. Count the node; fail before visiting more than2047 nodes or depth18.
   Discard a leaf only if al+bl>1. Equality/tangency is retained.
2. Obtain all four canonical vertex uppers through the exact S cache,
   requesting missing keys in sorted order. Compute V=max uppers and
   U=V+theta*Mcoarse, theta=(22/7)^2*(wa^2+kappa^2*wb^2)/8.
   The independent coarse norm permits theta>=1 during discovery.
3. Use the exact full-box leaf predicates below. If one passes, accept the
   leaf. Otherwise split the coordinate with larger squared weighted width:
   wa^2>=kappa^2*wb^2 selects a (including ties), else b. Split EXACTLY at
   its midpoint and visit the lower child then upper child. An unaccepted
   depth18 leaf or exhausted node/key budget is a first failure.

There is no pruning, polygon optimizer, additional seed or fallback method.
The complete trace records every box, visited node, fresh call, upper,
radius-floor and branch. Failed/pending nodes are preserved in raw output.

## Actual-near floor and phase predicates

For every retained box put p_lo157/50,p_hi22/7,
low=al+bl, high=min(ah+bh,1), r_B=min(1/2,p_hi*(ah+bh)). With r=r_B set

    a=1-r^2/4,
    U0=347a/1000-157r/500, V0=17a/20-r/2, W0=779a/750-5r/6,
    B41(r)=11711U0/48400-120V0/(157*41)
            -250W0/(157*41)-100V0/(3*41^2),
    delta_B=max(1/512,min(1/32,B41(r))).

D29's accepted n>=41 theorem proves this floor ONLY at ACTUAL noncorner
centers and ACTUAL rho<=r_B<=1/2. An actual near point satisfies that
radius bound by D32; a rational outer proxy alone does not establish it.
Do not apply this floor at an actual corner or sum projected defects.

For the chosen valid global M recompute U=V+theta*M. Fixed priority:

- FAR: U<L.
- Else NEAR:2*p_hi*high<=1 and U-delta_B<L.
- Else SPLIT: if low<=1/(2*p_lo) require U-delta_B<L;
  if high>=1/(2*p_hi) require U<L.

All required comparisons are strict, including equality/tangent proxies.
Full-box U is conservative on every clipped proxy. The exact closed tree,
PD-T364 physical chart cover/parity reflections, D29 floor and independently
validated actual corner criterion are the D32 sufficient witness. Every
final retained leaf and every required branch must pass.

## Final norm selection and proof-premise retention

After the producer completes ONCE, reconstruct the entire tree and FINAL
corner union. If EVERY retained theta<1 calculate
Rtree=max_B V_B/(1-theta_B), Mtree=ceil(Rtree); otherwise Mtree is unavailable.
The PREDECLARED selection is the minimum of independently valid Mcoarse and
available Mtree, with TREE winning ties. This choice occurs before FINAL
acceptance, never as fallback after a failed final phase/corner check.
Recompute ALL final Peano/phase predicates and the actual-corner criterion
using the selected M. Failure stops; no alternative norm retry.

Retain EVERY final corner upper. If GRID is selected, also retain all13 grid
uppers. If TREE is selected, unused grid/parent samples may be omitted from
the essential proof because the final own-tree norm independently establishes
M. Raw output retains the entire grid, both candidate bounds and selection
trace. A kept-point checker need only reconstruct the SELECTED sufficient
norm proof; it does not rely on omitted grid values to prove minimality.
No new pruning or discarded-child margin supplies a premise.

## Compact essential proof and whole raw evidence

ONE essential certificate contains the complete midpoint tree,n/pi bracket,
ALL retained S UPPERS keyed by canonical rational arguments, fresh actual
origin LOWER, all THREE ACTUAL lambda UPPERS with physical keys, selected
norm method/M, floor/corner identities, reconstructed verification and source/
raw identities. It is checked again using ONLY these kept premises before
writing. It must be strictly<16384B as a whole; overflow is a first failure.
There is no truncation, output split or point-dropping rescue to fit the cap.
This is declared mathematical-premise selection, not a cap-evasion strategy.

All native lower/upper/radius/counters/CPU records, unused samples, cache,
producer trace, grid/selection candidates, control results and complete build/
runtime/maps records are retained in ONE whole `raw-evidence.json` off Git,
with SHA256 and bytes. It includes every available record on failed paths
as well, never a truncated sample. Build binaries/TUs remain retained at their
manifested off-Git paths. The immutable supervised checkpoint identity is
rechecked before packaging. Temporary/checkpoint files are operational
copies, not partitions used to evade the evidence cap. AC selects any cold
archive; no permanent retrieval claim is made. Root alone integrates small
proof evidence after review.

## Budget, finalization and future obligations

Whole inclusive120CPU includes controls2/checker100, both fresh builds,
provisioning/imports, every child, all S/actual calls, production and final
checks, raw/essential serialization, supervision/output/write/return.
Sampled safety110; completed native stop10; unfinished kill15CPU; poll0.25s.
Walls: controls15seconds,checker900,whole1000. Controls are fixed synthetic
schema/grid/norm/floor/corner/strict-leaf cases only, no scientific point.
No separate author control slot may be consumed before review/release.

Accepted D15 runtime structure supplies Linux subreaper group kill/reap,
complete waited-descendant accounting and first-failure records. Establish
ECHILD, fix waited-child CPU c and launch no further child. Tighten absolute
parent selfHard<=floor(120-c)-1, hence c+selfHard<=119<120, with required
finalization headroom. Incomplete accounting cannot accept. Freeze/source/
loaded identities and postserialization CPU gates remain mandatory.

Summary/essential receipt are PROVISIONAL. Require directly observed EXIT0
AND atomic final-accounting complete=true,first_failure=null,result exactly
`EXACT_ADAPTIVE41_PRIMARY_ACCEPTED_PENDING_FRESH_REPLAY`. A killed writer or
failed finalizer cannot promote provisional artifacts. Preserve the first
failure and do not rescue it. Successful primary would be a finite prototype
witness, not degree adoption. Distinct fresh replay of ALL kept S/origin/
actual point premises plus the full final norm/phase/corner check and result
review remains required before any new global n41 claim.
