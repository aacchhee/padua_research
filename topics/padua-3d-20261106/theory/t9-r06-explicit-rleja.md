# PD-T?padua-3d-20261106-codex-T9-r06-05 — a verified explicit minimal 3D polynomial upper bound

Aliases: T9-R06-U; T9-R06-TH04; explicit R-Leja lower-set specialization. Explicit dependency: LIT?padua-3d-20261106-codex-T9-r06-03/04. Provisional local ID, no global allocation.

Status: **PROVED transfer with explicit LITERATURE dependency**. This is an explicit specialization of the existing lower-set interpolation theorem and known R-Leja bounds. It is not a new priority claim; the primary source itself reports the earlier cubic bound in the number of multivariate points.

## Verified one-dimensional premise

Chkifa, arXiv:1503.01731, defines a distinct real projected Leja sequence R=(r_0,r_1,...) by taking real parts of a disk Leja sequence and skipping repeated real parts (§3). One explicit version has r_0=1,r_1=-1,r_2=0 and, for j>=2,

```
r_(2j-1)=sqrt((r_j+1)/2),   r_(2j)=-r_(2j-1).      (source (3.5))
```

This recursion determines every index. Let I_k interpolate at r_0,...,r_k and Delta_k=I_k-I_(k-1), with I_-1=0. Corollary 4.3, equation (4.8), in the primary author paper states that D_0=1 and, for 2^m<=k<2^(m+1),

```
D_k=||Delta_k|| <= 2^sigma1(k) 2^m <= (k+1)^2.
```

Here sigma1(k) counts the one bits. The last inequality follows from 2^sigma1(k)<=k+1 and 2^m<=k. The source's all-prefix Theorem 3.2 and introductory equation (1.11) also imply ||I_k||<=6 sqrt(5)(k+1)^2, including the separate dyadic Lobatto prefixes. This is an every-prefix assertion, not merely a dyadic-subsequence assertion. For the bound below, Corollary 4.3 directly suffices and avoids a factor from differences of prefix norms.

The 2013 JAT DOI 10.1016/j.jat.2012.11.005 verifies the intended paper's identity and real-projection subject, but its full mathematical text was not retrieved. The exact quadratic premise used here is imported from the accessible later primary author paper, not asserted on the basis of the 2013 abstract. The premise and proof dependency are explicit in `literature-round06/t9-chkifa2015.md`.

## Minimal 3D construction and bound

For n>=0 put

```
X_n={(r_a,r_b,r_c):a,b,c>=0, a+b+c<=n}.
```

The sequence is distinct, so X_n has exactly N=binom(n+3,3) points. The multivariate Newton evaluation matrix is triangular with nonzero diagonal in any order extending the coordinatewise partial order. Thus X_n is Pi_n-unisolvent. The established lower-set interpolation identity gives

```
I_(X_n)=sum_(a+b+c<=n) Delta_a tensor Delta_b tensor Delta_c.
```

Taking norms and using the imported bound proves

```
Lambda(X_n) <= sum_(a+b+c<=n) (a+1)^2(b+1)^2(c+1)^2
             = sum_(j=0)^min(3,n) binom(3,j)binom(n-j+9,9)
             <= 8 binom(n+9,9) = O(n^9)=O(N^3).
```

For the equality, sum_(k>=0)(k+1)^2 t^k=(1+t)/(1-t)^3. Cubing this series and taking cumulative coefficients gives (1+t)^3/(1-t)^10. Every term is nonnegative. This proves an explicit algebraic minimal 3D sequence with a polynomial bound, meeting the fallback aim, but it is far weaker than the desired logarithmic quality.

## Source comparison and priority gate

Chkifa's primary introduction explicitly attributes an earlier cubic-in-point-count multivariate R-Leja interpolation bound to Cohen–Chkifa, *On the Stability of Polynomial Interpolation Using Hierarchical Sampling*, reference [7], formula (25). The construction and O(N^3) order above are therefore already within known multivariate R-Leja theory. The locally useful deliverable is the checked every-prefix/difference premise and a transparent three-dimensional constant, not a first explicit polynomial-bound claim. Full text of the cited hierarchical-sampling chapter was not read; this priority gate is already supported by the accessible author's explicit statement.
