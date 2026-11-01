# PD-T?proof-attempts-2-codex-04 — A bounded comparison with a squared Chebyshev sum

Final ID: **PD-T159**. Provisional ID `PD-T?proof-attempts-2-codex-04` is retained as an alias. Registered after accepted Claude audit-01 and response-01; historical pending-audit notes below are superseded.

Canonical Split from (registration): PD-T098 (A2 split; full A3 remains OPEN).

Current audit note, 2026-11-01: Claude audit-01 accepted this record at its stated scope. Historical audit-pending statements below describe development checkpoints.

ID kind: PD-T.
Aliases: A2 positive Cauchy sum; node-angle simplification; same-mesh square comparison.
Split from: supporting comparison for OPEN_TARGETS A2; it is not itself a conjunct of the original asymptotic statement.
Split into: none; the lower bound, explicit leading estimate, and logarithmic coefficient are recorded separately as -01, -02, and -03.

## Statement

For every integer n≥2, let Λ_c(n) be the maximum of the Padua Lebesgue function over the four corners, with the exact even-checkerboard convention of `PD-T?proof-attempts-codex-01 (audit pending)`. Set

\[
 L_n=\frac2n\sum_{\substack{1\le r\le n\\r\text{ odd}}}d_r
       \csc\frac{r\pi}{2n},\qquad
 d_r=\begin{cases}1/2&r=n,\\1&r<n.\end{cases}
\]

Then

\[
 |\Lambda_c(n)-L_n^2|\le54.                                      \tag{1}
\]

More precisely the right side can be replaced by π⁴/2+4+1/(n+1). Every non-node corner has the same value. The two node corners have value1.

## Definitions

Write ε_j=1/2 for j=0,n and1 otherwise. Put a_j=jπ/n, b_k=kπ/(n+1), and η_k=1/2 at k=0,n+1 and1 otherwise. A sum over an odd checkerboard means j+k odd. A prime on its same-mesh counterpart gives half weight to each endpoint index0,n. The summand

\[
 f(a,b)=\frac{1+\cos b}{|\cos a-\cos b|}
\]

is used only when a≠b.

## Assumptions

Exact real arithmetic, n≥2, the specified first-coordinate exceptional kernel mode. No corner-argmax theorem and no asymptotic hypothesis.

## Status by part

Overall status: **PROVED** (written elementary proof; required Claude audit pending).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Positive finite sum, exact same-mesh square, and bound(1) | PROVED | Proof below; independent hand reconstruction by `/root/a2_independent_route` confirmed the square and deformation algebra |

Candidate disposition: retained algebraic/analytic proof route for the registered A2 target. No novelty or priority claim.

## Depends on

**PD-T?proof-attempts-codex-01 (audit pending)**, every-n corrected corner kernel identity. Literal label retained as requested; root reported on2026-11-01 that Claude audit-01 at `95279b833bca5967fcf47c1b71a56ff622185b4e` accepted A1 without a mathematical finding; upstream dispositions remain pending. Other ingredients are elementary trigonometric identities, sine concavity, and Σ_{l odd≥1}l⁻²=π²/8.

## Checks

The proof is analytic and does not depend on finite computations. Developer actually executed `python topics/padua-proof-attempts-2-20261101/code/a2_exact_check.py > topics/padua-proof-attempts-2-20261101/outputs/a2_exact_check.json`: Python3.12.14, SymPy1.14.0, exact QQ(ζ) quotients; every83 odd-board kernel terms, all6 coincident endpoints, and all6 same-mesh square identities passed for n=1,…,6. The positive-sum rewrite uses a hard-coded sign rule in an abstract cyclotomic field, without a certified real embedding; that sign step is proved analytically, not independently tested by this regression. Code SHA256 `94438117d4510b248beaac3e22afb23c159c21d107e17d300206b73751be4101`; receipt SHA256 `91db451c362d59c8bd1d155b10e0e5da275d62cced0e165b82cff7242fcc3d0e`,2067bytes. Initial ANP/integer equality-coercion plumbing was fixed before the full successful run; no identity mismatch. A different agent `/root/input_manifest` actually reran both exact and sanity scripts, exit0 and byte-identical; see `../independent-execution-a2.md`. The independent route agent also reconstructed, without executing code, the exact square and pointwise deformation bound; see `../independent-checks-a2.md`. These supplement the required Claude audit.

## Sources

Page-locator qualification (audit-01 F6): printed page numbers below are per developer reading; the auditor confirmed theorem/equation content through page-less text, without confirming PDF pagination. LIT-379 identifies KL2021 and LIT-312 identifies Bos2006.

LITERATURE background: Kolomoitsev–Lomako2021, arXiv:2009.07114v1, Theorem2.1 printed p.4; Lemma3.5, especially(3.20), printed pp.10–11; parity-subgrid Lemma3.6(3.29), printed pp.11–12. Full16-page paper read before method use; no source theorem supplies(1). Bos–Caliari–De Marchi–Vianello–Xu2006, author preprint `PaduaCurve3.pdf`, Theorem3 printed pp.10–12, gives the background global O(log² n) order. Primary links and reading record: `../attempts/T-A2.md`.

## Proof or evidence

### A. Simplify the summand at a non-node corner

Reflect coordinates about that corner. The angular indices now form the odd checkerboard, and the corrected A1 summand becomes D_n(a_j,b_k)−(−1)^j. Indeed corner addition and reflection give the same cosines in the finite rhombus sum, while the exceptional mode becomes(−1)^j. The two non-node corners give the same reflected odd board with identical endpoint weights. The node corners have value1 by cardinality.

For j+k odd and a=a_j,b=b_k not coincident, product-to-sum gives

\[
 D_n(a,b)=(-1)^j\frac{2+\cos a+\cos b}{\cos a-\cos b},\qquad
 |D_n(a,b)-(-1)^j|=2 f(a,b).                                  \tag{2}
\]

For example, the two product-U numerators are(−1)^j(1+cos a)/2 and(−1)^j(1+cos b)/2, and their common denominator is(cos a−cos b)/2. The only coincident angular points satisfy j/n=k/(n+1), hence are the endpoints. The odd board excludes(0,0) and includes(n,n+1). At(π,π), the A1 continuous value is D_n=(−1)^n(2n+1); its corrected absolute value is2n, with weighted contribution1/(n+1). For the other k=n+1 terms f=0. Therefore, with N=n(n+1),

\[
 \Lambda_c(n)=\frac4N\sum_{\substack{0\le j\le n,\ 0\le k\le n\\j+k\text{ odd}}}
       \varepsilon_j\eta_k f(a_j,b_k)+\frac1{n+1}.             \tag{3}
\]

### B. The equal-mesh reference is an exact square

Define

\[
 F_n=\frac4{n^2}\sum_{\substack{0\le j,k\le n\\j+k\text{ odd}}}
       \varepsilon_j\varepsilon_k f(a_j,a_k).                 \tag{4}
\]

No diagonal occurs on the odd board. Simultaneously reflecting j,k to n−j,n−k preserves the denominator and the weights and changes1+cos a_k to1−cos a_k. Averaging shows that its numerator can be replaced by1. Put h=π/(2n), c_r=csc(rh), and restrict to j>k, with s=j−k and r=j+k. Both r,s are positive odd integers and s≤r≤2n−s. The denominator is2 sin(rh)sin(sh). The two orders j>k and k>j cancel the factor2. For fixed s<n, the two endpoint r values s,2n−s each have half weight; all intervening r values have weight1. Since c_{2n−r}=c_r, this inner sum is

\[
 c_s+2\sum_{\substack{s<r<n\\r\text{ odd}}}c_r
       +\boldsymbol1_{n\text{ odd}}c_n.
\]

If s=n is allowed, its sole point(j,k)=(n,0) has weight1/4. Consequently the total sum in(4), after its factor4/n², is exactly the expansion of

\[
 F_n=\frac4{n^2}\left(\sum_{r\text{ odd},\,r\le n}d_rc_r\right)^2=L_n^2. \tag{5}
\]

### C. Bound the deformation of each off-diagonal term

For 0≤j,k≤n, j+k odd, write a=jπ/n, b_0=kπ/n, b_1=kπ/(n+1), l=|j−k|. The angular ordering is unchanged: if k>j, both b_i>a; if k<j, both b_i<a. The cases k=0 and j=n have zero deformation, so take k>0,j<n. Let δ=b_0−b_1=πk/N, B=(b_0+b_1)/2, S_i=(a+b_i)/2, and T_i=|a−b_i|/2. Exact subtraction yields

\[
 E_{jk}:=|f(a,b_1)-f(a,b_0)|
 =\frac{\cos^2(a/2)\sin B\sin(\delta/2)}
        {\sin S_0\sin S_1\sin T_0\sin T_1}.                 \tag{6}
\]

Using sin S_i≥cos(a/2)sin(b_i/2), followed by the cotangent addition identity,

\[
 \frac{\cos^2(a/2)\sin B}{\sin S_0\sin S_1}
 \le\cot(b_0/2)+\cot(b_1/2)
 \le2\cot(b_1/2)\le\pi\frac{n+1-k}{k}.                     \tag{7}
\]

The last inequality uses sin x≥2x/π and cos x=sin(π/2−x)≤π/2−x for0≤x≤π/2. Thus the numerator after this comparison is at mostπ²(n+1−k)/(2N).

If k<j, both sin T_i≥l/n, so E_{jk}≤π²n/(2l²). If k>j, put r=n−j. Then

\[
 \sin T_0\ge l/n,\qquad
 \sin T_1\ge\frac{n(l-1)+r}{N},\qquad n+1-k\le r\le n.
\]

Substitution into(6) gives

\[
 E_{jk}\le\frac{\pi^2nr}{2l[n(l-1)+r]}\le\frac{\pi^2n}{2l^2}. \tag{8}
\]

This includes l=1 and k=n; no uniform relative-gap assertion was used. All T_i lie[0,π/2], as required by the chord inequality. Summing(8), discarding endpoint weights, and using at most two k for each positive odd l and each j gives

\[
 \frac4N\sum_{j+k\text{ odd}}\varepsilon_j\eta_kE_{jk}
 \le\frac{4}{N}\frac{\pi^2n}{2}(n+1)
               2\sum_{l\text{ odd}\ge1}\frac1{l^2}
 =\frac{\pi^4}{2}.                                         \tag{9}
\]

### D. Endpoint weights and normalization

Use the actual weights ε_jη_k in both sums in the deformation comparison. At k=n the reference numerator1+cos a_n is zero (j=n is excluded), so replacing η_n by ε_n changes no reference value. All actual weights are at most1, as used in(9); there is no separate half-row error. Thus(9) compares Λ_c−1/(n+1) directly with nF_n/(n+1).

Finally, sin(rπ/(2n))≥r/n implies

\[
 L_n\le2\sum_{r\le n,\,r\text{ odd}}\frac1r\le2+\log n.
\]

For the last bound compare each term r=2q+1≥3 with(1/2)∫_{2q-1}^{2q+1}dt/t; summing gives the claimed harmonic bound. The function(log x+2)²/x decreases for x≥1, so

\[
 F_n/(n+1)\le(\log n+2)^2/n\le4.
\]

Combining(3)–(5),(9), the factor n/(n+1) multiplying F_n, and the exceptional endpoint1/(n+1) proves the more precise bound in the statement. For n≥2 it is less than54 (for exampleπ<22/7 suffices). Partition of unity gives every Lebesgue-function value≥1; since the node corners have value1 and the two non-node corners have a common value, that common value is Λ_c. ∎

## Scope

Only the finite corner value is compared; this says nothing about the global argmax. The constant54 is deliberately loose. The same-mesh reference is a calculational object, not a new Padua family.

## Open items

Required Claude audit; developer and actual independent exact/sanity receipts are complete. A2 parts are in separate records. No full A3 constant or expansion is claimed.

## History

2026-11-01, Codex mathematical developer, requested gpt-6.1-sol xhigh. Rules/input/gate/audit interruption are recorded in `../attempts/T-A2.md`. Independent route agent separately confirmed the same-mesh square and every deformation inequality without code. Original A2 statement is preserved in record -03; this supporting result does not alter its status by itself.
