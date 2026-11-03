# R4 retained candidates and scoped G7 outcome

2026-11-03. Rules/input `8a1f394739293953e1566fd24a0a193cc78ff26f`; Codex, assigned gpt-6-astra ultra for mathematics. Full gate/search scope and pre-execution sequence: [attempt](../attempts/r3-r4-comparison.md). No historical novelty claim.

## IDEA?argmax-effective-codex-04-envelope — Precisely formulate IDEA-319's envelope class

Aliases: G7; generating-curve numerator factorization; envelope times convex sum.

- Question / scope: does an admissible generating-curve regrouping yield a useful sign-stable envelope for lambda on specified cells, uniformly in n?
- Mechanism and hypotheses: IDEA-319's proposed common numerator/envelope extraction; the admissible factor class and cells have not been specified.
- Closest registry entries (read in full): IDEA-319's original and final records, IDEA-206, IDEA-316/327 and their cardinal/primitive context.
- Separation criterion: an explicit identity whose admissible nonnegative factors carry a comparison stronger than the existing triangle majorant. An identity merely rewriting lambda as E times lambda/E, or partitioning by every cardinal zero set, supplies no such separation.
- Literature baseline and search limitations: literature INDEX and LIT-312/379/388 records/addenda inspected; no fresh historical novelty claim or 1-D theorem transfer.
- Applicable obstructions: PD-N079 forbids standalone coset-maximality of S; the new G7-F result forbids individual fixed signs on coarse diamonds only.
- Novelty gate verdict: **variant with difference** only as an explicit operationalization of IDEA-319; no successful new mechanism claimed.
- Cheapest decisive test: write the allowed envelope class and cell geometry first, then exact n4 sign checks on the factors actually required by that identity.
- Kill criterion written before testing: preserve original “kill if no cell-wise sign-stable envelope exists at n=4.” It is presently ill-posed because its quantifier domain is unspecified; a failed guessed identity cannot establish the universal negation.
- Test discriminability: unrestricted positive envelopes and sign-cell refinements are tautological, while forbidding all of them needs extra hypotheses. The bounded subtest below supplies those hypotheses explicitly and applies only there.
- Actual test results: original criterion cannot receive PASS or KILL as stated. The fixed-sign-cardinal submechanism is separately refuted below.
- Disposition: **deferred / OPEN**. Resume with a concrete identity, allowed factors, normalization and fixed partition, before spending on larger-degree signs.
- Disposition reason: deferred because no mathematical predicate presently distinguishes the intended useful class from trivial envelopes. No administrative PD-N is created for the ill-posedness diagnosis.
- Canonical theory / negative-result ID: none for this broad target; separate scoped obstruction below.
- Topic / audit / history: inherited original criterion preserved; dated operationalization and exact result retained, Claude audit pending.

## IDEA?argmax-effective-codex-04-fixed-sign — Fixed signs of individual cardinals on coarse complementary diamonds

Aliases: G7-F; positive common-factor cardinal representation; coarse cell sign elimination.

- Question / scope: at every n and standard complementary diamond, can each cardinal be assigned a constant sign, equivalently can the proposed individual-cardinal representation epsilon_B E a_B use fixed epsilon_B and nonnegative factors throughout that cell?
- Mechanism and hypotheses: coarse cells |qx-j|+|qy-k|<1, j+k odd. Preserve each individual cardinal before taking absolute values; no regrouping or finer partition.
- Closest registry entries (read in full): IDEA-319, IDEA-318/321's concrete diamonds, and PD-T101. This is a specified sufficient submechanism, not an interpretation declared equivalent to IDEA-319.
- Separation criterion: fixed signs permit removing absolute values with one sign vector per geometric cell. A cardinal with two opposite exact signs in one cell kills that property.
- Literature baseline and search limitations: no external theorem is used and no priority claim made.
- Applicable obstructions: coarse geometric cells need not be cardinal sign cells; no prior obstruction is imported as a proof of this precise statement.
- Novelty gate verdict: **variant with difference**: explicit factor/sign/cell hypotheses make a previously unspecified test falsifiable.
- Cheapest decisive test: n4 rational corner-node cardinal L00 on a simple coordinate line.
- Kill criterion written before testing: two opposite exact values of one cardinal within the same standard complementary diamond refute this mechanism only.
- Test discriminability: exact rational substitutions and exact angle inequalities establish the requisite signs and shared cell; sampling is not needed.
- Actual test results: L00(x,0)=(x²-1)(2x²+2x-1)/10. Values 4/405 and -11/4096 at x=1/3 and3/8, both in D(2,3), give a complete analytic obstruction.
- Disposition: **REJECTED: refuted**, only for individual fixed signs / the displayed nonnegative-factor representation on these coarse cells.
- Disposition reason: the two exact opposite signs make a cellwise fixed sign impossible. Regrouping, refined sign cells and the whole generating-curve route remain outside scope.
- Canonical negative-result ID: [PD-N?argmax-effective-codex-04](../theory/argmax-effective-codex-04-coarse-cell-sign-obstruction.md), **PROVED**, analytic proof; supplementary independent gpt-6-astra high reconstruction accepted, required Claude audit pending.
- Topic / audit / history: G7-F registered in the attempt before exact expansion. The result does not retroactively convert original G7 into a well-posed criterion.
