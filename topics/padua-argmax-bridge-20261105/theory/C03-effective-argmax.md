# PD-T?argmax-bridge-C03-effective-argmax — Improved effective global tail

ID kind: PD-T. Aliases: half-diamond near/far assembly; explicit global
boundary exp(10^7). Split from: the quantitative upper-bound continuation
of PD-T099. Split into: supporting inequalities retain their own files.

## Statement

Set N1=ceil(exp(10^7)). For every integer n>=N1, PD-T101's corrected
even-checkerboard Padua Lebesgue function has maximum Lambda_c(n),
attained exactly at {(-1,-1),(1,-1)} for even n and
{(-1,-1),(-1,1)} for odd n.

The remaining finite gap is41<=n<N1. This improves the separately proved
C01 boundary ceil(exp(10^12)); both are impractical. It does not certify
the intervening degrees, establish a practical campaign or settle the
all-degree PD-T099 target.

## Status, scope and dependencies

Status: PROVED analytic coordinator assembly; distinct supplementary
reconstruction requested before publication. Exact real arithmetic,
natural logarithms and exactly the inherited cardinal conventions.

This introduces no new mechanism or novelty claim: it substitutes the
accepted C02/C04 supporting bounds into C01's existing near/far assembly.
Accordingly no new idea-generation or historical-priority gate is claimed.

Dependencies, each at its exact quantified scope:

- C01-effective-global.md, including its written explicit component
  budget: S-aLambda_c<=512+20480H+8000H+16H<30000H,
  H=1+log(n+1), for n>=64 on the full closed phase diamond.
- C04-near-limit-comparison.md, current reviewed source3544d016...:
  the ACTUAL unchanged M_near<=Lambda_c+1/4096 for log n>=30,
  and N1-15's |S-M_near|<3/14000 for n>=10^6,rho<=1/2.
  This uses the actual finite-degree conclusion, not its limiting result.
- C01-allclass-defect.md: every admissible noncorner odd center has
  Delta>1/2048 for n>=64,rho<=1/2, all phase signs and both parities.
- C02-corner-halfdiamond.md: at both actual nonnode corners, inward
  0<rho<=1/2 gives lambda<Lambda_c if log n>=610000.
- PD-T157: Lambda_c>=(4/pi^2)log^2 n-54; PD-T215/364 exact
  odd-center physical cover and lambda=S-Delta; separate phase evenness
  of S; PD-T101/159's cardinal convention and equal corner values.

No ineffective localization, all-n3/4 energy hypothesis, assumed global
argmax, sampled maximum, runtime code or numerical fit is a premise.

## Proof

Put L=log n,m=n+1 and rho=|alpha|+|beta|. For L>=10^7,
PD-T157 and pi^2<10 give Lambda_c>=L^2/4. Also log m<=L+1.
The C01 budget and H<=2log m imply the useful explicit corollary

    S<=aLambda_c+60000log m, a=(cos alpha+cos beta)/2.       (1)

The physical odd-center cover puts every point of the angle square in
some admissible chart with rho<=pi. Endpoint phase signs are inward;
collisions and ties use the finite polynomial values as in PD-T364.

If rho>=1/2, separate absolute phases and the cosine product give

    a=cos(rho/2)cos((|alpha|-|beta|)/2)<=cos(1/4).

Both cosine factors are nonnegative on the fundamental diamond.
The alternating cosine estimate yields

    1-cos(1/4)>=1/32-1/6144=191/6144>3/100.

Thus (1) gives

    S-Lambda_c<=-3L^2/400+60000(L+1)<0.                    (2)

Indeed the positive opposite at L=10^7 equals149999940000, and its
derivative3L/200-60000 is positive for every L>=10^7. Therefore every
physical point represented by such a phase is strictly below Lambda_c.

For rho<=1/2 at a noncorner odd center, n>=N1 implies both n>=10^6
and log n>=30. The ACTUAL C04 comparison and N1-15 error, extended
by separate phase evenness, give

    S<Lambda_c+1/4096+3/14000.

The allclass defect then implies

    lambda=S-Delta
          <Lambda_c+1/4096+3/14000-1/2048
          =Lambda_c-107/3584000<Lambda_c.                (3)

For an actual nonnode-corner center with 0<rho<=1/2, the separate
C02 corner theorem applies since10^7>=610000. It gives strict
comparison directly, including arbitrarily small nonzero phases;
no positive constant error is substituted at the origin.

At phase0 in an actual corner chart, lambda=Lambda_c. There are
exactly the two stated nonnode corners, with equal values by the
parity-preserving reflection. All other points have been excluded by
(2), (3) or the corner theorem. This proves the maximum and exact
equality set. The shared rho=1/2 boundary satisfies both valid cases.

## Checks and remaining work

Pure finite-dependency assembly; no numerical execution is a premise.
Independent review must check in particular the stronger60000 coefficient
from the WRITTEN C01 budget, the actual rather than limiting C04 result,
the full allclass quantifier and direct punctured corner statement.

The boundary remains astronomical. Practical reduction of the finite
gap, a much sharper global threshold, cheap validated finite/degree-block
methods and formal Claude audit remain separate work. No Syvert release
or old-technology degree campaign follows from this result.

2026-11-06, Codex coordinator, requested gpt-6-astra high; serving
metadata unexposed. Original supporting proof bytes remain unchanged.
