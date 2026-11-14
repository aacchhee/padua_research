# Supplementary independent review: N5 round5 specified-certificate obstruction

2026-11-06. Reviewer: distinct Codex agent `/root/review_phase_round4`;
model/effort inherited, serving metadata unexposed. Rules/input commit:
`fc8c2885f47b08cecc7f65328db0e740cbc205ea`. This supplements, and does
not replace, the required Claude audit. No producer files, old reviews,
shared records or Git were changed by this review.

## Verdict and frozen scope

**ACCEPTED at the stated mathematical scope. No blocking finding.**
For exactly the phase-blind envelope F_n defined in equations (6)-(7)
of [N5-large-budget.md](theory/N5-large-budget.md), the admissible
sequence n=4t+1>=65, J=0, q=(n+1)/2, alpha=beta=0 satisfies

    lim F_n < 487302379/1968469140 < 1/4.

Its uniform quarter-floor certificate therefore fails. This proves
neither Q_v<1/4 anywhere nor the failure of a quarter floor for the
actual deficit S-lambda. The original full projected target Q_v>=1/4
on the unchanged N5-04 domain stays **OPEN**. No effective onset for
F_n<1/4 is supplied or required. No N1 correction is spent and no new
N5 continuation is proposed.

Frozen reviewed inputs, SHA256:

| File | SHA256 |
|---|---|
| theory/N5-large-budget.md | `0e86fe06ccf8845c5fa6e5715e7e35618775573c00bca69a7e9660ee02c76247` |
| code/n5_large_budget.py | `c7840ec6cfc801cbc353bf9f67d3831b9207b4b8d9d7da93009552b2f4bf8056` |
| evidence/n5-large-budget.json | `fc7582ff0375c0f55779aeb026f42a81228bb6c9dc479642f3d791fe64342c1e` |

All three identities were actually recomputed and checked. The theory,
developer code, receipt, round5 candidate and canonical attempt were
read; the mathematical argument below was reconstructed independently.

## Projection, admissibility and envelope

The load-bearing N5-04 identities were already examined in
[the distinct two-phase review](independent-checks-n5-two-phase.md),
including T222, T366, N5-03 and the earlier all-edge review. No
measurement supplies these identities. In the periodic projection,
s=q+k has parity r+k=J mod 2 because J+q is odd. Folding the two s
partners gives a factor two, with endpoint half weights. Multiplying
G by (-1)^r/2 gives H, so d(G,G')=2d(H,H'). These two factors turn
1/(4N) into the displayed 1/N, with r still ranging over 2n indices.
The exceptional term in H is -cos(alpha)/2; replacing it by -1/2
would be wrong off the zero phase. Beta is unchanged under the index
reflection. These features are retained in the reviewed definitions.

On |alpha|+|beta|<=1/2, cos t>=1-t²/2 gives a>=15/16; the total
absolute sine perturbation is <=1/4. Since 1+y>=0,
A>=a0(1+y)-1/4=a0(c+y), where c=11/15. For interior phi and
0<b<pi, y_--y_+=2sin(phi)sin(b)>0. On the specified support,
both numerator lower bounds are positive and the denominators have
opposite signs. Thus d=2min(|H_+|,|H_-|)>=ell. Elsewhere ell=0
is safe, including collisions where the underlying kernel retains
its finite polynomial value. This establishes F_n<=Q_v without an
incorrect converse.

For n=4t+1, m=4t+2 and q=2t+1 are admissible; q is odd and
strictly interior. J=0 and alpha=beta=0 obey the inward constraint.
Hence a single eventual obstruction on this subsequence disproves
the proposed uniform bound for this certificate on the full domain.
It is unnecessary to treat J=n or every parity to disprove that
uniform certificate, and no failure is asserted for every parameter.

## Central integral and parity limit

At phi=pi/2 put s=sin b. The envelope is nonzero only for
0<s<c and -s<x<s, and its two positive fractions are
(c-s)/(x+s) and (c+s)/(s-x). The second increases with x and
the first decreases. Their intersection is x_*=-s²/c, lying
strictly inside the interval, with common value c/s. Integrating
the increasing fraction first and the decreasing fraction second
gives exactly

    integral ell dx = 2a0 f(s),
    f(s)=(c+s)log(2c/(c+s))+(c-s)log(2c/(c-s)).

The extension f(c)=0 follows from t log t ->0. This also confirms
nonnegativity of f without relying on a numerical logarithm.

On each fixed eta<=b<=pi-eta the envelope is bounded by
2a0c/sin b. The support boundaries x=+/-sin b and sin b=c form
a set of area zero. Values assigned on these boundaries therefore
do not obstruct Riemann integrability. The even-even and odd-odd
lattices each have area spacing 4pi²/(nm); division by N gives
density 1/(4pi²) per lattice. Their sum gives 1/(2pi²), on
u in [0,2pi), b in [0,pi]. Endpoint half weights have no effect
because those envelope rows vanish.

The unbounded b endpoints require the separate estimate in the
theory; bounded-rectangle convergence alone would be insufficient.
For 0<b<=eta<=pi/2, |cos u|<sin b is the union of two intervals
of length 2b each. A parity grid of spacing 2pi/n contains at
most 2nb/pi+2 points there. Multiplying by a0c*pi/b and then
dividing by nm gives, at b=k*pi/m,

    2a0c/m + 2a0c/(nk).

Summation gives exactly the stated 2a0c*K/m+(2a0c/n)H_K.
This is <=2a0c*eta/pi+(2a0c/n)(1+log m). The opposite endpoint
has the same estimate; empty tails are harmless. The analogous
integral tail is O(eta). Taking n to infinity first and eta to
zero second justifies the improper integral limit. No unproved
uniform convergence rate or unbounded Riemann interchange is used.

Cosine symmetry now gives F_inf=(1/pi²) integral_b integral_(0,pi)
ell du db. Substitution x=cos u bounds its Jacobian by
1/sqrt(1-s²) on the support; the two b ranges supply another
factor two. Substituting s=sin b therefore yields precisely

    F_inf <= (4a0/pi²) integral_0^c f(s)/(1-s²) ds.

The comparison integral is an upper bound, not an identity for
F_inf. The developer's scratch value about .23782 refers to that
comparison integral, consistently with the theory's qualification.

## Entropy and strict rational estimates

Differentiating the entropy expression yields
log((1+z)/(1-z)); its positive power series can be integrated
term by term for z<1. Continuity and positivity extend the identity
to z=1. Keeping its first two nonnegative terms gives
f(s)<=2c log2-s²/c-s⁴/(6c³). Direct polynomial division gives

    I <= (2c log2-1/c-1/(6c³))*atanh(c)
                  +1+1/(6c²)+1/18.

The log2 upper series uses 1/(2j+1)<=1/7 in the remaining
positive tail starting with z^7, z=1/3; later terms make its
inequality strict. The first five positive terms of atanh(c)
give a strict lower bound. For Machin's identity, doubling the
tangent of atan(1/5) twice and subtracting atan(1/239) gives
tangent 1; its angle lies in (0,pi/2), fixing the branch pi/4.
The alternating arctangent bounds consequently give the claimed
strict pi lower bound. These are analytic arguments, not inferred
from floating evaluations.

The independent exact arithmetic verifies:

    log2 < 23581/34020 < 347/500,
    atanh(c) > 2253160124237/2421931640625 > 93/100,
    pi > 281476/89625 > 157/50.

After replacing log2, the coefficient is
-1917599/2495625<0; using the lower bound for atanh(c) thus
raises the upper estimate. The resulting positive bracket is
487302379/748687500. Positivity permits replacing pi by its
lower bound in the denominator, giving the strict bound stated
in the verdict. Its gap from one quarter is exactly
2407453/984234570>0. At least one strict series bound survives
through positive multiplication, so strictness is justified.

Convergence to a number strictly below 1/4 implies F_n<1/4
eventually along the admissible subsequence. This is an existential
onset statement, sufficient for the specified obstruction and not
an effective finite threshold.

## Executed independent check and limitations

Actually executed from the repository root:

```sh
python topics/padua-argmax-bridge-20261105/code/review_n5_large_budget.py
```

Exit 0, PASS, Python 3.12.14. This independently authored standard
library Fraction check imports no producer code. It checks the
three input hashes, Machin's tangent identity, exact series rational
values and comparisons, integrated polynomial division, coefficient
sign, positive bracket, final upper fraction and strict quarter gap.
It does not purport to mechanize the analytic convergence proof.
No floating case, phase job or whole-certificate replay was run by
this reviewer; repeating the developer's 72 unchanged diagnostics
would not establish the missing uniform inequality.

New review artifacts:

- [code/review_n5_large_budget.py](code/review_n5_large_budget.py), SHA256
  `12e67b29fe4712677ae95bac4d1e36bf0850c208494e6979336700b5517d75d2`.
- [evidence/n5-large-budget-review.json](evidence/n5-large-budget-review.json), SHA256
  `d9d0c6a1a4f9ba731e8397eeb23485cdcfd41f13cc2cbe5ec46efbc4a479f96b`.

The developer's 72 direct full-Q cases, reported minimum
0.5230485747479166311 and precision comparisons remain attributed
MEASURED evidence. They are neither independently rerun here nor
proof premises. No actual-Q counterexample is alleged.

## Gate and stopping scope

The full 1031-line state/IDEAS.md was read for this negative-result
review, SHA256 `0e1813b1f53e6aa4a970f19b86ebb3864dd6546b7f55c0bc2ffc4033320825f7`.
The retained projection/finite-defect mechanisms in IDEA327/328,
the broader ordering and corner routes IDEA318/330, the limiting
integral variants IDEA356/357, and the unresolved profile IDEA459
are consistent with the candidate's quantitative-variant scope.
No external novelty or exhaustive literature-priority claim is made.
The prospective round5 use of previously completed registry reading
is recorded in ideas/N5-round5-budget.md and attempts/N5.md. This
does not erase the canonical round4 timing qualification. Current
review reading likewise does not retroactively establish any earlier
prospective gate.

The sole frozen certificate is **REJECTED: failed** at its intended
quarter floor; the full-Q candidate remains deferred with its exact
target OPEN. This review freezes at acceptance of that separation.
No source repair, replacement certificate, new experiment or further
N5 development is authorized or performed here.
