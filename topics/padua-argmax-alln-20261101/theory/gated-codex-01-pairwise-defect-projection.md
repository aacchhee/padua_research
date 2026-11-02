# PD-T?argmax-alln-gated-codex-01 — Pairwise defect projection away from corners

ID kind:PD-T.
Aliases: four-copy pairing lower bound; compact strip defect; projected edge cancellation.
Split from: supporting cancellation obligation for PD-T099/P4/P5.
Split into:none; the two-phase primitive estimates and corner comparison remain separate.

## Statement and definitions

Let m=n+1 and use the even-checkerboard Padua nodes a_j=jπ/n,b_k=kπ/m,j+k even, weights w_jk=2e_jf_k/(nm) with half endpoint factors. Let G_n be the corrected cosine kernel of PD-T101 (its x mode(n,0) has coefficient1). Put Gση=G_n(θ+σa_j,φ+ηb_k) and

λ=Σw|ΣσηGση|/4, S=ΣwΣση|Gση|/4, Δ=S−λ,

Qv=Σw Σσ(|Gσ+|+|Gσ−|−|Gσ++Gσ−|)/4,

Qh=Σw Ση(|G+η|+|G−η|−|G+η+G−η|)/4.

These are finite polynomial/absolute-value expressions, including every removable quotient value.
Exactly, Δ≥Qv≥0 and Δ≥Qh≥0 on the entire angle square.

Write θ=Jπ/n+α/n,φ=Kπ/m+β/m with integers J,K,J+K odd. For any ρ_n→0 and fixed0<δ<π/2, uniformly over these physical angles and |α|+|β|≤ρ_n,

Qv−g_v(φ)→0 if δ≤φ≤π−δ, with no restriction on θ;

Qh−g_h(θ)→0 if δ≤θ≤π−δ, with no restriction on φ.

Here g_v,g_h are exactly prior records codex-04/05's positive compact integrals. Thus each projected defect has a positive uniform lower bound for sufficiently large n in its stated strip, including points whose other coordinate approaches a physical edge at any rate.

## Assumptions and status

Exact real arithmetic, n→∞, fixedδ, near the odd coset in both phases. Overall status:PROVED by the analytic argument below; supplementary independent review is complete; Claude audit-01 ACCEPTED the mathematics at its stated scope (record fixes pending). This is not an effective rate, not a bound away from the odd-coset phase neighborhood, and not a corner result.

## Dependencies and sources

PD-T101 corrected cardinal kernel and elementary product-to-sum; prior codex-04/05 integral definitions and positivity. The endpoint/tube argument is repeated with the changed periodic mesh. Closest mechanism IDEA305/originalClaude02/fallback04; a variant, no novelty/priority claim. Rules/input7d308b10d946b607ae0690454f6c0103690775a4; AC-authorized direction1 round1.

## Proof

The product-to-sum formula for each cosine product gives L_jk=w_jk ΣσηGση/4, including the corrected x mode, so the displayed λ identity is exact. Periodic reflection of both endpoint-weighted node meshes also identifies S with (2nm)^−1 times the shifted even periodic-board absolute kernel sum. Grouping the four summands into either two pairs and applying the triangle inequality proves Δ≥Qv,Qh exactly.

Set a=(cosα+cosβ)/2. On an odd shifted periodic board write u=jπ/n+α/n,v=rπ/m+β/m,j+r odd. The elementary divided difference P_n=T_(n+1)+T_n gives, away from equal cosines,

(-1)^j G_n(u,v)/2 =
[a(1+cos v)−(sinα/2)sin u+(sinβ/2)sin v]/(cos u−cos v). (A)

Indeed P_n(cos u)=(-1)^j[cosα(1+cos u)−sinα sin u] and P_n(cos v)=−(-1)^j[cosβ(1+cos v)+sinβ sin v]; subtracting the corrected cos(nu) term gives(A). The original finite kernel defines all collisions.

### Vertical projection

For a fixed physical k, the two η halves have v±=φ±b_k and a common sign(-1)^(J+j). Put H± equal to(A). Their point defect is d=|H+|+|H−|−|H++H−|.

Reflection-periodicizing the first mesh in Qv, then translating its index by J, gives exactly

Qv=(nm)^−1 Σ_(k=0)^m f_k Σ_(0≤j<2n,j+k≡J mod2) d(jπ/n+α/n,b_k). (B)

The two cosine denominator targets differ by2sinφ sin b. If φ∈[δ,π−δ], one denominator is separated by at least sinδ sin b. Bounded numerators in(A) imply0≤d≤Cδ/sin b. This remains valid at collisions through the other regular half. At b=0,π the original two kernels coincide, so d=0.

For b≤η or π−b≤η, η<δ/4, the zero-phase numerator1+cos(φ±b) has a positive uniform lower bound. Whenρ_n is sufficiently small both actual numerators in(A) are positive uniformly in u. Positive d then requires cos u between the two targets; a collision with positive numerator is impossible after clearing the denominator. In the full periodic u mesh this band has total angular length≤4min(b,π−b). Each row containsO(n min(b,π−b)+1) indices. Endpoint weights and the sine chord bound give total endpoint-tail contribution

Cδ[η+(1+log m)/n].

The same limiting integral tails areOδ(η). This bound does not depend on J, K or the unused macroscopic θ.

On η≤b≤π−η, d is uniformly bounded. Remove angular tubes of widtht around all solutions of cos u=cos(φ±b), and around the corresponding zero-phase curves. These are a bounded number of angle line segments, so their mesh mass isO(t+1/n+1/m), uniformly in movingφ and in either parity. Off them, denominators are separated, and(A) converges uniformly to(1+cos(φ±b))/(cos u−cos(φ±b)); absolute value preserves uniform convergence.

For the bounded bulk family, the parity Riemann sum in(B) has density1/(2π²) on[0,2π]×[0,π]. Pair adjacent first-grid indices to remove the alternating parity term; equicontinuity off tubes makes the error uniform in moving parameters. The zero-phase defect is2h_φ(cos u,b), where h is codex-04's integrand. Since this function depends on cos u,

(2π²)^−1 ∫_0^π∫_0^(2π)2h_φ(cos u,b)du db = g_v(φ).

Let n→∞, then t↓0, thenη↓0. This proves the stated compact-uniform vertical limit. No full four-copy defect limit is needed.

### Horizontal projection

Periodicize the second mesh instead and use the common sign of G+η,G−η. After reversing a harmless common sign, the half numerator is

a(1+B)+(sinβ/2)sin v−(sinα/2)sin(θ±a_j), B=cos v.

The two denominator targets cos(θ±a_j) have separation2sinθ sin a_j. In the compact θ interval, d_h≤Cδ/sin a_j. The difference of the two numerators is−sinα cosθ sin a_j. Outside their closed cosine band the denominators have the same sign; positive defect requires opposite numerator signs, so each numerator magnitude is at most|sinα|sin a_j. The regular separated half bounds this outside-band defect byCδ|α|.

Inside the band, the periodic v interval has lengthO(min(a_j,π−a_j)), giving the same row-count tail bound. The two endpoint tails together are at most

Cδ[η+(1+log n)/m+|α|].

At a_j=0,π the polynomial halves coincide. On the bulk, remove the moving pole tubes exactly as above. At zero phase the limiting defect is2h_h,θ(cos v,a_j), the codex-05 integrand. The parity Riemann density on[0,π]×[0,2π] gives precisely g_h(θ). Sending limits in the same order proves the horizontal claim uniformly in the unused macroscopicφ. ∎

## Checks and consequences

Direction1 round1 numerical diagnostics are separate MEASURED evidence under gated/d1/r01-screen.md. They are not premises of this proof.

Conditional reduction: if a global two-phase bound localizes any near-corner-level maximizer to |α|+|β|→0 and a local primitive bound gives S≤Λc+o(1), this theorem excludes every fixed compact complement of the four corner squares, including all intermediate strip scales. Remaining corner neighborhoods and effectivity still need proof. The two-phase estimates are not assumed proved here.

## Scope/history

This removes the need for a positive full four-copy limiting profile in P4/P5. It does not remove phase localization, local primitive gain, effective thresholds or the corner obligations. All-degree PD-T099 remains OPEN. Developed by Codex Sol xhigh within direction1 round1; Claude audit-01 ACCEPTED the mathematics at its stated scope (record fixes pending).


### Documentation correction — 2026-11-02

F3: publication-time review labels are updated; the original proof and claim scopes are unchanged.

Current review scope (F3): [Claude audit-01](../audit-01.md) ACCEPTED the mathematics exactly as stated; its record/protocol findings and the protocol check of this response remain pending. Supplementary independent checks are complete and do not replace that Claude audit. No proof status, statement, checker predicate or certificate changes. Earlier publication-time review wording is preserved here as history:

> independent check and required Claude audit pending
> required Claude audit PENDING
