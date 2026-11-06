# PD-T?mz-sharp-codex-S3-03 — compact corner characterization of the sharp slopes

ID kind: PD-T.
Aliases: signed Bessel corner spectrum; full logarithmic spectral transfer.
Split from: PD-T381's original sharp-limit question.
Split into: none. S3-02 and S3-kernel are separate supporting results.

## Statement

Put D={(a,b):a,b>=0,a+b<=1}, H=L2(D,ab da db), and

    J0(z)=sum_(r>=0) (-1)^r(z^2/4)^r/(r!)^2,
    psi_jk(a,b)=J0(pi j a)J0(pi k b),
    e_0=1/2, e_j=1 for j>=1.

For integer K>=1 define the finite-rank selfadjoint operator on H

    B_K=-16 sum_((1+j)(1+k)<=K, j+k even)
               e_j e_k (-1)^j |psi_jk><psi_jk|,           (1)

where |psi><psi|f=psi integral_D f psi ab da db. Then B_K converges
in operator norm to a compact selfadjoint B, with

    ||B-B_K||<=120/K.                                   (2)

Define c_minus=inf spectrum(B), c_plus=sup spectrum(B). For the exact
signed Lebesgue Padua rule of mass four, on total degree Pi_(m-1),

    lambda_minus(m,m-1)/log m -> c_minus<0,
    lambda_plus(m,m-1)/log m -> c_plus>0.                 (3)

Both limits hold over all integers, hence separately on even and odd m
with exactly the same constants. The constants in (1)-(3) specify a
fixed operator independent of the original finite Padua problems.
No decimal enclosure or closed elementary evaluation is asserted.

An explicit finite approximation bound is available. Write

    I_K={(r,s)>=0:(1+r)(1+s)<=K},  N_K=2|I_K|,
    U=pi(K-1),  C_U=3+5U+U^2/4,
    E_K(m)=N_K(32+24pi K)/(8m)+24N_K sqrt(C_U/m).

For every integer m>=max(4,2K) and either sign,

    |lambda_sign(m,m-1)/log m-c_sign|
       <=4300/log m+240/K+E_K(m).                       (4)

These coarse errors prove convergence but do not certify the practical
scan window or the displayed heuristic decimal predictions.

## Definitions and assumptions

All polynomial and operator norms use real coefficients and exact
arithmetic; spectra of real selfadjoint operators may equivalently be
taken after complexification. Continuous measure is unnormalized dxdy.
The Padua nodes are (cos(j pi/m),cos(k pi/(m+1))), j+k even, with the
signed interpolatory weights and endpoint factors of S3-02. Infinity
in (1) is defined by the specified product truncations and (2), rather
than an unproved rearrangement of a conditionally convergent series.

## Status by part

Overall status: **PROVED** (analytic development; independent check of
this complete integration pending).

| Mathematical part | Status | Evidence |
|---|---|---|
| compact B and explicit tail (2) | PROVED | full-grid CC tail and finite-corner kernel transfer |
| complete normalized spectral limits and parity agreement (3) | PROVED | uniform truncation and exact signed corner blocks |
| finite comparison (4) | PROVED | explicit coefficients, kernel errors and matrix square-root estimate |

Candidate disposition: retained implementation of the supplied corner
route, prospectively registered before model computations or final fits.
Coordinator controls PD-T381's registry disposition after review.

## Depends on

S3-full-form-log-model.md (S3-02), including its all-vector signed error,
CC floors and tensor upper bound; S3-corner-kernel-hard.md (S3-kernel),
whose complete proof was read at SHA256
0200a23f0262418fe12cf1458bfbbc11bcb85018dce488a913fc58eae3bd326a.
The kernel dependency is separate mathematical development, not an audit.
PD-T379 and S3-01 supply strict signs only, after convergence is proved.
No measured optimizer, numerical slope or external theorem is a premise.

## Proof

### 1. Uniform finite-corner tail in the continuous metric

Use R=floor(m/2), M=m+1 and the exact finite form of S3-02:

    L_m[p]=-2/(m M R^2) sum_(j+k even) epsilon_j eta_k
        [cos(2R theta_j)+cos(2R phi_k)] p(node)^2.

Let d_j=min(j,m-j), e_k=min(k,M-k), D_jk=(1+d_j)(1+e_k).
Let L_m^K retain only its terms with D_jk<=K. S3-02's CC weights
alpha_j,beta_k obey alpha_j beta_k>=D_jk/(m^2 M^2).
For every subset of nodes with D_jk>K, the absolute sum of its
quadratic terms is at most

    4/(m M R^2) sum_(subset) epsilon_j eta_k p(node)^2
      <=(4mM/(K R^2)) sum_(all j,k) alpha_j beta_k p(node)^2
      <=120/K ||p||^2.                                  (5)

The last inequality uses mM/R^2<=15/2 and the tensor CC bound<=4.
It follows, on the full continuous polynomial unit sphere, that

    ||L_m-L_m^K||<=120/K.                               (6)

Importantly, (5) also holds for any one-corner subset, and for the
terms between any two truncations. It uses the magnitude of the
entire retained tail; no cancellation estimate or weight-sign
classification is needed. Nodes near all four endpoints are included.

### 2. Exact local indices, coefficients, and the active corners

For m>=max(4,2K), the nodes with D_jk<=K are disjoint unions of four
corner patches, indexed by (r,s) in I_K. A corner with endpoint
signs ((-1)^delta_x,(-1)^delta_y) has indices

    j=r if delta_x=0, or j=m-r if delta_x=1;
    k=s if delta_y=0, or k=M-s if delta_y=1.

Retainment is precisely

    r+s+m delta_x+M delta_y even.                       (7)

Since 2R is even, reflection does not alter either cosine in L_m.
Put a_r=(-1)^r, a_s=(-1)^s. At every such node, its L_m weight
times m^4 is

    gamma_m=-q_m e_r e_s
                 [cos(2R pi r/m)+cos(2R pi s/M)],
    q_m=2m^3/(M R^2) ->8.                              (8)

If the base corner indices have even sum, (7) requires r+s even,
and (8) tends to -16 e_r e_s (-1)^r. If the base sum is odd,
(7) requires r+s odd and the two limiting cosines cancel, so
gamma_m tends to zero. Exactly two corners are active:

| m parity | active corners | remaining leading blocks |
|---|---|---|
| even | (1,1),(-1,1) | zero at (1,-1),(-1,-1) |
| odd | (1,1),(1,-1) | zero at (-1,1),(-1,-1) |

Thus there are N_K=2|I_K| retained nodes in the four patches; two
patches use the even subset of I_K, and two the odd subset. Label
the active patches first, independently on each m parity.

For later quantitative use, for every m>=4 one has

    |q_m-8|<=16/m.                                     (9)

For even m, q_m=8m/(m+1). For odd m,
q_m-8=8(m^2+m-1)/[(m+1)(m-1)^2]<=16/m; the last inequality
reduces to m^3-3m^2-m+2>=0 for m>=5. Furthermore the x phase
differs from pi r by at most pi r/m, and the y phase by at most
2pi s/m. Hence the diagonal coefficient matrix C_m of (8) differs
from its limiting diagonal matrix C_infinity by at most

    ||C_m-C_infinity||<=(32+24pi K)/m=:beta_K(m),
    ||C_infinity||<=16.                                (10)

This estimate includes the leading-zero patches and every endpoint
halfweight. No coordinate interchange of the actual rule is made.

### 3. Finite Gram kernels and signed finite-rank spectra

Let H_m=Pi_(m-1) with its continuous inner product. For each retained
patch node z, let v_(m,z)=m^(-2)K_(m-1)(.,z) in H_m, the scaled
evaluation representer. Then

    L_m^K=sum_z gamma_(m,z) |v_(m,z)><v_(m,z)|,
    G_m(z,z')=<v_(m,z),v_(m,z')>=m^(-4)K_(m-1)(z,z').

S3-kernel applies with angular coordinates pi r, pi s, shifts0,1,
and the relevant endpoint signs. It gives entrywise

    |G_m-G_infinity|<=C_U/m,    U=pi(K-1),
    ||G_m-G_infinity||<=N_K C_U/m.                     (11)

G_infinity is block diagonal over the four corners, and the block
at any one corner is the H-Gram matrix of its functions psi_rs.
This proves that every fixed finite signed corner form has exactly
the proposed Bessel realization. Active corner blocks have B_K's
coefficients; inactive blocks have zero coefficients.

For clarity, finite-rank signed spectral transfer uses no positivity
assumption on the coefficients. If V sends a finite coefficient
vector to the corresponding representer combination, then V*V=G.
The nonzero eigenvalues of V C V* are those of G^(1/2) C G^(1/2),
by the polar decomposition of this finite matrix map (or its singular
value decomposition). Additional eigenvalues are zero. Indeed
|I_K|<=K^2, so N_K<=2K^2<m(m+1)/2=dim H_m whenever m>=2K.
Thus zero belongs to the finite-rank form's spectrum throughout the
claimed range m>=max(4,2K). The limiting model H is infinite dimensional, so
its finite-rank forms also contain zero in their spectra.

By (10)-(11) and continuity of the positive matrix square root,
the minimum and maximum of L_m^K converge to those of B_K, each
duplicated active block having the same extreme eigenvalues. The
inactive blocks contribute only zero. Write these extremes c_sign(K),
including zero; this convention agrees with the spectrum of B_K on H.

### 4. Construction of the compact operator and full limiting spectrum

Fix integers K'>K and isolate one active corner. Its terms between
the two product truncations satisfy (5), hence their operator norm
is at most120/K for every sufficiently large m. The finite-Gram
transfer just proved identifies the limiting norm with
||B_(K')-B_K||. Therefore

    ||B_(K')-B_K||<=120/K.                             (12)

The B_K are Cauchy in bounded-operator norm and have a selfadjoint
limit B. Taking K' to infinity gives (2). This limit is compact:
given any bounded sequence, approximate B by a finite-rank B_K,
take a convergent subsequence for that finite-dimensional image,
and repeat along K tending to infinity; the uniform tail gives a
Cauchy diagonal subsequence for the B-images. Thus no unproved
infinite-series exchange enters (1)-(2).

The variational minimum and maximum of selfadjoint forms change
by at most their operator-norm difference. Consequently

    |c_sign(K)-c_sign|<=120/K.

For fixed K, (6) and finite-Gram transfer imply

    limsup_(m->infinity)|nu_sign(m)-c_sign|<=240/K,

where nu_sign are L_m's extreme quotients. Let K tend to infinity.
This proves nu_sign(m)->c_sign over all integers, including both
parities with identical c_sign. S3-02 gives
|lambda_sign/log m-nu_sign(m)|<=4300/log m, proving (3).

Finally S3-01's inherited normalized negative carrier bound gives
c_minus<=-c_new<0. PD-T379's positive bound gives
c_plus>=c_plus(PD-T379)>0. These trial bounds only establish signs;
the matching full-spectrum transfer above establishes the exact
operator characterization. The numerical model never enters this proof.

### 5. Explicit finite comparison

The bound |P_l(x)|<=1 follows from S3-kernel's integral proof.
Therefore every entry of G_m is bounded by its corner diagonal,

    m^(-4)K_(m-1)(corner,corner)
      =m(m+1)(m^2+m+1)/(24m^4)<1/8  (m>=4).

The same bound holds for G_infinity, whose within-corner diagonal
is at most integral_D ab=1/24. Thus both Gram operator norms are
at most N_K/8.

For positive matrices A,B, writing delta=||A-B|| gives the elementary
bound ||A^(1/2)-B^(1/2)||<=2 sqrt(delta). Indeed use

    A^(1/2)=(1/pi)integral_0^infinity
                   t^(-1/2) A(A+tI)^(-1) dt.

This is the scalar integral applied after diagonalization. In the
difference integrand, the norm is at most t^(-1/2), because both
resolvent factors A(A+tI)^(-1),B(B+tI)^(-1) lie between0 and I;
the resolvent identity also bounds it by delta t^(-3/2). Splitting
the integral at t=delta gives (4/pi)sqrt(delta)<=2sqrt(delta).
The delta=0 case is immediate, and no invertibility is required.

Apply this with (11), then telescope
G_m^(1/2) C_m G_m^(1/2) against its limiting matrix. Its operator
norm difference is at most

    (N_K/8) beta_K(m)
      +16[2sqrt(N_K/8)] [2sqrt(N_K C_U/m)]
       <=N_K beta_K(m)/8+24N_K sqrt(C_U/m)=E_K(m).

Hence |nu_sign^K(m)-c_sign(K)|<=E_K(m). Combining this with
(6), (2), and the S3-02 normalized error proves (4). For each fixed
K, E_K(m) tends to zero with an explicit rate; K may subsequently
increase. Finite coefficient/truncation errors have all been retained.

## Checks, preregistration and numerical limits

Exact operator and parity prediction were saved before numerical model
construction, original SHA256
c2e8b10ac01c04c514b16b1c239682d16342aef7a55590c99afc22e5611c5263,
and published by the coordinator at59d02c7e7dca3faa4a4687db331a784366595a26
before final S4 fits. See ../ideas/S3-corner-operator.md for chronology.

../code/S3_corner_model.py actually computed B_K Gram spectra with
triangle Gauss orders128,192 and K=16,32,64,128. Small receipt:
../evidence/S3-corner-model.json. It suggests c_minus near-0.1336 and
c_plus near0.0456. Floating quadrature is not enclosed and120/128 is
far too large to justify decimal accuracy. These values are MEASURED
orientation only; the theorem's constants are precisely (1)-(3).

The complete integration above needs independent mathematical check;
the earlier supplementary approval covers S3-02 only. Required Claude
audit remains separate. No final S4 fit was read by this developer.

## Sources, scope and open items

Full prospective predecessor gate ../novelty-gate-S3.md. No external
fulltext or external asymptotic/spectral theorem is used. Existing
reproducing-kernel algebra and the supplied limiting-corner route are
acknowledged; no historical novelty or priority claim is made.

The result determines exact constants by a fixed compact operator with
finite-rank error control. It does not give certified decimal intervals,
closed elementary constants, useful finite-degree onset, or a proof that
the inherited carrier family attains either extremum. Coordinator review
will decide whether this exact operator characterization resolves the
original PD-T381 value requirement; no shared registry is edited here.

## History

2026-11-06; Codex S3 mathematical developer, allocated gpt-6.1-sol xhigh;
runtime metadata unexposed. Rules/input2143ad622fa98faf8fe7d5cb8ed2bb7e0062f861.
Round3. Kernel-hard supporting developer separately owns S3-kernel;
development and independent audit are distinct. No Git/shared edits.


## 2026-11-06 audit-01 A2 interpretation

Equations (3) and (4) of S3-03 predict limits, and make no prediction about
finite-window slopes. K4 compared those limits with finite-window slopes;
its KILL_HEURISTIC_PROXY outcome remains unchanged and is not a PD-N.
The audit diagnostic audit-01-support/S3/big.json (MEASURED floating point,
m=400,800,801 with mid.json) places roughly 94–96% of the Q-minimiser on
L_m's second mode, while the bottom L_m mode is already near −0.1336.
Mode-dependent O(1) corrections explain the observed slopes near −0.092
without contradicting the limit theorem. This is finite-scope audit evidence,
not a proved branch law or certified crossover prediction.


Audit A7 clarification to §3: the corner Gram block does not depend on
corner signs. Thus the two active corner blocks are identical.


## 2026-11-06 audit completion pointer

The earlier requests for independent/Claude review describe the development
boundary. Claude audit-01.md now accepts this analytic proof at its stated
scope. That completed audit supersedes earlier pending-review metadata; it
does not certify floating decimal values or approve this response.
