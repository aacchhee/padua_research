# D03 joint finite-h: bounded perturbation lemma, reference still open

Rules/input `084a64f6465956f9c75b5538f83752c30318f151`.
2026-11-06, Codex mathematical developer; parent requested Sol xhigh,
serving metadata not independently exposed. Root owns Git and shared
records. This block owns only its new D03 idea, attempt and theory files.

## Gate and exact kernel inspected

The fresh gate is recorded in [candidate](../ideas/D03-joint-finite-h.md).
IDEAS headings/identifiers/alias columns, all obstruction tables and
the actual N1/D01/D02 shortlist were refreshed before proposing the
mechanism. Its direct predecessor is N1-03's equal-opposite *integral*
subtraction; this block instead bounds the BV of the difference of the
two *discrete cancellation functions*. No historical novelty is claimed.

Read the actual corrected ordinary kernel

    F=C cot((u-v)/2)+D cot((u+v)/2),
    C=(p-q-2a cot(v/2))/4, D=(p+q+2a cot(v/2))/4,

and N1-07's exact finite-h sinc chart, including its signed sine factors,
the n/(n+1) pole displacement, T(y)=y cot y and polynomial-compatible
collision limits. N1-09's special/central conventions and near-only
positive-numerator hypothesis were also read. No extension of that
near hypothesis or h-Taylor smoothness through moving zeros was assumed.

## Retained bounded result: PROVED developer lemma

[D03 cancellation perturbation](../theory/D03-cancellation-perturbation.md)
proves the following for the full closed phase diamond and both degree
parities, with exact N1-02 special rows retained. Put w=a cot(v/2)/2,
e=dist(v,pi*Z), P=sin|alpha|+sin|beta|, and subtract

    g0=g(-w,w,v;x)

from the actual cancellation g(C,D,v;x). Then

    sup|g-g0|<=P cot(e/2),
    Var_per(g-g0)<=28P cot(e/2)<=56P/e.

The exact difference of the corresponding ordinary-row quadrature errors
therefore sums to at most

    112P*H_n/(pi*n) <=56P*H_n/n.

There is no fixed-R floor or inverse-a factor. The first paper test
survives: a min-channel sandwich gives a uniform bounded difference,
and at most six sign arcs with at most one derivative zero each give
the explicit variation constant. Coefficient sign switches are covered
by separating |w|>P/4 and |w|<=P/4; absolute values are not differentiated
through a moving zero. All actual polynomial-collision rows and the two
central rows stay special. No weighted pole limit is discarded.

This is only a supporting lemma. The complete practical finite-n
S_n-M_infty target remains OPEN, rather than PARTIAL. In particular the
bound controls the actual cancellation error minus the symmetric
reference error; it does not bound that reference error itself.

## Decisive limitation of the simplest whole-kernel reference

A tempting stronger implementation would compare the whole ordinary
kernel to its symmetric A-channel counterpart, then bound their pole
norms independently. That is not valid on phase boxes crossing an actual
collision: the new unweighted reference can have a genuine pole where
the actual coefficient vanishes and the corrected polynomial is finite.

An exact illustrative instance uses n=4,m=5,beta=0,alpha=3pi/5,
r=2,j=1. The odd-board condition j+r=3 holds and

    u=(j*pi+alpha)/n=2pi/5=v=r*pi/m.

Let t=pi/5. Then p=sin(3pi/5)=sin(2t),
2a=1+cos(3pi/5)=1-cos(2t)=2sin^2 t, so

    C=[p-2a cot t]/4=0,
    w=a cot t/2=p/4>0.

The actual first pole factor uses its polynomial-compatible finite
limit, whereas -w cot((u-v)/2) in the unweighted reference is singular.
The same problem occurs approaching this collision, before declaring
the row special exactly on it. This is a scoped failure of the naive
whole-kernel comparison, not a negative result about bounded g0 or a
properly weighted joint reference. It is already consistent with the
N1 pole-product obstruction, so no new PD-N is allocated.

The proved difference lemma avoids this problem because g0 and g-g0
are bounded cancellation functions and collisions remain outside its
mesh theorem. It does not solve the remaining reference matching.

## Main reference obligation and next test

The symmetric cancellation has no moving numerator zeros; for a folded
endpoint its two nonzero pieces are precisely the fixed cotangent arcs
used in N1-03. Its exact mesh sum can be written with partial cotangent
sums. The remaining challenge is to join its finite-n error to the
actual endpoint polynomial rows and C08's E_infty *before* taking
absolute values. No complete compact finite-n identity or useful bound
for that joined expression was proved in this block.

Thus the next decisive analytical test is an exact weighted reference
telescope, with central/collision bookkeeping and its actual degree
domain. A bound that again leaves O(a/R), O(1/R^2), or independent R^2/n
losses does not pass the practical target. The present perturbation
lemma can be used after that identity, but cannot replace it.

A phase-relative subtraction S_n(phi)-S_n(0) is retained as a deferred
alternative, not developed or assumed. In particular phase changes
move sampled poles and special-row membership, so a smooth h- or phase-
Taylor premise is unavailable without further weighted cancellation.
No second near correction or replacement far model was introduced.

## Resources, verification and disposition

Parent's prospective cap was twenty analytical minutes for this first
block. No native/full-board/point/quadrature run, new floating measurement,
fit, Python numerical helper or compiled helper was executed. Tools were
used only to read/search files and write these records; analytical elapsed
time was not independently instrumented. The developer block stops here
for distinct review rather than proceeding to the harder reference proof.

Retain the standalone PROVED supporting lemma for independent review.
The main practical joint error and global threshold remain OPEN. The
naive unweighted whole-kernel subroute is abandoned for the exact pole
reason above, while the bounded symmetric cancellation route remains
retained with the explicit next test. No producer, degree certificate,
auxiliary-floor transfer or old-quantifier change follows.
