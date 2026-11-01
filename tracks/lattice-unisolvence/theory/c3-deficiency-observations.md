# PD-N?lattice-c3-codex-01 — Scoped deficiencies and annihilator certificates in the finite 3D catalogue

Final ID: **PD-N035** (allocated 2026-11-01 under AC's authorisation; the provisional ID above and in the text is retained as provenance — see ID_CROSSWALK.md).

ID kind: PD-N. Aliases: failed finite rank scopes; layer-cover and projected-count cases. Split from: c3-rank-observations.md. Split into: the general certificate theorem c3-annihilator-certificates.md.

## Statement and negative-result scope

Attempted mechanism: every cardinality-correct primitive single-congruence fibre in the frozen C0 3D catalogue might interpolate total degree n on generic distinct axes. In the exact finite scope of c3-rank-observations.md, 222 of364 actual-point/reversal representatives are deficient in all six modular draws. 127 have explicit coordinate-layer cover certificates of degree<=n; another86 have layer-removal/projected-count certificates. The remaining9 have no certificate from either method, despite rank deficiency in all six draws.

Overall status: MEASURED, for these finite exact checker results. The universal implications of an individual valid certificate are PROVED in PD-T?lattice-c3-codex-02. The per-pattern certificate enumeration remains a computer-assisted claim requiring the independent finite check documented by the auditor before completed acceptance. Always-deficient samples alone do not prove a zero determinant polynomial.

Candidate disposition: failed/refuted only for the individual certified patterns once their certificate is independently checked. The nine unresolved generic cases remain OPEN; their mechanism search is deferred, not a universal rejection. No assertion is made about every n, arbitrary modulus, coset union, boundary correction, or a different grid.

## Evidence

For n=1..6, cover-certificate counts are14,26,24,15,22,26. Additional projection counts are13,15,15,12,18,13. Thus all always-deficient representatives for n=1,4,5,6 receive one of the two certificates, whereas two degree2 and seven degree3 cases remain unresolved by these mechanisms.

The nine IDs are C3-146194f53e09, C3-63a9bc46428d, C3-b312ad59cf2d, C3-e94fa0f84746, C3-ed5be2a8aa20, C3-a86caab28e7a, C3-4b8f5204bfc8, C3-e52f073b516e and C3-1173efd58918. Their complete points, field ranks and attempted certificates are preserved in ranks.json, structure.json and obstructions.json. A further frozen subbox-dimension attempt is recorded in lowdegree.json and does not silently replace the original scope.

No failed run or absent certificate is treated as a theorem refutation. The certificate mechanisms themselves are elementary valid sufficient tests; their failure to explain a pattern does not reject them.

## Checks / dependencies / history

PD-T?lattice-c3-codex-02; c3_structure.py and c3_obstructions.py, with hashes and commands in C3/evidence.md. Independent Astra reported a separate recursive hitting-set check reproducing all222cover decisions; projection checks pending its durable report. Rules/base e949ef06895acd5463cdf8df7e0e5f795218f70f, 2026-10-31, Codex C3 mathematical developer, assigned gpt-6.1-sol xhigh. No novelty claim; elementary polynomial/dimension obstruction variants only.

## Audit history addendum — 2026-11-01

The pre-acceptance pending wording above is historical. Supplementary [Astra reconstruction](../../../topics/lattice-unisolvence-20261031/independent/report.md) completed, and [Claude audit-01](../../../topics/lattice-unisolvence-20261031/audit-01.md) accepted this exact existing statement and epistemic status. [Response-01](../../../topics/lattice-unisolvence-20261031/response-01.md) changes audit/integration metadata only; no proof, hypothesis, status or finite observation is upgraded. Literature/novelty gaps remain unresolved where stated. Codex administrative response, requested gpt-6.1-sol high; runtime metadata unexposed. Audit F2 separately supplies an additive-separation certificate for the nine cases left outside the original(A)/(B) mechanisms. Their description as unresolved above records the original development frontier. That proposed new result is preserved verbatim in the audit; adoption under a new result ID is deferred rather than folded into this unchanged audited statement.
