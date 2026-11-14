# PD-T?argmax-bridge-codex-D08-far — Full closed far exclusion from degree50000

ID kind: PD-T. Aliases: completed far constant budget; valid C08
coefficient loss at the preregistered fallback; all-degree far margin.
Split from: D08 global onset. Split into: none. Near representation
and near physical comparison have their own D08 files.

## Statement

For every integer n>=50000 and every real phase pair satisfying

    1/2<=|alpha|+|beta|<=pi,

the original corrected primitive satisfies

    S_n(alpha,beta)<Lambda_c(n)-1/100.                (1)

The whole closed far diamond, including a=0, vertices, axes, weighted
polynomial collisions and both parities, is included. This uses D02's
openly declared completed model M_infty and does not change the old
M_far or its nondecaying bias. Status: **PROVED**, analytic application
with a directed scalar endpoint; distinct review pending. The accepted
computer-assisted PD-T271 lower constant is an explicit dependency,
not a sampled or conjectured deformation value.

## 1. Degree-independent constant bounds

Let k_shift=gamma+log(8/pi)>3/2, B_c=4/pi^2 and b_c=8k_shift/pi^2.
Use k_shift separately from the limiting corner deformation D_infty.
The exact normalization S_n(0)=Lambda_c(n) and D02's uniform limit,
compared with PD-T271's expansion, give

    C_infty(0)=B_c*k_shift^2+D_infty.                 (2)

Indeed PD-T271 uses log(n+1/2), whose difference from log n is at
most1/(2n); its quadratic/linear changes tend to zero. Its remainder
tends to zero on both degree parities, so uniqueness of D02's origin
constant proves(2). This is a LIMIT comparison, not a finite inequality
Lambda_c>=A_n^2+D_infty.

PD-T271 Statement(2) is a PROVED strict outward enclosure

    D_infty>0.919710118388492535099518225790>9/10.

Its original source/receipts and independent/Claude reruns are documented
in attempts/D08-corner-limit.md; the canonical theorem is
topics/padua-lebesgue-followups-20261103/theory/t4-03-corner-constant.md.
Its trusted numerical base is the accepted Arb computation with exact
analytic tail, not a new numerical integration or a regression. Since
pi<22/7, B_c>49/121 and therefore

    C_infty(0)>9/10+(49/121)(3/2)^2=4383/2420.        (3)

For the full-phase upper, C08's degree-independent constant estimates
give C_far<8821/3000 for the UNCHANGED R64,delta1/100 member. D02's
exact bias identity and its uniform bound give

    C_infty<C_far+1/63^2+Q(2,1/100).

Using pi>31/10 and log(400pi)<8,

    Q(2,1/100)<637/4805,
    8821/3000+1/3969+637/4805<123/40.

Thus, on the complete closed phase diamond,

    C_infty(phi)<123/40.                             (4)

The logarithmic inequality follows elementarily from e>8/3,
pi<22/7 and (8/3)^8>400*(22/7); the final comparison is rational.
These statements bound phase-only constants and have NO finite-n
floor inherited from old C08/C13 representation theorems.

## 2. Use the actual accepted coefficient inequality

The accepted C08-far-weighted-coefficient theorem is

    b_full-b_c<=3(1-a)/pi^2.                         (5)

The parent brief's proposed b_full-a*b_c<=5(1-a)/4 was not adopted:
at the exact midpoint a=0,b_full=4/pi>5/4. This countercheck concerns
that proposed shortcut only. It does not affect the accepted(5).

On the far phase domain a<=cos(1/4), so the alternating cosine bound
gives u=1-a>=191/6144. For L>=log40000>21/2, (3)--(5) imply

    M_infty(0,L)-M_infty(phi,L)>F(L),
    F(L)=(191/6144)[(49/121)L^2-(147/484)L]
                                  -[123/40-4383/2420]. (6)

Here the coefficient loss is u(4L^2-3L)/pi^2, and pi<22/7 bounds
this positive quantity below by u(49/484)(4L^2-3L). The linear
coefficient is147/484; the invalid17/484 shortcut never enters.
F increases whenever L>3/8, since its derivative has the sign of
392L-147.

## 3. Fresh finite-degree far representation and its monotonicity

Let U_F(n) be EXACTLY the right side of D05-outer-comparison.md(2),
with its auxiliary R=2,delta=pi/8, after the conservative substitutions

    a=1,p=1,P=2,d=1,abs(U0)=8,H_n<=1+log n.           (7)

In other words U_F=E_D04+e4+I_n+D_pole+T_Z with ALL definitions
in that accepted D05 theorem unchanged. This full-phase bound has
the actual domain n>=ceil(2pi*2/(pi/8))=32. It is not an application
of the old R64,delta.01 finite representation below its floor. Its
old positive e_rows/I_n terms are allowed here as a conservative FAR
error; the separately proved NEW NEAR allowance does not use them.

Every term is nondecreasing in the independent phase inputs in(7).
For its entropy factor, u[1+log(1+S/u)] increases in u,S and has its
continuous zero limit. Thus on the full diamond,

    |S_n(phi)-M_infty(phi,L)|<=U_F(n), n>=32.          (8)

For completeness U_F decreases on every real n>=32, as follows
directly from these explicit formulas. Put m=n+1,X=m/8.

- E_D04,D_pole and e_rows are positive sums of (cL+d)/n^j, j>=1,
  decreasing here. The exact e_rows is(181+19L)/n+21600/n^2.
- The L/m share of e_mesh decreases since L>1+1/n. Both C_X shares
  decrease for X>=4: their log numerators grow at most as1/[2(X+1/2)]
  while their positive denominator powers grow faster relatively.
  The remaining inverse-power terms decrease.
- e_collision is a positive linear-log numerator in m divided by m,
  plus inverse products. Its numerator exceeds its log coefficient,
  so it decreases for m>=33.
- I_n is of the form(cL+d+e log m)/m with fixed nonnegative constants.
  Its derivative numerator is c(1+1/n-L)+e(1-log m)-d<0 here.
- The T_Z BV, initial-gap and hole shares are positive expressions
  (c log m+d)/m. Their actual logarithms are log(4m/pi),log(8m/5)
  and log(2m), and each numerator exceeds its logarithmic coefficient.
  The upper-gap share is W(delta-h/2)/m; delta-h/2 increases and W
  is positive decreasing, so it too decreases.

This verifies the complete U_F domain and all-n monotonicity, rather
than inferring either from sampled degrees. At the origin use D08's
independent NEAR bound |Lambda_c-M_infty(0,L)|<=Ehat(n), which also
decreases for n>=32.

## 4. Primary failure and preregistered fallback

The source and commands were preregistered in ideas/D08-onset.md.
Only40000 was executed first. Its valid margin was below its required
errors, with comparison slack enclosed in
[-.037870764666100,-.037870764666099]. That primary gate failure was
recorded in attempts/D08-onset.md BEFORE executing the already
authorized50000 fallback with unchanged source/formula/constants.
It is a failure of this sufficient allowance, not an argmax counterexample.

The directed scalar fallback gives

    F(log50000)>=.107768594441076,
    U_F(50000)<=.061683200165682,
    Ehat(50000)<=.009374512828106,
    F-U_F-Ehat>.0367>1/100.                          (9)

The stored interval evaluation of the last expression has lower
endpoint .036710881447289. Pi is enclosed by an exact rational Machin
series and all arithmetic/log operations have the directed Decimal
contract described in D08-near-representation.md. The two scalar calls
total .045671782 CPU seconds, including imports/helpers. No phase
values, board calls, integration or fitting were evaluated. Independent
source/arithmetic review is required for this new application.

Since F increases while U_F and Ehat decrease, (9) holds for every
integer n>=50000. Finally

    Lambda_c-S_n(phi)>F(log n)-U_F(n)-Ehat(n)>1/100,

which proves(1). No old n500000 quantifier has been changed or used
at the new degree, and no finite corner lower was inferred merely
from D_infty>9/10.

## Scope and history

This is the actual primitive FAR comparison. Physical lambda<=S_n
follows separately from the full defect identity; the global equality
classification still requires near noncorner and actual-corner cases.
The accepted full relative S_n-a*S_n(0) target remains OPEN. All models,
old proofs and degree certificates remain frozen. 2026-11-06, Codex
Sol xhigh, parent request, input`cbfdb044e184731984e3bf8be487008a86e68c37`.


### Supplementary review closure — 2026-11-06

The preceding developer-frozen text is retained unchanged. Distinct Astra
xhigh reconstruction ACCEPTED this scope with no unresolved findings;
[independent-checks-D08-global.md](../independent-checks-D08-global.md),
audited report SHA256 `c3ceac020dd1654b8b5be8340c2436b343ab740ba24253be3eab1837f17c9316`.
The independently executed scalar check confirms the failed40000 and
passed50000 budgets. This closes the earlier pending supplementary review;
final Claude audit remains pending and no theorem scope changes here.
