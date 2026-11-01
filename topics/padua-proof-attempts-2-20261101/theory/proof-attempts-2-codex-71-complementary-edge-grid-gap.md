# PD-T?proof-attempts-2-codex-71 — Positive corner gap on complementary edge-grid points

ID kind: PD-T.
Aliases: A4(a) complementary ordinate; exact triangle defect; singular endpoint correction.
Split from: the point-value part of A4(a), after the all-edge identity70.
Split into: the central-grid limiting gap is72; the central envelope and searched runner-up are separate.

## Statement

Use the Padua conventions of70. Put m=n+1,N=nm. Choose epsilon in{−1,1} and an integer1<=q<=m−1 with

`r+q odd`, where `r=n*1_(epsilon=−1)`, and set beta=q*pi/m.

Thus z=(epsilon,cos beta) is a vertical-edge Lobatto-grid point of the parity complementary to the edge nodes. For every original node index j+k even put A_j=epsilon*cos(j*pi/n), b_k=k*pi/m, z_+=cos(beta+b_k), z_−=cos(beta−b_k), and

\[
 h_\beta(A,b)=\begin{cases}
 \min\left\{\dfrac{1+z_+}{A-z_+},\dfrac{1+z_-}{z_--A}\right\},
             &z_+<A<z_-,\\
 0,&\text{otherwise}.
 \end{cases}                                                \tag{1}
\]

At b=0,pi the open band is empty. Then for every n>=1 and every such choice,

\[
 \boxed{\ \Lambda_c(n)-\lambda_n(\epsilon,\cos\beta)
 =\frac4{n(n+1)}\sum_{j+k\,\mathrm{even}}
       \epsilon_j\eta_k h_\beta(A_j,b_k)
   +\frac2{n(n+1)}>0.\ }                                   \tag{2}
\]

All terms of the sum are nonnegative finite real numbers. The final2/N is an exact removable-endpoint correction and must not be replaced by a limit of the mesh-simplified rational expression.

## Definitions and assumptions

The epsilon_j,eta_k are endpoint half weights, not the chosen sign epsilon. Lambda_c is the corner value already treated in A2. The points in this statement are fixed complementary grid points. They need not be critical points or the source's searched runner-up. All arithmetic and identities are exact.

## Status by part

Overall status: **PROVED** (written analytic identity; required Claude audit PENDING).

| Part | Status |
|---|---|
| Exact defect identity and strict positivity at every specified point | PROVED |
| Unique singular endpoint and the correction2/N | PROVED separately below |

## Depends on

70 and A2 supporting04, in particular its positive corner sum. The underlying literal dependency is **PD-T?proof-attempts-codex-01 (audit pending)**; dated2026-11-01 qualification: Part1 audit accepted A1, minor dispositions completed and merged; final alias PD-T101. No asymptotic or maximizer hypothesis.

## Checks

Supplementary independent analytic reconstruction by `/root/a2_independent_route` confirmed the general translated-grid normalization, the sole singular correction and the positivity identity. Its receipt is independent-checks-a4.md. Subsequently the separately implemented code/a4reg_complementary_check.py, frozen SHA256978bf8e00e09f4671d36d9de0e3c8dae531d34491ed7cdec1741aa6542032fca, was actually executed and independently replayed, both exit0 with both source/import hashes unchanged. Exact cyclotomic Vandermonde arithmetic checks all21 admissible points for n1..6:357 regular cardinal identities,21 unique endpoint corrections, the weighted raw-E multiset translation and the rational+2/N normalization. It does not compute absolute-value gap sums or the limiting integral. Developer elapsed1.543606s, separate replay1.681193s; their3074byte receipts are outputs/a4reg_complementary_developer.json (SHA2561c6c3ef524ce9d21a4eec1fe19d2120b7f572ce1e8c78847fbdafb96f0553f93) and outputs/a4reg_complementary_independent.json (SHA256fbdff9c29bee11828ac173fbd7f93d5606ff05d5b159e1813e91d8c1018c1520). All fields agree after removing only elapsed_seconds. Full commands and limitations are in independent-execution-a4-regression.md. The analytic proof does not depend on this finite regression; required Claude audit remains PENDING.

## Sources

Registered IDEA206/source05/A4(a); the full refreshed gate is in attempts/T-A4a.md. The finite-cosine translation and triangle-defect reformulation continue the accepted kernel normalization. No priority claim.

## Proof

For n=1 the only admissible choice is epsilon=1,q=1. The three cardinal polynomials are(1+x+2y)/4,(1+x−2y)/4,(1−x)/2. Direct substitution gives Lambda_c=2 and lambda_1(1,0)=1; every h term in(2) is0 and2/N=1. Thus(2) holds directly in this case. In the rest of the proof n>=2, the stated range of A2 supporting04 applies.

Reflect the first-coordinate mesh about the chosen endpoint: j'=j if epsilon=1 and j'=n−j if epsilon=−1. Then A_j=cos(j'*pi/n), the endpoint weights are unchanged, and tau_j=(−1)^j'=epsilon^n(−1)^j. Both shifted second angles beta±b_k are multiples of pi/m, and j'+(q±k) is odd. The same product-to-sum simplification used in A2 supporting04 consequently gives

\[
 D_n(j'\pi/n,v)-\tau_j
     =2\tau_j\frac{1+\cos v}{A_j-\cos v},                    \tag{3}
\]

away from coincident cosines. The all-edge average70 therefore gives the corrected kernel tau_j(E_++E_−), where E_±=(1+z_±)/(A_j−z_±).

There are no interior coincidences: equality cos(j'*pi/n)=cos(l*pi/m) forces j'/n=l/m after reflection into[0,pi], and coprimality of n,m leaves only endpoints. The complementary parity excludes A=z=1. For formal summation define E(−1,−1)=0 and retain the ordinary quotient elsewhere. Then

\[
 \sum_{j+k\,\mathrm{even}}w_{jk}(|E_+|+|E_-|)
       =\Lambda_c(n)-\frac1m.                              \tag{4}
\]

Here is the exact weight/translation accounting in(4). For each fixed j, reflecting the half-mesh k=0,…,m with endpoint half weights combines the plus and minus terms into the complete periodic second mesh k=0,…,2m−1 of the original k parity. Translation k->k+q preserves its counting measure and changes that parity byq. Reflection j->j' changes its parity byr. Since r+q is odd, the resulting mesh is precisely the odd checkerboard. Reflecting the periodic second mesh back to[0,pi] multiplies its endpoint-weighted sum by2. With w_jk=2epsilon_j eta_k/N the result is

`(4/N) sum_(j'+l odd) epsilon_(j') eta_l |(1+cos b_l)/(cos a_(j')−cos b_l)|`,

with its sole coincident endpoint set to0. A2 supporting04's exact positive corner formula says that this sum equals Lambda_c−1/m. This proves(4) without changing endpoint weights.

The unique exceptional original index is j'=n,k=m−q, so A=z_+=−1 and w_jk=1/N; the other shifted cosine is cos(2beta−pi)!=−1. At the singular angle the finite kernel has

`D_n(pi,pi)=(−1)^n(2n+1)`.

Its corrected half contribution is n*tau_j. The other regular half contribution is −tau_j, since E_−=−1. Thus the true corrected kernel has absolute value n−1, whereas the formally assigned E_+=0,E_−=−1 gives absolute value1. At every other index(3) is valid. Therefore

\[
 \lambda_n(\epsilon,\cos\beta)
 =\sum w_{jk}|E_++E_-|+\frac{n-2}{N}.                       \tag{5}
\]

This includes n=1: the correction is then negative and the true exceptional cardinal value is0. No continuity of a mesh-only quotient was assumed.

For real u,v, |u|+|v|−|u+v| is0 for equal signs and2min(|u|,|v|) for opposite signs. Because z_+<=z_− and their numerators1+z_± are nonnegative, the defect equals2h_beta inside z_+<A_j<z_− and is0 outside. If z_+=−1, its numerator vanishes and h_beta is0 throughout the open band; no claim of opposite nonzero signs is made on that degenerate line. Subtract(5) from(4) after restoring1/m=n/N. The result is

`2 sum w_jk h_beta(A_j,b_k)+(n−(n−2))/N`,

which is exactly(2). Every summand is nonnegative and2/N>0, proving the strict inequality. ∎

## Scope

Every specified complementary point on either vertical edge, all n>=1. This is not a maximum-over-an-edge assertion, not a count, and not identification of the programme's runner-up. Arbitrary edge values remain exactly covered by70, but(2) uses the stated mesh-phase hypothesis.

## Open items

Connection to a central maximizing branch/envelope and required Claude audit. The point-sequence asymptotics72 and supplementary finite regression are complete. No result about all-n A4(b)/(c) follows.

## History

2026-11-01, Codex gpt-6.1-sol xhigh. A naive mesh-quotient extension at the nonnode midpoint would give a wrong endpoint value; the independent reconstruction identified this before any computation or claim using it. The original finite D_n limit is retained explicitly here.
