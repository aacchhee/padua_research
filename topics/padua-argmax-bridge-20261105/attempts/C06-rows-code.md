# C06 — validated partial-cotangent backend

Rules/input b6e67b3c78cb668b6d2f9da5a5560537d2960bf3. Assigned technical development; actual serving metadata unexposed. No Git or shared-file ownership. Implements an accepted supporting reduction, with no novelty claim or new mathematical source changes.

## Prospective contract, before code/tests

First freeze ONLY C02 §1–3 partial-cotangent evaluation. Point-S assembly, guarded arc selection, retained/direct C01 primitive diagnostics, and whole-box interfaces remain OPEN and must not be claimed implemented. Inputs: integer n>=2, q>=0 and real ball y with 0<y and y+q-1<n; samples pi(y+i)/n. Empty blocks return zero. Production evaluation must have no q-sized loop except the bounded q<=K harmonic prefix; independent reference may enumerate small blocks. Use Arb 160-bit arithmetic, finite rational tangent/Bernoulli coefficients prepared at higher precision to control cancellation, polynomial moments by fixed-degree recurrence, stable removable residual endpoint evaluation. Include C02 smooth and harmonic errors explicitly as radii in addition to all Arb arithmetic radii. Refuse invalid/nonfinite domains.

Freeze J=48,K=32,Lh=16 initially: the exact C02 formulas M_J and eta=|B_32|/(32*32^32), evaluated outward, select the analytic budget; no empirical parameter fit. The analytic radius returned for each block is 7*q*(pi/n)^4*M_J/5760 + 2*eta/(pi/n) (zero harmonic error where q<=K). No unsupported epsilon. Numerical tightness is measured separately from validity. Compile and all tests together <=180 child/process CPU seconds. Tests initially n<=64, empty/singleton/full/interior blocks, near either pole and exact removable cell endpoints, with independent direct Arb cotangent enclosure and mpmath diagnostics. No full cover, new degree, or production reference fallback.

Expected output: separate source/build/control driver, frozen source and complete toolchain/header/runtime/actually-loaded closures in local raw manifest, compact receipt <16KiB. Kill test: nonfinite valid input, disagreement with independent enclosure, or q-dependent production operation counts beyond K prefix. If stable polynomial endpoint evaluation cannot be made useful at 160 bits, preserve the failed attempt rather than hide it with a degree-growing fallback.

## Conditioning change and frozen implementation contract

The first compiled controls (raw local `c06-rows/check-8kw2wqj9/controls.json`, SHA e8e251e8d306c613c180661ba2de61670d09ab1c1def9ad883e851debd6d8cf9) had 56/56 overlaps but regular-case radius 2.638108271639794e-4. This is a conditioning failure of the direct ball moment recurrence, not a counterexample to C02 or an invalid enclosure. Source `465697bb0721c9ffd7eb130050c4159be25b6f4d82582d1b105fa6c02bc320ad` and raw snapshots remain local. Two early compile failures were missing scalar-rational division and magnitude conversion APIs; corrected without mathematical changes. All development builds and controls consumed <20 CPU seconds cumulatively, below the 180-second allocation.

Before the changed-source controls, the implementation was changed to exact rational moment recurrence at the Arb input midpoint, with rigorous input-radius propagation, as notified to the coordinator. This is coefficient/polynomial preparation in exact arithmetic; elementary function and final interval operations remain Arb160. Coefficients are prepared at Arb640. There is no q-sized polynomial or harmonic-tail loop. Supported machine domain is 2<=n<=2147483647, 0<=q<=n; no 2^64 implementation support is claimed. Invalid, nonpositive-domain, or nonfinite computations return failure. A wide valid input ball can fail the numerical guard and is not a whole-box evaluator.

For normalized sample z_i=(y+i)/n-1/2, all z_i are in (-1/2,1/2). Put s=1/n and normalized cell endpoints zl,zr. Exact moments M_d=sum z_i^d are computed by

    M_0=q,
    M_d=(zr^(d+1)-zl^(d+1))/((d+1)s)
        -sum_(2<=k<=d,k even) binom(d,k)(s/2)^k M_(d-k)/(k+1).

This follows by integrating each centered-cell binomial expansion and summing. All arithmetic in this recurrence at the exact rational midpoint of y is rational, with d<=97. The whole input ball is enclosed by adding d*q*2^(1-d)*rad(y)/n to M_d; this follows from the mean value theorem and |z_i|<=1/2 throughout the input interval. Exact rational bit lengths grow with input magnitude/precision; no constant bit complexity is asserted.

The additional stable residual derivative uses the C02 centered series through WD=96, with radius

    16/(9*pi^2) * 4^(-97) * [195*4/3 + 8/9].

Indeed |b_j|<=4/pi*(3/2)^(-2j-2), |z|<=3/4, and differentiating gives a tail bounded by 16/(9*pi²)*sum_(j>=97)(2j+1)*4^-j; geometric summation is the displayed bound. Both endpoint derivative errors are included in their Arb balls and weighted by h/24. W uses `log(sinc(y)/(pi-y))`, reflecting x to pi-x when the entire ball is above pi/2; this is the same W identity, with its removable value supplied by Arb's entire sinc. No direct subtraction of singular terms occurs.

## Frozen final controls and disposition

Final source SHA `f381738049d793e81a93626bef11eeb1d2a0ff49d0027b6518dd3fec8ff0bcf0`; driver `8a7d48848510915508528a3849fef11f5b01341319ce2103466bdaba608064aa`; API header `b053eafcf79a77ab4d8fd921c8bb1c25a5e4b15312ecdeee0518855579b3771d`. These identities were frozen by the fresh unique-directory build before its controls. Command:

    python topics/padua-argmax-bridge-20261105/code/cheap_rows_C06/control.py

Final actual CPU 2.544674 seconds including compiler and reference work. 56 point inputs at n=2,3,4,8,16,32,64; all 56 production Arb balls CONTAIN the independently evaluated 512-bit direct cotangent reference balls. The reference parses each declared decimal at 512 bits and independently forms pi*(y+i)/n and cot; it is present only in `c06_compare`, never called by `partial`/`c06_partial_arb`. The already-run mpmath100-digit diagnostics also lie within all 56 outward binary64 projections. Three invalid domain inputs are rejected. There were no interval-input controls; whole input-image tightness is not inferred from these point tests.

Maximum regular-input radius is 1.1590152589422934e-24; maximum separate smooth/harmonic/residual-derivative budgets over this control set are respectively 1.1590152553522824e-24, 1.3169120385328504e-38, 2.4499249644762597e-58. The total returned radius already includes those and Arb rounding, coefficient uncertainty and moment input-radius propagation. The small J48 choice targets the explicit ~2^-80 block budget, not 2^-166; J96/K64/L32's C02 all-row theorem is not claimed for this implementation.

At the right pole 1e-30 away, parsing a number near n at 160 bits produces input uncertainty amplified by the cotangent derivative. Maximum absolute radius is 8.92121558024192e14, on a value of order1e31; this conditioned case remains contained and is explicitly NOT an absolute-small-error result. Left-pole cases are separately present. Narrow 512-bit reference containment resolves the earlier 46/56 containment count caused by a wider same-precision independent reference.

Receipt `evidence/c06-rows-partial.json` is <16KiB and pins full local raw manifest `check-g_flhoz0/controls.json`, SHA822287a8f5ab7cdb4084177b396f4a05883e0ded476a0190cf9961faac5f5a4c. Raw manifest pins source/header/driver/builder, preprocessed unit, compiled binary, 179 headers, four compiler tools and13 tool dependencies, eight linked and eight actually mapped runtime dependencies, with loaded identities checked before and after controls. Builder label `round9` is inherited only as a lookup label; the actual recorded source is C06 partial.cpp.

Disposition: developer implementation and bounded MEASURED controls complete for the partial-sum backend; independent review pending. This is not a new mathematical PARTIAL-status claim. The requested complete one-point S evaluator is deferred to C07: guarded arc-to-index conversion, sign/pole/parity branches, retained/direct C01 primitive radii and all-row normalization are entirely OPEN here. Whole-box gradient/corner-orbit/defect interfaces remain OPEN. No full cover, degree extension, scaling law, production completeness or archive transfer is claimed.
