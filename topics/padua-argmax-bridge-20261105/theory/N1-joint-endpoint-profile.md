# PD-T?argmax-bridge-codex-N1-05 — Joint logarithmic endpoint profile

ID kind: PD-T. Aliases: regularized two-pole endpoint compactification;
uniform constant-profile tail; exact logarithmic coefficient separation.
Split from: N1 full-diamond finite-dimensional model and usable onset,
both still OPEN. Split into: none.

## Definitions and statement

Let alpha,beta>=0, alpha+beta<=pi, and use a,p,q,P,C(v),D(v),I from
N1-03. Put e=alpha+beta, d=alpha-beta, c_e=cos(e/2), c_d=cos(d/2),

    eta_-(v)=1/2+(d+v)/(2pi),
    eta_+(v)=1/2+(e-v)/(2pi).

Use the continuous periodic Phi_L of N1-04. For 0<v<2pi, v!=pi,
define the explicit family

    H(L,v)=[c_e Phi_L(eta_-(v))+c_d Phi_L(eta_+(v))]
                /[2sin(v/2)] + I(C(v),D(v),v)/pi
          = A(v)*L+B(v),                                (1)

where

    A(v)=[c_e |cos((d+v)/2)|+c_d |cos((e-v)/2)|]
                /[pi sin(v/2)],
    B(v)=[c_e Phi_0(eta_-(v))+c_d Phi_0(eta_+(v))]
                /[2sin(v/2)] + I(C(v),D(v),v)/pi.

In particular A(v) is a fixed piecewise trigonometric function; its
coefficient is retained exactly, rather than bounded by a growing error.
Define

    U0=c_e Phi_0(1/2+d/(2pi))+c_d Phi_0(1/2+e/(2pi)).

For z=min(v,2pi-v), 0<z<=pi/4, the joint constant-profile remainder obeys

    |B(v)-[U0+(4a/pi)*log z]/z|
       <=7+(P/pi)*[3+2log(4pi/z)].                     (2)

The bound is independent of L, the degree, and inverse powers of a.
Thus it remains valid on the entire closed phase diamond, by separate
absolute phases, including a=0. Keeping the A(v)L term is necessary for
this L-independent conclusion.

For n>=2, m=n+1, v_r=(r*pi+beta)/m, and 0<delta<=pi/4, let E_delta
be any subset of the nonendpoint rows 1<=r<=2m-2 with
z_r=min(v_r,2pi-v_r)<=delta. Write

    Z_B(v)=B(v)-[U0+(4a/pi)*log z]/z.

Then the whole discrete endpoint residual satisfies

    (1/m)*sum_{r in E_delta}|Z_B(v_r)| <= Q(P,delta),     (3)
    Q(P,delta)=(2delta/pi)*
        [7+(P/pi)*(5+2log(4pi/delta))].

The same bound holds for the continuous residual tail
(1/pi)*integral_{(0,delta) union (2pi-delta,2pi)} |Z_B(v)|dv.
Thus deleting either tail costs at most Q, and comparing the signed
discrete and continuous tails costs at most 2Q. This removes the endpoint
residual's degree-dependent number of rows from the error bound.

### Connection to the actual primitive

Take 2<=R<=n and N1-02's special-row set A_R, of cardinality <=2R+4,
including all polynomial collisions and its two central rows. Use its
same Rhat_r (exact on the two endpoint rows) and define

    J_(n,R)=(1/(nm))*sum_{r in A_R} Rhat_r
                +(1/m)*sum_{r outside A_R} H(log n,v_r).

Then

    |S_n-J_(n,R)| <= r_n+E_(n,R)+D_n,                   (4)
    E_(n,R)=2P H_n/n+2a(n+1)/(n(R-1)),
    D_n=10/n^2+20a H_n/(pi*n^2),

with r_n from N1-01 and H_n the harmonic number. This uses the original
corrected kernel and exceptional mode. Exact collision rows remain in
A_R: a continuous pole-profile extension is not a substitute for their
polynomial values. Formula (4) still has an outer sum. The genuinely new
count-free reduction is its joint endpoint residual estimate (2)-(3).

## Status, assumptions and dependencies

Overall status: **PROVED**, analytic developer proof; distinct review
pending. Exact real arithmetic. No fit or computation is a premise.
N1-03 proves the endpoint cancellation estimate, N1-04 the regularized
pole estimate and periodic constants, and N1-01/N1-02/N2 supply the
actual row identity, coefficient sum, special rows and their errors.
No external source theorem is imported. The full all-degree finite
certificate and effective argmax threshold remain OPEN.

## Proof

### 1. Joint pole products and the exact logarithmic coefficient

Elementary half-angle identities, with a=c_e*c_d, give

    C(v)=-c_e*sin(pi*eta_-(v))/[2sin(v/2)],
    D(v)= c_d*sin(pi*eta_+(v))/[2sin(v/2)].               (5)

Both c_e and c_d are nonnegative. Hence a weighted single-pole norm is
regularized by its sine factor before approaching an integer offset.
For noninteger offsets N1-04 gives exactly

    |C|*B_n(frac eta_-)/n+|D|*B_n(frac eta_+)/n
      =[c_e F_n(eta_-)+c_d F_n(eta_+)]/[2sin(v/2)].

Replacing F_n by Phi_(log n) has error at most
5(|C|+|D|)/n^2. Also

    Phi_L(t)=Phi_0(t)+(2L/pi)*|sin(pi*t)|.

This proves the exact decomposition H=A L+B in (1). The extension at
integer offsets is only the definition of H; actual collision rows
continue to use their separate polynomial convention.

### 2. Constant pole profile at the two endpoints

Let N_0(v)=c_e Phi_0(eta_-(v))+c_d Phi_0(eta_+(v)). Its endpoint value
at v=0 is U0. At v=2pi the two arguments change by +1 and -1,
respectively, so periodicity gives the identical value U0.
The bound Lip(Phi_0)<=12, the slopes 1/(2pi), and c_e,c_d<=1 give

    |N_0(v)-U0|<=12z/pi,          |U0|<=8.              (6)

For 0<z<=pi/4, sine chords and x-sin x<=x^3/6 imply

    2sin(z/2)>=2z/pi,
    0<=1/[2sin(z/2)]-1/z<=pi*z/48.

Since sin(v/2)=sin(z/2), (6) yields

    |N_0(v)/[2sin(v/2)]-U0/z| <=6+pi*z/6.              (7)

No phase-offset derivative or distance from an integer was used.

### 3. Explicit logarithmic integral at an endpoint

N1-03 supplies

    |I(C,D,v)-2a cot(z/2)log(sin z)|
       <=P*[3+2log(4pi/z)].                            (8)

For 0<x<=pi/8,

    0<=1/x-cot x
       =[sin x-x cos x]/[x sin x]
       <=pi*x/6,

because the numerator is integral_0^x t sin t dt<=x^3/3 and
sin x>=2x/pi. Also 0<z<1 and sin z/z>=1-z^2/6 give

    0<=-log(sin z/z)<=z^2/(6-z^2)<=z^2/5.

Using cot(z/2)<=2/z, these imply

    |2a cot(z/2)log(sin z)-(4a/z)log z|
       <=a*z*[(pi/6)*|log z|+4/5]
       <=a*z*(1+|log z|).                              (9)

Since z(1+log(1/z))<=1 for 0<z<=1, a<=1, and pi^2<10,

    6+pi*z/6+(a/pi)*z*(1+|log z|)
       <=6+pi^2/24+1/pi<7.

Combine (7)-(9), dividing the integral contributions by pi, to prove
(2) at both endpoints. This subtraction is from B only; the distinct
A(v)L term remains exact.

### 4. Uniform whole-tail bound and actual row error

The envelope on the right of (2) is positive and decreasing in z.
Apply the left/right mesh comparison in N1-03 section 3, now with
normalization 1/m=(pi/m)/pi. Integrating the envelope gives (3) and the
identical continuous-tail bound. No sign decision or endpoint row count
appears in Q.

For every nonspecial row, N1-02's shifted cancellation quadrature and
N1-04's pole estimate give

    |(1/n)*sum_k |F_rk|-H(log n,v_r)|
       <=5(|C_r|+|D_r|)/n^2
                 +4max(|C_r|,|D_r|)/(n|sin v_r|).

The latter term sums, after division by m, to at most E_(n,R), exactly
as in N1-02. N1-01's full nonendpoint coefficient bound is

    sum_{r=1}^{2m-2}(|C_r|+|D_r|)<=2m+4am H_n/pi.

Therefore the first term contributes at most D_n. The special-row
approximation error is bounded by r_n; its endpoint rows are exact.
Adding these errors proves (4). Separate phase evenness gives every
quadrant, as in N1-01.

## Scope, limits and next falsifiable step

This theorem identifies a joint endpoint logarithm after both moving
pole factors have been regularized. Its remaining endpoint residual has
an explicit tail bound uniform in n, L and every phase, and can be
deleted with that cost. A phase-dependent coefficient zero cannot make
the bound blow up. These properties distinguish it from an O(n)-term
algebraic rewrite or a fitted log-family coefficient.

It does not yet sum the singular terms [U0+(4a/pi)log z]/z, replace the
interior outer sum by a finite certificate, or control every exceptional
row uniformly in h=1/n. Those are the exact missing compactification
steps. The next candidate must combine the endpoint harmonic/logarithmic
mesh sum with the finite exceptional rows and prove its remainder; it
must also account for the central v=pi chart. Merely producing more
phase samples or rewriting (4) is not further progress.

The complete N1 target remains OPEN, with no usable n1 and no B3 PASS.
The original B3 kill and one-correction limit still apply to the eventual
complete model error, not any of the isolated terms in (4) or (3).

## Checks and history

No numerical computation, fit or sample is a proof input. A separate
bounded analytic critique reconstructed the endpoint constants and found
no gap; distinct review of this frozen record remains pending. Candidate
and exact target were recorded in ../ideas/N1-endpoint.md before this
proof. 2026-11-05, round 3 at pushed boundary c000899, Codex requested
gpt-6-astra ultra; runtime metadata not independently exposed.
