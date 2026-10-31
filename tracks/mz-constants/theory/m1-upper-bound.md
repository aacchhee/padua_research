# PD-T014 — CC upper spectrum below two

Review update, 2026-10-31: final ID allocation and scoped independent Astra review are complete; see topics/mz-constants/independent-astra-01.md and ID_CROSSWALK.md. The original development-stage pending-review wording below is historical. Required Claude audit and unresolved literature/novelty coverage remain PENDING. This administrative update changes no mathematical claim or proof.

ID kind: PD-T. Aliases: absolute-coefficient Z-matrix comparison; CC upper MZ bound.
Split from: frozen M1 target \(\lambda_{\max}(Q_N|_{\Pi_{N-1}})<2\) for all \(N\ge2\).
Split into: supporting coefficient-floor lemma PD-T015, not a part of the target's own statement.

## Statement

For every integer \(N\ge2\) and every nonzero real polynomial \(p\in\Pi_{N-1}\), the Lebesgue CC rule on the \(N+1\) nodes \(\cos(j\pi/N)\) satisfies
\[
0<Q_N(p^2)\le\left(2-\frac2{\pi N}\right)\int_{-1}^1p(x)^2\,dx
<2\int_{-1}^1p(x)^2\,dx.\tag{1}
\]
Equivalently, all eigenvalues of its discrete Gram matrix in any continuous-Lebesgue-orthonormal basis for \(\Pi_{N-1}\) belong to \((0,2-2/(\pi N)]\). The same bound holds on every subspace \(\Pi_n\), \(n\le N-1\).

## Definitions, assumptions and status

CC weights, moments \(\mu_k\), the continuous mass matrix \(M\), the discrete mass matrix \(R\), and \(D=2(M-R)\) are defined in PD-T013. Throughout this proof their indices are \(0,\ldots,N-1\).

Overall status: **PROVED** in development; independent pinned review and prior-art screening remain pending. The strict target and its explicit finite-N strengthening are proved analytically. No claim about the sharp limiting upper constant is included.

Depends on: PD-T013 (exact defect/positive weights) and PD-T015 (quantitative coefficient floor). The qualitative upper bound \(<2\) uses only the exact defect and positivity of the continuous integral, not the floor or CC-weight positivity.

## Proof

Let \(A=2M-R=M+D/2\). We first show that every off-diagonal entry of \(A\) is nonpositive. Opposite parities give zero. For \(i\ne j\) of the same parity, put \(d=|i-j|\ge2\) and \(s=i+j\). If \(s\le N\), exactness gives \(A_{ij}=M_{ij}<0\). If \(s>N\), put \(r=2N-s\). Since \(i,j\le N-1\),
\[
r-d=2\bigl(N-\max(i,j)\bigr)\ge2.
\]
In particular \(r>d\ge2\), and the exact formula is
\[
A_{ij}=-\frac1{d^2-1}-\frac2{s^2-1}+\frac1{r^2-1}<0.\tag{2}
\]

Write \(p=\sum_{i=0}^{N-1}a_iT_i\) and \(v_i=|a_i|\). A symmetric matrix with nonpositive off-diagonal entries satisfies
\[
a^TAa\ge v^TAv,
\]
because its diagonal terms agree and \(a_i a_j\le |a_i||a_j|\). Entrywise \(D\ge0\), so
\[
2\int p^2-Q_N(p^2)=a^TAa\ge v^TMv+\tfrac12 v^TDv\ge v^TMv>0.\tag{3}
\]
The strict last inequality follows because \(v\ne0\) is the coefficient vector of a nonzero polynomial. This already proves the frozen qualitative target; it never uses positive semidefiniteness of \(D\).

To quantify the gap, set \(E=\operatorname{diag}(2,1,\ldots,1)\). The coefficient-floor lemma gives
\[
v^TMv\ge\frac1N v^TEv=\frac1N a^TEa
\ge\frac2{\pi N}a^TMa=\frac2{\pi N}\int p^2.
\]
Combine this with (3) to obtain the upper inequality in (1). Its positivity follows from the locally proved positive CC weights and polynomial unisolvence. Restriction proves the assertion for smaller degrees.

## Checks

The exact rational checker `tracks/mz-constants/code/m1_exact_check.py` checks the defect, entrywise signs, off-diagonal signs of \(A\), telescoping floor and obstruction in the finite range recorded in `topics/mz-constants/directions/M1/RUNS.md`. Optional floating generalized eigenvalues are explicitly MEASURED. The universal theorem depends on the written proof, not a finite numerical extrapolation.

The independent adversarial auditor reconstructed (2)–(3) from cosine moments before this pinned file was available and reported no gap; this is provisional analytic feedback, not completed pinned audit or acceptance. A separate reconstruction/rerun must identify file hashes.

## Sources, scope and open items

Closest local predecessor: supplied Hankel identity and source suggestion to exploit entrywise positivity, recorded in `literature/records/mz-input-reports.md`. Those notes do not supply this proof. Historical CC product-integration/interpolation prior art remains under documented screen in `topics/mz-constants/literature-search.md`; no novelty/priority claim is made. No private C4 theorem or external result is used.

The bound degrades toward two as \(N\) grows. The much smaller measured limiting value near 1.004437 remains OPEN as a sharp asymptotic question, and is not needed for (1). Full degree \(\Pi_N\) is expressly excluded and violates the threshold; see PD-T016.

## History

2026-10-31, Codex gpt-6.1-sol xhigh, rules/base `d36722823441dc40c6e19d69a174459348dd309c`: frozen strict target proved by a Z-matrix sign argument; strengthened with an explicit finite-N gap and supporting lemma split. No manuscript or acceptance claim made.
