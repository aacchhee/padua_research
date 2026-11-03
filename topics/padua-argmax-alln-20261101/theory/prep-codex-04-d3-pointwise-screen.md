# PD-T235 (PD-T?argmax-alln-prep-codex-04) — Finite common-phase edge-translation screen

Final registration: **PD-T235**, 2026-11-03. The provisional identifier in the title remains an alias; mathematical statement and historical evidence are unchanged.

ID kind: PD-T.
Aliases: D3 E-P float screen;90samples and8reversals.
Split from: floating E-P observations in gated/d3/r01-finite.md; exact E-C and E-P statements remain gated-codex-17 and gated-codex-N02.
Split into: none.

## Statement

At n7,12,on all ten registered directed centreward vertical-edge pairs and the nine common phases u=-1,-3/4,-1/2,-1/4,0,1/4,1/2,3/4,1,the float64 E-P screen evaluates90samples and finds eight target-minus-source values below-1e-6. All eight occur at n12: for each j=0,12, k5→7 at u=-3/4,-1/2,-1/4 and k11→9 at u=-3/4. This statement is the finite floating screen,kept separate from the later exact witnesses.

## Definitions

E-P translates the same rational phase u from source centre k to target k′ on the same vertical edge j=0 or n. Eligible centres satisfy2<=k<=n-1,j+k odd,and k′=k±2 is closer to(n+1)/2. The phase/angle convention and corrected edge sign x=+1 atj0,x=-1 atjn are fixed in [r01-finite](../gated/d3/r01-finite.md).

## Assumptions

NumPy2.3.5/SciPy1.17.0 float64 for the screen under Python3.12.14; no optimizer,randomness,degree beyond7/12 or global certificate scan. The-1e-6 threshold is a preregistered finite numerical screen rule.

## Status by part

Overall status: **MEASURED**.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| 90common-phase samples/8threshold reversals | MEASURED | Finite float64 screen only |

Candidate / claim disposition: none; this is a finite evidence record.

## Depends on

PD-T101 corrected-cardinal evaluator; original E-C/E-P definitions in attempts/P3-P5-and-pairing.md. Exact outward witnesses and whole-cell proofs are distinct gated-codex-N02/gated-codex-17 records,not inferred here from float agreement.

## Checks

Original command: `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-argmax-alln-20261101/code/gated/d3_edge_generate.py --output <scratch>/certificate.json --ep-output <scratch>/ep.json`. Frozen producer SHA256`b0c2b98851dd8721bc876686fd388c62085938ff24d97308a132a7f14e9e3145`; dependencies are pinned in r01-finite and the source artifact. Distinct Astra xhigh [D3 check](../gated/checks/d3-r01.md) separately ran producer/checker and compared mathematical rows excluding timing metadata; [receipt](../outputs/gated/check_d3_r01_receipt.json),SHA256`d77ee6d68926d3b19eaf663a6837a5fbcc9d9115fec0db36f26076cd37bf539b`. Later distinct storage reviews also regenerated this short screen byte-identically. No new run occurred at preparation.

## Sources

No external theorem, literature priority or new mechanism is claimed.
This is the durable rehoming required by audit-01 F11 and accepted
response-review-01, not a new scientific run.

## Proof or evidence

Claude [audit-01](../audit-01.md) accepted the numerical claims at their recorded finite scopes; its F11 requested these durable homes. Historical payloads are pinned at source `1cecd68ac0a64b01ed7b2d262b6263a955a7d4d7` in [cold-storage.json](../cold-storage.json); retrieval is byte-exact, and the active integrity manifest must never be overwritten. Archived E-P screen24,993B SHA256`3215523e1a768ce7e81c76283ac18bf476f8162bdcd84e579a7b93388707d14c`. Its eight floating reversals each subsequently received exact outward witness checks,with designated source angle9pi/26 versus targetpi/2 atn12. That exact >39/1000 result belongs only to the separate PROVED negative record.

## Scope

Only the registered finite E-P screen. A failed pointwise common-phase translation does not refute E-C whole-cell ordering,the all-degree corner target,or another phase map.

## Open items

All-degree E-C and alternative analytic phase comparison remain OPEN/deferred. Direction3 stopped after one round; no larger scan follows from this record.

## History

2026-11-03, Codex gpt-6.1-sol high (configured; serving metadata not
independently exposed), preparation input `cdb12257af24ea2542de707b9730f8278d69a168`.
Created from the already recorded finite observations and independent
checks cited above. No new measurement, criterion, bound or source output
was produced; no historical evidence was split or recommitted. This
record separates the measured claim from supporting PROVED theory and
from unresolved all-degree targets.
