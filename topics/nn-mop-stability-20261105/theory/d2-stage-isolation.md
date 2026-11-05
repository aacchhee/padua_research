# PD-T?nn-mop-stability-codex-D2-01 — finite C4 stage isolation

ID kind: PD-T. Aliases: stable-marginal comparator; oracle-marginal isolation.
Split from: none. Split into: none. Overall status: **MEASURED**.

## Statement

For both frozen PD-T290 families and N in {4,8,12,16,24,32}, replacing only
its marginal arithmetic by binary64 full two-pass reorthogonalization does
not uniformly reduce the full-array forward errors. Near-roundoff marginal
errors coexist with large NN errors. Even separately computed 220-digit
marginals, rounded once to binary64, give large errors under the unchanged
binary64 layers. This isolates a finite amplification/rounding issue after
the marginal computation; a weak-stability verdict still requires the D1
condition number and a matching input model. It does not prove universal
instability of C4 or satisfy G2 merely by inspecting forward error alone.

## Definitions and assumptions

Inputs and monic coordinate are exactly PD-T290: z=2k/(N−1)−1, the two
rational binomial/Hahn weight pairs, common N-point support. Normality on
the finite triangle is the predecessor's setting. E is the maximum of four
fieldwise relative sup errors, exactly `c4_float_baseline.errors`.
Reference precision comparisons are 140/220 dps; convergence is not
certification. Unit roundoff is u=2^-53, distinct from predecessor epsilon.

The four algorithms use the identical imported `base.layers`:
Stieltjes (the predecessor); full reorthogonalized Lanczos; exact-input HP
marginals rounded once; HP marginals of rounded binary64 inputs rounded once.
Rounded-input and exact-input references distinguish algorithm error from
input conversion. A rounding-effect difference is not itself a bound on a
condition number or evidence that every nearby input behaves that way.

## Status by part

| Observation | Status | Evidence |
|---|---|---|
| Twelve G0 exact replays match frozen E values | MEASURED | `attempts/D2.md` |
| Full table of four marginal choices and path diagnostics | MEASURED | Same receipt; producer scripts |
| HP exact-vs-rounded-input map difference | MEASURED | Separate converged references |

No candidate rejection or universal negative statement is asserted.
Independent rounding of two marginal Jacobi families need not preserve their
common spectrum. Thus the marginal representation may leave the exact
common-support image before layer arithmetic. The experiment isolates the
post-marginal computation/representation; it does not separate amplification
of incompatible boundary perturbations from local layer rounding.

## Depends on

PD-T286/288/289 supply the existing exact NN setting and identities.
PD-T290 fixes the comparator and metric. Code imports the frozen predecessor
without changing it. Python binary64, mpmath 1.3.0 and its eigensolver are
trusted numerical dependencies, not verified arithmetic.

## Local construction of marginal comparator

Let X=diag(z) and q0=sqrt(w/sum(w)). Exact orthonormal Lanczos gives
beta_k=q_k^T X q_k and residual after projection onto all previous q's.
Its norm t_(k+1) is the next Jacobi off-diagonal, so the monic coefficient
alpha_(k+1)=t_(k+1)^2. The implementation projects Xq twice by MGS against
the entire existing Q, using `math.fsum` dot products; it extracts these
beta/alpha and discards tiny off-tridiagonal projection terms. Measured
orthogonality and marginal errors validate only the recorded finite runs;
no general stability theorem for this implementation is claimed.

## Checks and evidence

The commands, file hashes, versions, full-precision G0 E and compact full
table are in `../attempts/D2.md`. Binary64 Q orthogonality defects are at
most 4.45e-16; marginal coefficient errors against the rounded-input HP
marginals are at most 2.20e-16, scaled by max(1, reference marginal sup).
Yet for example Lanczos-C4 E is .16607436616872293 at Krawtchouk N16
and 136.72604448384504 at Hahn N16. Exact-oracle E there is
.048170048586347054 and 19.347648933050827 respectively.

## Sources

No primary paper fulltext was read by this worker. The FHV and Leuven
attributions remain the prior readers' reports in the predecessor and
LIT-119/347/348. The formulas actually used here follow from the displayed
orthogonal diagonal multiplication construction and PD-T289. No unread
external theorem is used to certify this experiment.

## Scope and open items

Only the twelve inputs and stated arithmetic are measured. No general
stability theorem, induced derivative certification, joint backward bound,
N64 run or independent agent rerun is claimed. G1/G2 await matched D1
conditioning; the alternating-path diagnostic has its own limitations in
`d2-path-diagnostic.md`. Raw output is local and regenerable, with archival
transfer pending AC's cold-storage destination.

## History

2026-11-05, Codex dispatched gpt-6.1-sol medium, input/rules
823cf6a4ef7c01b4ef3d2a6fec3e9f19d4b4f6f1. Initial transport added one final LF
to predecessor inputs; coordinator restored pinned bytes before final runs.
This changed source hashes but no scientific code or numerical results.
