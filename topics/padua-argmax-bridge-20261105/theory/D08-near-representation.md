# PD-T?argmax-bridge-codex-D08-representation — Combined near representation with a practical allowance

ID kind: PD-T. Aliases: D07 component assembly; near completed-model
error without old endpoint/interior allowances. Split from: D08 global
onset. Split into: the constant bridge, near, far and global comparisons
have separate D08 records.

## Statement

Use precisely the corrected primitive S_n and completed model M_infty
of D02, the D07 fixed six actual polynomial rows, and their original
weighted collision/endpoint conventions. For integer n>=32 and the
CLOSED signed near domain rho=|alpha|+|beta|<=1/2,

    |S_n(phi)-M_infty(phi,log n)|
      <=E_D04+E_global+Bmesh+(d/pi)Blog+B6.             (1)

Every component on the right is exactly the accepted D07 definition,
at the actual absolute phase: D07-global-outer(2), D07-global-mesh(6),
and D07-endpoint-six-row-allowance(1). In particular

    B6=[14a+P(8+log n)]/n+(71a+4P)/n^2.

No old e_rows or I_n term is present in(1). Define the phase-independent
upper Ehat(n) by the following explicit scalar formulas, with
m=n+1,L=log n,b=4/pi^2,H=1+L and
r=log(5/2)+1/18:

    A_D={ [52/pi^2+176/(3pi)]H+7+1/pi }/n
                                      +10/n^2+20H/(pi*n^2),
    A_G=[(21/5)L+(9/4)log(2m)+1022/15]/m,
    A_M=b(2L+2r)/n+[4+b(L+1/n)]/(4n^2-1)
              +b/(2n-1)^2+[5+b(log(n+1/2)+2)]/[4(n-1/2)^2],
    A_log=[3log m+log2+2log pi+2]/(2pi*m),
    A_6=(18+L/2)/n+73/n^2,
    Ehat=A_D+A_G+A_M+A_log+A_6.                       (2)

Then the right side of(1) is <=Ehat(n). Ehat decreases for all real
n>=32, and the validated scalar endpoint yields

    Ehat(40000)<=0.011538619525006<1/80.              (3)

Consequently (1) is <1/80 for EVERY integer n>=40000, uniformly in
the stated near domain, including the origin, axes and collisions.
At the fallback endpoint Ehat(50000)<=0.009374512828106.

Status: **PROVED**, analytic component assembly with a directed scalar
endpoint check, distinct review pending. The numerical trusted base is
the explicitly stated Decimal correct-rounding contract below; no
kernel, integration or phase sampling is a premise. This is not yet
the physical noncorner or global comparison.

## Dependencies and proof of the assembly

The accepted D05 fixed-row theorem bounds |S-K_fixed| by E_D04.
D07-global-outer bounds |K_fixed-G_n| by E_global. Its separate exact
mesh identity gives

    G_n-M_infty=(J6-C2)+Rmesh+(d/pi)Rlog,
    |Rmesh|<=Bmesh, |Rlog|<=Blog.

The corrected and independently accepted D07 six-row theorem gives
|J6-C2|<=B6 on rho<=1/2,n>=32. Combining these four inequalities proves
(1). The accepted endpoint correction is its weak inequality at P=0;
no strict-origin version of that intermediate estimate is used.
All dependencies retain actual finite polynomial collisions, the
exceptional x mode and unequal n,m meshes.

On this near triangle a<=1,p,P,d<=1/2 and H_n<=1+L. The accepted
full-phase scalar constants are |D0|<=4,|Z_n|<=5 and
|h_2(t)+h_2(1-t)|<=2r. D07 bounds E_global by A_G and |J6-C2| by
A_6. Substitution in each positive term gives exactly(2), including
the factor d/pi<=1/(2pi). This proves the uniform majorization without
a lower phase distance, sign assumption or inverse-a constant.

## All-degree monotonicity

A_D is a sum of positive multiples of (1+L)/n,1/n,(1+L)/n^2 and
1/n^2, all decreasing here. A_G decreases by the derivative already
proved in D07-global-outer. A_6 decreases by its accepted D07 proof.
For A_log the derivative of its numerator divided by m has sign
3-[3log m+log2+2log pi+2]<0 for n>=32.

For A_M, (2L+2r)/n decreases since L>3. Split its second term into
(4+bL)/(4n^2-1)+b/[n(4n^2-1)]. The second share decreases as a
product of positive decreasing factors. For the first share its
derivative numerator is b(4n^2-1)/n-8n(4+bL)<0 when L>=1.
The term b/(2n-1)^2 decreases. Finally the logarithmic tail decreases:
if U=5+b(log(n+1/2)+2), then b<1/2 and
b(n-1/2)/(n+1/2)<1/2<2U, which is the derivative test for
U/[4(n-1/2)^2]. Thus Ehat decreases for n>=32.

The scalar endpoint(3) therefore applies to every larger integer;
no assertion log n is bounded above on an unbounded degree range is
made. Its lower L conditions follow from n>=32.

## Scalar evidence and trusted base

The command and primary/fallback order were preregistered in
../ideas/D08-onset.md before evaluation. The unchanged source
../code/post_audit_D08_onset/evaluate.py evaluates(2) by 50-digit
directed Decimal intervals. Pi uses independent exact rational
alternating Machin bounds. Ln endpoints are enclosed by adjacent
values around the documented correctly rounded Decimal ln value;
basic arithmetic uses directed contexts. The script reuses only
AST-selected definitions from the SHA-pinned independently checked
D06 arithmetic source, never its top-level cases or main program.

The endpoint records budget-40000.json and budget-50000.json save
every component and outward decimal endpoints. Numerical CPU totals
.045671782 seconds for both scalar calls. No native/board/quadrature/
phase-grid job. Independent source/arithmetic review is required for
this new application; the author does not approve its own scalar check.

## Scope and history

This fresh near allowance replaces the positively charged e_rows/I_n
allocation that failed D06, by joining accepted exact meshes and six
actual rows. It does not alter those old bounds or assert a full
phase-relative S_n-a*S_n(0) theorem. The old M_near and its one
correction are untouched. The full far allowance has a different,
separately stated proof/domain in D08-far-comparison.md.

2026-11-06, parent-requested Codex Sol xhigh, input
`cbfdb044e184731984e3bf8be487008a86e68c37`. D07 global supplementary
acceptance in independent-checks-D07-global-profile.md (SHA256
`1cf2c4444791d76549bb59e168937fa78e6720f21b47a439865e3f0a6a34fb66`)
and endpoint focused acceptance in independent-checks-D07-endpoints.md
(`bbebb245bfda321d98899ca45ae459a2f87aef2224026116aef79bb542fb1808`)
precede this combination. This is a new claim, not
an extension of an old n500000 theorem by changing its quantifier.


### Supplementary review closure — 2026-11-06

The preceding developer-frozen text is retained unchanged. Distinct Astra
xhigh reconstruction ACCEPTED this scope with no unresolved findings;
[independent-checks-D08-global.md](../independent-checks-D08-global.md),
audited report SHA256 `c3ceac020dd1654b8b5be8340c2436b343ab740ba24253be3eab1837f17c9316`.
The independently executed scalar check confirms the failed40000 and
passed50000 budgets. This closes the earlier pending supplementary review;
final Claude audit remains pending and no theorem scope changes here.
