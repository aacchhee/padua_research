# PD-T?argmax-bridge-C06-far-comparison — Uniform far exclusion at log n>=256

ID kind: PD-T.
Aliases: explicit half-diamond-complement exclusion; full far-phase onset.
Split from: the full effective global argmax assembly, which is separate.
Split into: none.

## Statement

For every integer n>=ceil(exp(256)) and every real phase pair satisfying

    1/2<=|alpha|+|beta|<=pi,

PD-T216's corrected primitive obeys

    S_n(alpha,beta)<Lambda_c(n).                              (1)

More precisely, with L=log n,

    Lambda_c(n)-S_n(alpha,beta)
       >191L^2/15360-22L/15-200>=3592/15.                     (2)

This covers the entire closed far diamond, including a=0, vertices,
central and endpoint polynomial collisions, and both degree parities.
The practical target n>=10^6 remains OPEN. This is an explicit first
alternative onset, substantially below the old log n=10^7 far bound;
it is still astronomically large in degree. No global argmax theorem
or finite-degree extension follows without the other phase/center cases.

## Definitions, assumptions and status

S_n,a and the exceptional (n,0) coefficient are exactly as in
[C06-far-full-profile.md](C06-far-full-profile.md). Lambda_c=S_n(0,0)
is the nonnode-corner value. Exact real arithmetic; no mesh swap, fit,
finite-energy extrapolation or numerical scan.

Overall status: **PROVED**, analytic application below; separate
independent supplementary review and formal Claude audit remain required
before parent publication. The broader n>=10^6 far target stays OPEN.

## Depends on

PD-T?argmax-bridge-C06-far-profile, equations(2)--(3), valid n>=10^6;
PD-T271's corner expansion and explicit error; N1-16's elementary
normalization k=gamma+log(8/pi)>3/2, so b_c=8k/pi^2>6/5.
Only that scalar corner normalization is inherited from N1-16, not a
near formula transferred outside its domain.

## Proof

PD-T271 has, with N=n+1/2,

    Lambda_c=(4/pi^2)log^2 N+b_c log N+c+R_n,
    c>1,
    |R_n|<=604 n^(-1/5)+[(L+2)^2+1]/(n+1)
             +A_n/(2n^2)+1/(16n^4)+(log N+2)/n,
    A_n<=L+2.

For L>=256 the displayed error is less than1. For example, use e>2
and monotonicity of (L+c)^j exp(-bL) on this range. The first term is
less than604/2^50<1/10; each other displayed term is also below1/10
at L=256 and decreases afterward, using log N<L+1. Thus c+R_n>0.
Since log N>L and b_c>6/5,

    Lambda_c>(4/pi^2)L^2+(6/5)L.                              (3)

Put rho=|alpha|+|beta|. The full-diamond identity gives

    a=cos(rho/2)cos((|alpha|-|beta|)/2)<=cos(1/4).

Taylor's alternating bound at1/4 therefore yields

    1-a>=1-cos(1/4)>=1/32-1/6144=191/6144.

Since4/pi^2>2/5, the loss of the quadratic coefficient is strictly
greater than191/15360. Subtract C06-far-profile(2), use b_full<8/3,
and combine with (3). This proves the first inequality in (2).
The polynomial191L^2/15360-22L/15-200 is increasing for L>=256,
and at256 its exact value is3592/15>0. This proves (1)--(2).
Separate phase evenness is the only phase symmetry used. QED.

## Checks and scope

No computation is a proof premise. The comparison is independent of
all-class projected-defect and actual-corner estimates. The parent may
combine it with separately proved near/corner coverage at the maximum
of their onsets, after distinct review. It must not replace those cases
by a statement about this primitive alone.

## History and next unresolved step

2026-11-06, C06, requested Astra ultra under the parent's recorded hard
full-phase allocation; runtime serving metadata unexposed. Input/rules
b6e67b3c78cb668b6d2f9da5a5560537d2960bf3. Candidate, first kill and
errors were recorded in ../ideas/C06-far.md before development.

The n>=10^6 target needs a much sharper constant/phase-dependent finite
part. The present proof deliberately leaves interior cancellation
negative and uses a loose finite endpoint-row upper. Those are explicit
remaining quantities, not fitted constants or claims of a second near
model correction.
