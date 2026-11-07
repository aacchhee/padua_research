# H06 — Independent reconstruction of the weighted harmonic aggregate

Verification record; no new global ID or independent claim allocation.
Aliases: weighted endpoint aggregation; logarithmic singular subtraction.
Rules/input `ad257038cdff1d66f6e9c03d7ed43405c76cf6b0`, 2026-11-07.

## Scope and disposition

The registered H06 candidate is mathematically equivalent to the aggregate
route simultaneously obtained by H01, and is consolidated there. This
record gives an independent paper derivation of the singular quadrature,
the endpoint sequence coefficient, and the final normalization. It also
records the distinct reading of the complete H04 and H05 proofs. It is a
supplemental reconstruction, not the required Claude audit or root
acceptance, and assigns no new novelty or priority claim.

The independently reconstructed conclusion, with notation below, is

    Hcal_m=A_m²+C_H+[-a² log m+beta_H]/m+O(log(m)/m²),     (1)
    beta_H=-2-a²*c0-a*(I1+I2).

The constant `-a² log m/m` is essential. The initial H01 theorem display
omitted it while the proof retained it; H06 reported that presentation
error to H01 and the root for correction. It must occur in every adopted
version of the supporting theorem. The subsequent H01 theorem display
was read and contains the correction exactly as in (1).

The main singular quadrature and endpoint sums are proved below without
numerical evidence. Applying them to the actual `D` uses H05's written
uniform centering theorem. The full-corner consequence additionally uses
H04 and the accepted exact F03 endpoint normalization. Neither review
acceptance nor original PD-T098 status is changed by this worker.

## Definitions and precise dependencies

Let m=n+1>=3, r=1,...,m-1, s=m-r, x=r/m, and put

    a=2/pi, c0=gamma+2log2, c=gamma+log(8/pi),
    c1=pi²/4-1, A_m=a*(log m+c), w(x)=cot(pi*x/2),
    F(x)=log x+log(1-x)-psi((1-x)/2),
    e_r=psi(r+1/2)-log r, u_r=r*psi'(r+1/2)-1,
    I1=integral_0^1 [w(x)/(1-x)-a/x] dx,
    I2=integral_0^1 x*w(x) dx.

Here psi is H05's locally defined harmonic-series function. H01/F03's
exact harmonic row and its contribution are

    D=psi(r+(1-x)/2)+psi(s-(1-x)/2)
                         -psi(m-(1-x)/2)-psi((1-x)/2),
    Hcal_m=(2a/m) sum_(r<m) w(r/m)*D.

H05 supplies, on the ENTIRE displayed index range,

    D=psi(r+1/2)+psi(s)-psi((1-x)/2)-psi(m)
      -[r*psi'(r+1/2)+s*psi'(s)-s*psi'(m)]/(2m)+E,
    |E|<=5/(4m²).                                      (2)

The exact original scalar normalization is

    Lambda_c=-1+2/m+Hcal_m+4V_n/(nm).                    (3)

Formula (3) keeps both actual polynomial endpoint rows and the separate
exceptional contribution. No signed complete-row replacement is used.
The inherited exact reduction is H01/F03's scope; the independent
analytic work below does not assume a finite one-index evaluator.

## 1. Elementary estimates used in this reconstruction

From H05's uniformly differentiable series,

    psi'(z)=sum_(k>=0)(z+k)^-2,
    psi(z+1)-psi(z)=1/z.

For any z>=1, the elementary unit-cell trapezoid identity applied to
f(t)=1/(z+t) gives

    psi(z)=log z-1/(2z)+O(z^-2).                        (4)

Indeed the left sum through K-1 equals its integral from 0 to K plus
`[f(0)-f(K)]/2` and the trapezoid error; that error is bounded by
`(1/8) integral_0^K |f''|=O(z^-2)`. Use
`psi(z)=lim_(K→infinity)[log K-sum_(k<K)1/(z+k)]`, which follows
directly from the harmonic definition. The same argument with
f(t)=(z+t)^-2 yields

    psi'(z)=1/z+1/(2z²)+O(z^-3).                       (5)

All constants here can be chosen independently of z>=1. On the shifted
grid the midpoint rule for t^-2 on [r,infinity) instead gives

    psi'(r+1/2)=1/r+O(r^-3).

For example, the midpoint error on [r+k,r+k+1] is bounded by a constant
times `(r+k)^-4`; summing costs O(r^-3). Thus `u_r=O(r^-2)`.
The function `e(t)=psi(t+1/2)-log t` tends to zero by (4), and its
derivative is O(t^-3) by the same midpoint argument for every real t>=1.
Integration from infinity proves `e_r=O(r^-2)`.

For the endpoint values, the harmonic definition gives

    psi(1/2)=-gamma-2log2,
    psi'(1/2)=4 sum_(j odd>=1)j^-2=pi²/2.               (6)

The first equality follows from the finite expression
`-gamma+2H_K-2H_(2K)`. For the second, the elementary cotangent partial
fraction proved locally in PD-T269 determines `sum j^-2=pi²/6` by
comparison of its linear term with the sine/cosine Taylor expansion;
subtracting the even terms gives (6). No special-function asymptotic
or unread external theorem is used.

## 2. Uniform reduction and the small-r sequence that cannot be dropped

Substitute (4),(5) into (2), while retaining `e_r,u_r` exactly. The result
is the pointwise, uniform inequality

    D=log m+F(x)+e_r-1/[2m(1-x)]-x/(2m)-u_r/(2m)+R,
    |R|<=C*[s^-2+(m*s)^-1+m^-2].                       (7)

To check its coefficient, `psi(s)-psi(m)` contributes
`log(s/m)-1/(2s)+1/(2m)`. The derivative bracket equals
`1+x+u_r+O(1/s+1/m)`, so the scalar 1/(2m) cancels and leaves `-x/(2m)`.

The weight inequalities

    0<w(r/m)<=a*m/r,
    w(r/m)<=C*s/m when r>=m/2

prove directly that `(1/m)sum w*|R|=O(log(m)/m²)`. Split at r=m/2.
On r<=m/2, s>=m/2 and the harmonic weight costs O(log m). On the
other half, the `s^-2` term is at most `C/(m²*s)` after weighting and
normalization. The two remaining terms are bounded by the same order.
This includes both s=1 and r=1.

Let g(x)=w(x)-a/x, g(0)=0. It is smooth on [0,1], with |g(x)|<=C*x.
The summable sequences satisfy

    (1/m)sum_(r<m)w(r/m)e_r=a*S_e+O(log(m)/m²),
    (1/m)sum_(r<m)w(r/m)u_r=a*S_u+O(log(m)/m²),          (8)
    S_e=sum_(r>=1)e_r/r, S_u=sum_(r>=1)u_r/r.

The tails of both series are O(m^-2). The g part is bounded by
`C*m^-2 sum_(r<m)1/r`. Hence the e contribution has NO 1/m term.
By contrast the explicit factor `-u_r/(2m)` in (7) contributes a
nonzero 1/m coefficient and cannot be subsumed into the final error.

Its exact sum follows from the finite recurrence identity

    sum_(r=1)^R psi'(r+1/2)
     =(R+1/2)*psi'(R+1/2)+psi(R+1/2)
                               -psi(1/2)-psi'(1/2)/2.

This is obtained by summing the finite recurrence for psi' and replacing
`k` by `(k+1/2)-1/2` in the resulting triangle. Subtract H_R and let
R tend to infinity, using (4)--(6). One obtains

    S_u=1+2log2-pi²/4,  c1+S_u=2log2.                  (9)

Finally the functions `w/(1-x)-a/x` and `x*w` are smooth on [0,1].
Ordinary trapezoid estimates give

    (1/m)sum w(r/m)/(1-r/m)=a*log m+a*gamma+I1+O(1/m),
    (1/m)sum (r/m)*w(r/m)=I2+O(1/m).                    (10)

In the first formula the a/x part is summed as `a H_(m-1)`; the
remainder has finite endpoint values a and pi/2-a. Only O(1/m) is
needed because (7) multiplies it by 1/m.

## 3. Complete singular quadrature and its uniform remainder

Define

    M_m=(1/m)sum_(r<m)w(r/m)*[log m+F(r/m)],
    R0(x)=w(x)*F(x)-a*(log x+c0)/x.

Near zero, put `J(x)=log(1-x)-psi((1-x)/2)`. It is analytic, with
`J(0)=c0`, `J'(0)=c1`, by (6), and

    R0(x)=a*[J(x)-c0]/x+g(x)*[log x+J(x)].

The first summand is analytic through zero; g=O(x). Consequently

    R0(0)=a*c1,
    R0(x)-R0(0)=O(x*(1+|log x|)),
    R0''(x)=O(1/x) near zero.                          (11)

Near one set y=1-x. The recurrence gives
`psi(y/2)=-2/y+psi(1+y/2)`, with the second term analytic.
Also `w(1-y)=tan(pi*y/2)=pi*y/2+O(y³)`. Thus
`wF` is analytic plus `tan(pi*y/2)*log y`; the explicitly subtracted
term is analytic there. It follows that

    R0(1)=pi-a*c0,
    R0(1-y)-R0(1)=O(y*(1+|log y|)),
    R0''(1-y)=O(1/y) near y=0.                         (12)

These are derivative bounds for actual functions, obtained from
analytic factors; differentiating an unspecified O term is unnecessary.
Compactness on the middle interval now gives a single absolute C with
`|R0''(x)|<=C*(1/x+1/(1-x))` for 0<x<1.

Let h=1/m. On each endpoint cell the difference between the trapezoid
value and its integral is O(h²(1+|log h|)) by (11),(12). On all other
cells the exact trapezoid remainder kernel is bounded by h²/8; hence
the total error is at most

    C*h²*integral_h^(1-h)[1/x+1/(1-x)]dx
       =O(log(m)/m²).

The endpoint-complete result is therefore

    (1/m)sum_(r<m)R0(r/m)
     =integral_0^1 R0-[a*c1+pi-a*c0]/(2m)
                                      +O(log(m)/m²).  (13)

This proof allows logarithmically divergent first derivatives and does
not assume bounded second derivatives at the endpoints.

Two elementary harmonic formulas are

    H_(m-1)=log m+gamma-1/(2m)+O(m^-2),
    sum_(r<m)log(r)/r
      =(log m)²/2+C_L-log(m)/(2m)+O(log(m)/m²).          (14)

The first is PD-T270. For the second, apply the unit-cell trapezoid
formula to `f(t)=log(t)/t` between 1 and m. The accumulated errors
converge to C_L because `f''(t)=(2log t-3)/t³` is integrable at infinity;
their tail is O(log(m)/m²). Since f(1)=0, deleting the endpoint m
contributes exactly `-f(m)/2`, which proves (14).

For g, the smooth trapezoid rule, g(0)=0, g(1)=-a, and
`integral g=a*log(2/pi)` imply

    (1/m)sum w(r/m)
       =a*(log m+gamma+log(2/pi))+O(m^-2).             (15)

Here the 1/m term of `a H_(m-1)` cancels the endpoint correction
`+a/(2m)` of g. Multiplying by log m preserves the required error.

The remaining singular sum is exactly

    a*sum_(r<m)[log r-log m+c0]/r.

Inserting (14), its `log(m)/m` terms cancel and its constant 1/m
coefficient is `-a*c0/2`. Combining this with (13),(15) proves

    M_m=(a/2)*(log m)²+a*c*log m+C_M
                    -[pi+a*c1]/(2m)+O(log(m)/m²).      (16)

This establishes the precise main-sum coefficient independently of
the H01 prose, including its actual uniform remainder.

## 4. Assembly and independent coefficient check

Insert (8)--(10),(16) into (7), then multiply by 2a. The first-order
term is

    -a²*log m
      -a*[pi+a*c1+a*gamma+I1+I2+a*S_u]
     =-a²*log m-2-a²*c0-a*(I1+I2),

using (9). The remaining constant is finite and independent of m; it
may be written `C_H=2a*C_M+2a²*S_e-a²*c²`. This proves exactly (1)
from the named H05 lemma, with no parity restriction or discarded layer.

For completeness, H04's written theorem gives

    4V_n/(nm)=C_B+beta_B/n+O(n^-2),
    beta_B=-a²+2*I_B+a*I2,
    I_B=integral_0^1 x*w(x)*B(x) dx,
    B(x)=cot(pi*x)-a/(2x)+a/[2(1-x)].

Only the constant coefficient beta_B permits replacement of 1/n by
1/m at cost O(m^-2). The logarithmic first coefficient in (1) is
retained with denominator m.

The exact cancellation identity is

    2*I_B-a*I1=a²-1+a²*log(pi/2).                      (17)

To verify it, combine the integrands before integrating. Double-angle
and `w'=-(1+w²)/a` give

    2*x*w*B-a*[w/(1-x)-a/x]
      =x*(w²-1)-2a*w+a²/x
      =-a*(x*w)'-a*(w-a/x)-2x.

This is integrable at both endpoints. Integrating from epsilon to 1
and using `epsilon*w(epsilon)→a` and
`integral_0^1(w-a/x)=a*log(2/pi)` proves (17).

Equation (3), (1) and (17) consequently give

    Lambda_c=A_m²+C
        -[a² log m+1+a²*c]/m+O(log(m)/m²).              (18)

The scalar +2/m in (3) is essential. Accepted PD-T269/270 show
`Lambda_c-A_m²→kappa`, so C=kappa; no new evaluation of kappa is needed.
For N=m-1/2, elementary Taylor bounds for log give

    A_N²=A_m²-[a² log m+a²*c]/m+O(log(m)/m²),
    1/N=1/m+O(m^-2).

Thus (18) implies the original requested sharp expansion from the exact
corner identity and the named H04/H05 supporting theorems. Their written
proofs and the complete mathematical inference are identified above.
Root adoption and the required distinct audit remain separate process
obligations. Both parities are covered because every estimate holds for
every integer m>=3.

## Independent reading, checks and limits

Read complete H04 and H05 final proofs in addition to the accepted
PD-T269/270/271 and F03 starting records. Reconstructed H04's exact
cell union, B derivative bounds, 17/n² error, endpoint correction and
beta_B expression; no mathematical gap found. Reconstructed H05's
series, Taylor sign, 257/(216m²) bound, weighted sum and midpoint
defect kernel; no mathematical gap found. Read H01's complete candidate
proof and identified the missing logarithmic term in its theorem
display. The corrected claim is (1).

PAPERONLY: no scientific executable, import, numerical check, scalar
evaluation, native/compiler run, fitting, quadrature job, external
literature/PDF or subagent occurred. Only repository prose reads/searches
and these owned prose writes were performed. No Git/shared-file changes.

The registered H06 full aggregate route is consolidated into H01 rather
than promoted as an independent novelty result. This verification cannot
replace the repository-required Claude audit; root owns adoption,
registry status, proof integration and the final sharp-target disposition.
