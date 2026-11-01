# PD-T116 — signed Padua MZ at every fixed degree ratio

Provisional alias: `PD-T?mz2d-codex-41`. Final ID assigned at PR preparation, 2026-11-01; required Claude audit PENDING.

ID kind: PD-T. Aliases: D4 target; eta(theta) below one for signed Lebesgue
Padua. Split from: the D4 campaign question. Split into: none. The separate
diamond-reconstruction theorem is a supporting result, not a parameter
case of this target.

## Statement

For every real `0<=theta<1`, find an explicit `eta(theta)<1` such that,
for every integer `m>=1`, integer `0<=n<=theta*m`, and real `p in Pi_n`,

\[
 (1-\eta(\theta))\int_{[-1,1]^2}p^2\,dx\,dy
 \le Q_m(p^2)
 \le(1+\eta(\theta))\int_{[-1,1]^2}p^2\,dx\,dy.      \tag{1}
\]

Alternatively produce a fixed ratio theta<1 and an admitted parameter or
sequence disproving this uniform strong-MZ assertion. No such
counterexample is supplied here.

## Definitions and assumptions

`Q_m` is exactly the campaign's signed interpolatory Lebesgue Padua rule:
even checkerboard, adjacent denominators m,m+1, total-degree-m exactness,
unnormalized measure of mass four. Its weights are not assumed positive.
The definition file fixes the Gram matrix and eta as the symmetric-form
spectral quantities. Inequality (1) requires both a uniformly positive
lower bound and an upper constant strictly below two.

## Status by part

Overall status: **OPEN**. No fixed-ratio spectral bound or counterexample
ratio has been proved by the D4 worker. Half-degree exactness is routine;
it is not a newly split resolved case or a reason to relabel this record
PARTIAL. The successful supporting reconstruction theorem does not
provide either signed spectral endpoint.

| Obligation | Status | Exact remaining gap |
|---|---|---|
| Uniform explicit lower constant for every fixed theta<1 | OPEN | Positive reconstruction energy has not been compared with the signed form on the admissible value space |
| Upper constant <2 for every fixed theta<1 | OPEN | D1 structure is not a mass-normalized sharp estimate; D2 is a separate direction |
| A counterexample ratio, as alternative resolution | OPEN | None established |

## Depends on and completed supporting work

- D1: exact aliases and finite-family operator structure; no spectral
  conclusion imported.
- `PD-T115`: exact parity-projected diamond reconstruction,
  PROVED in development, independent audit pending.
- `PD-N053`: direct rectangular reconstruction is false for
  every `m>=3,2<=n<m`.
- Existing [PD-N045 §3](mz2d-upper-sign-obstruction.md): the m3
  weight -1/18 obstructs positive pointwise conversion, but does not
  obstruct a restricted-degree energy theorem. Historical provisional
  N41 maps to N10; D4's equivalent application is retained as
  [verification only](../../../topics/padua-mz-2d-20261101/directions/d4-positive-floor-verification.md).

## Proof attempts, checks and sources

Three bounded analytic attempts and their prewritten kill tests are
retained in `topics/padua-mz-2d-20261101/ideas-d4.md`. The rectangular
transfer fails in its exact stated scope. The positive-floor transfer
applies the existing N10 §3 obstruction; supplementary Astra's duplicate
finding was accepted and no second negative is allocated. The third
attempt proves the reconstruction identity
and stops at the signed norm comparison. The local one-dimensional M3
proofs were read in full; their positive-weight hypotheses do not transfer.
The campaign primary-source report and MZ literature records were read;
this worker opened no original PDF and makes no historical novelty claim.

No numerical or exact-arithmetic mathematical program, spectrum, finite
exact checker, or independent rerun was executed by this worker. A small
mechanical link-existence check found all eight local Markdown links in
the direction/candidate summaries present. The analytic proofs and retained
positive-floor verification do not rely on the separate finite D0/D6 evidence.

## Scope and resumption criteria

This is an honest stop after the bounded D4 cycle. A successor must supply
a comparison on the restricted Padua sample-value subspace, rather than
assume arbitrary-data positivity. One possible concrete obligation is:
find a positive coercive sampled form S_(m,n) and `r(theta)<1`, explicit
and uniform for `n/m<=theta`, such that the negative nodal contribution
is at most r(theta) times an explicitly controlled positive part. The
resulting bound must be for the actual signed Q_m. The diamond filter's
weighted localization must also be checked in diagonal angles. A positive
reference MZ estimate alone does not meet the resumption condition.

The upper constant below two remains a separate obligation. Do not combine
a lower-only estimate with an unspecified finite upper norm to claim eta<1.
Finite examples for increasing m do not prove the uniform quantifier in
(1). Any future computer-assisted resolution needs a proved reduction,
exact arithmetic, essential code/evidence and an actual independent rerun.

## History

2026-11-01, Codex `/root/d4_ratio`, requested gpt-6.1-sol xhigh, rules read
at supplied main `806cc7b4509fd93bae652f9545d32d95529f8281`. D1 PASS was
received before development. No Git mutation, shared-registry edit,
manuscript change or ultra allocation. Original target wording and its
OPEN scope are preserved.

Supplementary Astra response: the former proposed D4 negative N41
duplicates existing N10 §3 and is consolidated there. Its application,
original proof bytes and historical alias are retained in the topic
verification archive. The diamond theorem and rectangular obstruction
are unchanged; the fixed-ratio target remains OPEN.
