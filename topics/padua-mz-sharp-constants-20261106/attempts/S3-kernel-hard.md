# S3 supporting kernel proof — decisive hard limit/error step

Rules/input: 2143ad622fa98faf8fe7d5cb8ed2bb7e0062f861.
Agent: Codex supporting mathematical developer; requested gpt-6-astra ultra;
runtime model/effort metadata independently unexposed. Coordinator's
one-line justification is in LOG. Ownership is restricted to this file
and ../theory/S3-corner-kernel-hard.md; no Git or shared-record writes.

## Scope and prospective gate

Read AGENTS.md, agents/WORKFLOW.md, agents/codex/CODEX.md, handoff01,
../novelty-gate-S3.md, the relevant full local-source shortlist
PD-T295/377/381 and ../theory/S3-full-form-log-model.md. This is a bounded
supporting proof for the existing registered corner model. It adds no
new mechanism, candidate, external theorem, attribution or priority claim.
No final S4 fits or numerical model norms were read.

The assigned obligations were the total-degree Legendre kernel limit
with fixed-coordinate errors, reflected-corner cancellation, and the
actual m+1 second-coordinate mesh. S3's operator developer owns the
finite-corner tail, model construction, parity and spectral passage.
Disjoint scope and intermediate quantified estimates were communicated.

## Development and retained route choices

Progress: **YES**, an analytic theorem with explicit errors.

The suggested exact factorial expansion of P_k was considered first.
Telescoping its factors gives a uniform O_U(1/m) bound, but loose
absolute-series constants are unnecessary. This route was superseded,
not refuted, by an elementary integral argument for the same kernel.
No separate candidate or negative-result claim is warranted.

Derive the Laplace representation from the Legendre generating series
and even cosine moments. Compare its integrand with exp(ikt cos(phi))
using a two-point distribution of mean cos(phi). The Taylor remainder
then gives, for every k>=0 and real t,

    |P_k(cos t)-J0(kt)|<=k t^2/4.

This includes degree zero and every k=o(m), without a hidden division
by k. A Bessel derivative bound controls a denominator change m->m+1.
Weighted product errors, the staircase triangular domain, and paired
alternating rows/columns yield the complete theorem:

    |m^-4 K_(m-1)(z_m,z'_m)-1_(same endpoint) kappa|<=C_U/m,
    C_U=3+5U+U^2/4,

for four coordinates in [0,U] and arbitrary denominator shifts in [0,1].
For the Padua mesh itself C_U=3+(9/2)U+U^2/4. The kernel uses continuous
dxdy normalization and kappa(0,0;0,0)=1/24. Every m>=1 and both parities
are covered. Complete proof: ../theory/S3-corner-kernel-hard.md.

## Verification and remaining work

The proof is analytic; no computational claim or measured spectrum is
used. Rule/source reads and managed-environment readiness inspection
were performed. The cloud-environment skill was read; no network work,
Docker execution, private credentials, or new external sources were
needed. Independent mathematical verification and the required Claude
audit remain separate. Coordinator integration must combine the fixed
kernel result with its uniformly controlled finite-corner tail.
