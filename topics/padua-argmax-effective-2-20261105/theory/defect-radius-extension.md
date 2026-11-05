# PD-T?argmax-effective-2-codex-04 — Noncorner reflection defect through phase radius 1/10

ID kind: PD-T.
Aliases: A2 radius enlargement; finite middle-line defect; rho 0.1 cancellation bound.
Split from: none; quantitative variant of PD-T224 with a larger radius and a smaller lower bound.
Split into: none. Primitive excess comparison and H1 box certification remain separate.

## Statement

Let n≥48, m=n+1, and let a physical point have an odd-center representation θ=(Jπ+α)/n, φ=(Kπ+β)/m with 0≤J≤n, 0≤K≤m, J+K odd and |α|+|β|≤1/10. If (J,K) is not one of the two physical nonnode corners, its full four-copy reflection defect satisfies

\[
 \Delta_{JK}(\alpha,\beta)\ge\frac1{8192}.                    \tag{1}
\]

The bound is uniform over all admissible phase signs, centers and degrees in this range. It is not a comparison with S_n−Λ_c and does not certify a maximum.

## Definitions and assumptions

The corrected finite kernel, positive endpoint weights, full defect Δ and projected defects Q_v,Q_h are those of PD-T215 and `phase-structure.md`. Exact real arithmetic. The inherited adaptive-block theorem PD-T222 applies at ρ≤1/8 to points whose relevant physical angular endpoint distance is at least 4π/n. We use that theorem only in this stated regime.
Throughout, ρ:=|α|+|β|.

## Status by part

Overall status: **PROVED**, by the analytic finite construction below.
Dated review note, 2026-11-05: Claude [audit-01](../audit-01.md) accepted
the original scope; the record response check is pending.

| Mathematical part | Status | Evidence / limitation |
|---|---|---|
| Uniform noncorner defect (1), n≥48 and ρ≤1/10 | PROVED | Same lattice-line selections as PD-T224 with improved baseline and a smaller resulting numerator floor |

Candidate disposition: retained quantitative variant of IDEA-328 / PD-T224. No new mechanism or historical novelty claim.

## Depends on

PD-T215 for Δ≥Q_v,Q_h and the exact projection identities; PD-T222 for the far adaptive-block bound 1/1536. PD-T224 supplies the predecessor selection and is read in full, but its smaller-radius inequality is not extrapolated. The estimates needed for the enlarged radius are proved below.

## Proof or evidence

### Numerator and target interval

For odd periodic index pairs, a signed half-kernel has the form

\[
 \frac{A(u,v)}{\cos u-\cos v},\qquad
 A(u,v)=a(1+\cos v)-\tfrac12\sin\alpha\sin u
                         +\tfrac12\sin\beta\sin v,
 \quad a=\tfrac12(\cos\alpha+\cos\beta),
\]

up to a sign common to the two terms of the relevant projected pair. Throughout ρ≤1/10, use α²+β²≤(|α|+|β|)²=ρ² to obtain

\[
 a\ge1-(\alpha^2+\beta^2)/4\ge399/400,
 \quad \tfrac12(|\sin\alpha|+|\sin\beta|)\le1/20.
\]

For w∈[π/8,3π/4], both 1−cos w and 1+cos w exceed 3/40. Indeed cos(π/8)<37/40: use √2<17/12 to get cos²(π/8)<41/48<(37/40)². Also 1+cos(3π/4)=1−√2/2>1/4. Therefore whenever the relevant baseline is 1±cos w on this interval,

\[
 A\ge (399/400)(3/40)-1/20
       =397/16000>1/64.                                      \tag{2}
\]

Take an endpoint-distance index s∈{1,2,3,4}. The two target angles in each construction below differ by 2t, where t=(sπ±β)/m vertically or t=(sπ±α)/n horizontally. They are positive and

\[
 2t\le(8\pi+1/5)/m<26/m
 \quad\hbox{or}\quad 2t<26/n.                               \tag{3}
\]

If the selected comparison angle lies strictly between the two targets, the cosine denominators are nonzero, opposite in sign and bounded in magnitude by their target span. The vertical and horizontal constructions below verify this ordering on [π/8,3π/4], where cosine is strictly decreasing. Equations (2)–(3) give a defect of the two signed half-kernels of at least m/832 vertically or n/832 horizontally. The normalization of each half-kernel projected sum is 1/N.

### Vertical lines, including parity

Let l run through all integers n/4≤l≤n/2; there are at least n/4−1≥n/8. The physical second index is k=l+q and the periodic first index is r. Define b=kπ/m. The choices and exact displacements are:

| Physical center | q | r and comparison angle w | t | m(w−b) |
|---|---:|---|---|---|
| K=m−s, s odd | 1 | r=n−l, w=(lπ−α)/n | (sπ−β)/m | lπ/n−π−(m/n)α |
| K=m−s, s even | 0 | same | same | lπ/n−(m/n)α |
| K=s, s odd | 0 | r=l, w=(lπ+α)/n | (sπ+β)/m | lπ/n+(m/n)α |
| K=s, s even | 1 | same | same | lπ/n−π+(m/n)α |

All selected k are interior, so f_k=1. At the top u=π−w and the cosine targets are −cos(b−t),−cos(b+t); at the bottom u=w and the targets are cos(b−t),cos(b+t).

The unperturbed displacement magnitude is at most 3π/4 in the first/fourth rows, and π/2 in the other rows. After including β, the perturbation is at most

\[
 (m/n)|\alpha|+|\beta|\le49/480<\pi/4.
\]

Since s≥1 in odd rows and s≥2 in even rows, this proves |w−b|<t in every row. Both target angles lie in [π/8,3π/4], because for n≥48

\[
 b-t\ge\frac{(n/4-4)\pi-1/10}{n+1}\ge\pi/8,
 \quad
 b+t\le\frac{(n/2+5)\pi+1/10}{n+1}\le3\pi/4.
\]

These follow by clearing the positive denominator; the resulting linear expressions in n have their worst value at n=48, where both inequalities are strict. Thus the top baselines 1−cos(b±t) and bottom baselines 1+cos(b±t) satisfy (2).

For the top, r+k=n+q and odd J+K gives J≡n+s (mod 2); q≡s. For the bottom r+k≡q and J≡1−s; q≡1−s. Hence every selected point has the required r+k≡J parity in the exact Q_v sum. Each of at least n/8 distinct physical rows contributes at least m/832, giving

\[
 Q_v\ge\frac1{nm}\frac n8\frac m{832}=\frac1{6656}.         \tag{4}
\]

### Horizontal lines and the fixed numerator

Let l run through integers m/4≤l≤m/2; there are at least m/4−1≥m/8, since m=n+1≥49. The physical first index is j=l+q and the periodic second index is r. Put b=jπ/n (a first-mesh angle in this subsection). Use

| Physical center | q | r and comparison angle w | t | n(w−b) |
|---|---:|---|---|---|
| J=n−s, s odd | −1 | r=m−l, w=(lπ−β)/m | (sπ−α)/n | π−lπ/m−(n/m)β |
| J=n−s, s even | 0 | same | same | −lπ/m−(n/m)β |
| J=s, s odd | 0 | r=l, w=(lπ+β)/m | (sπ+α)/n | −lπ/m+(n/m)β |
| J=s, s even | −1 | same | same | π−lπ/m+(n/m)β |

All physical j are interior, so e_j=1. Base displacement magnitudes are ≤3π/4 in odd-top/even-bottom rows and ≤π/2 in the others. The perturbation including α is ≤|α|+(n/m)|β|≤1/10<π/4. Thus w lies strictly between b−t and b+t. For n≥48 these targets are in the required interval, as

\[
 b-t\ge\frac{((n-19)/4)\pi-1/10}{n}\ge\pi/8,
 \quad
 b+t\le\frac{((n+9)/2)\pi+1/10}{n}\le3\pi/4.
\]

In the horizontal pair the relevant numerator is

\[
 a(1+B)+\tfrac12\sin\beta\sin v
              -\tfrac12\sin\alpha\sin(\theta\pm b),\quad B=\cos v.
\]

Its baseline comes from the **fixed periodic second angle**, not from a target angle. At the top v=π−w, giving 1−cos w; at the bottom v=w, giving 1+cos w. In both cases w∈[π/4−1/(10m),π/2+1/(10m)]⊂[π/8,3π/4]. Equation (2) therefore applies without interchanging the corrected mode. The selected denominators have opposite signs and span bound (3).

For the top, r+j=m+q while K≡m+s, and q≡s. For the bottom r+j≡q while K≡1−s, and q≡1−s. This is the required parity in Q_h. At least m/8 distinct rows contribute at least n/832, yielding

\[
 Q_h\ge\frac1{nm}\frac m8\frac n{832}=\frac1{6656}.         \tag{5}
\]

### Exhaustion of all noncorner centers

If K is interior, let s=min(K,m−K). For s≤4 apply (4). For s≥5,

\[
 \min(\phi,\pi-\phi)\ge(5\pi-1/10)/m>4\pi/n
\]

for n≥48, and ρ≤1/10<1/8. PD-T222 gives Q_v≥1/1536. If K is an endpoint, the noncorner assumption forces J interior. Take s=min(J,n−J); for s≤4 use (5), and for s≥5 the first-angle endpoint distance is ≥(5π−1/10)/n>4π/n, so the horizontal PD-T222 bound applies. Thus every case satisfies

\[
 \Delta\ge\max(Q_v,Q_h)\ge\min(1/6656,1/1536)>1/8192,
\]

which proves (1).

## Checks

No floating run is a premise. The inequality endpoints and all eight line selections were reconstructed from PD-T224 at input ed21cc0bf205549936fccde90244a291bc6de324. Independent mathematical check and Claude audit requested. A2 sampled projected profiles are separate evidence and cannot strengthen the bound in (1).

## Sources and novelty gate

Internal predecessor PD-T224 and its IDEA-328 lineage; the complete H1 gate is in `../novelty-gate-H1.md`. This variant changes the exact radius/budget pair from (1/64,1/4096) to (1/10,1/8192). Its falsifiable distinction is the larger uniform admissible phase domain; a failed band/numerator inequality at any n≥48 would kill this extension. The weakest inequalities were checked at n=48 before writing the proof. No external source or priority claim.

## Scope and open items

Only noncorner odd centers, n≥48. The corner centers have zero defect at zero phase and are excluded. The theorem supplies a rigorous A2 lower bound at the preregistered radius 0.1, but comparison with the maximum primitive excess on every relevant box still needs a rigorous bound. No statement is made at radii 0.2 or 0.3, or about n<48. The constant is deliberately conservative.

## History

2026-11-05, Codex mathematical worker, AC-requested gpt-6-astra ultra; runtime metadata not independently exposed. Root proposed enlarging the inherited numerator floor during the A2 gate, and the worker reconstructed all eight lines, parity and far cases before recording the theorem. No final ID assigned; no registry edit.

2026-11-05 audit response, Codex, gpt-6-astra ultra: E5 corrects the
first-writing description above. The baseline improves from 1/16 to
3/40, while the resulting numerator floor decreases from 223/4096 to
397/16000 as the admissible radius grows. E6 makes ρ, the square bound,
the later angle-ordering check and the horizontal row-count step explicit.
These explain estimates already used in the accepted proof; no statement,
proof step, constant or epistemic status is changed.
