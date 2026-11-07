# C08 complementary integral attempt

2026-11-06. Rules/input and complete gate are in ../ideas/C08-far-integral.md.
The assigned target is the exact K_delta<=1/2 on the full closed phase
triangle, delta=1/100, with no changed model. The endpoint convolution
and its R64 tail are separately owned by the C08 comparison worker.

Initial exact bookkeeping: writing l=log delta gives

    K_delta=(4a/pi²)(l²-log² pi)+(2U0/pi)(l-log pi)
                                +(1/pi) integral B.

Thus the two endpoint U0/z and (4a/pi)log(z)/z singularities cancel
exactly with the displayed polynomial. Independent absolute bounds on
these terms before cancellation are unsuitable. No new execution,
sample, fit or interval computation has occurred in this continuation.

Analytic continuation: the generic cancellation remainder R is
nonpositive, since its separation derivative is nonnegative and its
value at separation pi/2 is zero (the same-sign entropy branch is also
nonpositive). Summing the two folded coefficient pairs therefore gives

    I_L+I_R<=4a cot(z/2)log(sin z)+2sin(alpha)|log(sin z)|.

The exact renormalized integral of the first term is -c*a, with
c=1/3+4(log²pi-log²2)/pi²>1/2. The second contributes at most
.45sin(alpha). A uniform scalar pole-functional bound H<1/2 then gives
the limiting upper .5(1+a)-c*a+.45sin(alpha)<=.95.

The stronger scalar domination H(x)<=cos(x/2)H(0) was considered and
left OPEN; it is not needed. A sharper curvature-only route Phi''<=8
was also considered without execution or a completed proof; the worker's
existing global one-sided Phi''<=12 and a sharper kernel inequality
suffice for H<1/2. These are alternate proof estimates, not refutations.

The separately developed extra1/2 finite-corner lower makes K_delta<1
sufficient. The original K_delta<=1/2 target remains OPEN. The explicit
finite-cutoff charges are less than.027 for the pole functional and
1e-5 for the sine-log primitive, giving K_delta<.98. The theorem is
being written with the scalar lemma as a separate named dependency;
no degree-sized sum, new numerical execution or fitted constant is used.

Developer freeze,2026-11-06: ../theory/C08-far-integral-bound.md now
contains the complete analytic K_delta<49/50 proof, SHA-256
445a449d83e3d575222b3832ad6adb3c401a21e2e89d1d2ced8e8b1dca860ead.
Its scalar dependency is C08-far-pole-functional.md, frozen SHA-256
6cb61ebc3f3808c61bc8d72feb2bee3a57c1dbecf597a7915833b4f43c8cda67.
The exact total upper97701/100000 is below49/50. The parent received a
distinct review request for the folded J sign, sine-log antiderivative
and cutoff accounting. No independent acceptance is claimed by the
developer. Combined with the separate endpoint bound this yields
C_far<3, leaving final model/corner/primitive assembly separately owned.
C06-far-compact-error.md retains its accepted SHA-256
64d88fd3bce387630cf55fcc559fb88cc15cf9f27e93487fc662f5050e8d4520.
