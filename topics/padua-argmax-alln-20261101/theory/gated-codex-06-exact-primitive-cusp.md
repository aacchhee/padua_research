# PD-T?argmax-alln-gated-codex-06 — Exact primitive endpoint cusp

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

Exact real arithmetic, the corrected kernel and its actual polynomial collision values. Overall status:PROVED by finite Taylor expansion and elementary cotangent bounds; independent review of the underlying calculation completed in gated/checks/d1-r02.md; required Claude audit PENDING.
Depends on gated-codex-02's exact physical-mesh/reflection normalization and numerator algebra. No numerical fit or external literature theorem.

## Proof

At zero phase, a noncollision half is F=(1+cos v)/(cos u−cos v). The only zero terms on the physical odd mesh are r=m=n+1,j<n with j+n even. The common endpoint(j,r)=(n,m) has actual finite polynomial value n and is not zero. All other zero-phase values are nonzero because coprimality of n,m leaves no other equal-cosine interior mesh pair.

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
