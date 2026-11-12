# PD-T?padua-3d-20261106-codex-U2-02 — admissible joint sampled-norm updates

ID kind: PD-T. Aliases: U2-AB; separation-capped projected Armijo update.
Split from: none. Split into: none.

## Statement

The fixed U2-AB update produces the recorded finite N-node outputs and
quality/cost observations under the registered pilot and conditional
degree-holdout protocol. Its pilot n6/8 and unchanged previously unseen
n10/12 outputs meet the registered five-percent quality/cost/guard gates.
No global minimum, certified supremum, convergence or asymptotic claim
is made. This is a known optimization variant, without priority.

## Definitions

Pi_n is total-degree3D polynomial space, N=binom(n+3,3). The matrix,
smooth cardinal-row objective and basis convention are those of
[U2-SN](u2-sampled-norm.md), unchanged. At accepted physical coordinates
x and objective gradient g, d=clip(x-g,-1,1)-x. Let r be current minimum
Euclidean node separation, delta=r/(8*sqrt(3)); scale d so that its
maximum coordinate displacement is at most delta. Backtrack alpha through
1,1/2,...,2^-24. Before trial inversion, require
rho=||(V_trial-V_current)V_current^-1||_infinity<=1/2. Accept only the
registered Armijo inequality with coefficient1e-4.

## Assumptions

The full protocol, including starts, costs, assessment and exact fallback,
is [usable2](../usable2.md), published at
86b9e26920272bcb6a9a55b3eaf2d41bd63d2d58 before dependent code or
execution. One start, maximum200 accepted steps/25 backtracks/120 CPU
seconds, no assessment-based selection or tuning. The pilot assessment
clouds are reused after R1 findings and are not unseen R2 validation.
U2-AB outputs/quality at degrees10/12 were reserved unseen; historical
baseline values/design were already known, as clarified in usable2.
That rule is applied without change.

## Status by part

Overall status: **MEASURED**.

| Part | Status | Evidence / gap |
|---|---|---|
| Finite pilot results, costs, safeguards and dyadic rank checks | MEASURED | Actual frozen producer and separate24-case supplementary replay |
| Unchanged unseen-degree transfer at n10/12 | MEASURED | Actual completed holdout and registered gate summary |
| Global supremum, optimality, convergence, asymptotic rate | OPEN, outside statement | No enclosure or all-degree proof |

Candidate disposition: retained finite pilot improvement; no all-degree
promise. U2-SN's earlier failed update remains rejected in its own home.

## Depends on

Frozen inherited QR/Leja/one-sweep localdet and the U2-SN objective.
Actual source/data identities are in
[pilot receipt](../evidence/u2-admissible.json) and
[holdout receipt](../evidence/u2-admissible-holdout.json). The new update is in
`code/u2_admissible.py`; the new driver preserves all R1 source bytes.
No external theorem is used to upgrade numerical results.

## Checks / sources

[Shared predecessor gate](../usable-gate.md), IDEA027/187/209 and
coverage-qualified LIT336/382. Established projected-gradient, Armijo
and Neumann arguments are elementary context; no historical novelty claim.
The exact commands, raw directories and all unsuccessful trial traces
are retained by the receipts. Numerical conditions/residuals and exact
dyadic modular rank are separate checks, with no inferred exact rank
from floating singular values. The
[supplementary replay](../evidence/uc12-u2-ab-replay.json) actually
reproduces24/24 scientific rows and6/6 optimization traces, independently
reconstructs every trial safeguard, and checks actual dyadic ranks by
Python integer monomial elimination at1000037. The maximum reconstructed
rho difference is2.31e-14; no interval enclosure is inferred. Its
[separate assessment](../evidence/uc12-u2-ab-fresh.json) preserves the
mixed function/noise outcomes. Required Claude audit remains separate.

## Proof or evidence

Minor routine exact-arithmetic safeguards: a trial moves each node by
at most sqrt(3)*delta=r/8, hence every node pair remains separated by
at least r-2*(r/8)=3r/4. If V is invertible and the stated exact matrix
norm rho<=1/2, then V_trial=(I+(V_trial-V)V^-1)V is invertible by the
Neumann series. Floating evaluation of rho is a numerical safeguard;
without interval/exact error bounds it is not an enclosure proof.

| n | localdet fresh refined | U2-AB fresh refined | ratio | extra CPU seconds |
|---:|---:|---:|---:|---:|
|2|4.153631|3.155869|0.759786|1.4614|
|4|11.140116|5.544014|0.497662|1.2552|
|6|17.669650|8.222854|0.465366|3.6232|
|8|24.124151|12.299585|0.509845|10.7107|
|10|34.870367|17.265295|0.495128|26.6001|
|12|55.677884|26.007323|0.467103|60.4840|

All six outputs satisfy the numerical guards and full exact dyadic
rank at prime1000003. All six runs reach the registered200-step limit
and report optimizer success=false; this is recorded rather than called
convergence. Every attempted geometric step, accepted Neumann safeguard
and accepted Armijo inequality passes the post-run trace checks. Failed
guard/Armijo trials remain in raw output with exact identities.

The [gate/trace summary](../evidence/u2-admissible-gates.json) reports
both gates true after checking all actual attempted geometric steps and
every accepted Neumann/Armijo condition. At n12 the unscaled/orthonormal
conditions are11.0750/8.24010 versus localdet33.8341/24.9675, numerical
inverse residual4.015e-13, logabsdet998.211 versus1019.588. Its
train21/mesh41/Gauss32/Sobol/fresh-refined values are
23.99215/25.96543/24.58423/24.75756/26.00732; the mesh refinements
matter and do not certify the global maximum.

RMS function outcomes are mixed and preserved. n10 improves all four
functions on both measures; n12 has one worse combination (absolute-value
Sobol RMS+2.15%). Pilot n2 worsens exponential RMS and some noise outcomes;
n8 worsens absolute-value RMS; n4 rational Sobol RMS worsens 0.33%; n2 also worsens Gauss cosine RMS (+2.47%) and Sobol absolute-value RMS (+6.45%). At n12 frozen Gauss max/RMS noise change
8.056e-6/1.444e-6→6.203e-6/1.255e-6. No universal error improvement
is inferred from the sampled norm objective.

Extra construction CPU at n10/12 is26.60/60.48 seconds, and total
construction including QR/localdet is31.01/73.17 seconds. Whole batches
including assessment cost22.5913+113.5608 CPU seconds. Dense objective
work O(MN^2+N^3), M=21^3, and O(MN+N^2) working memory explain the
finite practical limits; the rule is not a low-cost all-degree formula.

The actual n12 output is supplied as the single small essential
[lossless node payload](../evidence/u2-degree12-nodes.json), not merely
as a mutable temporary path. It supplies455 exact dyadic coordinate
triples. The separately split
[exact finite unisolvence theorem](u2-degree12-unisolvence.md) uses that
essential payload, a written modular reduction and an independently
executed standard-library-only determinant check, residue318086 modulo
prime1000037. Its PROVED status concerns only that stored set;
this optimization/quality record remains MEASURED.

## Scope

Finite fixed algorithm and observations. Samples/local searches are lower
samples only. Pilot assessment is reused, while the subsequent degree
holdout is unseen before its run. Function errors and noise have distinct
sampling measures and are not selected against. Positive exact modular
checks use rational interpretations of actual binary64 nodes. Large raw
trials are regenerate-only; no blanket computer-proof status follows.

## Open items

Required Claude audit. No further
tuning follows the successful finite transfer. Global norm enclosure,
optimality and degree-uniform stable minimal interpolation remain open.

## History

2026-11-07, Codex U2 worker, assigned gpt-6.1-sol xhigh; runtime model
metadata unexposed. Rules3822720. R2 changed the update after a preserved
training-trial collision diagnosis; its full protocol was published
before implementation/execution. R1 sources and failures remain intact.
