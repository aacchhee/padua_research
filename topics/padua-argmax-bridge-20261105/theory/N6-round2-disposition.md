# N6 round2 disposition — Fixed-trace lifts narrowed; broader route deferred

Record kind: research disposition and equivalence verification; no new
PD-T or PD-N ID. Main unresolved comparison(G): **OPEN**.

2026-11-05. Codex N6, assigned gpt-6.1-sol xhigh; rules/input
`714f3cad18859c07cd13f31561f2a185f9591a7f`.

## Exact outcome

[N6-02](N6-trace-mixture-application.md), provisional
`PD-N?argmax-bridge-codex-N6-02`, applies N4's sole generic variance
theorem to fixed trace supports. It proves that positive probability
mixtures of complete cardinal vectors cannot move an off-support point
onto any fixed collection of traces. The two-trace support is exactly
T_n(x)^2=T_(n+1)(y)^2, so explicit off-support points exist at every n>=2.
The n2 witness from round1 is outside both entire traces, irrespective
of comparison time. Signed mass1/TV<=1 lifts, positive scalar envelopes
and invertible complete-vector groupings are consolidated with this
class, not re-registered as different mechanisms.

The surviving scalar question is

    C_n=max(max_t lambda_n(Gamma_0(t)),
            max_t lambda_n(Gamma_pi(t))),
    lambda_n(z)<=C_n on the square.                         (G)

Round1 refutes only the same-t comparison(C). Round2 refutes only
positive full-vector lifts on restricted support. Neither refutes(G).
Because both nonnode corners lie on Gamma_pi, C_n>=Lambda_c(n).
To close PD-T099 through(G), one still needs the separate trace bound
C_n<=Lambda_c(n), including its strict equality classification.
The conjunction would be sufficient; merely naming the traces proves
neither inequality. At n2, both follow from the inherited global
theorem PD-T209 and supply no new certified degree or mechanism.

## Scalar-mixture reformulation gate

There is a precise reason not to replace a complete vector by an
unrestricted single scalar block and call its mixture a repair. For
U=Gamma_0(T) union Gamma_pi(T), compactness and continuity make C_n
attained. Partition of unity implies lambda_n(y)>=1 everywhere, and
U contains a node corner with lambda=1. Therefore, for any z,

    there exists a probability mu on U with
    lambda_n(z)=integral lambda_n(y)dmu(y)
              iff  1<=lambda_n(z)<=C_n
              iff  lambda_n(z)<=C_n.                       (3)

The forward implication is the scalar maximum bound. Conversely,
if C_n>1, mix a node corner and an attained trace maximizer with weight
(lambda_n(z)-1)/(C_n-1); if C_n=1, the implication requires lambda=1
and the node point mass suffices. This elementary scalar equivalence
is verification, not a new structural theorem or a usable construction
independent of the unknown comparison. No experiment on unrestricted
scalar feasibility is authorized as a new test here.

Exact pairwise Hadamard grouping retains both even/odd features and
the norm2max(|E|,|O|), so an evaluation-vector mixture in those features
is merely invertible N6-02. Nonlinear block maxima may avoid N4's
reproduction premise, but no independently justified block comparison
or restricted admissible measure class was found in this round.
They remain outside the negative theorem and have not been sampled
or asserted impossible.

## Direction disposition

**Defer the broader IDEA-319/341 parallel-family route after round2.**
Round2 made recorded progress by narrowing the explicit positive-lift
class, but it yielded no surviving comparison that would improve the
certified range2–32 or produce an effective analytic onset. The fifteen
round ceiling is not a quota. No direction-wide mathematical kill or
counterexample is claimed, and an empty round3 is unnecessary.

Resume only with a concrete additional inequality or a restricted
signed/nonlinear feature class specified independently of the desired
norm comparison, together with its exact low-degree separation test.
It must retain four-copy cancellation, the corrected exceptional mode
and endpoint/collision terms. A scalar-mixture feasibility test equivalent
to(G), a positive full-evaluation lift, an invertible renaming or the
square-covering reparameterization alone does not meet that condition.

## Verification / publication boundary

No new numerical run was needed. Round1 original code, receipt,
candidate, novelty gate and theory bodies were left unchanged. Parent
owns the round counter, publication, audit and all Git operations.
Round2 is complete for parent review; no round3 was started.
