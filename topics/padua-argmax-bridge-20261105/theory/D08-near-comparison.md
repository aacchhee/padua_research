# PD-T?argmax-bridge-codex-D08-near — Physical near noncorner exclusion from degree40000

ID kind: PD-T. Aliases: phase-only limiting residual at the new loss;
near defect budget with absolute completed-model errors.
Split from: D08 global onset. Split into: constant bridge and near
representation have their own substantive D08 files.

## Statement and exact physical scope

For every integer n>=40000 and every physical odd center (J,K) of
PD-T364 which is NOT an actual nonnode corner, suppose

    theta=(J*pi+alpha)/n, phi=(K*pi+beta)/(n+1) in[0,pi],
    |alpha|+|beta|<=1/2.

Then the corrected Padua Lebesgue function satisfies

    lambda_n(cos theta,cos phi)<Lambda_c(n)-1/250.     (1)

The proof uses the exact physical full defect lambda=S_n-Delta;
no sum of the two projected floors is taken. All signed phases,
axes, chart boundaries, edges, both parities and polynomial collisions
are included. Actual nonnode corner centers are excluded from this
statement and have the separately accepted D02 inward comparison.

Status: **PROVED**, analytic assembly with D08's validated scalar
representation endpoint, distinct review pending. No old finite
M_near representation theorem is applied at this degree.

## 1. A fresh phase-only bound for T with the actual logarithmic loss

Write alpha,beta for absolute phases in this section, r2=alpha^2+beta^2,
L=log n, c=15/32. The inherited exact coefficient loss is

    G=(B_c-B0)L^2+(b_c-b_full)L>=A(L)r2,
    A(L)=47L^2/(48pi^2)+L/(24pi^2).                  (2)

The inequalities in(2) are the PHASE-ONLY coefficient inequalities of
N1-16, whose proofs do not use a finite-degree model approximation.
The exact equality b_M=b_full is in D08-near-constant-bridge.md.
For n>=40000, positive logarithmic series give

    L>=log40000=4log10+2log2
       >4(23/10)+2(69/100)>21/2.

Since pi^2<10, (2) gives A(L)>A0=20811/1920.

C04-near-limit-comparison.md equation(3) is a PHASE-ONLY bound for its
fixed limiting function T on alpha+beta<=1/2:

    T-T(0)<=c*alpha^(3/2)+(1225/144)alpha^2
       +(4/9)alpha^2 log(1/alpha)+(395/48)beta^2
       +(1/9)beta^2 log(1/beta)+10^-9 beta.           (3)

Its proof uses C04's noncentral bound and C01's directional central
integral bound, with no finite-n Q_n approximation. Hence this exact
phase inequality is usable here even though C04's old finite-model
comparison had a much larger degree floor. All zero-axis expressions
in(3) have their continuous values.

For alpha>=exp(-4), use

    A0-1225/144-16/9>11/20=:K.

Thus its net contribution in(3) minus A(L)r2 is bounded by
c*alpha^(3/2)-K*alpha^2. The exact maximum over x>=0 is

    27c^4/(256K^3)<1/32.                             (4)

If 0<alpha<exp(-4), first drop the negative quadratic
(1225/144-A(L))*alpha^2. Both remaining positive functions increase
up to exp(-4), so the alpha contribution is at most

    c*exp(-6)+(16/9)*exp(-8)
        <c(3/8)^6+(16/9)(3/8)^8<1/32,              (5)

using e>8/3. The origin contributes zero. Every comparison in(4)--(5)
is a finite exact rational inequality; the scalar source checks them.

For beta, A0-395/48>5/2 because the difference after subtracting5/2
is211/1920>0. Its entropy maximum is therefore at most

    sup_(x>=0) x^2[(1/9)log(1/x)-5/2]
         =exp(-45)/(18e)<1/(36*2^45).

Adding10^-9 beta<=1/(2*10^9) is still <1/1000000. We have proved
anew, for every L>=log40000 on the stated phase domain,

    T(phi)-T(0)-G(phi,L)<1/32+1/1000000.              (6)

No smooth Taylor expansion through absolute-value roots or finite-n
origin cusp is assumed. This is a comparison for the limiting T only.

## 2. Transfer to the completed model and actual primitive

D08's constant bridge gives

    M_infty(phi,L)-M_infty(0,L)
           <=T(phi)-T(0)-G(phi,L)+2eta0,
    2eta0<1/500.

D08-near-representation.md gives Ehat(n)<1/80 at both phi and0 for
every n>=40000, with S_n(0)=Lambda_c(n) exactly. Consequently

    S_n(phi)-Lambda_c(n)
      <1/40+1/500+1/32+1/1000000
       =58251/1000000<1/16.                         (7)

This is an absolute-error triangle, not an unproved full relative
S_n-a*S_n(0) theorem. The fixed old near representation enters only
the n->infinity bridge already proved in its separate file.

## 3. Subtract the actual physical defect

C02-defect-dense-band.md applies for n>=4096, physical odd centers,
rho<=1/2, with its original coordinate guards. If an odd center has
both endpoint coordinates it is one of the two actual nonnode corners.
Every other physical odd center has 0<J<n or0<K<m, so at least one
of its projected floors is strictly greater than1/16. The exact
PD-T364 identity gives Delta>=max(Q_v,Q_h)>1/16.
Separate phase evenness was used only for the common primitive/model
bound; this defect is still the original signed physical-center defect.

Combining lambda=S_n-Delta with(7) yields a deficit greater than
4249/1000000>1/250, proving(1). No assumption about an unknown
maximizer, localization, energy bound or sampled minimum is used.

## Checks, limits and history

The five exact Fraction controls and the directed Ehat endpoint are
in code/post_audit_D08_onset/evaluate.py and its two compact records.
The full proof of their analytic n monotonicity is in D08-near-
representation.md. No phase grid, kernel, board or quadrature execution.
The constant bridge, phase-only(3) and finite physical defect have their
own stated scopes. Old C04/C13 degree quantifiers and M_near remain
unchanged. Global far phases and actual inward corner patches have
separate comparisons. 2026-11-06, Codex Sol xhigh, parent request,
input`cbfdb044e184731984e3bf8be487008a86e68c37`; review pending.


### Supplementary review closure — 2026-11-06

The preceding developer-frozen text is retained unchanged. Distinct Astra
xhigh reconstruction ACCEPTED this scope with no unresolved findings;
[independent-checks-D08-global.md](../independent-checks-D08-global.md),
audited report SHA256 `c3ceac020dd1654b8b5be8340c2436b343ab740ba24253be3eab1837f17c9316`.
The independently executed scalar check confirms the failed40000 and
passed50000 budgets. This closes the earlier pending supplementary review;
final Claude audit remains pending and no theorem scope changes here.
