# PD-T?mz-cleanup-codex-03 — odd-m carriers and all-parity spectral divergence

ID kind: PD-T.
Aliases: even-y-mesh carrier; all-integer half-exactness classification.
Split from: the explicitly missing odd-m parameter cases of PD-N105/106/107.
Split into: exact norm limits and quantitative one-sided coefficients
are separate PD-T?mz-cleanup-codex-04.

## Statement

Use the frozen signed Padua form Q_m and continuous L²(dxdy) norm.
Let m tend to infinity through odd integers, M=m+1, r=floor(am),
s=floor(bm), and F_u the degree-u Fejer polynomial

    F_u(cos t)=1+2 sum_(l=1)^u [1-l/(u+1)]cos(lt).

For a,b>0 with a+b<1/2, the polynomials

    p^-_m(x,y)=T_(M/2)(y) F_r(y) F_s(x)               (1)

have degree M/2+r+s<=m-1 eventually and satisfy

    Q_m((p^-_m)²)/log m -> -16ab/9.                  (2)

For a,b>0 with 2a+b<1/2,

    p^+_m(x,y)=[T_(M/2-r)(y)-T_(M/2+r)(y)]
                         F_r(y)F_s(x)/2             (3)

have degree M/2+2r+s<=m-1 eventually and satisfy

    Q_m((p^+_m)²)/log m -> 8ab/9.                    (4)

All displayed polynomials are nonzero eventually and
0<||p^±_m||²<=C0², C0=(1+pi^4)/2.
Consequently, over **all integers** m tending to infinity,

    lambda_-(m,m-1)->-infinity,
    lambda_+(m,m-1)->+infinity.                      (5)

More generally, for each fixed theta with 1/2<theta<1, (5) holds
with m-1 replaced by floor(theta m). For 0<=theta<=1/2, the latter
Gram matrix is exactly I for every m for which the space is defined.
No effective onset or sharp extremal coefficient is asserted.

## Definitions and assumptions

Frozen even checkerboard, actual meshes m and m+1, unnormalized dxdy.
The continuous Legendre basis in the definitions makes its Gram extreme
eigenvalues the variational extrema of Q_m(p²)/||p||².
All limits hold at fixed a,b in the displayed open triangles. No
rotation symmetry or equality of full y and x marginals is assumed.

## Status by part

Overall status: **PROVED** (analytic development; supplementary and
required Claude audits pending).

| Part | Status | Evidence |
|---|---|---|
| Odd-m negative and positive packets | PROVED | Whole signed sums below |
| All-parity divergence and sharp half-degree transition | PROVED | Combination with even-m PD-N105–107 |

Candidate disposition: retained parity extension. PD-N105/106 already
refute the universal positive assertions, so this adds no duplicate PD-N.

## Depends on

PD-T?mz-cleanup-codex-02 for odd weights and domination; PD-N105/106
for Fejer bounds and elementary finite DCT identities, and their accepted
even-m carrier statements. The all-m threshold combines PD-N107's
existing even-m conclusions with the newly proved odd-m conclusions.

## Checks

Analytic, no computer-assisted premise. Rules/input
ad503cb0603fc017444b0aa732240981eefa4d24. Independent reconstruction
and required Claude audit are pending. This author claims no executed
spectral scan; the parent's scans remain separately MEASURED.

## Sources

../novelty-gate-math.md. No external theorem or priority claim used.

## Proof

### Polynomial and degree constraints

M is even, so every Chebyshev degree in (1),(3) is an integer.
For (3), a<1/4 and hence 1<=r<M/2 eventually. At y=cos t its
first factor is exactly sin(Mt/2)sin(rt), a product which is a
polynomial in cos t by the displayed cosine-difference identity.
Its highest degree is M/2+r. Nonzero leading coefficients of all
factors prove the exact total degrees in the statement. The extra
1/2 in M/2=m/2+1/2 is absorbed by the strict parameter inequalities;
eventually both degrees are <=m-1. The continuous Fejer bound

    |F_u(cos t)|<=min(u+1,pi²/[(u+1)t²])

and sin t<=t give ||F_u||²<=C0, by splitting at t=1/(u+1),
as proved explicitly in PD-N105. Both carrier factors have magnitude
<=1, so product integration gives the claimed uniform squared norms.
Nonzero polynomials have strictly positive norm.

### Exact finite parity energies

For a mesh denominator L with endpoint halfweights c_i,

    sum_(i=0)^L c_i cos(l i pi/L)=0 (1<=l<=2L-1),
    sum c_i=L.                                     (6)

For a polynomial h of degree <L this gives zero alternating sum
sum c_i(-1)^i h(cos(i pi/L)); its ordinary sum is L times its
constant Chebyshev coefficient. For F_u² the latter is

    D_u=1+u(2u+1)/[3(u+1)],   D_u/u->2/3.            (7)

Use mesh M for the carrier in y and mesh m for its unmodulated x
factor, with normalization m in both arrays. Since 2r<M and 2s<m,

    V^-_(m,k)=cos²(k pi/2)[F_r(cos(k pi/M))/m]²,
    U_(m,j)=[F_s(cos(j pi/m))/m]²,
    sum_k eta_k V^-_(m,k)=M D_r/(2m²)->a/3,
    V^-_(m,k)=0 for odd k,
    sum_j epsilon_j U_(m,j)=D_s/m->2b/3,
    sum_j epsilon_j(-1)^j U_(m,j)=0.                (8)

For (3), put h_r(cos t)=sin²(rt)F_r(cos t)².
Its degree is 4r<M eventually. Its constant coefficient is

    d_r=D_r/2-1/[2(r+1)²],                          (9)

because the T_(2r) coefficient of F_r² is 2/(r+1)². Equation (6)
applied to h_r gives

    V^+_(m,k)=sin²(k pi/2)sin²(r k pi/M)
                             [F_r(cos(k pi/M))/m]²,
    sum_k eta_k V^+_(m,k)=M d_r/(2m²)->a/6,
    V^+_(m,k)=0 for even k.                         (10)

These are actual y-mesh identities, not a silent interchange of the
exceptional mode in the Padua cardinal formula.

### Full signed energies

For every fixed index the normalized Fejer profiles converge to

    f_a(i)=a (i=0),
    f_a(i)=sin²(a pi i/2)/[a (pi i/2)²] (i>0).

Using M/m->1 gives this same formula for the y mesh. The uniform
bounds |F_r(cos(k pi/M))|/m<=C_a(1+k)^(-2) and
|F_s(cos(j pi/m))|/m<=C_b(1+j)^(-2) hold on their entire grids:
use the endpoint bound at zero, and sin(k pi/(2M))>=k/M elsewhere.
Extend finite arrays by zero. Thus all ordinary and alternating
profile sums in (8),(10) converge under summable domination; moving
far halfweights cause no difficulty. The limiting x energy on each
parity is b/3. The limiting y energy is a/3 on even k for p^-,
and a/6 on odd k for p^+.

For either sign the exact sampled form is

    Q_m((p^±_m)²)/log m
      =sum_(j+k even) [m^4w_(j,k)/log m] U_(m,j)V^±_(m,k).

The odd-weight majorant bounds every absolute summand by a constant
times [(1+j)(1+k)+1]/[(1+j)^4(1+k)^4], which is summable.
Dominated convergence therefore applies to the **complete signed form**.
By the fixed-node limit, only even-even indices contribute to p^-,
with leading coefficient -16e_j e_k. Only odd-odd contribute to p^+,
with leading coefficient +16e_j e_k. Equations (8),(10) give
-16(b/3)(a/3) and 16(b/3)(a/6), proving (2),(4).

### Variational consequences and all-m classification

The uniform positive norm bound implies a negative Rayleigh quotient
at most -c_-log m eventually for every 0<c_-<16ab/(9C0²);
likewise a positive quotient at least c_+log m for
0<c_+<8ab/(9C0²). The variational principle proves divergence on
odd m. PD-N105/106 prove the same on even m. The two subsequence
statements imply (5) on all integers (take the larger of their eventual
thresholds for any prescribed finite bound).

For fixed theta>1/2, choose a,b>0 with 1/2+a+b<theta in (1),
and 1/2+2a+b<theta in (3). The resulting degrees are <=floor(theta m)
eventually, including their odd-m +1/2 overhead. The same variational
argument, combined with the even case, proves both divergences there.
For theta<=1/2, 2floor(theta m)<=m, so quadrature exactness through
Pi_m makes every Gram entry equal its continuous orthonormal integral.
Hence G=I exactly. ∎

## Scope

This completes the qualitative parity classification of both actual
signed extrema, including fixed ratios strictly above half-exactness.
The continuous-data C-to-L² norm is a different operator and its
uniform bound PD-T297 is compatible with this divergence.

## Open items

Finite onset, spectral growth limits and first crossings remain separate;
this proof does not identify the parent's finite minimizing branch.
Required supplementary/Claude checks pending.

## History

2026-11-05, Codex, inherited gpt-6.1-sol xhigh; input/rules ad503cb.
New odd-parity argument and all-m synthesis; accepted even files unchanged.
