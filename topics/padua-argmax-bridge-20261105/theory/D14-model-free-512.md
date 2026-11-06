# PD-T?argmax-bridge-codex-D14-512 — Degree512 argmax without the completed-model norm

ID kind: PD-T.
Aliases: model-free degree512 finite certificate; quarter-grid global
norm30; existing three actual plus53 primitive points.
Split from: D14 dependency simplification.
Split into: the all-n analytic finite-grid implication is in
`D14-grid-norm.md` and is not proved by this instance.

## Statement and status

Fix n=512,m=513, the original corrected even-checkerboard Padua
cardinals of PD-T101/PD-T364, and Lambda_c=lambda_512(-1,-1).
The existing D09 three ACTUAL point enclosures and existing D12
53 common-S point enclosures, at their exact rational-turn inputs,
establish

    S_512(alpha,beta)<30 for ALL real alpha,beta,
    max_[-1,1]² lambda_512=Lambda_c,
    argmax_[-1,1]² lambda_512={(-1,-1),(1,-1)}.       (1)

This is the SAME degree and equality set as D12, with a smaller
mathematical dependency graph. It is not a new degree certificate,
historical speedup, sharper analytic onset or priority claim.

Overall status: **PROVED developer computer-assisted application**.
Distinct review of the NEW D14 norm/application is pending. Root's
D12 fresh native replay is separately reported complete; its final
review/essential receipt is being completed by its own owner. This
file does not self-approve either review or change the adopted graph.
Final Claude audit remains separate.

## Exact inputs and retained numerical trusted base

The D14 metadata receipt is
[`d14-grid-norm.json`](../evidence/d14-grid-norm.json),4243bytes,
SHA256 `66a65cb456a2665ac76acd9834ae2164331bcdbb7d101f738a5f39cf41e6a6bd`.
Its fixed source is
[`check.py`](../code/post_audit_D14_grid_norm/check.py),7537bytes,
SHA256 `e79eb19f17d9651a9eb4ef3f29aa8732653dcb611d17c301349b687d65a21350`.
One preregistered metadata-only execution used0.060840548CPU through
the final arithmetic sample, under hard2CPU, with ZERO native calls.
The tiny final JSON write lies after that sample under the same hard
limit. No numerical/kernel/phase/board/quadrature/root/degree job ran.

The reader checked these unchanged inputs:

| Input | SHA256 |
|---|---|
| D12 complete author raw checkpoint,37857B, local-output/.../post-audit-D11/point-cover/checker-checkpoint.json | b1747afae4b6cbd6f53eb4604e214056b8aa128ffbbbf2033a39b714e7658bb8 |
| Essential D12 result,10972B, evidence/d12-point-cover.json | 5404f0b9679db125640ece212c85f86dfa7cfac13a41a9956c290e2804fe33c4 |
| Complete D12 tree,147B, evidence/d12-point-cover-tree.json | 62a0f35a51730ab57b0a0931122b9cab7c6ca1d113ea38dc779a059ade3eda2e |
| Essential D09 actual-point receipt,11236B, evidence/d09-threepoint.json | 34553e6d91dc77285f1bbb277a0f519c5a8a5da5f27a8f43501c7caf13631509 |

All53 raw rows were complete and unique, with exact equality between
the native raw hexadecimal endpoint, retained endpoint hex and saved
rational endpoint. `Fraction.from_float(float.fromhex(...))` preserves
the finite outward binary64 endpoint EXACTLY. All15 quarter-triangle
points reduce to13 canonical keys, all present among those53 rows;
there are no missing inputs. The compact D14 receipt retains every
grid key, canonical key, exact upper and upper hex. No raw checkpoint
is needed merely to inspect those13 norm premises. The raw checkpoint
remains provenance and the exact helper's pinned input; permanent raw
cold-storage retrieval is still pending under the existing policy.

The outwardness of a saved endpoint is established by the accepted C11
finite point-source/tail contract and actual D12 execution, with its
distinct fresh-build replay. Metadata consistency alone does not prove
that outwardness. The existing Arb/FLINT/GMP/MPFR, compiler, full-tail
and outward-export trusted base remains exactly as documented in
D12-global512.md and the D09 actual-point application. Neither an
old binary nor the FLOAT producer arithmetic is a proof premise.

## 1. Global norm30 from the fixed saved grid

Use the general all-n finite-grid theorem with the15 fixed triangle
grid vertices. Their maximum certified upper occurs at key(0,0):

    V=3556138968885113/140737488355328.

This is a certified upper of the finite grid maximum, NOT an asserted
global maximum and not an assumed Lambda_c identity. The exact test is

    30*663-784V=703480736346583/8796093022208>0.

Consequently the independent analytic norming implication gives

    M_512*<=784V/663
      =13403908421182349/448600744132608<30.         (2)

It follows that30 bounds S globally, physical lambda and both complete
signed families. No completed model/error, PD-T271 scalar constant,
accepted D09 norm34 or expected argmax has been used to obtain(2).

## 2. Re-establish the actual-corner patch with30

Retain the certified true-corner LOWER

    L=7112277937770225/281474976710656<=Lambda_c

and the same three ACTUAL lambda UPPER endpoints, in order x,y,xy,

    Ux=3148016308623273/140737488355328,
    Uy=6644655510519255/281474976710656,
    Uxy=2916781692560455/140737488355328.

Their normalized PHASE endpoints are(pi/4,0),(0,3pi/16),
(pi/4,3pi/16); the inward PHYSICAL angle turns are respectively
(1/2048,0),(0,1/2736),(1/2048,1/2736). These are the accepted D09
point premises, independent of its previously chosen norm34.

Let p=22/7,kappa=512/513,u'=1/32,v'=9/512 and set

    q=min((L-Ux)/u',(L-Uy)/v',(L-Uxy)/(u'+v'))
      =816245320523679/8796093022208.

The D08 squared-phase ACTUAL-cardinal theorem, with the now independently
proved GLOBAL M=30, has the exact sufficient test

    q>30*p^4*max(u',kappa^4*v')/6=73205/4802.

The saved exact arithmetic gives

    gap=1637846019731984959/21119419346321408>0,
    epsilon_lower=gap/p²
      =1637846019731984959/208608142114684928>38/5.   (3)

Thus on BOTH closed actual inward rectangles
0<=alpha<=pi/4,0<=beta<=3pi/16 the original corrected lambda obeys

    lambda<=Lambda_c-(19/5)(alpha²+beta²).           (4)

The true origin remains symbolic in D08's positive bilinear loss
argument; only L minus the actual point uppers supplies the losses.
The norm now comes from(2), so this reconstruction does not cite the
old D09-patch statement as a black box with its norm34 dependency.
It cites only D08's pure theorem and the independently accepted actual
point enclosures. The even-n x reflection gives the second corner.
Since pi/4>1/2 and3pi/16>1/2, both rectangles contain the full closed
inward phase half diamond alpha+beta<=1/2. No S interpolation in
squared phases, finite energy sweep or sign-stability premise is used.

## 3. The SAME complete tree and every physical center

Use the unchanged D12 83-node tree, root[0,1]², exact midpoint splits,
42closed leaves and53 canonical point inputs. It is a complete binary
partition, clipped to T. Retain the original leaf tags:31 FAR,
8 NEAR,3 OUTSIDE. The three outside rectangles satisfy a_l+b_l>1;
closed tangencies stay in the cover. At every other rectangle set

    U_B=max_(four raw vertices) U
       +(30*p²/8)[(a_h-a_l)²+kappa²(b_h-b_l)²].     (5)

Only S evaluation keys are folded; actual rectangle geometry, signed
physical center and radius guards are untouched. The finite norm(2)
and D08 ordinary Peano establish S(pi*a,pi*b)<=U_B throughout B.
The original34 bounds are monotone increasing in M, so every original
strict comparison remains valid at30. The independent pure D14
reader also decoded the entire fixed tree and recomputed these
comparisons, giving minimum exact positive margins

| Retained tag | Count | Required margin at30 |
|---|---:|---|
| FAR |31| L-U_B >=1220840625178958669/151237454964681867264>0 |
| NEAR |8| L-U_B+1/32 >=15969326879182055749/1209899639717454938112>0 |
| OUTSIDE |3| a_l+b_l>1, exact emptiness |

The helper's literal34 is used only to recover the historical tag
selection; it then checks EVERY required inequality directly at30.
Neither that tag selection nor the new proof assumes that34 was a
valid global norm. The model-derived34 theorem is not a premise.

Every NEAR leaf retains the exact guard

    2*p*min(a_h+b_h,1)<=1,

so every point of its clipped patch has ACTUAL signed phase radius
rho=pi(a+b)<=1/2. No cut-crossing SPLIT leaf occurs in this instance.

For any physical point PD-T364 supplies an admissible odd physical
center(J,K),0<=J<=512,0<=K<=513,J+K odd, with signed phases
rho=|alpha|+|beta|<=pi. Every physical point, square edge, node and
chart tie is included; this is the exact odd-vertices L1-distance
cover, not a sampled center reduction. Set a=|alpha|/pi,b=|beta|/pi.
Some closed tree leaf contains(a,b) in T and cannot be OUTSIDE.

On FAR, lambda=S-Delta<=S<=U_B<L<=Lambda_c. On NEAR at a
NONCORNER physical center, C02's n>=160 dense-band theorem applies
at the guarded radius and gives Delta>1/32. Hence
lambda<=U_B-1/32<L<=Lambda_c. Every noncorner center has an
interior coordinate, so one of the two projected C02 floors applies;
the projections are never added. On NEAR at an ACTUAL corner,
admissibility makes the signed phase inward and(4) gives strictness
unless both phases vanish. At zero phase the point is exactly the
corner and PD-T364 gives Delta=0,S(0)=Lambda_c. The only odd
endpoint centers are(0,513),(512,513), corresponding to(1,-1),
(-1,-1), with equal values by the node-preserving x reflection.
This proves(1), including every closed boundary and equality case.

## Dependency change and limits

The mathematical chain for this application is:

    finite corrected kernel + period/evenness + signed Bernstein
      -> ordinary Peano + compact continuous norm + 13 saved S uppers
      -> global norm30
      -> SAME 3 actual-point losses + pure squared-cardinal Peano
      -> actual corner patch
      -> SAME53 S uppers + C02/PD-T364 + SAME closed tree
      -> exact degree512 two-corner argmax.

D09's completed-model norm34, D05 completed-model error, D06's uniform
completed-model numerical budget and PD-T271 corner-constant enclosure
are absent from this proof graph. Their valid results, source/evidence
identities and old audited application remain unchanged. The separate
D06 finite algebraic actual-row reduction and C11's complete numerical
tail/source validation remain part of the point-enclosure trusted base;
the term model-free does not mean free of validated numerical arithmetic.

This is a dependency simplification, not independent new native evidence.
The D14 source/receipt/proof need a distinct mathematical review, and
the original actual enclosures retain their own independent-replay
obligations. Root alone adopts any model-dependency removal. No shared
registry, old proof/source/evidence, degree range or published scientific
state has been changed by this worker.

2026-11-06, Codex gpt-6.1-sol xhigh, input/rules
`e13a538bda80e6cc785f4835937b2ca338bc1d6f`. Prospective gate and exact
resource/source history: `../attempts/D14-grid-norm.md`.


### Supplementary review closure — 2026-11-06

Distinct mathematical reconstruction ACCEPTED this unchanged developer
scope; [independent-checks-D14-grid-norm.md](../independent-checks-D14-grid-norm.md),
report SHA256b3050a39d9fec8ed8c101f8cbd2c5bf116ce39fadf42be9d9813b5e12da11d6e.
The preceding pending supplementary-review wording is historical. Exact
review scope, process notes and computational provenance remain in that
report. Final Claude audit is separate; executable instance/source release
is not implied by acceptance of a sufficient mathematical contract.
