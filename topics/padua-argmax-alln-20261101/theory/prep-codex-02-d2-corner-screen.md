# PD-T233 (PD-T?argmax-alln-prep-codex-02) — Finite corner slope and weighted-gradient-energy screen

Final registration: **PD-T233**, 2026-11-03. The provisional identifier in the title remains an alias; mathematical statement and historical evidence are unchanged.

ID kind: PD-T.
Aliases: D2 round1 first-variation screen; thirteen degrees and five inward directions.
Split from: numerical claims in gated/d2/r01-screen.md; exact structural identities remain in gated-codex-13.
Split into: none.

## Statement

At n=2,3,4,5,8,12,16,24,32,48,64,96,128, the registered coefficient-matrix float64 calculation gives strictly negative inward first variations at each of v=(t,1-t),t=0,1/4,1/2,3/4,1. The measured normalized energy W/(n^4*Lambda_c) lies between.2946712648 and.3831018519 on this finite set. These finite observations do not establish uniform all-degree slope or energy estimates.

## Definitions

At canonical nonnode corner c=(-1,-1),use the exact integer structural zero/sign mask and corrected Chebyshev coefficients in [r01-screen](../gated/d2/r01-screen.md). D_v is the signed nonzero-cardinal gradient sum plus the absolute zero-cardinal directional-gradient sum. E_x=sum_nonzero gx²/|L0|,E_y=sum_nonzero gy²/|L0|,E_xy=sum_nonzero gx*gy/|L0|,W=E_x+E_y; matrix gradients and analytic corner magnitudes are used, not floating zero tests.

## Assumptions

Python3.12.14/NumPy2.3.5 float64 for the reported slope/energy screen,deterministic inputs,no random samples. Exact rational n2 and outward n3,4,8 diagnostics are separate finite controls; they are not promoted to new global proofs or all-degree estimates.

## Status by part

Overall status: **MEASURED**.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| 65finite directional slopes | MEASURED | 13degrees×5directions; float64 signs |
| 13finite normalized energies | MEASURED | No boundedness or limit theorem |

Candidate / claim disposition: none; this is a finite evidence record.

## Depends on

PD-T101 corrected kernel; gated-codex-13 for the separately proved structural mask,gradients and first-variation representation. The exact small-degree controls are diagnostics inherited from the existing rational/outward constructors.

## Checks

Original main command: `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-argmax-alln-20261101/code/gated/d2_screen_r01.py <scratch>/d2_screen_r01.json`; weighted energies use the separately registered inline command in r01-screen on the same thirteen degrees. Frozen producer SHA256`1fb72190e9ea0ae53450ad5e379bfe2a74246520e8dd43ae50f7f6a65e0009d2`. The independent Astra xhigh [check](../gated/checks/d2-r01.md) separately reran both calculations:1,503numeric and203other main leaves agree exactly in that environment,with only argv/timing exclusions; weighted-energy values agree with only timing and completed-note hash exclusions. [Receipt](../outputs/gated/check_d2_r01_receipt.json) SHA256`0d35b696ee0c3c1607e2e2fdac6d8fa4c011081e0d2ea4a50bab2e02d7476eb2`. No screen was rerun at preparation.

## Sources

No external theorem, literature priority or new mechanism is claimed.
This is the durable rehoming required by audit-01 F11 and accepted
response-review-01, not a new scientific run.

## Proof or evidence

Claude [audit-01](../audit-01.md) accepted the numerical claims at their recorded finite scopes; its F11 requested these durable homes. Historical payloads are pinned at source `1cecd68ac0a64b01ed7b2d262b6263a955a7d4d7` in [cold-storage.json](../cold-storage.json); retrieval is byte-exact, and the active integrity manifest must never be overwritten. Archived main72,838B SHA256`78dbf52b06c15d2ebae5f0fee5153236de28034ac8cc0fdf0d923de887ead5ad`. Committed weighted-energy4,675B SHA256`8250472c4d73a9ac9c8a74d2d587581fa2976e6f094efbe2829daab12b8dc43b`. At n128,Dx=-103567.8210693,Dy=-105175.9830741,Lambda_c=17.3460568001; W/(n^4 Lambda_c)=.3303843693. At n2,the separately exact axis controls are-7/3,-14/3. At n128 the closed-gradient comparison has maximum absolute discrepancy1.16001e-5 and relative1.19335e-7 after scaling bymax(1,|matrix gradient|); these cancellation-sensitive diagnostics are not enclosures.

## Scope

Finite numerical negativity and energies only. The exact controls/structural proof remain separately identified; neither justifies a uniform physical corner radius by sampling.

## Open items

Uniform all-n slope and weighted-energy estimates remain OPEN. The eventual local/global corner proofs use their own analytic routes; no new degree,off-corner scan or threshold is implied.

## History

2026-11-03, Codex gpt-6.1-sol high (configured; serving metadata not
independently exposed), preparation input `cdb12257af24ea2542de707b9730f8278d69a168`.
Created from the already recorded finite observations and independent
checks cited above. No new measurement, criterion, bound or source output
was produced; no historical evidence was split or recommitted. This
record separates the measured claim from supporting PROVED theory and
from unresolved all-degree targets.
