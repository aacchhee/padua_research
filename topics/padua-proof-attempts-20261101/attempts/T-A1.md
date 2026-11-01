# T-A1 — exact corner value

- Rules/base: `cadb35066160e466cb1704b9791ad6f374446422`.
- Developer: Codex `/root/a1_develop`, requested gpt-6.1-sol xhigh; resolved runtime metadata unexposed.
- Result: **PROVED**, `PD-T?proof-attempts-codex-01`, [written proof](../theory/proof-attempts-codex-01-padua-corner.md); required Claude audit pending.
- Stop: done criterion reached; no exact mismatch, no PD-N.

## Gate and route, recorded scope

Read the rules, complete `state/IDEAS.md` headings/aliases/obstruction/disposition tables and `literature/INDEX.md`; read the programme IDEA-17, source theory -04, OPEN_TARGETS A1, the T2 kernel code, source audit A1/proposal review, source cardinal/normalization conventions. Mechanism search terms: `corner`, `rhombus`, `Dirichlet`, `Lagrange`, `Chebyshev`, `absolute-cardinal`, `degenerate`, `2006`, `2008`. Closest entries: IDEA-047 (Morrow–Patterson norm order), IDEA-048 (Padua maxima geometry), MZ IDEA-069 / PD-N005 (uniform cardinal-L1-column domination fails), programme IDEA-17 and its corner-expansion record. These are different targets or predecessor ingredients; none authorizes a fresh novelty claim. This attempt proves the already-stated A1 identity, not a new research mechanism. The MZ L1 obstruction is not used or escaped to obtain a norm estimate here.

Primary CDMV 2008 preprint inspection gives the exact nodes as its **third family**, eqs. (6a–c), not its first family. Source normalization in eqs. (1),(3) matches the task. The authoritative coordinate/parity definition is unchanged. Bos et al. 2006 Theorem 2 has the coordinate-swapped y correction. Literature coverage and locators are in the theory record; no full-paper-reading or priority claim.

Route completed: locally derive the cardinal kernel by discrete cosine Gram orthogonality (rather than inheriting the published proof), then identify the rhombus Fourier sum with the two product-U terms using the parity split in p+q,q−p. Corner substitution finishes the proof, including n=1 and continuous singular limits.

## Executed exact checks

```text
python topics/padua-proof-attempts-20261101/code/a1_exact_check.py > topics/padua-proof-attempts-20261101/outputs/a1_exact_check.json
```

Python 3.12.14, SymPy 1.14.0, exact cyclotomic fields; n=1,…,6, all 332 corner-cardinal equalities from independent Vandermonde inversion and all six Laurent coefficient identities pass. No numerical evaluator imported and no tolerance. Receipt is 1,875 bytes. Code and receipt hashes are in the theory record and receipt. Independent rerun belongs to a distinct agent and is recorded separately by root.

## Failed or deferred routes

No mathematical route failed. A naive direct copy of a “first-family” citation would have mismatched the source's parity label, so the comparison was made against the primary third-family formulas. Checker API property `.is_Identity` was unavailable in SymPy; replaced by exact comparison to `DomainMatrix.eye`, then the entire successful run was executed. A2 asymptotics and A4 argmax were not attempted here.

## Runs needed

- Required Claude (Opus 5.5 xhigh) audit of the written proof and exact-check scope at the orchestrator's final SHA.
- Independent exact regression receipt, if not yet present in the orchestrator's independent-check record.

Next: `Claude (Opus 5.5 xhigh): Audit codex/padua-proof-attempts-20261101.`
