# Internal referee report: exposition, notation and literature (MZ-SP manuscript)

- Referee: Claude Opus 5.5 (`claude-opus-5-5`), effort high. I did not write the paper. I made no manuscript edits and ran no git commands that change state (read-only `git rev-parse`: HEAD `8f08d9a82a174974b0b26ed5bb98932835f2fc71`, clean tree).
- Manuscript: `tracks/mz-constants/paper-sp/manuscript.tex`, sha256 956fdee6…; `refs.bib`, sha256 318b8320…. Line numbers below refer to this file.
- Build: `tools/build.sh … /tmp/ref-sp-expo` gives 47 A4 pages (elsarticle preprint, 12pt). There are no log issues and no BibTeX warnings. I read the PDF through pdftotext and inspected pages 1, 21 and 30 as images.
- Page map (PDF):
  - §1 pp. 1–3; §2 pp. 3–6; §3 pp. 6–7; §4 pp. 7–10; §5 pp. 10–16; §6 pp. 16–22 (6.2 from p. 20); §7 pp. 22–25; §8 pp. 25–29; §9 pp. 29–30;
  - data statement p. 30; App. A pp. 31–40; App. B pp. 40–46; references p. 47.
- Register checked: `topics/padua-mz-paper-20261113/notation-sp.md`.
- Literature checked:
  - `literature/INDEX.md` and the records `mz2d-sommariva-vianello-zanovello-2008` (LIT-427), `mz2d-caliari-demarchi-vianello-2007` (LIT-428), `kolomoitsev-lomako-prestin-2018` (LIT-488), `wu-aml-2026` (LIT-489), `mz-an-sommariva-vianello-2026` (LIT-045), `mz-an-wu-2022` (LIT-046) and `an-ran-wu-2025` (LIT-387);
  - `lattice-unisolvence/records/{padua-2006, xu-1996, padua-ideal-2007, caliari-demarchi-vianello-2008, demarchi-2022}`, plus the records `caliari-dmv-2008` and `bos-dmv-xu-2007`;
  - for comparison with the companion paper, the MZ-CC manuscript and its frozen numbering in `correspondence-cc.md`.
- Severity scale:
  - MAJOR: a JAT referee would ask for the change, or the text breaks one of AC's criteria;
  - MINOR;
  - TYPO.
- Math: I spot-checked arithmetic only where I read for exposition, namely Lemma A.2/A.3 (constants 15/2 and 120), Lemma 5.5 (the u·g identity), Prop. 5.8 (2^16 > 3^10), the A_R inequality in Thm 7.1, and Remark 6.4's 64/√8 ≤ 24. I found no error. The mathematical audit belongs to the math referee.

## Overall assessment

The paper is mathematically coherent and complete, and it is honest about its scope:
- the abstract and §1 match the theorems almost everywhere;
- the computer-assisted statements (Props. 6.9, 8.1, 8.2) are labelled in the text;
- the measured material is fenced off in §8.3;
- MZ-CC is cited for the three CC inputs (Prop. 2.2).

A JAT referee would still ask for five changes:
1. Situate the work in the Padua literature (introduction) and name the classical tools it re-proves, Mehler–Heine above all.
2. Fix several global notation clashes that break the register, worst of all J₀ used both for Bessel and for rectangle integrals.
3. Define core terms that are used before, or without, a definition: 𝒫_n in §1, Π_n, "CC", "strong MZ constant", "carrier", "signed energy".
4. Remove the audit-trail sentences left in proofs and in §8.
5. Correct the abstract's "Exact spectral brackets" and add the computer-assisted labels there.

Length is not a problem for JAT, and the paper would be about 25 to 28 journal pages. About 3–4 preprint pages can be cut without losing explanation (§I). About 1.5–2 pages should be added: motivation, section openings and a notation table.

---

## A. MAJOR

**A1. MAJOR: The introduction does not place the paper in the Padua literature. Section 1, ll. 76–98.**
- Problem:
  - The reader is not told why Padua points matter. They are the first explicit unisolvent total-degree set on the square with an O(log² m) Lebesgue constant. They have public software (Padua2D/Padua2DM). Their signed Lebesgue rule (non-tensorial Clenshaw–Curtis) is the one that software uses.
  - The reader is not told where the signed rule is used either: hyperinterpolation and least squares with this rule, and quadrature-based Galerkin.
  - The paper that introduced the points (Caliari–De Marchi–Vianello 2005), the ideal-theory/unisolvence paper (Bos–De Marchi–Vianello–Xu 2007) and Sloan's hyperinterpolation (1995) are absent. The last is notable because "hyperinterpolation" appears in the keywords and in the title of Section 7.
  - Of the paper's own literature context, An–Wu 2022 (LIT-046, read) is uncited. It defines exactly the "hyperinterpolation with relaxed quadrature exactness" setting that $H_{m,n}$ instantiates, though for positive weights.
- Fix: insert before "Lagrange interpolation at the Padua points…" (l. 79) a paragraph of about six lines, citing only at read scope (see §G for the reading status of each item).
  > Padua points were introduced by Caliari, De Marchi and Vianello [CDMV05] and are, up to symmetries, the first known explicit unisolvent set for total-degree interpolation on the square whose Lebesgue constant grows like $O(\log^2 m)$ [BCDMVX06, Thm.~3]; the ideal-theoretic description is due to [BDMVX07]. Four families related by symmetries of the square exist [CDMV08]; we use the family \eqref{eq:padua}.

  In §7's opening (l. 1235), add:
  > For a rule that is exact only beyond degree $n$ but not through $2n$, the operator $H_{m,n}$ is the hyperinterpolant of Sloan [Sl95] with relaxed quadrature exactness, studied for positive weights by An and Wu [LIT-046]. The survey [LIT-387, §2.3] notes that a positive-weight hyperinterpolation built directly on the degree-$n$ Padua set is open, because that rule is not exact on $\mathcal P_{2n}$; the signed operator here is a different object.

  The LIT-387 sentence must stay at that scope: the record says "should not be cited as saying signed Padua hyperinterpolation is open or closed".

**A2. MAJOR: Global notation clashes that break the register (`notation-sp.md`).** Full list in §D. The four that a reader will actually trip over:
1. **J₀ has two meanings in §6.2 and App. B.** Bessel $J_0$ appears in (K-infty), in $\psi_{jk}$ and in $\Sigma_t$. The rectangle integrals $J_t(U,U')$ appear at l. 1140, in the statement of Prop. 6.8(c) at l. 1167, and at ll. 2416 and 2465. So "$J_0(U_i,U_j)$" and "$J_0(\pi ja)$" stand side by side, and $J_\pm(a)$ of §5 is a third family. The register prescribes $\mathcal J_t$, and that rename was not applied. Fix: rename to $\mathcal J_t(U,U')$ throughout.
2. **$T_R$ against the Chebyshev $T_a$.** The tail $T_R(t)=\sum_{a>R}t_a\cos(2at)$ (l. 423) is made global for App. A in its preamble (l. 1674). The same appendix uses $T_m(x_j)$ (l. 1683), and the bracket proof uses $T_A$, $T_B$. Fix: write the tail as $\mathcal R_R$ or $\tau_R$, avoiding τ (see 3), e.g. $\mathrm{tail}_R$ or $\Xi_R$.
3. **τ is both the degree ratio (register: "only") and $\tau=\min(t,\pi-t)$** in the *statement* of Lemma A.1 (l. 1693) and in (S-remainder). The same applies to σ: $\sigma(B)$ is the spectrum, and $\sigma=\min(s,\pi-s)$ in Lemma A.1. Fix: $\hat t=\min(t,\pi-t)$, $\hat s=\min(s,\pi-s)$.
4. **$E_k(f)$ against $E_K(m)$.** The best-approximation error (Remark 7.2) and the finite-comparison error (Remark 6.4) are both global and differ only by the case of the index. Fix: write $\mathcal E_K(m)$ or $\epsilon_K(m)$ for Remark 6.4.

   Two further collisions of global symbols:
   - $d_m(x,y)$ is the density (Lemma 4.1) while $d_j=\min(j,N-j)$ is the distance. $d_m$ reads as "the distance at index m". Fix: $\varpi_m$ or $\delta_m$ for the density, or $\mathrm{dens}_m$.
   - $h_a=\int T_a$ (§4, App. A, Prop. 7.3) against $h(x)=x^2\log|x|$ in Lemma 5.5, Props. 5.7 and 5.8. Fix: write the latter as $\ell(x)$ with $\Delta^4\ell$, or rename $h_a$ to $\mu_a$ (as in SVZ08's moments).

**A3. MAJOR: Core terms used before definition or never defined.**
- **𝒫_n.** Used in §1 (ll. 62, 77, 85, 102) and defined only at l. 282 in §3.
- **Π_n (univariate) is never defined.** It is first used at l. 180 as "$\ell_j\in\Pn_N$". The register still lists "Π_n" as *the* total-degree space, which is the reverse of the text.
  - Fix: at l. 60, "Let $\Pi_n$ denote real univariate polynomials of degree at most $n$ and $\mathcal P_n$ bivariate polynomials of total degree at most $n$."
  - Then delete the definition at l. 282 and update the register.
- **"CC" is never expanded.** It is first used at l. 174. Fix: "Clenshaw–Curtis (CC)" at l. 95 or l. 143.
- **"strong MZ constant" is never defined**, but it appears in Result B (l. 118), in the statement of Cor. 5.3 (l. 652) and in Remark 5.4.
  - Fix: after (eq:eta), add:
    > A uniform strong MZ constant at degree ratio $\tau$ is a number $\eta_\tau<1$ with $\|I-G_{m,\lfloor\tau m\rfloor}\|_2\le\eta_\tau$ for all $m$; the weak constants are $\lambda_{\min}$ and $\lambda_{\max}$ themselves, in the terminology of [ASV27].
- **"carrier" is never defined.** It appears in the §5 title, Thm 5.1 and Prop. 5.6. Fix: open §5 with a sentence such as "We call *carriers* explicit trial polynomials that concentrate near one corner of the square and that the signed weights see with a definite sign."
- **"signed energy" is never defined.** It appears in Prop. 5.2, l. 611, and l. 780. Fix: "We call $Q_m^{\mathrm P}(p^2)$ the signed energy of $p$" at its first use.
- **Harmonic numbers are undefined.** See $H_{\lfloor R/2\rfloor}$ (l. 436) and $H_L$ (l. 1724). Fix: "$H_q=\sum_{i=1}^q1/i$".
- **"mode 2" is ill-defined** (l. 1549, "the span of the second eigenvalue"). See B14.

**A4. MAJOR: Visible process and audit language.** AC's criterion is "no repository/process language in visible text". These sentences answer an internal auditor, not a JAT reader:

| Line | Text | Fix |
|---|---|---|
| 498 | "No coordinate interchange in the cardinal density is used." | delete |
| 594–595 | "No finite threshold is inferred from these limits." | "The divergences are asymptotic; no onset degree follows." (or delete; §9 item 3 says it) |
| 789–790 | "No boundary-value packet is assumed admissible." | delete ("packet" is undefined) |
| 793–796 | "raw energy suprema … nonunit continuous packet norms" | rewrite as a remark: "The limits $-16ab/9$ and $8ab/9$ of the unnormalized energies have suprema $1/9$ and $1/36$ on the closures of the parameter domains; they are not Rayleigh quotients, since the carriers do not have unit norm." |
| 856–857 | "No negative-corner estimate is subtracted and no boundary parameter family is assumed admissible." | delete |
| 1199 | "Sharper arithmetic … has not been carried out." | "We have not attempted sharper enclosures." |
| 1499 | proof heading "Certificate reduction and trust" | "Proof (computer-assisted)" |
| 1519 | "No eigensolver accuracy is a premise" | "The argument does not use the accuracy of any eigensolver" |
| 1523–1524 | "Of the even degrees for which a witness was certified, $m=1240$ is the smallest" | delete (it reveals search history and says nothing about mathematics) |
| 1565–1569 | "noticed a posteriori … prescribed in advance … compressed branches" | "These secants are within $0.0034$ of the second proxy in (4). We record this only as an observation; it carries no information about $c_\pm$." |
| 664–677, Remark 5.4 | "the natural conjectures … are false" | unattributed conjectures from inside the project. Rephrase as consequences: "Consequently, for large $m$ the form on $\mathcal P_{m-1}$ is indefinite, its largest eigenvalue is unbounded, its defect at $n=m-1$ tends to $+\infty$, and no fixed ratio $\tau\in(1/2,1)$ admits a uniform strong MZ constant." Keep the sentence on positive Chebyshev Padua and tensor CC. |
| 115, 1193, 1625–1660 | "receipts" (×4) | "output logs" / "certificate files" |
| 1612 | "Code and evidence" | "Code and data" |

The many scope disclaimers ("is not asserted", "no claim is made", ten instances: ll. 407, 759, 873–876, 898, 1028, 1049, 1107, 1422, …) are accurate. Together, though, they read like an audit trail. Keep the ones inside statements that limit scope: Prop. 5.6 l. 758, Thm 6.3 l. 1027, Prop. 8.1 l. 1422. Shorten the rest. The negative list in Prop. 5.8 (ll. 873–876) can become one sentence: "The bound concerns only these scalar trial families."

**A5. MAJOR: The abstract states the finite results inaccurately and omits two labels.** (ll. 33–50)
- "Exact spectral brackets at six degrees up to $80$" is wrong. Prop. 8.1 gives *certified* brackets of width 10⁻⁶ with exact rational endpoints. They are not exact eigenvalues. The degrees also run from 10, not "up to 80".
- The brackets and the witnesses are computer-assisted, but the abstract labels only the enclosure as such.
- "For every fixed ratio $n/m>1/2$" overstates Cor. 5.3, which is stated for $\tau\in(1/2,1)$. The Gram matrix is defined for $n\le m$.
- The abstract does not say that the enclosure fixes no digit, nor that $c_\pm$ are open. The BRIEF and plan asked for "what is open".
- Fix (replace the last three sentences):
  > Its norm is the modulus of its least eigenvalue, which is simple, and $0<c_+<\|B\|$. A computer-assisted certificate gives $0.0131\le\|B\|\le0.478$; no decimal digit of the limits is determined. In contrast, the direct signed coefficient hyperinterpolant has a $C\to L^2$ norm below thirty, uniformly. Computer-assisted spectral brackets at six degrees between $10$ and $80$, and computer-assisted negative directions at three degrees above $1000$, complete the picture.

  Also change "For every fixed ratio $n/m>1/2$" to "For every fixed ratio $1/2<n/m<1$".

**A6. MAJOR: Named classical tools are re-proved without being named.**
- **Lemma 6.2 is a quantitative Mehler–Heine formula.** It says $P_k(\cos(u/k))\to J_0(u)$, here with the kernel $\mathcal K_{m-1}$. A JAT referee will say so at once.
  - Fix: before Lemma 6.2 (l. 978), add "The limit is a two-variable, quantitative form of the Mehler–Heine formula $\lim_k\mathsf P_k(\cos(z/k))=J_0(z)$ [Szegő, Thm 8.1.1; DLMF §18.11]."
  - Also name it in App. A.2 Step 2.
- **App. A.2 Step 1 ("classical facts, with proofs", about one page)** proves standard results: Rodrigues, the generating function, orthogonality and the norm of $\mathsf P_k$, Laplace's integral (DLMF §18.10), and Poisson's integral for $J_0$ (DLMF 10.9.1).
  - AC's rule is "cited or stated in the form used". Stating them with DLMF citations (§§18.5, 18.9–18.12, 10.9) satisfies it and saves about 0.8 page.
  - If AC prefers self-containedness, keep the proofs but add the citations.
- **Prop. 6.7 is a Jentzsch / Perron–Frobenius-type argument for a positivity-improving square.** Add: "(a Jentzsch/Krein–Rutman-type argument; cf. Reed–Simon IV, §XIII.12)". The proof can stay.
- **Lemma A.4 square-root bound.** The classical estimate $\|A^{1/2}-B^{1/2}\|\le\|A-B\|^{1/2}$ (Bhatia, *Matrix Analysis*, X.1) is sharper than the $4\sqrt\delta/\pi$ proved there. Either cite it and drop the integral-representation proof, or keep the proof and add the citation.

**A7. MAJOR: Several sections open with no motivation.** This matters for AC's value of sufficient explanation.
- **§4 (l. 342).** Its opening is one sentence. Add 3–4 lines:
  > The asymptotics of the signed weights near the corners drive everything that follows: the weights are of order $m^{-4}\log m$ within bounded index distance of a corner, with signs alternating on the checkerboard. Polynomials of degree $<m$ can concentrate there, which produces the logarithmic growth of §§5–6.
- **§5 (l. 501).** It starts directly with the Fejér definition. Add the idea:
  > The factor $T_{m/2}(x)$ restricts the carrier to even (respectively odd) $x$-nodes, where the corner weights have a fixed sign. The Fejér factors localise at the corner in a window of $O(m)$ indices.

  Also split §5 into 5.1 "Carriers and the threshold" (Thm 5.1–Remark 5.4) and 5.2 "Normalized one-sided constants" (Lemma 5.5–Prop. 5.8).
- **§6.1, before Lemma 6.2.** The text never explains why the limit lives on the triangle $\mathcal T$ with measure $ab\,\mathrm da\,\mathrm db$. Add 3 lines:
  > The total-degree constraint $k+l\le m-1$ becomes $a+b\le1$ after the scaling $a=k/m$, $b=l/m$. The Legendre normalisation $(k+\tfrac12)(l+\tfrac12)\approx m^2ab$ gives the measure, and Mehler–Heine turns $\mathsf P_k(\cos(u/m))$ into $J_0(au)$.
- **§7 (l. 1233).** Add one sentence of motivation:
  > Although the Gram form diverges at $n=m-1$, the coefficient operator built from the same rule stays bounded from $C$ to $L^2$, because only $\sum|w_z|\,|p(z)|$ enters, and the logarithmic corner weights are summable against $L^2$-normalised polynomials.

  Add the An–Wu/Sloan context of A1 here as well.

---

## B. MINOR

**B1. MZ-CC citation, Prop. 2.2 (l. 274) and §1 (ll. 143–150).** MZ-CC's numbering is frozen (`correspondence-cc.md`, 2026-11-13). Cite by statement:
- "$\lambda_+(N,n)\le2-4/N+4/N^2$ [MZ-CC, Thm 3.1 and Cor. 3.2]";
- "$\lambda_-(N,N-1)\to0$ [MZ-CC, Thm 4.3; the sharp rate $\pi^4/(8\log^2N)$ is Thm 4.6]";
- "$\lambda_-(512,511)<1/4$ [MZ-CC, Prop. 8.1]".

The register's cross-paper rule asks for this.

Optional: MZ-CC's Thm 3.3 ($\lambda_+\le5/3$) would sharpen Lemma A.2's factor 4 to 25/9. This is not needed, and it would change constants that the audit checked, so leave it.

**B2. The MZ-CC title in refs.bib is wrong.** refs.bib has "…constants of Clenshaw–Curtis rules beyond half-exactness". The MZ-CC title (`paper/manuscript.tex` l. 25) is "…constants of Clenshaw–Curtis **quadrature** beyond half-exactness". Fix the bib title. Replace "Preprint in preparation" with the arXiv identifier once MZ-CC is posted.

**B3. §3 overloads $Q_m^{\mathrm P}$ and $G^{\mathrm P}_{m,n}$.** At ll. 291–301 they denote an *arbitrary* rule exact on $\mathcal P_m$ with weights $W_{jk}$. Everywhere else, including the intro's definition at l. 101, they denote the interpolatory rule. Fix: write $\widetilde Q_m$, $\widetilde G_{m,n}$ in §3, and add after Thm 3.1: "In particular this applies to $Q_m^{\mathrm P}$."

**B4. §3 opening wording (ll. 293–300).** "This assumption applies to the interpolatory rule … needs neither positivity … nor a separate existence or uniqueness theorem … Its univariate comparison object is …" is defensive and uses jargon. Replace with:
> Every such rule, in particular the interpolatory rule $Q_m^{\mathrm P}$, is compared with the Clenshaw–Curtis rule $Q_N$ of Section 2 with $N=m$; no sign condition on $W_{jk}$ is needed.

Also change l. 174, "Throughout the CC analysis", to "For the Clenshaw–Curtis rule we write".

**B5. Thm 7.1 proof (ll. 1263–1284).**
- "The absolutely convergent coefficients $t_r$ used above" refers to a symbol defined inside the proof of Thm 4.2, three sections earlier. Restate it: "$t_0=2$, $t_r=-4/(4r^2-1)$".
- $A_R$ is used at l. 1268 before its definition ":=" at l. 1274, and the two displays look like two different formulas. Put the definition first and mark the first display as an intermediate identity.
- $w^{\mathrm{CC}}_{N,j}$ (l. 1311) is new notation. Use "$w_j$ of the mesh $N$", as in Lemma 2.1.

**B6. Cor. 5.3 and the open problems: an order statement at every fixed ratio is missing.** This may be a new claim, so register it before use. The carriers of Prop. 5.6, with $a+b$ small, have degree below $\tau m$. By restriction, Thm 6.1 bounds $|\lambda^{\mathrm P}_\pm(m,n)|\le120\log R+4096$ for every $n<m$. Together these give $|\lambda^{\mathrm P}_\pm(m,\lfloor\tau m\rfloor)|\asymp\log m$ for every fixed $\tau\in(1/2,1)$.
- If the math referee confirms this, it belongs in Cor. 5.3 as an order statement.
- §9 could add the question: do $\lambda^{\mathrm P}_\pm(m,\lfloor\tau m\rfloor)/\log m$ converge for every $\tau\in(1/2,1)$, presumably to the extremes of the analogous operator on $\{a+b\le\tau\}$? State it as a question, not a conjecture.
- Not to be added without registration (BRIEF §4 rule).

**B7. Prop. 6.9 states integers and digits that carry no information.** The statement prints two 77-digit integers and 24-digit decimals (ll. 1177–1185). The following text says the enclosure "fixes no decimal digit". State "$0.01316\le\|B\|\le0.4779$ (outward rounded)" and move $n_L$, $n_U$ and the 24-place decimals to App. B.5, or to the deposit.

**B8. Thm 6.3 (l. 1019): "the exact signed Lebesgue Padua rule".** Write "the interpolatory (signed) Padua rule $Q_m^{\mathrm P}$". "Exact" is ambiguous here, given §3's arbitrary exact rules.

**B9. Result B (l. 113): "For the actual signed rule"** should read "For the interpolatory rule $Q^{\mathrm P}_m$".

**B10. λ notation is mixed.** The register fixes $\lambda^{\mathrm P}_\pm(m,n)$. §§3, 5 and 8 write $\lamin(G^\Pa_{m,n})$ and $\lamax(G^\Pa_{m,n})$; §6 writes $\lambda^\Pa_\pm$. Both are defined at l. 103, but use one form, preferably $\lambda^{\mathrm P}_\pm(m,n)$, in statements. Keep $\lamin(G)$ for the generic §2 discussion.

**B11. The weight notation drifts.**
- §3: $W_{jk}$ for arbitrary weights. This clashes with $W_N(\theta)$, the $W_x$ set of B.3, the partial isometry $W_m$ of Lemma A.4 and the bins $W_i$ of B.5.
- Lemma A.2: the CC weights are called $\alpha_j$, $\beta_k$, while $\beta$ is the kernel of $B$ (a global symbol in Prop. 6.6), $\beta_K(m)$ appears in A.3, and α, β are the fit parameters of §8.3.
- App. A.2 Step 3: $w_{kl}=(k+\frac12)(l+\frac12)/m^2$ clashes with the Padua weights $w_{jk}$.
- Fix:
  - CC weights $w^{(m)}_j$, $w^{(M)}_k$ in Lemma A.2 (register: "w_j^{CC}");
  - $\omega_{kl}$ or $\varkappa_{kl}$ in A.2 Step 3;
  - bins $\Omega_i$ in B.5;
  - $\widetilde W_{jk}$ in §3.

**B12. Other register violations, all local but avoidable.** See §D for the complete table.
- N: $N=|\mathcal Z|$ in Lemma A.4, and $N$ the squared norm in the Prop. 8.2 proof (register: "N only CC mesh index").
- B: "$A$, $B$ the distances" in the Prop. 8.1 proof, and "$A,B$ psd matrices" in the Lemma A.4 proof. The register prescribes $X$, $Y$ there.
- ϱ: $\varrho(r,s)$ in the Prop. 8.1 proof (register: ϱ is the Abel parameter only).
- ρ: $\rho_1,\rho_2$ in B.2 (register: only $\rho_{jk}$).
- $c_j$: the endpoint halfweights in the Thm 5.1 proof, l. 552 (register: ε^{(M)}).
- M: the generic "mesh denominator M" at l. 552 (register: M = m+1 only).
- $\Pi_{kl}$: the product in A.2 Step 3, which clashes with the space Π.
- u: the eigenfunction $u$ (Prop. 6.7) against the endpoints $u<v$ (Prop. 6.8), in consecutive statements.
- U, L:
  - $L$ and $U$ are the enclosure endpoints (Prop. 6.9) in the same section as $L_m$, the cube $[0,U]^4$, $U=\pi(K-1)$ and $U_-$;
  - suggested rename: $\underline r$, $\overline r$ for the enclosure endpoints.
- n as summation index: in the formal series for $\Sigma_t$ (l. 1084) and in B.1 (n is the total degree). Use $\ell$.
- I: $I_t(a;[u,v])$ and $I_K$ against the identity $I$. Use $\mathcal I_t$ or $\Phi_t$.

**B13. Two appendix numbering collisions.** "Lemma A.1" (triangular tail) and "Appendix A.1" (proof of Thm 6.1) both exist; likewise A.2, B.1, B.2. Text such as "by A.2" becomes ambiguous. Number the appendix lemmas through a separate counter (e.g. Lemma A.I or A.1′), or refer to subsections as "Appendix A, Section A.2".

**B14. §8.3 item (2) and its table (ll. 1537–1550).** "weight of the minimizer in mode 2" and "Mode 2 is the span of the second eigenvalue of the finite form $L_m$" are imprecise.
- Fix: "the squared norm of the orthogonal projection of the normalised computed minimiser onto the eigenspace of the second-lowest eigenvalue pair of $L_m$ (a doublet by Remark 6.5)".
- Also say in one sentence why the *second* doublet is the relevant one at these m. If no proved reason exists, say "we have no explanation for this", or drop the column.
- "proxies", "doublet" and "compressed branches" (l. 1567) are undefined.

**B15. Data and code availability (ll. 1609–1663).** It names repository-internal work directories, such as `topics/padua-mz-cleanup-20261105/…`, `S4_padua_fit.py` and `P1_rectangle.py`, and the "receipts". These are accurate locators. For a journal, though:
- (a) a curated `paper-sp/code/` directory, or a README in the Zenodo deposit mapping each proposition to one script and one output file, would cut this to about 8 lines;
- (b) "public repository": AC should confirm that `aacchhee/padua_research` is public at submission, or point only to the Zenodo DOI;
- (c) `\texttt{P1\_rectangle.py --N 16 --theta 256}` (l. 1645) prints a non-typewriter underscore. Use `\path{}` or `\verb` (see TYPO C3).

**B16. The Theorem 4.2 statement has a remark inside it (ll. 406–407).** "The indices in this majorant are distances from the corner (1,1); the fixed-index limit is not asserted uniformly across the grid." The second clause belongs after the theorem. The first is not quite right: $j,k$ run over the whole grid, and for $j$ near $m$ the "distance from (1,1)" reading is literal but not the natural one. Say "Here $j,k$ are the raw indices, so the bound is weakest near the corners other than $(1,1)$." The math referee should confirm that this is intended.

**B17. Prop. 5.8 (ceiling) weighed against its use.** It bounds only one scalar trial family and is used nowhere else. Demote it to a remark after Prop. 5.7. That saves about 0.4 page and removes the long negative list (A4).

**B18. Keywords and MSC.** Add MSC 47B38 or 47A75 (operator spectra, corner operator) and 65G20 (computer-assisted proofs, interval arithmetic). Optional.

**B19. Sec. 2 (l. 160): "Let $Q(f)=\sum_jw_jf(x_j)$ approximate a finite positive measure μ".** "μ" later becomes $\mathrm d\mu=ab\,\mathrm da\,\mathrm db$ (§6.2, App. B), and "ν" is both a measure (§7 proof) and $\nu_\pm(m)$ (Thm 6.1). Rename the §6.2 measure to $\mathrm d\mathfrak m$ or $\mathrm d\mu_{\mathcal T}$, and the §7 measure to $\mathrm d\nu_{\mathrm{Ch}}$.

**B20. Remark 6.5 (l. 1065): "strip contributions".** This is jargon from the proof of Thm 4.2. Say "the two terms $\cos(2R\theta_j)$ and $\cos(2R\phi_k)$ of (L-m)".

---

## C. TYPO

- **C1.** The label `sec:data` (l. 1609) sits on an unnumbered section and resolves to "9". It is unused, so delete it to prevent a wrong future reference.
- **C2.** l. 1084: "Formally, $\Sigma_t(a,a')=\sum_{n\ge0}$…" should use index $\ell$ (see B12).
- **C3.** l. 1645: `\texttt{P1\_rectangle.py …}` should be `\path{P1_rectangle.py} --N 16 --theta 256`.
- **C4.** l. 1549: "the span of the second eigenvalue" should read "the eigenspace of the second eigenvalue" (or see B14).
- **C5.** l. 1499: the proof heading (see A4).
- **C6.** bib `ASV27`: the author field "An, C." beside full given names for the coauthors. The record has "C. An" only; use "An, Congpei" if AC confirms, or abbreviate all three.

---

## D. Notation register conformance (`notation-sp.md`)

### D1. Register entries not applied in the text

| Register rule | Text | Location |
|---|---|---|
| 𝒥_t for rectangle integrals | $J_t(U,U')$ | ll. 1140, 1167, 2416, 2465 (A2) |
| τ ratio only | $\tau=\min(t,\pi-t)$ | Lemma A.1 statement l. 1693; (S-remainder) |
| ϱ Abel parameter only | $\varrho(r,s)=Q_m(T_rT_s)$ | Prop. 8.1 proof ll. 1441–1448 |
| ρ only ρ_{jk} | $\rho_1,\rho_2$ | B.2 l. 2294 |
| N CC index only | $N=|\mathcal Z|$; $N$ squared norm | Lemma A.4 l. 2022; Prop. 8.2 proof l. 1506 |
| X, Y replace A, B (PD-T536 §5) | "psd matrices $A,B$" | Lemma A.4 proof l. 2060 |
| B never for other uses | "$B$ the distance from $s$…"; $B_t$ | Prop. 8.1 proof ll. 1443–1462 |
| M = m+1 only | generic "mesh denominator $M$" | l. 552 |
| ε^{(N)} replaces all endpoint factors | "$c_j$ endpoint halfweights" | l. 552 |
| w_j^{CC} for CC weights | $w^{\CC}_{N,j}$; $\alpha_j,\beta_k$ | ll. 1311–1315; Lemma A.2 |
| λ^P_±(m,n) | $\lamin(G^\Pa_{m,n})$ in §§3, 5, 8 | B10 |
| Π_n listed as total-degree space | text: $\mathcal P_n$ bivariate, Π_n univariate (undefined) | register entry wrong; A3 |
| η listed among locally reusable letters | η is the global defect (eq:eta), and η_τ appears in Cor. 5.3 | register entry wrong |

### D2. Clashes not in the register

New global symbols that the register should list, with collisions:

| Symbol | Meanings | Severity |
|---|---|---|
| $T_R$ / $T_a$ | tail sum (App. A global) / Chebyshev | MAJOR (A2) |
| $E_K(m)$ / $E_k(f)$ | finite-comparison error / best approximation | MAJOR (A2) |
| $d_m$ / $d_j$ / $d$ | density / distance / $\dim\mathcal P_n$ (§7) / integer $d_t$ | MAJOR (A2) |
| $h_a$ / $h(x)$ / $h_r$ / $h_i$ / $h$ | moments / $x^2\log|x|$ / Thm 5.1 proof / certificate weights (Prop. 6.8 statement) / B.4 test function | MAJOR (A2) for the first two |
| $g$ | $(\sin(u/2)/(u/2))^4$ (Lemma 5.5 statement, global in §5) / $\pi\sqrt{1-x^2}$ (Thm 7.1 proof) / $g(\theta)$ (B.5) | MINOR |
| $W$ | $W_N(\theta)$ / $W_{jk}$ / $W_x$ / $W_m$ / $W_i$ | MINOR (B11) |
| $w$ | Padua and CC weights / $w_{kl}$ (A.2) | MINOR (B11) |
| $\beta$, $\alpha$ | kernel of B / CC weights $\beta_k$ / $\beta_K(m)$ / fit slope; $\alpha=\pi-4/3$ / $\alpha_j$ / fit intercept / angle $\alpha$ (B.1) | MINOR |
| $U$, $L$ | enclosure endpoints / rectangles $U\times V$ / $U_-$ / $\pi(K-1)$ / cube; $L_m$ / $L=r+1$ / $L=\lfloor R/2\rfloor$ / cardinal $L_z$ | MINOR (B12) |
| $u$ | eigenfunction / interval endpoint / integration variable | MINOR |
| $Q$ | rule / bracket matrix (Prop. 8.1 proof) / $Q_i$ (Prop. 6.8 statement) | MINOR |
| $H$ | $H_{m,n}$ / matrix $H$ / $H_q(u)$ / harmonic $H_L$ (undefined) | MINOR |
| $P$ | basis $P_i$ / Legendre $\mathsf P_k$ / $P_{U\times V}$ / Poisson $P_\varrho$ | MINOR |
| $F$ | Fejér $F_r$ / index set $F$ (Prop. 6.8 statement) / $F(a,b)$ / $F_a$ | MINOR |
| $I$ | identity / $I_t$ / $I_K$ | MINOR |
| $\sigma$ | spectrum / $\min(s,\pi-s)$ / $\sigma_s$ / $\sigma=s^2$ | MINOR |
| $\mu$, $\nu$ | §2 measure / $ab\,\mathrm da\,\mathrm db$; Chebyshev measure / $\nu_\pm(m)$ | MINOR (B19) |
| $c$ | $c_\pm$ / $c_a\in\{1,2\}$ (§4 global) / $c_j$ / $c_t$ / $c_l$ / corner $c$ / $c\in[-1,1]$ | MINOR; register says "$c_\pm$ only these", which $c_a$ violates in spirit |
| $\kappa$ | $\kappa^{\rm car}_\pm$, $\kappa_{\rm new}$, $\kappa_-(a,b)$ / $\kappa=1/2+1/\pi$ (Thm 7.1 proof) | MINOR; rename the last to $k_\nu$ |
| $\Pi_{kl}$ / $\Pi_n$ | product / space | MINOR |
| $r$ | $\|B\|$ (global in §6.2) / $\lfloor am\rfloor$ (§5) / summation index | acceptable; the register allows local r |

Not yet in the register, and worth adding:
- $\mathcal P_n$, $\Pi_n$, $W_N$, $c_a$, $h_a$, $t_a$, $S_R$, $V_R$, $F_r$, $D_r$, $g$, $J_\pm$, $\kappa_-(a,b)$, $U_-$, $J_{\rm end}$;
- $L_m$, $\nu_\pm$, $\mathcal K_{m-1}$, $\mathcal K_\infty$, $\mathcal T$, $\mathcal H$, $\psi_{jk}$, $\Sigma_t$, $\beta$, $I_t$, $P_{U\times V}$, $\chi_t$;
- $C_{\mathrm P}$, $H_{m,n}$, $E_k(f)$, $E_K(m)$, $N_K$, $I_K$, $C_U$, $\gamma_m$, $q_m$, $G_m$, $X_m$, $\omega_a$, $q_{a,a'}$, $\Omega$, $Z$.

### D3. Forward uses and undefined symbols

| Symbol / term | First use | Status |
|---|---|---|
| $\mathcal P_n$ | l. 62 | defined only at l. 282 (A3) |
| $\Pi_N$ | l. 180 | never defined (A3) |
| CC | l. 174 | never expanded (A3) |
| strong MZ constant | l. 118 | never defined (A3) |
| carrier, signed energy | §5 title, l. 611 | never defined (A3) |
| $H_q$ (harmonic) | ll. 436, 1724 | undefined (A3) |
| $A_R$ | l. 1268 | defined at l. 1274 (B5) |
| $t_r$ in §7 | l. 1264 | defined only in the proof of Thm 4.2 (B5) |
| $w^{\CC}_{N,j}$ | l. 1311 | not introduced (B5) |
| "mode 2", "doublet", "proxy", "compressed branches" | §8.3 | B14 |
| "packet", "thin-corner limit", "strip contributions" | ll. 492, 789, 795, 1065 | A4, B20 |
| Lemma A.4 cited in Remark 6.5 | l. 1061 | forward reference into the appendix; acceptable |

---

## E. Literature: per-citation scope check (MZ-SP)

Coverage is quoted from the LIT record and checked against the bib `coverage` field.

| # | Line | Key (LIT) | Claim in text | Record coverage | Verdict |
|---|---|---|---|---|---|
| 1 | 68 | Wu26 (LIT-489) | Wu's theorem, for positive-weight rules, needs a defect below coercivity/continuity | complete; Thm 3.1 p. 3: η < α/β, positive weights | **OK** |
| 2 | 80 | BCDMVX06 (LIT-312) | Lagrange interpolation at Padua points analysed; Thm 2 gives the fundamental polynomials by a corrected-kernel formula | journal pp. 15–25 read in full (2026-11-05); Thm 2 pp. 20–21 | **OK** |
| 3 | 82 | Xu96 (LIT-314) | interpolation at parity-separated Chebyshev–Lobatto points "of this type" | journal read in full; §2.2–2.3 parity-separated CL nodes, corrected kernel | **OK**. Optional: "(Xu points, in a different polynomial space)" |
| 4 | 85 | SVZ08 (LIT-427) | the weights of $Q^{\mathrm P}_m$ are formula (33); exact on $\mathcal P_m$ | journal pp. 409–421 read; (33) p. 419, (36) p. 420, exactness n | **OK**. Optional: "formulas (33) and (36)" ((36) is the stated form at exactness n) |
| 5 | 87 | SVZ08, p. 421 | negative weights noted to be few and small | p. 421 read: "few and small" | **OK** |
| 6 | 89 | KLP18 (LIT-488) | "the two-sided $L^p$ MZ inequalities of KLP18 at Padua-type nodes are for positive weights in the Chebyshev-weighted norm, with unspecified constants" | arXiv v1 pp. 1–12 read; journal labels coincide. Lemma 5.1: (5.1) for all p and (5.2) for 1<p<∞ are **quoted from Erb 2016**; only p=1 is proved there. The space is the anisotropic $\Pi^L_{m,n}$ | **NEEDS-SOFTENING.** Replacement: "the two-sided $L^p$ MZ inequalities at Lissajous–Chebyshev nodes, which include the Padua points, recorded by Kolomoitsev, Lomako and Prestin [KLP18, Lemma 5.1] (for $1<p<\infty$ taken from Erb), are for positive weights in the Chebyshev-weighted norm on an anisotropic interpolation space, with unspecified constants" |
| 7 | 91 | CDMV07 (LIT-428) | hyperinterpolation on the square with positive Chebyshev-measure weights at Xu points | AC-supplied journal read in full (2026-11-05); §2 Xu/MPX points, product Chebyshev measure, positive weights | **OK** |
| 8 | 93–97 | ASV27 (LIT-045) | finite computations for "a Padua-based cubature rule for Lebesgue measure", ADE m ≤ 20, give η<1 up to n=m−1; CC behaviour beyond half-exactness "to their knowledge, not known theoretically" | published: complete keyword screen, §§1–2, 3.1, 3.6 read; "Padua: η<1 up to n=m−1 observed" (no page locator recorded); "not known" p. 738; ADE m=1…20 from the arXiv reading | **OK**, with a named gap: the record gives no locator for the Padua experiment and does not identify ASV's Padua rule with $Q^{\mathrm P}_m$. AC has the PDF; add the page (D in §G) |
| 9 | 274 (and 147) | MZ-CC | three CC spectral inputs | companion; frozen numbers available | **OK**; add statement numbers (B1); fix the bib title (B2) |
| 10 | 360–362 | SVZ08 (33); BCDMVX06 Thm 2 | the density is (33) up to orientation and normalisation; the cardinal kernel is BCDMVX Thm 2 | as #2 and #4 | **OK** |
| 11 | 1429–1431 | ASV27 | "consistent with the finite observation … that the Padua-based rule has η<1 up to n=m−1 for m≤20, and extend it at the six listed degrees" | as #8 | **NEEDS-SOFTENING.** (i) m=10, 20 lie inside ASV's range, so "extend it at the six listed degrees" is wrong. (ii) The record does not show that ASV's Padua rule is $Q^{\mathrm P}_m$. Replacement: "An, Sommariva and Vianello [ASV27] report η<1 up to n=m−1 for a Padua-based cubature rule for Lebesgue measure with degree of exactness m≤20. If that rule is the interpolatory rule studied here, the brackets certify their observation at m=10, 20 and extend it to m=30, 40, 60, 80." Drop the conditional once AC confirms the rule from the PDF |
| 12 | 1535 | SVZ08 | negative weights few and small already noted | p. 421 | **OK** |

**Summary:** 12 citation occurrences across 9 keys. 10 are OK (one with a named locator gap, #8). 2 NEED SOFTENING (#6 KLP18, #11 ASV27). None is UNSUPPORTED.

## F. Bibliographic data against the records

| Key | Field | refs.bib | Record | Action |
|---|---|---|---|---|
| MZ-CC | title | "…Clenshaw–Curtis rules beyond half-exactness" | MZ-CC manuscript: "…Clenshaw–Curtis quadrature beyond half-exactness" | fix (B2) |
| MZ-CC | author/note | "[Author names to be inserted]", "Preprint in preparation" | — | placeholder (§H) |
| BCDMVX06 | doi | 10.1016/j.jat.2006.03.008 | the record gives only the preprint URL | resolver-check the DOI ([doi.org/10.1016/j.jat.2006.03.008](https://doi.org/10.1016/j.jat.2006.03.008)) and add it to the record |
| Xu96 | doi | 10.1006/jath.1996.0102 | record: author PDF URL only; LOG says "not resolver-checked" | AC: check [doi.org/10.1006/jath.1996.0102](https://doi.org/10.1006/jath.1996.0102) |
| KLP18 | coverage | "arXiv v1 pp. 1–12 read in full; journal theorem and lemma numbering coincides, journal body not otherwise read" | record: arXiv pp. 1–12, 16, 19; journal labels coincide (2026-11-05); "wording not diffed" | matches |
| SVZ08 | all fields | match (vol. 49, no. 1–4, pp. 409–427, doi) | — | OK |
| CDMV07 | all fields | match | — | OK |
| ASV27 | year/vol/pp/doi | 2027, 252, 733–745, 10.1016/j.matcom.2026.10.001 | match | author style only (C6) |
| Wu26 | all fields | match (AML 182, 110033) | — | OK |

## G. Missing essential Padua literature, and unread items for AC

**Read records the text should cite, at the recorded scope:**
1. **An–Wu 2022, BIT 62, 1899–1919 (LIT-046).** Hyperinterpolation with relaxed quadrature exactness, positive weights, η<1. It is the direct context of §7 (A1). [doi:10.1007/s10543-022-00935-x](https://doi.org/10.1007/s10543-022-00935-x).
2. **An–Ran–Wu 2025 survey, DRNA 18(1) 135–145 (LIT-387).** Read: arXiv §2.3 and §3.1. Context for §7, with the scope caveat in A1. [doi:10.25430/pupj-DRNA-2025-1-11](https://doi.org/10.25430/pupj-DRNA-2025-1-11).
3. **Bos–De Marchi–Vianello–Xu 2007, Numer. Math. 108, 43–57 (LIT-313).**
   - Read: arXiv excerpts pp. 1–4, Thm 2.3, Prop. 3.1, Thm 3.2, Prop. 3.4. This covers "ideal-theoretic description", the corrected kernel, and positive cubature of degree 2n−1.
   - Do not cite it for the Lebesgue constant (not read).
   - [arXiv:math/0604604](https://arxiv.org/abs/math/0604604). The journal DOI is not verified (probably 10.1007/s00211-007-0112-z).
4. **Caliari–De Marchi–Vianello 2008, JCAM 221, 284–292 (LIT-330).** Read: preprint §2 (four families). Cite it for "four families related by symmetries". [doi:10.1016/j.cam.2007.10.027](https://doi.org/10.1016/j.cam.2007.10.027).

**Unread items the text needs.** AC should read these, or approve citing them at metadata scope:
- **Caliari–De Marchi–Vianello 2005**, *Bivariate polynomial interpolation on the square at new nodal sets*, Appl. Math. Comput. 165 (2005) 261–274. This is the origin of the Padua points. There is no record. DOI [10.1016/j.amc.2004.07.001](https://doi.org/10.1016/j.amc.2004.07.001) (checked on [MaRDI](https://portal.mardi4nfdi.de/wiki/Publication:1780531)). Free author PDF: [CDMV05.pdf](https://profs.scienze.univr.it/caliari/pdf/CDMV05.pdf).
- **Sloan 1995**, *Polynomial interpolation and hyperinterpolation over general regions*, J. Approx. Theory 83 (1995) 238–254. It defines hyperinterpolation; there is no record. DOI [10.1006/jath.1995.1119](https://doi.org/10.1006/jath.1995.1119) (checked on [MaRDI](https://portal.mardi4nfdi.de/wiki/Publication:1904377)).
- **The Lebesgue-constant statement for Padua points** (O(log² m)). BCDMVX06 Thm 3 is read (LIT-312: order bound C(log n)² on the square), so A1's sentence can cite BCDMVX06 Thm 3. No further reading is needed unless the text names the constant.
- **Caliari–De Marchi–Sommariva–Vianello 2011, Padua2DM**, Numer. Algorithms 56, 45–60. The record LIT-368 is secondary and UNVERIFIED. It is needed only if the text mentions the software or identifies ASV's rule. Free preprint: [preCDMSV09.pdf](https://profs.scienze.univr.it/caliari/pdf/preCDMSV09.pdf). The DOI is not verified (probably 10.1007/s11075-010-9373-1).
- **Erb 2016**, *Bivariate Lagrange interpolation at the node points of Lissajous curves – the degenerate case*, Appl. Math. Comput. 289, 409–425. It is the source of KLP's L^p MZ inequalities. Cite it only if #6 names it. [arXiv:1503.00895](https://arxiv.org/abs/1503.00895); the DOI is not verified.
- **ASV27 published version, the Padua experiment section.** Needed for the page locator, and to check which Padua rule they use (#8, #11). AC has the PDF (`1-s2.0-S0378475426004416-main.pdf`). [doi:10.1016/j.matcom.2026.10.001](https://doi.org/10.1016/j.matcom.2026.10.001).
- **Mehler–Heine and the classical Legendre/Bessel facts** (A6). These are standard references, not LIT items: Szegő, *Orthogonal Polynomials*, Thm 8.1.1, and [DLMF §18.11](https://dlmf.nist.gov/18.11), [DLMF §10.9](https://dlmf.nist.gov/10.9).
- **Optional:** De Marchi 2022 survey (LIT-326, excerpts only), [landing page](https://dergipark.org.tr/en/pub/cma/article/1070020). Clenshaw–Curtis 1960, Numer. Math. 2, 197–205: no record; not needed, since MZ-CC carries the CC history.

## H. Tables, captions, placeholders

- **Tables.** There are three, all uncaptioned and embedded in statements or list items: Prop. 8.1, Prop. 8.2 and §8.3(2). That is acceptable for JAT. The §8.3 table needs a precise column definition (B14).
- **Figures.** There are none. Optional: one figure of $m^4w_{jk}/\log m$ near the corner (1,1) for a moderate m. It would show the checkerboard sign pattern behind §§4–6 and should be labelled as a computation.
- **Visible placeholders** to resolve before submission (AC-reserved items marked †):
  - "[Author names to be inserted]" in the front matter (l. 32) and in the bib entry MZ-CC†;
  - "[to be fixed at submission]" (commit) and "[Zenodo DOI to be added]" (l. 1614)†;
  - "DOI to be added" in the text after Prop. 8.2 (l. 1497)†;
  - MZ-CC "Preprint in preparation" (replace with arXiv id);
  - `\date{13 November 2026}` (l. 22) in the footer.
- **Missing elsarticle front-matter and back-matter items, all AC-reserved, not to be edited by agents:** affiliations (`\address`), corresponding author and e-mail, CRediT statement, declaration of competing interest, declaration of generative-AI use, acknowledgements and funding. JAT's guide should be checked at preparation for highlights.

## I. Structure and flow for a JAT reader: where to cut, where to add

**Flow.** The order Intro → CC recap → compression → weights → carriers and threshold → corner operator → uniform norm → finite results → open problems follows Results A–D and is sound. The appendices hold the long proofs, which is right for JAT. Three flow problems:
1. **§5 mixes two topics.** The threshold (Thm 5.1–Remark 5.4) is one. The normalized constants (Lemma 5.5–Prop. 5.8) are the other, and they matter only for the lower bounds of Cor. 6.10 and the signs in Thm 6.3. Split §5 into subsections (A7). Optionally move Props. 5.7–5.8 to §6.2 next to Cor. 6.10, keeping Prop. 5.6 in §5 because Thm 6.3 uses $\kappa^{\rm car}_+$ for $c_+>0$.
2. **§6.1 states Lemma 6.2 without saying why a triangle and $ab\,\mathrm da\,\mathrm db$ appear** (A7). It also does not name Mehler–Heine (A6).
3. **§7 starts abruptly** after the corner analysis (A7).

**Possible cuts, about 3–4 preprint pages, none losing explanation:**

| Item | Saving | Note |
|---|---|---|
| App. A.2 Step 1, replaced by statements with DLMF/Szegő citations | ~0.8 p | AC's choice: the criterion allows "stated in the form used" |
| §8.3 secant paragraph and the mode column, unless explained (B14) | ~0.4 p | measured, used in no proof |
| Data statement condensed through a deposit README (B15) | ~0.6 p | |
| Prop. 6.9: integers and 24-digit decimals moved to B.5 or the deposit (B7) | ~0.2 p | |
| Prop. 5.8 demoted to a remark; disclaimer sentences shortened (A4, B17) | ~0.6 p | |
| Lemma A.4: the square-root bound cited instead of proved (A6) | ~0.2 p | optional |

**Additions, about 1.5–2 pages:**

| Item | Size |
|---|---|
| Intro motivation and Padua literature paragraph (A1) | ~0.5 p |
| Notation table at the end of §2 (symbols used across sections, from D2) | ~0.5 p |
| Openings of §§4, 5, 7 and the §6.1 heuristic (A7) | ~0.6 p |
| Definitions of the strong MZ constant, carrier and signed energy (A3) | ~0.1 p |
| Optional fixed-ratio order statement and question (B6), subject to registration | ~0.2 p |

**Keep as is:**
- the CC weight lemma with proof (Lemma 2.1);
- all appendix proofs except the classical facts above;
- the computer-assisted reduction proofs (Props. 8.1 and 8.2, App. B.5);
- the scope sentences inside statements (Prop. 5.6, Thm 6.3, Prop. 8.1).

---

## Nothing for memory

I learned nothing new about AC's preferences in this task.
