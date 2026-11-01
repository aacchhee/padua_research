# Audit04 scope review — response03 A03-L2/L3

**ACCEPT within this bounded scope: A03-L2 and A03-L3 RESOLVED; no new
high, medium or low findings.** This is an independent review of Claude's
corrections, not a repeat of the campaign or acceptance of unexecuted repairs.

- Auditor: Codex independent mathematical subagent, configured `gpt-6-astra`
  high; resolved serving variant/effort independently unexposed. 2026-11-01.
- Rules/read head: `39b3c5d8690566ce461e6e3a0a628e772a695dbc`.
- Candidate: `02bd97b892ed409ec64e9b281130c71a85e914e9`.
- Delta base, previous published step: `3cca9b929ac006a5ed4295b3beba909dfd602271`.
- Candidate-to-read-head diff is only handoffs09/10. Checked scientific inputs
  equal candidate blobs; hashes and sizes are in
  [audit-04-scope.json](../../evidence/audit-04-scope.json).
- Owned outputs: this report, `scope_check.py`, that receipt. No developer,
  registry, frozen evidence or Git-state edits. Root owns L1, integration,
  full regeneration and publication.

## A03-L2: minimum-comparator target

Record05 line55 correctly defines squared bounds on the same full formal
scalar-graph capacities, at degree12 on rotQ24:
`L_X² <= K_X² <= U_X²`. Capacities and the represented square roots are
nonnegative. Thus the strict target is equivalent to

    K_BJ² > 100 min(K_alt², K_pivot²).

For either comparator X, the proposed proof certificate gives the chain

    K_BJ² >= L_BJ² > 100 U_X² >= 100 K_X²
                              >= 100 min(K_alt², K_pivot²).

The proposed refutation certificate instead gives

    K_BJ² <= U_BJ² <= 100 min(L_alt², L_pivot²)
                  <= 100 min(K_alt², K_pivot²).

Equality suffices to refute the strict `>` target. These are sufficient
certificate conditions; the prose's “needs” is understood in this described
interval-certificate route, not as excluding another proof method. A reversal
using only L_alt proves `K_BJ <= 10 K_alt`, which refutes that named-comparator
target only. The exact illustration `(9,1,1/10)` has `81 <= 100`, but
`9 > 10 min(1,1/10)=1`; it defeats the old inference. The added equality
check `(10,1,2)` confirms the corrected weak refutation inequality.

The displayed ratio62.09 below100 remains insufficient evidence to prove or
refute the target. No change to the MEASURED experiment, INCONCLUSIVE test,
PARTIAL two-conjunct target or OPEN rotQ24 conjunct occurs. The script compares
the entire old/new record after removing exactly the rotated-target row and
the new History line: all other lines agree. E1.md's existing both-comparator
reversal was inspected as contextual support; its aggregate model and frozen
strict inequality are not silently substituted for record05's scalar model.

## A03-L3: reference information versus geometry

Let P=R_(<=p)R_(<=p)^T, q=qhat_p in the stored span S, and a=||Pq||>0.
The guard `|gamma_p|>=1/2` ensures a>0 in the exact reference model.
The change **before** normalization is `c=Pq-q=-(I-P)q`. The actual
normalized change is `d=Pq/a-q`, so these vectors need not agree. If N is
the orthogonal normal projector of S, then

    Nc = NPq,       Nd = NPq/a,

because Nq=0. Consequently an outside-span change occurs exactly when the
normal component is nonzero. External construction of P alone supplies no
such condition. This independently reconstructs the corrected criterion.

In reference coordinates, use q0=r0, q1=(3r1+4r2)/5,
q2=(4r1-3r2)/5 and p=1. Their Gram matrix is the identity, gamma=3/5,
Pq1=3r1/5 and the normalized replacement is r1. The two corrections are
`-4r2/5` and `2r1/5-4r2/5`; both are nonzero and lie in the stored span.
The checker verifies these identities exactly, plus the near-identity rational
example with cosine9999/10001 and sine200/10001. These are algebraic examples,
not alleged IEEE trajectories or newly run repair experiments.

The new sentence distinguishes reference information from the conditional
outside-span geometry and requires the run to record the normal component.
“R17a type” is an in-span classification, not equality to R17a's particular
prefix algorithm. Finite precision/reference error still requires the already
specified quality records; a nonzero residual alone does not prove efficacy.

Whole-file comparison, excluding only the separation paragraph and its new
History line, establishes that R17a/R17b recipes, the gamma guard, H17,
kill/survival thresholds, double storage, deferred disposition, no-run and
no-novelty statements are unchanged. PD-T055 remains OPEN. No lower bound for
all degrees or universal reorthogonalization obstruction follows here.

## Coverage, execution and limitations

Read AGENTS.md, agents/WORKFLOW.md, agents/codex/CODEX.md; handoff10;
audit03/response03; latest LOG entry; complete record05 and ideas-e3-e4;
the previous E34 audit03 report; E1's frozen comparison section. Inspected
the candidate diff and exact preservation of unchanged text.

Read the full783-line state/IDEAS.md, including every obstruction/disposition
table, in bounded views (re-read truncated portions). Read full linked
predecessor records PD-T055, PD-T043, PD-N013 and PD-N016; relevant full L2
candidate entries203/204/207/210 and their amended dispositions. The complete
local IDEA14–17 entries preserve the quantifier/fixed-prefix/deferred-route
limits. This satisfies the idea-scope reading obligation; no new candidate,
mechanism, priority or novelty claim is proposed. No external paper was opened
or fresh literature completeness asserted.

Fresh independent execution from `/workspace/padua_research`:

    python3 -B topics/padua-lanczos-drift-20261101/checks/audit-04/scope_check.py

PASS under Python3.12.14, standard-library Fraction arithmetic, no seed or
external dependency. This uses no developer or earlier-audit implementation.
An initial inline version of the same elementary checks also passed; the
committed standalone checker was then executed and generated the final receipt
with command, source hash, input identities and exact rational results.
Read-only Git show/diff and cat/sed/rg supplied provenance and coverage.

These elementary calculations corroborate the written logical reconstruction;
they are not a finite computer proof of new capacity bounds. Existing endpoint
proofs, all-degree targets, repair efficacy, actual rounding realizability,
storage delivery and other audit scopes are not revalidated by this report.
