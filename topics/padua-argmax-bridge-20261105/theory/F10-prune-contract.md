# PD-T?argmax-bridge-codex-F10-prune — Fixed-premise GRID pruning and query-set inclusion

ID kind: PD-T. Aliases: two-fifths raw-box guard; conditional pre-query
domination; discovery versus retained key sets. Split from: quantitative
application of F07 to the existing finite-cover producer. Split into: none.

## Statement

Use the ORIGINAL final-hybrid source geometry and mathematical predicates
at any legal source degree n (integer41..4095). Compare its old E15-only
pre-query analytic predicate A0 with the following PROPOSED mathematical
predicate A1, on raw positive-width closed boxes in[0,1]^2. Write
s(B)=a_l+b_l. Outside boxes are discarded FIRST when s(B)>1. Otherwise

    A0(n,B): n>=192 and1/2<=s(B)<=1;
    A1(n,B): A0(n,B) if n<256,
             2/5<=s(B)<=1 if n>=256.                 (1)

These are propositions in a PAPER comparison, not modified source.
Assume the following SAME fixed premises:

1. One fixed extensional map of canonical rational S keys to valid
   upper enclosures U, with a fixed positive lower L<=true Lambda_c at
   the origin. It suffices that this map is available at all keys the
   old producer requested. Values on overlapping keys do not change.
2. Identical mandatory13-grid premises, Mcoarse, L, numeric leaf predicate,
   floor/corner witnesses, canonicalization, midpoint split rule/ties and
   left-first traversal. Both mathematical discovery recursions use the
   SAME Mcoarse throughout, exactly as the current source does.
3. An accepted complete OLD source-generated tree T0, containing at
   least one analytic f leaf. Its final METHOD is therefore GRID and its
   final numerical norm is Mcoarse. All its mathematical premises are
   valid at the stated degree and original source guards.
4. The written F07 regional theorem is valid at its exact stated scope,
   along with the existing E15, D14, D32/PD364 and unchanged numeric
   floor/corner dependencies. F07 has distinct mathematical ACCEPT;
   root adoption/source use remain separate process decisions.

Then the finite mathematical tree T1 produced under A1 and these SAME
premises is obtained from T0 solely by replacing old subtrees with valid
analytic leaves. In particular every new visited numeric/internal-query
node and every new final numeric leaf has the SAME path and raw box as
an old node/leaf of that kind. T1 still contains an f, its final METHOD
is GRID, and its Mcoarse/L are unchanged.

Define D_i as mandatory grid keys UNION canonical vertices queried at
EVERY visited nonoutside/nonanalytic node, INCLUDING internal nodes.
Define Q_i as mandatory grid keys UNION canonical vertices of FINAL
nonempty numeric dot leaves. Then

    D_1 subset D_0, Q_1 subset Q_0,                  (2)
    |D_1|<=|D_0|, |Q_1|<=|Q_0|.

These are distinct finite sets. Strict saving is not guaranteed. The
fixed retained numerical premises of T1 are inherited unchanged from
T0's valid kept premises; its newly analytic leaves have independent
whole-patch primitive exclusions. This establishes a mathematical
finite-cover witness transformation under the hypotheses, not acceptance
by the currently unchanged executable parser.

## Status and exact limits

Overall status: **PROVED developer PAPER implication under the explicit
fixed-premise hypotheses above**, requiring distinct review/root adoption.
This theorem claims no engine/worker/native success, resource bound,
CPU/wall improvement, certificate byte saving, query-call order, strict
query reduction, new finite degree, global onset or unconditional TREE
case. It changes no delivered source, certificate schema, pack or guard.
No F10 replay, script, import, fixture or mathematical oracle was run.

## Definitions and accepted sources

Let T={a,b>=0:a+b<=1}. A raw B=[a_l,a_h]x[b_l,b_h] has rational
coordinates0<=a_l<a_h<=1,0<=b_l<b_h<=1. Its physical patch is B intersect T.
It is nonempty EXACTLY when s(B)<=1: the lower-left corner proves one
direction, and coordinate monotonicity proves the other. Equality is a
retained tangent patch, never OUTSIDE.

Use EXACTLY the current canonicalization c on rational raw vertices:
fold(a,b) to(1-a,1-b) if a+b>1, then take the lexicographic minimum
of(a,b),(b,a) ONLY when their sum is1. In the interior there is no
coordinate exchange or n,m swap. D19/PD364 prove that this preserves
the same finite primitive VALUE. It never changes a raw box, width,
lower sum, physical center or radius guard.
The map is idempotent by these same cases, so the engine's second
canonicalization inside its upper-cache wrapper leaves each key unchanged.

Write V(B)={c(a,b):a in{a_l,a_h},b in{b_l,b_h}}. The mandatory set is

    G={c(i/4,j/4):i,j nonnegative integers,i+j<=4},
    Mcoarse=ceil[(784/663)*max_(k in G)U(k)].          (3)

G has the accepted13 canonical keys and includes the origin. D14 gives
the GLOBAL norm(3), independently of tree coverage or analytic leaves.
The lower L is the SAME valid origin lower, not a numerical replacement
for true Lambda_c in an analytic inequality.

The authenticated source inspected as text only is
code/final_hybrid_engine/{checker,producer,engine,runtime}.py, with full
SPEC and independent source/result review. Its exact hashes and reading
coverage are in the owned idea/attempt. In particular producer queries
V(B) AFTER OUTSIDE and analytic tests but BEFORE numeric leaf acceptance
or splitting. The engine computes G/Mcoarse first and supplies that SAME
norm to discovery; final method selection happens afterwards.

Its numeric predicate is exactly the unchanged checker.leaf on
n,B,max_(k in V(B))U(k),L,Mcoarse, with original strict FAR/NEAR/SPLIT,
actual-near radius/floor domains and closed seam handling. It is a
deterministic function of those fixed arguments. No new numerical
formula or evaluation is introduced. Failed numeric nodes split the
larger of width_a^2 and(n/(n+1))^2 width_b^2, splitting a on a tie,
at its exact midpoint; lower child is visited first.

## Proof

### 1. Raw guard validity and closed physical patches

The accepted pi bracket gives

    pi>157/50>25/8,
    157/50-25/8=3/200>0.

At n>=256, if A1 holds and(a,b) belongs to the ENTIRE closed physical
patch B intersect T, then

    2/5<=s(B)<=a+b<=1,
    rho=pi(a+b)>=2pi/5>5/4, rho<=pi.                (4)

Thus F07 applies throughout that patch and gives
S_n(pi*a,pi*b)<true Lambda_c-9/100. The closed lower boundary2/5
is safe; no sample, center or folded-key membership substitutes for(4).
The theorem is not asserted on the nonphysical portion of B outside T.
At n<256, A1=A0 and E15 supplies the unchanged closed half-pi exclusion
S_n<true Lambda_c-3/100, on its n>=192 domain. Both use the SAME S.
Separate absolute phases/PD364 handle the signed physical charts without
exchanging unequal meshes. In each chart physical lambda<=the SAME S.

All OUTSIDE tests precede(1). A tangent s(B)=1 remains nonempty and
is correctly analytic where(1) holds. If an actual box lies partly
outside T, only its entire clipped patch needs an analytic inequality.

For every legal n,B, A0 implies A1: below256 they agree; from256,
1/2>=2/5. This is the only predicate enlargement used in the proof.

### 2. Establish the exact fixed-premise coupling BEFORE recursion

Both mathematical procedures first retain ALL keys of G with the SAME
U values. Equation(3) therefore gives identical Mcoarse. The same fixed
origin lower gives identical L. The analytic guard cannot remove a
mandatory grid premise, even if that point lies in an analytic patch.
Neither discovery procedure selects a TREE norm during traversal.

At any common nonanalytic raw box, the SAME canonicalization and U give
the SAME V(B) and vertex maximum. The unchanged n/B,L,Mcoarse and floor
data then give the SAME numeric predicate outcome. If that outcome is
failure, the fixed widths,n/(n+1) and tie rule give the SAME midpoint,
split axis and two closed child boxes. This is an equality of arguments
to deterministic finite rules, not a claim that fresh native evaluations
in different environments return equal bits.

The fixed extensional map hypothesis is not circular: the induction
below first shows every requested new key was an old requested key.
One may equivalently start with U defined on all canonical rational
keys, with only its values on the old finite request set used. No
unavailable numerical point is evaluated to establish the coupling.

### 3. Structural induction on the finite old tree

Compare nodes by their binary PATH from the root, not a preorder integer
ID, since pruning renumbers later IDs. The root box is identical.
Suppose a common reached path has the same raw B.

- If s(B)>1, both rules emit the same OUTSIDE dot and make no vertex
  query there.
- If A1 holds, the new rule emits a valid analytic f BEFORE any query.
  The old subtree rooted there is simply removed. It may have been
  numeric, internal or already analytic; no old child bound is needed
  for the new analytic parent, by(4).
- Otherwise A0 is false as well. Both rules query the SAME canonical
  vertices. Section2 gives identical numeric outcomes. If numeric
  acceptance occurs, both emit the same numeric dot. If it fails, both
  use the SAME two children and the induction applies to each child.

The old finite tree supplies the induction. There is no new node path,
split or numeric leaf. Equivalently, traverse T0 top-down and stop at
the first A1-eligible node on each path, replacing its whole subtree
by f; all other node types/boxes remain. This gives exactly T1's finite
mathematical skeleton. It is NOT a run of a modified engine.

Each replacement preserves complete CLOSED coverage: the old closed
subtree covered its parent patch, and the new analytic parent covers
that same entire patch. Closed midpoint child unions, shared edges,
hypotenuse tangencies, degree parity and actual polynomial collisions
remain those of the inherited cover. New analytic validity uses(4),
not inherited child acceptance or a numerical parent bound.

### 4. Final GRID coupling and retained mathematical validity

Choose any old f leaf. If an earlier ancestor is newly pruned, that
ancestor is an f in T1. Otherwise the chosen path survives and is an f
because A0 implies A1. Hence T1 still has an f. The exact current
method policy therefore selects GRID for BOTH trees. In each case its
numerical norm is the SAME Mcoarse from ALL13 unchanged premises.

Every new numeric leaf is an unchanged old numeric leaf, at the SAME
box with the SAME fixed U,L,Mcoarse,floor data. Its strict mathematical
predicate remains valid. The old corner witness is unchanged and uses
the same premises/norm; above256 the existing E12 analytic corner
witness is in any event independent of the numerical phase norm.
Old analytic leaves retain a valid E15 exclusion, or at n>=256 may
use the stronger F07 exclusion. Newly analytic leaves use(4). Thus the
transformed tree is a valid mathematical cover witness with no new
numerical premise.

An analytic leaf never supplies the absent vertex information needed
for D19 TREE absorption. This proof avoids that inference by retaining
the mandatory GRID norm. Without the old-f/GRID fixed-norm hypothesis,
or with changed numerical inputs, this statement supplies no automatic
TREE-to-GRID or fresh-acceptance conclusion. No general failure theorem
for such cases is asserted either.

### 5. Separate discovery-request and retained-key inclusions

Let N_i be the paths where the i-th procedure reaches the vertex-query
step; these include INTERNAL split nodes as well as numeric dot leaves.
Let L_i be its final nonempty numeric dot paths. Section3 proves

    N_1 subset N_0,L_1 subset L_0,

and the boxes agree at every surviving path. Therefore, with the SAME
canonical map,

    D_i=G UNION union_(w in N_i)V(B_w),
    Q_i=G UNION union_(w in L_i)V(B_w),              (5)

immediately give(2). A key shared with a surviving node or G remains
required; it is not saved merely because another occurrence disappears.
The cache counts distinct canonical keys once. No ordered unique-call
subsequence is claimed, since deleting a first occurrence may move a
key's later first remaining occurrence relative to other keys.

The exact set-count reductions, if later computed, are

    |D_0|-|D_1|=|D_0 setminus D_1|,
    |Q_0|-|Q_1|=|Q_0 setminus Q_1|.                 (6)

They can both be zero. Q_i is the retained/fresh-verification obligation
set; D_i also includes production-only parent vertices. They must not
be conflated. This proves the complete advertised finite-query contract.

## Data-only consequence and limits

For an authenticated source-generated OLD preorder, its exact raw boxes,
node types and therefore N_0,L_0 are reconstructible from geometry alone.
Every internal node was reached only after the vertex-query step, every
f stopped before it, and an OUTSIDE dot is identified by its raw lower
sum. Section3 constructs the proposed pruned skeleton from this same
topology and the rational guard, without a new numeric decision. Thus
(5),(6) are computable without interpreting any S value or evaluating
an oracle, conditional on that producer provenance and fixed coupling.

This identifies a possible cheap DATA-only follow-up on the already
accepted511 kept records. It is NOT executed, released, or needed for
this PAPER theorem. No strict saving at511 is asserted. A future
separately frozen/released structural count would preserve all old
records, keep all13 grid keys, report D and Q separately, and accept
zero saving without guard retuning. It would not be a native benchmark,
new oracle, new degree or new scientific case.

No conclusion about runtime, CPU/wall, byte caps, invocation success,
current parser acceptance or changed fresh enclosures follows from
finite key inclusion. Current source still recognizes its old E15
guard and descriptors; any actual F07 integration requires a separate
focused source contract/review/release. The already delivered Syvert30
scientific source, oracle, worklist and proof path remain untouched.

## Checks, provenance and history

Only PAPER induction, exact hand rational geometry, read/search/hash
metadata and owned prose. ZERO scripts/imports/calculators/data replays,
numerical oracles/degree endpoints/native/phase/quadrature/compiler/
fixtures/pack jobs. No author/shared source, evidence or Git mutation.
Author read-back is not independent verification. Distinct mathematical
review and root adoption remain required; final Claude and prior findings
are separate.

2026-11-07, requested/API Codex gpt-6.1-sol xhigh. Rules read at
4a5de2012bad94601c713b2ff5517f2e3fb80af2. Completed gate preceded root's
durable exact F10 campaign/LOG registration and SEPARATE PAPER release.
The local idea4461B and attempt4978B were written BEFORE derivation;
their preserved prospective prefixes have hashes
39d7e35282efc440d00549a9164daceb1eddc454a910dbd6fedaf4a92650a8ba
and74288a4816fd975f2f94f9b8f85f8239dcf14dcc5d1f252f6d36e001269b0fce.
This is the allocated tenth analytic round, with no further research
round, replay or source execution launched.


## Root disposition after distinct mathematical acceptance —2026-11-07

Root adopts the exact mathematical statement under its written quantifiers, hypotheses and dependencies. The original frozen proof/record prefix is preserved and identified in [independent review](../independent-checks-F08-F10.md), final SHA2561e63875c450d08f87b4b2b24934bf8baad67958f727b8df3e789998757db9d72. No global-onset change, new finite degree, source integration, strict runtime saving, novelty/priority verdict, protocol waiver or readiness follows beyond the exact statement. Final Claude review remains separate.
