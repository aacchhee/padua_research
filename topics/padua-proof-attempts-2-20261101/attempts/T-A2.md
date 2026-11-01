# T-A2 — corner leading and logarithmic coefficients

Developer: Codex `/root/a2_develop`, requested gpt-6.1-sol xhigh; runtime-resolved metadata is not separately exposed. Rules first read at `a09d910ae7d5526b1e216066421a0bee7fc20da4`, reread unchanged at `b3c333b6519740c21953ed41501a66d37768c1f2` and `818ca4ad0942eb4743860f913a299ff30d959dae`. Authoritative programme input is pinned throughout to `9bd14a6d2c4da69139a10107d8a787f2be0c5c9e`; no older working-tree wording supplies an assumption.

## Start, stop conditions, and current state

Pre-computation start: **2026-11-01T09:06:18Z**. Approximate five-hour box ends 14:06 UTC; literature/gate work preceded this timestamp. No numerical/exact computation had run at registration. Ordered deliverables are (i) corner lower bound with leading coefficient 4/pi²; (ii) two-sided explicit O(log n); (iii) b=(8/pi²)(gamma+log(8/pi)) with explicit O(1). Each substantive completed part gets its own theory record.

Kill criteria written before any exploratory computation: an exact failure of a proposed identity rejects only that identity; an unbounded comparison error rejects a proposed uniform comparison, not A2; any asymptotic counterexample must be supported analytically or by certified evidence before a scoped PD-N. Stop at (iii), a scoped refutation, or the five-hour box. A supporting lemma alone is not a stop or a status upgrade. Any finite floating check is MEASURED. Consequential exact/interval checks require an actual independent rerun by another agent.

Audit interruption: root reported the arrival of part-1 Claude audit at `95279b833bca5967fcf47c1b71a56ff622185b4e`; all A1-dependent work paused immediately while independent literature reading continued. Root reviewed the full audit, merged it via `818ca4ad0942eb4743860f913a299ff30d959dae`, and authorized resumption. A1 had no mathematical finding requiring adaptation. Per the user's requested literal reference the dependency remains **PD-T?proof-attempts-codex-01 (audit pending)**; dated qualification: audit-01 accepted A1 at `95279b8`, while part-1 disposition records are pending. No dependent claim was promoted during the pause.

Current target status: OPEN; no computation or theorem is claimed at this checkpoint.

## Relaxed registry and predecessor gate

Read the complete `state/IDEAS.md` (all 496 lines), including all headings, IDs, aliases, summaries, every source/campaign/current disposition table, all obstruction tables, and the programme rows. Read `literature/INDEX.md` before any PDF. Search scope: state, topics, tracks, literature, including negative results. Terms: `corner`, `Lebesgue`, `shear`, `cotangent`, `Kolomo`, `Lomako`, `log.coefficient`, `harmonic`, `Chebyshev.*sum`, `rhombus`, `Dirichlet`, and `absolute-cardinal`.

Closest full shortlisted entries read: programme IDEA?programme-ideas-claude-17 (its entire candidate entry at pinned programme SHA), source theory -04, OPEN_TARGETS A1/A2/A3/A4, decisive-gen4-2 T2 source and narrative; part-1 A1 theory/attempt; IDEA-047/048; MZ IDEA-065 through -071 and linked PD-N005 in full. The absolute-cardinal L1-column obstruction concerns CC weighted L2 estimates, not the present finite point value. The programme's projection-constant route is capped at 16/pi⁴ and cannot prove the desired corner coefficient; this route is excluded. The maxima-cell uniqueness obstruction does not bear on a point evaluation. Finite fits do not establish b or a remainder. No new programme, priority, or historical novelty claim is made: this is completion of an already registered target.

Verdict: registered sharpening of a classical kernel identity, not a candidate novelty claim. Cheapest decisive test: simplify the A1 summand at the node angles, treating endpoint limits separately, then compare a regularized staggered Cauchy sum with an explicitly analyzable one-dimensional product. Before adopting a comparison, test its precise bounded-error statement rather than refitting b.

## Literature coverage

Kolomoitsev–Lomako, *Asymptotics of the Lebesgue constants for bivariate approximation processes*, arXiv:2009.07114v1, corresponding to Appl. Math. Comput. 403 (2021), [primary PDF](https://arxiv.org/pdf/2009.07114): full 16-page paper read through the web PDF text, including introductory definitions, all main statements, Lemmas 3.1–3.7 and proofs, section 4 and references. The theorem-level load-bearing locator for the global upper bound is Theorem 2.1, printed p.4, with its Padua specialization immediately below. Its discretization comparison is Lemma 3.5, printed pp.10–11, especially (3.20); the parity-subgrid ingredient is Lemma 3.6, (3.29), printed pp.11–12, used in (4.5)–(4.6), printed pp.14–15. These estimates leave an O(log n) error and do not identify b. Reading was completed before borrowing a method. Direct shell download was denied HTTP403; no proxy bypass was attempted and no third-party fulltext is committed.

Bos–Caliari–De Marchi–Vianello–Xu, *Bivariate Lagrange interpolation at the Padua points: the generating curve approach*, JAT143 (2006), 15–25, [author preprint](https://www.math.unipd.it/~marcov/pdf/PaduaCurve3.pdf): primary definitions and Theorem 3, printed pp.10–12, with the displayed sum/integral estimates inspected. The source proves global O(log² n), with unspecified constant. The normalized A1 identity is locally proved in the named part-1 dependency. No full-paper reading of Bos2006 is claimed.

## Candidate memory

- Prescribed shear/product-U route: retained as an available route; its generic triangle inequality would lose cross-term information, so no b conclusion from it yet.
- Node-angle rational simplification: under development, with the coincident endpoint treated by its A1 limit. This is an algebraic rewrite of A1, not a new mechanism. Kill test: exact mismatch against A1 at any degree/node/corner.
- Same-mesh comparison: not yet accepted; must prove a uniform total error before it can supply (iii). Kill test: a comparison error growing with n or an unhandled near-diagonal endpoint.

## Runs needed

Independent exact/interval rerun of any consequential checks once code exists; required Claude audit of all written proofs. Computation commands and result paths will be appended when actually executed.
