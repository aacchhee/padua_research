# PD-T381 — sharp logarithmic Padua spectral limits

ID kind: PD-T.
Aliases: sharp signed extremal growth coefficients; existence and values
of the endpoint logarithmic limits.
Split from: the original C3 target in handoff 01, preserved here explicitly.
Split into: [PD-T534](../../padua-mz-sharp-constants-20261106/theory/S3-full-form-log-model.md), [PD-T535](../../padua-mz-sharp-constants-20261106/theory/S3-corner-kernel-hard.md), [PD-T536](../../padua-mz-sharp-constants-20261106/theory/S3-corner-operator-limit.md) establish existence, parity agreement and exact operator characterization; decimal values remain OPEN. [PD-T379](growth-carrier-bounds.md) records separate supporting packet bounds.

## Original target and statement

For the actual signed Lebesgue Padua rule of the frozen definitions,
determine whether the two limits

    lim_(m->infinity) lambda_-(m,m-1)/log m,
    lim_(m->infinity) lambda_+(m,m-1)/log m

exist, and determine their values if they do. The original handoff first
asked this on even m and then on odd m after C2. Both parity questions
and their agreement, if each converges, remain part of the target; the
all-integer formulation does not silently remove either obligation.

## Definitions and assumptions

Integer m>=2; the unchanged even-checkerboard signed interpolatory
Lebesgue rule; continuous unnormalized dxdy of mass four; total-degree
space Pi_(m-1); lambda_-/lambda_+ are the continuous-normalized variational
extrema, as defined in the original 2D topic. No fitted coefficient or
packet normalization is assumed to equal an extremal limit.

## Status by part

Overall status: **PARTIAL**.

| Mathematical part of the original target | Status | Split result / remaining gap |
|---|---|---|
| Both even/odd logarithmic limits exist | PROVED | [PD-T536](../../padua-mz-sharp-constants-20261106/theory/S3-corner-operator-limit.md), using [PD-T534](../../padua-mz-sharp-constants-20261106/theory/S3-full-form-log-model.md), [PD-T535](../../padua-mz-sharp-constants-20261106/theory/S3-corner-kernel-hard.md) |
| Parity limits agree, giving full-integer limits | PROVED | [PD-T536](../../padua-mz-sharp-constants-20261106/theory/S3-corner-operator-limit.md) |
| Exact characterization as c_minus=inf spectrum(B), c_plus=sup spectrum(B) | PROVED | [PD-T536](../../padua-mz-sharp-constants-20261106/theory/S3-corner-operator-limit.md); explicit kernel and spectral properties in [PD-T539](../../padua-mz-sharp-constants-20261106/theory/P1-elliptic-kernel.md), [PD-T540](../../padua-mz-sharp-constants-20261106/theory/P1-positive-spectrum.md) |
| Decimal values of c_minus and c_plus | OPEN | [PD-T541](../../padua-mz-sharp-constants-20261106/theory/P1-rectangle-certificate.md), [PD-T542](../../padua-mz-sharp-constants-20261106/theory/P1-numeric-certificate.md) give only a coarse enclosure, with no useful digits |

The one-sided PD-T379 packet bounds remain supporting results, not the conjuncts that justify PARTIAL.

## Dependencies and existing support

[PD-T534](../../padua-mz-sharp-constants-20261106/theory/S3-full-form-log-model.md), [PD-T535](../../padua-mz-sharp-constants-20261106/theory/S3-corner-kernel-hard.md), [PD-T536](../../padua-mz-sharp-constants-20261106/theory/S3-corner-operator-limit.md) establish the convergence and parity assertions. [PD-T539](../../padua-mz-sharp-constants-20261106/theory/P1-elliptic-kernel.md), [PD-T540](../../padua-mz-sharp-constants-20261106/theory/P1-positive-spectrum.md), [PD-T541](../../padua-mz-sharp-constants-20261106/theory/P1-rectangle-certificate.md), [PD-T542](../../padua-mz-sharp-constants-20261106/theory/P1-numeric-certificate.md) give the explicit kernel, spectral structure and coarse certificate. PD-N105/106/107, PD-T378 and PD-T379 retain their separate divergence and supporting bounds. PD-T380 and [PD-T538](../../padua-mz-sharp-constants-20261106/theory/S3-measured.md), [PD-T543](../../padua-mz-sharp-constants-20261106/theory/P2-measurements.md) remain finite MEASURED observations.

## Proof or evidence

The full-form reduction [PD-T534](../../padua-mz-sharp-constants-20261106/theory/S3-full-form-log-model.md) and corner kernel estimate [PD-T535](../../padua-mz-sharp-constants-20261106/theory/S3-corner-kernel-hard.md) support [PD-T536](../../padua-mz-sharp-constants-20261106/theory/S3-corner-operator-limit.md)'s operator-norm limit and both extremal limits with parity agreement. The fixed compact operator B has ||B−B_K||<=120/K. Its infimum/supremum give the exact characterization; finite fitted slopes are not proof premises. The linked records contain all substantive proofs.

## Applicable obstruction, limitations and next step

PD-N048's full-form obstruction remains scoped. IDEA-470's resume condition is met by [PD-T534](../../padua-mz-sharp-constants-20261106/theory/S3-full-form-log-model.md), [PD-T536](../../padua-mz-sharp-constants-20261106/theory/S3-corner-operator-limit.md). Certified useful decimal values of both spectral extrema remain OPEN; the P1 certificate supplies no useful digits. No new localization mechanism or computation is introduced here.

## Checks and sources

[audit-01](../../padua-mz-sharp-constants-20261106/audit-01.md) and [audit-02](../../padua-mz-sharp-constants-20261106/audit-02.md) accept the linked split results at their stated scopes. No new computation, literature dependence or priority claim is made here.

## History

The original [handoff 01 C3 goal](../handoffs/01-work.md) reads verbatim:

> **Goal:** determine lim λ_min(m, m−1)/log m and lim λ_max(m, m−1)/log m along even m (and odd m after C2), or the best proved bounds.

The original C3 sharp-growth wording is preserved instead of silently
narrowing it to packet bounds. During development the separate -04 file
used “Split from: C3's sharp-growth target” without a durable target ID.
This response supplies that OPEN home and explicit relationship; it
adds no claim that a sharp limit exists and changes no accepted formula.

2026-11-06: The Original target and statement section is preserved verbatim. Existence on each parity, agreement and exact operator characterization are PROVED under [PD-T534](../../padua-mz-sharp-constants-20261106/theory/S3-full-form-log-model.md), [PD-T535](../../padua-mz-sharp-constants-20261106/theory/S3-corner-kernel-hard.md), [PD-T536](../../padua-mz-sharp-constants-20261106/theory/S3-corner-operator-limit.md); the decimal-values conjunct stays OPEN. Overall status OPEN → PARTIAL; the dated original OPEN registration above is historical. See [canonical decision](../../padua-mz-sharp-constants-20261106/LOG.md).

## Final registration

2026-11-05: registered as PD-T381 (OPEN), with separate PROVED support
PD-T379 and candidate IDEA-470's deferred route. The response-stage
mapping/preparation-pending sentence above is historical and is now
satisfied by the [final map](../preparation/final-id-map.json) and
[registration record](../preparation/record.md). No target statement,
hypothesis, proof or mathematical status changes.
