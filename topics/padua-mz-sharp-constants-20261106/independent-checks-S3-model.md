# Supplementary independent check — S3 full signed logarithmic reduction

Date: 2026-11-06. Role: separate Codex mathematical checker; requested
gpt-6-astra high, runtime model metadata not independently exposed.
Rules and source: `2143ad622fa98faf8fe7d5cb8ed2bb7e0062f861`.
This supplements, and does not replace, the required Claude audit.

## Scope and identity

**Verdict: no unresolved mathematical finding in the reviewed scope.**
The frozen theorem establishes the all-polynomial, both-parity form
error 4096, model norm bound 120, and normalized extremal error
4300/log(m). Its proof is uniform across the full grid. The sharp
spectral limits and their parity agreement remain OPEN.

Reviewed in full:

- `theory/S3-full-form-log-model.md`, SHA-256
  `3e1a9a0c8fc7c6878ebe2607d2a3ad491a5147ab1e2de51f2ce30e363ccc60d1`.
- PD-T295, `topics/padua-mz-2d-frontier-20261105/theory/f12-local-weight-asymptotic.md`,
  SHA-256 `0cb69640bb49b5a4f58f9932504479c4982e7e3513db40db8715a1b9832d4703`.
- PD-T377, `topics/padua-mz-cleanup-20261105/theory/odd-weight-asymptotic.md`,
  SHA-256 `20e575241fc36c110d13f3749bf5b3936347b54b373c5a6858cf80d225dff41e`.
- PD-T017, `tracks/mz-constants/theory/m2-cardinal-lower.md`,
  SHA-256 `1c9a3bf5fe8bb9dfbb2943500fb7aafd092eb8a5892c43a2e292f117fabf7776`.
- PD-T014, `tracks/mz-constants/theory/m1-upper-bound.md`,
  SHA-256 `b315927af335c8894afcb588616879fdb7d73ee1da30ad1946baed3c39e3f93a`.
- PD-T379, `topics/padua-mz-cleanup-20261105/theory/growth-carrier-bounds.md`,
  SHA-256 `8f88baa6870fbc00132622fe5b3e2e461bbdf96ff4fffad41b33f288761ff3e7`.

PD-T017/014 were read in the developer's pinned-source copies under
`/tmp/S3-sources/`; the repository-relative names above identify their
durable sources. Also read PD-T013, PD-T022, the original PD-T381 target,
and the topic handoff. The accepted exact signed-weight identity is used
as quoted completely in PD-T295/377; this check does not reopen the
foundational Padua cardinal proof. The scalar rational-carrier
improvement has a separate checker and is outside this report.

This audit concerns mathematical validity and dependencies, not novelty,
priority, or literature coverage. The workflow's exception to reading
the full ideas registry therefore applies. No final numerical slope
fits were read.

## Analytic reconstruction

1. **The strip partition covers the whole omitted triangle.** For
   L=floor(R/2), the strips a<=L and b<=L cannot intersect when a+b>R.
   Each first-strip row has exactly a entries, R-a+1<=b<=R. All other
   entries have a,b>R/2. This includes the R=2 and odd-R boundary cases.

2. **The phase approximation has an explicit moving-index error.** Set
   tau=min(t,pi-t), sigma=min(s,pi-s). Even integer frequencies make
   reflection exact, including frequency 2R. On the first strip,
   b^2-1/4>=3R^2/16 and
   |R^2 t_b+1|<=12a/R. The residual phase product is bounded by
   |cos(2b sigma)-cos(2R sigma)|+|cos(2a tau)-1|
   <=2a(sigma+tau). Thus multiplication by |t_a| and summation over
   the exactly a b-values yields 8+(4/3)R(tau+sigma). No fixed-node
   asymptotic or unquantified uniform limit enters this step.

3. **The logarithm and the middle have bounded residuals.** The exact
   identity -a t_a=1/a+1/[a(4a^2-1)] bounds the correction sum by 1/2.
   R/4<=L<=R/2, including R=2,3, and
   0<=H_L-log L<=1 imply the stated <4 harmonic residual. The two strips
   contribute at most 24+(8/3)R(tau+sigma); the middle contributes at
   most 256/9. Hence their sum is below the claimed
   64+4R(tau+sigma). Signs agree with V_R being subtracted from S_R.

4. **All nontriangle terms and both parities are controlled.** Absolute
   convergence justifies the rectangle-minus-triangle identity. The
   tail bound 1/R and f(t)=pi sin(t) give the stated product, linear,
   and constant terms. At every grid point R tau<=pi d_j/2 and
   R sigma<=pi e_k/2; both coefficients are smaller than 65.
   The exceptional even-m term contributes less than 2 after R^2
   scaling, and the odd-m term vanishes. Multiplying by
   2 epsilon_j eta_k/(m(m+1)) gives the residual coefficient 134.
   Endpoint halfweights and moving far endpoints are retained.

5. **The continuous norm conversion is valid on the full stated space.**
   PD-T017's interior estimate alpha_j>=sin(theta_j)/m and
   sin(theta_j)>=2d_j/m give alpha_j>=(1+d_j)/m^2 for d_j>=1;
   its explicit endpoint weights cover d_j=0. The same proof applies
   to the other mesh. For m=2R, m(m+1)/R^2<=5; for m=2R+1 it is
   <=15/2, with the latter maximum at m=5. The signed residual is
   consequently at most 1005 alpha_j beta_k pointwise. Each coordinate
   degree is <=m-1, so it lies within PD-T014's mesh-m and mesh-(m+1)
   domains. Apply its bound first in x at each y node, sum with positive
   beta_k, then apply it in y for each x and integrate. This gives the
   tensor bound 4||p||^2 without requiring p to factor. Restricting the
   nonnegative majorant to the retained checkerboard is valid. The
   resulting constant is 4020, less than 4096.

6. **The model and spectral constants follow on exactly the same domain.**
   The absolute cosine sum is <=2. Dropping endpoint factors and using
   alpha_j beta_k>=1/[m^2(m+1)^2] yields
   |L_m[p]|<=16m(m+1)R^(-2)||p||^2<=120||p||^2.
   The quadratic-form error holds on every continuous unit vector;
   infimum and supremum therefore give the two separate extremal
   errors. Finally log R>0, m/R<=5/2, and
   4096+120log(5/2)<4300 prove the normalized statement.

Combining this upper control with PD-T379's strictly positive carrier
constants proves eventual two-sided logarithmic orders for both signed
extrema on both parities. Neither that combination nor the finite-family
reduction proves convergence of nu_minus/nu_plus, identifies sharp
constants, or establishes agreement between the parities. The identical
formula template for L_m does not identify its spectra across meshes.

## Independent exact arithmetic diagnostic

The all-m argument above is analytic, with no computational premise.
As a supplementary check of the strip coefficient and finite constants,
the checker independently executed

```text
python topics/padua-mz-sharp-constants-20261106/code/check_S3_model_constants.py
```

Environment: Python 3.12.14; standard-library rational arithmetic;
deterministic, no seed. Checker SHA-256:
`0243a0f7827d5029b9d6eba78a047001e143a17aec369bb7eb13b4c751108a1b`.
The checker covers every first-strip pair for each R=2,...,256 and
both m=2R,2R+1 mesh factors. Execution completed successfully:

```text
strip_coefficient_cases: 707264
R_range: [2, 256]
max_bound_fraction: 195581/399378
form_constant: 4020
norm_constant: 120
```

The fraction is the maximum ratio of the exact coefficient residual to
its proposed 12a/R bound. This finite diagnostic is not a
computer-assisted all-degree proof.

## Residual limits

No unresolved mathematical finding in this scope. The constants are
coarse, and a vanishing normalized error alone supplies no fixed model
operator, spectral compactness theorem, or practical asymptotic scan
window. The theorem's explicit OPEN statements correctly preserve these
limitations. Required Claude audit and campaign-level novelty coverage
remain separate obligations.

## Editorial impact check

After completion the developer removed the future-target OPEN row from
the theorem's proved-result table (retaining all scope limitations) and
replaced its Checks paragraph with a report of this supplementary check.
The resulting theorem SHA-256 is
`8c991ebc077b8f27edaf9baf887c076db7737903f859d5a8de286734d53a2a77`.
The checker reversed precisely those two textual changes in memory and
recovered the originally audited SHA-256 `3e1a9a0c8fc7c6878ebe2607d2a3ad491a5147ab1e2de51f2ce30e363ccc60d1`.
Thus the statement, definitions, proof, and limitations are unchanged;
the scoped mathematical verdict also applies to the updated file.
