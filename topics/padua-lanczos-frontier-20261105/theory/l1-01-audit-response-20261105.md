# PD-T324 — L1-01 metadata companion — audit response, 2026-11-05

Final registration (2026-11-05): **PD-T324**; status **PROVED** unchanged. Canonical provisional/historical aliases: `PD-T?lanczos-frontier-codex-L1-01`; `PD-T?lanczos-frontier-codex-L1a`. See [complete map](../preparation/final-id-map.json). This is ID metadata only; original statement/proof and frozen input bytes retain their scopes.

This is additive metadata for the existing PROVED analytic result, not a
separate mathematical claim or result ID. The theorem/checker inputs stay
frozen. Canonical provisional ID: **PD-T?lanczos-frontier-codex-L1-01**.
Aliases: `PD-T?lanczos-frontier-codex-L1a`; L1a; SH_n aggregate span separation.
The old title in the frozen record is a historical alias.

Frozen [theorem](l1-01-sheared-U-aggregate-separation.md) SHA-256:
`f27a22c4c6f13d03710750f52eef4dc9bac31f27bd009beaa536866fbbe24d9f`.
It is pinned by `code/sh_independent.py`; neither file is changed here.

## Statement and scope qualifier (A-m1; L1-1, L1-4)

Both bounds hold for all n>=2; the ratio bound exceeds 1 only for n>=18;
no small-n ordering is claimed. The physical family is an **affine image
of a product grid**, with positive tensor weights in latent coordinates.
The T24/rotQ24 all-degree question remains OPEN; finite G1 is INCONCLUSIVE.
The theorem concerns worst-case first-order aggregate-source span capacity
under exact full projection/normalization. No IEEE, scalar-realizability,
closure-defect or uniform finite-error conclusion follows.

## Committed provenance and dependencies (L1-3, L1-9; L2-2)

The historical Astra input hash `9f59217da265a433470bb6030074acf76e63e4ffb0a6590add800666a64de90d`
was never committed and is not reconstructible from repository bytes.
Claude [audit-01/L1.md](../audit-01/L1.md) directly audited the committed
`f27a22c4...` bytes and accepted their analytic proof. The seven-section
digest is `13325943c81b8f21760a2ed79f77ddf442bdf42609007aa108f4e4589bb7ac05`.
Its repository-only recipe is
`python3 topics/padua-lanczos-frontier-20261105/audit-01/code/L1/section_hash.py topics/padua-lanczos-frontier-20261105/theory/l1-01-sheared-U-aggregate-separation.md`.
This checks the documented section digest, not recovery of the old whole file.

L2-04/05 use only the PROVED elementary facts in L1 proof sections 1–2:
positive normalized weights, injectivity/dimensions through n+1, exact
tensor orthonormal basis, creator identities and source scales. They do
not use L1's span-capacity separation as a closure lower bound.

## History and protocol qualifier (A-P1/R2; L1-8)

The SH_n candidate/formulas were drafted before the mandatory novelty
gate was complete and first committed at `0574c47`. Full reading and the
later handoff03 gate preceded analytic development. Later reading does
not waive or cure this deviation; acceptance is AC's decision, with
permanent disclosure in [gate-timing-response-01.md](../gate-timing-response-01.md).
This companion qualifies the existing theorem's History while preserving
the checker-pinned bytes. There is no novelty or priority claim.

## Family NOTE dispositions

| Finding | Disposition |
|---|---|
| L1-3 | Accept provenance limit; committed hash/digest above supersede the missing hash as a current dependency. |
| L1-4 | Accept affine-product qualifier above; original non-product question remains OPEN. |
| L1-5 | Defer optional fixed-grid extension; it would add scope and needs impact review. |
| L1-6 | Accept loose-rate limits; matching rates and finite-error behavior remain OPEN. |
| L1-7 | Accept checker hygiene observation; keep pinned checker unchanged. Audit exact latent-monomial and physical-node checks independently cover it; no new run claimed. |
| L1-8 | Accept factual deviation and permanent disclosure; AC decides acceptance. |
| L1-9 | Accept precise elementary-dependency labeling above; no theorem split needed. |

Metadata response: Codex, assigned gpt-6.1-sol high; runtime-resolved model/effort are not independently exposed; rules read
at `7f50cae80f5372db7c278aef4ba4a0a05e1137ea`. No scientific rerun or
status upgrade. Focused Claude re-audit remains required.

## History addendum — 2026-11-05 (handoff10; A-P1)

This result descends from l1-02 SH_n transfer family, drafted before completion of the mandatory reading gate and first committed at `0574c47`. AC accepted the disclosed deviation on 2026-11-05. The deviation remains permanently disclosed, not waived and not cured. Completed-gate receipt: G12: `aab7bbe`, delta `b81c374`; these are publication SHAs, not worker input/rules SHAs. The reported gate-before-development order within the shared `b81c374` publication is prose-attested; Git does not order the receipt against the co-published L1/L2 descendants. Earlier pending-decision wording is historical and is superseded by this dated acceptance record. See [gate-timing-response-01.md](../gate-timing-response-01.md).

## Audit-02 selection-context addendum — 2026-11-05

GATE N2 accepted: this single-family formal mirror upper bound supplies no general rule ordering. PD-N011 measured set-dependent dev/mirror ordering; PD-N015 measured failure of uniform safety. The all-degree normal-projected aggregate SH_n result remains distinct from IDEA-130/134’s finite loss/raw-propagator observations and finite exact impulse certificates.

## Merged-source attribution addendum — 2026-11-05

PR21 merged into main as `b4d292e`. The current source is [topics/padua-literature-20261103/p3-comparison.md](../../padua-literature-20261103/p3-comparison.md), unchanged memo blob `4741c38943f37ae05ba525552ceafc3f32ac5537`. The following per-statement attributions now cite that merged path with the same blob; earlier “unmerged” prose remains historical.

- frozen theorem’s Literature paragraph, through this companion: cite the merged P3 path and blob above; the original statement’s selected-source, version/page and primary-reading coverage limits remain unchanged.

This updates source location only. It asserts no new primary reading, proof import or exhaustive priority/novelty clearance.
