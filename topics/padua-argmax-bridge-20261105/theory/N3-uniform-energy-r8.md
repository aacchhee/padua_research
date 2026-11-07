# PD-T?argmax-bridge-codex-N3-uniform-energy-r8-01 — A logarithmic energy remainder and explicit eventual bootstrap premise

ID kind: PD-T.
Aliases: N3 round8 analytic energy subtask; common-gradient weighted l2;
diagonal logarithmic mass; explicit eventual three-quarter energy.
Split from: the quantitative continuation of IDEA-330/457 and the OPEN
all-degree energy premise of N3-bootstrap-corner.md. The original
all-n target is retained there and remains OPEN here.
Split into: none. The onset below is a routine algebraic corollary of
the main bound; no new negative result is asserted.

## Statement

For every integer n>=32, use precisely the corrected even-checkerboard
Padua cardinals of PD-T101. Let Lambda_c and W_n be the exact corner
mass and physical weighted gradient energy of PD-T227. Write

    m=n+1, P=nm, H=1+log m.

Then

    W_n <= n^4[(21/32)Lambda_c+1500000000 H].                 (1)

Consequently, with the explicit integer onset

    N_E=ceil(exp(128000000000)),

every integer n>=N_E satisfies the unchanged bootstrap energy premise

    W_n <= (3/4)n^4 Lambda_c.                               (2)

Both inequalities transfer to the other parity-correct nonnode corner.
N_E is a sufficient energy onset, not a first crossing, a usable finite
bridge, or a global argmax onset. The range129<=n<N_E is not resolved
by (1), (2), or the existing finite2..128 energy theorem.

## Definitions and assumptions

All arithmetic and logarithms are exact real quantities. At the
canonical nonnode corner c=(-1,-1),

    W_n=sum_(L_jk(c)!=0)
        [L_jk,x(c)^2+L_jk,y(c)^2]/|L_jk(c)|.

Indices satisfy0<=j<=n,0<=k<=m,j+k even. The positive weights are
w_jk=2 epsilon_j eta_k/P with endpoint factors1/2. The removable00
cardinal is included. Precisely k=0,j>0 even are omitted from W;
their equal inward gradient components remain included in the slopes
of PD-T227/251 and in the inherited bootstrap theorem.

For a regular nonzero index put

    u=j*pi/n, v=k*pi/m, a=cos u, b=cos v,
    C=1-b, A=1-a, d=b-a,
    V=|L_jk(c)|=2w_jk C/|d|,
    q_x=L_jk,x(c)/L_jk(c), q_y=L_jk,y(c)/L_jk(c).

Here k>=1 and d!=0. The diagonal consists of j=k>=1; all remaining
regular nonzero indices are off-diagonal. H is a logarithmic factor,
not the physical increment used under the same letter in older local
radius records. P=nm is a mesh product, not a node count or PD-T271's
N=n+1/2.

## Status by part

Overall status: **PROVED**, analytic bound (1) and routine corollary (2).
The complete proof below uses no numerical observation or finite sweep.
This is a developer proof, not independent acceptance or formal audit.

| Mathematical part | Status | Evidence / limit |
|---|---|---|
| Explicit leading-plus-logarithmic bound (1), n>=32 | PROVED | Written weighted-square estimate below |
| Three-quarter premise (2), n>=N_E, and corner transfer | PROVED routine corollaries | Explicit lower-bound absorption and inherited reflection |

Candidate disposition: retained quantitative variant of IDEA-457/330.
The separate original target W_n<=(3/4)n^4 Lambda_c for every n>=129
remains OPEN on129<=n<N_E. No narrower statement silently replaces it.

## Depends on

- PD-T227: exact corner mass, physical gradients, zero mask and00 term.
- PD-T367, proof §§1–4: exact ratio difference, diagonal cancellation,
  off-diagonal weighted square bounds and endpoint-inclusive index sums.
  Their precise intermediate statements are repeated below; its coarse
  final constant10^10 is not used to infer a sharper constant.
- PD-T157(1): Lambda_c>=(4/pi^2)log^2 n-54 for every n>=2.
- PD-T251 / PD-T367's reflection argument: the same corner mass and
  energy at both parity-correct nonnode corners.
- N3-bootstrap-corner.md only for the stated application of (2), not
  as an input to the proof of (1) or (2).

PD-T271 was read to check the corner normalization and explicit remainder
domain. Its sharper expansion and numerical c enclosure are not needed;
the older elementary PD-T157 lower bound suffices. No global norm upper
bound, known argmax, fitted coefficient, uniform per-cardinal O(n^2)
ratio, or sign preservation is assumed. PD-N085 remains valid.

## Proof

### 1. Exact decomposition and inherited quantitative estimates

PD-T227 and PD-T367 §1 give

    q_x=-n^2/2+T_2+T_3+T_4,
    T_2=n(ab-1)/(Cd), T_3=-a/d, T_4=2(1-a^2)/d^2,
    R:=q_y-q_x=-(2n+1)/2+A/d.                              (3)

For clarity the last identity follows by subtracting the exact x and y
ratios: the nonconstant difference is
(1+2b+a)/d+2(a^2-b^2)/d^2=(1-a)/d. Thus no angular derivative or
approximate near-collision expression replaces a physical ratio.

The following proved bounds from the indicated parts of PD-T367 hold
for every n>=2, so in particular for n>=32:

    q_x^2+q_y^2 <10000 n^4                    (j=k>=1),   (4)

    sum_off V T_2^2 <=360000 n^4 H,
    sum_off V T_3^2 <=976 n^4,
    sum_off V T_4^2 <=32000000 n^4 H,
    sum_off V/d^2 <=976 n^4.                              (5)

Equation (4) is PD-T367 §2's pair |q_x|<30m^2,|q_y|<31m^2
together with1861(m/n)^4<10000, valid since m/n<=3/2. Its
diagonal cancellation must be retained; bounding its singular terms
separately would not prove (4).

For (5), PD-T367 §§3–4 set

    L=|j-k|>=2, D=min(j+k,2n+1-j-k)>=1,
    |d|>=DL/m^2, C>=2k^2/m^2,

and prove the termwise majorants

    V T_2^2 <=22500 n^4 D/(k^2 L^3),
    V T_3^2 <=61 n^4/(D^3 L^3),
    V T_4^2 <=2000000 n^4/(D L^5).

The positive sums of their rational factors are respectively bounded
by16H,16,16H, using at most two j for fixed(k,L) and at most four
index pairs for fixed(L,D). These are exactly its endpoint-inclusive
finite index sums. The same middle majorant holds for V/d^2 because
it was derived using |a|<=1: directly,

    V/d^2 <=8m^5/[n D^3 L^3]
           <=61n^4/(D^3 L^3).

Hence its sum is at most976n^4. This verifies the last line of (5)
without incorrectly inferring an upper bound on V/d^2 from an upper
bound on V a^2/d^2. All regular nonzero off-diagonal indices, including
j=0,j=n and k=m where admissible, are covered; 00 and the zero row
are excluded from these sums exactly as defined above.

### 2. The diagonal mass is only logarithmic

Write

    D_n=sum_(j=k>=1) V.

For these indices,0<v<u<=pi and

    s=(u+v)/2=pi*j*(2n+1)/(2P),
    t=(u-v)/2=pi*j/(2P), d=2sin s sin t>0.

Since w<=2/P and C=2sin^2(v/2),

    V <=4sin^2(v/2)/(P sin s sin t).                         (6)

First suppose1<=j<=n/2. Then0<t<=s<=pi/2. The chord lower
bound sin z>=2z/pi on[0,pi/2] and sin(v/2)<=v/2 give

    V <=pi^2 v^2/(4P s t)
       =pi^2*n/[m(2n+1)] <5/m.                            (7)

There are at most n/2 such indices, so their total mass is less than5/2.

For integer j>n/2 one has j>=(n+1)/2=m/2, so s>pi/2,
while0<t<pi/2. Put r=n-j>=0. Since

    pi-s=pi[(2n+1)r+n]/(2P)
          >=pi(r+1/2)/m,

the chord bound applied to pi-s and to t, and sin^2(v/2)<=1,
give

    V <=pi^2/[P(pi-s)t]
       <=2m/[j(r+1/2)] <=6/(r+1/2).                       (8)

The final inequality uses j>n/2 and m/n<=3/2. For any of the finite
r ranges here, the r=0 term contributes2 and
sum_(r=1)^R1/(r+1/2)<=sum_(r=1)^R1/r<=1+log n;
the empty R=0 sum also obeys that upper bound. Combining (7),(8),

    D_n <5/2+6(3+log n)
         =41/2+6log n <=21(1+log m)=21H.                  (9)

The ordinary endpoint j=n is included in (8) at r=0; its half weight
was only enlarged by the bound w<=2/P. No endpoint is lost. Equations
(4),(9) prove

    W_diag <=210000 n^4 H.                                (10)

This is the needed refinement: multiplying (4) by all of Lambda_c
would lose the leading coefficient required in (1).

### 3. Preserve the common term in the off-diagonal square

At every regular off-diagonal index put

    b_0=(-n^2/2,-n^2/2),
    r_x=T_2+T_3+T_4, rho=(r_x,r_x+R),
    (q_x,q_y)=b_0+rho.

For any two real vectors, the elementary inequality
2b_0.rho<=(1/4)|b_0|^2+4|rho|^2 gives

    q_x^2+q_y^2 <=(5/4)|b_0|^2+5|rho|^2
                  =(5/8)n^4+5|rho|^2.                    (11)

Also

    |rho|^2=r_x^2+(r_x+R)^2 <=3r_x^2+2R^2,
    r_x^2<=3(T_2^2+T_3^2+T_4^2).

As A<=2 and(2n+1)/2<m, (3) implies

    R^2<=2m^2+2A^2/d^2<=2m^2+8/d^2.

Let Lambda_off=sum_off V<=Lambda_c. Summing these inequalities
and using (5) yields

    W_off <=(5/8)n^4 Lambda_off
              +45sum_off V(T_2^2+T_3^2+T_4^2)
              +20m^2 Lambda_off+78080n^4
           <=[(5/8)n^4+20m^2]Lambda_c
              +1456200000 n^4 H+122000n^4
           <=[(5/8)n^4+20m^2]Lambda_c
              +1456322000 n^4 H.                         (12)

The constants are exact:45(360000+32000000)=1456200000,
45*976=43920, and43920+78080=122000. The last step uses H>=1.

For n>=32,

    20m^2/n^4 <=20*33^2/32^4 <1/32,

since21780<32768. Hence

    W_off <=(21/32)n^4 Lambda_c+1456322000 n^4 H.          (13)

This is a weighted square estimate. It neither asserts nor requires
that rho, r_x, q_x or q_y be bounded by a fixed multiple of n^2 at
each index. Thus the superquadratic ratio of PD-N085 is compatible
with every inequality above.

### 4. Retain the removable00 term and assemble

PD-T227 gives its exact energy

    W_00=(2n^2+1)^2/(36m)+m(2n+1)^2/36
         <=n^4/(4m)+mn^2/4 <n^4.                          (14)

For example, n>=2 and m<=3n/2 bound the two final terms by
n^4/12 and3n^4/16, respectively, whose sum is less than n^4.
Adding (10), (13), (14), and H>=1 gives

    W_n <=(21/32)n^4 Lambda_c+1456532001 n^4 H
         <=(21/32)n^4 Lambda_c+1500000000 n^4 H.

This proves (1), with a positive unused allowance43467999 in the
logarithmic coefficient.

### 5. Explicit absorption and reflection

Put ell=log n. For ell>=20, PD-T157 and pi^2<10 give

    Lambda_c >=(2/5)ell^2-54 >=ell^2/4,
    H=1+log(n+1)<=ell+1+log(3/2)<=2ell.                    (15)

The first inequality uses(3/20)ell^2>=60>54; the second uses
log(3/2)<1/2 and ell>=20. If ell>=128000000000, then

    1500000000H <=3000000000ell
                 <=3ell^2/128 <=(3/32)Lambda_c.           (16)

Inserting (16) into (1) proves (2), since21/32+3/32=3/4.
The integer choice N_E above ensures the required logarithmic
condition without any floating evaluation of exp or ceil.

For even n, reflection j->n-j in the x coordinate preserves the
checkerboard and weights. For odd n, m is even and reflection k->m-k
in the y coordinate does so. Cardinal uniqueness therefore permutes
the corrected cardinals. Their absolute corner values and squared
physical gradients, and hence Lambda_c and W_n, agree at the two
nonnode corners. This transfers (1),(2) as claimed. QED.

## Checks, scope and open items

Analytic only; no numerical or symbolic diagnostic, energy sweep,
producer rerun, phase job or independent execution was performed for
this result. The fixed2..128 theorem is an independent prior result,
not evidence for (1) or (2). No constant was fitted to its endpoints.

By the inherited bootstrap theorem, (2) excludes offcorner global
maximizers in0<z=n^2(h_x+h_y)<=1/8, and hence in the inward half-phase
diamond, for every n>=N_E. A strict complement cover remains necessary
for global equality. This application is maximum exclusion, not a
pointwise descent predicate before global closure.

The original requested uniform energy bound for n>=129 remains OPEN
on129<=n<N_E. No global degree extension, practical bridge, effective
argmax onset, cost law, model correction or proof of PD-T099 follows.
The next useful refinement must reduce the explicit residual constant
or directly control that intervening range, rather than extrapolate
from finite2..128 data. Separate independent reconstruction and the
required formal Claude audit are the orchestrator's next checks.

## Sources and history

No external theorem or historical novelty claim. All load-bearing
mathematics is the locally proved PD-T227/367/157 content and the
explicit estimates above. Prior-source search and gate timing are
recorded once in ../ideas/N3-uniform-energy-r8.md; execution/provenance
is in ../attempts/N3-uniform-energy-r8.md.

2026-11-06, Codex mathematical worker, inherited parent allocation;
actual serving model/effort not independently exposed. Rules/input
8dc1521cf68f7780bd10e02495f6f71a639c03c6. Scoped subtask of N3 round8.
Only the three assigned new files are written; no shared records or
Git state changed. Threshold3/4, existing masks, derivative conventions,
bootstrap model and finite theorem remain unchanged.
