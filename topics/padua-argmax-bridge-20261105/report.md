# Padua argmax bridge — WORK checkpoint, 2026-11-06

The exact global equality set is proved for **degrees2–40** and for
**every integer n>=ceil(exp(256))**. It consists of {(-1,-1),(1,-1)} for
even n and {(-1,-1),(-1,1)} for odd n. The intervening finite gap and
all-degree PD-T099 remain OPEN. This is a much smaller effective upper
boundary than C01's exp(10^12) and C03's exp(10^7), but still impractical.
The campaign prioritizes reducing that boundary and developing a cheap
certifier; it has not run a new old-tech degree-extension campaign.

## Analytic progress

The [C06 global assembly](theory/C06-effective-argmax.md) and
[distinct coordinator reconstruction](independent-checks-C06-effective.md)
combine three independently checked pointwise cases on the complete
closed physical phase cover, with both parities and exact corner equality.
No energy premise or assumed global maximum is used.

| Case | Proven comparison | Exact scope |
|---|---|---|
| Far phases | S<Lambda_c with gap>3592/15 | rho>=1/2, log n>=256; full closed phase diamond |
| Near noncorner centers | lambda<Lambda_c-869/28000 | rho<=1/2, every integer n>=10^6, all admissible noncorner odd centers |
| Actual corner patches | lambda<Lambda_c away from the origin | rho<=1/2, log n>=25, direct C05 theorem |

Sources: [far](theory/C06-far-comparison.md),
[actual finite-degree near](theory/C05-finiteh-model-comparison.md),
[all-class defect](theory/C02-defect-dense-band.md),
[actual corner](theory/C05-corner-quarterangle-bound.md).
The far result controls a=0, axes, endpoints and polynomial collisions.
The closed odd-center cover and endpoint-weighted reflection preserve
the exceptional x mode and exact identity lambda=S-Delta.

The near proof uses the unchanged fixed-count model with
|S-M_near|<3/14000 and proves M_near<Lambda_c+1/32. Strong projected
defect>1/16 supplies the actual margin. The **original tighter C1 bound
with1/4096 remains OPEN at n>=10^6**; it is unnecessary for the sufficient
weaker comparison just proved. C04's limiting residual inequality is
separate from the finite-h C05 proof; no limiting statement has been
silently substituted for the actual degree-dependent model.

C07's stronger actual-corner result is now independently accepted:
for every n>=10^6 on both inward half diamonds,
lambda<=Lambda_c-(alpha²+beta²). Its separate finite positive-deformation
lemma gives Lambda_c>=(nL_n²+1)/(n+1) for all n>=2.
[Corner proof](theory/C07-corner-million-onset.md),
[lower bound](theory/C07-corner-positive-deformation.md),
[independent review](independent-checks-C07-corner.md).
Thus the current far target at n>=10^6 is the remaining analytic phase
case. A compact full-phase model/error proof and a separate all-phase
comparison are in development. Binary64 diagnostics are measurements only.

## Cheap certification progress

The original exact [finite theorem](theory/native-finite-range.md) remains
2–40; no new degree is claimed. Known n32 is being used to test new
algorithms on an immutable already accepted364-leaf candidate.

| Checker | Outcome on the same364-leaf candidate | CPU seconds |
|---|---|---:|
| Previous accepted Arb v3 | PASS,0failed/pending |139.405 subprocess |
| First fixed-work C02 | FAIL,76failed/0pending |31.965 total |
| Refined C03 mode0 | PASS,0failed/pending |46.090 total;45.229 subprocess |

The accepted C03 checker is about3.08times faster on comparable subprocess
accounting. It recovers all76 C02 failures without a new tree, mode switch,
producer, retry or degree. It makes333 native box calls and verifies all254
recorded build/runtime identities. [Full independent outcome](independent-checks-C03-cheap-n32.md).
Bounds are still weaker than the old checker on many leaves; all required
strict predicates nevertheless pass. The first failure is retained.
This is a known-case speed result, not a general scaling theorem.

The C03 refinement removes degree-growing harmonic evaluation using
validated fixed-work ratio charts and sharp endpoint monotonicity. All
three source modes have independent bounded controls; only mode0 was
released for the full run. The original producer cost222.813CPU seconds
has not been reduced by this checker result. A fresh MPFR producer port
is now being developed with bounded controls only; C02's earlier bounded
port/tightness and compile failures remain preserved.

For larger algorithmic gains, [C02 row reduction](theory/C02-row-cotangent.md)
gives an exact-real O(n) point representation using bounded cotangent
blocks, four retained rows and ambiguous endpoint samples. The C06 partial
backend passed independent LP64 review:76 cases and784 exact moment checks
in2.69CPU seconds. It is one component; it does not itself implement full
S or whole-box/gradient/defect/corner predicates. C07 guarded point-S integration is now independently accepted on LP64.
It is still expensive: n128 costs11.55CPU in the fixed cost pilot,
and the n512 attempt reached its cap. Source countO(n) is not yet cheap
runtime. A faster interval moment recurrence is in development.
The direct moving-root whole-box interface and its fixed-width quadratic
enumeration obstruction are now proved; a coefficient-convexity escape
to guardedO(n) whole-box upper bounds is under independent review.

## Limits, resources and next work

The fresh campaign has completed seven coordinated rounds; C08/C09/C10
work continues under AC's allowance of up to15. The [campaign ledger](campaign-20261106.md)
is authoritative for round outcomes, with historical direction totals in
[rounds](rounds.md). Next scientific priorities are the practical far
comparison, reviewed full point-S evaluation, rigorous whole-box root
handling and a cheaper producer. No second near-model correction is allowed.

Finite bootstrap energy2–128 and its astronomical analytic tail remain
separate results. They are unnecessary for the new actual-corner/far
assembly and do not close their intermediate energy range. The N4/N6
specified families failed, with scoped negative records retained. N5's
quarter target remains OPEN; its failed particular certificate does not
refute the target. No practical Syvert pack or completed finite bridge exists.

Formal **Claude Opus5.5 xhigh audit remains PENDING**. Supplementary distinct
Astra mathematical/source checks do not replace it. PR27 remains draft
WORK; final shared-registry application and merge readiness are pending.
Only AC merges. Generated evidence remains under the temporary10,000,000-byte
aggregate ceiling; major archive cleanup is a separate topic. Large raw
outputs stay local with identities in small receipts; physical archival
transfer is pending. Historical outcomes and failures remain in LOG,
attempt records, frozen sources and evidence.
