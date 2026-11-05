# G1 fitting and universal-interval gate: implementation specification

Rules read at `bb67c1ee830d468fa33007e15008d5574d00ccf4`; Codex,
requested `gpt-6.1-sol` xhigh. This is a routine analytic specification of
the **unchanged** G1 preregistration in [attempts/L1.md](attempts/L1.md),
read in full together with [g1-methods.md](g1-methods.md). It introduces no
new scientific mechanism, threshold, fit or growth claim. No code or fit
was executed for this document. Implementation and distinct execution
remain due.

Status: prospective implementation specification; independent analytic
review requested. No fit result or executed interval algorithm is asserted.

## Entry gate and exact inputs

**Do not compute fits, diagnostic slopes, holdout SSEs or a trend verdict
until all152 required rows exist:** both frozen grids, all four rules,
every integer degree2–20. A row is complete only after every source in its
declared prefix was processed. Duplicates, partial-source stages or capped
cases do not fill missing rows. Preserve exact pivot/X-tie conventions,
all-source metric and original overlap checks. Mathematical acceptance
also requires the separately assigned independent endpoint checks; a
producer-only fit is not an accepted G1 gate result. No fit on the currently
incomplete scan is authorized by this specification.

For each row use the positive exact rational quantities
`L_r(s)^2`, `H_r(s)^2`, `Urow_r(s)^2`, and
`U_r(s)^2=min(H_r(s)^2,Urow_r(s)^2)`. Verify their input hashes, grid/rule/
degree coverage, source coverage and `0<L_r(s)^2<=U_r(s)^2<infinity`.
If positivity or another input prerequisite fails, STOP fitting and
diagnose; do not insert a floor, omit a degree or silently regularize logs.
These endpoints enclose the aggregate spectral condition `K_r(s)` of
PD-T137, not the scalar model of L4.

For each degree define the positive rational ratios

```
q_s^- = L_BJ(s)^2 / min_(c in {mirror,alt,pivot}) U_c(s)^2,
q_s^+ = U_BJ(s)^2 / min_(c in {mirror,alt,pivot}) L_c(s)^2,
a_s = (1/2) log q_s^-,       b_s = (1/2) log q_s^+.       (1)
```

Then the exact log condition ratio lies in `[a_s,b_s]`. Take the minimum
over the three comparators separately at each degree and at each endpoint;
the lower/upper winners can differ. A ratio of two lower condition bounds
is not a ratio certificate. Check `q_s^-<=q_s^+` exactly. Logs are natural;
the one-half in (1) is essential because the supplied endpoints are squared
conditions. The log interval can contain negative values or zero. Do not
square its endpoints as if that were a monotone operation.

The preregistered ordinate domain is the entire product
`mathcal B=product_(s=2)^20 [a_s,b_s]`: choices at different degrees are
independent for this universal test. Do not narrow it using apparent
smoothness, monotonicity, a fixed comparator winner or either fitted model.

## Outward logarithms without an unverified floating conversion

A directed-rounding MPFR/Arb implementation with checked rational input
enclosures is sufficient. The following exact-rational alternative gives a
complete specification of the required enclosure, including negative logs.
For a positive rational `q`, choose the integer `k` by integer comparisons
so `t=q/2^k` is in `[1,2)`. Enclose `t` between dyadic rationals
`t^-<=t<=t^+` in `[1,2]`, using exact integer floor/ceiling division. This
initial dyadic enclosure avoids taking many powers of a potentially huge
input numerator/denominator.

For `v` in `[1,2]`, let `z=(v-1)/(v+1)` in `[0,1/3]`. With `m>=1`,

```
S_m(z)=2 sum_(j=0)^(m-1) z^(2j+1)/(2j+1),
0 <= log(v)-S_m(z)
   <= R_m(z)=2 z^(2m+1)/[(2m+1)(1-z^2)].                 (2)
```

This follows by bounding the positive tail of the atanh series by a
geometric series. Use `S_m(z(t^-))` as a lower bound for `log t`, and
`S_m(z(t^+))+R_m(z(t^+))` as an upper bound. The same formula at `z=1/3`
encloses `log2`. Combine `k[log2]+[log t]` with interval arithmetic;
**negative k reverses the endpoints** of its multiplied interval.
Refine mantissa enclosure and series length until the resulting interval
width is at most `2^(-p)`. In particular, allocate the log2 error after
multiplication by `|k|`; a fixed unscaled log2 tolerance is insufficient.
Handle `q=1` exactly as `[0,0]`.

All operations can use exact rationals followed by dyadic outward rounding.
For example, rounding a rational to multiples of `2^(-p)` uses exact
integer floor/ceiling, including for negative values. No binary64 log or
unchecked nearest-rounded rational-to-float conversion is a certificate.
The construction also encloses the fixed predictors `log(s+1)`.

## OLS and descriptive endpoint/midpoint reports

For a degree set `T`, predictors `x_t` and ordinates `y_t`, put

```
m=|T|, xbar=(sum_T x_t)/m, ybar=(sum_T y_t)/m,
D_T=sum_T (x_t-xbar)^2,
slope=sum_T (x_t-xbar)y_t / D_T,
intercept=ybar-slope*xbar.                              (3)
```

The predictors are `x_t=t` for the exponential model and `x_t=log(t+1)`
for the polynomial model. The labels mean linear models for **log**
ordinates; they do not impose a positive fitted exponent. Distinct fixed
predictors give `D_T>0`. If an outward denominator enclosure contains zero,
increase log precision within the schedule below until its lower endpoint
is positive; do not divide through zero or perturb the data. An unresolved
denominator guard at the precision cap leaves the calculation unaccepted,
with an arithmetic/guard INCONCLUSIVE outcome. For `x_t=t`, the weights in (3) are exact
rationals and can be precomputed exactly.

For each of the eight grid/rule combinations, fit both models over **all
degrees2–20**, separately to these three exactly defined ordinate curves:

```
ell_s=(1/2)log L_r(s)^2,
u_s=(1/2)log U_r(s)^2,
mid_s=(ell_s+u_s)/2.                                    (4)
```

Report outward intervals for each fit's intercept and slope. The lower-
endpoint curve's regression is not a lower bound on every possible
regression coefficient: OLS weights have both signs. The same caution
applies to upper-endpoint fits. Midpoints in (4) are midpoints of the true
log endpoints, not a rounded surrogate with unreported error. Arithmetic
enclosures can certify these descriptive fit calculations; they do not
identify the unknown true condition curve or establish an asymptotic rate.

For each grid also report lower-endpoint (`y=a`), upper-endpoint (`y=b`)
and midpoint (`y=(a+b)/2`) diagnostics for the log-ratio gate below.
Midpoint trend diagnostics retain the preregistered **MEASURED,
descriptive** label. Their passing does not trigger the interval gate.

## Exact form of the saved universal kill predicate

For log-ratio ordinates `y=(y_2,...,y_20)` in `mathcal B`, use
`T={2,...,14}` for model fitting and `V={15,...,20}` for prediction errors.
For either predictor family `j in {E,P}`, its heldout prediction is

```
yhat_h^j=sum_(t in T) w_ht^j y_t,
w_ht^j=1/13+(x_h^j-xbar_T^j)(x_t^j-xbar_T^j)/D_T^j,
SSE_j(y)=sum_(h in V) (y_h-yhat_h^j)^2.                  (5)
```

Thus SSE means squared **log-ordinate prediction errors on15–20**, after
training only on2–14. Do not compare training SSE, refit on holdout data,
exponentiate predictions before taking residuals, or compare relative/raw
condition errors. When interval-squaring a residual `[l,u]`, use lower
zero if it straddles zero, otherwise `min(l^2,u^2)`; the upper endpoint is
`max(l^2,u^2)`.

Let `B_early` be the linear slope on2–10 and `B_late` on11–20. The original
two conditions, including the phrase **early positive linear slope**, are
precisely the following universal predicate:

```
for every y in mathcal B:
    2*SSE_P(y)-SSE_E(y) <= 0,
    B_early(y) > 0,
    B_late(y)-(1/2)B_early(y) <= 0.                       (6)
```

The latter two inequalities constitute the saved late-versus-early
condition. Positivity of the early slope must hold for every admissible
ordinate vector, not just the midpoint. A negative late slope is allowed;
there is no additional slope threshold. Use the SSE difference in (6),
not division by `SSE_E`: if both SSEs are zero their inequality is true.
There is no special positive-SSE assumption.

## Cheap exact decisions for the two slope clauses

The exact slope coefficient vectors are

```
e_s=(s-6)/60                 for2<=s<=10, else0,
l_s=(2s-31)/165              for11<=s<=20, else0,
g_s=l_s-e_s/2.
```

For the minimum of `e^T y` over `mathcal B`, choose `y_s=a_s` when
`e_s>0` and `y_s=b_s` when `e_s<0`; zero-coefficient coordinates can use
their midpoint. For the maximum of `g^T y`, choose `b_s` when `g_s>0` and
`a_s` when `g_s<0`. These corners are explicit admissible witnesses if
the respective clauses fail.

These two extrema have an exact rational-product sign test, so no
transcendental equality ambiguity is needed. Each used endpoint has form
`(1/2)log q_s`, with `q_s` selected from (1). For rational weights `c_s`
and a positive common denominator `D` with `m_s=D c_s` integral,

```
2D sum_s c_s y_s = log product_s q_s^(m_s).               (7)
```

Compare that positive rational product with1 by exact integer arithmetic.
For the early minimum take `D=60`, `m_s=s-6` on2–10. For the late-minus-
half-early maximum take `D=1320`, giving
`m_s=-11(s-6)` on2–10 and `m_s=8(2s-31)` on11–20.
Zero coefficients contribute nothing. Negative exponents invert their
rational bases. Log enclosures usually decide the sign cheaply first;
exact product comparison supplies a fallback and equality decision.

The early clause holds iff its product is **strictly greater than1**;
equality fails it. The late-minus-half-early clause holds iff its product
is **at most1**; equality passes it. A failing corner proves that the
unchanged universal predicate is false and certifies an interval-based
**INCONCLUSIVE** verdict, not a kill. Store the endpoint choices and
product comparison recipe; do not commit a giant expanded product.

## SSE quadratic and a rigorous finite interval algorithm

For each family form its six-by-nineteen residual matrix `M_j`: row `h`
has `-w_ht^j` in training positions and1 at position `h` in the holdout.
Then define the symmetric matrix

```
Q_j=M_j^T M_j,
Q=2Q_P-Q_E,
q(y)=y^T Q y=2*SSE_P(y)-SSE_E(y).                         (8)
```

Compute outward coefficient enclosures from (2)–(5), retaining symmetry.
`Q_E,Q_P` are positive semidefinite individually, but their difference
need not be. Checking endpoint fits or the corners of `mathcal B` does
not prove `q<=0` throughout it. Do not assume convexity or replace the
universal predicate by a midpoint or vertex test.

Use parameters `tau_s in[0,1]` and the exact map
`y_s(tau)=(1-tau_s)a_s+tau_s b_s`. This covers the original box, including
zero-width coordinates. A stored rational nineteen-vector tau therefore
specifies an admissible ordinate vector without relying on numerical
membership tests. Outward evaluation of this exact expression encloses
the chosen vector even if the log endpoint enclosures overlap.

First try five deterministic witness vectors: all tau=0, all tau=1/2,
all tau=1, the early-minimizing corner, and the late-minus-half-early-
maximizing corner. The zero-weight coordinates of those corners use1/2.
If any vector has a certified positive lower bound for `q`, it is an
explicit counterchoice to (6). It certifies INCONCLUSIVE. The exact slope
corner tests can of course finish the gate decision earlier. The prescribed
descriptive fit reports still remain due, or must be explicitly listed as
pending. Witnesses are verification of
the saved domain, not new data, degrees or scientific fit variants.

If all slope clauses pass but no SSE counterchoice is found, cover the
tau cube by rational boxes. For a tau box `[t^-,t^+]`, monotonicity from
`a_s<=b_s` gives an outward ordinate box `Y` by evaluating
`(1-t_s^-)a_s+t_s^- b_s` for its lower endpoint and
`(1-t_s^+)a_s+t_s^+ b_s` for its upper endpoint. This may overenclose the
true image, which is conservative. Write its rational center as `m` and
halfwidths as `r_s`. An explicit valid quadratic upper bound is

```
UB = upper(m^T Q m)
     +2 sum_s abs_upper((Qm)_s) r_s
     +sum_s max(0, upper(Q_ss)) r_s^2
     +2 sum_(s<t) abs_upper(Q_st) r_s r_t.                (9)
```

Here `abs_upper([l,u])=max(|l|,|u|)`; all coefficients are outward
enclosures. Expanding `q(m+z)` and using `|z_s|<=r_s` proves (9).
The upper endpoint of a direct interval evaluation of (8) on `Y` is also
valid; take the minimum of the two upper bounds if useful.

If `UB<=0`, mark the box certified. Otherwise test its rational tau center
as a potential strict SSE counterchoice; a certified positive `q` ends
with INCONCLUSIVE. If neither works, bisect one tau coordinate at its
rational midpoint. Choose the largest current ordinate-width upper bound
times tau width, breaking ties by smallest degree. Retain both children;
their union must exactly cover their parent. A finite all-certified leaf
cover, together with the two exact slope passes, proves (6) for every
admissible ordinate vector and yields **KILL under the frozen finite
operational rule**.

For a concrete bounded implementation, use log/arithmetic precision
128, then256, then512 fractional binary bits, with at most4096 processed
boxes per grid per precision, including the root. Restart the covering
calculation at a higher precision if necessary; keep any already certified
counterchoice. Use dyadic outward rounding after operations to control
integer sizes. These are verification resource caps, not changes to the
training set, holdout set, universal domain or scientific thresholds.
Record the exact schedule before execution. Any later increased resource
allocation must be dated and retain earlier results.

The bounded procedure always terminates. It returns one of:

- **KILL, certified universal:** both slope extrema passed and a finite
  covering certificate proves `q<=0` everywhere.
- **INCONCLUSIVE, certified counterchoice:** a stored admissible tau vector
  violates at least one clause, including the exact early-slope equality
  case. This proves that the universal kill predicate fails.
- **INCONCLUSIVE, not certified within budget:** neither universal proof
  nor a violating vector was certified. Do not call this a counterexample
  or claim the universal predicate false. Equality/tangency boundaries
  and interval overestimation may cause this outcome.

No complete exact decision procedure for arbitrary transcendental boundary
equalities is claimed. Finite interval verification is sufficient for an
accepted universal KILL or a certified counterchoice; resource exhaustion
never becomes a kill or a scientific asymptotic conclusion.

## Receipt, independent check and interpretation

The small receipt must pin all152 endpoint inputs/coverage, source/grid/
rule/tie identities, code versions, precision/caps and exact comparator
minima. Report endpoint/midpoint descriptive parameters and log-ratio
holdout/early/late diagnostics separately from each grid's universal
verdict. Include the three universal clauses' statuses and distinguish
arithmetic uncertainty from a certified counterchoice.

For a counterchoice, store its nineteen rational tau coordinates, the
violated clause, strict signed outward margin or exact rational-product
comparison, and the recipes/hashes needed to recheck from original rational
endpoints. For a universal result, retain the complete rational split/leaf
cover and outward bounds. Put a large regenerable tree/report outside Git
with a compact manifest and exact regeneration command; do not split a
large generated artifact merely to evade size limits.

A distinct checker must independently construct the OLS prediction weights,
slope extrema and gate expressions from the complete exact inputs, verify
outward logarithms, recheck the stored witness or full covering certificate,
and actually execute. Reusing only the producer's final Boolean or rounded
fit parameters is insufficient. This specification is analytic preparation,
not evidence that either implementation or execution has occurred.

Each grid has its own verdict. A KILL rejects only continuing exponential-
separation development on that frozen grid under the saved operational
rule. A certified counterchoice means only that this universal interval
rule cannot kill there; it need not show exponential behavior of the true
conditions. A positive finite fitted slope proves no rate. No finite fit
settles subexponential asymptotics, the SH_n theorem, every-rule stability
or actual IEEE activation. Required later scientific/protocol audit remains
separate.
