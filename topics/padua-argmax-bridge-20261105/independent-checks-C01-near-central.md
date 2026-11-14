# Independent supplementary review — C01 central cancellation upper bound

Reviewer: distinct Codex `/root/c01_near_review`, parent-assigned Astra high;
serving identity and effective effort are not independently exposed.
Date: 2026-11-06. Rules and input HEAD:
`4b728b04216a5490910780bc609a82b853058426`, branch
`codex/padua-argmax-bridge-20261105`. Main/base supplied by the coordinator:
`f654e32daff27b6846849311092f6daebbbf235b`.

**Disposition: accepted at the stated supporting-component scope, with no
mathematical finding.** This is a separate supplementary check, not the
required Claude formal audit. The complete continuous Q_n comparison, C1
and any argmax onset remain OPEN.

## Frozen input and scope

The reviewed new file is `theory/C01-near-central-upper.md`, SHA-256
`ef5b3b62e5c079889525f291b4874bb6aff8b1033ef790de67aa62f62ee361b7`.
It was read in full and its hash checked before and after reconstruction.
The accepted claims are its directional estimate (1), radial estimate (2),
and whole-central-integral increment estimate (3), for alpha,beta>=0 and
alpha+beta<=1/2, including the axes and origin.

Read AGENTS/WORKFLOW/CODEX, handoffs 06 and 05, the topic LOG, and the
C01-near idea/attempt. Mathematical dependencies inspected include the
N1-02 half-kernel cancellation definition, full N1-05 normalization,
full N1-14 central formulas, N1-15 retained-cell/model definitions, full
N1-16 coefficient proof, full N1-18/19 and their independent round-8
review, and the C1 criterion. Relevant frozen dependency hashes are:

| Dependency | SHA-256 |
|---|---|
| N1-14 | `9a3f4d3f123ce82be5199a7631c8ead317ed15415b29dee44d126ead8bbbceb1` |
| N1-16 | `e7a7d4464e787df527aa6f155d223ae504a9be8f79221089ee43303c5b8d21e8` |
| N1-18 | `efa3fa15f17fd7f355a139616ebb951665703060095252cd1d988e7cd9ca8976` |
| N1-19 | `77ac04295f571dfce13b2793bc3164182072954977f0c595ba4f595c8cfb8cf0` |

This is a pure analytic validity review. Historical novelty, priority,
the author's search chronology and a new mechanism classification are
excluded; the workflow's no-novelty review exception applies. No full
state/IDEAS audit is claimed. No mathematical program, numerical integral,
fit, diagnostic or certified-cover replay was run. Shell operations were
read-only source/rule reads, searches and hashes; only this new report
was written. No author proof, old review, shared file or Git state was edited.

## Normalization and connection to the model

N1-02 uses C=(p-q-2a cot(v/2))/4 and
D=(p+q+2a cot(v/2))/4, so C+D=p/2=u. At v=pi-epsilon,
the coefficient difference is q/2+a tan(epsilon/2)=sL. At
v=pi+epsilon it is q/2-a tan(epsilon/2); exchanging coefficients
when necessary gives its absolute value sR. Separation reflection and
cotangent periodicity give exactly J(u,sL,epsilon) and J(u,sR,epsilon).
There is no extra factor two from the folding or from the half-kernel.

N1-05 places I/pi inside H; N1-15 integrates H with another factor
1/pi. The new Ic therefore has the correct pi^-2 normalization. Its
epsilon range corresponds precisely to the two whole central halves
pi/2<=z<=pi. At zero phase, u=q=0,a=1 and J=2tan(epsilon/2)log(sin
epsilon), so the stated baseline Ic(0,0) has integrand
4tan(epsilon/2)log(sin epsilon)/pi².

N1-18's Q_n uses the retained outer cells, exact permanent central rows,
endpoint/strip/jump pieces and signed seam corrections, after removing
the stated artifacts. Consequently Ic-Ic(0,0) is not by itself that
function's central finite-degree increment. The author explicitly retains
this distinction and the missing central-cell/row estimate. The new lemma
does not spend N1-16's full coefficient loss or imply Q_n-G_n<=1/40000.

## Positive majorant and degenerate regimes

For fixed u,s, let E=J-2s log(sin epsilon). In the opposite-sign regime
s>u, N1-14 writes J=2(s-u)log(sin epsilon)+R and gives
R_epsilon=2[u cos epsilon-D]/sin epsilon, where
D=sqrt((u²-s²sin²epsilon)_+). Subtraction gives
E_epsilon=-2D/sin epsilon exactly. Above arcsin(u/s), the no-root
formula gives E=0. Integrating back therefore gives E=H with the
author's positive integral. At the threshold the square root vanishes,
so the two expressions join without an uncharged moving-root term.

For s<u, the entropy formula has both coefficient fractions in [0,1],
so J<=0. Also u²-s²sin²t>=s²cos²t and cos t>=0 on the integration
interval. Hence H>=-2s log(sin epsilon)>=E. At s=u, J=0 and
H=-2u log(sin epsilon), giving equality. For u=0 the no-root formula
gives J=2s log(sin epsilon), including s=0 by its zero convention;
there is no division by u in this case.

The integrand defining H is nonnegative and decreases with s; increasing
the lower limit decreases H as well. For all permitted parameters,
H<=2u log(cot(epsilon/2))<=2u log(2/epsilon). Together with N1-14's
bounded R and bounded u,s this supplies a phase-uniform integrable
constant times 1+|log epsilon| for J,E and H near zero. It justifies
the improper integrals and passage through q=p, either zero phase,
root collisions and the double origin. At alpha=0, E=0 for each
branch and E_c<=0 directly; the positive beta allowance is harmless.
At the origin E_c=0 exactly.

## Right-pole translation and cancellation sign

Taylor's cosine bound gives a>=1-r²/4>=15/16. For
b=2arctan(q/(2a)), cos alpha<=1 gives b>=beta and arctan x<=x
gives b<=16beta/15. Thus 0<=b<pi/2.

For epsilon>=b, tangent subtraction gives
tan(epsilon/2)-tan(b/2)
=tan((epsilon-b)/2)[1+tan(epsilon/2)tan(b/2)], so sR is at least
a tan((epsilon-b)/2). Decreasing both its s argument and its lower
integration limit increases H, proving (6). Translation leaves an
interval [0,pi/2-b], whose positive H integral can be enlarged to
[0,pi/2]. The logarithmic singularity at the translated zero endpoint
is integrable.

Below b, sR=q/2-s0, so 2sR<=q. The original cancellation integrand
is |X+Y|-|X|-|Y|<=0, hence J<=0 in every coefficient regime and
E<=-q log(sin epsilon) there. Finally

    J_L+J_R-4s0 log(sin epsilon)
      =E_L+E_R+2(sL+sR-2s0)log(sin epsilon)
      <=E_L+E_R.

The sign is essential and is correct. In particular the pole translation
costs the one beta entropy term in (7), with no linear beta contribution
and no additional fractional-width factor.

## Fractional constant and entropy bounds

For alpha>0, tau=u/a and theta=2arctan tau obey
alpha<=theta<=16alpha/15, tau<=8alpha/15<=4/15, and
a tau^(3/2)<=2alpha^(3/2)/sqrt(30). These follow from
cos beta<=1, sin alpha<=alpha and a>=15/16. Also
2theta<=16/15<pi/2. On (0,2theta), integrating
2u log(2/epsilon) gives exactly
4u theta[1+log(1/theta)], bounded by
(32/15)alpha²[1+log(1/alpha)]. Both logarithmic factors used in
that comparison are positive.

For epsilon>=2theta, lambda=u/[a tan(epsilon/2)]<=
tau/tan theta=(1-tau²)/2<=1/2. If s sin epsilon>=u, H=0.
Otherwise y=sin t and z=y/lambda give the integral (10), with
the factor 1/sqrt(1-lambda²z²)<=2/sqrt(3). The further substitution
x=(1-cos epsilon)/tau has precisely
d epsilon=sqrt(tau)dx/[sqrt(x)sqrt(2-tau x)]. Extending the positive
x-domain to (0,1) is valid even when its original domain is empty.

Tonelli and z=y² give integral_0^1 h(x)/sqrt(x)dx=4I4.
The elementary inequality sqrt(1-v)<=1-v/2 gives I4<9/10;
the inequality is strict on positive measure. Combining all factors,
including 2/pi² from (7), yields

    fractional coefficient <=64I4/[pi²sqrt(156)]
                           <1200/2561<15/32.

Here pi²>197/20 and sqrt(156)>312/25 produce exactly 1200/2561;
the last comparison is 38400<38415. The square-root lower bound
follows by squaring; standard rational pi bounds suffice. No decimal
quadrature or fitted estimate enters. The small-epsilon coefficient
is below 4/9 since pi²>48/5.

For beta>0 the sine chord gives the integral in (13) bounded by
qb[1+log(pi/(2b))]. Using q<=beta, b<=16beta/15 and b>=beta
is legitimate because the bracket is positive; log(pi/2)<1/2 then
gives (16/15)beta²[3/2+log(1/beta)]. Division by pi² gives 1/9.
The zero-beta value is its continuous limit.

For rho>0, writing t=x/rho gives t log(1/t)<=1/e and hence
sum x²log(rho/x)<=rho²/e<3r²/4. The directional quadratic part
is at most (4/9)r², and both entropy coefficients are at most 4/9.
This produces 7r²/9+(4/9)r²log(1/rho), with the zero-origin
convention valid. Finally tan(epsilon/2)<=epsilon and the sine
chord give -Ic(0,0)<=1/4. Since 1-a<=r²/4,

    Ic(alpha,beta)-Ic(0,0)=E_c+(a-1)Ic(0,0)
                        <=E_c+r²/16.

The signs and exact arithmetic 7/9+1/16=121/144<1 and 4/9<1/2
prove the claimed whole-integral estimate (3).

## Findings and remaining obligations

No BLOCKING, MAJOR or MINOR mathematical finding in this frozen component.
No author repair was made or required before this acceptance. The claimed
PROVED status is supported for the specified whole central integrals only.
Finite central cells/rows and all other Q_n components still require their
combined phase bound. The coefficient gaps, jump envelope and this lemma
do not alone close C1, provide an argmax onset or establish a global result.
Formal Claude audit remains pending.
