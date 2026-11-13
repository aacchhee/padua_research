# T8 mathematical development reconstruction — 2026-11-06

Role: supplementary **mathematical development validation**, assigned
gpt-6.1-sol xhigh by the root orchestrator. Runtime identity/effort is not
independently exposed. This is not the Claude audit, not the separate
Astra mathematical audit, and not a retrospective change to the original
T8 worker's assigned Sol high allocation. The reconstruction below supplies
new xhigh mathematical development against the exact inputs identified here.

Rules were read at e5b64450fce42262dafc88ee357b72e5f203916b and reread
unchanged after the known120a19ee71baa8e7834b3b183798df2cf489c432
integration. AGENTS, WORKFLOW, CODEX, handoff04's model/scope/D3 requirements,
the T8 gate, attempt and preregistration were read for this task. The prior
full IDEAS gate was completed in this worker's T9 development; this task
introduces no candidate, novelty/priority claim or new literature premise.
It reconstructs only four new T8 analytic statements. Frozen T9 files and
all original T1–T6 claims remain outside this task's edit/re-audit scope.

## Exact inputs

Paths below are relative to topics/padua-3d-20261106. These hashes identify
the read prose; no checker pins prose and no result-bearing code was changed.

| Input | SHA-256 |
|---|---|
| theory/t8-cyclic-reduction.md | 1b07d850cd3e7ab49ac11d0cc4862e4b441ce47fcdf7f08263442031c44af276 |
| theory/t8-phase-obstructions.md | b8f1c31a8e2269ec19a756298712e2167a499035699883890073cfbe9d30427d |
| theory/t8-even-parity.md | e24e8ab03ac603003f5c0fe37fae0b0636b36fa912816a068a293855c247149a |
| theory/t8-phase-order-obstruction.md | 40a0e6e61797f1e0efee65b22565daf0ceb5535b2f878e1081786cfe5b25b573 |
| novelty-gate-T8.md | bcc55a3975cdf0b5ecb2974ec71f6cade7166930959f0271852cb3b5d3573d33 |
| attempts/T8.md | a79981c00d6ffa08ad21b0c816672dd33095474b4bd0dc1e4451a858c8d019ac |
| preregistration-T8.md | 8cad326a7fea6d7c2b629d6417f222756a61a60a714affaa3daf5564351754a9 |

## 1. Primitive cyclic reduction and Padua admission

Let h generate a finite subgroup H of (R/Z)^d, of order M. Then Mh=0,
so h=z/M. Its order is M/g, where g=gcd(M,z₁,…,z_d): M/g annihilates
all coordinates, and Bezout shows that any annihilating k satisfies
M|kg, hence M/g|k. Thus true order M is exactly primitivity g=1.

For a fixed physical node, each coordinate cosine has at most two torus
preimages. Its fibre within H therefore has at most2^d points, including
endpoint degeneracies. Consequently |H|=M≤2^d|cos(2πH)|. This proves
the finite order cap for fixed N independently of all census outputs.
The same fibre estimate holds for translated cosets, but supplies no
finite reduction of their continuous phase parameter.

For zero phase the equality criterion is precisely r≡±s mod M in each
coordinate. The canonical folded angle is min(r mod M,−r mod M)/M,
in[0,1/2]; cosine is injective there. Reduced fractions therefore decide
cross-order node equality exactly. Multiplying z by a unit only permutes
k; independent coordinate sign changes leave each cosine unchanged;
coordinate permutations are cube isometries. Folding/sorting generator
coordinates followed by unit-orbit marking consequently loses no class.
Neither primitivity nor that quotient permits deleting zeros, repeated
coordinates or no-unit-coordinate tuples without a separate rank reason.
This validates the analytic reduction, not its implementation or census.
Angle reflection θ_j↦−θ_j is the reflection meant in the subgroup control;
it should not be confused with the physical cube sign change x_j↦−x_j.

For d2 Padua take M=2n(n+1), z=(n+1,n). Coprimality makes the true
order M. The parameter k produces angle indices i=k mod2n,
j=k mod2(n+1). Generalized CRT admits exactly i≡j mod2 and one
k per such pair modulo M. Folding i to[0,n] and j to[0,n+1]
preserves parity, hence gives exactly the usual even checkerboard.
For n=2m the count is(m+1)²+m(m+1); for n=2m+1 it is
(m+1)(m+2)+(m+1)². Both equal(n+1)(n+2)/2. Also
2n(n+1)≤4·(n+1)(n+2)/2. Thus the full finite reduction includes
Padua for every n≥1, without a unit-coordinate assumption. This derives
count/admission only; no old Padua interpolation proof is re-audited here.

## 2. Even half-grid involution and all-degree trace

Now let d3, N=binom(n+3,3), M=2N−2, z=(1,b,c), zero phase,
n≥2. Equality in the first coordinate forces l=±k mod M, and either
choice gives equality in all coordinates. The nodes are exactly the
global-inversion classes [k]={k,−k}; the two singleton parameters0,M/2
give M/2+1=N nodes.

The half-period map[k]↦[k+M/2] is the physical sign change on the r odd
coordinates, with1≤r≤3. A fixed class requires2k≡−M/2 mod M.
There are no solutions if M≡2 mod4. If4|M, the two solutions M/4,
3M/4 form one inversion class, so the number of fixed physical nodes
is f=1; otherwise f=0. Thus the nodal involution has trace f and
eigenspace dimensions(N±f)/2.

On Π_n³ the monomial x^α has eigenvalue(-1)^{α₁+…+α_r}, after
relabeling coordinates. Summing exact total degrees up to n contributes
an extra factor1/(1−t), so the trace coefficients are

Σ_{n≥0}D_r(n)t^n=(1−t)^{−(4−r)}(1+t)^{−r}.

For r1 rewrite this as(1−t)^{−2}(1−t²)^{−1}; hence
D₁(n)=Σ_{j=0}^{floor(n/2)}(n−2j+1). For r2 it is
(1−t²)^{−2}. For r3 it is the r1 series evaluated at−t.
Therefore, independently extracting coefficients,

| r | D_r(2m) | D_r(2m+1) |
|---|---:|---:|
|1|(m+1)²|(m+1)(m+2)|
|2|m+1|0|
|3|(m+1)²|−(m+1)(m+2)|

Evaluation intertwines the two real involutions. If bijective it identifies
their plus and minus spaces, so D_r(n)=f is necessary. For n≥2 the
r1/r3 values have absolute value≥4. For even n the r2 value is≥2.
Only odd n with r2 can survive. At odd n the product(n+1)(n+2)(n+3)
has at least three powers of2, so N is even (indeed divisible by4);
therefore M≡2 mod4, f=0, consistent with D₂(n)=0. This is a necessary
condition, not a construction or sufficiency claim.

The same reasoning gives the general finite-dimensional ceiling
rank(E)≤N−|D_r(n)−f|/2 in this N-node situation, by summing the smaller
domain/codomain dimension in each sign sector. The source theorem needs
only the weaker trace obstruction and uses no computed rank as a premise.

## 3. Every continuous phase at modulus ten

Let X be the full ten-parameter image with arbitrary integer z and real
phase φ. If |X|<10, dimension alone prevents injectivity of Π_2³,
which has dimension10. If |X|=10, parameterization is bijective and
k↦k+5 induces a fixed-point-free involution on X. Its physical action
flips exactly the r odd coordinates of z, since adding πz_j changes
cosine by(-1)^{z_j}, independently of φ. All-even z would already
give repeated parameters, so r∈{1,2,3}. Nodal sign spaces have dimensions5/5.

Write σ_j=±1 and s=Σσ_j=3−2r. On Π_2 the trace equals
constant1 + linear trace s + square trace3 + mixed trace(s²−3)/2.
This is4,2,4 for r1,r2,r3. The polynomial dimensions are consequently
7/3,6/4,7/3. Intertwining bounds the respective ranks by
min(7,5)+min(3,5)=8, min(6,5)+min(4,5)=9, and8. None is10.
The derivation handles every phase and all fold strata: folded cases
are in the dimension branch, and the ten-node branch forces a free action.
It requires no finite phase census or generic-phase assertion.

This excludes exactly an every-degree-n≥2 single cyclic family with
M=N, since n2 forces M10. It does not exclude another order, a union,
an omitted-degree sequence, or arbitrary translated interpolation.

## 4. D3 Padua trace consistency

In the d2 Padua representation exactly one of n,n+1 is odd, so a
half-period shift flips one physical axis. If n=2m, it flips x and
fixed nodes have i=m; j runs over the m+1 indices of matching parity
in[0,2m+1]. If n=2m+1, it flips y and fixed nodes have j=m+1;
there are m+1 matching i in[0,2m+1]. Thus f=floor(n/2)+1.
The single-axis polynomial trace in Π_n² has generating function
1/[(1−t)(1−t²)], also giving floor(n/2)+1. This verifies D3 for
every n≥1. The modulus-ten theorem's equal-dimensional bijective
parameterization cannot be imposed on the usual Padua folded orbit.

## 5. PK, PT and PO quadratic identities

At n2, t=πk/5 and the frozen phases are(π/2,π/3,π/4).
The generators reduce to(1,3,9),(1,3,6),(1,5,3). Write x,y,w for
the coordinates, so x=−sin t in all three cases.

For PK the two coordinate angles satisfy θ_x+θ_w=3π/4 mod2π.
The elementary relation cos²u+cos²v−2cos(u+v)cos u cos v
=sin²(u+v) gives x²+w²+√2xw−1/2=0, a nonzero quadratic.

For PO, y=cos(πk+π/3)=(-1)^k/2, so4y²−1=0.

For PT, reducing6t modulo10t gives

w=(cos4t+sin4t)/√2,
T₂(w)=−sin2t,
T₂(y)=−cos4t/2+√3 sin4t/2,
xy=−sin4t/4+sin2t/4+√3 cos2t/4−√3 cos4t/4,
T₂(x)=−cos2t.

Let A=2−2√3/3. In the displayed source polynomial, the w term
contributes A to both cos4t and sin4t. The T₂(y) term contributes
−1+2√3/3 to cos4t and√3−2 to sin4t. The xy term contributes
−1 to cos4t, −√3/3 to sin4t, +√3/3 to sin2t and+1 to cos2t.
The remaining terms contribute−√3/3 to sin2t and−1 to cos2t.
Thus every coefficient cancels, proving the identity. Its x² coefficient
is2, so it is a nonzero member of Π_2. These identities independently
prove the three injectivity failures; no cyclotomic rank receipt is used.

Cardinality ten also has a direct elementary verification here. Equality
of x at parameters k,l gives either k=l mod10 or k+l=5 mod10.
For the second option, with the odd second generator b∈{3,5},
y(l)=−cos(bt−π/3). Equality with y(k)=cos(bt+π/3) would force
cos(bt)=0. But t=πk/5 would then require2bk≡5 mod10, impossible
by parity. Hence distinct parameters already have distinct(x,y), proving
ten distinct triples for all three rules without enumerating their nodes.
Their odd-coordinate counts are3,2,3, respectively, consistent with
the analytic rank ceilings8,9,8; exact equality to those ceilings is
outside this analytic reconstruction.

## Development disposition and limits

All four analytic statements reconstruct under their explicit hypotheses;
no mathematical finding requires a material source-proof correction.
The direct cardinality derivation above supplies a written check of the
ten-node side statement without importing numerical enumeration.

Only shell reads/searches and sha256sum were executed. No mathematical
script, census, rank calculation, equality screen, quality computation,
source fetch or Git command was run for this task. Consequently this record
does not validate enumeration completeness in executable code, numerical
quality, exact finite rank equalities, source novelty, or the original
worker's historical provenance. Those retain their separate records and
the planned Claude/Astra checks. No source theory, script, receipt, registry,
T9 file or handoff was modified; this single development record is the output.
