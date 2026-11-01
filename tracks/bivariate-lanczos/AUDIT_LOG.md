# Audit log — bivariate Lanczos track

| Result ID | Pinned commit | Auditor (model, effort) | Finding | Evidence |
|---|---|---|---|---|
| L1 PD-T?…-101–109, -401, PD-N?…-101, -102 | b84af76 | Claude Opus 5.5 xhigh (independent reconstruction 01; supplementary) | proofs confirmed; B1, B2 blocking (applied: PD-N?…-105, K1 inconclusive) | topics/bivariate-lanczos-20261031/reviews/L1-reconstruction-01.md |
| L1 R04–R07 (110–115, N103, N104) + response 01 | c8ccce0 | Claude Opus 5.5 xhigh (reconstruction 02; supplementary) | no blocking; T-113 exact rerun → PROVED | reviews/L1-reconstruction-02.md |
| L3 300–309, N301, N302 | 0b7b396 | Claude Opus 5.5 xhigh (reconstruction 01; supplementary) | no PROVED claim refuted; exact rerun of 306, N301; M1–M3 applied | reviews/L3-reconstruction-01.md |
| L3 310–315, N303–N306 + response 01 | ae991c1 | Claude Opus 5.5 xhigh (reconstruction 02; supplementary) | no high findings; 313/N303 confirmed n = 4..16 | reviews/L3-reconstruction-02.md |
| L5 501–506 | dd919d2 | Claude Opus 5.5 high (reconstruction 01; supplementary) | five medium corrections applied | reviews/L5-reconstruction-01.md |
| L2 201–207, N201–N204 | 9378b68 | Claude Opus 5.5 xhigh (reconstruction 01; supplementary) | span drift confirmed; high finding on 205 applied | reviews/L2-reconstruction-01.md |
| all 67 theory files | 5ccfac2 | Codex gpt-6-astra xhigh (audit-01) | CHANGES REQUIRED; core exact certificates and foundational proofs survive; findings answered in response-01 | topics/bivariate-lanczos-20261031/audit-01.md |
| response-01 impact map (65 changed/new files) | 075d407 | Codex gpt-6-astra xhigh (audit-02) | original findings resolved; T209, T318 confirmed; four low qualifications A2-L1–L4 | topics/bivariate-lanczos-20261031/audit-02.md |
| response-02 (6 files) | aea0128 | Codex gpt-6-astra xhigh (audit-03) | CLEAN within scope; proceed to PR preparation | topics/bivariate-lanczos-20261031/audit-03.md |

Final IDs (PR preparation 2026-11-01): see [ID_CROSSWALK.md](../../ID_CROSSWALK.md); the result IDs above are provisional labels of the time of each audit.

## Integration correction handoff (2026-11-01)

Audit-04 at a2dd845 required preparation corrections; [response-04](../../topics/bivariate-lanczos-20261031/response-04.md) records direct Codex fixes under AC's explicit no-extra-Claude-loop instruction. A distinct reviewer independently verified candidate98945cbcf10c4f8eb53f77c996db358392d42391: [audit-05](../../topics/bivariate-lanczos-20261031/audit-05.md) is technically CLEAN. All77 complete theory files, scientific evidence and404 allocations are unchanged. AC subsequently resolved the remaining output-budget condition with the [PR#10-only exception](../../topics/bivariate-lanczos-20261031/response-04/AC-EXCEPTION.md). Original audit reports are preserved. Ready for AC’s merge decision; only AC merges.
