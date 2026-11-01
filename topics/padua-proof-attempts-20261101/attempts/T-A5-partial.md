# T-A5-partial — exact degenerate identities and local bounds

- Rules/source base: `cadb35066160e466cb1704b9791ad6f374446422`.
- Developer: Codex `/root/input_review`, assigned gpt-6.1-sol xhigh; resolved runtime metadata not separately exposed.
- Scope: only the `degenerate_max` path of the n=3,…,8 frozen search. Development started after root declared A1 and B5 complete, respecting target order.
- Durable result: **PROVED**, `PD-T?proof-attempts-codex-03`, [theory](../theory/proof-attempts-codex-03-degenerate-maxima.md). Its exact identities, root enclosures and uniform Hessian inequalities passed the developer and an actual separate independent rerun/proof inspection; Claude audit-01 ACCEPTED; response-01.md records the minor dispositions.
- Stop: the local done criterion is reached for every decision in the reconstructed trace; broader A5 counting is still unresolved. No failed proof route or counterexample is claimed.

## Gate and authoritative inputs

The same agent's full input/novelty review is in `../inputs-review.md`. Read all IDEAS headings, aliases, summaries and obstruction/disposition tables and the literature index, then the required THEORY 01/04/06/N04, OPEN_TARGETS, T2/T3 corrections and audit A1/P1. Mechanism searches included `rhombus`, `corner.value`, `corner.kernel`, `pattern.commutant`, `degenerate.max` and `absolute.cardinal` across state, topics, tracks and literature. Closest Padua entries are IDEA-047 (Morrow–Patterson bounds), IDEA-048 (maxima geometry), MZ IDEA-069 / PD-N005 (a different, failed uniform cardinal-L1-column route), programme IDEA-17 and its source -06 record. This is proof completion of an existing obligation, without an historical novelty claim or a new proposed mechanism.

## Reconstructed finite decision list

Root's `code/a5_trace.py` subclasses the frozen certifier, logs every call and never invokes the source's output-writing main block. It ran n=3,…,8 with single-thread BLAS. The actual trace is `outputs/a5_trace.json`, SHA-256 `093fe1d4171f4416e28ba5e269f30378f4e32165f03bc5969a5d94919e92d468` at this attempt. It has exactly two calls, both accepted at n=3, both with Z={6}, grid label `(2,2)`. There are no unsuccessful calls and no calls for n=4,…,8. All stored candidate-count and box totals reproduced. These are MEASURED execution facts; no claim of certified counts follows.

| n / call | Exact representative | Z / exact identity | Root enclosure and margin |
|---|---|---|---|
| 3 / 1 | `(0,acos(1/sqrt(3)))` | `{6}`; `L6=(x−1)(2x²+x+2y²−2)/3`; value and angle gradient zero | φ∈[.955316618124509278,.955316618124509279]; uniform background-minus-zero Hessian margin ≥3.557444 on l1 radius .0021 |
| 3 / 2 | `(0,acos(−1/sqrt(3)))` | same cardinal and exact identity | φ∈[2.186276035465283960,2.186276035465283961]; same uniform margin |
| 4,…,8 | no calls | no missing local decision in this trace | no all-degree identity inferred |

The backgrounds have exactly zero angle gradient at these representatives and exact centre Hessians stated in the theory. Every nonzero cardinal sign is rigorously stable on the larger neighbourhood; L6≤0 there, so λ3 is the single smooth expression `g−L6`. Direct strict concavity gives the unique local maximum. This also supplies the requested rigorous background-Hessian-minus-excluded-cardinal bound, rather than validating digits of the old floating `mu0`.

The old floating seeds have tiny nonzero θ coordinates. They are rigorously enclosed near the exact representatives, with l1 errors at most 9.4e−17 and 3.6e−17, respectively. The proof radius .0021 contains each entire old `.002` disc about its floating seed, including native binary radius rounding. We do not assert an exact zero at an arbitrary rounded angle.

## Executed developer exact check

```text
python topics/padua-proof-attempts-20261101/code/a5_exact_certificate.py > topics/padua-proof-attempts-20261101/outputs/a5_exact_certificate.json
```

Python 3.12.14, SymPy 1.14.0; deterministic exact polynomial algebra and Fraction intervals. The command passed. Script SHA-256 at that run: `ffcc1508176aa0b60a0a709d41a6e736ca0a4b38ec8aa436d5d706f800431c84`. The default run verifies the frozen input hashes and matches every logged decision; the development `--skip-trace` run had earlier checked the local algebra while the trace was still running. It is not counted as complete trace coverage.

Arithmetic reduction: invert the exact degree-three monomial Vandermonde, derive L6 and the two signed background polynomials, differentiate exactly, prove the two angle-root intervals by alternating rational cosine sums and verified radical brackets, and evaluate the finite angle-Hessian expressions in inclusion-preserving Fraction intervals. Symmetric row-sum bounds certify eigenvalues. No floating Hessian or interval-library rounding convention is trusted by this proof.

Independent execution by `/root/a1_develop` completed using the default script, including trace coverage, and produced `outputs/a5_exact_independent.json`, byte-identical to the developer output: SHA-256 `279c8e7ca9c4781bb3c528a21f870162aab8402ea219e3ec339c4b9d676d25f3`, 7,011 bytes. The same independent agent inspected the written proof and explicit backgrounds with no finding. Its receipt is `../independent-checks-a5.md`; this supplements the required Claude audit and is not that audit.

## Failed or deferred routes

No new mathematical route failed. The old tolerance-based one-maximum inference is already invalid in general (source audit A1's non-Padua countermodel) and is not reused. The exact factor/sign structure here gives a smooth λ expression instead. Full counting certification and source logic repairs were deliberately deferred as outside this local obligation. No PD-N is warranted by that deferral.

## Remaining work and scope

The independent exact rerun is complete and Claude audit-01 is ACCEPTED. Obligation (2) is discharged for `degenerate_max` only; rigorous versions of the (D) corner and (E) edge-node certificates in `t3_degenerate.py` remain needed. For the broader A5 counting target the four other obligations remain: finite reduction/coverage, rigorous per-pattern root enclosures and exclusions over the discarded region, all consistent patterns without the early return, and exact crease-crossing treatment. Global rigorous arithmetic and an independent counting checker remain necessary. Counts 15/27/25/41/50/62 remain MEASURED and no correction to authors is authorized or made.

Source records, OPEN_TARGETS, registries and shared crosswalks remain untouched; root owns proposed old-to-new edits and the log. User's local result-track entry is root's responsibility, with unavailable Windows delivery recorded under Runs needed.

Next: `Codex (gpt-6.1-sol medium): Continue codex/padua-proof-attempts-20261101 — reconcile PR #9 after PR #6 integration.`
