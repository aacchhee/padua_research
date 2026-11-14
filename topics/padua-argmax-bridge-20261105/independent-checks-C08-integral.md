# Independent supplementary review — C08 renormalized integral

2026-11-06. Reviewer: distinct Codex `/root/c06_far_review`, parent-assigned
Astra high; runtime serving identity and effective effort are not independently
exposed. Rules were read at
`b6e67b3c78cb668b6d2f9da5a5560537d2960bf3` and reread in this continuation;
the coordinator records unchanged rules after the main reconciliation at
`547a473a6e1c1268ff4f1ada7243b12afb02d0bc`. Only this report was written.
No author source, earlier report, shared file or Git state was edited.

## Disposition and scope

**Accepted at its stated full-triangle integral scope after one MINOR
strictness wording correction. No unresolved mathematical finding.**

The exact C06 renormalized integral at delta=1/100 satisfies
K_delta<49/50 on alpha,beta>=0, alpha+beta<=pi, including a=0, vertices,
axes and pole-offset cusps. Other quadrants use the inherited separate
phase evenness. The originally proposed stronger K_delta<=1/2 remains
**OPEN**. The full model maximum and actual far/global argmax conclusions
are separate obligations and are not promoted by this report. Formal Claude
audit remains separate.

Initial frozen source `theory/C08-far-integral-bound.md`:
`445a449d83e3d575222b3832ad6adb3c401a21e2e89d1d2ced8e8b1dca860ead`.
Accepted source after the focused correction:
`e76a45698ab5c0f2af53816fb74487fb929eff99011e8004e9f79e3f84f8f7a5`.

The scalar premise `theory/C08-far-pole-functional.md` remains frozen at
`6cb61ebc3f3808c61bc8d72feb2bee3a57c1dbecf597a7915833b4f43c8cda67`.
Its separate review by `/root/c01_near_review` accepted H<749/1500<1/2,
the signed cutoff bound and the exact two-channel interface with no finding:
`independent-checks-C08-pole.md`, SHA-256
`d1d9fea50b982112251ec5b5fd7284264d897f56ae87c1d03d9457f760bc0375`.
That report was read before this disposition; the premise is no longer awaiting
distinct review. This report checks its use in the integral theorem rather than
counting the developer as its own approver.

## Reading and verification boundary

Read the complete new integral source, idea and attempt, the scalar-functional
source and its independent report, and the C08 weighted-coefficient proof's
local cotangent-partial-fraction argument. The exact C06 model contract and
generic full-range J formulas were already reconstructed in this reviewer's
`independent-checks-C06-compact.md`; its predecessor normalization, endpoint
conventions and full b_full integral were reconstructed in
`independent-checks-C06-far.md`. They remain unchanged premises here.
The accepted endpoint and extra-corner-margin review dispositions were inspected
for the stated use boundary, not relabeled as a new audit of those sources.

This is mathematical correctness review of the specified quantitative
continuation. Historical novelty, priority and exhaustive author-gate coverage
are excluded; the workflow's no-novelty exception applies. The new idea and
attempt preserve the stronger unsuccessful targets and the reason that the
separate additional corner margin permits the weaker integral budget. No second
near-model correction is introduced or assumed.

## Finding and focused closure

**I1 — MINOR, closed.** The original source's section3, line146, stated

    (2log2/pi)p < 9p/20

throughout the closed triangle. At p=0 both sides equal zero. The scalar
coefficient inequality is strict, but multiplication by a zero coefficient
does not preserve strictness. This was returned to the coordinator before
any author change, with the requested non-strict inequality and an explicit
note that the final theorem's strictness is supplied independently by the
cutoff slack.

The author changed only this '<' to '<=' in the theorem. An executed byte
comparison reversed that one added '=' byte and recovered the original
frozen SHA-256 exactly. Thus there was no other theorem change. The author
also changed the attempt's informal 'less than .45sin(alpha)' to 'at most'
and its upper-envelope '<.95' to '<=.95'; equality of that envelope can
occur at a=0,p=1. These clarifications leave every theorem constant, scope,
definition and substantive estimate unchanged. The original finding and
source identity are preserved here. No author file was repaired by the reviewer.

## Exact renormalization and pole-functional interface

Write l=log delta and b=log pi. Since D0=U0/pi+B0 b,

    B0(l-b)^2+2D0(l-b)
      =B0(l^2-b^2)+(2U0/pi)(l-b).

With B=V+I/pi, the source's K_V and K_I therefore have exactly the
normalizations 1/pi and 1/pi^2. This is a decomposition into finite
cutoff combinations; no individually divergent endpoint integral is bounded.

For f(x)=Phi_0(1/2+x/(2pi)), the numerator of V is
c_e f(d+v)+c_d f(e-v), with U0=c_e f(d)+c_d f(e). In the second
channel substitute v -> 2pi-v and use f's periodicity. This gives exactly

    K_V=c_e H_delta(d)+c_d H_delta(e),

including the subtraction 2f(x)log(delta/pi)/pi in each scalar functional.
There is no lost factor of two or shifted cutoff. The scalar lemma uses the
same continuous Phi_0 at integer offsets and accounts for its negative
derivative atoms. On the entire closed triangle c_e,c_d lie in [0,1].

Using the separately accepted H<1/2 and finite-cutoff allowance, together
with c_e+c_d<=1+c_e c_d=1+a, gives

    K_V<(1+a)/2+27/1000.

Indeed the two-channel cutoff is less than
(24/9)(1/100+1/48000000)<27/1000. Nonnegative weights preserve the upper
inequality; if both weights vanish, K_V=0 still satisfies the final strict
bound. No division by a weight or inverse phase distance is used.

## Full folded cancellation upper and signs

The source has T=2a cot(z/2)>=0 on 0<z<pi. Its left coefficients are
(p-q-T)/4 and (p+q+T)/4, so the generic parameters are
u=p/2 and s_L=(q+T)/2. On the right the sign of T reverses;
channel exchange gives s_R=|q-T|/2. Cotangent periodicity and reflection
reduce the separation to epsilon=min(z,pi-z), with sin epsilon=sin z.
These are invariances of the cancellation integral; no n/(n+1) mesh exchange
is made.

The generic identity is J=2(s-u)_+ log(sin epsilon)+R. Its same-sign
entropy branch has R<=0 because both fractions c/u and b/u lie in [0,1].
For s>u, the already proved derivative R_epsilon is nonnegative and
R(u,s,pi/2)=0, so R<=0 at smaller separation. The no-root branch is
included by the positive-part square root; zero parameters follow by the
continuous generic limit.

Thus the sum of the two folded integrals is bounded above by

    [(q+T-p)_++(|q-T|-p)_+] log(sin z).

The bracket is at least q+T-p+|q-T|-p=2max(q,T)-2p>=2T-2p.
Because log(sin z)<=0, multiplication reverses this inequality, yielding

    I_L+I_R <=4a cot(z/2)log(sin z)+2p|log(sin z)|.

This sign reversal is essential and is correct in the source. It remains valid
when 2T-2p is negative (the resulting upper is merely loose), when a=0,
or when p and q change their ordering. At z=pi/2 the logarithm is zero
and the generic entropy still gives a nonpositive left side. At z=pi the
upper and the inherited exact central logarithm are integrable. Hence the
inequality can be integrated over delta<z<pi with no discarded singularity.

## Sine-log antiderivative and finite cutoff

The absolute log-sine integral on (0,pi) is pi log2, by reflection and the
double-angle identity. It bounds the second term above by
(2log2/pi)p<=9p/20. The coefficient bound is strict, since
2(7/10)/(25/8)=56/125<9/20; the corrected non-strict product handles p=0.

Let y=sin^2(z/2). From the positive power series,
Li2'(y)=-log(1-y)/y on 0<y<1. Differentiating the source's primitive gives

    d/dz [4a log^2(2sin(z/2))-4a log^2 2-2a Li2(sin^2(z/2))]
      =4a cot(z/2)[log(2sin(z/2))+log(cos(z/2))]
      =4a cot(z/2)log(sin z).

The reciprocal-square value is inherited analytically: the local cotangent
partial fraction gives sum over odd l of l^-2=pi^2/8 by differentiation
at zero, justified by uniform convergence near zero. If Z=sum k^-2,
then Z=pi^2/8+Z/4, so Li2(1)=Z=pi^2/6. Thus the primitive at z=pi
is exactly -a*pi^2/3, with no numerical special-function evaluation.

Combining the lower cutoff with B0(l^2-log^2 pi) gives precisely

    -c*a+(a/pi^2){4[log^2 delta-log^2(2sin(delta/2))]+2Li2(y)},
    c=1/3+(4/pi^2)(log^2 pi-log^2 2),
    y=sin^2(delta/2).

Because 0<2sin(delta/2)<delta<1, the square-log difference is negative;
discarding it is favorable for an upper bound. The remaining term is at most
(2/pi^2)y/(1-y), using 0<=a<=1 and Li2(y)<=sum y^k. With y<=1/40000
and pi^2>9 this is strictly below 2/(9*39999)<1/100000. This charge is
separate from the scalar H cutoff and is included exactly once.

The elementary lower bounds give

    c>1/3+(2/5)[(11/10)^2-(7/10)^2]=233/375>1/2.

The difference of squares is positive, so replacing 4/pi^2 by 2/5 has
the correct direction. Consequently the source's strict bound
K_I<-c*a+9p/20+1/100000 holds also at p=0 or a=0: the unused positive
cutoff allowance supplies strictness independently of the product estimate.

## Final budget and use boundary

Adding the two finite combinations gives

    K_delta<1/2+(1/2-c)a+9p/20+27/1000+1/100000.

Since c>1/2 and a>=0, its a term is favorable. With p<=1 the remaining
upper is 97701/100000<49/50. This is uniform on the entire closed triangle;
continuous f and finite combined products handle cusps and vertices without
evaluating an unweighted divergent C series.

The stated arithmetic consequence with the separately accepted endpoint
constant is also correct:

    49/25+1/3000+49/50=8821/3000<3.

This does not itself prove the separately owned full model comparison, which
also needs the weighted logarithmic coefficient, finite corner lower and
actual-primitive approximation. Neither the stronger K_delta<=1/2 target
nor the exploratory scalar shape bound is inferred.

## Executed checks

An inline `python -` command in `/workspace/padua_research`, Python 3.12.14
with standard-library `fractions.Fraction`, checked eight rational predicates:
both cutoff allowances, the p coefficient, the exact c lower bound and its
comparison with 1/2, the final budget identity and inequality, and the
conditional endpoint-plus-integral sum. All passed, exit0, process CPU
0.000073199 seconds. There was no random seed or numerical quadrature.
These controls supplement the displayed exact arithmetic, not a finite-grid
proof of the continuum statement.

A separate standard-library byte/hash check confirmed the one-byte author
correction by exact recovery of the original theorem hash. Source reads and
hashes also confirmed the frozen scalar premise. No diagnostic integral,
phase sample, fitted constant or mathematical floating computation was run.
The MINOR finding is closed; all stated algebra, signs, normalizations and
cutoff constants are accepted at the declared scope.
