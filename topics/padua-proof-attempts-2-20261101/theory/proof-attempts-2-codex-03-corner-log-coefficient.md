# PD-T?proof-attempts-2-codex-03 — The corner logarithmic coefficient with explicit remainder

ID kind: PD-T.
Aliases: A2(iii); Padua corner b-term; bounded square comparison asymptotic.
Split from: `PD-T?programme-ideas-claude-04`, first asymptotic part, precisely OPEN_TARGETS A2 at programme SHA `9bd14a6d2c4da69139a10107d8a787f2be0c5c9e`.
Split into: none; weaker ordered deliverables -01 and -02 retain their own proved statements. The original full A3 expansion remains OPEN.

## Statement

For every integer n≥2,

\[
 \left|\Lambda_c(n)-\frac4{\pi^2}\log^2n
       -\frac8{\pi^2}\left(\gamma+\log\frac8\pi\right)\log n\right|
 \le68.                                                       \tag{1}
\]

Thus the A2 statement is proved, with explicit O(1) constant68 and coefficient

\[
 b=\frac8{\pi^2}\left(\gamma+\log\frac8\pi\right).
\]

The original A2 wording is: “Λ_c(n)=(4/π²)log²n+b log n+O(1) as n→∞, with b=(8/π²)(γ+log(8/π))=2·(2/π)·c₁, where c₁=(2/π)(γ+log(8/π)) is the constant of the1-D Chebyshev Lebesgue constant.” No full constant term, parity independence of that term, or A3 remainder is included in(1).

## Definitions

The Padua nodes and corner value are those of -04; γ=lim_m(H_m−log m) is Euler's constant. Set c₁=(2/π)(γ+log(8/π)), A_n=(2/π)log n+c₁, and use L_n from -04.

## Assumptions

Exact real arithmetic, every integer n≥2, the specified even checkerboard and first-coordinate exceptional mode. No global corner-argmax theorem and no asymptotic assumption.

## Status by part

Overall status: **PROVED** (written all-n proof; required Claude audit pending).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Explicit b-term(1), closing A2(iii) | PROVED | Bounded comparison -04 and elementary one-dimensional expansion below |

Candidate disposition: completion of a registered target. No historical novelty/priority claim. The source's full A3 expansion remains OPEN and is not relabelled by this proof.

## Depends on

`PD-T?proof-attempts-2-codex-04`, |Λ_c−L_n²|≤54, and `PD-T?proof-attempts-2-codex-02`, its routine monotonicity argument for g; indirectly **PD-T?proof-attempts-codex-01 (audit pending)**. Per user instruction the literal dependency label is retained. Qualification dated2026-11-01: root reviewed Claude audit-01 at `95279b833bca5967fcf47c1b71a56ff622185b4e`, accepted A1 without a mathematical finding, and merged it; upstream disposition edits remain pending. The one-dimensional expansion here is proved locally, not inherited from a fit or source citation.

## Checks

The proof has no computational dependency. Independent route agent `/root/a2_independent_route` reconstructed the same-mesh square, the deformation bound, and the harmonic/quadrature expansion by hand; see `../independent-checks-a2.md`. Developer exact regression passed n=1,…,6 (details in -04 and the attempt record). Developer also actually ran `python topics/padua-proof-attempts-2-20261101/code/a2_sanity.py > topics/padua-proof-attempts-2-20261101/outputs/a2_sanity.json`, NumPy2.3.5/64-bit-mantissa longdouble, n=2,…,64 and128,256,512,1024. Maximum measured b-remainder≈1.955813; at n=1024 it is≈1.848524867410685. Pinned T2 longdouble values at64,128,256 agree within3e−16; the pinned mpmath values agree within7e−16. These are MEASURED sanity checks, not fits or proof. A different agent actually reran both scripts, exit0 and byte-identical; its separate receipt is `../independent-execution-a2.md`. Required Claude audit remains pending.

## Sources

LITERATURE: Kolomoitsev–Lomako, arXiv:2009.07114v1 (2020 preprint; Appl. Math. Comput.403,2021), introductory one-dimensional expansion printed p.1 and Theorem2.1 printed p.4; discretization Lemma3.5(3.20), printed pp.10–11, and parity Lemma3.6(3.29), printed pp.11–12. Full16-page paper read before method use. It reports the same one-dimensional c₁ and proves the global Padua leading term with O(log n), without a corner b-term. Bos et al.2006 Theorem3, author preprint printed pp.10–12, gives global O(log² n). Exact reading scope and URLs: `../attempts/T-A2.md`. No claim that the present target was historically open follows from this bounded literature check.

## Proof or evidence

### 1. Uniform elementary harmonic remainder

Let e_m=H_m−log m−γ. For m≥1,

\[
 0<e_m=\sum_{r=m}^{\infty}\left(\log(1+1/r)-\frac1{r+1}\right)
 \le\frac1{2m}.                                              \tag{2}
\]

Each summand is positive. Convexity of1/t bounds its integral over[r,r+1] by the endpoint trapezoid, hence bounds the summand by(1/2)(1/r−1/(r+1)); summing telescopes to(2).

Let B_n=Σ_{r odd≤n}d_r/r. For even n, B_n=H_n−H_{n/2}/2, so

\[
 \left|B_n-\tfrac12(\log n+\gamma+\log2)\right|\le1/(2n).
\]

For odd n≥3, m=(n−1)/2 and B_n=H_n−H_m/2−1/(2n). Its difference from the same main term is

\[
 q_n+e_n-\tfrac12e_m,\qquad
 q_n=\tfrac12\log\frac n{n-1}-\frac1{2n}.
\]

Integral comparison gives0≤q_n≤1/[2n(n−1)]. Combining with(2) places this difference between−1/[2(n−1)] and1/[2(n−1)]. Thus, uniformly for n≥2,

\[
 \left|B_n-\tfrac12(\log n+\gamma+\log2)\right|\le1/n.      \tag{3}
\]

### 2. The regular csc part is a monotone quadrature

Put g(x)=csc x−1/x, g(0)=0, and A=π/2. As shown directly in -02, g is increasing on[0,A], with g(A)=1−2/π. Also

\[
 \int_0^A g(x)\,dx=\log(4/\pi),                              \tag{4}
\]

by the antiderivative log tan(x/2)−log x and its limit−log2 at0.

Let h=π/(2n). For even n, the odd-r nodes rh are midpoints of successive length2h intervals covering[0,A]. On one such interval the absolute midpoint-rule error for a monotone function is at most h times its endpoint variation: split the integral at the midpoint and bound its two signed parts separately. Summing gives at most h[g(A)−g(0)]. For odd n, the same midpoint intervals cover[0,A−h], and the remaining interval[A−h,A] uses its right endpoint A with weight h. Its error is at most h[g(A)−g(A−h)], so the same total bound holds. After normalizing,

\[
 \left|\frac2n\sum_{r\text{ odd}\le n}d_rg(rh)
            -\frac2\pi\log(4/\pi)\right|
 \le\frac{1-2/\pi}{n}.                                     \tag{5}
\]

Combining the singular part(4/π)B_n, (3), and(5) gives

\[
 |L_n-A_n|\le\frac{1+2/\pi}{n}<\frac2n.                     \tag{6}
\]

The odd-r sum is also the familiar endpoint Lebesgue value at n Chebyshev roots: pair cotangent summands at reflected root angles using cot t+tan t=2csc(2t). This interpretation is not needed for the proof.

### 3. Square and transfer the bounded remainder

Since0<γ<1, π>3 and log(8/π)<1, one has0<c₁<2 and0<A_n≤log n+2. For x≥1, (log x+2)/x decreases and is at most2. From(6), for n≥2,

\[
 |L_n^2-A_n^2|\le\frac{4A_n}{n}+\frac4{n^2}\le9.           \tag{7}
\]

The comparison -04 now gives|Λ_c−A_n²|≤63. Expanding A_n² produces exactly the leading coefficient4/π² and the coefficient b stated above; the remaining constant c₁² is below4. Hence the left side of(1) is below67, and in particular at most68. ∎

## Scope

All-n corner b-term with an explicit loose remainder. No conclusion about where the global Lebesgue constant is attained, the A3 constant c or κ, an asymptotic limit of the bounded remainder, or its parity independence.

## Open items

Required Claude audit. Supplementary actual independent check receipts are complete. Full A3 and global A4 remain OPEN. The next analytic refinement, if separately authorized, would analyze the bounded difference Λ_c−L_n² rather than infer its limit from fits.

## History

2026-11-01, Codex `/root/a2_develop`, requested gpt-6.1-sol xhigh; rules/input/gate/stop record in `../attempts/T-A2.md`. Written after the separate lower and two-sided-leading deliverables. A1-dependent work paused when its audit arrived and resumed only after root reviewed the findings and recorded the impact. No MEASURED fit was promoted to proof.
