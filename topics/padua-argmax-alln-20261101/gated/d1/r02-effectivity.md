# Direction 1, round 2 — quantitative primitive diagnosis

Date: 2026-11-02. Codex, parent-assigned gpt-6.1-sol xhigh; runtime
metadata not independently exposed. Rules/snapshot head
`2dde541f1e5af239cae6e93e4438b9be89d15d87`; scientific input
`7d308b10d946b607ae0690454f6c0103690775a4`.
Contract: [round 2](r02-contract.md). This is bounded diagnosis after the
round-1 GO, not another phase scan or a future-round execution.

The global and local primitive lemmas are now split, with their complete
proofs, into [global bound](../../theory/gated-codex-02-two-phase-global-bound.md)
and [local gain](../../theory/gated-codex-03-two-phase-local-gain.md).
The distinct Astra xhigh [round-1 reconstruction](../checks/d1-r01.md)
reported no blocking finding. The split preserves exactly those claims;
the refinements investigated here are not silently added to either theorem.
Required Claude audit and all-degree PD-T099 remain PENDING / OPEN,
respectively.

## What is effective and what is missing

The proof currently supplies an unspecified absolute global constant,
a small local phase radius, unspecified constants in the local gain,
and compact-uniform defect convergence without a numerical modulus.
These are genuine quantifier-level proofs but do not give a computable
useful degree threshold as written. The paired-defect positive rectangle
provides an explicit compact lower limit; a lower limit alone supplies no
finite-degree error budget.

Three separate quantitative obligations remain:

1. An explicit global phase exclusion that enters the actual local window.
   From the coarse bound alone one gets
   \((1-a)\Lambda_c\le C_g\log m+O(1)\). To force
   \(\rho<\rho_0\), this can require
   \(\log n\gtrsim C_g/\rho_0^2\). Merely writing down a large
   \(C_g\), or shrinking \(\rho_0\), can make this threshold worse.
2. A useful numerical local excess bound, retaining the true endpoint cusp.
3. A numerical paired-defect error modulus, uniform in the unused angle and
   both phases on the same window selected in step 1. Endpoint tails,
   moving pole tubes, and Riemann approximation must all be quantified.

Improving item 2 does not resolve items 1 or 3. No degree threshold or
feasible finite-computation range is claimed in this diagnosis.

## A sharper collision-family estimate is viable

Use the notation of local proof section 5. For
\(B=\{r=j+1,j\ge2n/3\}\), write \(h=n-j\), and at zero phase set
\(x=h\pi/n,y=h\pi/m,X=(x+y)/2,T=(x-y)/2\).
For \(1\le h\le n/3\),

\[
 F_h(0,0)=\frac{1-\cos y}{\cos y-\cos x}
        =\frac{\sin^2(y/2)}{\sin X\sin T}
        \ge\frac{y^2}{\pi^2XT}
        \ge\frac{4}{3\pi^2}\,n.                         \tag{D1}
\]

Here \(\sin(y/2)\ge y/\pi\), \(X\le x\),
\(T=h\pi/(2nm)\), and \(n/m\ge2/3\). The endpoint \(h=0\)
has the true polynomial value \(F_0(0,0)=n\). This is a uniform
positive lower bound on the whole family, not just pointwise positivity.

The finite-sum identity from round 1 is

\[
 D_n=(-1)^n\{V_n(X)U_m(T)+U_n(X)V_n(T)\},\quad
 V_n(z)=\frac{\cos((2n+1)z/2)}{\cos(z/2)}.                 \tag{D2}
\]

The arguments stay in a fixed interval on which \(\cos(z/2)\ge c>0\).
Consequently \(|V_n^{(k)}|\le C_kn^k\), \(k=0,1,2\).
Finite Fourier sums give \(|U_m^{(k)}(T)|\le C_kn^{k+1}\).
For \(h\ge1\), differentiating the sine quotient gives

\[
 |U_n(X)|\le Cn/h,\quad
 |U_n'(X)|\le Cn^2(h^{-1}+h^{-2}),
\]
\[
 |U_n''(X)|\le Cn^3(h^{-1}+h^{-2}+h^{-3}).                \tag{D3}
\]

For \(h=0\), use the global finite-sum bounds
\(n,Cn^2,Cn^3\). Every phase derivative of \(X,T\) is
\(O(1/n)\), with zero second derivatives. Applying the product rule to
(D2), and retaining the corrected cosine, proves

\[
 |F_h|+|\nabla_{\alpha,\beta}F_h|
                  +|\nabla^2_{\alpha,\beta}F_h|\le C_B n. \tag{D4}
\]

These are elementary analytic bounds with an unspecified absolute
\(C_B\). Together (D1) and the gradient part of (D4) show that, on
a sufficiently small fixed diamond
\(\rho\le\rho_B\), all \(F_h\) remain at least
\(2n/(3\pi^2)\). For example it suffices to take
\(\rho_B\le\min(\rho_0,2/(3\pi^2 C_B))\), after fixing a common valid derivative
constant. Thus this family has no absolute-value cusp in that window.
Symmetric Taylor, the Hessian bound, and \(1-a=O(\rho^2)\) give

\[
 \frac1N\sum_{B} e_jf_r
 \left[\sum_{\sigma,\tau=\pm1}
 |F_{jr}(\sigma\alpha,\tau\beta)|
             -4a|F_{jr}(0,0)|\right]\le C\rho^2.          \tag{D5}
\]

The normalization contains \(O(n)\) terms of Hessian size \(O(n)\).
This explains why the round-1 \(C\rho\) allowance on \(B\) is
avoidable. The derivation establishes viability of a quadratic family
bound; it does not yet provide numerical \(C_B,\rho_B\) useful for
effectivity. The next independent check should inspect (D1)–(D5), in
particular every endpoint and the \(U_n''\) chain-rule factors.

## A linear endpoint cusp cannot be removed

There is a different zero family, \(r=m,j<n\), with \(j+n\) even.
It is regular and has \(F_{jr}(0,0)=0\). Differentiating the exact
numerator at zero, with \(u_0=j\pi/n\), gives

\[
 \partial_\alpha F_{j,m}(0,0)
              =-\frac{\sin u_0}{2(1+\cos u_0)}
              =-\tfrac12\tan(u_0/2),\qquad
 \partial_\beta F_{j,m}(0,0)=0.                           \tag{D6}
\]

Every nonzero zero-phase term is smooth at zero. Its simultaneous
reflections cancel its linear derivative in (2) of the local theorem.
The only zero-phase terms are this regular row; the apparent common
endpoint is the nonzero polynomial \(B\) term above. Applying the
endpoint half weight and both reflections to (D6) therefore gives the
exact finite-degree directional slope

\[
 S_n(\alpha,0)=\Lambda_c(n)+L_n|\alpha|+o(|\alpha|),
 \quad
 L_n=\frac1{nm}\sum_{k=1}^{\lfloor n/2\rfloor}
                                \cot(k\pi/n).            \tag{D7}
\]

This is a finite-sum Taylor calculation, not a fit or a transferred
literature statement. In particular \(L_n>0\) for \(n\ge3\), while
\(L_2=0\). The elementary expansion
\(\cot t=1/t+O(t)\) uniformly on \((0,\pi/2]\) gives

\[
 L_n=\frac{\log n}{\pi n}+O(1/n),\qquad
 0\le L_n\le\frac{H_{\lfloor n/2\rfloor}}{\pi m}.         \tag{D8}
\]

Consequently a pure quadratic bound
\(S_n\le a\Lambda_c+C\rho^2\log m\), for every phase in a
fixed neighborhood, is false for each fixed \(n\ge3\) and every
finite \(C\): divide by \(|\alpha|\) in (D7) and let
\(\alpha\to0\). The next local formulation must retain a linear
coefficient that can shrink with degree. This scoped obstruction does not
reject the existing local gain theorem, whose \(C\rho\) term allows it.
No new globally registered negative claim is allocated in this diagnostic.

## Keep the square-root sign-change cost

The local proof's far-row numerator support has
\(y\le C(\rho+\sqrt{\rho x})\). Before the final coarse
\(O(\rho)\) simplification, its estimate was

\[
 C\rho^{3/2}+C\rho^2\log(2+1/\rho)
                       +C\rho\log(m)/m.
\]

The near-corner part was
\(C(\rho^2+\rho/n)\log(n\rho+2)\). Thus, after (D5), the existing
proof reduces a sharper local estimate to numerical constants in

\[
 S_n\le a\Lambda_c
       +C_2\rho^2\log m+C_{3/2}\rho^{3/2}
       +C_e\rho\,\frac{1+\log m}{n}.                    \tag{Q}
\]

Indeed \(\rho^2\log(2+1/\rho)\le C\rho^{3/2}\) for bounded small
\(\rho\). The last term includes the necessary slope (D7). There is
no valid reason in the present argument to replace the square-root support
by an \(O(\rho)\)-width band or to discard its \(\rho^{3/2}\) cost.
No lower bound proving the \(\rho^{3/2}\) exponent sharp is asserted.

With unspecified constants and a sufficiently small fixed radius, (Q)
would improve the asymptotic excess estimate to

\[
 O(\log^{-6}n)+O(n^{-2}).                                \tag{D9}
\]

For this implication absorb \(C_2\rho^2\log m\) into the leading
quadratic loss, split that negative loss in two, and optimize
\(-c\rho^2\log^2 n+C_{3/2}\rho^{3/2}\) and
\(-c\rho^2\log^2 n+C_e\rho(1+\log m)/n\) separately.
This implication is analytic but conditional on an accepted (Q); neither
(Q) with numerical constants nor (D9) is substituted into the published
local theorem in this round.

## Next falsifiable lemma and gate recommendation

**Next local lemma, OPEN in effective form:** produce explicit numbers
\(\rho_*,C_2,C_{3/2},C_e>0\), independently checkable elementary
inequalities proving (Q) for all \(n\ge2\), \(\rho\le\rho_*\),
and explicitly verify (D4) and uniform positivity on \(B\) for the
same \(\rho_*\). Report the resulting numerical local-excess envelope
and its actual comparison with the chosen compact defect margin. A bound
with only unspecified constants is not completion of this lemma.

Cheapest discriminating test: analytically bound the derivatives in (D2)
with explicit constants and test the endpoint slope identity (D7) against
those constants. This requires no larger degree grid. A failure of
positivity or Hessian control on the proposed radius kills that radius
and constant choice; a polynomially larger Hessian on the whole family
would kill this particular quadratic repair. Any proposed endpoint
coefficient below \(L_n\) is contradicted by the exact directional slope.
Keep failed numerical constants and radius choices if the next round is
authorized; none were invented or tested here.

**Recommendation: GO for one bounded explicit-constant local repair,
subject to the orchestrator's campaign gate.** The concrete reason for
hope is the finite-sum Hessian structure plus the exact shrinking cusp
slope, which distinguishes that test from another scan or fit. A stronger
recommendation toward a usable all-degree threshold is not justified:
global phase entry and the paired-defect error modulus remain separate
bottlenecks. If that next local calculation only supplies another
unspecified constant, or cannot be matched to a specific global/defect
budget, stop the quantitative direction rather than spend rounds on
larger scans.

No new round, numerical phase scan, external-source transfer, Git action,
shared-registry update, or direction-2 work was executed by this worker.
Actual checks: read the round-2 contract and round-1 check receipt; split
and reread the two theorem records; derive (D1)–(D8) algebraically; inspect
the retained pre-simplification sign-change estimates. Independent review
of these new diagnostic calculations remains needed.

## Dated supersession — direction 1 round 3, 2026-11-02

The orchestrator's independently checked
[explicit finite projected-defect block](../../theory/gated-codex-05-finite-projected-defect.md)
supersedes the missing defect-modulus item 3 and the corresponding later
bottleneck wording above. It gives a positive finite-degree bound on an
explicit phase radius; no convergence error modulus is needed for that
comparison. The old diagnosis is retained as history.

The separate [round-3 constant calculation](r03-explicit-local.md) addresses
the sharpened local estimate on an explicit radius. Its constants give an
unusable local degree scale, while quantitative global phase entry remains
unresolved. Its STOP recommendation concerns that coarse quantitative
implementation only; the orchestrator controls the direction-level gate.
