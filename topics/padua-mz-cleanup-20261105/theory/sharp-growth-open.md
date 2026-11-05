# PD-T381 — sharp logarithmic Padua spectral limits

ID kind: PD-T.
Aliases: sharp signed extremal growth coefficients; existence and values
of the endpoint logarithmic limits.
Split from: the original C3 target in handoff 01, preserved here explicitly.
Split into: [PD-T379](growth-carrier-bounds.md) records
separate exact packet norm limits and one-sided quantitative bounds.

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

Overall status: **OPEN**. Existence, values and agreement of the two
parity limits are unresolved. This target is not PARTIAL: the one-sided
packet bounds are supporting results, not a proved decomposition of the
target's own convergence and exact-value assertions. No status changes
for any accepted result.

## Dependencies and existing support

PD-N105/106/107 prove even-m divergence; the separate odd extension
PD-T378 gives qualitative divergence over all integers.
PD-T379 proves exact continuous norms of specified
carriers and explicit normalized one-sided limsup/liminf bounds. These
do not establish matching opposite bounds or an extremal spectral limit.
PD-T380 retains finite observations and fits as MEASURED.

## Proof or evidence

No proof of the target is supplied. The support is linked above rather
than duplicated. The raw sampled-energy optima 1/9 and 1/36 cannot be
identified with spectral constants without continuous normalization and
a matching extremal argument. The finite fitted slopes prove no limit.

## Applicable obstruction, limitations and next step

PD-N048 shows why negative corner mass by itself cannot control the
complete signed form. The deferred localization route
IDEA-470 may resume only with a bound for the full signed
quadratic form on every admissible polynomial in the continuous metric,
with exact normalization and a matching lower/upper argument. No new
localization mechanism or computational run is introduced here.

## Checks and sources

Administrative durable-target restoration for Claude audit-01 F11.
Rules/head a64ef35; Codex, gpt-6.1-sol xhigh, 2026-11-05. No computation,
new literature dependence or historical-priority claim. Final ID and
original-to-split/support crosswalk mapping wait for PR preparation.

## History

The original [handoff 01 C3 goal](../handoffs/01-work.md) reads verbatim:

> **Goal:** determine lim λ_min(m, m−1)/log m and lim λ_max(m, m−1)/log m along even m (and odd m after C2), or the best proved bounds.

The original C3 sharp-growth wording is preserved instead of silently
narrowing it to packet bounds. During development the separate -04 file
used “Split from: C3's sharp-growth target” without a durable target ID.
This response supplies that OPEN home and explicit relationship; it
adds no claim that a sharp limit exists and changes no accepted formula.
