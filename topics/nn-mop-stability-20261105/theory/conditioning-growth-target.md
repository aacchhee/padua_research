# PD-T448 — sharp conditioning growth target

ID kind: PD-T. Aliases: D1 sharp growth-law target; useful matching rate.
Split from: none; durable home of the original D1 target.
Split into: PD-T?nn-mop-cond-codex-C2-hard-01, the solved exact benchmark
Krawtchouk exponential-rate conjunct in
[the sharp-rate theorem](../../nn-mop-conditioning-20261106/theory/c2-sharp-upper.md).
The remaining conjuncts stay in this PARTIAL parent. The local derivative,
coarse upper bound, lower bounds, normality and measurements are separate
supporting results, not solved target cases.

## Statement and definitions

For the exact Krawtchouk and Hahn input families of handoff01/PD-T290,
with N common nodes z_k=2k/(N-1)-1 and the induced condition kappa_N
defined in conditioning-local.md, determine matching all-N growth bounds
with explicit useful constants and a sharp exponential rate if one exists.
In particular determine liminf and limsup of kappa_N^(1/N), whether they
are equal and finite, and the required subexponential factors. A usable
digit-loss expression must state its input/output norms and finite-perturbation
radius; it cannot predict every algorithm's actual rounding error.

## Assumptions and status

Overall status: PARTIAL. The input model allows unit-scale absolute node
perturbations and componentwise relative weights; the output uses four
field-sup relative norms. Full mixed normality is required. Krawtchouk
normality is proved for all N by PD-T433. For the exact Hahn benchmark,
all-N normality (every N>=2, all mixed indices through degree N) is proved
by the separate analytic theorem
[PD-T?nn-mop-cond-codex-C2-02](../../nn-mop-conditioning-20261106/theory/c2-hahn-normality.md),
accepted in [audit-01](../../nn-mop-conditioning-20261106/audit-01.md).
PD-T436 remains the original finite N4–64 computer-assisted certificate;
it is historical finite evidence, not the current limit of Hahn normality.

The following table decomposes the unchanged statement's own conjuncts
and family cases, as accepted in
[classification-proposal.md](../../nn-mop-conditioning-20261106/classification-proposal.md)
and [audit-02](../../nn-mop-conditioning-20261106/audit-02.md), NOTE-1.

| Direct target part | Status | Split-off result / remaining obligation |
|---|---|---|
| Exact benchmark Krawtchouk: determine liminf and limsup of kappa_N^(1/N), their equality and finite value | PROVED | PD-T?nn-mop-cond-codex-C2-hard-01, [sharp-rate theorem](../../nn-mop-conditioning-20261106/theory/c2-sharp-upper.md), together with PD-T437: both limits equal 5+2sqrt(6) |
| Krawtchouk: determine the required subexponential factors and useful sharp constants | OPEN | The current lower polynomial factor and loose upper 3,000,000 N^13 do not determine a matching prefactor or sharp polynomial correction |
| Krawtchouk: an informative finite-perturbation radius and useful finite-error digit allowance | OPEN | Local first-order sensitivity does not supply finite-radius remainder control |
| Exact benchmark Hahn: determine full-map liminf and limsup of kappa_N^(1/N), equality and finite exact value | OPEN | The terminal-row rate and full-map lower liminf at rho_H do not supply a matching full-map upper or equality |
| Hahn: matching subexponential factors, useful constants and finite-perturbation radius | OPEN | Full-map upper, prefactor and finite-radius obligations remain unresolved |

The exact benchmark Krawtchouk rate is a solved part of this target itself.
Every remaining part is OPEN; no MEASURED or CONDITIONAL result enters
this aggregation. Lower bounds, normality, derivatives and finite tables
remain supporting dependencies and alone would not justify PARTIAL.
No candidate is rejected here.

## Dependencies, evidence and scope

PD-T286/288/289 define the exact map; PD-T290 fixes the benchmarks and
PD-T432 the induced derivative metric. PD-T?nn-mop-cond-codex-C2-hard-01
is the split-off solved rate conjunct, using PD-T437's matching lower bound.
The local derivative, coarse upper bound, lower/proximity proofs, finite
Hahn certificate and measured tables retain their own statements and
statuses in their linked predecessor theory files. Their commands/checks
are in attempts/D1.md and attempts/D1-hard.md.

The separate [all-N Hahn normality](../../nn-mop-conditioning-20261106/theory/c2-hahn-normality.md),
[Hahn lower bound](../../nn-mop-conditioning-20261106/theory/c2-hahn-lower.md),
[Hahn terminal-row rate](../../nn-mop-conditioning-20261106/theory/c2-hahn-terminal-rate.md)
and [general-parameter Krawtchouk lower bound](../../nn-mop-conditioning-20261106/theory/c2-krawtchouk-parameter-lower.md)
are supporting dependencies. None closes the full Hahn rate or the
remaining prefactor/radius conjuncts. No computation, new proof or new
mathematical mechanism is added by this classification record.

## History and next step

### 2026-11-06 — historical OPEN classification before the matching rate

The following rationale predates the accepted matching Krawtchouk upper
bound and is retained verbatim as the earlier status decision:

> The original handoff requested, for example, an explicit exponential lower
> bound. That example is now proved separately with lower base at least
> 5+2sqrt(6). A coarse rational-height upper bound is also proved. Neither
> is a matching sharp growth law, so this parent target remains OPEN, not
> PARTIAL on the strength of supporting results. The Hahn and finite-radius
> questions likewise remain unresolved. No candidate is rejected here.

At that point the Hahn normality record was limited to the finite N4–64
certificate PD-T436; the separate all-N analytic theorem cited above now
supplies the additional normality result. The following audit-01/audit-02
history also predates the present classification application.

The phrase 'D1 sharp growth-law target (OPEN)' was previously used without
a durable home. Added for audit-01 MINOR4 on2026-11-06 by Codex, requested
gpt-6.1-sol high.

2026-11-06, Codex, audit-02 R-4: the original D1 target from
[handoff01, D1 section, lines 54–64](../handoffs/01-work.md) is quoted verbatim below:

> - Define the first-order condition number κ_N of the map (nodes, weights) → (a₁, a₂, b₁, b₂), in normwise and componentwise forms, matching PD-T290's metric. Do this for the NN map and, for comparison, for the step-line map of LIT-347.
> - Compute κ_N exactly, or in high precision with a certified derivative, for both families, N = 4–64.
> - Then be adventurous:
>   - prove the growth law, for example κ_N ≥ c·ρ^N for multiple Krawtchouk with an explicit ρ(p₁, p₂);
>   - identify its mechanism: proximity of the two measures through d = b₂ − b₁, discrete-measure Vandermonde conditioning, or potential-theoretic node-density effects;
>   - give a formula that predicts digits lost.
> - Tools:
>   - the exact first-order span and sensitivity machinery of PD-T136/137;
>   - moment-cone conditioning (PD-T058/059);
>   - the explicit NN coefficients of the classical multiple Krawtchouk and Hahn families (LIT-562 and sources it cites; read the fulltext before use).
> - Done: a PROVED conditioning theorem with explicit constants on at least one family, or a precise PARTIAL. A MEASURED κ_N table is the minimum.

Reformulation and reason: the statement above reformulates
the unresolved sharp-growth question using matching all-N bounds, liminf/limsup
and explicit norms/radii. It makes the remaining question precise after the
explicit Krawtchouk lower bound and coarse upper bound were split into
separate supporting records. It does not replace the original mechanism
questions or Done criterion, and it does not upgrade the OPEN parent.
Next unresolved step: an informative matching upper rate or a proof that
the proposed sharp-rate formulation fails.

### 2026-11-06 — accepted PARTIAL classification applied

The accepted matching Krawtchouk theorem now solves the exact-rate
conjunct of the preserved statement, which the earlier lower/coarse-upper
results alone did not solve. The five-part table above records the
PROVED-plus-OPEN decomposition and the resulting PARTIAL status. The
original Statement and definitions wording is unchanged. This application
follows the accepted classification proposal and audit-02 NOTE-1; it does
not amend the proofs or broaden their scopes.

The D1 mechanism questions in the handoff quotation (measure proximity
through d=b2-b1, discrete-measure Vandermonde conditioning and
potential-theoretic node-density effects) remain OPEN supporting research
leads outside the formal registered Statement and definitions. They are
retained, not claimed resolved by the rate theorem or scoped proximity
obstruction. Supporting mechanism results do not enter the PARTIAL
aggregation.

Next unresolved steps are the Krawtchouk matching prefactor/useful constants
and finite-radius digit allowance, and the full Hahn matching rate,
prefactor/useful constants and finite-radius digit allowance. The separate
mechanism leads remain open as described above.

## Identifier mapping — 2026-11-06

Final identifiers use the permanent topic reservation; the provisional labels remain aliases:

- `PD-T?nn-mop-stability-codex-D1-target` → `PD-T448`.
