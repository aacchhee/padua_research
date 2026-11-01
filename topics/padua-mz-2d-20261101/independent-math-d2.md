# Supplementary peer reconstruction by D2

Date: 2026-11-01. Reconstructor: Codex `/root/d2_upper`, requested
gpt-6.1-sol xhigh. Rules read at
`cf89b140530d5838bdb208a8c28f3e7aa676ace3`; unchanged rules after the
campaign update to `806cc7b4509fd93bae652f9545d32d95529f8281`.

This is the root-assigned analytic peer reconstruction after D2 STOP.
It supplements development and does **not** replace the required Claude
audit, establish developer/auditor independence for the entire campaign,
or approve this reconstructor's own D2 negative results.
No peer proof was edited. No numerical rerun is represented as having
occurred in the checks below.

## Pinned scope checked

| File | SHA-256 at reconstruction |
|---|---|
| `tracks/mz-constants/theory/mz2d-aliasing.md` | `ca22c888e00b46c2caf569dd9221b9c490367a5f16384460b27b111ef3229947` |
| `tracks/mz-constants/theory/mz2d-defect-structure.md` | `25bc96aa605afdfa9e16d6f05baf9a5e44a1800c1b56c0323272d936e2e47eec` |
| `tracks/mz-constants/theory/mz2d-lower-corner-weights.md` | `3c763e54a5758db7f444917c46d07312bc97c411f400b4c85f6a59af7232dc07` |
| `tracks/mz-constants/theory/mz2d-lower-corner-subtraction-obstruction.md` | `b7ebf2023118c2fbd2c492ff6318addee2802a3faad1244caed5db840705fcac` |
| accepted PD-T101 cardinal proof | `ea59aa077a4d021fc69354383f69340f21d17d87d3a28c6ecaaf302cc763612c` |

Read the campaign definitions, full D1/D3 theory files above, and the
accepted PD-T101 proof of its cardinal normalization. A2 is not used.
The complete idea/obstruction screen was already performed for D2;
this supplementary task reconstructs existing claims and generates no
new candidate or priority claim.

## D1 aliases and exactness: reconstructed without a spectral premise

Let `A=F_m(a)`, `B=F_(m+1)(b)`. Standard cosine folding agrees at every
coordinate node. At an even checkerboard node,

`T_(m−A)(x_j) T_(m+1−B)(y_k) = (−1)^(j+k) T_A(x_j) T_B(y_k)`.

The sign is one. The two representative total degrees sum to `2m+1`,
so exactly one is at most `m`. Exactness on that representative yields
the claimed all-degree moment formula. This proof does not require
positivity of the interpolatory weights, a Gram eigenvalue bound, or an
unproved high-degree Lebesgue cubature property.

The degree-`m+1` test `T_(m+1)(y)` has representative `T_m(x)`, so its
quadrature value is `2h_m` instead of `2h_(m+1)`. Consecutive indices
have opposite parity and the even index is positive, so one moment is
zero and the other nonzero, including `m=1`. Exactness degree is
therefore precisely `m`.

Product-to-sum in both coordinates gives the four-term rational pencil.
The repetitions when a basis degree is zero must be retained; they are
retained in the statement. Since the continuous mass is positive
definite, its congruence to the Legendre Gram gives the generalized
spectrum without a sign assumption on the discrete mass.

**Finding:** no mathematical issue found in the pinned alias/exactness
or pencil statements.

## D1 finite-family architecture: boundaries, term count and norm

In the endpoint moment range, simultaneous `a>m` and `b>m+1` would
give `a+b>=2m+3`, impossible. If only x is outside, its fold is
`A=2m−a`; the low branch condition `A+b<=m` becomes `a−b>=m`.
If only y is outside, its fold is `B=2m+2−b`; the low branch condition
becomes `b−a>=m+2`. The complements and central region reproduce all
five active zones in the file with the stated weak/strict boundaries.
No boundary mode is dropped. Subtracting `h_a h_b` gives ten separable
scalar kernels under one coupled half-plane per zone.

For each product choice, a sum coordinate gives a Hankel matrix and
an absolute-difference coordinate splits into two disjoint one-sided
Toeplitz pieces; the zero difference belongs to the weak sector only.
There are at most four coordinate sign sectors, hence at most
`10×4×4=160` terms. Within a sector every half-plane becomes one
condition `r_alpha+s_beta<=c`; each label has absolute value at most
`2n`. Coordinate range restrictions are absorbed into the scalar
sequences. Compression to total degree ensures the moment-range
restriction without a further coupled mask.

The Fourier representation has coefficient

`(2pi)^−1 integral d_F(t) exp(i(r_alpha+s_beta)t) dt`,

which is exactly the desired indicator because the frequencies are
integers. Both diagonal factors in the integral are unitary; they need
not be adjoints of one another for the operator-norm estimate. Repeated
labels have no effect. If the consecutive frequency set has length L,

`|d_F(t)| <= min(L, pi/|t|)` for `0<|t|<=pi`.

Splitting the normalized integral at `pi/L` gives exactly

`pi^−1 [L(pi/L) + integral_(pi/L)^pi pi/t dt] = 1+log L`.

Since `L<=8n+1`, the displayed bound follows. The empty and `n=0`
cases are handled explicitly. The norm metric is correctly identified
as Euclidean Chebyshev coefficients. Nothing in this reconstruction
converts that logarithmic coefficient-space bound into the desired
continuous-mass spectral threshold.

**Finding:** no mathematical issue found within the pinned finite-family
statement. D1 PASS is justified under its stated structural criterion;
the quantitative spectral targets remain separate and OPEN.

## D3 corner weights: independent hand reconstruction

The accepted cardinal identity has factor
`rho_corner=1/[2m(m+1)]` and subtracts exactly the exceptional x mode.
At a corner, surviving even modes all have value one. Consequently its
integral has numerator `sum_(i+j<=r) t_i t_j−2h_m`, with
`t_0=2`, `t_i=−4/(4i²−1)` and `r=floor(m/2)`.
The exceptional x-mode corner value is one whenever its moment is
nonzero, so no parity sign is missing.

The telescoping identity `sum_(j=0)^q t_j=2/(2q+1)` reduces the
triangular sum to

`4/N−8 sum_(i=1)^r [(2i−1)(2i+1)(N−2i)]^−1`,

where `N=2r+1`. Multiplying the proposed partial fractions by the
common denominator gives numerator

`[(N+1)(x+1)−(N−1)(x−1)](N−x)+2(x²−1)`

over `2(N²−1)`. Its numerator is `2(N²−1)`, verifying the identity
exactly. The three reciprocal sums are respectively
`S_r`, `S_r+1/N−1`, and `S_r` (reverse the odd indices for the last).
Their coefficients give

`2S_r/(N²−1)+(N−1)/[2N(N+1)]`.

Substitution produces exactly
`A_r=8/[N(N+1)]−16S_r/(N²−1)`.

For odd `m>=3`, `h_m=0`, and the negative expression follows from
`S_r>=1>(N−1)/(2N)`. For even m, insertion of `N=m+1` and the
exceptional correction gives the three terms displayed in the file.
Replacing `S_r` by one is an upper bound for that numerator. Its strict
negativity for `m>2` reduces to
`16(m²−1)>12m²`, exactly `m²>4`. At `m=2`, equality and `S_1=1`
give zero. As a normalization check, the formula gives `−1/18` at
`m=3` and `−2/225` at `m=4`.

The elementary harmonic relation
`S_r=H_(2r)−H_r/2=(1/2)log m+O(1)` and `N=m+O(1)` give numerator
`−8log(m)/m²+O(m^−2)`. Dividing by `2m(m+1)` yields
`−4log(m)/m⁴+O(m^−4)`, in agreement with both parities and the
claimed sign. This states negativity of the two actual node corners;
it does not classify other nodes.

**Finding:** no mathematical issue found in the pinned finite sum,
normalization, strict sign, or asymptotic statements. This derivation
uses accepted PD-T101 and no audit-pending A2 result.

## D3 continuous-corner subtraction obstruction

At every corner, squared product-Legendre evaluation equals
`(2a+1)(2b+1)/4`. Thus its total-degree evaluation kernel is the
coefficient of `z^(m−1)` in `(1+z)²/[4(1−z)^5]`, namely

`[binom(m+3,4)+2binom(m+2,4)+binom(m+1,4)]/4`
`= m(m+1)(m²+m+1)/24`.

The latter equality follows by expanding the common quartic numerator;
it also gives `1/4` at `m=1` and `7/4` at `m=2`, as the direct small
bases require. A rank-one positive matrix has norm its trace, so the
magnitude of a negative corner form has norm
`(−w_corner) K_corner = (1/6)log m+O(1)`.
The full negative-node form dominates this single positive rank-one
subform. Therefore its norm cannot have an upper bound independent of
m in the continuous metric. This invalidates the fixed-constant premise
of the specified subtraction mechanism; it says nothing by itself
about the signed difference or a positive-node-adapted leverage metric.

**Finding:** no issue found with the exact endpoint kernel, the
logarithmic divergence, or the negative claim's restricted scope.

## D4 additional pinned scope

| File | SHA-256 at reconstruction |
|---|---|
| `tracks/mz-constants/theory/mz2d-fixed-ratio-diamond-reconstruction.md` | `8d517cc6435a7936f4eb3572089e9990659e1a02b560ae602059c394b78ac4d5` |
| `tracks/mz-constants/theory/mz2d-fixed-ratio-rectangular-obstruction.md` | `777046f5b57d853db12e2df8470ba5b14624fbe3eb35f96bc3e6a30b9ca4dfbd` |
| `tracks/mz-constants/theory/mz2d-fixed-ratio-energy-conversion-obstruction.md` | `bcecd47698bea9679f6b734a26f8afb0fd85874a51b414ad75cf9ac650e98903` |

These three D4 files were read in full and reconstructed analytically.
No program was executed for these peer checks.

### Corrected diamond filter

Write scalar filter coefficients as kappa. The simultaneous shifts
`(u,v)->(u+pi,v+pi)` multiply the scalar Fourier pair `(r,k)` by
`(−1)^(r+k)`. Averaging retains equal parity pairs with coefficient
one, rather than introducing an additional factor one half. For every
retained pair the original frequencies are the integers
`a=(r+k)/2,b=(r−k)/2`; the inverse is the unique pair `r=a+b,k=a−b`.
Thus the Fourier coefficient of the projected kernel is exactly
`kappa(a+b) kappa(a−b)`.

The identity `max(|a+b|,|a−b|)=|a|+|b|` gives both the full diamond
plateau through n and zero coefficients outside radius `m−1`.
In particular the half-angle construction is genuinely 2pi-periodic
in each original angle. There is no fractional-frequency ambiguity
left after the parity projection.

The checkerboard character average has exactly the dual lattice union
written in the proof: direct even grid multiples and their translate
by `(m,m+1)`. Its smallest nonzero l1 length is at least `2m`.
An input frequency in radius n and an output filter frequency in radius
`m−1` have difference length at most `n+m−1<=2m−2`, so only the
zero dual-lattice vector survives. Its multiplier is one. This checks
the normalization `1/[2m(m+1)]`, alias exclusion and endpoint plateau
without a norm assumption. At `m=1,n=0`, the filter and input are both
constant, and the normalized average reproduces that constant.
Reflection extension from the physical Padua nodes preserves checkerboard
parity because both angular periods have even integer lengths.

**Finding:** no mathematical issue found in the exact reconstruction
statement at the pinned hash. It asserts reconstruction of general
diamond-supported trigonometric inputs, hence of total-degree algebraic
inputs, but no signed sampling norm inequality. The OPEN fixed-ratio
status and stated missing signed conversion are appropriate.

### Failed rectangular transfer

For `q=cos(t)cos(s)` the four Fourier coefficients are one quarter.
At `v=(1−m,−m)`, only the input `(1,1)` has difference in the
translated checkerboard dual lattice, namely `(m,m+1)`. Neither
of the other first-coordinate differences m or m−2 is a direct
multiple of `2m` for `m>=3`; the translated first coordinate forces
u1=1, and its second-coordinate congruence forces u2=1.
The two boundary filter coefficients are exactly
`1/(m−n)` and `1/(m+1−n)`, even when `n=m−1`.
The spurious coefficient is consequently
`1/[4(m−n)(m+1−n)]`, nonzero and absent in the original input.
The input belongs to total degree n precisely in the claimed range
`n>=2`. The negative statement deliberately leaves n=0,1 and other
filters undecided.

**Finding:** no issue found in the coefficient, normalization or scoped
failure of the specified product-filter operator.

### Signed positive-floor conversion

The m3 cardinal formula is exactly the same cubic independently obtained
in D2 and checked by its four x-level restrictions. Integrating its
Chebyshev expression leaves only `4−8/3−8/3` in the numerator,
and the corner factor `1/24` gives `−1/18`. A strictly positive
reference floor at this node is impossible; arbitrary data supported
there disprove the quadratic-form version. Both formulations are
correctly quantified over arbitrary nodal data, with no claim that
this vector is attained in `Pi_2`. The displayed cardinal polynomial
is in `Pi_3`, as required to identify the weight.

**Finding:** no issue found in the local negative-weight witness or
in the scope of the failed positive-floor conversion. This agrees
with the independently reconstructed D3 all-degree corner formula.

## Supplementary reconstruction outcome

No unresolved mathematical finding was identified in the pinned
D1/D3/D4 statements above. These peer checks do not decide any OPEN
spectral target, approve D2's own work, certify a numerical run, or
replace the required Claude audit. Root retains integration and audit
handoff authority.

