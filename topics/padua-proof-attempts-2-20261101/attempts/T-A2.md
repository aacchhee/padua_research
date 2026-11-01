# T-A2 — corner leading and logarithmic coefficients

Developer: Codex `/root/a2_develop`, requested gpt-6.1-sol xhigh; runtime-resolved metadata is not separately exposed. Rules first read at `a09d910ae7d5526b1e216066421a0bee7fc20da4`, reread unchanged at `b3c333b6519740c21953ed41501a66d37768c1f2` and `818ca4ad0942eb4743860f913a299ff30d959dae`. Authoritative programme input is pinned throughout to `9bd14a6d2c4da69139a10107d8a787f2be0c5c9e`; no older working-tree wording supplies an assumption.

## Start, stop conditions, and current state

Pre-computation start: **2026-11-01T09:06:18Z**. Approximate five-hour box ends 14:06 UTC; literature/gate work preceded this timestamp. No numerical/exact computation had run at registration. Ordered deliverables are (i) corner lower bound with leading coefficient 4/pi²; (ii) two-sided explicit O(log n); (iii) b=(8/pi²)(gamma+log(8/pi)) with explicit O(1). Each substantive completed part gets its own theory record.

Kill criteria written before any exploratory computation: an exact failure of a proposed identity rejects only that identity; an unbounded comparison error rejects a proposed uniform comparison, not A2; any asymptotic counterexample must be supported analytically or by certified evidence before a scoped PD-N. Stop at (iii), a scoped refutation, or the five-hour box. A supporting lemma alone is not a stop or a status upgrade. Any finite floating check is MEASURED. Consequential exact/interval checks require an actual independent rerun by another agent.

Audit interruption: root reported the arrival of part-1 Claude audit at `95279b833bca5967fcf47c1b71a56ff622185b4e`; all A1-dependent work paused immediately while independent literature reading continued. Root reviewed the full audit, merged it via `818ca4ad0942eb4743860f913a299ff30d959dae`, and authorized resumption. A1 had no mathematical finding requiring adaptation. Per the user's requested literal reference the dependency remains **PD-T?proof-attempts-codex-01 (audit pending)**; dated qualification: audit-01 accepted A1 at `95279b8`, while part-1 disposition records are pending. No dependent claim was promoted during the pause.

Initial checkpoint status was OPEN, with no computation or theorem claimed. **Stop reached2026-11-01T09:18 UTC: all three ordered A2 deliverables PROVED in written analytic form; required Claude audit pending.** No A3 attempt was launched. Completion is well within the five-hour box; no supporting-lemma-only stop was taken.

## Relaxed registry and predecessor gate

Read the complete `state/IDEAS.md` (all 496 lines), including all headings, IDs, aliases, summaries, every source/campaign/current disposition table, all obstruction tables, and the programme rows. Read `literature/INDEX.md` before any PDF. Search scope: state, topics, tracks, literature, including negative results. Terms: `corner`, `Lebesgue`, `shear`, `cotangent`, `Kolomo`, `Lomako`, `log.coefficient`, `harmonic`, `Chebyshev.*sum`, `rhombus`, `Dirichlet`, and `absolute-cardinal`.

Closest full shortlisted entries read: programme IDEA?programme-ideas-claude-17 (its entire candidate entry at pinned programme SHA), source theory -04, OPEN_TARGETS A1/A2/A3/A4, decisive-gen4-2 T2 source and narrative; part-1 A1 theory/attempt; IDEA-047/048; MZ IDEA-065 through -071 and linked PD-N005 in full. The absolute-cardinal L1-column obstruction concerns CC weighted L2 estimates, not the present finite point value. The programme's projection-constant route is capped at 16/pi⁴ and cannot prove the desired corner coefficient; this route is excluded. The maxima-cell uniqueness obstruction does not bear on a point evaluation. Finite fits do not establish b or a remainder. No new programme, priority, or historical novelty claim is made: this is completion of an already registered target.

Verdict: registered sharpening of a classical kernel identity, not a candidate novelty claim. Cheapest decisive test: simplify the A1 summand at the node angles, treating endpoint limits separately, then compare a regularized staggered Cauchy sum with an explicitly analyzable one-dimensional product. Before adopting a comparison, test its precise bounded-error statement rather than refitting b.

## Literature coverage

Kolomoitsev–Lomako, *Asymptotics of the Lebesgue constants for bivariate approximation processes*, arXiv:2009.07114v1, corresponding to Appl. Math. Comput. 403 (2021), [primary PDF](https://arxiv.org/pdf/2009.07114): full 16-page paper read through the web PDF text, including introductory definitions, all main statements, Lemmas 3.1–3.7 and proofs, section 4 and references. The theorem-level load-bearing locator for the global upper bound is Theorem 2.1, printed p.4, with its Padua specialization immediately below. Its discretization comparison is Lemma 3.5, printed pp.10–11, especially (3.20); the parity-subgrid ingredient is Lemma 3.6, (3.29), printed pp.11–12, used in (4.5)–(4.6), printed pp.14–15. These estimates leave an O(log n) error and do not identify b. Reading was completed before borrowing a method. Direct shell download was denied HTTP403; no proxy bypass was attempted and no third-party fulltext is committed.

Bos–Caliari–De Marchi–Vianello–Xu, *Bivariate Lagrange interpolation at the Padua points: the generating curve approach*, JAT143 (2006), 15–25, [author preprint](https://www.math.unipd.it/~marcov/pdf/PaduaCurve3.pdf): primary definitions and Theorem 3, printed pp.10–12, with the displayed sum/integral estimates inspected. The source proves global O(log² n), with unspecified constant. The normalized A1 identity is locally proved in the named part-1 dependency. No full-paper reading of Bos2006 is claimed.

## Candidate memory

- Prescribed shear/product-U route: deferred after the exact positive rewrite gave a bounded comparison. A generic triangle inequality would lose cross-term information; no negative theorem is inferred from not following it.
- Node-angle rational simplification: retained PROVED in -04, with the coincident endpoint separately contributing1/(n+1). Exact regression against the finite kernel passed every83 odd-board terms for n=1,…,6. This is an algebraic rewrite of A1, not a new mechanism.
- Same-mesh comparison: retained PROVED in -04. The same-mesh reference is exactly L_n², with L_n an odd-cosecant sum. The pointwise deformation error is≤π²n/(2|j−k|²), including adjacent indices nearπ; summation, endpoint and normalization yield |Λ_c−L_n²|≤54. Independent route agent reconstructed this analytically. The actual k=n deformation is nonzero; using actual endpoint weights in both sums avoids a false vanishing argument.
- A coarse mean-value derivative estimate near the adjacent upper endpoint would produce an excessive bound; exact subtraction of the rational summands gives the needed product of the two gaps. This is a discarded estimate, not a refuted A2 candidate or a PD-N.

## Completed ordered results

1. `PD-T?proof-attempts-2-codex-01`: for every n≥2, Λ_c≥(4/π²)log²n−54, hence≥(4/π²)log²n−80log n. This closes(i), with a stronger constant additive lower loss. The global KL theorem alone supplies the previously known upper asymptotic.
2. `PD-T?proof-attempts-2-codex-02`: for every n≥2, (4/π²)log²n−54≤Λ_c≤(4/π²)log²n+(12/π)logn+63, hence the absolute leading-term error≤95logn. This closes(ii) with explicit constants.
3. `PD-T?proof-attempts-2-codex-03`: for every n≥2, |Λ_c−(4/π²)log²n−b logn|≤68 with the requested b. This closes(iii). The key locally proved one-dimensional estimate is |L_n−(2/π)(logn+γ+log(8/π))|<2/n.

Supporting result `PD-T?proof-attempts-2-codex-04` has its own theory file and PROVED status; it is not used to relabel an unresolved source target. The full A3 constant, its parity independence, κ, and its finer remainder remain OPEN. A2 is done; the next active target belongs to root's ordered plan.

## Actual computations and evidence

Executed from repository root:

```text
python topics/padua-proof-attempts-2-20261101/code/a2_exact_check.py > topics/padua-proof-attempts-2-20261101/outputs/a2_exact_check.json
python topics/padua-proof-attempts-2-20261101/code/a2_sanity.py > topics/padua-proof-attempts-2-20261101/outputs/a2_sanity.json
```

Python3.12.14, SymPy1.14.0; exact cyclotomic quotient fields. n=1,…,6: all83 corrected-kernel simplifications, all6 coincident-endpoint checks, all6 positive-sum identities, and all6 same-mesh square identities pass. No floating tolerances and no Vandermonde/kernel code imported. First execution hit an ANP-versus-Python-int equality-coercion assertion at the endpoint; converting the expected integer to the same field fixed the checker, and the full run then passed. This was a checker-type mismatch, with no mathematical identity failure. Script SHA256 `94438117d4510b248beaac3e22afb23c159c21d107e17d300206b73751be4101`; developer receipt SHA256 `91db451c362d59c8bd1d155b10e0e5da275d62cced0e165b82cff7242fcc3d0e`,2067bytes.

NumPy2.3.5 longdouble (64-bit mantissa): MEASURED sanity n=2,…,64 and128,256,512,1024; maximum observed |Λ_c−L_n²|=1 and maximum observed absolute b-remainder≈1.955813, both comfortably inside the proved loose constants. The values at n=64,128,256 agree with pinned T2 longdouble values within3e−16; this is a sanity check only. At n=1024, Λ_c≈29.81522415101805 and the remainder after leading and b is≈1.848524867410685. No fit was performed and these numbers play no role in the proof. Sanity script SHA256 `8ca20d9690664430fe596ebdda881183034ef6e1ea81ca3bd841d9c2bfbb0649`; receipt SHA256 `caf52a027f271f0f47ab07ed4289ca2115618aa2970290d2d10d89b90da59b4f`,19691bytes.

The independent mathematical route agent recorded its own handwritten reconstruction in the topic's separate `independent-checks-a2.md`. A different agent `/root/input_manifest` then actually reran BOTH scripts, exit0, producing `outputs/a2_exact_independent.json` and `outputs/a2_sanity_independent.json`. Both outputs are byte-identical to the developer receipts with the SHA256 values above. Its separate receipt is `../independent-execution-a2.md`. Neither code inspection nor the hand proof was counted as that rerun. These supplement, and do not replace, the required Claude audit.

## Runs needed

- Actual independent exact and sanity reruns are complete, with separate `independent-execution-a2.md` receipt; no computation remains needed for A2 development.
- Required Claude audit of all written A2 proofs at root's final candidate SHA.
- For any later A3 work, first prove existence and determine the limit of the bounded difference Λ_c−L_n²; boundedness alone does not imply convergence. No A3 status upgrade here.
