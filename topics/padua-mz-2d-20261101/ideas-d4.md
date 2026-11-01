# D4 fixed-ratio candidates and bounded work record

Rules/base read: `806cc7b4509fd93bae652f9545d32d95529f8281` (the three
rule files are unchanged from the campaign's recorded `cf89b140...`).
Developer: Codex `/root/d4_ratio`, requested `gpt-6.1-sol` xhigh; resolved
runtime model/effort metadata is not independently exposed. No Git authority.
D1's structural PASS activates this direction. Target: every fixed
`0<=theta<1`, an explicit `eta(theta)<1` for the actual signed Lebesgue
Padua form and every integer `n<=theta*m`.

## Relaxed novelty gate

Read the campaign LOG, handoff, conventions and full D1 proof; all four M3
theory files and their candidate/run records; M1's exact CC foundation;
PD-T021/028 and the Padua foundation candidate. Inspected the complete
`state/IDEAS.md` headings, identifiers, aliases and summaries, including
every canonical/historical/seed/current MZ, lattice, programme and
bivariate-Lanczos obstruction and disposition table. Accessed
`literature/INDEX.md`, scanned its source/identifier headings and read its
MZ/Padua-relevant rows. Read the campaign primary-source report and the
shortlisted classical-MZ/mean-convergence records, with their stated
reading limits. The searches included `Fejer`, `Fejér`, `Vallée`, `filter`,
`Schur`, `oversampling`, `fixed ratio`, `checkerboard`, `signed`,
`positive`, `weight`, `alias` and `tensor` across state, track theory,
topic records and MZ literature. Tool-output truncation was followed by
smaller reads of the registry sections; no primary PDF was opened by this
worker. No historical novelty claim is made.

Closest entries: IDEA-055/056/072--076; PD-T022--024; D1's complementary
mode formula; and D2's current tensor-weight/Schur candidates. The important
obstructions are signed weights, one-sided marginal compression, the
difference between a positive sampling norm and the signed form, and the
need to bound both spectral endpoints. The one-dimensional lower proof's
exact-reconstruction step and positive-weight-conversion step must be
tested separately. Half-degree exactness alone does not close D4.

## IDEA-224 — rectangular Fejér reconstruction on the checkerboard

Aliases: direct tensor M3 filter; rectangular oversampled convolution.

- Question / scope: does the product of the two one-dimensional M3
  plateau kernels reconstruct every total-degree-`n` polynomial from the
  even checkerboard, when `2<=n<m`?
- Mechanism and hypotheses: extend angular samples to the full periodic
  checkerboard; use cutoffs `m-1` and `m`, plateaus through `n`, and the
  normalized checkerboard average.
- Closest entries read in full: IDEA-074/PD-T023 and D1's alias proof.
- Separation criterion: the tensor filter would remain exactly alias free
  on the checkerboard. A nonzero output Fourier coefficient outside the
  input's frequency support kills this direct transfer.
- Literature baseline: classical tensor filtered convolution; the only
  proposed change is the checkerboard sampling lattice. No priority claim.
- Obstructions escaped or retained: a full rectangular grid has a different
  annihilator; complementary checkerboard frequencies are retained here.
- Novelty verdict: variant with a testable sampling-lattice difference.
- Cheapest decisive test: apply the operator to `q(t,s)=cos(t)cos(s)` and
  inspect the complementary Fourier mode `(1-m,-m)`.
- Kill criterion, recorded before the formal test: any nonzero coefficient
  at that absent mode rejects exact reconstruction, for the parameter range
  where its two scalar filter coefficients are nonzero.
- Test discriminability: a coefficient identity can settle this exact
  operator claim for all indicated parameters; it does not refute a
  different filter or the signed MZ target.
- Actual test results: analytic coefficient identity gives the absent-mode
  output `1/[4(m-n)(m+1-n)]>0` for every `m>=3,2<=n<m`.
- Disposition: **REJECTED: failed**, exactly for the specified rectangular
  operator. Diamond filters and the signed spectral target are not rejected.
- Canonical negative/theory record: `PD-N053`,
  `tracks/mz-constants/theory/mz2d-fixed-ratio-rectangular-obstruction.md`,
  **PROVED** in development, independent audit pending.

## IDEA-225 — direct positive-energy conversion after Schur

Aliases: signed M3 last-step transfer; pointwise Padua sampling floor.

- Question / scope: can the M3 positive angular sampled energy be converted
  to signed Padua energy by a pointwise positive nodal lower bound?
- Mechanism and hypotheses: require `w_jk >= c_m v_jk` on all retained
  nodes, with `c_m>0` and reference weights `v_jk>0`; the regularized
  product angular weights are one such reference.
- Closest entries read in full: IDEA-074, IDEA-056, PD-T023 and the campaign
  source formulas. Supplementary review identified existing D2
  `PD-N045` §3 as the same negative-weight/arbitrary-data
  obstruction; that full record has now been read for consolidation.
- Separation criterion: actual signed weights would admit the required
  positive floor. A negative retained weight kills this pointwise step.
- Literature baseline: positive CC weights are an explicit assumption in
  M3; signed Padua weights have never been interchangeable with them.
- Applicable obstruction: the signed form is not an arbitrary-data norm.
  Negative weights alone do not refute coercivity on `Pi_(m-1)`.
- Novelty verdict: **equivalent known obstruction applied to D4**. The
  original proposed distinction from positive CC filtering does not
  distinguish this negative statement from D2's existing §3.
- Cheapest decisive test: derive the weight of `(1,1)` at `m=3` from the
  integrated cardinal formula.
- Kill criterion, recorded before the formal test: a strictly negative
  weight rejects every strictly positive pointwise comparison at that m.
- Test discriminability: exact weight arithmetic settles only this proof
  step; low-degree value vectors satisfy constraints and are not arbitrary.
- Actual test results: explicit degree-three cardinal polynomial, checked
  at all ten nodes, integrates to `w_(1,1)=-1/18` at m=3. Thus every
  strictly positive pointwise floor fails. D3 independently develops the
  stronger all-m corner formula; that is unnecessary for this obstruction.
- Disposition: **equivalent**, with the attempted positive-floor transfer
  **failed** in its pointwise/arbitrary-data scope. The allowed value
  subspace of `Pi_(m-1)` is not arbitrary. Retained as an application and
  verification; no duplicate mechanism is pursued or negative allocated.
- Canonical negative/theory record: existing `PD-N045` §3,
  [theory](../../tracks/mz-constants/theory/mz2d-upper-sign-obstruction.md).
  Historical provisional `PD-N045` is an alias mapped to N10,
  for root's crosswalk. D4's original proof bytes and history are retained
  in the [verification-only archive](directions/d4-positive-floor-verification.md).
  This consolidation accepts the supplementary Astra finding.

## IDEA-226 — diamond plateau filter in diagonal angles

Aliases: rotated tensor filter; total-degree checkerboard reconstruction.

- Question / scope: construct an exactly reproducing filter for every
  `0<=n<m` whose frequency support lies in the total-degree diamond.
- Mechanism and hypotheses: transform frequencies by `(a,b)->(a+b,a-b)`;
  enforce same parity and apply a scalar plateau filter in both transformed
  frequencies. Checkerboard alias vectors have l1 length at least `2m`.
- Closest entries read in full: IDEA-074, D1 and candidate 40 above.
- Separation criterion: the corrected filter's support is a diamond,
  rather than candidate 40's rectangle; exact reproduction must follow
  from the shortest nonzero alias vector. A surviving alias or a wrong
  Fourier multiplier at the plateau boundary kills the construction.
- Literature baseline: rotated-square/diamond Fourier summation is
  classical context; only an independently checked application is claimed.
- Applicable obstructions: this may repair aliasing but does not repair
  signed-energy conversion, nor does exact reproduction alone give eta<1.
- Novelty verdict: variant with an explicit geometric difference.
- Cheapest decisive test: compute all Fourier coefficients symbolically,
  check the plateau at total degree n, and compare `n+m-1` with `2m`.
- Kill criterion, recorded before formal proof: coefficient different from
  one on the plateau, nonintegral frequencies after parity projection, or
  a nonzero checkerboard alias with l1 length <=`n+m-1` kills it.
- Test discriminability: a finite-symbol Fourier argument is universal;
  it makes no assertion about the signed quadratic form.
- Actual test results: the kernel has coefficient
  `kappa(a+b)kappa(a-b)`, one on the n-diamond and zero outside the
  (m-1)-diamond. Every nonzero checkerboard alias has l1 length >=2m,
  whereas an input/output difference has length <=n+m-1<=2m-2. This
  proves exact reconstruction including n=0,m=1.
- Disposition: exact reconstruction **retained**, signed weighted-Schur
  completion **deferred**. No signed form comparison or upper <2 follows
  from the reconstruction. Resumption requires a uniform restricted-value
  comparison controlling the negative nodal part, and compatible weighted
  localization estimates in the diagonal angles; a general bound on a
  positive reference norm alone does not meet that condition.
- Canonical theory: `PD-T115`,
  `tracks/mz-constants/theory/mz2d-fixed-ratio-diamond-reconstruction.md`,
  **PROVED** in development, independent audit pending.

## Bounded-round disposition

| Round | Cheapest decisive test | Outcome |
|---|---|---|
| 1 | Rectangular filter's coefficient at `(1-m,-m)` on input xy | Failed for every `m>=3,2<=n<m`; scoped negative retained |
| 2 | Positive pointwise floor at the m3 node corner | Existing N10 §3 obstruction applied: failed step, equivalent candidate retained; no second PD-N |
| 3 | Parity-projected diamond filter's plateau and shortest alias | Exact reconstruction proved; signed coercivity comparison still missing |

D4 is **STOPPED / OPEN** after these three bounded attempts. Neither
an explicit eta(theta)<1 for every theta<1 nor a counterexample ratio has
been obtained. The exact half-degree case is routine and is not promoted
to PARTIAL status for the original target. The diamond theorem is a
supporting result, not a resolved parameter case. No further mathematical
direction or speculative candidate was opened. No ultra allocation.

Root assigned supplementary analytic reconstruction to the separate D2
developer after that developer stopped its own direction. The completed
[peer record](independent-math-d2.md) was received and read in full: no
mathematical issue found in all three D4 proofs, with independent hand
derivations of parity, frequency cutoff, character normalization,
spurious coefficient and the m3 corner cubic/integral. Pinned SHA-256
values: diamond `8d517cc6435a7936f4eb3572089e9990659e1a02b560ae602059c394b78ac4d5`,
rectangle `777046f5b57d853db12e2df8470ba5b14624fbe3eb35f96bc3e6a30b9ca4dfbd`,
conversion `bcecd47698bea9679f6b734a26f8afb0fd85874a51b414ad75cf9ac650e98903`.
These are analytic peer checks, not executed program reruns or the
required Claude audit. Diamond and rectangle proof bytes remain at their
pinned hashes. The conversion hash is historical: supplementary Astra
identified the duplicate negative; the exact original body is preserved
in the verification-only archive at byte offset 2255, length 4450, with
its old N41 alias mapped to canonical N10 §3.

## Runs needed

No numerical or exact-arithmetic program has been executed by this worker.
The three first tests above are analytic. Do not run expensive spectra to
replace any failed exact-reproduction or signed-energy obligation.
