# Proposed shared-record changes — not applied

These literal proposals are for audited PR preparation. They do not assign final
IDs or modify any merged registry. Refresh the actual target text and every live
reservation before applying them. PD-T099 stays OPEN and the global finite
range remains exactly 2–32.

## state/CURRENT.md, effective-argmax paragraph ending

Old:

```text
This supersedes the historical PR17 all-n-slope gap above; weighted energy and the fixed scaled phase radius remain OPEN.
```

Proposed replacement after accepted audit and registration:

```text
This supersedes the historical PR17 all-n-slope gap above. Phase 2 proves W_n<=10^10 n^4 Lambda_c and instantiates PD-T227 Scope (8) with an explicit physical corner radius 10^-11/n^2 for every n>=2, allowing individual cardinal sign changes. PD-T228 already gives an eventual radius 2^-17/n^2, in particular for log n>=10^7; the phase-2 distinction is its every-n>=2 scope. Combining PD-T251 with T07 gives the usable all-degree strict-descent radius max(1/(2[n(n+1)]^3),10^-11/n^2), applying each theorem's loss bound only on its own domain. T07's radius exceeds PD-T251's only for n>=473. A larger practical corner zone, the complete phase-box certifier and the effective all-degree bridge remain OPEN; the finite global range remains exactly 2–32.
```

## PAPER_MAP.md, effective-argmax remaining-gap cell excerpt

Old:

```text
weighted energy and the fixed scaled phase radius remain OPEN; G8 transfer/novelty coverage incomplete
```

Proposed replacement after accepted audit and registration:

```text
weighted-energy scale and an explicit physical n^-2 corner radius for every n>=2 are proved in phase 2 by instantiating PD-T227 Scope (8); PD-T228 already gives an eventual 2^-17/n^2 radius, in particular for log n>=10^7. The usable all-degree strict-descent radius is max(1/(2[n(n+1)]^3),10^-11/n^2), combining PD-T251 and T07 without extending either loss estimate. T07's radius exceeds PD-T251's only for n>=473. T06 is an explicit-constant re-derivation of the known O(log^2 n) norm theorem (LIT-312/LIT-379), not a priority claim. Useful constants, full-diamond asymptotics, complete phase-box certificates and an effective bridge remain OPEN; G8 transfer/novelty coverage incomplete
```

## New records to consider at preparation

The following 2026-11-05 response proposals implement audit-01 F4–F7.
They preserve every accepted statement, proof, constant and epistemic status.
Only the future registration scope and dispositions are clarified; no final
ID is assigned here.

| Provisional record | Proposal for future preparation | Status / scope |
|---|---|---|
| T01, `theory/phase-structure.md` | Register **one narrow finite phase-chart sufficiency reduction**, as audit-01 recommends; PD-T210 is its predecessor. | Existing PROVED sufficiency statement only. Identities verify PD-T101/215/216/218/223/225/226/228; the orbit formula is a routine generalization of PD-T228 (3). Keep those as labeled verification/routine lemmas, not separately new PROVED dependencies. |
| T02, `theory/localization-diagnosis.md` | **Do not register**; retain as gate-A0 evidence linked from R1's deferred disposition in `gates.md`. | CONDITIONAL on hypothetical C=1.4–1.7, prescribed by handoff-01 and motivated by measured PD-T247/252. No global C or practical threshold is proved. T04 now covers the noncorner radius 1/16. |
| T03, `theory/profile-boundary-cotangent.md` | Register the exact boundary profile and its existing uniform remainder. | PROVED on the diamond boundary only. |
| T04, `theory/defect-radius-extension.md` | Register the quantitative PD-T224 variant, paired with IDEA05. | PROVED noncorner (ρ,d)=(1/10,1/8192), all n≥48. |
| T05, `theory/corner-weighted-energy.md` | Register the completed PD-T227 weighted-energy premise; cite measured predecessor PD-T233. | PROVED W_n≤10^10 n^4 Λ_c for every n≥2; no measurement is a premise. |
| T06, `theory/corner-global-norm-ratio.md` | Register the explicit-constant re-derivation and all-degree ratio, with LIT-312 Theorem 3, LIT-379/T-A2 and PD-T216+PD-T157/PD-T227 Scope as predecessors. | PROVED existing bounds 110[1+log(n+1)]² and 27500Λ_c; known O(log² n) order, no first-explicit-constant claim. External fulltext/priority comparison remains pending. |
| T07, `theory/corner-n2-local-radius.md` | Register the explicit every-n≥2 instantiation of PD-T227 Scope (8), citing PD-T228's eventual n^-2 radius and PD-T251. | PROVED existing radius 10^-11/n² and stated loss on that radius only. The maximum-radius usability note above combines existing strict-descent domains. |
| T08, `theory/phase2-measurements.md` | Register **one scoped MEASURED home** for the already accepted phase/projection/box-pilot observations; cite PD-T232/247 as phase/defect predecessors and PD-T233 as the separate energy-screen predecessor. | MEASURED finite samples and INCOMPLETE capped covers only; no new run, continuous bound, certified degree, A1 pass/kill or inferred global constant. |
| N01, `theory/profile-leading-only-obstruction.md` | Register only the already refuted leading-factor-only H2 form, paired with IDEA03. | PROVED scoped obstruction; PD-T099 and the full H2 profile remain OPEN. |

The existing numerical records are transcribed into T08 without altering
their evidence or status, as PD-T232/233 did for earlier screens. It is a
supporting measurement record, not a new analytic dependency or an extra
proved part of PD-T099. At preparation, retain provisional-to-final mappings
for the records actually registered; T02 remains a local label only.

| Retained provisional IDEA | Explicit disposition / canonical home |
|---|---|
| IDEA01, H1 | Retained, OPEN certifier; original pilot incomplete at n=17/32/64/128/256, neither A1 pass nor growth-law kill; T01/T08. |
| IDEA02, boundary H2 | Retained, accepted boundary theorem T03. |
| IDEA03, leading-only H2 | REJECTED: refuted, only the stated a*b_n form; N01. |
| IDEA04, aggregate H3 | Retained continuation of IDEA-330/PD-T227, with accepted T05/T06/T07 and their corrected predecessors. |
| IDEA05, finite-line defect extension | Retained quantitative variant of IDEA-328/PD-T224; T04. |
| IDEA06, phase-dependent-log full-diamond profile | Deferred, target OPEN; resume after an explicit interior profile, transition control and uniform tail are specified. |
| IDEA07, signed-polynomial Markov shortcut | Equivalent to PD-T227 (6)–(7); consolidate there, no PD-N. |
| IDEA08, cell-integral envelope norm route | Deferred, distinct from IDEA07; resume for a concrete cover-budget need with a specified envelope capable of improving the available constant. No failure theorem. |

The full candidate records are in `ideas/H1.md` and `ideas/H2-H3.md`.
Existing obstructions and their exact scopes remain unchanged. Import this
topic's permanent reservation from ALLOCATIONS.md into the shared batch ledger,
link it from ID_CROSSWALK.md and preserve all earlier ranges/gaps. Preparation
must preserve every other topic's RESULTS section and add only this topic's
accepted summary. No source/priority claim or new literature transfer is proposed.
