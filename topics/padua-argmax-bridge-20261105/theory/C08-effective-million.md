# PD-T?argmax-bridge-C08-global — Exact two-corner global argmax from degree one million

ID kind: PD-T. Aliases: practical effective upper boundary; million-degree
analytic tail. Split from: the large-degree part of PD-T099; its full
all-degree statement remains OPEN. No new mechanism or priority claim.

## Statement and status

For every integer n>=1000000, the corrected Padua Lebesgue function of
PD-T101 satisfies

    max_[-1,1]^2 lambda_n=Lambda_c(n),
    Lambda_c(n)=lambda_n(-1,-1),

with equality set exactly

    {(-1,-1),(1,-1)} for even n,
    {(-1,-1),(-1,1)} for odd n.

Status: **PROVED analytic assembly; independent review pending**. The
complete argument uses the written C08 far theorem and separately
accepted near/corner theorems below. Its independent review and the
formal Claude audit are separate obligations. The finite exact range
2–40 is unchanged. The remaining gap41<=n<=999999 and all-degree
PD-T099 stay OPEN. No computation or degree-extension campaign is used.

## Definitions and exact premises

Let m=n+1 and N=nm. Use PD-T101's corrected kernel

    G_n(u,v)=sum_(i+j<=n) h_i h_j cos(iu)cos(jv)-cos(nu),
    h_0=1, h_i=2 for i>0.

The exceptional coefficient is at the x mode(n,0), without a mesh swap.
All values at collisions mean the finite polynomial value. For a
physical odd center0<=J<=n,0<=K<=m,J+K odd, write

    theta=(J*pi+alpha)/n, phi=(K*pi+beta)/m in[0,pi],
    rho=|alpha|+|beta|<=pi,
    S_n=(1/(2N))sum_(0<=r<2n,0<=s<2m,r+s odd)
                   |G_n((r*pi+alpha)/n,(s*pi+beta)/m)|.

PD-T364 proves the exact identity lambda_n=S_n-Delta_JK with full
four-copy defect Delta>=0, Delta>=max(Q_v,Q_h). The projected defects
are lower bounds, not equalities in that identity.

The numerical premises have precisely these scopes:

1. [C08 far comparison](C08-far-model-comparison.md), frozen SHA256
   0b69e38a8d27f36228c41374b51766bd7955d0bc11d9ba6239b0171d422ba8f3:
   every integer n>=10^6 and every signed far phase1/2<=rho<=pi obey
   S_n<Lambda_c-6/25. This is the actual finite primitive; its compact
   model and error are not substituted separately in this assembly.
2. [C05 actual near noncorner comparison](C05-finiteh-model-comparison.md),
   frozen a0a29f76ad72abab9c44684c8793e9a7c500d12abfefce51dab9fcfed7ba5e4e,
   independently accepted in ../independent-checks-C05-finiteh.md:
   every integer n>=10^6, every physical odd noncorner center, and
   every signed physical rho<=1/2 obey lambda_n<Lambda_c-869/28000.
   This uses the unchanged fixed near model and C02's all-class floor.
3. [C07 actual corner comparison](C07-corner-million-onset.md), frozen
   9fa0d3f3b507f1a772adda1bbc4841e42b13b7f0adada39b6ede2ab8ee5247e4,
   independently accepted in ../independent-checks-C07-corner.md:
   at both nonnode corners and all integer n>=10^6, inward phases
   A,B>=0,A+B<=1/2 give lambda_n<=Lambda_c-(A²+B²).
4. PD-T364 and the already reviewed [C06 assembly](C06-effective-argmax.md)
   supply the exact endpoint-weighted identity, closed physical cover,
   phase evenness and parity-valid corner reflections. The structural
   argument is restated below, without its superseded degree threshold.

There is no energy premise, assumed global maximum, per-cardinal sign
stability, ineffective localization or numerical fit. The original tight
near-model C1 tolerance1/4096 is not a hypothesis of this theorem.

## Proof

Fix n>=1000000 and any physical point(cos theta,cos phi). In a mesh
rectangle containing(theta,phi), let normalized coordinates beX,Y in[0,1].
The two odd opposite vertices have L1 distances X+Y,2-X-Y, or
1-X+Y,1+X-Y. Their sum is two, so one distance is at most one.
Choose such an odd vertex. An adjacent interior rectangle handles the
physical boundary. This constructs the displayed physical odd-center
chart with rho<=pi, including mesh ties, nodes, edges and corners.

Endpoint reflection counts every periodic residue once: the two
coincident copies of an endpoint each carry weight1/2. Applied in both
coordinates to the corrected cardinal identity, this gives exactly
lambda_n=S_n-Delta_JK, with nonnegative Delta. It preserves the exceptional
x coefficient. Reindexing a periodic integer coordinate proves separate
evenness of S in alpha,beta; the actual signed center defect is retained.
These are finite polynomial identities and include all collisions.

If rho>=1/2, premise1 and Delta>=0 give

    lambda_n<=S_n<Lambda_c-6/25<Lambda_c.

If rho<=1/2 and the chosen odd center has an interior coordinate,
premise2 gives the stated strict noncorner gap. Its degree hypothesis
is met exactly at n=1000000 and at every larger integer; no limiting
near estimate is used.

Otherwise both center coordinates are endpoints. The odd endpoint pairs
are exactly(n,m) and(0,m) for even n, or(n,m) and(n,0) for odd n.
These are precisely the two nonnode corners in the statement. Physical
admissibility fixes inward phase signs there. Thus A=|alpha|,B=|beta|
are their inward scaled angle distances. Premise3 gives

    lambda_n<=Lambda_c-(A²+B²),

strict unless A=B=0. It handles arbitrarily small nonzero phases and
introduces no positive absolute approximation error at the origin.
At A=B=0 the physical point is the actual corner. The value at(-1,-1)
is Lambda_c by definition. For even n, reflection in x preserves the
even checkerboard nodes and weights; for odd n, reflection in y does
so because m is even. Interpolation uniqueness makes the corresponding
reflection permute cardinal polynomials, hence the other corner has
the same Lambda_c value. No interchange of meshes is involved.

The shared rho=1/2 boundary belongs to both proved cases. Every node
has rho=pi in this cover: its even mesh parity differs from the odd
center, so its index L1 distance is a positive odd integer at most one.
It is therefore strictly excluded by the far case, including node
corners. Closed-square boundaries and tied charts leave no omitted point.
Consequently equality holds at exactly the two stated nonnode corners,
and every other physical point has smaller Lebesgue function. QED.

## Checks and limitations

This is routine analytic integration of exact pointwise comparisons;
there is no new candidate or historical novelty verdict. No executable,
phase sample, certificate generation or degree scan was run. The author
is the coordinator and does not independently approve this assembly.
Distinct review must check the new far theorem and all degree/scope
interfaces. Formal Claude audit remains PENDING. The proof supplies an
upper boundary1000000, not the minimal onset, and does not certify any
of the remaining degrees41–999999. Cheap numerical implementations,
whole-box source validity and runtime claims remain separate.

2026-11-06. Codex coordinator; requested Astra high, serving metadata
unexposed. Input published head4ca11b8, frozen component hashes above.
