# PD-T?padua-3d-20261106-codex-U2-01 — finite joint sampled-norm descent

ID kind: PD-T. Aliases: U2-SN; simultaneous physical-node descent.
Split from: none. Split into: none.

## Statement

The fixed U2-SN algorithm run at n=2,4,6,8 produced the finite values in
the linked receipt. At n4 its independently assessed lower samples and
unscaled condition improve over the inherited one-sweep localdet set;
at n2/6/8 the registered fallback returns that initial set. No continuous
supremum, global optimum, all-degree quality or asymptotic rate is asserted.

## Definitions

N=binom(n+3,3), V_ij=product_k T_(a_jk)(x_ik), with the exact inherited
degree-major exponent order. E evaluates that basis on the21^3 training
mesh, C=E V^-1, s_m=sum_j sqrt(C_mj^2+1e-16), beta=40/L0, and
F=log(sum_m exp(beta*s_m))/beta. L0 is the initial unsmoothed training
maximum. Fresh assessment is Gauss32^3,8192 scrambled Sobol points,
corners and twelve local starts fixed before optimization. Reported
refined values are lower samples, not certified suprema.

## Assumptions

Precisely U2-01's protocol in [usable2](../usable2.md), published at
fe23e002f25912b2ca2a09b225e385f596f824fe before dependent work. One
L-BFGS-B start from unchanged one-sweep localdet, bounds[-1,1], frozen
stops and fallback, with no assessment-based node selection or tuning.
Exact dyadic modular rank interprets saved binary64 coordinates as
rational numbers. Its finite-field arithmetic uses prime1000003 and
bounded integer products; it is separate from floating conditioning.

## Status by part

Overall status: **MEASURED**.

| Part | Status | Evidence / limit |
|---|---|---|
| Recorded finite quality, cost, errors, noise and rank checks | MEASURED | Actual producer receipt and preserved raw identities; supplementary execution separate |
| Continuous norm, global optimum, degree-uniform quality | OPEN, outside statement | No enclosure or all-degree proof |

Candidate disposition: the isolated n4 improvement is retained; the fixed
rule fails its registered n6/8 extension gate in the separate
[negative record](u2-negative-unrestricted-step.md). This measured home
does not revive the failed extension.

## Depends on

Inherited controls and source chain `t9_r06_maxima.py`, `t9_maxima.py`,
`t4_stacks.py`, `c3_lebesgue.py`, `c3_rank.py`; actual source/data hashes
are in [u2-pilot.json](../evidence/u2-pilot.json). IDEA027 and LIT336/382
are attribution/context only; no external theorem supports the numerical
gain. The direct-optimization method is established, with no priority claim.

## Checks

Executed full command and failure/serialization history are in
[usable2](../usable2.md) and [diagnosis](../evidence/u2-diagnosis.json).
The successful rerun used Python3.12.14, NumPy2.3.5, SciPy1.17.0 with
one requested BLAS/OpenMP thread. Raw:
`/tmp/padua-u2-pilot-20261107-a2`, full-precision `full-results.json`,
trial arrays, refinement details and a hash/byte inventory.

All16 assessed sets have N distinct nodes, condition<1e12 and inverse
residual<=1e-7; every exact dyadic check has rank N modulo1000003.
Historical QR n4/n8 and localdet n2 reproduce node NPY hashes, mesh41
and the original refined values exactly. The numerical objective gradient
check has maximum normalized central-difference error5.838e-10.
The supplementary checker independently reran all16 scientific rows and
all4 optimization traces with agreement. Its alternate monomial matrix,
Python integer elimination and fresh checked prime1000037 give full rank
on all16 rows (13 distinct node arrays):
[replay receipt](../evidence/uc12-u2-replay.json). Its separate SVD/fresh
assessment confirms the n4 gain and the mixed function-error outcome:
[fresh receipt](../evidence/uc12-u2-fresh.json). This supplements the
required Claude audit; it does not certify global suprema or archive raw.

## Sources

[Shared gate](../usable-gate.md), IDEA027/187/209 and coverage-qualified
LIT336/382. Van Barel–Humet–Sorber's original2014 paper was not newly
inspected; no claim depends on unverified details of that publication.

## Proof or evidence

Minor routine differential: dC=-C(dV)V^-1. If D=partial F/partial C,
then dF=trace(D^T dC)=-trace(V^-1 D^T C dV), hence
partial F/partial V=-C^T D V^-T. Product-row derivatives follow by
differentiating T_(k+1)=2xT_k-T_(k-1). This justifies the implemented
finite objective gradient; it does not establish convergence.

| n | QR fresh refined | localdet | U2-SN | extra descent CPU s |
|---:|---:|---:|---:|---:|
|2|7.000000|4.153631|4.153631|0.00494|
|4|11.263055|11.140116|5.434721|0.87645|
|6|22.508222|17.669650|17.669650|0.04493|
|8|45.564648|24.124151|24.124151|0.11678|

At n4 the actual selected set has N35 nodes, unscaled/orthonormal
condition4.25938/3.25223, residual6.07e-15 and logabsdet44.80923,
compared with localdet9.07936/7.80642, residual6.39e-15 and
logabsdet45.58012. Its training/mesh41/fresh values are
5.41825/5.42794/5.43472. The determinant decrease and norm decrease
demonstrate the registered distinction from determinant ascent.

With the frozen16 noisy trials of amplitude1e-6, Gauss maximum noise
falls5.827e-6→3.409e-6 and pooled RMS1.179e-6→0.977e-6.
Function performance is mixed: Gauss exponential RMS0.26507→0.11614,
rational0.04277→0.04170, absolute-value0.05662→0.06011,
cosine0.50871→0.36549. Separate Sobol values remain in the receipt.
No uniform dominance claim is made.

The total successful pilot cost is6.578 process CPU seconds including
construction, assessment and historical calibration. Candidate n4 total
construction is1.02663 CPU seconds, including QR/localdet. Timings are
environment observations and not complexity theorems.

## Scope

Only this fixed implementation, input ordering, seeds and four degrees.
Raw nodes and trials are local regenerate-only, not an archived essential
evidence bundle. Therefore this document does not promote the complete
finite construction batch to a computer-assisted PROVED theorem.
Modular full rank is a positive exact witness under the stated rational
interpretation; numerical full rank alone proves no exact claim.

## Open items

Required independent Claude audit. The first-trial
collision diagnosis motivates a separately preregistered update, U2-AB;
its future outcomes cannot change U2-SN's recorded failure. Any claim of
certified global maxima or degree-uniform small norms remains unresolved.

## History

2026-11-07, Codex U2 worker, assigned gpt-6.1-sol xhigh; runtime metadata
unexposed. Rules/input38227202bc6908d5a5a874950145761a8ca4312f.
Prospective protocol published before execution. One size-limit failure
is preserved with exact source, then unchanged mathematics was rerun.
