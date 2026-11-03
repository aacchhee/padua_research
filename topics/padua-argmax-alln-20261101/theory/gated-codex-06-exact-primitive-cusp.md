# PD-T220 (PD-T?argmax-alln-gated-codex-06) — Exact primitive endpoint cusp

Final registration: **PD-T220**, 2026-11-03. The provisional identifier in the title remains an alias; mathematical statement and historical evidence are unchanged.

ID kind:PD-T.
Aliases: coset directional slope; shrinking nonquadratic majorant gain.
Split from: quantitative primitive-gain diagnosis in direction1 round2.
Split into: scoped failure of coset-maximality and a pure quadratic gain is in gated-codex-N01.

## Statement

For the periodic odd-board primitive S_n(α,β) of gated-codex-02, every fixed integer n≥2 satisfies

S_n(α,0)=Λc(n)+L_n|α|+o_n(|α|),

L_n=[n(n+1)]^−1 Σ_(k=1)^floor(n/2) cot(kπ/n).

Here L_2=0 and L_n>0 for every n≥3. Also

0≤L_n≤H_floor(n/2)/(π(n+1)),
L_n=log n/(πn)+O(1/n).

## Assumptions/status/dependencies

Exact real arithmetic, the corrected kernel and its actual polynomial collision values. Overall status:PROVED by finite Taylor expansion and elementary cotangent bounds; independent review of the underlying calculation completed in gated/checks/d1-r02.md; Claude audit-01 ACCEPTED the mathematics at its stated scope (record fixes pending).
Depends on gated-codex-02's exact physical-mesh/reflection normalization and numerator algebra. No numerical fit or external literature theorem.

## Proof

At zero phase, a noncollision half is F=(1+cos v)/(cos u−cos v). The only zero terms on the physical odd mesh are r=m=n+1,j<n with j+n even. The common endpoint(j,r)=(n,m) has actual finite polynomial value n and is not zero. Away from the zero row r=m, the reference numerator 1+cos v is nonzero. Coprimality of n,m excludes other equal-cosine mesh collisions; it is not the reason that a noncollision numerator is nonzero.

Every nonzero-reference term is smooth near the origin. Its first phase derivative cancels when the four reflected phases are summed; at fixed n the finite sum of their remaining contributions is O_n(α²).

On the zero row r=m, exact differentiation of the corrected numerator gives

∂αF_jm(0,0)=−sin u_j/[2(1+cos u_j)]=−(1/2)tan(u_j/2),
∂βF_jm(0,0)=0.

The endpoint factor f_m=1/2 and the four reflected terms yield contribution
[e_j/(nm)]tan(u_j/2)|α|+o_n(|α|) per j. Writing j=n−2k, 1≤k≤floor(n/2), changes tan(u_j/2) to cot(kπ/n). If j=0 its half weight has no effect because the derivative is zero. This proves the exact finite sum and expansion, including n2.

On0<t≤π/2, 0≤cot t≤1/t, and cot t−1/t=O(t) with an absolute constant. Summing at t=kπ/n gives the harmonic upper bound and

Σcot(kπ/n)=(n/π)H_floor(n/2)+O(n).

Divide by n(n+1), use H_floor(n/2)=log n+O(1), and obtain the asymptotic. For n≥3 the k1 summand is strictly positive; at n2 it equals cot(π/2)=0. ∎

## Scope/history

This is a primitive-majorant statement, not a directional derivative of the physical Lebesgue function. The latter may have reflected cusps cancel. No all-degree corner assertion follows. Codex Sol xhigh, direction1 round2 calculation retained during round3, source7d308b10d946b607ae0690454f6c0103690775a4.


### Documentation correction — 2026-11-02

N5: the original sentence “All other zero-phase values are nonzero because coprimality of n,m leaves no other equal-cosine interior mesh pair” conflated two reasons. Nonzero noncollision values use 1+cos v≠0; coprimality excludes the other collisions. This clarifies the existing argument without changing the zero mask or cusp formula.

Current review scope (F3): [Claude audit-01](../audit-01.md) ACCEPTED the mathematics exactly as stated; its record/protocol findings and the protocol check of this response remain pending. Supplementary independent checks are complete and do not replace that Claude audit. No proof status, statement, checker predicate or certificate changes. Earlier publication-time review wording is preserved here as history:

> required Claude audit PENDING

F13 closest-prior citation: [PD-T190](../../padua-proof-attempts-2-20261101/theory/proof-attempts-2-codex-75-local-edge-phase-bound.md), statement (1) and proof §§2–4, already retains an explicit C|s| cusp allowance in its one-phase primitive upper bound. [Plan P3](../plan.md) likewise says the primitive rise and cancellation are “probably cusp-linear, not quadratic”. The exact fixed-n cusp formula in gated-codex-06 and the scoped obstruction in gated-codex-N01 refine that already retained issue; they do not establish a historical novelty or priority claim and do not transfer the primitive obstruction to the physical Lebesgue function.
