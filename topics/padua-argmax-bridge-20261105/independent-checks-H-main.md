# Campaign H independent main-proof mathematical review

Date: 2026-11-07. Reviewer: `/root/h_main_review`, a distinct Codex
mathematical audit worker. Parent-requested/API-accepted model and effort:
`gpt-6-astra`, xhigh; actual serving metadata is not independently exposed.
Rules/input branch head: `9eba8790948279942a5108e0512c30baf8efbfb8`,
`codex/padua-argmax-bridge-20261105`. The branch-ref file was read without
running Git. Concurrent proof files are pinned separately below.

## Decision and exact scope

**ACCEPTED within supplementary mathematical scope:** the frozen H01
harmonic expansion (1) and its complete assembly in section 5 prove

    Lambda_c(n)=A_N^2+kappa-1/N+O(log(N)/N^2),
    N=n+1/2, A_N=(2/pi)[log N+gamma+log(8/pi)],

over the full integer sequence. This is the original PD-T098 sharp corner
expansion, with its original constants and parity independence. There is
no unresolved BLOCKING, MAJOR or MINOR mathematical finding in this scope.
The proof supplies a degree-independent big-O constant; the original
target does not require a displayed numerical constant or onset.

The main proof reviewed is `theory/H01-exact-sum.md`, SHA-256
`a57e3e1d7fbfd5c347bf7e0bd50591dbd6d384ff20a9bc41ba0e79683fdb1226`.
Its statement includes `[-a^2*log m+beta_H]/m`. The earlier omitted
logarithmic term was a material pre-freeze development correction,
documented by its owner. This review accepts only the corrected hash and
does not retrospectively accept the earlier statement.

The accepted support inputs are:

| Input | Exact reviewed hash | Scope used here |
|---|---|---|
| H04 smooth residual | `25ffa263c0e66cd1bce983f7d9f7c29bb2e333884260ba00d49eb10f2e86a8bd` | Exact V_n object, C_B and beta_B, error at most 17/n^2 |
| H05 harmonic centering | `755e574e1653a3bbdac214a169e42668f7cf4f7e35d3020930b39091e600727c` | Local psi series, exact centering and uniform remainder; its weaker 2/m^2 consequence suffices |

Both support proofs were read and checked for their use in H01. The
separate [support review](independent-checks-H-support.md) independently
accepts these exact hashes, including the stronger signed H05 bound and
H04's coefficient sign. This report does not use that sign, H02, H03,
H06's developer reconstruction, an argmax theorem, a fitted coefficient,
or numerical enclosures as premises. It does not claim review of the
separately authored H06 prose.

This is mathematical soundness review only. It gives no historical
priority, novelty, gate-chronology, global-argmax, registry, final-ID or
readiness judgment. Under WORKFLOW's explicit no-novelty audit exception,
the complete IDEAS inventory was not reread. The Campaign-H briefing and
gate were read for scope and predecessor boundaries. No new candidate or
mechanism is proposed. This supplementary Codex review does not replace
the final Claude audit.

## Exact starting object and endpoints

PD-T159's corrected positive corner formula retains its exceptional
polynomial contribution 1/m. For each interior second row, folding the
periodic first grid converts its weighted absolute row to R_r/2. At the
other endpoint the periodic row is R_0=n^2 and the second-coordinate
half weight gives n/m. PD-T226 at zero phase gives the signed interior
row n, so R_r=2P_r-n. Consequently the exact scalar base is

    1/m+n/m+(2/(nm))*sum_(r=1)^n(2P_r-n)
      =1-2n/m+(4/(nm))*sum_(r=1)^n P_r,
    1-2n/m=-1+2/m.

The positive samples have centered first indices
`-r+1,-r+3,...,r-1`: there are exactly r of them because
`r-1<nr/m<r`. The cotangent addition identity on this symmetric set
gives F03's exact partial row `P_r=w(r/m)T_(n,r)`. The r=n=m-1 row
is present. A complete signed row has not replaced a partial row.

For q=(1-r/m)/2=s/(2m), F03's second harmonic sum has initial argument
`n-r+1-q=s-q`. Telescoping the locally defined psi series gives exactly

    D=psi(r+q)+psi(s-q)-psi(m-q)-psi(q).

The harmonic prefactor is exactly `(4/(nm))*(n/pi)=4/(pi*m)`.
The smooth residual is exactly H04's V_n. These checks derive H01 (2)
from the original conventions, including both endpoint weights, rather
than assuming the candidate's normalization.

## Uniform centering and the two endpoint sequences

The H05 shifts are `r+1/2-r/(2m)`, `s-s/(2m)` and `m-s/(2m)`.
The sign from expanding `-psi(m-s/(2m))` is positive in its linear
term. Thus the derivative bracket in H01 (7) has precisely the three
displayed terms. H05's stronger bound
`0<rho<=257/(216m^2)` implies H01's absolute `|E|<=2/m^2`
for every r,s>=1; there is no endpoint restriction.

For every real t>=1, the unit-cell midpoint comparison for y^-2 and
its second derivative 6y^-4 has a summable error O(t^-3). This proves
`psi'(t+1/2)=1/t+O(t^-3)` uniformly on that real range, not merely at
integers. Monotonicity of psi and its integer harmonic values show
`psi(t+1/2)-log t` tends to zero. Integrating the derivative difference
from infinity gives `e(t)=O(t^-2)`, while `u(t)=O(t^-2)` follows
directly. The constants in these bounds are independent of t and m.

The finite identity for the sum of `psi'(r+1/2)` in H01 (5) checks
by recurrence, including R=1. Since `u(r)/r=psi'(r+1/2)-1/r`,
subtracting H_R and taking the limit yields

    S_u=1-gamma-psi(1/2)-psi'(1/2)/2
       =1+2log2-pi^2/4.

The value `psi(1/2)=-gamma-2log2` follows from the same harmonic
series; `psi'(1/2)=pi^2/2` uses the elementary odd-square sum already
present in the original proofs. No evaluated or fitted constant enters.
Both S_e and S_u converge absolutely.

Substitution of the integer harmonic and derivative estimates into the
centered expression gives exactly

    D=log m+F(x)+e(r)-1/(2s)-x/(2m)-u(r)/(2m)+R_(m,r),
    |R_(m,r)|<=C[s^-2+(ms)^-1+m^-2].

In particular the psi(s) and -psi(m) scalar corrections are
`-1/(2s)+1/(2m)`, while the derivative bracket is
`1+x+u(r)+O(1/s+1/m)`. These facts verify the sign and coefficient
of every retained first-order term.

For r<=m/2, `w(r/m)/m<=a/r` and the remainder bracket is O(m^-2),
so that half contributes O(log(m)/m^2). For r>=m/2, writing s=m-r,
`w(r/m)/m<=Cs/m^2`; its three costs are respectively bounded by
`C/(m^2s)`, `C/m^3` and `Cs/m^4`. Summation gives the same scale.
This explicitly includes s=1, namely the potentially delicate last row.

With `v(x)=w(x)-a/x`, the bound `|v(x)|<=Cx` gives an error
`C/m^2 sum_(r<m)1/r` in each e/u sum. The omitted infinite tails
are O(m^-2). Therefore the e sequence contributes the constant aS_e
and no 1/m term; the u sequence contributes the required aS_u in the
first-order coefficient. The regularized integrands defining I1 and I2
are smooth through both endpoints. Their ordinary quadrature errors are
O(1/m) before multiplication by 1/m. All these steps produce at most
one harmonic logarithm in the final error.

## Singular trapezoid and the harmonic coefficient

Put `c0=gamma+2log2`, `c1=pi^2/4-1`. At zero,
`F(x)=log x+c0+c1*x+O(x^2)`. At the other endpoint, with y=1-x,
`psi(y/2)=-2/y-gamma+O(y)` and `w(1-y)=pi*y/2+O(y^3)`.
Consequently H01's regularized function has exactly

    R(0)=a*c1, R(1)=pi-a*c0.

Near zero it is an analytic function plus `v(x)log x`, where
v(x)=O(x) is analytic. Near one its only leading nonsmooth term is
a multiple of y*log y, with smoother analytic factors. Direct
differentiation gives

    |R''(x)|<=C[1+1/x+1/(1-x)].

The endpoint-cell errors are O(m^-2 log m) from
`R(x)-R(0)=O(x|log x|)` and its upper-endpoint counterpart.
On interior cells the sum of the second-derivative suprema is
O(m log m); multiplying by the local m^-3 trapezoid error gives
O(log(m)/m^2). Thus the endpoint-excluded rule contains the exact
charge `-[R(0)+R(1)]/(2m)` with the stated uniform remainder.

The logarithmic harmonic sum in (17) follows from the convergent sum
of local trapezoid errors for log(t)/t. Its error tail is
O(log(m)/m^2), since the second derivative is
`(2log t-3)/t^3`. The constant C_K is thereby independent of m.
Also the smooth v trapezoid correction cancels the `-a/(2m)`
in aH_(m-1), so the cotangent weight average is

    a(log m+gamma)+I_v+O(m^-2), I_v=a log(2/pi).

For an independent coefficient check, rewrite the main sum as

    M_m=a sum_(r<m)log(r)/r+a*c0*H_(m-1)
        +log(m)*(1/m)sum_(r<m)v(r/m)+(1/m)sum_(r<m)R(r/m).

The `-a log(m)/(2m)` from the first sum cancels the
`+a log(m)/(2m)` from the v trapezoid charge. The remaining first
coefficient is

    -[a*c0+R(0)+R(1)]/2=-(pi+a*c1)/2.

The logarithmic coefficient is `a*c0+I_v=a*c`, where
`c=gamma+log(8/pi)`. This proves H01 (19) with a true constant C_M.
The only error multiplied by log m here is O(m^-2), not
O(log(m)/m^2); no hidden log-squared remainder is introduced.

Combining these terms and `c1+S_u=2log2` gives the accepted harmonic
expansion with the exact logarithmic first correction
`-a^2 log(m)/m` and

    beta_H=-2-a^2(gamma+2log2)-a(I1+I2).

## Integral cancellation, assembly and original constant

For I_B from H04, the double-angle identity reduces the combined
integrand of `2I_B-aI1` to

    x(w^2-1)-2a*w+a^2/x.

Keeping the lower endpoint epsilon until integration, and using
`w'=-(1+w^2)/a`, its integral is exactly

    a*epsilon*w(epsilon)-1+epsilon^2
      +a^2 log(sin(pi*epsilon/2)/epsilon).

Its limit is `a^2-1+a^2 log(pi/2)`. The cancellation is performed
before splitting divergent terms, so there is no untracked endpoint
constant. H04 gives `beta_B=-a^2+2I_B+aI2`. This is a constant,
so replacing beta_B/n by beta_B/m costs O(m^-2), with no logarithmic
factor. Including the exact base +2/m therefore gives

    2+beta_H+beta_B=-1-a^2[gamma+log(8/pi)],
    Lambda_c=A_m^2+C-[1+a*A_m]/m+O(log(m)/m^2).

The identification C=kappa is noncircular. The previously accepted
PD-T269 theorem proves `Lambda_c-L_n^2 -> kappa` independently of
the sharp expansion. PD-T270 proves `L_n^2-A_n^2=O(log(n)/n^2)`.
Finally `A_n^2-A_m^2=O(log(n)/n)` tends to zero. Hence
`Lambda_c-A_m^2 -> kappa`, fixing the constant in the new expansion.
PD-T271's decimal enclosure, and all earlier fits, are unnecessary.

For N=m-1/2, elementary logarithmic Taylor remainder gives

    A_N^2=A_m^2-a*A_m/m+O(log(m)/m^2),
    1/N=1/m+O(m^-2).

Substitution proves the stated sharp result. Every bound holds on all
integers m>=3, and log(m)/m^2 is comparable to log(N)/N^2 there.
No parity step, excluded endpoint strip or degree-dependent signed
constant is hidden in the conclusion. Expanding A_N^2 gives the original
`b=(8/pi^2)(gamma+log(8/pi))` and constant term
`[(2/pi)(gamma+log(8/pi))]^2+kappa`.

## Other complete-read inputs and performed actions

The original target and the following full theory files were read,
including their proof and scope. Hashes were obtained locally:

| Original input | SHA-256 |
|---|---|
| PD-T098, programme-ideas-claude-04-padua-corner-expansion.md | `0cb7bf1f797f20a8c5dd5cf8f88aaf75571fdc2908ec46cc2eb15c04f190d499` |
| PD-T159, proof-attempts-2-codex-04-corner-product-comparison.md | `3da8a12e841d3555af2a586909ed7a258c760f17c9ea4af2079c9f044568e263` |
| PD-T226, gated-codex-12-row-primitive-identity.md | `2692c28af71b4f5eeb129f3a2f32a24a5a3e7e8929279063e0c63f3edbaf3d92` |
| PD-T269, t4-01-corner-defect-limit.md | `a40f61a44d787201ecfe82f08eccb9e57de02a9d3a18161741be7f2f8cde4b46` |
| PD-T270, t4-02-one-dimensional-remainder.md | `ead57816c2b33e250462514e25bcd4e709902523b33bd4cf1a17c007a6ec2e28` |
| PD-T271, t4-03-corner-constant.md | `957802f2b3060a704f5a8b72042951f2a623716e2f817eccbed2ee8a23595e8f` |
| F03-origin-sign.md | `ddccb0512f0f4abfb50531a762216a7fb71a038de6cd1b64e4f73e44de42d1ea` |

Rules read: AGENTS.md, agents/WORKFLOW.md and agents/codex/CODEX.md.
All displayed proof hashes were checked against the frozen inputs.
Read-only actions used `pwd`, `rg --files`, `rg -l`, `cat`, bounded
`sed`, `wc -l`, and `sha256sum`; truncated aggregate outputs were
followed by bounded rereads. The only write is this assigned report,
using apply_patch. No developer proof was edited. No Git command or
mutation, shared-file edit, PDF, numerical experiment, scalar evaluation,
scientific job, native/compiler job or computational rerun occurred.

The verification is independent paper reconstruction. No scientific
rerun is required for this analytic result. Parent integration may cite
this accepted mathematical scope; materially altered proof text or a
different final theorem requires the corresponding focused check.

## Parent integration acceptance addendum — 2026-11-07

At the root's separate request, the complete parent integration
`theory/H-sharp-corner-expansion.md` was read at SHA-256
`e3d402944ab4bfab0d743db7328282fe039c143618c3ac0d59e9a68dff73101e`.
**ACCEPTED:** its statement, normalization, coefficients, constants,
dependency scopes and proof agree with the accepted sharp theorem above.
The root may adopt its corner theorem as PROVED on this mathematical
review; the proposed status/disposition update does not require repeating
the accepted proof audit. No unresolved integration finding remains.

In particular (-1,-1) is a nonnode for either parity: its endpoint
indices have sum n+(n+1)=2n+1. The stated all-n quantifier is valid.
Any eventual uniform big-O constant can be enlarged over the finitely
many initial n>=2, since each exact R_n is finite and log(n+1/2)>0.
The same enlargement works for both parities. Multiplication by N leaves
error O(log(N)/N), proving the displayed limit -1. The constant kappa
is the original analytic PD-T269 constant; the decimal enclosure remains
optional and is not a premise of the corner theorem.

All relative theory/review links resolve to the read records. H06 was
also read to check the integration's description of it as a developer
reconstruction, rather than a distinct acceptance; the accepted main
proof chain remains H01/H04/H05. Its read hash was
`75a56f858515c831cfe598cbca347cc0e6720db084b86e5e1635a8b848d220bf`.
This addendum does not turn H06 into an independently allocated result.

The complete G01 statement and verification boundary were read at hash
`646cca0b0fd8c1faccbff504e263545b073318da3211c150cfc06a827aead86f`.
The parent's separate global consequence correctly inherits G01's
computer-assisted and implementation dependencies. It does not make
those dependencies analytic or supply a fresh G01 audit/rerun. The
corner theorem itself is independent of argmax. Final Claude review,
registry application and readiness remain separate.

This focused check used prose reads, file discovery and hashes only;
the sole write was this addendum. No developer text, source, shared file
or Git state was changed and no scientific job was executed.
