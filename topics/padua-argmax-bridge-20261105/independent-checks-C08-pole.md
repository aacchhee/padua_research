# Independent supplementary review — C08 pole functional

Reviewer: distinct Codex `/root/c01_near_review`, parent-assigned Astra high;
serving identity and effective effort are not independently exposed.
Date: 2026-11-06. Rules were read at
`4b728b04216a5490910780bc609a82b853058426`; their diff to review
input HEAD `547a473a6e1c1268ff4f1ada7243b12afb02d0bc` was checked
empty in this review sequence. Branch:
`codex/padua-argmax-bridge-20261105`.

**Disposition: accepted at the stated scalar scope, with no mathematical
finding.** The functional exists at every real phase, including cusp
phases, satisfies H<749/1500<1/2, and has the asserted signed
finite-cutoff upper error. The two-channel error at delta=1/100 is
strictly below 27/1000. This does not itself bound the complete
renormalized cancellation integral or prove the far-model comparison.
Formal Claude audit is separate and pending.

## Frozen source and coverage

Reviewed `theory/C08-far-pole-functional.md`, SHA-256
`6cb61ebc3f3808c61bc8d72feb2bee3a57c1dbecf597a7915833b4f43c8cda67`.
Read the full source and complementary C08 integral idea; the C08
comparison idea/attempt, endpoint and coefficient sources and exact
C06 model contract were already read in this bounded review sequence.
Reread the full N1-04 pole source, C04 sharp-remainder section 1,
C06-far-full-profile section 6, and C06 compact model definitions.
The source's shortened C06-far-profile reference resolves to the
global scalar argument in `C06-far-full-profile.md` section 6.

Only globally proved scalar statements from those predecessors are
used. No near-domain two-phase theorem is extended by assumption.
This review excludes historical novelty, priority and a full registry
or author-search audit. No numerical quadrature, phase sample, fitted
constant, mathematical program or computational certificate was used.
Source reads and hashes were the checking commands. Only this new
report was written; no author source, prior report, shared file or
Git state was changed.

## Full-period range

N1-04 defines the periodic Phi_0 continuously with value 1 at each
integer. Reflection about a half-integer shows that
f(x)=Phi_0(1/2+x/(2pi)) is even and 2pi-periodic. Every real x
therefore reduces to x=pi*y, 0<=y<=1, for the range calculation.

C06's global upper bound uses the exact decomposition

    Phi_0(t)=sinc(pi*t)+[2gamma-2log pi+R(t)]sin(pi*t)/pi,
    0<=R(t)<=4t²<=1, 0<t<=1/2.

The bracket is negative by gamma<3/5 and log pi>11/10.
Consequently Phi_0<=1 on this half-period, and reflection,
periodicity and continuity supply the global upper bound. This
argument has no small-phase restriction.

For the new lower bound, the reciprocal-pair identity has exactly the
coefficient 4 in source (6). Keeping its positive l=1 term gives

    pi*f(pi*y)>=c*k0+4c*y²/(1-y²),
    c=cos(pi*y/2), k0=C(1/2)-2log pi.

The auxiliary inequality c>=(3/4)(1-y²) follows from the source's
q(t), t=1-y. Its second derivative decreases from a positive to a
negative value and crosses zero once. Thus q' first increases and
then decreases to q'(1)=0, with q'(0)>0. Hence q'>=0 and q>=0.
The signs and both endpoint derivatives in this argument are correct.

It follows that the retained rational term is at least 3y².
The constants give k0<2, while 1-c<=pi²y²/8 and pi²<10, so
k0(1-c)<(5/2)y²<=3y² when k0>=0. If k0 were negative the
same desired inequality would hold immediately; the subsequent
lower bound in fact proves k0>0. Thus f(pi*y)>=k0/pi in the
open range, and continuity covers y=1.

The elementary lower estimates give
k0>2(23/40)+4(69/100)-2(23/20)=161/100>pi/2.
The exponential series through degree 5 at 23/20 exceeds 22/7,
so its stated proof of log pi<23/20 is valid. Therefore f>1/2
everywhere, and the weaker closed range [1/2,1] used later follows.
In particular the cusp value is 1; no divergent unweighted C value
is assigned there.

## Global curvature, jumps and scaling

C04 section 1 proves the distributional inequality Phi_0''<=12 dt
on the entire real line. Its proof on (0,1/2] uses R''<=19,
the negative sinc second derivative, and the upper bound
2R'cos(pi*t)<=3pi/4. Together with the remaining sine term these
give Phi_0''<=-pi²/12+2pi+19/pi<12. Reflection covers each
open period; the derivative matches at the half-integer.

At each integer the derivative jump is
2(2gamma-2log pi)<0. Thus these atoms have the favorable sign
for an upper second-derivative measure bound. They are not removed
by imposing smoothness at the cusp. Integration against the positive
triangular kernel gives the global second-difference upper bound
12t², including intervals crossing any integer.

The phase scaling t=v/(2pi) consequently gives

    f(x+v)+f(x-v)-2f(x)<=3v²/pi².

N1-04's global Lipschitz constant 12 becomes Lip(f)<=6/pi.
This estimate remains valid across cusps and supplies the absolute
integrability needed below. The curvature inequality is one-sided;
no absolute quadratic remainder is assumed at a cusp.

## Exact subtraction at both singular endpoints

Pairing v and 2pi-v uses periodicity to replace f(x+2pi-v) by
f(x-v). The exact constant-kernel integral is

    integral_delta^(2pi-delta) dv/[2sin(v/2)]
       =2log cot(delta/4).

After including the precise 2f(x)log(delta/pi) subtraction, its
limiting constant is lambda0=(2/pi)log(4/pi). Thus the source's
representation (8) has the correct overall factor 1/pi and no
uncancelled endpoint constant. The second-difference numerator has
absolute value at most 12v/pi, whereas the denominator is comparable
to v. Its integral at zero is therefore absolutely convergent, even
when x is a cusp position. The other endpoint has already been
included by pairing; there is no separate singular integral to assign.

The scalar comparison lambda0<1/(2pi) follows from pi>25/8
and exp(1/4)>32/25. The latter follows from the first four
positive series terms. Since f>=1/2>0, replacing lambda0 by
1/(2pi) later makes a strict upper bound for every x.

## Range/curvature envelope and exact integration

Set q=1-f(x), so 0<=q<=1/2. The range upper bound gives the
second difference at most 2q, and the curvature estimate gives
at most Kv² with K=3/pi². Replacing it by min(Kv²,2q) is
valid even when the actual second difference is negative. The
replacement is nonnegative, so an upper kernel bound can then be
multiplied without reversing an inequality.

For x=v/2 and t=x²<=pi²/4<5/2, multiplication of the alternating
sine lower polynomial gives exactly

    (1+t/4)(sin x/x)-1
       >=t/12-t²/30+19t³/10080-t^4/20160.

The first two terms sum to t(5-2t)/60>=0, and the remaining
two to t³(38-t)/20160>0 when t>0. Rearranging yields
1/[2sin(v/2)]<=1/v+v/16 on the full required interval.

For q>0 the switch point is t_q=pi*sqrt(2q/3)<pi. Direct
integration on its two sides gives q from the quadratic times 1/v
part, q log(3/(2q)) from the constant times 1/v part, and
(pi²/16)(q-q²/3) from the v/16 terms. This verifies source (11)
including its factors of two. The expression tends to zero as q
tends to zero, so it also covers q=0.

After the strict lambda0 replacement the resulting upper bracket has
derivative

    log(3/(2q))-1/2+(pi²/16)(1-2q/3)>0

for 0<q<=1/2. Thus its largest value is at q=1/2. Substitution
gives [3/4+(1/2)log 3+5pi²/192]/pi. The elementary strict
bounds log 3<11/10, pi²<10 and pi>25/8 give

    H(x)<[3/4+11/20+25/96]/(25/8)
         =(749/480)*(8/25)=749/1500<1/2.

The remaining gap is exactly 1/1500. No numerical evaluation of
the profile or its singular integral enters this estimate.

## Signed cutoff and exact C06 channel interface

For the finite cutoff, the constant coefficient is
lambda_delta=(2/pi)log[(delta/pi)cot(delta/4)]. Since
z cot z<1 for 0<z<pi/2, lambda_delta<lambda0. Its contribution
to H_delta-H is strictly negative because f>0. The remaining
difference is minus the second-difference integral from 0 to delta.
Using its absolute Lipschitz bound only for this omitted piece gives

    H_delta-H <(12/pi²) integral_0^delta(1+v²/16)dv
               =(12/pi²)(delta+delta³/48).

This also explains why the source's displayed non-strict intermediate
estimate establishes the strict asserted bound: the discarded constant
coefficient difference is strictly favorable.

In the exact C06 model, d=alpha-beta, e=alpha+beta, and

    V(v)=[c_e f(d+v)+c_d f(e-v)]/[2sin(v/2)],
    U0=c_e f(d)+c_d f(e).

The substitution v -> 2pi-v, with periodicity of f, converts the
second orientation to the same functional as the first. Consequently
the pole integral together with its own subtraction is exactly
c_e H_delta(d)+c_d H_delta(e). On the full closed triangle,
c_e=cos(e/2) and c_d=cos(d/2) both lie in [0,1], with sum<=2.
Zero weights at a=0 or a vertex cause no problem because H and
H_delta are finite at every phase.

At delta=1/100 the two-channel excess is bounded above by

    (24/pi²)(1/100+1/48000000)
       <(8/3)(1/100+1/48000000)<27/1000,

using only pi²>9 and rational arithmetic. Weights summing to zero
give zero excess and still satisfy the claimed strict upper. No
coefficient, orientation or extra copy of the endpoint subtraction
is lost in this interface.

## Findings and use boundary

No BLOCKING, MAJOR, MINOR or mathematical NOTE finding. The scalar
full-period result and its two-channel cutoff allowance are accepted.
The cancellation integral, the other logarithmic terms in C06's fixed
constant, and the final far-model maximum comparison are separate
obligations. This review does not supply those bounds or promote any
global argmax claim. Required formal audit remains separate.
