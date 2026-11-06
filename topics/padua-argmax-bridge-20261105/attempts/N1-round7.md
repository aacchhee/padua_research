# N1 round7 — exact coefficient comparison, bounded work record

Rules/input: `8dc1521cf68f7780bd10e02495f6f71a639c03c6`.
Codex mathematical worker, inherited model/effort; serving metadata unexposed.
The prospective gate, shortlist, search scope, exact target and <=300 CPU-s
pilot contract are in [the candidate](../ideas/N1-round7.md).

## State before computation

All N1 round5/6 sources and independent reviews and the N5/C1 sources were
read. The leading endpoint-strip term is 4a L^2/pi^2; the other pieces
contribute at most linearly or remain bounded after their actual finite-h
normalization. The exact L coefficient is the next decisive analytic test.
The full C1 comparison remains OPEN; n>=10^6 is approximation validity only.

No new mathematical computation, fit, integrator or model evaluation has
run at this writing. The optional normalization pilot is explicitly
preregistered in the candidate. All old proofs/reviews and Git are unchanged.

## Analytic result and frozen review scope

[N1-16](../theory/N1-round7-coefficients.md) proves the exact coefficients
and their uniform gaps

    B_c-B_M>=47(alpha^2+beta^2)/(48pi^2),
    b_c-b_M>=(alpha^2+beta^2)/(24pi^2).

Its uniform bounded residual controls the compact t=1/log n endpoint,
but has no small constant or phase modulus. In particular phases of
order1/log n have only O(1) leading loss, so the bounded residual
cannot be discarded. PD-T220's exact finite-n cusp is O(log n/n)
and is retained. No second correction or model was introduced.

The distinct reviewer was notified directly of these frozen files:

| File | SHA-256 | Claim scope |
|---|---|---|
| `theory/N1-round7-coefficients.md` | `e7a7d4464e787df527aa6f155d223ae504a9be8f79221089ee43303c5b8d21e8` | PROVED developer coefficient/boundedness statements |
| `theory/N1-round7-comparison.md` | `3ff66dfe8d67fe25a6ceda01c9bde7da4c225aec0b38430ae3d749ecae32fbb5` | Full C1 OPEN; exact remaining-function contract |

No old developer or reviewer file was changed. Supplementary review
does not substitute for the coordinator's formal Claude audit.

## Completed pilot

Executed once, after the candidate and exact pilot contract were written:

```sh
python topics/padua-argmax-bridge-20261105/code/n1_near_r7_normalization.py > topics/padua-argmax-bridge-20261105/evidence/n1-near-r7-normalization.json
```

Python3.12.14, mpmath1.3.0, 60 digits, exactly n17/24/32 at zero phase.
Process CPU0.31307493s, exit0, hard CPU cap300s. Absolute discrepancies
are1.62e-59,4.98e-60,2.49e-60; each periodic board includes one actual
polynomial endpoint collision. These are MEASURED normalization checks,
with no interval roundoff certification or claim about M_near at those
degrees. Exact Fraction controls also confirm the finite elementary
rational inequalities explicitly written in the analytic proof.

Code SHA `4e78df28472e1c9464dda5e0739b333b927d19d5addcde3688c309cb150d3e5e`;
receipt SHA `64a192218ea4749319c3fe35080437b3cae4833d242eb3aa3d76c21f765f4bd7`.
The receipt pins the imported unchanged `n1_rows.py` source, command,
degree list, versions and CPU outcome. No raw/bulk output was generated.

## Precise remaining obligation / no next round launched

[N1-17](../theory/N1-round7-comparison.md) defines
R_n=M_near-B_M L^2-b_M L and F_n=R_n(phase)-R_n(0). It is sufficient
to prove F_n<=G_n+eta, where G_n is the exact favorable polynomial
coefficient loss and eta107/3584000 is the remaining C1 allowance.

The cheapest proposed next test is a proved increment modulus
K0*r2+c(n)*rho+J(n), explicitly retaining finite-n cusps and bounding
every model cutoff/collision jump. Its numerical budget reduces to
J(n)+c(n)^2/[2(A(log n)-K0)]<=eta when A(log n)>K0.
This is a falsifiable next-step contract, not an executed test or
permission for another round. A primitive version could instead bound
S_n-Lambda_c by eta and then charge the existing model error once.
Full comparison, actual onset, far phases, other classes and all-n
energy remain OPEN; global2–40 is unchanged.
