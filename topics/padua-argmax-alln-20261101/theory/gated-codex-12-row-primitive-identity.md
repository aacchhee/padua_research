# PD-T?argmax-alln-gated-codex-12 — Exact axis primitive row identities

ID kind: PD-T.
Aliases: direction1 round6 cotangent row resummation; signed row equals
n*a; negative-part sign intervals; beta-zero primitive decomposition.
Split from: quantitative row-sum repair of the primitive estimates.
Split into: none. A sharper uniform interior remainder remains OPEN.

## Statement and definitions

Use n>=2,m=n+1,N=nm and the corrected finite polynomial kernel of
gated-codex-02/03. Set beta=0, |alpha|<=2/5 and a=(1+cos alpha)/2.
For each periodic second index 0<=r<2m, put

v_r=r*pi/m, delta_r=1-r mod 2,

u_k=(delta_r*pi+alpha)/n+2k*pi/n, 0<=k<n,

F_k=(-1)^delta_r [D_n(u_k,v_r)-cos(nu_k)]/2,

T_r=sum_k F_k, R_r=sum_k |F_k|, Z_r=sum_k(-F_k)_+.

All values are polynomial at a quotient collision. Then

\[
 T_r=na\quad(1\le r<2m),\qquad
 T_0=-n(m-a),\qquad R_0=n(m-a).                          \tag{1}
\]

For an interior folded row put r_*=min(r,2m-r), so
v=r_* pi/m=min(v_r,2pi-v_r) in (0,pi) and r_*=r mod 2. Let

\[
 A_v=(\sin\alpha-2a\cot(v/2))/4,\qquad
 B_v=(\sin\alpha+2a\cot(v/2))/4.
\]

Away from a collision, exactly

\[
 F_k=A_v\cot((u_k-v)/2)+B_v\cot((u_k+v)/2).              \tag{2}
\]

The absolute row R_r is even in alpha. For its sign-interval evaluation
one may therefore put sigma=|alpha|, use its corresponding parity grid
u_k, and set D=(v,2pi-v). If sigma=0 set I empty. Otherwise put
q=(1+cos v)/tan(sigma/2); if q>=1 set I empty, and if q<1 set
I=(asin q,pi-asin q). With E the grid indices in the symmetric difference
D triangle I, excluding collisions, the complete absolute row is

\[
 R_r=na-2A_v\sum_{k\in E}\cot((u_k-v)/2)
          -2B_v\sum_{k\in E}\cot((u_k+v)/2).             \tag{3}
\]

Here the coefficients and grid in (3) use sigma, and zero terms may be
included or excluded without changing the sum. At an interior collision
the actual finite value is

\[
                        F_k=(n+\cos v)/2>0,             \tag{4}
\]

so it makes no negative-part contribution in (3).

For the endpoint r=m, the exact row is R_m(0)=n, and for
0<sigma=|alpha|<=2/5,

\[
 R_m=na+\sin\sigma\sum_{k=1}^{\lfloor n/2\rfloor}
                  \cot((k\pi-\sigma/2)/n),              \tag{5}
\]

in particular

\[
 0\le R_m-na\le
       \frac{n\sigma}{\pi-1/5}H_{\lfloor n/2\rfloor}.   \tag{6}
\]

The primitive therefore has the exact negative-part representation

\[
 S_n(\alpha,0)=1+\frac{2n}{m}a
                  +\frac2{nm}\sum_{r=1}^{2m-1}Z_r.      \tag{7}
\]

## Assumptions and status

Exact real arithmetic, the stated parity mesh and corrected x mode.
Overall status: **PROVED**, by the finite algebra below; supplementary
independent mathematical review and required Claude audit pending at
publication. No numerical computation is a premise. Candidate disposition:
retained exact supporting identity, while the quantitative repair is
stopped because no sharper interior negative-part estimate was obtained.

The full absolute-value primitive gain bound does not follow from (7).
It still requires control of the displayed negative partial sums relative
to their zero-phase values.

## Depends on

PD-T185 for the finite divided difference and Fourier kernel;
gated-codex-02/03 for the exact two-phase numerator and primitive
normalization. The cotangent full-sum identity is proved below, without
using or transferring an unread external theorem.

## Proof

### Quotient to cotangents

On beta=0, put T=(u-v)/2,P=(u+v)/2. The exact half kernel is

F=[a(1+cos v)-(sin alpha/2)sin u]/(cos u-cos v).

The elementary identities

(1+cos v)/(cos u-cos v)
  =-(cot(v/2)/2)(cot T-cot P),

sin u/(cos u-cos v)=-(cot T+cot P)/2

prove (2). Equivalently

A_v=-cos(alpha/2)cos((alpha+v)/2)/(2sin(v/2)),

B_v= cos(alpha/2)cos((alpha-v)/2)/(2sin(v/2)).

These coefficient factors vanish when the corresponding grid cotangent
has an actual removable collision. One must retain their product's
polynomial continuation rather than separately substituting zero times
infinity.

### Full cotangent sum from a polynomial

For any real z with none of z+k*pi/n a multiple of pi,

\[
 \sum_{k=0}^{n-1}\cot(z+k\pi/n)=n\cot(nz).               \tag{8}
\]

To prove this locally, let w=exp(2iz), omega=exp(2pi*i/n). Factoring
t^n-1 into its distinct roots omega^k and differentiating its logarithm
gives sum_k 1/(w*omega^k-1)=n/(w^n-1). This is also a rational
identity, obtained by multiplying through by the polynomial denominator.
Now cot(z+k*pi/n)=i(w*omega^k+1)/(w*omega^k-1); summing gives
i*n*(w^n+1)/(w^n-1)=n*cot(nz), proving (8).

Apply (8) with z=(u_0-v)/2 and z=(u_0+v)/2. For the folded row,
n*v=r_* pi-v and delta_r+r_* is odd because r_*=r mod 2.
The two terminal cotangents are respectively
-tan((alpha+v)/2) and -tan((alpha-v)/2). Inserting the factored
A_v,B_v gives the signed row n*cos^2(alpha/2)=na whenever these
intermediate expressions are regular. The finite row is analytic in
alpha, so polynomial continuation gives the same identity at every
removable value.

There is an alternative finite Fourier verification which also handles
the endpoint rows immediately. Summing over the n equally spaced first
angles kills every cosine frequency p with 1<=p<n. Only p=0,n survive
in the corrected kernel, giving

\[
 T_r=\frac n2\{(-1)^{\delta_r}D_n^{(1)}(v_r)+\cos\alpha\},
 \quad D_n^{(1)}(v)=1+2\sum_{q=1}^n\cos(qv).             \tag{9}
\]

For 1<=r<2m the finite sine/geometric sum gives
D_n^(1)(v_r)=(-1)^(r+1)=(-1)^delta_r, including v_r=pi by its
finite value. For r=0 its value is 2n+1 and delta_0=1. These facts
prove both signed identities in (1), retaining the corrected mode.

At r=0 the rational numerator is 2a-(sin alpha/2)sin u. On
|alpha|<=2/5 it is strictly positive, whereas cos u-1 is negative
on this odd first grid. There is no endpoint collision on this phase
range. Thus every F is negative and R_0=-T_0=n(m-a).

### Complete sign intervals and polynomial collisions

Reflecting first indices sends alpha to -alpha, preserving parity and
the finite kernel; hence R_r is even. For sigma>0 and 0<v<pi,
the numerator is negative exactly when sin u>q. This is I if q<1,
and is empty if q>=1. The denominator is negative exactly on D.
Away from zero numerators and collisions, F is negative precisely on
the symmetric difference D triangle I. Since R_r=T_r+2Z_r and
T_r=na, inserting (2) on those negative indices proves (3).
At a numerator zero its contribution is zero, so boundary conventions
there do not affect the sum.

An actual interior collision has cos u=cos v. From
P_n=T_(n+1)+T_n and v=r*pi/m with 0<v<pi,

P_n'(cos v)=n*(-1)^(r+1),

cos(nu)=cos(nv)=(-1)^r cos v.

Multiplication by (-1)^delta_r/2 therefore gives exactly (4).
This is positive and contributes nothing to Z_r. This argument handles
both signs of the collision phase. It also justifies the continuation
of the signed full-row calculation without an artificial cotangent pole.

### The pi endpoint and its shrinking linear coefficient

At v=pi the quotient reduces, when alpha is nonzero, to
F=(sin alpha/2)cot((u-pi)/2). At alpha=0, all regular values are
zero and the polynomial value at u=pi is n. This proves R_m(0)=n.
For sigma>0 the negative values occur on 0<u<pi. Their parity
indices are j=n-2k, 1<=k<=floor(n/2), and

-F=(sin sigma/2)cot((k*pi-sigma/2)/n).

Together with the signed row na this proves (5). All these cotangent
arguments lie in (0,pi/2), so cot t<=1/t, sin sigma<=sigma and
k*pi-sigma/2>=k*(pi-1/5) imply (6). In particular the normalized
endpoint negative-part error is at most
sigma*H_floor(n/2)/(m*(pi-1/5)); it shrinks like sigma*log(n)/n.
This controls that endpoint only, not the interior row remainders.

Finally R_r=T_r+2Z_r for each nonzero row. Summing those identities
and R_0=n(m-a), then dividing by N=nm, gives

n(m-a)/N+(2m-1)na/N+2 sum Z_r/N
  =1+(2n/m)a+2 sum Z_r/N,

which is (7). This completes the proof.

## Checks and limits

The predeclared bounded correctness run in gated/d1/r06-row-sum.md
executes n=2,3,4,8,16 and alpha=0,+-.17,+-.4 only, with every periodic
second row. Its agreement is MEASURED binary64 sanity evidence and is
not a premise. Source/output identities and the actual maximum errors
are recorded in the round note. No larger degree or fitting run occurred.

The primitive excess can be written exactly as

S_n(alpha,0)-a*Lambda_c
 =1-a+(2/N)[Z_m(alpha)+2 sum_(r=1)^(m-1)(Z_r(alpha)-a Z_r(0))].

The endpoint is bounded by (6), but the interior sign intervals change
with the row and phase, and their cotangent poles move relative to the
grid. No sharper uniform estimate for those partial-sum differences is
proved here. The row identities consequently do not justify continuing
the stalled quantitative primitive route or an all-degree conclusion.

## Sources and history

2026-11-02, Codex assigned gpt-6.1-sol xhigh; runtime metadata not
independently exposed. Rules/snapshot
`2dde541f1e5af239cae6e93e4438b9be89d15d87`, scientific base
`7d308b10d946b607ae0690454f6c0103690775a4`.
Registered direction1 round6, same candidate/obstruction gate as the
earlier phase work. Exact identities retained despite STOP of this
quantitative repair. Required independent review and Claude audit remain
pending at publication. No shared registry, Git, future round or
direction-2 action by this worker.
