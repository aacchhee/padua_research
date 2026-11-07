# PD-T?argmax-bridge-codex-D04-halfline — A uniform half-line cotangent defect

ID kind: PD-T. Aliases: truncated cotangent versus reciprocal mesh defect;
bounded symmetric cancellation reference. Split from: D04 practical joint
remainder, which remains OPEN. Split into: none.

## Statement and status

Let h>0, 0<v<pi/2, 0<=t<=1, d=v/h, and let psi be the real digamma
function defined by its convergent harmonic finite part. Define

    Q(h,v,t)=sum_{k>=0, v+h(k+t)<pi/2} cot(v+h(k+t))
                                      +(1/h)log(sin v).

An equality sample at pi/2 may be included with value zero. Then

    |Q(h,v,t)-(1/h)[log d-psi(d+t)]| <=4/pi.          (1)

For integer n>=1, h=pi/n, s>=0, and an n-point shifted circle mesh
x_k=x_0+k*h avoiding both poles 0 and -v modulo pi, put

    g0(x)=|-s cot x+s cot(x+v)|-s|cot x|-s|cot(x+v)|,
    t_-=frac(x_0/h), t_+=frac((x_0+v)/h),
    T0=sum_k g0(x_k)-(n/pi)*integral_0^pi g0(x)dx.

Then, with both offsets strictly between zero and one,

    Theta=-(2s/h)[2log(v/h)-psi(v/h+t_-)
                                    -psi(v/h+1-t_+)],
    |T0-Theta|<=16s/pi.                              (2)

Status: **PROVED**, written analytic developer result; distinct review
pending. This is a supporting identity with an explicit error, not the
full S_n-M_infty estimate. No numerical computation is a premise.

## Dependencies and definitions

For y>0 use

    psi(y)=lim_{K->infty}[log K-sum_{k=0}^{K-1}1/(k+y)].

Existence and psi(y+1)-psi(y)=1/y follow from elementary integral
comparison, as in C08-far-endpoint-constant.md. The nonzero arcs of g0
are the elementary opposite-sign minimum identity already proved in
N1-endpoint-tail.md. The proof below supplies the new uniform mesh defect.
Candidate/gate: ../ideas/D04-endpoint-reference.md.

## Proof

Put, for x>=0 and y=v+x,

    f_v(x)=cot y for y<pi/2, and 0 otherwise,
    r_v(x)=f_v(x)-1/(v+x).

The function r_v is continuous. Before y=pi/2 its derivative is
-csc^2 y+1/y^2<0; after that point its derivative is 1/y^2>0.
Its minimum is -2/pi, its limit at infinity is zero, and its initial
value cot v-1/v is nonpositive. Consequently

    Var_[0,infinity)(r_v)=4/pi+cot v-1/v<=4/pi.       (3)

On each cell [kh,(k+1)h], comparison of the value at (k+t)h with the
cell average costs at most the variation of r_v on that cell. Hence

    |sum_{k=0}^{K-1}r_v((k+t)h)
                    -(1/h)integral_0^{Kh}r_v(x)dx|<=4/pi.   (4)

The separate infinite sum and integral of r_v diverge; only these finite
matched differences are used. For the reciprocal term the matched
difference is exactly

    (1/h)[psi(d+t+K)-psi(d+t)-log(d+K)+log d],

which tends to (1/h)[log d-psi(d+t)]. For f_v both its sum and integral
stabilize as K tends to infinity. Its integral is -log(sin v).
Subtracting the reciprocal difference from the f_v difference in (4),
and then taking the limit, proves (1). No convergence of a separately
divergent sum or integral was asserted.

The only nonzero pieces of g0 on [0,pi) are

    -2s cot(x+v),  0<x<pi/2-v,
     2s cot x,     pi/2<x<pi-v.

For the first piece the positive distance from the pole at zero has
mesh offset t_-. For the second, reflect x about pi-v: its positive
distance from that pole has offset 1-t_+. Both pieces therefore have
the same truncated cotangent form in (1). Their separate integrals are
2s log(sin v), so their two mesh defects add to

    T0=-2s[Q(h,v,t_-)+Q(h,v,1-t_+)].

Applying (1) twice proves (2). The samples avoid the poles, so no
assigned value of g0 at a pole enters this argument. Cotangent zeros
and their equality samples have value zero and cause no ambiguity.

## Limits and verification

Equation (2) keeps the actual displaced arguments v/h+t. Replacing them
prematurely by their h=0 values would discard the endpoint matching
needed for D04. The two actual weighted pole profiles must remain in
any application to the corrected Padua polynomial; (2) does not create
an admissible whole A-channel kernel at an actual collision.

No scalar run, quadrature, board computation or fit was performed.
2026-11-06, root-supplied rules/input 2db4a226dad798491be3ec2fe5ce0238e21cfaec; requested Astra ultra,
serving metadata unexposed. Independent review is required before use.
