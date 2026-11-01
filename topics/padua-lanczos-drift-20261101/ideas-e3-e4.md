# E3/E4 candidate memory and novelty gate

Codex mathematical developer; requested `gpt-6.1-sol`, xhigh, actual variant/effort not separately exposed. Rules/base read at `806cc7b4509fd93bae652f9545d32d95529f8281`, branch `codex/padua-lanczos-drift-20261101`. New files only; no allocation of final global IDs, shared-state mutation, Git operation or handoff by this subagent.

## Gate performed before mechanism development

Scanned the complete `state/IDEAS.md` headings, IDs, aliases and summary/disposition rows in bounded views, and read its obstruction/disposition tables, including the historical seed dispositions, canonical bivariate entries IDEA-077–176, MZ, lattice and programme-ideas warnings. Broad tables were also searched for span, selection, staircase, inverse, triangular, Krylov, residual, reorthogonalization, orthogonality and commutator. Searched the bivariate theory, registry/negative-results records, old topic report/SPLITS and L2 candidate/review records for those mechanisms and synonyms. Read `literature/INDEX.md` metadata/scope rows and relevant full rows; did not read all literature fulltexts. One attempted search named nonexistent `tracks/bivariate-lanczos/PROOF_STATUS.md`; the existing theory/negative-result records were used instead. A failed path search is not evidence of absent prior art.

Shortlist: PD-T029–055 (in particular full detailed reading of PD-T029/PD-T032/PD-T041/PD-T046/PD-T047/PD-T050/PD-T051/PD-T053/PD-T054/PD-T055); PD-N013/PD-N015; summaries of the remaining PD-T029–080 and PD-N007–031 to check neighboring claims and negative scopes. Read the old topic report and L2 sections of SPLITS; L2 candidates; L2 prior-art and reconstruction reviews. Nearest IDEA records are IDEA-127/130/134/140 (node coefficients, propagators and exact growth), IDEA-147/148/150/151 (formed sections, full-reorth drift and tested selections), and IDEA-079/084 (original reorthogonalization/commutator seeds). The complete canonical summary of each was read; linked detailed L2 records and the theory above supply the hypotheses.

Literature shortlist: LIT-241–243 (Barrio–Peña–Sauer: one coordinate per polynomial, selection freedom and inverse triangular error bounds), LIT-280–284 (Hokanson / Zhu–Nakatsukasa: exact span versus orthogonality and fitting), LIT-251 (Zhang–Su–Li fitted-value bound), LIT-253/255/256/257 (one-operator backward/subspace context), and the Simon/Jia–Li template via the existing L2 review. Existing records include WebFetch digests, secondary accounts and pending fulltexts; these reading limits are inherited. No new PDF was opened, no new external search conducted, and no historical novelty asserted.

Applicable obstructions read in full: partly formed J-columns (OBST-03); full versus truncated orthogonalization (OBST-07); finite exact certificates are not asymptotic statements; PD-N013's full-reorth drift; PD-N015's four-rule failures do not quantify over every selection; (C) gives acyclicity but not residual-size control; the K recursion contains reorthogonalization coefficients and gives no universal lower bound. Moment-cone, cubature and Givens obstructions were screened as neighboring mechanisms; none supplies an E3/E4 conclusion.

The exact E1 setup was coordinated with its developer: T_24 and rationally rotated Q_24, BJ/dev, mirror, alt and pivot rules; aggregate preprojection residual sensitivity; normal projector; no automatic reduction of arbitrary aggregate directions to a standard per-operation error realization. New E1 analytic records are related dependencies only where explicitly cited, not inherited measurements.

## IDEA?drift-codex-10 — Polynomial-surrogate residual certificate and filtered minimax selection

Aliases: computed polynomial surrogate; normalized node inverse; finite staircase certificate.

- Question / scope: obtain a computable sufficient selection criterion for span accuracy, keeping the unrestricted staircase theorem visible.
- Mechanism and hypotheses: computed-coefficient polynomials still form a triangular basis of Π_s; their node-row difference from Qhat is a forced triangular recurrence. A Gram bound converts its norm into a projector-distance upper bound. Minimize a row-normalized exact inverse score over (C)-staircases after filtering by χ.
- Closest registry entries (read in full): IDEA-127/130/134/140 and their PD-T029/032/037/041 records; IDEA-147/148/151 and detailed L2 records PD-T046/047/050/051/053/054/055, PD-N013/015.
- Separation criterion vs closest entry (and observation that falsifies it): prior node identities/amplification observations do not alone establish the computed polynomial surrogate's exact range or a span upper certificate. A missing triangular leading coefficient, a non-admissible parent, or a source outside the declared residual relation kills this proof. A matching predecessor theorem for this exact span certificate erases any distinction; no novelty is claimed.
- Literature baseline and search limitations: BPS inverse triangular error bounds and selection freedom are known; the additional output quantity is span distance. Existing L2 review separates V+A fitting/orthogonality results from span accuracy. Primary-literature coverage is incomplete as stated above.
- Applicable obstructions and exact hypotheses broken: does not claim (C) bounds inverse norms; does not infer drift from large inverse entries; χ is retained; the source model is explicit; empty acceptance sets remain failures to certify.
- Novelty gate verdict: variant with a documented output distinction; no historical priority claim.
- Cheapest decisive test: prove triangularity of the surrogate and check the row normalization/source scaling before any benchmark computation.
- Kill criterion written before testing: reject the certificate if the surrogate need not span Π_s under the stated support/admissibility assumptions, or if the projector bound needs a hidden coefficient-closeness hypothesis. Reject a global safety claim if it has no independent bound on K and χ.
- Test discriminability: the symbolic proof addresses precisely those two possible gaps; it does not test whether any frozen benchmark selection passes the score.
- Actual test results and committed evidence: analytic proofs in PD-T?drift-codex-10/11. No score computation or computer proof claimed. An independent mathematical checker accepted the span/inverse/first-order reconstruction and requested a computability representation qualification; that qualification was applied. Parent owns the check record and audit.
- Disposition and precise rejected scope, if any: retained sufficient criterion; unrestricted polynomial staircase safety remains OPEN. Family application is CONDITIONAL on explicitly unverified polynomial score/χ/source bounds.
- Disposition reason: conditional application, not an all-degree success. A computable sufficient condition is substantive but may reject all available candidates.
- Canonical theory / negative-result ID: PD-T?drift-codex-10 and PD-T?drift-codex-11.
- Topic / audit / history: E3; analytic development 2026-11-01; Claude audit pending.

## IDEA?drift-codex-11 — Minimize an unqualified inverse norm and omit χ

Aliases: raw-L minimax; unnormalized propagator score; staircase structure alone.

- Question / scope: can the informal phrase “minimize max ||L^*(-1)||” directly yield O(u poly(s)) drift?
- Mechanism and hypotheses: use the old unnormalized L and assume its inverse score is the relevant dimensionless response.
- Closest registry entries (read in full): PD-T032/041 and IDEA-134/140; PD-T046's explicit normalization factor and IDEA-147; PD-T054/IDEA-151.
- Separation criterion vs closest entry (and observation that falsifies it): a correct criterion must preserve the source budget under coordinate scaling and row normalization. Failure to distinguish L^*(-1) from Lbar^*(-1)=L^*(-1)diag(1,β) erases the alleged improvement.
- Literature baseline and search limitations: BPS triangular scaling is prior art; PD-T041 explicitly records coordinate scaling. No novelty claim or new external search.
- Applicable obstructions and exact hypotheses broken: near-breakdown χ can be arbitrarily large; (C) does not bound it or the inverse. PD-N015 preserves failures even for staircase rules.
- Novelty gate verdict: unqualified variant, consolidated into IDEA?drift-codex-10 after correction.
- Cheapest decisive test: write the normalized residual f_k/β_k and transform L.
- Kill criterion written before testing: if a factor 1/β_k remains in the source budget, the χ-free reading is unsupported and must not be claimed.
- Test discriminability: this is a scaling/normalization test, not an empirical safety test.
- Actual test results and committed evidence: the source is f_k/β_k; local budgets give χ. PD-T?drift-codex-10/11 state the corrected score and a χ filter. No counterexample theorem is invented from a failed route.
- Disposition and precise rejected scope, if any: consolidated/corrected; unconditional χ-free or (C)-alone theorem not pursued. Existing stronger safety claims remain OPEN or retain their old measured failures.
- Disposition reason: equivalent after correct normalization; a separate PD-N is not warranted merely by this correction or abandonment.
- Canonical theory / negative-result ID: no separate ID; correction in PD-T?drift-codex-11.
- Topic / audit / history: E3; retained failed route, 2026-11-01.

## IDEA?drift-codex-14 — Every-rule, every-error positive BJ drift lower bound

Aliases: pathwise universal obstruction; noiseless quantifier test.

- Question / scope: does BJ's missing J information force positive drift for every permissible rule and every upper-bound-model error realization?
- Mechanism and hypotheses: interpret the unfixed PD-T055 quantifier pathwise over all allowed errors, while allowing zero errors and exact-real full projection.
- Closest registry entries (read in full): IDEA-148 and PD-N013 (tested real runs), PD-T047 (identity only), PD-T055 (unfixed universal target).
- Separation criterion vs closest entry (and observation that falsifies it): a lower bound must survive the zero-error branch to have this pathwise quantifier. An exact run with correct spans kills that interpretation; it says nothing about deterministic IEEE storage.
- Literature baseline and search limitations: standard perturbation sets include zero; no literature priority claim. The existing L2 review never proved a universal lower bound.
- Applicable obstructions and exact hypotheses broken: the commutator recursion has no positive source lower bound. Working-precision storage is explicitly relaxed here; this refutation must not be transferred back to literal IEEE runs.
- Novelty gate verdict: variant/quantifier correction to the supplied OPEN target.
- Cheapest decisive test: exact full Gram–Schmidt on a non-product unisolvent measure with all errors zero.
- Kill criterion written before testing: zero defect and exact implicit section contradict every positive proposed lower bound in that model.
- Test discriminability: decides the pathwise perturbation-model quantifier only; does not decide worst-case or actual IEEE quantifiers.
- Actual test results and committed evidence: analytic proof for every admissible measure, with a row-factor proof for explicit T_3, in PD-N?drift-codex-14.
- Disposition and precise rejected scope, if any: REJECTED: refuted for the stated pathwise model. Original PD-T055 remains OPEN and unchanged.
- Disposition reason: refuted by the zero-error exact-real branch, not by an asserted IEEE execution.
- Canonical theory / negative-result ID: PD-N?drift-codex-14.
- Topic / audit / history: E4; literal-old versus new-proposed scope preserved in the theory file; audit pending.

## IDEA?drift-codex-15 — Prior-vector subtraction repairs a missing J-product under adverse sources

Aliases: information-never-formed local obstruction; fixed-degree quotient invariant.

- Question / scope: can arbitrary projection coefficients, using only already permitted BJ products, repair exact J-closure after a source in one degree-two product?
- Mechanism and hypotheses: fix the exact orthonormal degree-one prefix, fixed degree-two raw products, no revision of earlier vectors or extra products; allow arbitrary finite prior-subtraction coefficients and passes.
- Closest registry entries (read in full): IDEA-148/151, PD-T047/050/053/055 and PD-N013/015. Prior records give recursions and tested failures, not this all-coefficient finite quotient calculation.
- Separation criterion vs closest entry (and observation that falsifies it): a joint-span identity independent of projection coefficients gives a genuine every-rule statement within this fixed-degree class. A permitted operation adding a vector outside the current product plus prior span, or revising a parent, kills that invariant.
- Literature baseline and search limitations: elementary quotient-space linear algebra applied to the old missing-product mechanism. No historical novelty claim, no new external search.
- Applicable obstructions and exact hypotheses broken: strengthens tested-schedule failure to all arbitrary coefficients within one degree; does not freeze the coefficients in the old clamped recursion or assume they never change K.
- Novelty gate verdict: variant with precise rule-class distinction.
- Cheapest decisive test: derive the completed degree-two span with one source and compute its angle exactly on T_3.
- Kill criterion written before testing: if later allowed raw products restore the missing exact direction, the adverse source cannot certify persistent closure failure. If the defect remains only O(u), do not promote it to the exponential PD-T055 target.
- Test discriminability: exact finite span identity decides closure repair for all the declared coefficient rules; it does not decide amplification or IEEE realizability.
- Actual test results and committed evidence: span V⊕span{w+εe}, ||w||²=28/115; exact ten-row sum certificate in PD-N?drift-codex-15. A temporary SymPy calculation helped derive the rational expressions; the proof contains all arithmetic and is independent of that program. The parent's distinct mathematical checker independently recomputed all moments, norms, the J decomposition and the u inequalities using Fraction arithmetic, reporting PASS; its durable command/output/hash record awaits parent integration. No computer-proof status claim.
- Disposition and precise rejected scope, if any: REJECTED: refuted for the claimed exact-closure/o(u) remedy against all admitted aggregate sources. The obstruction itself is PROVED; O(u poly(s)χ) stability is not refuted.
- Disposition reason: every permitted rule has the same completed span, which has θ_2≥2u and δ_J(1)≥u for the specified relative source.
- Canonical theory / negative-result ID: PD-N?drift-codex-15.
- Topic / audit / history: E4; analytic fixed-degree development, 2026-11-01, audit pending.

## IDEA?drift-codex-16 — Extend the quotient invariant to exponential every-rule drift

Aliases: multi-degree information obstruction; universal adverse-source amplification.

- Question / scope: prove the strong PD-T055-type result for every projection-only rule on one explicit non-product family, with an adverse source and controlled χ/reference conditioning.
- Mechanism and hypotheses: propagate the fixed-degree missing-direction quotient across many degrees while allowing the parent basis to change under earlier projections.
- Closest registry entries (read in full): PD-T041's exact finite inverse growth; PD-T047/050's coefficient-dependent residual recursion; PD-T055's OPEN target; IDEA-140/148/151 and new IDEA?drift-codex-15.
- Separation criterion vs closest entry (and observation that falsifies it): must prove invariance or a lower response bound after **all** allowed earlier basis changes, not just arbitrary coefficients within a degree whose parents are fixed. A rule-dependent parent change that can cancel the chosen direction kills this proof route unless controlled.
- Literature baseline and search limitations: no new external search. Existing prior-art reviews are bounded and do not prove absence of such a theorem.
- Applicable obstructions and exact hypotheses broken: K changes with reorthogonalization; large unprojected inverse does not imply large normal drift; arbitrary aggregate sources need not be per-operation realizable; zero errors prohibit a pathwise positive lower bound.
- Novelty gate verdict: continuation of the existing OPEN target, not a newly proved mechanism.
- Cheapest decisive test: identify a multi-degree invariant that is unchanged by every permitted parent-gauge change; alternatively construct a valid cancelling rule.
- Kill criterion written before testing: reject a universal deduction if it treats coefficients as invariant, neglects normal projection, or switches from “some adverse error” to “every actual error.”
- Test discriminability: failure of that argument leaves the theorem OPEN; it does not refute the theorem.
- Actual test results and committed evidence: the fixed-degree invariant is proved in -15; it does not survive arbitrary parent revision by the argument given. No multi-degree lower bound obtained.
- Disposition and precise rejected scope, if any: deferred/OPEN, not REJECTED. Resume with a genuinely invariant quotient or controlled parent-gauge argument plus a realizable error generator.
- Disposition reason: missing substantive mathematical step; insufficient evidence is not a negative theorem.
- Canonical theory / negative-result ID: original PD-T055 remains the durable OPEN target; no new PD-N for an unfinished proof route.
- Topic / audit / history: E4; all stronger wording retained as OPEN, 2026-11-01.
