# PD-N?lanczos-frontier-codex-L4-01 — fixed old BJ lower cannot pass the absolute-envelope spectral certificate on rotQ24

ID kind: PD-N.
Aliases: fixed-lower envelope obstruction; post hoc Rayleigh diagnostic.
Split from: only the fixed-old-lower subroute of
`IDEA?lanczos-frontier-codex-L4a`, after all nine original positive-vector
upper tests failed. The scalar factor-ten target is independently proved
by the stronger full-output lower in the separate L4 theorem; this
fixed-old-lower obstruction remains valid.
Split into: none.

## Statement

Use the exact degree12 rotQ24 alternating full scalar envelope
`C=S^T D^(-1) S` defined in `l4-envelope-bound.md`, with all90 sources
and the complete local rho of PD-T138. Let G_R be exactly the old BJ
target90 greedy node-sign squared lower of PD-T141, unchanged.

The following finite inequalities hold:

    lambda_max(C) >= 13462955378,
    0 < G_R <= 100*13462955378.                              (1)

It follows that **no** certified upper B of this absolute-envelope
spectral value, `B>=lambda_max(C)`, can satisfy `G_R>100B`. In particular,
no choice of a positive vector v, including any vector not tested in the
original nine proposals, can make the bound
`B=max_i(Cv)_i/v_i` prove the strict factor-ten comparison when paired
with this fixed old BJ lower.

This is a statement about the named certificate method and fixed lower.
It does not assert `K_inf,BJ<=10K_inf,alt`, any upper on actual K_inf,BJ,
or any lower on actual K_inf,alt. A stronger BJ lower, a bound retaining
the final projector/sign constraints, or a different sharper upper can
still establish the original target. The envelope upper remains useful.

## Definitions

All notation and the full scalar graph are those of the L4 envelope
record and PD-T138. C is rational, symmetric and positive semidefinite.
For any nonzero rational vector v define the rational Rayleigh quotient

    R(v) = [sum_(k=1)^90 (sum_i S_ki v_i)^2/d_k]
           /[sum_i v_i^2]
         = (v^T C v)/(v^T v).                              (2)

The reported diagnostic uses retained positive integer proposal3 (and
proposal8 as a cross-check) from the failed upper search. It does not
search a new source realization or regenerate sources. Exact floor
comparisons of (2), rather than numerical eigenvalues, are decisive.

## Assumptions

Exactly the same rational grid, degree, fixed alternating selection,
monic positive pivots, operation order, exact q_0 and complete formal
relative-operation model as the L4 envelope record. Source h ranges1–90;
row0 is zero. G_R is read from the hash-pinned inherited BJ certificate,
not changed by this diagnostic.

For the computational part of (1), the exact assembly of S,d, the retained
v, rational products and floor comparison must be independently verified.
No empirical lower on an eigenvalue or trust in an unchecked boolean is
sufficient.

## Status by part

Overall status: PROVED, finite computer-assisted, for the specified
certificate pairing. Separate Claude scientific/protocol audit pending.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Rayleigh quotient (2) lower-bounds lambda_max(C) | PROVED, analytic | Direct real-symmetric variational argument |
| The two exact numerical inequalities (1) | PROVED, finite computer-assisted | Exact developer diagnostic and distinct independent floor/comparison checks |
| Exclusion of every envelope spectral upper paired with old G_R | PROVED | Immediate implication below; no stronger scope intended |

Candidate disposition: `REJECTED: failed` for the
**fixed-old-lower envelope subroute only**. The full-output BJ lower used
by the separate positive L4 theorem is outside this failed subroute.
No rejection of the original factor-ten target or of a new witness is implied.

## Negative-result scope

Attempted mechanism: `IDEA?lanczos-frontier-codex-L4a`, restricted to
combining the unchanged old BJ lower G_R with any upper of the exact
unprojected absolute envelope's spectral value lambda_max(C_alt).

Parameter range: the single frozen rotQ24 degree12 case; the complete
PD-T138 formal scalar graph; all90 sources; any valid upper of this C,
including all strictly positive-vector certificates. No all-degree,
universal-selection, actual-rounding or fitted-value statement is made.

## Depends on

- The L4 envelope record's definition of S,C and proved reduction
  `K_inf,alt^2<=lambda_max(C)<=max_i(Cv)_i/v_i` for v>0.
- PD-T138 for the exact full scalar source interpretation.
- PD-T141 for the unchanged exact attained BJ lower G_R and its source pins.
- The separately executed exact diagnostic and distinct independent
  regeneration/checker receipts for (1), listed below.

## Checks

The original medium producer `code/l4_envelope.py` regenerated all sources,
reproduced the old trace exactly, and retained all nine failed positive
vectors and the complete S,d arrays. Its receipt is
`evidence/l4-envelope.json`; source SHA-256 is
`0da27e69ddd3cff5ca23e3fcac764f53891ad164ffab20324540fd67d2faf901`.

After those failures root authorized a **separate post hoc diagnostic**
from the retained data. This is not a rewritten preregistered upper-test
outcome. The medium developer executed `code/l4_rayleigh.py`, SHA-256
`54399e4e2dea3a19d943130bf67e7549b16c98aac600e196ba932ba512069551`,
validating envelope/candidate identities and computing both rational
Rayleigh quotients without a source rerun. Its compact
`evidence/l4-rayleigh.json` receipt, SHA-256
`3309c5dba3bee00c4e93a166cfa626e1986f657010202d74b8c78692c69f4492`,
records floor13462955378 for proposal3 and proposal8 and both exact
`100 floor-R(v)>=G_R` comparisons. Exact rational values remain in
hash-manifested external files; the receipt gives the actual command.

The distinct supplementary reviewer separately regenerated all90 sources,
compared every exact S entry with the developer's run, reproduced the
old trace and BJ lower, and used `code/l4_independent.py` to recompute
the saved proposal3 Gram product. It additionally recomputed that product
by explicit scalar loops, evaluated the Rayleigh quotient rationally,
and checked `a<=R(v)<a+1` and `100a>=G_R` exactly. These are explicit
fields of `evidence/l4-independent.json`, not conclusions from a decimal
display. The checker is separately written and imports no producer
function; source regeneration shares the reviewed exact producer.

The independent report `independent-checks-l4.md` and its compact receipt
provide execution and source pins. Definitive checker SHA-256 is
`491be4db86f4a0c1ff369f4b51043d63944562d7ca522e60cd794ed4d70248ac`;
receipt SHA-256 is
`7c3c89a0f52a6cfbab4b98e8b00185932adf18e2f310330a942ca2e45a2abb3b`.
The mathematical worker read the
complete relevant source, final numerical receipt and proof before this
status was accepted. The main L4 theorem's Checks section records the
combined checker and the verifier-only portability amendment; saved
rational vectors, not future floating proposal agreement, define this
certificate. No execution by this mathematics worker is claimed.

## Sources

Full closest repository entries IDEA250 and PD-T138/140/141, and the
written L4a reduction. This is the already registered method's finite
obstruction, not a new sign/source mechanism. The complete source-reading
gate and original prospective timing deviation remain documented in
`ideas-l3-l4.md`. No external paper is a proof premise and no historical
priority claim is made.

## Proof or evidence

Because C is real symmetric, write an orthonormal eigenbasis u_j with
real eigenvalues lambda_j. For nonzero v,

    v^T C v/(v^T v)
      = sum_j lambda_j (u_j^T v)^2 / sum_j (u_j^T v)^2
      <= max_j lambda_j.

The identity `C=S^T D^(-1)S` gives (2), so all computations are rational.
The independently checked exact finite certificate shows

    a <= R(v) < a+1,  a=13462955378,
    0 < G_R <= 100a.                                        (3)

The first lower inequality alone proves
`lambda_max(C)>=R(v)>=a`; the strict upper in (3) merely identifies the
reported floor. For every B>=lambda_max(C),

    100B >= 100lambda_max(C) >= 100a >= G_R.

Thus `G_R>100B` is impossible. The positive-vector upper theorem in the
L4 record says every such vector supplies a B>=lambda_max(C), which gives
the universal positive-vector exclusion in the statement. This conclusion
does not turn the envelope into a lower bound for K_inf,alt: the actual
response set is smaller and final orthogonal projection was discarded in
forming C. Nor does a fixed attained BJ lower bound the capacity from above.
Those two missing directions are precisely why this is not a kill of the
original capacity comparison.

The analytic implication and numerical hypotheses (3) have both been
verified. They are scoped to this exact certificate pairing.

## Scope

This negative record excludes one exact certificate pairing, including
untested positive vectors. It is stronger than saying that nine proposals
failed, and narrower than saying the formal scalar model fails its
factor-ten target. It imposes no ceiling on an improved BJ lower. The
next authorized test retains the same frozen formal error vector but uses
its complete output, as preregistered under L4b in `attempts/L4.md`.

## Open items

The separate positive L4 theorem uses a stronger lower from the same
frozen formal error vector and proves the finite factor-ten target; this
does not contradict the fixed-old-lower obstruction. Keep the original
PD-T140 INCONCLUSIVE experiment unchanged. Claude's scientific/protocol
audit, including the historical reading-gate timing deviation, and the
orchestrator's external-artifact archival/delivery remain pending. No
actual-rounding or all-degree conclusion follows.

## History

- 2026-11-05: Codex mathematics worker, configured gpt-6.1-sol xhigh.
  Prepared on root's explicit instruction after all nine preregistered
  upper candidates failed. Rayleigh diagnosis is a separately labeled
  post hoc extension; no old criterion or receipt is rewritten. Initial
  finite status OPEN pending durable exact independent evidence.
- 2026-11-05: Changed finite status OPEN→PROVED after reading the exact
  developer diagnostic and the distinct independent complete-envelope,
  Rayleigh-floor and unchanged-G_R checks. Finalized only the
  fixed-old-lower subroute as REJECTED:failed. The separate full-output
  lower succeeds on the original finite target; that result and the
  original experiment's INCONCLUSIVE verdict remain separate.
