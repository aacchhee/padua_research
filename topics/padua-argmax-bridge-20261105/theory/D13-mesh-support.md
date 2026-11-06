# PD-T?argmax-bridge-codex-D13-mesh — Origin-relative singular-mesh remainder

ID kind: PD-T. Aliases: phase-relative macroscopic h/g mesh; paired upper
mesh constants; exact leading-coefficient cancellation.
Split from: D13 full finite relative remainder, OPEN.
Split into: none. This file concerns only D07's two scalar remainders.

Rules/input `e13a538bda80e6cc785f4835937b2ca338bc1d6f`.
2026-11-06, parent-assigned Codex Sol xhigh; serving metadata unexposed.
Written analytic developer result; distinct review required.

## Statement and exact definitions

Let n>=32 be an integer, m=n+1, L=log n, and let alpha,beta>=0 with
rho=alpha+beta<=1/2. Put

    a=(cos alpha+cos beta)/2, t=beta/pi,
    d=(sin beta-sin alpha)_+,
    B=4a/pi^2, D=U0/pi+B log pi,
    eps=log(m/n), Z=D-B eps.

Use EXACTLY the complete U0 and the convergent h_j,g_j constants of
[D07-global-mesh.md](D07-global-mesh.md), including its actual last
index m-1=n. Write

    H_j(t)=h_j(t)+h_j(1-t), Q_j(t)=g_j(t)+g_j(1-t).

The new letter Q avoids confusion with D07's intermediate G_n. The
objects Rmesh and Rlog below are EXACTLY D07 equation(6), with every
constant and the exact n/m displacement unchanged. A superscript zero
means their value at alpha=beta=0 and the SAME integer n. Then

    |Rmesh(phi)-a Rmesh(0)| < rho/(2n)             (rho>0),       (1)
    |Rmesh(phi)-a Rmesh(0)| <= rho/(2n)            (all rho),     (2)
    |Rmesh(phi)-a Rmesh(0)|+(d/pi)|Rlog(phi)|
                    <=rho[L+7/3]/n
                    <=(7/3)rho(1+L)/n.                         (3)

Overall status: **PROVED**, analytic developer proof below. The full
finite S-aS(0) comparison remains **OPEN**, because the retained-row,
regular outer-quadrature and row-reduction relative errors are outside
this theorem. The substantive split here is a supporting lemma, not a
proved conjunct of that full target.

## Dependencies

- D07-global-mesh supplies the exact Rmesh,Rlog definitions, its exact
  telescoping to index n, and |Rlog|<=Blog.
- N1-round4-mesh supplies the convergent h/g definitions and the
  centered-cell tail bounds, applied to the actual upper endpoints.
- N1-joint-endpoint-profile gives the complete U0 formula.
- N1-regularized-pole gives sup|Phi_0|<=4 and Lip(Phi_0)<=12.

No D10 constant estimate, finite-board claim, numerical premise or
external source theorem is used. D07-global-outer fixes the six-row
geometry being complemented, but its absolute allowance is not used
to infer a relative allowance.

## Proof

### 1. Cancel the exact leading coefficient before all estimates

Directly expand D07's Tmesh and subtract its displayed lower h/g
constants. This is a finite algebraic identity:

    Rmesh=-B eps H_2(t)-Z H_n(t)-B Q_n(t)-B L^2-2D L.          (4)

The index n is m-1 literally. No endpoint truncation or replacement
of eps=log((n+1)/n) by zero occurred. In particular

    B=a B^0,
    DeltaD=D-aD^0=(U0-aU0^0)/pi,
    Z=aZ^0+DeltaD.

Subtract a times (4) at zero phase BEFORE taking absolute values:

    Rmesh(phi)-a Rmesh(0)
      =-B eps[H_2(t)-H_2(0)]
       -aZ^0[H_n(t)-H_n(0)]
       -B[Q_n(t)-Q_n(0)]
       -DeltaD[H_n(t)+2L].                                  (5)

Thus B L^2 cancels exactly, and the apparent 2L DeltaD term is part
of H_n(t)+2L. Estimating it separately would lose the result below.

### 2. Paired h/g increments, including their constant terms

The definitions in N1-06 also give the finite-limit representations

    h_j(v)=lim_(K->infty)[sum_(k=j)^K 1/(k+v)
                                      -log(K+v+1/2)],
    g_j(v)=lim_(K->infty)[sum_(k=j)^K log(k+v)/(k+v)
                                -log^2(K+v+1/2)/2].

Their differentiated series converge uniformly on 0<=v<=1, so

    h_j'(v)=-sum_(k=j)^infty (k+v)^(-2),
    h_j''(v)=2sum_(k=j)^infty (k+v)^(-3),
    g_j'(v)=sum_(k=j)^infty [1-log(k+v)]/(k+v)^2,
    g_j''(v)=sum_(k=j)^infty [2log(k+v)-3]/(k+v)^3.            (6)

Uniform differentiation can equivalently be justified by applying
the integral test to each derivative of the finite-limit expressions;
the differentiated terminal logarithms tend uniformly to zero.
Consequently

    |H_2'(v)|<=2sum_(k=2)^infty k^(-2)<=2,
    |H_n'(v)|=|h_n'(v)-h_n'(1-v)|<=(n-1)^(-2).              (7)

For the second inequality use |2v-1|<=1 and
sup h_n''<=2 integral_(n-1)^infty x^(-3)dx.

For x>=n-1>=31, (2log x-3)/x^3 is positive and decreasing.
Hence (6) and the same pairing yield

    |Q_n'(v)|<=sup_(0<=w<=1)|g_n''(w)|
       <=integral_(n-1)^infty (2log x-3)/x^3 dx
       =[log(n-1)-1]/(n-1)^2
       <=(L-1)/(n-1)^2.                                    (8)

Using 0<=t<=rho/pi<rho/3, (7)--(8) imply

    |H_2(t)-H_2(0)|<=2rho/3,
    |H_n(t)-H_n(0)|<=rho/[3(n-1)^2],
    |Q_n(t)-Q_n(0)|<=rho(L-1)/[3(n-1)^2].                  (9)

The paired form in (7)--(8) is essential: it retains the upper h/g
constants instead of replacing each by an unrelated tail allowance.

### 3. The small coefficient of DeltaD

The actual upper cell endpoints are n+c and n-c with
c=t-1/2, |c|<=1/2. N1-06's reciprocal tail identity gives

    H_n(t)=-log(n+c)-log(n-c)-E_h,
    0<=E_h<=1/[4(n-1/2)^2].

Therefore, using -log(1-y)<=y/(1-y),

    |H_n(t)+2L|
       <=1/(4n^2-1)+1/[4(n-1/2)^2]
       <1/n^2.                                             (10)

For example, n>=2 gives 4n^2-1>=3n^2 and n-1/2>=3n/4,
so the right side before the strict inequality is <=7/(9n^2).
This is the cancellation of the large logarithm in the last line
of (5), rather than a separate estimate for 2L DeltaD.

To bound DeltaD put e=alpha+beta and delta=alpha-beta, and write
f(x)=Phi_0(1/2+x/(2pi)). The inherited exact endpoint numerator is

    U0=c_e f(delta)+c_delta f(e),
    c_e=cos(e/2), c_delta=cos(delta/2), a=c_e c_delta,
    U0^0=2f(0).

On the stated near triangle both cosine factors lie in[0,1]. Thus

    U0-aU0^0
      =c_e[f(delta)-f(0)]+c_delta[f(e)-f(0)]
                      +f(0)[c_e+c_delta-2c_e c_delta].

Here Lip(f)<=6/pi, |f(0)|<=4, and

    0<=c_e+c_delta-2c_e c_delta
       <=(1-c_e)+(1-c_delta)
       <=(e^2+delta^2)/8<=rho^2/4.

Consequently

    |U0-aU0^0|<=12rho/pi+rho^2<=(9/2)rho,
    |DeltaD|<=(3/2)rho.                                   (11)

Also B<=1/2, eps<=1/n, and |Z^0|<5. Indeed |U0^0|<=8,
log pi<6/5 and pi>3 give |D^0|<4, so
|Z^0|<=|D^0|+B^0 eps<4+1/64<5.

### 4. Explicit finite-n constant

Insert (9)--(11) in (5). For every rho>=0,

    |Rmesh(phi)-a Rmesh(0)|
       <=rho[1/(3n)+(L+9)/(6(n-1)^2)+3/(2n^2)].             (12)

For n>=32, (n-1)^2>7n^2/8. The function
(log n+9)/n decreases there, and log32<4, whence

    (L+9)/n<=13/32,
    n/rho * right side of (12)
       <1/3+13/168+3/64=205/448<1/2                       (rho>0).

This proves (1)--(2), including rho=0 by the exact identity (5).
The elementary log32<4 follows, for example, from e_Euler>5/2
and (5/2)^4>32; no scalar numerical evaluation is involved.

Finally D07's unchanged central-log bound is

    |Rlog(phi)|<=[3log m+log2+2log pi+2]/m.

Since log m=L+eps<=L+1/32, log2<1, log pi<6/5,
and 3/32+1+12/5+2=879/160<11/2, it follows that

    (d/pi)|Rlog(phi)|<=rho[L+11/6]/n.                       (13)

Here d<=sin beta<=beta<=rho. Add (2) and (13) to obtain (3).

## Scope, checks and remaining gap

These are the literal D07 remainders, not a new correction or a new
near/far model. The exact n/m displacement, the h/g lower constants,
their actual last index and the phase-dependent U0 all remain in (4).
The proof covers both phase axes and phase zero. Extension by separate
absolute phases is available under the inherited even-phase convention.
No claim on larger rho or all closed phases is made here.

The full relative finite remainder still needs the phase increments of
the six actual polynomial rows, the regular F quadrature completion,
and the D04 reduction error. Two absolute bounds for any of those do
not close that obligation. This supporting theorem supplies only the
scalar singular-mesh component and does not change the full target's
OPEN status, an onset, a certified degree range, or an old model.

Paper proof only. No numerical job, board evaluation, scalar run,
quadrature, fit or native calculation occurred. Repository operations
were read-only except the three parent-owned D13 mesh-support files.
Independent mathematical review has not been performed by this author.
Gate coverage and its limits are recorded in
[the candidate](../ideas/D13-mesh-support.md).


### Supplementary review closure — 2026-11-06

Distinct Astra high mathematical reconstruction ACCEPTED the two support
scopes and the full target's OPEN status, no unresolved findings;
[independent-checks-D13-relative-support.md](../independent-checks-D13-relative-support.md),
report SHA256de9a18a24b1acc2c78ddfe71ab55f665f4145fb3fc3c5474d82f62dde396eaaf.
The display NOTE interprets strict intermediate estimates at positive rho;
at rho=0 the exact subtractions vanish. Final non-strict statements and
audited proof text are unchanged. No numerical jobs or new onset result.
