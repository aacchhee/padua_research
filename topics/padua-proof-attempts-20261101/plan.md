# Proof-attempt plan

Pinned authority: `../programme-ideas-20261031/OPEN_TARGETS.md` at
`cadb35066160e466cb1704b9791ad6f374446422`. No new programme or historical
novelty claim is proposed. User instructions restrict all writes to new files in
this directory and override ordinary shared-registry/ID preparation.

1. **T-A1** (at most about two hours): prove the all-degree corner formula,
   independently reconstruct its normalization, inspect the primary literature
   with a precise locator, and check degrees 1–6 exactly in SymPy. Stop at a
   written proof and exact checks, or at an exact mismatch (scoped PD-N).
2. **T-B5** (at most about two hours, starts after A1): prove support inclusion,
   dimension ≥3 and genericity using a rational algebraic rank model. Construct
   one exact rational witness for each n=2,…,6. Explicitly address disconnected
   real parameter domains; a nonzero analytic function on one component alone
   does not establish density on all components. All-degree extension optional.
3. **T-A5-partial** (at most about three hours, starts after B5): rerun the
   frozen certifier with a wrapper logging *all* `degenerate_max` calls and
   successful decisions, identify (n,z,Z), then prove exact vanishing and angle
   gradient identities, critical-point location and rigorous Hessian bounds for
   each successful decision. Distinguish the reconstructed numerical execution
   trace from the mathematical certificates. Leave the other four counting
   obligations OPEN; do not certify any maxima count.
4. Obtain actual independent reruns for consequential exact computations;
   preserve code, small evidence, versions, input/code identities and limitations.
5. Write exact old→new proposals against pinned PR #6 records, without applying
   them. Set AUDIT, commit as Andrey Chesnokov with Agent/Model trailers, push,
   and open a draft PR targeting `claude/programme-ideas-20261031`.

Only if all three targets finish with time remaining: bounded attempt note on
B1 or A2, without a stronger status than the written argument supports.

## Ownership and resources

Root owns Git, plan, LOG, proposed changes, evidence manifest and PR.
`a1_develop` owns A1 attempt, theory local number 01, `code/a1_*`,
`outputs/a1_*`, and optional local literature note. `input_review` is read-only
except for its own new `inputs-review.md`. Later allocations are logged before
writing. No agent changes an existing base file.

The execution environment is managed Linux at `/workspace/padua_research`.
No bridge to AC's Windows computer is exposed. The intended local result entry
will be retained under LOG's Runs needed, not written to another destination or
to shared RESULTS.md. No large output is planned; essential committed outputs
must be ≤1 MB each and ≤5 MB total.
