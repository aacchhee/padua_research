# PD-T?argmax-bridge-codex-H05-centering — Uniform first-order centering of the exact harmonic row

ID kind: PD-T; provisional supporting theorem, no global allocation.
Aliases: H05 digamma centering; shifted harmonic row; uniform trigamma
correction; endpoint-complete first-order harmonic centering.
Split from: supporting obligation for H01 and original OPEN PD-T098.
Split into: none. The full corner expansion remains a separate OPEN target.

## Statement

For EVERY integer m>=2 and EVERY integer 1<=s<=m-1, put

    r=m-s, q=s/(2m), c=1-1/(2m),
    D_s=psi(m-cs)-psi(q)-psi(m-q)+psi(cs),
    M_s=psi(r+1/2)+psi(s)-psi(q)-psi(m),
    J_s=r*psi'(r+1/2)+s*psi'(s)-s*psi'(m).

Then

    D_s=M_s-J_s/(2m)-rho_s,                         (1)
    0<rho_s<=257/(216m^2)<5/(4m^2).                 (2)

In particular the proposed epsilon_s in the H05 registration equals
`-rho_s`; it is uniformly O(m^-2) and has a definite negative sign.
For the actual weights `w_s=tan(pi*s/(2m))`, define

    Hcal_m=4/(pi*m) sum_(s=1)^(m-1) w_s*D_s,
    Ccal_m=4/(pi*m) sum_(s=1)^(m-1) w_s*M_s
                  -2/(pi*m^2) sum_(s=1)^(m-1) w_s*J_s.

With `H_k=sum_(j=1)^k 1/j`, the complete weighted consequence is

    0<Ccal_m-Hcal_m
      <=257*H_(m-1)/(27*pi^2*m^2)
      <10*H_(m-1)/(pi^2*m^2)
      <=10*(1+log(m-1))/(pi^2*m^2).                (3)

The exact first-order coefficient also has the positive finite-tail form

    J_s=r*psi'(r+1/2)+s sum_(k=s)^(m-1) 1/k^2,
    0<J_s<1+2r/m<3.                               (4)

There is no parity restriction. All these statements include s=1 and
s=m-1 and use the exact denominator m. No origin-sign theorem, sharp
corner expansion, remaining weighted-harmonic asymptotic or smooth-B
remainder is asserted by (1)--(4).

## Definitions and assumptions

For x>0 define the harmonic-series function

    psi(x)=-gamma+sum_(k=0)^infinity
                         [1/(k+1)-1/(k+x)],        (5)

where gamma is the harmonic constant used in PD-T270. Every derivative
and finite-shift identity needed here is proved below from (5). No
external digamma or polygamma theorem is imported. Natural logarithms.

The theorem is a statement about (5) for the displayed exact arguments.
Its identification with H01's harmonic part of the actual corner formula
uses H01's separately owned exact row derivation. H05 neither proves nor
assumes a replacement of partial cotangent rows by complete signed rows.

## Status by part

Overall status: **PROVED**, written developer proof.

| Mathematical part | Status | Evidence |
|---|---|---|
| Exact centering (1), uniform one-sided remainder (2) | PROVED | Local series and integral Taylor remainder below |
| Actual weighted uniform estimate (3) | PROVED | Positive cotangent-weight sum bound below |
| Exact positive correction (4) | PROVED | Finite recurrence and elementary midpoint comparison |

The derivative, recurrence and midpoint estimates below are routine
lemmas of this single centering theorem. No independent acceptance is
claimed; root retains integration and distinct review. This supporting
result does not change the status of original PD-T098.

## Depends on

- Definition of gamma in PD-T270. Its value does not enter any error
  estimate because constants disappear under differentiation.
- H01 supplies the exact identification of D_s with its harmonic row;
  that identification is not needed to prove the abstract estimate.
- [F03-identities-support](F03-identities-support.md), via H01 and the
  PD-T159/PD-T226 exact rows, identifies the actual corner contribution.
- The completed Campaign-H predecessor gate, the OPEN F03 target and PD-T269/270/271
  are scope/predecessor records, not imported analytic estimates here.

## Proof

### 1. The series and its first two derivatives, proved locally

Fix any compact interval [a,b] contained in (0,infinity). For k>=1,

    |1/(k+1)-1/(k+x)|
      =|x-1|/[(k+1)(k+x)]<=C_(a,b)/k^2.

Thus (5) converges uniformly there. The formal derivative and second
derivative series are uniformly absolutely convergent there as well:
their terms are bounded respectively by `(k+a)^-2` and
`2(k+a)^-3`, whose tails are bounded by elementary integrals. This is
enough to justify the derivatives without using a special-function
theorem. Indeed, integrate the finite partial-sum derivative between two
points in [a,b], pass to the uniform limit, and use the fundamental
theorem of calculus; repeat with the second derivative series. Hence

    psi'(x)=sum_(k=0)^infinity (x+k)^-2>0,
    psi''(x)=-2 sum_(k=0)^infinity (x+k)^-3<0.       (6)

For any u>0, the decreasing function (u+t)^-3 gives

    sum_(k=0)^infinity (u+k)^-3
      <=u^-3+int_0^infinity (u+t)^-3 dt
      =u^-3+1/(2u^2).

Consequently

    |psi''(u)|<=u^-2+2u^-3.                        (7)

The positive series in (6) also proves directly that psi'' is strictly
increasing on (0,infinity): each negative summand increases with x.
No third derivative is needed. Telescoping the absolutely convergent
first-derivative series gives, for integers 1<=s<m,

    psi'(s)-psi'(m)=sum_(k=s)^(m-1) 1/k^2.          (8)

### 2. Exact remainder, including its sign

For x>h>0, integrating (6) twice gives the exact Taylor identity

    psi(x-h)=psi(x)-h*psi'(x)+R(x,h),
    R(x,h)=int_0^h (h-t)*psi''(x-t) dt<0.           (9)

The sign and (7) imply

    0<-R(x,h)
      <=(h^2/2)*[(x-h)^-2+2(x-h)^-3].             (10)

The actual three shifted arguments are exactly

    m-cs=r+1/2-r/(2m),
    cs=s-s/(2m),
    m-q=m-s/(2m).

Apply (9) at `(x,h)=(r+1/2,r/(2m))`, `(s,q)` and `(m,q)`.
Keep the term -psi(q) unchanged. The resulting first-order terms are
exactly -J_s/(2m), with the PLUS contribution from expanding
`-psi(m-q)` retained. Therefore (1) holds with

    -rho_s=R(r+1/2,r/(2m))+R(s,q)-R(m,q).          (11)

Here both remainders in the difference have the SAME shift q. Because
s<m, strict monotonicity of psi'' in (6) gives

    R(s,q)-R(m,q)
      =int_0^q (q-t)*[psi''(s-t)-psi''(m-t)]dt<0.

Together with the strict negativity of the first remainder this proves
rho_s>0. In particular no absolute-value estimate is needed to infer
the summed sign. It also gives the sharper useful upper comparison

    rho_s<=-R(r+1/2,r/(2m))-R(s,q),                (12)

since R(m,q)<0. The positivity of every argument follows from the
lower bounds in the next step; no pole is evaluated or assigned a value.

### 3. Uniform constants on the whole index range

For the first remainder,

    r+1/2-r/(2m)=r+q>=r,

so (10) gives

    -R(r+1/2,r/(2m))
      <=r^2/(8m^2)*[r^-2+2r^-3]
      <=3/(8m^2).                                 (13)

For the second remainder, m>=2 gives

    s-q=s*(1-1/(2m))>=3s/4.

Thus

    -R(s,q)
      <=s^2/(8m^2)*[16/(9s^2)+128/(27s^3)]
      <=22/(27m^2).                               (14)

Adding (13) and (14) in (12) proves

    rho_s<=[3/8+22/27]/m^2=257/(216m^2),

which is (2). Every inequality holds for every r,s>=1. In particular
the cases r=1 and s=1 need no exclusion, limiting convention or change
of constants. For completeness the third remainder also obeys a
separate uniform estimate: m-q>=3m/4, q<1/2 and m>=2 imply

    -R(m,q)<=1/8*[16/(9m^2)+128/(27m^3)]
            <=14/(27m^2).                         (15)

The cruder triangle bound is 41/(24m^2)<2/m^2. The signed comparison
(12) improves that bound to (2). This records the original endpoint
kill test explicitly rather than relying only on cancellation.

### 4. The actual weighted sum

On 0<x<pi/2, the derivative of `sin x-x*cos x` is x*sin x>0, and
the expression is zero at zero. Hence cot x<1/x. With r=m-s,

    w_s=cot(pi*r/(2m))<2m/(pi*r),
    sum_(s=1)^(m-1) w_s<(2m/pi)*H_(m-1).           (16)

All weights are positive. Multiply (1) by them and sum; (2) and (16)
give

    Ccal_m-Hcal_m=4/(pi*m) sum_s w_s*rho_s>0,
    Ccal_m-Hcal_m
      <=4/(pi*m)*257/(216m^2)*(2m/pi)*H_(m-1)
      =257*H_(m-1)/(27*pi^2*m^2).

Finally H_k<=1+log k for every integer k>=1 follows by comparing the
terms from 2 through k with the integral of 1/x on [1,k]. This proves
all of (3), including the minimal case m=2, where H_(m-1)=1 and
log(m-1)=0. Since n=m-1, the weighted error is O(log n/n^2) over all
integers n>=2 without substituting n for the exact denominator m in
any displayed first-order term.

### 5. Exact form and elementary size of the correction

Equation (8) gives the finite-tail identity in (4). To bound its first
term, use f(x)=x^-2. This function is strictly convex, so its value at
the midpoint of any unit interval is strictly smaller than its average
over that interval. Summing intervals [r+k,r+k+1] and taking the limit
gives

    psi'(r+1/2)<int_r^infinity x^-2 dx=1/r.

Also, for every integer k>=1,

    1/k^2<=2/[k(k+1)].

The finite telescoping sum therefore yields

    s sum_(k=s)^(m-1) 1/k^2
      <=2s*(1/s-1/m)=2r/m.

Both terms in J_s are strictly positive. Combining these bounds proves
(4). A useful optional midpoint-defect estimate is

    d_r=1-r*psi'(r+1/2),
    0<d_r<=1/(4r^2).                               (17)

Here is a local proof of its constant. On a unit interval [k,k+1] with
midpoint a=k+1/2, integrate the two Taylor formulas about a. The linear
terms cancel, giving

    int_k^(k+1) f(x)dx-f(a)
      =1/2 int_k^(k+1) (1/2-|x-a|)^2*f''(x)dx.

For f=x^-2 the kernel is nonnegative and at most 1/8. Summing from
k=r to infinity gives an error at most

    (1/8) int_r^infinity 6x^-4 dx=1/(4r^3).

Multiply by r to obtain (17). This estimate does not authorize replacing
the first-order correction by its limiting value in the singular
weighted sum: its small-r contribution can affect the coefficient of
1/m. The finite-tail form (4) is the exact simplification supplied here.

## Checks and sources

PAPER ONLY: repository text reads/searches, prospective owned prose
registration and the written series/Taylor proof. No Python/import,
numeric/scalar/native, degree/endpoint/corner/phase, quadrature, compiler,
source-control job or finite experiment was executed. No external paper
or unread theorem is a premise. No Git or shared-file mutation occurred.

This is developer verification, not an independent audit. The endpoint
tests, sign, constants and exact weight factor are exposed above for
distinct reconstruction. No executable run is needed for this lemma.

## Scope and open items

H05 completes the registered uniform centering support only. H01/H06
still have to control their remaining weighted harmonic terms, H04 the
smooth B contribution, and the full assembly its original normalization,
first-order coefficient and N=n+1/2 transfer. The F03 absolute partial
row cannot be replaced by its full signed row. Original PD-T098 remains
OPEN until a separate complete proof is written and reviewed.

## History

2026-11-07, parent-released H05 PAPER ONLY. Rules/input
`ad257038cdff1d66f6e9c03d7ed43405c76cf6b0`. Parent-assigned Codex
mathematical developer; actual serving model/effort metadata is not
independently exposed. The same-basename idea and attempt files were
written with the candidate, separation and endpoint kill test BEFORE
this derivation. The first reported bound was the cruder absolute
triangle bound 2/m^2; the subsequent SAME-shift comparison in (11)
proves the stronger one-sided result (2). All are inside the originally
registered support scope. Root owns Git/shared LOG/integration.

## Dated status addendum — 2026-11-08 (Claude audit-03 MINOR fix H-C01)

Statements above that "the full corner expansion remains a separate OPEN
target" and that "no independent acceptance is claimed" describe the state at
first freeze and are historical. The full expansion
[H-sharp-corner-expansion](H-sharp-corner-expansion.md) is PROVED, and this
centering lemma was accepted by [independent-checks-H-support.md](../independent-checks-H-support.md)
and [independent-checks-H-main.md](../independent-checks-H-main.md); the Claude
reconstruction is [audit-03](../audit-03.md). The status of original PD-T098 in
shared registries follows reviewed registry application, not this note.


## Dated dependency correction — 2026-11-08 (F-01, H-C02)

The canonical exact origin reduction is now the separate **PROVED**
[F03-identities-support](F03-identities-support.md), split from historical
F03 sections 1–3. Its PD-T159 endpoint normalization and PD-T226 signed
periodic/polynomial endpoint rows are explicit premises of the reduction.
References above have been repointed accordingly. The original F03 sign and
useful-lower targets remain **OPEN** and are not assumptions of this result;
the proposed exact O(n) evaluator is also not assumed. H05's abstract series
estimate itself does not require the corner identification.

This corrects the source/status mapping, not the exact formulas or H theorem.
The original prose and reviewed source pins remain available at input commit
`b45e29fa1fe3dbfa2517ff8043e5d9c440870530`; no historical audit has been edited.
The [distinct review](../independent-checks-onset512-response.md#f03-source-split-and-h04-majorants--accepted-focused-response)
accepts the split and dependency map; H04's two valid majorants are also
independently reconstructed there.
