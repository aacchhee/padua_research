# PD-T?proof-attempts-2-codex-70 — Exact Padua formula on all four edges

ID kind: PD-T.
Aliases: A4(a) all-edge closed form; symmetrized rhombus edge kernel.
Split from: the exact-edge-identity part of ordered target A4(a), programme source05 / OPEN_TARGETS A4.
Split into: edge-midpoint/central-branch gap remains a separate target.

## Statement

For every integer n>=1 use the even checkerboard Padua nodes B_jk=(cos a_j,cos b_k), a_j=j*pi/n, b_k=k*pi/(n+1), j+k even, and the positive weights w_jk=2epsilon_j eta_k/[n(n+1)] with half endpoint weights. Set

`D_n(u,v)=U_(n+1)((u+v)/2) U_(n+1)((v-u)/2)+U_n((u+v)/2) U_n((v-u)/2)`,

where U_m(s)=sin(ms)/sin(s) has its continuous extension at multiples of pi. For theta_c,phi_c in{0,pi} and every t in[0,pi],

\[
\begin{split}
\lambda_n(\cos\theta_c,\cos t)
 &=\sum_{j+k\,\mathrm{even}}w_{jk}\left|
 \frac{D_n(\theta_c+a_j,t+b_k)+D_n(\theta_c+a_j,t-b_k)}2
       -\cos(n\theta_c)(-1)^j\right|,                         \tag{1}\\
\lambda_n(\cos t,\cos\phi_c)
 &=\sum_{j+k\,\mathrm{even}}w_{jk}\left|
 \frac{D_n(t+a_j,\phi_c+b_k)+D_n(t-a_j,\phi_c+b_k)}2
       -\cos(nt)(-1)^j\right|.                              \tag{2}
\end{split}
\]

These are exact finite formulas on all four closed edges, including every node, corner and singular-looking argument. Each requires a fixed number of elementary evaluations per Padua node. Equivalently, if P_n(z)=T_(n+1)(z)+T_n(z), then

\[
 D_n(u,v)=\begin{cases}
 \dfrac{P_n(\cos v)-P_n(\cos u)}{\cos v-\cos u},&\cos v\ne\cos u,\\
 P_n'(\cos u),&\cos v=\cos u.
 \end{cases}                                                \tag{3}
\]

The divided difference in(3) is a polynomial in cos u,cos v, so(3) also supplies a purely polynomial evaluation of every removable limit in(1)–(2).

## Definitions

T_r(cos s)=cos(rs). Lambda_c is the maximum over the four corners only. The source's R(n) is a searched runner-up, not defined or identified by this theorem. Formula(1)'s free variable is the y angle and formula(2)'s free variable is the x angle. The exceptional corrected mode stays in x.

## Assumptions

Exact real arithmetic and the stated nodes, parity, weights and total-degree space Pi_n. No corner argmax, branch location or asymptotic assumption.

## Status by part

Overall status: **PROVED** (written analytic identity; required Claude audit PENDING).

| Part | Status |
|---|---|
| Both x edges and both y edges for all n,t | PROVED by the product-to-sum argument below |
| Every removable limit, including n=1 | PROVED by the finite polynomial divided difference |

This closes only the requested exact-edge-identity part. It proves no asymptotic gap and does not by itself complete A4(a).

## Depends on

**PD-T?proof-attempts-codex-01 (audit pending)**, specifically its independently proved general corrected cardinal identity and its finite rhombus sum. Dated2026-11-01 qualification: Part1 Claude audit accepted A1, minor dispositions completed, and Part1 merged; accepted alias PD-T101. The literal requested historical label is retained. Other ingredients are finite cosine sums and polynomial identities. Required Part2 Claude audit remains PENDING.

## Checks

The proof below is analytic and does not depend on a finite regression. The supplementary independent reconstruction in independent-checks-a4.md has read the complete all-edge and diagonal proof. The separately implemented code/a4reg_exact_check.py, frozen at SHA25613e8c524c4c21701bdee2a009cda2245d8f289d6a6cca0dba19afec1842f872e, was actually executed by its implementer and replayed by a different agent. Both exited0 under Python3.12.14, SymPy1.14, python-flint0.9/FLINT3.6; exact QQ(zeta) quotient arithmetic, no signs or tolerances. All n=1,…,6 checks passed:332 complete cardinal edge-polynomial identities for each formula,472 removable cardinal values,592 diagonal branch evaluations,6 full polynomial diagonal identities and24 edge partitions. The source guard remained unchanged. The developer elapsed2.408987s, separate replay2.415554s. Their outputs agree in every field except elapsed_seconds. The4561byte receipts are outputs/a4reg_exact_developer.json (SHA2561bfcfa3a08861911d2b6ec1cf857f797a0f14c3d22fd3acda1b43aa08a88cef1) and outputs/a4reg_exact_independent.json (SHA2567f21d8e033b260de220f578f2cf81fefd23101417a2fed8781bdd9285351b7a6); independent-execution-a4-regression.md records both actual commands and limitations. This finite regression supplements, and does not replace, the all-n proof or required Claude audit.

## Sources

Registered IDEA206 / programmeIDEA17, source05 and OPEN_TARGETS A4 at scientific pin9bd14a6d2c4da69139a10107d8a787f2be0c5c9e. The complete refreshed gate and current input state are in attempts/T-A4a.md and a4-input-preparation.md. This is a direct continuation of the classical corrected cardinal kernel, with no historical novelty or priority assertion.

## Proof or evidence

Write c_0=1 and c_r=2 for r>0. The accepted A1 proof establishes

\[
 L_{jk}(x,y)=w_{jk}\{K_n((x,y),B_{jk})-T_n(x)(-1)^j\},
\quad
 K_n(z,B)=\sum_{p+q\le n}c_pc_qT_p(z_1)T_p(B_1)T_q(z_2)T_q(B_2), \tag{4}
\]

and the finite rhombus identity

\[
 D_n(u,v)=\sum_{p+q\le n}c_pc_q\cos(pu)\cos(qv).              \tag{5}
\]

At x=cos theta_c, sin(p theta_c)=0 for every integer p, so the x factor in(4) is cos(p(theta_c+a_j)). In the free coordinate,

`cos(qt)cos(qb_k)=[cos(q(t+b_k))+cos(q(t-b_k))]/2`.

Insert this equality into the finite sum(4) and apply(5) to each term. The correction T_n(x)(−1)^j equals cos(n theta_c)(−1)^j. This proves the termwise cardinal formula inside(1). Positive w_jk may be moved outside its absolute value, and summation proves(1).

At y=cos phi_c the same argument fixes the second cosine factor and symmetrizes the first. Its correction remains T_n(cos t)(−1)^j=cos(nt)(−1)^j. This proves(2), without interchanging the two node meshes or the exceptional mode.

To prove(3), put S=(u+v)/2,T=(v−u)/2. Product-to-sum in the numerator of the product-U expression gives

\[
\begin{split}
&\sin((n+1)S)\sin((n+1)T)+\sin(nS)\sin(nT)\\
&\qquad=\tfrac12\{\cos((n+1)u)+\cos(nu)-\cos((n+1)v)-\cos(nv)\},
\end{split}
\]

whereas sin S sin T=(cos u−cos v)/2. When this denominator is nonzero the quotient is exactly(3). For every polynomial P, [P(z)−P(w)]/(z−w) is a polynomial in z,w and equals P'(w) on the diagonal. Consequently(3) extends continuously to all real u,v. The finite Fourier polynomial(5) and that divided-difference polynomial agree on the dense set cos u!=cos v, hence agree everywhere. This verifies every endpoint, repeated-angle and integer-pi limit at once and completes the proof. ∎

## Scope

Only exact edge point values for the stated Padua interpolation problem. No inference about the maximum along an edge, its central branch, a positive corner gap, neighbourhoods or the global square. All degrees n>=1 are included.

## Open items

The asymptotic/branch portion of A4(a) and required Claude audit. Supplementary exact regression/reconstruction are complete for the stated finite scope. Parts(b)/(c) remain route-note scope only.

## History

2026-11-01 after the15:24UTC A4 start, Codex gpt-6.1-sol xhigh. The preparatory registry and source reading occurred earlier without a mathematical attempt; changed MZ rows were refreshed before this candidate. All A5 source files remain frozen.
