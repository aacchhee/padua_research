# PD-T?padua-xu-lebesgue-20261114-claude-23 — sign structure and closed forms of λ_n(±1, 1) for Morrow–Patterson points

ID kind: PD-T.
Aliases: X2-23; upper-vertex closed form; band formula; one-sum formula; target T2 of round X2-2.
Split from: none.
Split into: none.

## Statement

Let n ≥ 2 be even, M = n + 2, N = M(M+1), κ := (2M+3)/(2M−1) = (2n+7)/(2n+3). For a node (p, q) ∈ 𝒩 (notation of X2-21) put
X := (1 + x_p)/2 = cos²(w_p/2), Y := (1 + y_q)/2 = cos²(v_q/2), A_{p,q} := (−1)^p ℓ_{p,q}(1, 1).

(a) **Closed form.** A_{p,q} = 16 X(1−X) Y(1−Y) [ (M−½)X − (M+3/2)Y ] / ( N (X−Y)³ ), and X ≠ Y.

(b) **Signs.** Let B := {(p, q) ∈ 𝒩 : Y < X < κY} (the "band"). Then A_{p,q} < 0 on B, A_{p,q} > 0 if X < Y or X > κY, and A_{p,q} = 0 iff X = κY. Hence
sgn ℓ_{m,k}(1,1) = (−1)^m · sgn[ (x_m − y_k)( (2n+3)x_m − (2n+7)y_k − 4 ) ].

(c) **Band formula.** Σ_𝒩 A_{p,q} = −(n+1), and
λ_n(1, 1) = λ_n(−1, 1) = Σ_𝒩 |A_{p,q}| = 2 Σ_B |A_{p,q}| − (n+1) = (n+1) + 2 Σ_{𝒩∖B} A_{p,q},
where every term of the last sum is ≥ 0.

(d) **One-sum formula.** With X_r := sin²(πr/(2M)), Y_r := sin²(πr/(2M+2)) for integers r:
λ_n(1, 1) = (8/N) Σ_{r=1}^{N−1} X_r(1−X_r) Y_r(1−Y_r) |(M−½)X_r − (M+3/2)Y_r| / |X_r − Y_r|³,
where X_r ≠ Y_r for 1 ≤ r ≤ N−1 and the terms with M | r or (M+1) | r are zero.

(e) **Hyperbolic form.** With u := ½ log(X/Y): A_{p,q} = (2/N)(1−X)(1−Y) [ (2M+1) sinh u − 2 cosh u ] / sinh³u, and B = {0 < tanh u < 2/(2M+1)}.

(f) **Non-vanishing (minor).** X = κY never occurs; so ℓ_{p,q}(1,1) ≠ 0 for every node.

## Definitions

As in X2-21. In the (m, k) indexing p = m. In (d) the index r is a plain integer; the correspondence with nodes is given in the proof.

## Assumptions

n even, n ≥ 2. Part (f) additionally uses the standard fact ℚ(ζ_a) ∩ ℚ(ζ_b) = ℚ(ζ_{gcd(a,b)}) for cyclotomic fields (e.g. Washington, *Introduction to Cyclotomic Fields*, Prop. 2.4 for the compositum/intersection statement); nothing else in this topic depends on (f).

## Status by part

Overall status: PROVED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| (a) closed form in X, Y | PROVED | algebra from X2-21 part 3 |
| (b) sign pattern | PROVED | from (a) |
| (c) band formula | PROVED | X2-21 part 1 with f = U_n(x) |
| (d) one-sum formula | PROVED | Chinese remainder bookkeeping below |
| (e) hyperbolic form | PROVED | algebra |
| (f) non-vanishing | PROVED (minor routine step; uses a textbook fact about cyclotomic fields) | not used elsewhere |

Candidate / claim disposition: none.

## Depends on

- X2-21: part 1 (reproduction on Π_n), part 3 (formula at (1,1)), part 4 (λ_n(−1,1) = λ_n(1,1)).

## Checks

- `python3 code/mp/research/x2_corner_checks.py ident` (40 digits), n ∈ {2,4,6,8,10,12,16,20,24,30}: forms (a) and (e) against X2-21 part 3 at every node: max abs difference 7.5e−38; sign pattern (b) holds at every node (`sign_pattern_ok: True`); band formula minus direct sum ≤ 2e−36; one-sum formula minus direct sum ≤ 8e−37; Σ A + (n+1) ≤ 2e−36; band sizes |B| = 3, 5, 7, 9, 11, 13, 18, 22, 27, 34.
- Agreement with the independent path-A certificate (`evidence/mp-cmp-certificate.json`, Vandermonde solve in ball arithmetic): distance of the closed-form value of λ_n(1,1) to the certified enclosure ≤ 1e−33 for every listed n ≤ 30 (the working precision here is 40 digits; the enclosures have width 2e−45).
- `python3 code/mp/research/x2_corner_arb.py --nmax 60` (python-flint 0.9.0, 256 bits): rigorous enclosures of form (a) summed over all nodes; for every even n ≤ 60 no term's ball contains 0 and the enclosure of Σ A contains −(n+1). Values, e.g.: λ_2(1,1) = 5.845559233168126967689901947…, λ_4 = 14.84083546603432874155661148…, λ_6 = 28.02502760599746156533775494…, λ_30 = 510.5422101018094869577979239…, λ_60 = 1952.520045671169625892311657….
- Independent rerun: pending (auditor).

## Sources

- LITERATURE: Beberok, JAT 311 (2025) 106191, eq. (2) is the (1,1) kernel in the form of X2-21 part 3; his proof bounds part of the resulting sum from below and does not state the sign pattern, the band formula or the value. BBDM (Constr. Approx. 63 (2026)) do not treat vertex values analytically.

## Proof or evidence

Throughout x = x_p, y = y_q, ω = ω_{p,q}, x − y = 2(X − Y), 2 + x + y = 2(X + Y), 1 − x² = 4X(1−X), 1 − y² = 4Y(1−Y), ω = 128 X(1−X)Y(1−Y)/N.

**(a)** By X2-21 part 3, A = ω[(2M+1)/(4(x−y)²) − (2+x+y)/(2(x−y)³)] = ω[(2M+1)(x−y) − 2(2+x+y)]/(4(x−y)³) = ω[(2M+1)(X−Y) − 2(X+Y)]/(16(X−Y)³) = ω[(2M−1)X − (2M+3)Y]/(16(X−Y)³). Insert ω. X ≠ Y because x_p ≠ y_q.

**(b)** The prefactor 16X(1−X)Y(1−Y)/N is positive (0 < X, Y < 1). If X < Y: (X−Y)³ < 0 and (M−½)X − (M+3/2)Y < (M−½)(X − Y) < 0, so A > 0. If X > Y: A has the sign of (M−½)X − (M+3/2)Y = (M−½)(X − κY). In the original variables (X − Y) and (2M−1)X − (2M+3)Y are positive multiples of x − y and (2n+3)x − (2n+7)y − 4.

**(c)** U_n(x_p) = (−1)^{p+1} (X2-22), so Σ_𝒩 A_{p,q} = −Σ_𝒩 U_n(x_p) ℓ_{p,q}(1,1) = −U_n(1) = −(n+1) by X2-21 part 1. Since |A| = A + 2[−A]_+ and [−A]_+ = |A|·1_B by (b): Σ|A| = −(n+1) + 2Σ_B|A|. Since |A| = −A + 2[A]_+: Σ|A| = (n+1) + 2Σ_{𝒩∖B}A. λ_n(−1,1) = λ_n(1,1) is X2-21 part 4.

**(d)** *Reindexing.* For (p, q) ∈ 𝒩 put p' := M − p ∈ [1, M−1], q' := M + 1 − q ∈ [1, M]. Then X = cos²(pπ/(2M)) = sin²(πp'/(2M)), Y = sin²(πq'/(2M+2)), and p + q odd ⟺ p' + q' even (2M + 1 is odd). So nodes correspond to 𝒩' := {(p', q') : 1 ≤ p' ≤ M−1, 1 ≤ q' ≤ M, p' ≡ q' (mod 2)}.
*Residues.* X_r depends only on ±r mod 2M and Y_r only on ±r mod 2(M+1). Let 𝓡 := {r ∈ ℤ/2Nℤ : M ∤ r, (M+1) ∤ r}; |𝓡| = 2N − 2(M+1) − 2M + 2 = 4·|𝒩'|. For r ∈ 𝓡 there are unique p' ∈ [1, M−1] with p' ≡ ±r (mod 2M) and q' ∈ [1, M] with q' ≡ ±r (mod 2M+2), and p' ≡ r ≡ q' (mod 2); this defines a map 𝓡 → 𝒩' with (X_r, Y_r) = (X, Y) of the image node. Conversely, since gcd(2M, 2M+2) = 2, lcm = 2N and p' ≡ q' (mod 2), each of the four systems r ≡ ε p' (mod 2M), r ≡ ε' q' (mod 2M+2), ε, ε' ∈ {±1}, has exactly one solution mod 2N, namely ±r₁, ±r₂ with r₁ := p'(M+1) − q'M and r₂ := p'(M+1) + q'M (indeed r₁ = p' + (p'−q')M = q' + (p'−q')(M+1) and r₂ = p' + (p'+q')M = −q' + (p'+q')(M+1)). They are pairwise distinct mod 2N: r₁ ≡ −r₁ or r₂ ≡ −r₂ would force M | p'; r₁ ≡ r₂ would force (M+1) | q'; r₁ ≡ −r₂ would force M | p'. So every node has exactly four preimages.
*Sum.* Let a_r be the r-th summand of (d). For r ∈ 𝓡, a_r = (N/16)|A| of the image node, so Σ_{r∈𝓡} a_r = (N/4)λ_n(1,1). For 1 ≤ r ≤ 2N−1: X_r − Y_r = sin(πr(2M+1)/(2N)) sin(πr/(2N)) ≠ 0, because gcd(2M+1, 2N) = 1 and 2N ∤ r; and a_r = 0 if M | r (then X_r(1−X_r) = ¼ sin²(πr/M) = 0) or (M+1) | r. Hence Σ_{r=1}^{2N−1} a_r = (N/4)λ_n(1,1). Finally a_{2N−r} = a_r and a_N = 0, so Σ_{r=1}^{N−1} a_r = (N/8) λ_n(1,1).

**(e)** With u = ½log(X/Y): X − Y = 2√(XY) sinh u and (M−½)X − (M+3/2)Y = √(XY)[(M−½)e^u − (M+3/2)e^{−u}] = √(XY)[(2M+1) sinh u − 2 cosh u]. Insert in (a): A = 16X(1−X)Y(1−Y)√(XY)[…]/(8N (XY)^{3/2} sinh³u). The band condition 1 < X/Y < κ is 0 < u and (2M+1) sinh u < 2 cosh u.

**(f)** Suppose (2M−1)X = (2M+3)Y, i.e. (2M−1)(2 + 2x_p) = (2M+3)(2 + 2y_q). Now 2 + 2x_p = 2 + ζ^p + ζ^{−p} with ζ = e^{iπ/M} is an algebraic integer of ℚ(ζ_{2M}), and 2 + 2y_q is an algebraic integer of ℚ(ζ_{2M+2}). The equation puts 2 + 2x_p in ℚ(ζ_{2M}) ∩ ℚ(ζ_{2M+2}) = ℚ(ζ_2) = ℚ, so it is a rational integer in (0, 4), i.e. in {1, 2, 3}; likewise 2 + 2y_q. Their quotient κ = 1 + 4/(2M−1) would lie in {3/2, 2, 3}, i.e. M ∈ {9/2, 5/2, 3/2}: impossible. ∎

Remark (shape of the band; description only, not used and not claimed as proved). In angles, X/Y = cos²(w/2)/cos²(v/2), so B consists of nodes with v_q slightly larger than w_p: 0 < log cos(w_p/2) − log cos(v_q/2) < ½ log κ ≈ 1/(M − ½). Numerically it consists of the first superdiagonal q = p + 1 and, towards the vertex (1,1), of further superdiagonals q = p + 3, p + 5, …; the measured sizes |B| are listed under Checks. The quantitative description actually used later is the exact sandwich of X2-25, Step B.

## Scope

Exact identities for every even n ≥ 2 at the vertices (±1, 1). No absolute values remain in (c) once B is known; B is described by an explicit inequality but not by a closed index formula.

## Open items

None for this record. Asymptotics are in X2-25.

## History

- 2026-11-14, Claude Fable 5.2 (xhigh), researcher subagent of round X2-2; uncommitted at writing. First version.
