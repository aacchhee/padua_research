# PD-T?argmax-bridge-codex-N1-15 — Fixed-count near-phase integral model

ID kind: PD-T. Aliases: completed corrected near-profile representation;
central/interior outer compactification. Split from: the N1 full-diamond
profile and maximum comparison, which remain OPEN. Split into: none.

## Statement

Assume alpha,beta>=0, rho=alpha+beta<=1/2, integer n>=10^6, m=n+1,
L=log n, h=pi/m, R=128 and delta=1/1000. Define M_near below using
the corrected kernel and the same one-correction terms as N1-09–12.
Then

    |K_endpoint-M_near|<1/14000+1/10^6<1/7000,
    |S_n(alpha,beta)-M_near(alpha,beta,log n)|
                         <3/14000<1/4096.             (1)

Every sum, special row, branch list and integral in M_near has a number
of terms independent of n. Dependence on n is retained through h,
L and a fixed number of scalar integer cutoffs, with n=exp L on the
stated integer-degree domain. Separate absolute phases extend (1) to
|alpha|+|beta|<=1/2. No exchange of the two meshes is used.

This proves the representation and its uniform integral remainder.
It does not bound M_near's maximum, prove an argmax onset or cover
rho>1/2. In particular it is not a full B3 PASS or B4 release.

## Exact finite-count model

Use N1-12's E_R (first/last R rows), A_R (all special rows), H and
finite-h endpoint terms. Use N1-10's M_strip and N1-11's M_jump
unchanged. The remaining special set is B=A_R outside E_R, with at
most four members. It is obtained without scanning rows: start with
{m-1,m}, and test the two possible collision angles

    v^(1)=pi-alpha+beta, v^(2)=pi+alpha+beta,
    r^(i)=(m*v^(i)-beta)/pi.                          (2)

Include a candidate only if r^(i) is an integer row index and the
corresponding actual grid collision occurs; merge duplicates. The
grid test is the exact t_- or t_+ pole condition of N1-02. At a double
collision its distinct grid indices are both retained, as in N2/N1-08.

For s=L,R put t_L=beta/pi, t_R=1-beta/pi and

    K_s=floor(delta/h-t_s),
    a_s=h*(K_s+t_s+1/2), b_s=h*(m-3/2+t_s).

Let C_s be [a_s,b_s] with each actual nonendpoint collision-row cell
[h(k+t_s-1/2),h(k+t_s+1/2)] removed when its center lies in this
interval. On the left k=r; on the right k=2m-r-1. There are at most
two such removed cells in total. The central rows m-1,m are already
excluded by the upper index m-2. Thus the two C_s together are a
union of at most four intervals, with all endpoints specified by a
fixed number of arithmetic/floor tests. Define v_L(z)=z,v_R(z)=2pi-z.

For the finite evaluation of Rhat on B, replace each exact shifted
harmonic sum in N1-01's cotangent blocks by the following function.
For y>0 and integer q>=0, set J=8 and

    H8(q,y)=sum_{i=0}^{q-1} 1/(y+i),                 if q<=J,
    H8(q,y)=sum_{i=0}^{J-1} 1/(y+i)
              +log[(y+q-1/2)/(y+J-1/2)],            if q>J.      (3)

Each sum has at most eight terms. For a block i=b,...,e of offset t,
the two positive reciprocal sums use q=e-b+1 with y=b+t and
y=n-e-t, respectively, reversing the second progression. Keep all
other W,w' terms, signed-row terms and exact polynomial collision
terms of Rhat unchanged. Call the resulting row Rtilde_r. Exact pole
samples remain excluded from the cotangent blocks; no zero times an
infinite factor is substituted for a polynomial collision value.

The model is

    M_near=(1/(nm))*{
           sum_{r in E_R} R_r^finite-h
              +sum_{r in B} Rtilde_r }
           +M_strip+M_jump
           +(1/pi)*sum_{s=L,R} integral_(C_s) H(L,v_s(z))dz.   (4)

The ordinary integrals in (4) are exact model functions. The formulas
in N1-05, N1-10 and N1-14 make their integrands explicit, with a fixed
number of trigonometric/sign branches. No degree-growing row or
column sum is hidden in their definition. Certifying numerical integral
evaluations for a later maximum comparison is a separate obligation.

## Status and dependencies

Overall status: **PROVED**, analytic developer proof; independent review
pending. N1-12 bounds the existing corrected model by 1/14000. N1-13
proves regular coefficient/pole variation, N1-14 the central logarithm.
N1-01/N5 supply the special-row cotangent blocks, and N1-09 supplies
the exact finite-h endpoint rows and endpoint integral branches. All
old frozen formulas remain unchanged. No fit, numerical computation
or external theorem is used.

## Proof

### 1. Exact cell and special-row indexing

N1-02's offsets are eta_-=1/2+(alpha-beta+v)/(2pi) and
eta_+=1/2+(alpha+beta-v)/(2pi). Their only possible integer values
in 0<v<2pi on rho<=1/2 occur at the two angles (2). Hence all extra
collision rows are in [pi-1/2,pi+1/2]. The same is true of m-1,m.

On each folded half the remaining ordinary samples have exactly
k=K_s+1,...,m-2, excluding the collision rows just identified. Their
actual centered cells are C_s. This convention has only one physical
v=pi row when beta=0, and that row is special. In particular every
cell in C_s lies in (0,pi), its lower endpoint is greater than

    ell=delta-h/2>499/500000,                         (5)

and its distance from pi is at least h/2. There is no duplicated
central sample or discarded initial/final ordinary interval.

### 2. Quadrature for the remaining H profile

Decompose the existing profile exactly as

    H(L,v_s(z))=Q_L/z+L*f_s(z)+P_s(z)+I_s(z)/pi,
    Q_L=4a*L/pi+U0,                                  (6)

with the regular pieces from N1-13. For a twice differentiable f on
the actual cell union, the centered-cell kernel gives normalized
error at most h^2/(8pi) times the integral of |f''|. For the first
term of (6), summing the two halves and using |U0|<=8 yields

    e_singular <= (L+2pi)/(m^2*ell^2)<1/40000.         (7)

Indeed each half integrates (1/z)''=2/z^3 to at most ell^-2.
The scalar bound is uniform because (log n+2pi)/(n+1)^2 decreases
for n>=10^6, log(10^6)<14, pi<4 and (5) holds.
N1-13 gives independently

    e_regular<1/50000.                               (8)

Split the I cells by their centers: call a cell an endpoint cell if
z_center<=pi/2+h/2 and a central cell otherwise. Every central cell
lies in [pi/2,pi), while every endpoint cell lies in (ell,pi/2+h),
whose upper endpoint is below 8/5.

On the endpoint cells the exact formula is

    I_s(z)=[2a cot(z/2)+q_s]*log(sin z),
    q_L=q,q_R=-q.                                    (9)

N1-09/N1-10 prove it through pi/2. The same formula remains valid
up to 8/5: the complete numerator is positive, since
2a(1+cos z)-P>=2*(15/16)*(97/100)-1/2>0, and the two coefficients
remain opposite in sign. On the part beyond pi/2, the no-root case
of N1-14(3), with separation pi-z, gives (9). Here cos z>=-3/100
follows from pi>3.14.

For 0<z<=8/5, elementary sine bounds give

    csc^2(z/2)<=6/z^2, csc^2 z<=4/z^2,
    |cot z|<=1/z, |log(sin z)|<=log(2/z).

For the first two inequalities use sin x>=x(1-x^2/6) and
sin z>=z/2. The latter sine bound follows from
1-z^2/6>=43/75>1/2. The cotangent bound above pi/2 follows from
tan(z-pi/2)<31/1000<1/z; below pi/2 it is standard.
Differentiating (9) twice therefore gives

    |I_s''(z)|<=14a*[log(2/z)+2]/z^3+4q/z^2.

Consequently the combined second-derivative integral of the two
endpoint cell unions is at most

    14a*[log(2/ell)+5/2]/ell^2+8q/ell.

The I/pi normalization makes its midpoint error at most this number
divided by 8m^2. Using (5), q<=1/2 and log(2/ell)<8 gives

    e_endpoint-I<1/50000.                            (10)

On the central cells N1-14 gives I_s=d log(pi-z)+Z_s(pi-z), with
combined Var Z_s<15 and d<=1/2. Thus

    e_central-residue<=15/(2pi*m)<1/400000.            (11)

For log(pi-z), the two cell unions have distance at least h/2 from
their singular endpoints. The integral of the absolute second
derivative over both is at most 4/h. The same centered-cell kernel
therefore gives

    e_central-log<=d/(2pi*m)<1/10^6.                 (12)

This retains the exact cell endpoints and needs no lower bound on
d, alpha or beta. The logarithmic integrals themselves use the
ordinary primitive x log x-x at those endpoints.

All cell errors above add over the disjoint unions; their bounds
have no factor for the number of cells or holes. Equations (7)-(12)
prove the complete outer replacement error

    e_outer<1/40000+2/50000+1/400000+1/10^6
            <1/14000.                               (13)

### 3. Fixed-count special rows with uniform harmonic tails

The kernel for f(x)=1/x has absolute bound 1/8 on unit centered
cells. Apply it after the first eight samples in (3). Convexity and
integration of f''=2/x^3 give

    |sum_{i=0}^{q-1} 1/(y+i)-H8(q,y)|
       <=1/[8(y+15/2)^2]<=1/450.                    (14)

For q<=8 the error is zero. Keeping the near-pole terms exact is
essential: this bound is uniform as y tends to zero.

Each row's sign set is cut by at most four arc endpoints from its
denominator/numerator conditions. Allowing the two exact collisions,
two exact numerator zeros, and the circle cut still gives at most
twelve contiguous blocks in either cotangent channel. This deliberately
loose count covers tangent and coincident endpoints. Each block has
two reciprocal sums, so (14) changes its Q value by at most
2/(450*h_inner), where h_inner=pi/n.

Every row in B lies within 1/2 of pi. Since tan(1/4)<1/3,

    |C_r|+|D_r|=max(p,|q+2a cot(v_r/2)|)/2<1.

There are at most four such rows. Their Rhat formula and the 12-block
bound therefore give, after normalization by nm,

    e_special<=192/(450*pi*m)<1/10^6.                (15)

There is no growing sum in Rtilde. Its signed term and the W,w'
terms are closed functions. There are at most two collision grid
indices per row, and their exact values use
P_n'(cos v)-cos(nu), P_n=T_(n+1)+T_n, with
T_k'(cos v)=k sin(kv)/sin v and its finite endpoint limits. These
are fixed-count trigonometric/sinc expressions, not polynomial sums
of increasing length. The finite-h endpoint rows already have the
O(R^2) sinc representation identified in N1-12.

Combining (13) and (15) proves the first line of (1). N1-12 adds
its unchanged error below 1/14000, proving the second line.

## What is and is not closed

The remaining outer computational count and the special-row harmonic
counts are now removed. This completes the specified near-phase
representation of the single corrected model with a proved uniform
error below the current half-budget. It neither spends nor proposes a
second row/jump correction. The unchanged old certificate obstruction
and all failed/deferred alternatives are preserved.

The new integrals and fixed special functions still require certified
evaluation when used in a computer-assisted maximum comparison. No
such comparison is claimed here. In particular the finite representation
may have phase-dependent cutoff/branch changes; an eventual interval
proof must enclose them, including the exact polynomial collision rows.
The full far-phase domain, the profile inequality and a usable argmax
onset remain OPEN. The original complete B3 gate is not declared passed.

## Verification and history

All bounds are analytic; no numerical evaluation, integration, fit or
mathematical computation was run. The full model (4) is defined before
any such evaluation. Distinct review of N1-13/14 and this file is
pending. 2026-11-06 after published 88e7023, requested gpt-6-astra ultra.
Candidate and 1/7000 objective: ../ideas/N1-round6.md. Root owns review,
publication and any further boundary authorization.
