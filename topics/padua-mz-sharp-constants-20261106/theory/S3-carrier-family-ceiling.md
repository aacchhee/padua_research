# PD-T?mz-sharp-codex-S3-04 — a global ceiling for the inherited negative packet coefficients

ID kind: PD-T.
Aliases: normalized negative Fejer packet ceiling; scalar-family gap bound.
Split from: the quantitative inherited-carrier candidate S3-01.
Split into: none.

## Statement

Let A=4 log 2, h(x)=x^2 log|x| for x!=0 and h(0)=0, and

    C(q)=3h(q)-2h(q+1)-2h(q-1)+(h(q+2)+h(q-2))/2,
    J(a)=[A+C(1/a)]/2.

For every fixed a,b>0 with a+b<1/2, the exact normalized negative
packet coefficient of PD-T379 satisfies

    kappa_minus(a,b)=16ab/[9 A J(a)]
       < U_minus := 1/[9 A(16 log 2-9 log 3)] < 1/24.    (1)

In particular the supremum over this entire scalar parameter domain is
at most U_minus. This is a global family ceiling, not an assertion that
the ceiling is optimal or attained. It holds for the inherited negative
packets on either m parity, with exactly their PD-T379 normalization.

## Definitions, assumptions and scope

The family is precisely PD-N105/PD-T378's single negative carrier with
the product Fejer envelopes and fixed positive parameters a,b satisfying
a+b<1/2, whose continuous-normalized logarithmic coefficient is proved
in PD-T379. Continuous measure is unnormalized dxdy of mass four.
The carrier coordinate and mesh follow PD-T378 on odd m and PD-N105 on
even m. The limit m->infinity is taken at fixed interior parameters.

The result bounds those limiting trial coefficients, including their
scalar parameter closure. It does not bound the full Padua minimum,
linear combinations or changed envelopes, the positive packet family,
or any broader meaning of packet. It supplies no uniform asymptotic for
parameters depending on m; such a use would need an additional proof.

## Status by part

Overall status: **PROVED** (analytic development; separate check pending).

| Mathematical part | Status | Evidence |
|---|---|---|
| positive endpoint norm floor and global coefficient ceiling (1) | PROVED | monotonicity, exact logarithmic algebra and product bound below |

Candidate disposition: retained quantitative bound within the existing
S3-01/IDEA-469 scalar family. No new mechanism or priority claim.

## Gate basis and dependencies

The complete prospective gate is ../novelty-gate-S3.md. This bounded
followup reuses the existing candidate ../ideas/S3-carrier-variant.md
and its previously read full PD-N105/PD-T378/PD-T379 dependencies.
PD-T379 and S3-01's finite-difference proof were reread for this
followup. It generates no new model.

The exact coefficient formula is PD-T379. The monotonicity identity is
proved in S3-normalized-carrier-improvement.md and repeated below. No
finite optimizer, spectral fit, fixed-operator result or external source
is a premise.

## Proof

### 1. Monotonicity and the endpoint floor

For q>2, the centered fourth-difference identity gives

    C(q)=-integral_[0,1]^4
             (q-2+s1+s2+s3+s4)^(-2) ds,
    C'(q)=2 integral_[0,1]^4
             (q-2+s1+s2+s3+s4)^(-3) ds>0.

All arguments are positive for each fixed q>2, so differentiation under
the compact integral is justified. The explicit formula for C is
continuous at q=2, because h is continuous at zero. For q>2, choose
2<r<q. Monotonicity and the right endpoint limit give

    C(q)>C(r)>=C(2).

No differentiation at q=2 or integral exchange there is needed. Since
0<a<1/2 gives 1/a>2, it follows that

    J(a)>[A+C(2)]/2.

The exact endpoint algebra is

    h(2)=4 log 2, h(3)=9 log 3, h(1)=h(0)=0,
    h(4)=16 log 4=32 log 2,
    C(2)=28 log 2-18 log 3,
    [A+C(2)]/2=16 log 2-9 log 3
               =log(2^16/3^9)=:J_endpoint.              (2)

This number is positive: 2^16=65536>19683=3^9. The value in (2)
is the continuous scalar endpoint J(1/2), not a claim that boundary
parameters give admissible finite-degree packets.

### 2. Product bound and the ceiling

Because b<1/2-a,

    ab<a(1/2-a)=1/16-(a-1/4)^2<=1/16.

Consequently 16ab/9<1/9. Combining this with A>0 and the strict
positive floor J(a)>J_endpoint proves

    16ab/[9 A J(a)]<1/[9 A J_endpoint]=U_minus.

Taking the supremum over all fixed interior parameters preserves the
non-strict ceiling sup kappa_minus<=U_minus. No local optimizer is used.

For the elementary comparison in (1), note that
2^16=65536>59049=3^10, so J_endpoint>log 3. Strict convexity of 1/t
(or its tangent at the interval midpoint) gives

    log 2=integral_1^2 dt/t>2/3,
    log 3=integral_1^3 dt/t>1.

Thus A>8/3, J_endpoint>1 and 9 A J_endpoint>24, proving
U_minus<1/24. This also verifies positivity without decimal evaluation.

## Interpretation of the finite reported gap

Retuning a,b in this inherited negative family cannot produce an
asymptotic normalized trial coefficient of magnitude0.0915, since
0.0915=183/2000>1/24>U_minus. The number0.0915 is used here only as
the finite measured comparison supplied by the coordinator; its source
fits were not read and it is not identified with an asymptotic spectral
constant. The ceiling explains a limitation of that particular scalar
family, not the finite spectral branch or the full sharp slope.

The earlier raw coefficient bound1/9 omits the continuous denominator.
Equation(1) retains that denominator and is the relevant normalized
ceiling. It is deliberately coarse and proves no global family optimum.

## Checks and sources

No numerical command or new fit was run for this followup. The proof
is exact scalar algebra and the inherited monotonicity identity.
Supplementary independent check requested on the frozen file; required
Claude audit remains separate. No external source or priority claim.

## Open items and history

An optimal coefficient within the inherited scalar family is not proved.
No alteration is made to the fixed-operator theorem, PD-T381's shared
status, or the final-fit records.

2026-11-06; one bounded explanatory followup, S3 round4. Codex developer,
allocated gpt-6.1-sol xhigh; runtime metadata unexposed. Source/rules
2143ad622fa98faf8fe7d5cb8ed2bb7e0062f861. Original gate and S3-01
candidate retained; no new mechanism and no numerical exploration.


## 2026-11-06 audit completion pointer

The earlier requests for independent/Claude review describe the development
boundary. Claude audit-01.md now accepts this analytic proof at its stated
scope. That completed audit supersedes earlier pending-review metadata; it
does not certify floating decimal values or approve this response.
