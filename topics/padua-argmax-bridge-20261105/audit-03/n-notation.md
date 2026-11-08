# Notation register: Padua argmax-bridge paper and companion

Prepared at AC's request during the substantive Claude audit (handoff 28) as a
starting point for Codex's notation repair. Editor: Claude (Opus 5.5, xhigh),
read-only on the repository. Branch `codex/padua-argmax-bridge-20261105`, head
`f366535e1fa4ede566cb83bdc554220c12b307cf` (rules read there); the `paper/` and
`companion-paper/` trees are unchanged at the later head `2bb805cf` [E: git diff]. Texts: the
48-page paper `topics/padua-argmax-bridge-20261105/paper/` and the 162-page
companion `…/companion-paper/`; comparison-unified.tex is input inside
localization-unified.tex and forms Sections 4.1–4.2.

- **Committed scripts and reproduction:** the register's scripts are in `audit-03/code/n/`
(python3 standard library only). From the repository root,
`python3 topics/padua-argmax-bridge-20261105/audit-03/code/n/notation_scan.py --repo . --out OUTDIR`
reproduces the baseline counts in `audit-03/code/n/baseline-summary.txt` (the orchestrator re-ran it
from this location: exit 0, 1.1 CPU-s, same counts). The generated tables (`definitions-*.tsv`,
`symbols-*.tsv`, flags) are not committed; they are regenerable.
- **Evidence labels:** [D] read at the cited source line; [E] established by
  running the scripts of §5 on the head sources; [I] editorial inference or
  proposal.
- **Status column** (AC's classes, written without brackets): **A** two
  meanings live in one subsection or proof; **B** different sections, but the
  reader carries the earlier meaning; **C** introduced only by the companion's
  added prose; **D** the symbol is in the paper's numbered display blocks, so a
  rename must be made in both texts; **glyph** one object, two glyphs. (D thus
  has two roles in this file too; the bracket tells them apart.)
- **Locations:** `P file:line (p.N); C line (p.N)` gives the paper line and
  printed page, then the companion line in the same-named file and its page;
  `C only` marks companion text. File names drop `-unified.tex`.

## 1. Method and coverage

1. **Extraction [E].** `notation_scan.py` (§5) reads each text in typeset
   order (following `\input`), strips comments and finds every math region
   (`$…$`, `\(…\)`, `\[…\]`, and equation, align, gather, multline, flalign,
   alignat, eqnarray, starred or not). It records every Latin and Greek letter,
   `\ell` and decorated symbol (`\bar`, `\overline`, `\hat`, `\widehat`,
   `\tilde`, `\widetilde`, `\mathcal`, `\mathsf`, `\mathfrak`, `\mathbb`,
   `\mathbf`, `\boldsymbol`, `\dot`, one-letter `\mathrm`) with its subscript
   and decorative superscript (`*`, `±`, `\phi`, `(M)`, `\sharp`). It drops
   `\text`, `\hbox`, `\operatorname`, `\rm` words, labels, references and
   differentials (`dt`, `\frac{d}{ds}`, `df'`). Each occurrence carries file,
   line, unit (subsection), printed page and equation number.
2. **Definition sites [E], heuristic.** A candidate is a token followed by
   `:=` or `\coloneqq`, preceded by `=:`, or opening a clause (after `,`, `;`,
   `\quad`, `&`, `\\`) followed by `=` or `&=` in a sentence with a trigger
   word (put, let, write, define, set, denote, introduce, take, fix, call,
   where, with, here, recall, throughout, hereafter, once, use, retain, keep),
   or an inline token followed by *denotes* or *be* (or *is/are* after
   let/where/here). It finds 367 sites in the paper and 578 in the companion;
   it misses prose-only definitions and admits restatements.
3. **Pages [E].** Both PDFs were rebuilt into scratch with `-synctex=1` (48
   and 162 pages, as in the reference build); a line gets the page holding most
   of its glyph and math records. This matches the auxiliary label pages for
   111 of 113 labels in each text. The exceptions: align blocks numbered on the
   page after they begin ((53) paper, (40) companion); a display opening at a
   page break ((92) companion); Lemma 2.1, where the auxiliary page is the
   theorem-head quirk and pdftotext agrees with synctex (p.5). At a page break a
   cited page can be one less than the printed one.
4. **Companion lines [E].** Paper lines are mapped by `difflib` on the
   same-named file; where the companion rewrote a line, the nearest companion
   line with the same TeX needle is used.
5. **Hand verification [D].** I read the paper's six section files in full
   (2932 lines) and every companion seed location in the brief. Each cited line
   and its companion counterpart was checked by script to contain a stated TeX
   needle (all 229 register rows, no failure); all 92 equation numbers match
   the auxiliary file. Meanings, live ranges and classes are my reading.
6. **Coverage limits.** Live ranges are by subsection. Companion-only meanings
   are listed where they clash with a symbol used elsewhere, not every local
   abbreviation. Minor overlaps not tabulated: $X$ (P comparison:289, :682,
   :738); $\lambda_n$ against $\lambda_0$ (:206); $i$ as imaginary unit
   (corner:26) and index ($S_i$, $B_i^n$); the companion's radius $\rho$ in
   $\psi_B$ (C only preliminaries:52).

**Count.** 61 base symbols carry two or more meanings within the paper, within
the companion, or between them (32 grouped entries below; minor ones in item 6).

## 2. Symbol register

Rank is by severity: same-proof collisions (A), then numbered-block
collisions (D), then carry-over (B), then companion-only (C). Numbered formulas
are the paper equations containing that meaning, computed per token and live
range [E]; "–" means companion-only.

| # | Symbol | Meaning | Defined at (paper / companion, printed page) | Live range | Paper numbered formulas | Status |
|---|---|---|---|---|---|---|
| 1 | $\varepsilon,\epsilon$ | endpoint weights $\epsilon_j$ (Sec. 2) $=\varepsilon_j$ (Sec. 3): same object, two glyphs | P preliminaries:17 (p.4); C 92 (p.11)<br>P corner:11 (p.6); C 30 (p.20) | §2–§3 | 8, 13 | glyph |
|  |  | cutoff in the finite parts $H(w)$, $C_\infty$ | P comparison:106 (p.15); C 362 (p.55) | 4.1 | 34, 38 | A (4.1) |
|  |  | coefficient displacement bound | P comparison:266 (p.18); C 800 (p.61)<br>P comparison:828 (p.26); C 2278 (p.84) | 4.1 (proof of (39)); 4.2 | 64 | A (4.1, 4.2) |
|  |  | $\epsilon=\min(t,\pi-t)$ (separation) | P comparison:378 (p.19); C 1138 (p.66) | 4.1 (proof of L. 4.3) |  | A (4.1) |
|  |  | $\epsilon=3\pi/(2m)$ cutoff of $\ell$; written $\varepsilon$ in 4.5 | P comparison:558 (p.21); C 1531 (p.72)<br>P localization:373 (p.38); C 1310 (p.124) | 4.2, 4.5 | 53 | A (4.2), D, glyph |
|  |  | $\epsilon_n=\log(m/n)$; $\epsilon=h/2$ with a second $\ell=-\log\sin\epsilon$ | P comparison:656 (p.23); C 1699 (p.74)<br>P comparison:1330 (p.33); C 3835 (p.108) | 4.2 |  | A (4.2: two $\ell$) |
|  |  | sign vectors $\varepsilon_\ell$, $\varepsilon_{rs}$, $f_\varepsilon$ | P certification:9 (p.42); C 65 (p.134)<br>P certification:116 (p.43); C 705 (p.145) | §5 |  | B |
| 2 | $T$ | Chebyshev polynomial $T_r$ | P preliminaries:14 (p.4); C 89 (p.11) | global (§2, §5) | 6 | D |
|  |  | angle $T=(v-u)/2$ (with $S$); $T_t=2a\cot(t/2)$ | P corner:28 (p.6); C 95 (p.21)<br>P comparison:289 (p.18); C 858 (p.62) | 3.1; 4.1 |  | B |
|  |  | row sum $T_{n,r}$ | P corner:64 (p.7); C 235 (p.23) | 3.1 | 12 | D |
|  |  | quadratic-log model loss $T=(4L^2-3L)/\pi^2$ | P comparison:536 (p.21); C 1492 (p.71) | 4.2–4.6 | 52, 75, 83 | A (4.2), D |
|  |  | half-line defect $T_0$, $T_{0,r}$ | P comparison:730 (p.24); C 1994 (p.79)<br>P comparison:738 (p.25); C 2002 (p.79) | 4.2 | 62, 63 | A (4.2), D |
|  |  | outer increment $T_{\rm out}$ | P comparison:1274 (p.32); C 3639 (p.105) | 4.2 | 69 | A (4.2), D |
|  |  | $\mathcal T_c=4-2c+4\log c$; triangle $\mathcal T$ | P localization:200 (p.36); C 779 (p.117)<br>P certification:112 (p.43); C 645 (p.144) | 4.3; §5 | 73 | B, D |
|  |  | companion: $T(t)=\sin(\pi t)/(\pi t)$; $T_R$; $T=2\tan(e/2)$; trig. polynomial $T$ | C only comparison:453 (p.57)<br>C only comparison:2109 (p.81)<br>C only comparison:2975 (p.95)<br>C only certification:743 (p.146) | 4.1; 4.2; 4.2; 5.2 | – | C (A in 4.2) |
| 3 | $H,\mathcal H$ | harmonic numbers $H_k$, $H_{m-1}$, $H_n$; shifted $H_j(q)=\psi(j+q)-\psi(q)$ | P corner:140 (p.8); C 500 (p.28)<br>P comparison:5 (p.14); C 29 (p.51)<br>P comparison:766 (p.25); C 2085 (p.81) | 3.2–3.3; 4.1–4.2 |  | B |
|  |  | $\mathcal H_m$ harmonic row aggregate | P corner:76 (p.7); C 250 (p.23) | 3.1–3.3 | 11, 12, 17, 21 | D |
|  |  | $H=1+L=1+\log n$ | P comparison:4 (p.14); C 28 (p.51) | 4.1–4.6 | 52, 53, 68 | A (4.1), D |
|  |  | finite part $H(w)$, $H_0=H(0)$ | P comparison:106 (p.15); C 362 (p.55)<br>P comparison:110 (p.15); C 366 (p.55) | 4.1, 4.4 | 34, 40, 43, 46, 49 | A (4.1), D |
|  |  | $\mathcal H(L,v)=A(v)L+\mathcal B(v)$ | P comparison:238 (p.17); C 719 (p.60) | 4.1–4.2 |  | A (4.2 with $\mathcal H_j$) |
|  |  | $\mathcal H_j=h_j(t)+h_j(1-t)$, $\mathcal H_2,\mathcal H_n$ | P comparison:654 (p.23); C 1697 (p.74) | 4.2 |  | A (4.2) |
|  |  | periodic primitive values $H_{rs}$ | P localization:37 (p.13); C 128 (p.48) | §4 pre., 4.3, 5.2 | 26, 28 | D |
|  |  | $H_h=(1+\cos v)/(2K)$ | P comparison:944 (p.28); C 2620 (p.89) | 4.2 |  | A (4.2) |
|  |  | companion: $H_n^*$; $H(g)=A_g(1-d/g)$ with $d=\pi/L$ | C only comparison:1902 (p.78)<br>C only localization:676 (p.116) | 4.2; 4.3 | – | C |
| 4 | $C,\mathcal C$ | generic finite constant (Thm 1.2, L. 3.1, (20)); $C=-1+C_H+C_B$ then $C=\kappa$ | P introduction:131 (p.3); C 363 (p.7)<br>P corner:439 (p.13); C 1722 (p.45) | §1, §3 | 20 | B |
|  |  | named constants $C_H,C_B,C_K,C_M$ | P corner:275 (p.10); C 1080 (p.37)<br>P corner:372 (p.12); C 1478 (p.42) | 3.3 | 17, 18 | D |
|  |  | real coefficients $C,D$ in $I(C,D,e)$, $g(C,D;t)$ | P comparison:16 (p.14); C 59 (p.51) | 4.1–4.2 | 29 | A (4.1), D |
|  |  | row coefficient $C(v)$ | P comparison:231 (p.17); C 712 (p.60) | 4.1–4.2 | 37 | A (4.1), D |
|  |  | $\mathcal C(t)$ reciprocal pair, $C_0=\mathcal C(1/2)$ | P comparison:80 (p.15); C 312 (p.55) | 4.1–4.2 | 32, 38, 44, 61 | D |
|  |  | model constants $C_\infty,C_*$; $C_2$; $C_4$; $C_{E,\phi},\overline C_E,C_{6,\phi},C_B^\phi$ | P comparison:249 (p.17); C 730 (p.60)<br>P comparison:543 (p.21); C 1499 (p.71) | 4.1–4.6 | $C_\infty,C_*$: 38, 40, 41, 43, 47; $C_4$: 52, 58, 75; $C_{E,\phi},C_{6,\phi},C_B^\phi,\overline C_E$: 53, 54, 55, 56, 65 | D |
|  |  | $\mathcal C_s=I_s(\phi,z)-aI_s(0,z)-\dots$ | P comparison:1271 (p.32); C 3636 (p.105) | 4.2 |  | A (4.2 with $\mathcal C(t)$) |
|  |  | local $C$: $C=a_r-r/2$; $C=1+8a_0m/(3\pi)$ (with $C_b,C_s,C_l,C_{B,b}$); $C=\Lambda_c(n)$ | P localization:211 (p.36); C 841 (p.118)<br>P localization:374 (p.38); C 1311 (p.124)<br>P certification:64 (p.42); C 310 (p.138) | 4.3; 4.5; 5.1 |  | B |
| 5 | $D$ | Dirichlet-type diamond kernel $D_n(u,v)$ | P corner:26 (p.6); C 78 (p.20) | 3.1 |  | B |
|  |  | digamma row $D_{m,r}$ | P corner:75 (p.7); C 249 (p.23) | 3.1–3.3 | 11, 19, 20 | D |
|  |  | coefficient $D$ in $I(C,D,e)$; row coefficient $D(v)$; $D_0$ | P comparison:16 (p.14); C 59 (p.51)<br>P comparison:231 (p.17); C 712 (p.60)<br>P comparison:240 (p.17); C 721 (p.60) | 4.1–4.2 | 29, 37 | A (4.1), D |
|  |  | $D=\mathcal C(\cdot)+\mathcal C(\cdot)-2C_0$ (proof of L. 4.3); $D_h=\mu^2w^2-z^2$, $D'$ | P comparison:361 (p.19); C 1088 (p.66)<br>P comparison:942 (p.28); C 2618 (p.89) | 4.1; 4.2 |  | A (4.1, 4.2) |
|  |  | allowance $D$; $D_a$, $D_\phi$, $\overline D_\phi$ ($D_a$ restated as $D-10/n^2$ in 4.5) | P comparison:537 (p.21); C 1493 (p.71)<br>P comparison:556 (p.21); C 1529 (p.72)<br>P localization:374 (p.38); C 1311 (p.124) | 4.2–4.6 | 52, 53, 54, 75 | A (4.2), D |
|  |  | $D_b=\sin\gamma\sin b$ vs $D_b=4w_0/\pi+a_0b_0\log\pi$ | P localization:192 (p.36); C 771 (p.117)<br>P localization:384 (p.38); C 1321 (p.124) | 4.3 vs 4.5 |  | B (same token) |
|  |  | $D_R$ largest coefficient sum | P certification:65 (p.42); C 311 (p.138) | 5.1 |  | B |
|  |  | companion: $D=\operatorname{diag}(\dots)$; $D_*=(v^2-s^2\sin^2e)_+^{1/2}$ | C only preliminaries:365 (p.15)<br>C only comparison:219 (p.53) | §2; 4.1 | – | C |
| 6 | $k$, $K$ | node index $k$ and generic summation index | P preliminaries:15 (p.4); C 90 (p.11)<br>P corner:70 (p.7); C 244 (p.23) | global | 2, 8, 10, 13, 32, 48, 59, 69 | D |
|  |  | $k=2\gamma-2\log\pi$; $k_0=C_0-2\log\pi$ | P comparison:122 (p.16); C 392 (p.56)<br>P comparison:128 (p.16); C 398 (p.56) | 4.1 | 35, 46 | A (4.1: index $k$ in (32)) |
|  |  | allowance slopes $k_{Nx},k_{Ny},k_{Wx},k_{Wy}$ | P comparison:547 (p.21); C 1503 (p.71) | 4.2–4.6 | 52, 58, 75 | D |
|  |  | mesh ratio $k=n/m$ ($=\mu$ of 4.2) | P localization:473 (p.40); C 1595 (p.129)<br>P certification:113 (p.43); C 646 (p.144) | 4.6, §5 | 86, 90 | B, D, synonym of $\mu$ |
|  |  | local: $k_s$; $k_\pm\in\{0,1\}$; $k=r\pm j$; argument of $K(k)$ | P comparison:898 (p.27); C 2477 (p.87)<br>P comparison:798 (p.26); C 2167 (p.82)<br>P comparison:1190 (p.31); C 3358 (p.100)<br>P comparison:507 (p.21); C 1407 (p.70) | 4.1–4.2 |  | A (4.2) |
|  |  | kernel $K_n(z,B)$ | P preliminaries:25 (p.4); C 136 (p.11) | §2 |  | B |
|  |  | chart index $K$ (with $J$), $\Delta_{JK}$, $Q_v(K)$ | P localization:28 (p.13); C 93 (p.47) | §4, 5.2 | 25, 28 | D |
|  |  | truncation $K$ in (48); $K(k)$; $K_D$; $K=\operatorname{sinc}\cdot\operatorname{sinc}$; $K=L+25\log(2m)+193/3$; $K_t(w)$ | P comparison:428 (p.20); C 1256 (p.68)<br>P comparison:542 (p.21); C 1498 (p.71)<br>P comparison:943 (p.28); C 2619 (p.89)<br>P comparison:1089 (p.30); C 3044 (p.96)<br>P comparison:1163 (p.31); C 3248 (p.99) | 4.1–4.2 | 48, 52, 55, 56 | A (4.2), D |
|  |  | outer-gate slope $K$ | P localization:407 (p.39); C 1362 (p.125) | 4.5 | 83 | B (chart $K$), D |
|  |  | companion: curvature bound $K$; $K_M$; trapezoid kernel $K$ | C only certification:42 (p.134)<br>C only corner:780 (p.32)<br>C only corner:896 (p.34) | §5 pre.; 3.2; 3.3 | – | C |
| 7 | $j$, $J$ | node/summation index $j$ (also $j$ in (74)) | P preliminaries:15 (p.4); C 90 (p.11)<br>P localization:249 (p.36); C 993 (p.120) | global | 2, 8, 13, 74 | D |
|  |  | model constant $j=H_0+d_0-g_0$; $j_*=23/250$ | P comparison:309 (p.18); C 924 (p.63)<br>P localization:401 (p.39); C 1356 (p.125) | 4.1–4.6 | 40, 43, 49, 52, 75, 83 | A (4.2, 4.4), D |
|  |  | reference label $j$ in $\ell_r$, $h_j,g_j,B_j,\Xi_j,e_j$ | P comparison:637 (p.23); C 1660 (p.74)<br>P comparison:1113 (p.30); C 3097 (p.96) | 4.2 | 59, 63 | A (4.2), D |
|  |  | $J(x)=\log(1-x)-\psi((1-x)/2)$ | P corner:357 (p.11); C 1359 (p.41) | 3.3 |  | B |
|  |  | cancellation $J(v,s,e)$; $J_0$ | P comparison:20 (p.14); C 63 (p.51)<br>P comparison:101 (p.15); C 357 (p.55) | 4.1–4.2 | 29, 31, 33, 42 | A (4.1–4.2), D |
|  |  | chart index $J$, $\Delta_{JK}$, $Q_h(J)$ | P localization:28 (p.13); C 93 (p.47) | §4, 5.2 | 25, 28 | D |
|  |  | allowances $J_N,J_W$; retained rows $J_6,J_{\rm end},J_{\rm cen}$ | P comparison:545 (p.21); C 1501 (p.71)<br>P comparison:634 (p.23); C 1641 (p.73) | 4.2–4.4 | 52, 68 | D |
| 8 | $a$, $\mathfrak a$ | $a=2/\pi$ (Thm 1.2) | P introduction:112 (p.3); C 297 (p.6) | §1, §3 | 3, 17, 18, 21, 22, 23 | B, D |
|  |  | $a=c_ec_d=(\cos x+\cos y)/2$ | P comparison:10 (p.14); C 34 (p.51) | 4.1–4.6 (also in $A(u,v)$, 4.3) | 37, 38, 39, 41, 42, 45, 50, 53, 63, 68, 69, 82 | A (4.3 with $a_r,a_0$), D |
|  |  | $a_j=j\pi/n$ (with $b_k$) | P localization:14 (p.13); C 47 (p.47) | §4 pre. | 24 | D |
|  |  | radius profile $a_r=1-r^2/4$, $a_\rho$ | P localization:77 (p.34); C 321 (p.111) | 4.3–4.4 |  | A (4.3) |
|  |  | band endpoint $a_0$ ($\pi/20$, $\pi/100$) | P localization:193 (p.36); C 772 (p.117)<br>P localization:230 (p.36); C 938 (p.119) | 4.3 | 73 | A (4.3), D |
|  |  | $a_0=337/384$ | P localization:354 (p.38); C 1262 (p.124) | 4.5 | 82 | B (same token) |
|  |  | phase coordinate $a$, rectangle $[a_0,a_1]$ | P certification:19 (p.42); C 122 (p.135)<br>P certification:113 (p.43); C 646 (p.144) | §5 | 88, 90 | B, D |
|  |  | $\mathfrak a_p$ series coefficients | P comparison:413 (p.19); C 1241 (p.68) | 4.1 | 48 | D |
|  |  | companion: $a,b$ real parts; Fourier coefficients $a_p$ | C only preliminaries:223 (p.13)<br>C only certification:745 (p.146) | §2; 5.2 | – | C |
| 9 | $A$ | node $A\in\mathcal P_n$ | P preliminaries:3 (p.4); C 30 (p.10) | §2 |  | B |
|  |  | $A(z)=a(\log z+d)$ | P corner:15 (p.6); C 34 (p.20) | §3 | 15, 17 | B, D |
|  |  | $A(v)=2(\vert C\vert +\vert D\vert )/\pi$ | P comparison:234 (p.17); C 715 (p.60) | 4.1 | 37 | D |
|  |  | $A=398/(11\pi^2)$ (with $B=48/\pi$) | P comparison:1004 (p.28); C 2794 (p.92) | 4.2 |  | A (4.2: $A_4,A_6$) |
|  |  | $A_4$ allowance; $A_6$ row set | P comparison:543 (p.21); C 1499 (p.71)<br>P comparison:633 (p.23); C 1640 (p.73) | 4.2–4.4 | 52, 68 | D |
|  |  | pair numerators $A(u,v)$, $A_*$, $A_g$, $A(b)$, $A_0$, $A_r$; $A_h,A_w$ | P localization:127 (p.35); C 389 (p.112)<br>P localization:192 (p.36); C 771 (p.117)<br>P localization:99 (p.34); C 343 (p.112)<br>P localization:281 (p.37); C 1072 (p.121) | 4.3–4.4 |  | A (4.3) |
|  |  | outer-gate coefficient $A$; $A_u=1-u$ | P localization:407 (p.39); C 1362 (p.125)<br>P localization:434 (p.40); C 1453 (p.127) | 4.5 | 83 | D |
|  |  | inward corner phases $A,B$ | P localization:471 (p.40); C 1593 (p.129)<br>P certification:214 (p.45); C 1397 (p.156) | 4.6, 5.2 | 86, 87 | B, D |
|  |  | companion: integer indices $A=p+q$, $B=q-p$; $A=c_e/(2c)$; $A_N$ | C only corner:105 (p.21)<br>C only comparison:3526 (p.103)<br>C only certification:510 (p.142) | 3.1; 4.2; 5.1 | – | C |
| 10 | $B,\mathcal B$ | node $B$, coordinates $B_1,B_2$ | P preliminaries:31 (p.5); C 194 (p.12) | §1–§2 | 6 | D |
|  |  | $B(x)$ two-pole-removed cotangent; $I_B,C_B,\beta_B,F_B,G_B$ | P corner:58 (p.7); C 195 (p.22) | §3 | 9, 17, 18 | D |
|  |  | $\mathcal B(v)$; $B_0=4a/\pi^2$; $B=C_0^2/\pi^2$; $B_\beta$ | P comparison:235 (p.17); C 716 (p.60)<br>P comparison:239 (p.17); C 720 (p.60)<br>P comparison:306 (p.18); C 921 (p.63)<br>P comparison:473 (p.20); C 1349 (p.69) | 4.1–4.2 | $\mathcal B$: 37, 38, 39; $B_0$: 38; $B$: 45; $B_\beta$: 50, 51 | A (4.1), D |
|  |  | pole norm $B_n(t)$ | P comparison:685 (p.24); C 1833 (p.77) | 4.2 | 61 | D (same token as below) |
|  |  | floor $B_n(r)$ | P localization:81 (p.34); C 325 (p.111) | 4.3 | 70 | B, D |
|  |  | $B_j(s)$; $B=48/\pi$; $B_{\rm out}$; $B_h,B_w$ | P comparison:746 (p.25); C 2010 (p.80)<br>P comparison:1004 (p.28); C 2794 (p.92)<br>P comparison:1084 (p.30); C 3014 (p.95)<br>P localization:282 (p.37); C 1073 (p.121) | 4.2, 4.4 |  | A (4.2) |
|  |  | Bernstein basis $B_i^n$; inward phase $B$ | P certification:31 (p.42); C 134 (p.135)<br>P localization:471 (p.40); C 1593 (p.129) | §5; 4.6 | 89 | B, D |
|  |  | companion: $B=c_d/(2c)$; $B_t$; $B_{\rm ord}$ | C only comparison:3526 (p.103)<br>C only comparison:3254 (p.99)<br>C only comparison:1770 (p.76) | 4.2 | – | C |
| 11 | $g$ | function in $Q_M(g)$; quadrature function in L. 3.1 | P preliminaries:41 (p.5); C 210 (p.13)<br>P corner:212 (p.9); C 880 (p.34) | §2; 3.3 |  | B |
|  |  | second derivative $g=f''$ of the scalar profile | P comparison:94 (p.15); C 350 (p.55) | 4.1 (L. 4.2) | 33 | A (4.1), D |
|  |  | cancellation integrand $g(C,D;t)$ | P comparison:22 (p.14); C 65 (p.51)<br>P comparison:817 (p.26); C 2267 (p.84) | 4.1–4.2 |  | A (4.1–4.2), D |
|  |  | $g_0$; $g_j(t)$; $g_n$; $g_L,g_R$ | P comparison:308 (p.18); C 923 (p.63)<br>P comparison:639 (p.23); C 1662 (p.74)<br>P comparison:582 (p.22); C 1555 (p.72)<br>P comparison:1270 (p.32); C 3635 (p.105) | 4.1–4.2 | 41, 49, 54, 59, 69 | A (4.2), D |
|  |  | $g_{\sigma\eta}$ reflected values | P localization:44 (p.14); C 145 (p.48) | §4 pre. | 27 | D |
|  |  | constant $g$ of the radial quadratic | P localization:304 (p.37); C 1121 (p.122) | 4.4 | 77 | B, D |
|  |  | angle $g$ in $A_g$; descent margin $g=q-M\pi^4\max/6$ | P localization:177 (p.36); C 638 (p.115)<br>P certification:216 (p.45); C 1399 (p.156) | 4.3; 5.2 |  | B |
| 12 | $f$, $F$ | interpolated function $f$ | P introduction:8 (p.2); C 43 (p.2) | §1–§2 | 1 | D |
|  |  | corner summand $f(u,v)$ | P corner:19 (p.6); C 71 (p.20) | §3 | 8, 13, 14 | D |
|  |  | scalar profile $f(w)=\Phi(1/2+w/(2\pi))$ | P comparison:86 (p.15); C 318 (p.55) | 4.1–4.2 | 32, 33, 34, 35, 36 | A (4.2), D |
|  |  | weights $f_k$ (with $e_j$) | P localization:14 (p.13); C 47 (p.47) | §4 pre., 4.3 | 24 | D |
|  |  | $f=g(-w+c,w+d)-g(-w,w)$ | P comparison:828 (p.26); C 2278 (p.84) | 4.2 | 64 | A (4.2), D |
|  |  | sinc row $f_j$ (with $F_j$) | P comparison:926 (p.27); C 2559 (p.88) | 4.2 | 66 | A (4.2), D |
|  |  | $f_b(z)$; decreasing $f$; quadratic coefficient $f$; even $f$ | P localization:195 (p.36); C 774 (p.117)<br>P localization:303 (p.37); C 1120 (p.122)<br>P localization:474 (p.40); C 1596 (p.129) | 4.3, 4.4, 4.6 | 77 | B, D |
|  |  | $f_\sigma$, $F=\max f_\sigma$; $f_\varepsilon$ | P certification:18 (p.42); C 121 (p.135) | §5 | 88 | B, D |
|  |  | $F_r(u)$; $F(x)$; $F_B$; $F_s(L,z)$; $F_0$; $F(v,a)$; $F_{\rm near},F_{\rm small},F_h,F_w$; $F_u$ | P corner:87 (p.7); C 260 (p.24)<br>P corner:322 (p.11); C 1247 (p.39)<br>P comparison:659 (p.23); C 1702 (p.74)<br>P comparison:502 (p.21); C 1402 (p.70)<br>P localization:435 (p.40); C 1454 (p.127) | §3–4.5 |  | B |
| 13 | $r$, $s$ (indices vs parameters) | row index $r$; Chebyshev degree $r$; $r=j+k$ | P corner:61 (p.7); C 232 (p.23)<br>P corner:122 (p.8); C 427 (p.27) | §2–§3, 4.2 | 11, 12, 19, 22 | D |
|  |  | radius bound $r$ of Lemma 4.6 ($\rho\leq r$); $a_r,U_r,\dots$ | P localization:77 (p.34); C 321 (p.111) | 4.3–4.4 | 70, 71 | A (4.3 proof), D |
|  |  | periodic indices $(r,s)$ in $\Gamma^-$, $H_{rs}$ | P localization:35 (p.13); C 126 (p.48)<br>P localization:120 (p.35); C 382 (p.112) | §4 pre., 4.3, 5.2 | 26 | A (4.3 proof), D |
|  |  | endpoint index distance $s$ ($1\leq s\leq4$) | P localization:145 (p.35); C 496 (p.114) | 4.3 (proof) |  | A (4.3) |
|  |  | $s=m-r$; $s=j-k$; $J(v,s,e)$ argument; $c_s$; $s=b/\pi$, $\pm y/\pi$; side label $v_s,N_s,P_s$ | P corner:62 (p.7); C 233 (p.23)<br>P corner:122 (p.8); C 427 (p.27)<br>P comparison:20 (p.14); C 63 (p.51)<br>P comparison:1115 (p.30); C 3099 (p.97) | §3, 4.1–4.2 | §3: 11, 19, 20; §4.1–4.2: 29, 30, 31 | A (4.2), D |
|  |  | $r_0$; $r(w)$ residual; $r=c_e+c_d-2a$; $r_U$; $r_R$; Abel $r$ | P comparison:536 (p.21); C 1492 (p.71)<br>P comparison:1147 (p.30); C 3197 (p.98)<br>P comparison:1297 (p.33); C 3757 (p.107)<br>P localization:513 (p.41); C 1734 (p.131)<br>P certification:188 (p.45); C 1141 (p.152) | 4.1–§5 | 52, 53 | A (4.2), D |
|  |  | squared inward variables $s=A^2/2$, $t=B^2/2$; Bernstein $(s,t)$ | P localization:471 (p.40); C 1593 (p.129)<br>P certification:32 (p.42); C 135 (p.135) | 4.6, §5 | 89 | B, D |
| 14 | $L$ | cardinal polynomials $L_B$, $L_{jk}$, $L_\ell$ | P introduction:74 (p.2); C 188 (p.4)<br>P localization:17 (p.13); C 50 (p.47) | §1–§2, §4 pre., §5 | 6, 24, 89 | D |
|  |  | square reference $L_n$ | P corner:113 (p.8); C 418 (p.26) | 3.2–3.3 | 13 | D |
|  |  | $L=\log n$ | P comparison:4 (p.14); C 28 (p.51) | 4.1–4.6 | 38, 52, 53, 54, 56, 61, 67, 68, 69 | B (4.3/4.4), D |
|  |  | periodic mesh size $L$ in $(M,L)$ | P localization:135 (p.35); C 452 (p.113) | 4.3 (proof) | 72 | B, D |
|  |  | floor $L_h(\rho)$; cyclic vector $L_{n,k}$; lower endpoint $L_c$ | P localization:275 (p.37); C 1066 (p.121)<br>P comparison:1215 (p.31); C 3454 (p.102)<br>P certification:60 (p.42); C 277 (p.138) | 4.4; 4.2; §5 | 76 | B, D |
|  |  | companion: $L=\log m$; $L(y)$ analytic factor | C only corner:1519 (p.43)<br>C only corner:1427 (p.41) | 3.3 | – | C |
| 15 | $M,\mathcal M$ | grid size $M$ in $Q_M$, $h_p^{(M)}$; offset cutoff $M$ ($\ell>M$); $M_m$; $C_M$ | P preliminaries:39 (p.5); C 208 (p.13)<br>P corner:194 (p.9); C 758 (p.32)<br>P corner:347 (p.11); C 1342 (p.40) | §2; 3.2; 3.3 | 21 | B, D |
|  |  | $M_\infty$ completed model; $\mathcal M$, $\mathcal M_\phi$; $M_A^\phi,M_A$ | P comparison:243 (p.17); C 724 (p.60)<br>P comparison:538 (p.21); C 1494 (p.71) | 4.1–4.6 | $M_\infty$: 38, 55; $\mathcal M,\mathcal M_\phi$: 52, 53, 54, 65; $M_A^\phi,M_A$: 53, 54 | D |
|  |  | analytic norm $M(n)$ (also bare $M$ in 4.6, §5) | P comparison:601 (p.22); C 1589 (p.73)<br>P localization:471 (p.40); C 1593 (p.129) | 4.2–§5 | $M(n)$: 56; 4.6: 86; L. 5.1 (generic): 88; 5.2: 90 | D |
|  |  | coefficient height $M$ in $M\tan(e/2)$ | P comparison:824 (p.26); C 2274 (p.84) | 4.2 |  | A (4.2: $M(n)$, $\mathcal M$) |
|  |  | physical mesh size $M$ in $(M,L)$ | P localization:135 (p.35); C 452 (p.113) | 4.3 | 72 | B, D |
|  |  | $M_b$, $\mathcal M_b$; $M_*$ true norm | P localization:378 (p.38); C 1315 (p.124)<br>P certification:142 (p.44); C 943 (p.149) | 4.5; 5.2 | 91, 92 | B, D |
|  |  | companion: $M_*:=2\varepsilon\cot e$; $M=\sup\vert F_0'\vert $; $N=2M+1$ | C only comparison:2305 (p.84)<br>C only comparison:3957 (p.109)<br>C only comparison:977 (p.64) | 4.2; 4.1 | – | C ($M_*$ clashes with §5) |
| 16 | $Q,\mathcal Q$ | quadrature $Q_M(g)$; $Q_\tau[F]$ | P preliminaries:41 (p.5); C 210 (p.13)<br>P comparison:661 (p.23); C 1704 (p.74) | §2; 4.2 | 69 | D |
|  |  | $Q_i=\vert u-v_i\vert /2$; remainder $Q_{m,r}$ | P corner:155 (p.8); C 567 (p.29)<br>P corner:325 (p.11); C 1250 (p.39) | 3.2; 3.3 | 20 | D |
|  |  | square $Q=[-1,1]^2$; series $Q(t)=2\sum\zeta(2j+1)t^{2j}$ | P preliminaries:2 (p.4); C 2 (p.9)<br>P comparison:116 (p.16); C 372 (p.56) | §2; 4.1 |  | B (vs $Q_t$ in 4.2) |
|  |  | $\mathcal Q_j$; $Q_0(z)$; $Q_u$ | P comparison:654 (p.23); C 1697 (p.74)<br>P comparison:1047 (p.29); C 2886 (p.93)<br>P localization:436 (p.40); C 1455 (p.127) | 4.2; 4.5 |  | A (4.2: $Q_0$ vs $Q_\tau$) |
|  |  | projections $Q_v(K),Q_h(J)$ and bare $Q$ for a projection value | P localization:53 (p.14); C 192 (p.49)<br>P localization:160 (p.35); C 562 (p.114) | §4 pre., 4.3 | 28, 72, 73 | D |
|  |  | companion: $Q$ = magnitude of negative sum; $Q_*$; $Q_H$ | C only corner:353 (p.25)<br>C only comparison:1031 (p.65)<br>C only comparison:3344 (p.100) | 3.1; 4.1; 4.2 | – | C |
| 17 | $R$ | remainder $R(v,s,e)$, derivatives $R_s,R_e$ | P comparison:30 (p.14); C 100 (p.52)<br>P comparison:36 (p.14); C 106 (p.52) | 4.1–4.2 | 30 | D |
|  |  | $R(x)$ singularity-subtracted; cutoff $R$ | P corner:356 (p.11); C 1358 (p.41)<br>P corner:312 (p.11); C 1215 (p.39) | 3.3 |  | B |
|  |  | row sums $R_r$; $R_{\rm mesh}$, $R_{\log}$ | P comparison:622 (p.22); C 1610 (p.73)<br>P comparison:665 (p.23); C 1708 (p.74) | 4.2 | 60, 65, 68 | A (4.2: $R(v,s,e)$), D |
|  |  | band remainder $R$; $R_h,R_w$; $R_b$ | P localization:213 (p.36); C 843 (p.118)<br>P localization:100 (p.34); C 344 (p.112)<br>P localization:382 (p.38); C 1319 (p.124) | 4.3; 4.5 | 73 | B, D |
|  |  | rectangle $R$, $I_R,q_R,V_R,\theta_R,\delta_R,r_R$ | P certification:19 (p.42); C 122 (p.135) | §5 | 90, 91 | B, D |
|  |  | companion: $R_n$ remainder (intro) and $R_n(z,B)$ kernel (§2); $R_t$ | C only introduction:369 (p.7)<br>C only preliminaries:180 (p.12)<br>C only comparison:578 (p.58) | §1; §2; 4.1 | – | C (same token) |
| 18 | $\gamma$, $\kappa$, $\zeta$, $\psi$ | Euler's constant $\gamma$ | P introduction:115 (p.3); C 300 (p.6) | global ((3), (10), (32), (40)) | 3, 10, 17, 18, 21, 22, 32, 33 | D |
|  |  | center angle's distance $\gamma$ to the nearest endpoint; $\gamma_b$ | P localization:136 (p.35); C 453 (p.113)<br>P localization:377 (p.38); C 1314 (p.124) | 4.3 (proof); 4.5 |  | B (Euler $\gamma$ live in 4.1) |
|  |  | main constant $\kappa$ (4) | P introduction:117 (p.3); C 302 (p.6) | global | 3, 4, 15, 46, 47, 48 | D |
|  |  | companion: $\kappa=8a_0/(3\pi)$ | C only localization:1421 (p.126) | 4.5 | – | C (severe) |
|  |  | Riemann $\zeta$ vs companion root of unity $\zeta=e^{2\pi\mathrm i/N}$ | P comparison:116 (p.16); C 372 (p.56)<br>C only comparison:965 (p.64) | 4.1 | – | C (A in 4.1) |
|  |  | digamma $\psi$ vs companion hat function $\psi_B$ | P corner:70 (p.7); C 244 (p.23)<br>C only preliminaries:55 (p.10) | §3–4.2; §2 | – | C |
| 19 | $e$, $\bar e$ | Euler's number: $\mathrm e$ in (53), but italic $e^{i(pu+qv)}$ in 3.1 | P corner:26 (p.6); C 78 (p.20)<br>P comparison:562 (p.21); C 1535 (p.72) | 3.1; 4.2, 4.5 | 53 | glyph |
|  |  | separation $e$ in $I(C,D,e)$, $J,E,Z,R$ | P comparison:16 (p.14); C 59 (p.51) | 4.1–4.2 | 29, 30, 31 | A (4.2), D |
|  |  | weights $e_j$; $e_r=\psi(r+1/2)-\log r$, $S_e$ | P localization:14 (p.13); C 47 (p.47)<br>P corner:304 (p.11); C 1165 (p.38) | §4 pre.; 3.3 | 24 | B, D |
|  |  | $e_j$ endpoint comparison; $e=\rho$; $e=\pi-z$ | P comparison:1120 (p.30); C 3104 (p.97)<br>P comparison:1260 (p.32); C 3625 (p.105)<br>P comparison:894 (p.27); C 2473 (p.87) | 4.2 |  | A (4.2) |
|  |  | radial-quadratic coefficient $e$ | P localization:302 (p.37); C 1119 (p.122) | 4.4 | 77 | B, D |
|  |  | allowance $\bar e=D+\mathcal M+1/n$ | P comparison:541 (p.21); C 1497 (p.71) | 4.2–4.6 | 52, 57, 75, 83 | D |
|  |  | companion: odd-$n$ indicator $e$; $e_{pq}$; $e_B$; $e_r:=R_r/(nm)-\ell_r$ | C only corner:468 (p.27)<br>C only preliminaries:287 (p.14)<br>C only introduction:74 (p.3)<br>C only comparison:3332 (p.100) | 3.2; §2; §1; 4.2 | – | C ($e_r$ same token as 3.3) |
| 20 | $b$ | $b=2ac_1$ (3); $b_{\rm full}$, $b_c$, $b_*$ | P introduction:113 (p.3); C 298 (p.6)<br>P comparison:244 (p.17); C 725 (p.60) | §1; 4.1 | 3, 5, 38, 40 | D |
|  |  | $b_k=k\pi/m$ | P localization:14 (p.13); C 47 (p.47) | §4 pre. | 24 | D |
|  |  | $b=(v+s)/2$ in proof of L. 4.1; $b=2\arctan(q/(2a))$ | P comparison:53 (p.15); C 123 (p.52)<br>P comparison:472 (p.20); C 1348 (p.69) | 4.1 |  | A (4.1) |
|  |  | $b_0=4/\pi^2$ | P comparison:536 (p.21); C 1492 (p.71) | 4.2, 4.5 | 52, 53 | D |
|  |  | residual $b$; $b(z)$; $b=\xi+\vert s\vert $; $b_s,b_L,b_R$; second argument of $\ell_r(x,b)$ | P comparison:691 (p.24); C 1853 (p.77)<br>P comparison:1045 (p.29); C 2884 (p.93)<br>P comparison:1131 (p.30); C 3132 (p.97)<br>P comparison:1324 (p.33); C 3820 (p.107) | 4.2 |  | A (4.2), D |
|  |  | physical row $b=l\pi/M$; band $[a_0,b_0]$ | P localization:137 (p.35); C 454 (p.113)<br>P localization:216 (p.36); C 887 (p.118) | 4.3 |  | B ($b_0$ token) |
|  |  | phase coordinate $b$, $[b_0,b_1]$ | P certification:19 (p.42); C 122 (p.135) | §5 | 88, 90 | B, D |
| 21 | $c$ | $c=c_1^2+\kappa$, $c_1=ad$ | P introduction:113 (p.3); C 298 (p.6) | global | 3, 5 | D |
|  |  | $c_r=\csc(r\pi/(2n))$ | P corner:123 (p.8); C 428 (p.27) | 3.2 |  | B |
|  |  | $c=(v-s)/2$ in proof of L. 4.1; $c_s$, $c=\cos(\pi s/2)$ | P comparison:53 (p.15); C 123 (p.52)<br>P comparison:128 (p.16); C 398 (p.56)<br>P comparison:342 (p.19); C 1016 (p.65) | 4.1 |  | A (4.1) |
|  |  | $c_e,c_d$ (phase cosines); $c_k$ (48) | P comparison:9 (p.14); C 33 (p.51)<br>P comparison:418 (p.19); C 1246 (p.68) | 4.1–4.6 | 37, 41, 48, 53, 66 | D |
|  |  | shift $c$ in $g(-w+c,\dots)$; $n\pm c$; $c$ in $2\cos$ denominators; $c_P$ | P comparison:828 (p.26); C 2278 (p.84)<br>P comparison:980 (p.28); C 2717 (p.91)<br>P comparison:1235 (p.32); C 3492 (p.103)<br>P comparison:1365 (p.34); C 3977 (p.110) | 4.2 |  | A (4.2) |
|  |  | band parameter $c$ ($5/4$, $2$); $c=\cos(1/2)$; descent $c$ | P localization:196 (p.36); C 775 (p.117)<br>P localization:361 (p.38); C 1282 (p.124)<br>P localization:527 (p.41); C 1775 (p.132) | 4.3; 4.5; 4.6 | 73, 86 | B, D |
|  |  | Bernstein coefficients $c_{\ell,ij}$; $c=q/\pi^2$ | P certification:28 (p.42); C 131 (p.135)<br>P certification:210 (p.45); C 1393 (p.156) | §5 | 89 | B, D |
|  |  | companion: $c=\cos u$, $c_i=\cos v_i$; $c_v$; $c_j$ | C only corner:571 (p.29)<br>C only corner:1519 (p.43)<br>C only certification:750 (p.146) | 3.2; 3.3; 5.2 | – | C |
| 22 | $d,\mathfrak d$ | $d=\gamma+\log(8/\pi)$ | P introduction:112 (p.3); C 297 (p.6) | global | 3 | D |
|  |  | weights $d_r$ | P corner:114 (p.8); C 419 (p.26) | 3.2 |  | B |
|  |  | $d_0=\gamma+2\log2$ | P corner:321 (p.11); C 1246 (p.39) | 3.3 |  | B (same token) |
|  |  | $d_0=C_0b_*/\pi^2$ | P comparison:306 (p.18); C 921 (p.63) | 4.1 | 45, 49 | B (same token), D |
|  |  | $d_+=(q-p)_+$; $d_\beta$ | P comparison:13 (p.14); C 37 (p.51)<br>P comparison:544 (p.21); C 1500 (p.71) | 4.1–4.6 | 52, 68 | D |
|  |  | $d=v/h_*$; shift $d$; $d(z)$; $d_1,d_2$ | P comparison:718 (p.24); C 1982 (p.79)<br>P comparison:828 (p.26); C 2278 (p.84)<br>P comparison:1045 (p.29); C 2884 (p.93)<br>P localization:296 (p.37); C 1113 (p.121) | 4.2; 4.4 |  | A (4.2) |
|  |  | pair defect $\mathfrak d(z,w)$ | P localization:51 (p.14); C 190 (p.49) | §4 pre., 4.3 | 28 | D |
|  |  | companion: $d=\pi/L$; degree $d$; $d_i^{(r)}$ | C only localization:676 (p.116)<br>C only certification:745 (p.146)<br>C only certification:418 (p.140) | 4.3; 5.1–5.2 | – | C |
| 23 | $h$ | $h=n-j$; $h_{\sigma,\ell}$; cell width $h$; shift $h$ | P corner:167 (p.8); C 627 (p.30)<br>P corner:185 (p.9); C 683 (p.31)<br>P corner:227 (p.9); C 900 (p.34)<br>P corner:296 (p.11); C 1119 (p.38) | 3.2; 3.2; 3.3; 3.3 |  | A (3.3) |
|  |  | mesh steps $h=\pi/m$, $h=\pi/n$, $h_*=\pi/n$ | P comparison:635 (p.23); C 1658 (p.74)<br>P comparison:697 (p.24); C 1871 (p.77)<br>P comparison:718 (p.24); C 1982 (p.79) | 4.2 |  | A (4.2) |
|  |  | series $h_j(t)$; $H_h$, $D_h$ | P comparison:637 (p.23); C 1660 (p.74) | 4.2 | 59 | A (4.2), D |
|  |  | label h(orizontal) in $Q_h$, $I_h,R_h,F_h,A_h,B_h$ | P localization:55 (p.14); C 194 (p.49)<br>P localization:100 (p.34); C 344 (p.112) | §4 pre.–4.4 | 28, 71 | D |
|  |  | $h_p^{(M)}$; $h=x-1/2$; $h=\pi/4$; vector $(h_\ell)$ | P preliminaries:47 (p.5); C 278 (p.14)<br>P localization:362 (p.38); C 1283 (p.124)<br>P localization:490 (p.40); C 1694 (p.130)<br>P certification:7 (p.42); C 63 (p.134) | §2; 4.5; 4.6; §5 |  | B |
| 24 | $u,v,w,z$ (variables) | kernel arguments $u,v$ in $G_n(u,v)$, $f(u,v)$, $A(u,v)$; $v=r\pi/m$; $v_0,v_1$ | P preliminaries:70 (p.5); C 535 (p.17)<br>P corner:85 (p.7); C 257 (p.24)<br>P corner:153 (p.8); C 565 (p.29) | §2–§4 |  | D |
|  |  | $u_r$; $v(x)=w(x)-a/x$ | P corner:304 (p.11); C 1165 (p.38)<br>P corner:336 (p.11); C 1304 (p.40) | 3.3 |  | A (3.3: $v$ angle and $v(x)$) |
|  |  | $u=1-a$, $z=(1-c_e)(1-c_d)$ | P comparison:10 (p.14); C 34 (p.51) | 4.1–4.6 | 40, 43, 45, 58 | A (4.2: $u$ angle), D |
|  |  | $J(v,s,e)$ coefficient $v$ ($v=p/2$); row variable $v$ in $C(v)$ | P comparison:20 (p.14); C 63 (p.51)<br>P comparison:229 (p.17); C 710 (p.60)<br>P comparison:492 (p.20); C 1368 (p.69) | 4.1–4.2 | 29, 30, 31, 37, 38 | A (4.1), D |
|  |  | $v_0=7b_*/(2\pi^2)$ vs $v_0=\pi j/m$ vs $v_0=\theta_k$ | P comparison:307 (p.18); C 922 (p.63)<br>P comparison:1170 (p.31); C 3279 (p.99) | 4.1; 4.2 | 40, 43, 45 | B (same token), D |
|  |  | $v=w/m$, $u_j=z/n$, $w=r\pi+b$, $z=j\pi+x$ | P comparison:917 (p.27); C 2550 (p.88) | 4.2 | 66 | A (4.2), D |
|  |  | $w(x)=\cot(\pi x/2)$; $w_{jk}$ weights | P corner:57 (p.7); C 194 (p.22)<br>P preliminaries:20 (p.4); C 95 (p.11) | §3; §2, §4 | 6, 9, 11, 12, 17, 18, 22, 24, 27 | D |
|  |  | $w$ in $f(w)$, $H(w)$; $w=a\cot(t/2)/2$; $w_r$; effective angle $w$; $w_0=721/384$; $w_*$ | P comparison:86 (p.15); C 318 (p.55)<br>P comparison:265 (p.18); C 799 (p.61)<br>P localization:147 (p.35); C 498 (p.114)<br>P localization:354 (p.38); C 1262 (p.124) | 4.1–5.1 | 32, 33, 34, 35, 36, 82 | A (4.1–4.2), D |
|  |  | $v=u-u_1$ (outer variable); $u_1$, $u_0$; $u',v'$ | P localization:353 (p.38); C 1261 (p.124)<br>P certification:201 (p.45); C 1368 (p.156) | 4.5; 5.2 | 82, 83 | B, D |
| 25 | $p,P$ and $q$ | mode indices $p,q$ | P preliminaries:25 (p.4); C 136 (p.11) | §2–§3 | 7 | D |
|  |  | $p=\sin x$, $q=\sin y$, $P=p+q$ | P comparison:13 (p.14); C 37 (p.51) | 4.1–4.6 | $p$: 37, 38, 40, 42, 48, 50, 53, 82; $q$: 37, 38, 42, 53, 82; $P$: 39, 53, 55, 63, 68, 82 | D |
|  |  | $q_0=\pi^2/4-1$ vs $q_0=7/48$ | P corner:321 (p.11); C 1246 (p.39)<br>P localization:490 (p.40); C 1694 (p.130) | 3.3; 4.6 |  | B (same token) |
|  |  | $q_\pm$; offsets $q$; corner-witness ratio $q$; $q_R$ | P comparison:744 (p.25); C 2008 (p.80)<br>P localization:145 (p.35); C 496 (p.114)<br>P certification:203 (p.45); C 1370 (p.156)<br>P certification:124 (p.44); C 713 (p.145) | 4.2; 4.3; 5.2 | 90 | A (4.3: $q$ offset vs $q=\sin y$), D |
|  |  | $P_r$; nodes $\mathcal P_n$; $P_n=T_{n+1}+T_n$ | P corner:96 (p.7); C 313 (p.25)<br>P localization:21 (p.13); C 69 (p.47) | 3.1; §4 pre. | 2 | D |
|  |  | $P_0(z)$ function vs $P_0=24/25$ | P comparison:1046 (p.29); C 2885 (p.93)<br>P localization:354 (p.38); C 1262 (p.124) | 4.2; 4.5 | 82, 83 | B (same token), D |
|  |  | $P_s$, $P_s^0$; polynomial $P(\rho)$; $p_\pi,p_0,p_\pm$ | P comparison:1266 (p.32); C 3631 (p.105)<br>P localization:328 (p.38); C 1193 (p.123)<br>P localization:94 (p.34); C 338 (p.112)<br>P certification:176 (p.44); C 1111 (p.152) | 4.2; 4.4; 4.3–§5 | 79 | A (4.4/4.5: $P(\rho)$ vs $P$), D |
| 26 | $\delta,\Delta$ | Kronecker $\delta_{AB}$; Dirac $\delta_\pi$ | P preliminaries:3 (p.4); C 30 (p.10)<br>P comparison:100 (p.15); C 356 (p.55) | §2; 4.1 | 33 | D |
|  |  | $\delta=v_0-v_1$; Riemann width $\delta$ | P corner:154 (p.8); C 566 (p.29)<br>P corner:190 (p.9); C 754 (p.32) | 3.2 |  | A (3.2) |
|  |  | $\delta=9/4-C_*$; $\delta=q/2$ | P comparison:464 (p.20); C 1326 (p.69)<br>P comparison:492 (p.20); C 1368 (p.69) | 4.1 |  | A (4.1) |
|  |  | $\delta_r$ parity; operator $\delta_aX$; $\delta\mathcal H_j$; $\delta=x-y$ | P comparison:620 (p.22); C 1608 (p.73)<br>P comparison:682 (p.24); C 1800 (p.76)<br>P comparison:1251 (p.32); C 3571 (p.104)<br>P comparison:1260 (p.32); C 3625 (p.105) | 4.2 | 68 | A (4.2), D |
|  |  | floors $\delta_n(r)$; gates $\delta_A,\delta_D,\delta$; $\delta_R$ | P localization:87 (p.34); C 331 (p.112)<br>P localization:494 (p.41); C 1698 (p.131)<br>P certification:174 (p.44); C 1109 (p.152) | 4.3; 4.6; §5 | 70 | D |
|  |  | $\Delta_n$; $\Delta_{JK}$; $\Delta_2$ | P corner:173 (p.9); C 660 (p.30)<br>P localization:47 (p.14); C 148 (p.48)<br>P comparison:656 (p.23); C 1699 (p.74) | 3.2; §4; 4.2 | 27, 63, 76 | D |
| 27 | $\eta,\sigma,\tau$ | weights $\eta_k$ vs signs $\eta=\pm1$ (24), (27) | P preliminaries:19 (p.4); C 94 (p.11)<br>P localization:18 (p.13); C 51 (p.47) | §2–§3; §4 pre. | 24, 27 | B, D |
|  |  | profile offsets $\eta_\pm(v)$; $\eta j$; $\eta_r$; $\eta=3/2$ | P comparison:232 (p.17); C 713 (p.60)<br>P comparison:771 (p.25); C 2104 (p.81)<br>P localization:96 (p.34); C 340 (p.112)<br>P localization:355 (p.38); C 1263 (p.124) | 4.1; 4.2; 4.3; 4.5 | $\eta_\pm$: 37; $\eta=3/2$: 82, 83 | B, D |
|  |  | $\sigma=\pm1$; $\sigma_\pm$; label $\sigma=N,W$; sign index of $f_\sigma$ | P corner:180 (p.9); C 678 (p.31)<br>P comparison:919 (p.27); C 2552 (p.88)<br>P comparison:1379 (p.34); C 4013 (p.110)<br>P certification:18 (p.42); C 121 (p.135) | 3.2; 4.2; 4.2; §5 | 24, 27 | A (4.2), D |
|  |  | $\tau=v/a$; $\tau(w)=w\cot w$; offset $\tau$ in $Q_\tau$; $\tau_j$ | P comparison:503 (p.21); C 1403 (p.70)<br>P comparison:802 (p.26); C 2171 (p.82)<br>P comparison:661 (p.23); C 1704 (p.74)<br>P comparison:1122 (p.30); C 3106 (p.97) | 4.1; 4.2 | 66 | A (4.2), D |
| 28 | $\ell$, $l$ | odd index $\ell$ in $\kappa$, (35), (48); $\ell=\vert j-k\vert $; row index in $T_{n,r}$ | P introduction:118 (p.3); C 303 (p.6)<br>P corner:147 (p.8); C 559 (p.29) | §1, §3, 4.1 | 4, 14, 35, 48 | D |
|  |  | $\ell=-\log\sin\epsilon$ (two values of $\epsilon$ in 4.2) | P comparison:558 (p.21); C 1531 (p.72)<br>P comparison:1330 (p.33); C 3835 (p.108)<br>P localization:373 (p.38); C 1310 (p.124) | 4.2, 4.5 | 53 | A (4.2), D |
|  |  | endpoint references $\ell_r(x,b)$, $\ell_1,\ell_2$ in $C_2$ | P comparison:648 (p.23); C 1691 (p.74) | 4.2 |  | A (4.2) |
|  |  | linear coefficients $\ell_1,\ell_2$ | P localization:296 (p.37); C 1113 (p.121) | 4.4 | 77 | B (same token as $\ell_1(x,y)$), D |
|  |  | arc length $\ell$; row index $l$ | P localization:140 (p.35); C 457 (p.113)<br>P localization:137 (p.35); C 454 (p.113) | 4.3 |  | A (4.3) |
|  |  | cardinal index $\ell$: $h_\ell,L_\ell,c_{\ell,ij}$ | P certification:28 (p.42); C 131 (p.135) | §5 | 89 | B, D |
| 29 | $I$ | operator $I_n$; bilinear $I_R,I_a,I_b$ | P introduction:5 (p.2); C 40 (p.2)<br>P certification:27 (p.42); C 130 (p.135) | §1–§2; §5 | 1, 88, 90 | D |
|  |  | integrals $I_1,I_2,I_B$; $I(t)$ | P corner:270 (p.10); C 1075 (p.37)<br>P corner:399 (p.12); C 1596 (p.43) | 3.3 | 17, 18, 21, 23 | D |
|  |  | cancellation $I(C,D,e)$; $I_4$; $I_s$ | P comparison:18 (p.14); C 61 (p.51)<br>P comparison:479 (p.20); C 1355 (p.69)<br>P comparison:1271 (p.32); C 3636 (p.105) | 4.1–4.6 | 29, 37, 50 | D |
|  |  | band integral $I$; $I_h,I_w$ | P localization:212 (p.36); C 842 (p.118)<br>P localization:100 (p.34); C 344 (p.112) | 4.3 | 73 | B, D |
|  |  | companion: intervals $I_1,I_2$ | C only comparison:2299 (p.84) | 4.2 | – | C (same tokens as 3.3) |
| 30 | $E,\mathcal E$ | $E(v,s,e)$; $E_\infty$; $E_c$ | P comparison:42 (p.15); C 112 (p.52)<br>P comparison:246 (p.17); C 727 (p.60)<br>P comparison:325 (p.18); C 940 (p.64) | 4.1–4.6 | $E$: 31; $E_\infty$: 38, 41, 45; $E_c$: 41, 42, 43, 50, 51, 58 | D |
|  |  | error $E_n=S_n-M_\infty$; $E_2,E_{\rm row},E_{\rm out},E_{\rm ret}$; $\mathcal E$ | P comparison:603 (p.22); C 1591 (p.73)<br>P comparison:1150 (p.31); C 3224 (p.98) | 4.2 | 57, 60 | D |
|  |  | lower bound $E_n=245931/6050000-\dots$ | P localization:224 (p.36); C 921 (p.119) | 4.3 |  | B (same token) |
|  |  | quarter grid $E$, $V_E$ | P certification:155 (p.44); C 1027 (p.151) | 5.2 | 92 | B, D |
|  |  | companion: $E_j$ trapezoid error; $E_{n,M,\delta}$ | C only corner:1487 (p.42)<br>C only corner:789 (p.32) | 3.3; 3.2 | – | C |
| 31 | $S$, $N$, $U,V,W$, $G$, $Z$, $\Gamma$ | $S,T$ angles; $S_i$; $S_e,S_u$ vs majorant $S_n(\alpha,\beta)$ | P corner:28 (p.6); C 95 (p.21)<br>P corner:309 (p.11); C 1170 (p.38)<br>P localization:38 (p.13); C 129 (p.48) | §3; §4–§5 | $S_n$: 26, 27, 55, 58, 79, 81, 83, 84, 85, 90 | B, D |
|  |  | $N=n+1/2$ vs $\mathsf N=nm$ vs $N_s,N_L,N_R$ vs labels $U_N,J_N,k_{Nx}$ | P introduction:125 (p.3); C 357 (p.7)<br>P localization:11 (p.13); C 44 (p.47)<br>P comparison:278 (p.18); C 830 (p.62)<br>P comparison:1263 (p.32); C 3628 (p.105) | §1, §3; §4–§5; 4.1–4.2 | $N$: 5; $\mathsf N$: 24, 26, 28 | B, D |
|  |  | $U_0$; $U_N,U_W$; $U_j$; $U_r$; vertex value $U$; Chebyshev $U_{n-1}$ | P comparison:239 (p.17); C 720 (p.60)<br>P comparison:551 (p.21); C 1507 (p.71)<br>P comparison:1123 (p.30); C 3107 (p.97)<br>P localization:79 (p.34); C 323 (p.111)<br>P localization:490 (p.40); C 1694 (p.130)<br>P comparison:1218 (p.32); C 3457 (p.102) | 4.1–§5 | $U_N,U_W$: 52, 58, 75; vertex $U$: 86 | A (4.2: $U_N$, $U_j$, $U_{n-1}$), D |
|  |  | $V_n$; $V$; $V_A^\phi,V_B^\phi$; variation $V$ (67); $V_s,V_0$; $V_\pm$; $V_r$; $V_b$; $V$; $V_R$ | P corner:65 (p.7); C 236 (p.23)<br>P corner:154 (p.8); C 566 (p.29)<br>P comparison:1053 (p.29); C 2910 (p.94)<br>P comparison:1265 (p.32); C 3630 (p.105)<br>P localization:79 (p.34); C 323 (p.111)<br>P certification:128 (p.44); C 717 (p.145) | §3–§5 | $V_n$: 12, 18; $V_A^\phi,V_B^\phi$: 53; $V$ (67): 67; vertex $V$: 86; $V_R,V_E$: 90, 91, 92 | A (4.2: $V$, $V_s$, $V_A^\phi$), D |
|  |  | $W(t)=tw(t)$ vs $W(t)=\int\log\cot$ ; span $W$; $W_r$; $W_n$; $W_z$ | P corner:401 (p.12); C 1598 (p.44)<br>P comparison:209 (p.17); C 624 (p.59)<br>P localization:132 (p.35); C 432 (p.113)<br>P comparison:576 (p.22); C 1549 (p.72)<br>P certification:22 (p.42); C 125 (p.135) | 3.3; 4.1; 4.3; 4.2–4.5; §5 | $W_n$: 53, 54, 65; $W$ (§5): 88, 90 | B (same token $W(t)$), D |
|  |  | $G_n$ kernel; $G_B$; $G_\phi,G_g$; $G_b$; gate $G$ | P preliminaries:70 (p.5); C 535 (p.17)<br>P corner:403 (p.12); C 1600 (p.44)<br>P localization:406 (p.39); C 1361 (p.125) | §2–4.5 | $G_n$: 7, 24, 26; $G_\phi,G_g$: 53, 54, 65; gate $G$: 83 | B, D |
|  |  | $Z(v,s,e)$; $Z_n$; $Z=2a\cot(z/2)$; $Z_b$; $\overline Z_\phi$ | P comparison:43 (p.15); C 113 (p.52)<br>P comparison:657 (p.23); C 1700 (p.74)<br>P comparison:1269 (p.32); C 3634 (p.105) | 4.1–4.5 | $Z$: 31; $\overline Z_\phi$: 53 | A (4.2), D |
|  |  | $\Gamma^-$ periodic lattice; entropy $\Gamma_\phi$, $\Gamma_b$, $\Gamma(p,a)$ | P localization:35 (p.13); C 126 (p.48)<br>P comparison:560 (p.21); C 1533 (p.72) | §4 pre., 4.3; 4.2, 4.5 | $\Gamma^-$: 26, 28; $\Gamma_\phi$: 53 | D |
| 32 | $\alpha,\beta,\theta,\phi,\nu,x,y,t$ | $\alpha=(1-x)/2$ (11) vs phase $\alpha$ (25) | P corner:62 (p.7); C 233 (p.23)<br>P localization:28 (p.13); C 93 (p.47) | §3; §4–§5 | §3: 11, 19; phase: 25, 26 | B, D |
|  |  | $\beta_H,\beta_B$ vs phase $\beta$; $B_\beta$, $d_\beta$ (label) | P corner:278 (p.10); C 1083 (p.37)<br>P localization:28 (p.13); C 93 (p.47) | 3.3; §4 | $\beta_H,\beta_B$: 17, 18; phase: 25, 26 | B, D |
|  |  | $\theta_j$ mesh angles vs physical $\theta,\phi$; $\theta$ in (44); $\theta_\pm$; $\theta_R$ | P preliminaries:15 (p.4); C 90 (p.11)<br>P localization:17 (p.13); C 50 (p.47)<br>P comparison:338 (p.19); C 953 (p.64)<br>P comparison:1168 (p.31); C 3277 (p.99)<br>P certification:129 (p.44); C 718 (p.145) | §2–§5 | physical: 24, 25; (44): 44; $\theta_R$: 90, 91 | B, D |
|  |  | $\phi_k$ vs physical angle $\phi$ vs phase point/label $\phi$ ($D_\phi$, $E_n(\phi)$) | P preliminaries:15 (p.4); C 90 (p.11)<br>P comparison:557 (p.21); C 1530 (p.72)<br>P comparison:1378 (p.34); C 4012 (p.110) | §2–§4 | physical $\phi$: 24, 25; label: 53 | B, D |
|  |  | $\nu_r$ multiplicities vs $\nu=j+s$ | P preliminaries:22 (p.4); C 129 (p.11)<br>P comparison:744 (p.25); C 2008 (p.80) | §2; 4.2 |  | B |
|  |  | $x=r/m$, $y_r$, $y=1-x$ (§3) vs phases $x=\vert \alpha\vert ,y=\vert \beta\vert $ (§4); $X,Y$ | P corner:62 (p.7); C 233 (p.23)<br>P comparison:8 (p.14); C 32 (p.51)<br>P comparison:289 (p.18); C 858 (p.62) | §3; §4 | §3: 17, 18, 20; phase: 37, 38, 41, 51, 58 | B, D |
|  |  | offset $t=y/\pi$ (4.2) vs dummy $t$; $t=j/n$; $t=r/m$; $t_0,t_1,t_\pm,t_d,t_e,t_*$ | P comparison:635 (p.23); C 1658 (p.74)<br>P corner:181 (p.9); C 679 (p.31)<br>P comparison:309 (p.18); C 924 (p.63) | §3–4.6 | 59, 61, 63, 69 | A (4.2), D |

**Further findings [D].**
- The same object is written $\epsilon_j$ (P preliminaries:17) and
  $\varepsilon_j$ (P corner:11), and $\epsilon=3\pi/(2m)$ in (53) is
  re-introduced as $\varepsilon=3\pi/(2m)$ at P localization:373.
- In Section 4.2, $\ell=-\log\sin\epsilon$ is defined with
  $\epsilon=3\pi/(2m)$ in (53) and again with $\epsilon=h/2=\pi/(2m)$ at
  P comparison:1330: two values for one token in one subsection.
- $k=n/m$ (P localization:473, (86)) and $\mu=n/m$ (P comparison:917, (66))
  name the same number; Section 5 writes $k=n/(n+1)$.
- The periodic index $r$ runs over $0\leq r<2n$ in $\Gamma^-$ (P
  localization:35), but over the second coordinate, $0\leq r<2m$, in the row
  sums $R_r$ of Section 4.2 (P comparison:621–623).
- $D_a$ is defined in (53) and restated as $D-10/n^2$ at P localization:374;
  the two agree [D], so this is redundancy, not a collision.
- $\widehat D,\widehat G,\widehat C_6,\widehat{\mathcal M}$ (P
  localization:448–449; C 1508–1509, p.128) are never defined; only
  $\widehat C_E(n,u)$ is named (P localization:438). [I] They are presumably the
  $u$-majorized $D_\phi,G_\phi,C_{6,\phi},\mathcal M_\phi$.
- Italic $e^{i(pu+qv)}$ (P corner:26) versus upright $\mathrm e$ in (53); the
  companion also uses $\mathrm i$ (C only comparison:965).

## 3. Constants reused without a reminder (Sections 4.3–4.6)

Reuse lines are paper `localization` lines; pages are paper/companion. Only
the block (75) cites its source, "Substitution into \eqref{uc:constants}" (P
localization:254; C 1012, p.120), and Section 4.5 recalls $b_0,r_0$ (P
:371–372; C 1308–1309, p.124) and $M(n)$ (P :490; C 1694, p.130). The
companion adds no further reminders at these sites [E: grep of the companion's
Section 4 for `uc:constants`, `recall`, `meanings in`].

| Constant | Defined (paper; companion) | Reused without reminder | Note |
|---|---|---|---|
| $T=(4L^2-3L)/\pi^2$ | comparison:536, (52), p.21; C 1492, p.71 | 268, 270 (p.37/120); 406–407 in (83) (p.39/125); 447, 459 (p.40/128); 494–495, 509 (p.41/131) | (75) only reminded |
| $\bar e=D+\mathcal M+1/n$ | comparison:541, (52); C 1497, p.71 | 269–270 (p.37/120); 406 in (83); 447 (p.40/128); 494–495, 509 (p.41/131) | in gates $G$, $\delta_A$, $\delta_D$ |
| $A_4$, $C_4$ | comparison:543, (52); C 1499 | 268 ($A_4$), 294, 324 (p.37–38/121–123); 494, 510 (p.41/131) | |
| $k_{Nx},k_{Ny},k_{Wx},k_{Wy}$ | comparison:547–550, (52); C 1503–1506 | 264–265 (p.37/120); 494, 511 (p.41/131) | |
| $U_N$ | comparison:551, (52); C 1507 | 267 (p.37/120) | |
| $J_N$, $d_\beta$ | comparison:545, 544, (52); C 1501, 1500 | 268, 265 (p.37/120) | |
| $D$, $\mathcal M$ | comparison:537–538, (52); C 1493–1494 | 374 ($D_a=D-10/n^2$, p.38/124); 448–449 as hats (p.40/128) | hats undefined |
| $K_D$ | comparison:542, (52); C 1498 | 399, 406–407, 413 (p.39/125–126); 447 (p.40/128); 495, 509 (p.41/131) | |
| $W_n$ | comparison:576, (53), p.22; C 1549, p.72 | 391, 413 (p.39/125–126); 449 (p.40/128) | |
| $\overline C_E$ | comparison:585, (54), p.22; C 1558 | 495, 510 (p.41/131) | |
| $j=H_0+d_0-g_0$ | comparison:309 (Lemma 4.3), p.18; C 924, p.63 | 261, 270 in/after (75) (p.37/120); 494–495 (p.41/131) | collides with index $j$ in (74) |
| $M_\infty$ | comparison:243, (38), p.17; C 724, p.60 | 399 (p.39/125) | |
| $M(n)$ | comparison:601, (56), p.22; C 1589, p.73 | 511, 524, 526 (p.41/131–132) | recalled at 490 |
| $E_c$, $I_4$ | comparison:325, (42); :479, (50); C 940, 1355 | 499, 504 (p.41/131) | |
| $L=\log n$, $H=1+L$ | comparison:4, p.14; C 28, p.51 | 253 (p.37/120); 382–390, 444 (p.38–40/124–128); 506, 519 (p.41/131) | 4.3 uses $L$ for a mesh |
| $u,x,y,a,p,q,P$ | comparison:8–13, p.14; C 32–37, p.51 | 290–324 (p.37–38); 353–367, 434–437 (p.38–40); 502 (p.41) | phase quantities of 4.1 |

## 4. Proposed renaming plan [I]

### 4.1 Convention

1. **Reserved global symbols:** $a=2/\pi$, $b$, $c$, $c_1$, $d$ of (3),
   $\kappa$ of (4), Euler's $\gamma$, $\pi$, $\mathrm e$, $\mathrm i$, Riemann
   $\zeta$, digamma $\psi$, $N=n+\tfrac12$, $m=n+1$, $\mathsf N=nm$,
   $\Lambda_n,\Lambda_c,\lambda_n$. They are never reused.
2. **Integer indices** $i,j,k,l,\ell,p,q,r,s$: summation, node, mode and row
   indices only, one meaning per proof; never constants or functions.
3. **Sizes:** $n,m,\mathsf N$; per-projection mesh sizes $\bar m,\bar n$.
4. **Angles and phases:** $\theta,\phi$ physical; $\alpha,\beta$ phases with
   $x=|\alpha|$, $y=|\beta|$, $\rho=x+y$; $u,v$ kernel arguments; $t$ a dummy
   or a local offset declared in its proof.
5. **Functions and kernels** reused across subsections are calligraphic
   ($\mathcal C,\mathcal B,\mathcal D_n,\mathcal N_n,\mathcal V,\mathcal W$);
   sans-serif lowercase is kept for the companion's local abbreviations.
6. **Constants:** one letter per role with a named subscript; an overline or
   bar marks a uniform majorant ($\overline C_E$, $\overline D_\phi$, and
   $\bar a,\bar w,\bar p,\bar P$ in 4.5); fraktur marks scalar constants of the
   comparison model ($\mathfrak T,\mathfrak j,\mathfrak k,\mathfrak k_0$,
   $\mathfrak e,\mathfrak f,\mathfrak g,\mathfrak p$), extending the paper's
   $\mathfrak a_p,\mathfrak b_q,\mathfrak d$.
7. **Small parameters:** bare $\epsilon$ only for the limit variable in (34)
   and (38); every other small parameter is $\varepsilon$ with a subscript or
   accent naming its role.

Each new name below was checked with `notation_scan.py --free` [E]: 0
occurrences as a token in either text (77 names, `free-check.tsv`). None
replaces a standard meaning; where the base letter exists, the new token is a
separate labelled family.

### 4.2 Companion-only renames (unnumbered prose; check_correspondence unaffected)

All sites lie outside the checked statement and display environments [E];
symbols absent from the paper cannot occur in numbered blocks, since those
blocks are identical in both texts.

| Old (companion line, page) | New | Reason |
|---|---|---|
| $R_n$ remainder, introduction:369–376 (p.7) | $\mathcal R_n$ | $R_n$ is also the kernel below |
| $R_n(z,B)$ corrected kernel, preliminaries:180–557 (p.12–18) | $\widetilde K_n(z,B)$ | it is $K_n$ corrected |
| indices $A=p+q$, $B=q-p$, corner:105–112 (p.21) | $i_1,i_2$ | $A(z)$, nodes, $B(x)$ |
| $P$, $Q$ (positive, negative sum), corner:353–355 (p.25) | $P_+$, $P_-$ | $Q$ square, $Q_{m,r}$ |
| $e$ (odd-$n$ indicator), corner:468–480 (p.27) | $\boldsymbol1_{n\text{ odd}}$ | the paper's own notation (corner:127) |
| $c=\cos u$, $c_i=\cos v_i$, corner:571–585 (p.29) | $\mathsf c$, $\mathsf c_i$ | $c$, $c_1$ of (3) |
| $S=\sum k^{-2}$, $S_o$, corner:1033–1036 (p.36) | $\zeta(2)$, $\zeta_{\rm odd}(2)$ | standard; $S_n$, $S_i$ |
| $L=\log m$, $c_v=\log(2/\pi)$, corner:1519–1533 (p.43) | $\mathsf L_m$, $\mathsf c_v$ | $L=\log n$, $L_n$ |
| $\kappa=8a_0/(3\pi)$ and $C=1+\kappa m$, localization:1421 (p.126) | $c_\Gamma$, $C_\Gamma$ | main constant $\kappa$ |
| $N=2M+1$, $\zeta=e^{2\pi\mathrm i/N}$, $w=e^{2\mathrm iz/N}$, comparison:965–977 (p.64) | $\mathsf K=2\mathsf k+1$, $\mathsf u$, $\mathsf w$ | $N$, Riemann $\zeta$, $w$ |
| $\psi_B$ hat function, preliminaries:52–58 (p.10) | $\mathsf h_B$ | digamma $\psi$ |
| $M_*:=2\varepsilon\cot e$, comparison:2305–2325 (p.84) | $\mathsf M_e$ | true norm $M_*$ of §5 |
| intervals $I_1,I_2$, comparison:2299–2316 (p.84) | $\Omega_1,\Omega_2$ | integrals $I_1,I_2$ of 3.3 |
| $E_j$ trapezoid error, corner:1487–1509 (p.42) | $\mathsf E_j$ | $E$ family |
| curvature bound $K$, certification:42–188 (p.134–136) | $M$ | Lemma 5.1 already uses $M$ |
| $D_*$ root, comparison:219–233 (p.53) | $\mathsf D_*$ | $D$ family |
| $H(g)=A_g(1-d/g)$, $d=\pi/L$, localization:676–700 (p.116) | $\mathsf A(g)$, $\mathsf d$ | $H$ family, $d$ |

### 4.3 Paper-wide renames (both texts together)

These change paper text, and most change numbered display blocks or
statement environments; the block columns are computed [E]
(`blocks_touched.py`; "paper lines" counts paper source lines holding the old
token in the stated scope). Apply each rename to the paper and to the
companion, including the companion's added prose, in one commit.

| Old → new (scope) | Clashes with | Numbered displays | Statements | Paper lines |
|---|---|---|---|---|
| model loss $T\to\mathfrak T$ (4.2–4.6) | Chebyshev $T_r$, $T_{n,r}$, $T_0$, $T_{\rm out}$ | 52, 75, 83 | none | 15 |
| $j\to\mathfrak j$ (4.1–4.6) | index $j$ in (59), (63), (74) | 40, 43, 49, 52, 75 | L 4.3 | 15 |
| $j_*\to\mathfrak j_*$ (4.5) | as above | 83 | none | 3 |
| $k\to\mathfrak k$ (4.1) | index $k$ in (32) | none | none | 5 |
| $k_0\to\mathfrak k_0$ (4.1) | as above | 35, 46 | none | 7 |
| $k=n/m\to\mu$ (4.6, §5) | synonym of $\mu$ in (66); index $k$ | 86, 90 | none | 11 |
| $H=1+L\to\bar L$ (4.1–4.6) | $H(w)$, $H_0$, $H_n$ in 4.1 | 52, 53, 68 | none | 22 |
| $C(v),D(v)\to C_-(v),C_+(v)$ (4.1–4.2) | coefficients $C,D$ of (29); allowance $D$ | 37 | none | 7 |
| $\mathcal H(L,v)\to\mathcal V(L,v)$ (4.1–4.2) | $\mathcal H_j$ (4.2), $\mathcal H_m$ (§3) | none | none | 3 |
| $W(t)$ of 4.1 $\to\mathcal W(t)$ | $W(t)=tw(t)$ of 3.3 | none | none | 6 |
| pole norm $B_n(t)\to\mathcal N_n(t)$ (4.2) | floor $B_n(r)$ of Lemma 4.6 | 61 | none | 2 |
| $(\ell_1,\ell_2,d_1,d_2)\to(\ell_x,\ell_y,d_x,d_y)$ (4.4) | $\ell_1(x,y)$ of 4.2; $d$ family | 77 | none | 5 |
| radial $(e,f,g)\to(\mathfrak e,\mathfrak f,\mathfrak g)$ (4.4) | $e$, $f$, $g$ elsewhere in §4 | 77 | none | 6 |
| $P(\rho)\to\mathfrak p(\rho)$ (4.4) | $P=p+q$ | 79 | none | 2 |
| $d_0,v_0$ of Lemma 4.3 $\to d_*,v_*$ | $d_0$ of 3.3; $v_0$ thrice | 40, 43, 45, 49 | L 4.3 | 8 |
| 4.5 bounds $a_0,w_0,p_0,P_0\to\bar a,\bar w,\bar p,\bar P$ | $a_0$ of 4.3, $P_0(z)$ of 4.2 | 82, 83 | none | 24 |
| band $[a_0,b_0]\to[b_-,b_+]$ (4.3) | $b_0=4/\pi^2$; §5 $a_0,b_0$ | 73 | none | 11 |
| $C=a_r-r/2\to A(0)$, $A_0\to A(b_-)$ (4.3) [D: $A(0)=C$, $A(a_0)=A_0$] | $C$ family | 73 | none | 8 |
| 4.3 lower bound $E_n\to B_n^\sharp$ | $E_n=S_n-M_\infty$ of (57) | none | none | 2 |
| $D_b=\sin\gamma\sin b\to w_b$ (4.3) | $D_b$ of 4.5 | none | none | 6 |
| meshes $(M,L)\to(\bar m,\bar n)$ (4.3 proof) | $L=\log n$; $M(n)$ | 72 | none | 24 |
| angle $\gamma\to\theta_c$ (4.3); $\gamma_b\to\lambda_b$ (4.5) | Euler $\gamma$ | none | none | 12 |
| radius $r\to\bar\rho$ in Lemma 4.6 ($a_{\bar\rho}$, $U_{\bar\rho}$, …) | periodic $(r,s)$ in the same proof | 70, 71 | L 4.6 | 34 |
| endpoint distance $s\to i$ (4.3 proof) | periodic $s$ in the same proof | none | none | 9 |
| gate $G,K,A\to\mathcal G,\mathcal K,\mathcal A$ (4.5) | chart $K$, $K_D$; $A$ family | 83 | none | 6 |
| $C=1+8a_0m/(3\pi)\to C_\Gamma$ (4.5) | $C$ family; companion $\kappa$ | none | none | 3 |
| $q_0=7/48\to q_h$ (4.6) | $q_0$ of 3.3 | none | none | 5 |
| $\epsilon,\ell$ of (53) and 4.5 $\to\hat\varepsilon,\hat\ell$ | second $\ell$ at comparison:1330 | 53 | none | 11 |
| $\epsilon,\ell$ at comparison:1330 $\to\varepsilon_h,\ell_h$ | as above | none | none | 4 |
| displacement $\varepsilon\to\varepsilon_d$ (comparison:266–275, 828–843) | limit $\epsilon$ in (34), (38) | 64 | none | 15 |
| $\epsilon=\min(t,\pi-t)\to e_t$ (comparison:378) | it is the separation $e$ | none | none | 2 |
| $f$ of (64) $\to\tilde g$ | scalar profile $f$ | 64 | none | 4 |
| $g=f''$ of Lemma 4.2 $\to f''$ | integrand $g(C,D;t)$ | 33 | L 4.2 | 7 |
| variation $V$ of (67) $\to V_F$ | $V$ family | 67 | none | 2 |
| §3: $D_n\to\mathcal D_n$, $(S,T)\to(u_+,u_-)$ | $D_{m,r}$; $T_r$, $T_{n,r}$, $S_n$ | none | none | 8 |
| §2–§3: $\epsilon_j\to\varepsilon_j$; $e^{i\cdot}\to\mathrm e^{\mathrm i\cdot}$ | glyph | none | none | 3 |
| optional: §3 $\alpha\to\alpha_r$ | phase $\alpha$ | 11, 19 | none | 9 |

**check_correspondence implications [D].** `companion-paper/check_correspondence.py`
(1) asserts that every tracked file under `paper/` is byte-identical to commit
`c6e195fa5211d4504fd2638f3c7686368e28daee`; (2) compares the companion's
headings, statement environments (theorem, lemma, proposition, corollary,
definition, remark, full text), numbered display environments, labels and
counter commands with that **frozen** paper; (3) with `--artifacts`, pins the
stored original PDF (640116 bytes, SHA-256 `07db8635…`) and compares built
label numbers. Hence:
- §4.2 renames keep it passing; they touch only unnumbered companion prose.
- Every §4.3 rename fails (1) at once and fails (2) for each listed block,
  even when both texts are renamed identically, because the reference is the
  frozen paper. A rebuilt paper PDF would also no longer match the pin in (3);
  label numbers are unaffected.
- So a coordinated rename needs AC's decision (the README records the original
  paper and PDF as intact). Either (a) move `BASELINE`, the PDF pin and the
  README/BUILD records to the post-rename commit, or (b) replace the
  byte-identity test by "frozen blocks plus declared renames equal the current
  blocks of both texts", which `notation_scan.py --baseline-rev …
  --rename-map …` checks (§5). Both change a checker: a material change that
  needs audit.
- Notation tables in the companion go in unnumbered `tabular` material, not in
  a `remark` (a checked statement environment) or a numbered display; in the
  paper they are a frozen-paper change like the renames.

### 4.4 Draft notation tables (state of names after §4.3)

**Section 3.** $m=n+1$; $\theta_j=j\pi/n$, $\phi_k=k\pi/m$; weights
$\varepsilon_j,\eta_k$. $a=2/\pi$, $d=\gamma+\log(8/\pi)$, $A(z)=a(\log z+d)$.

| Symbol | Meaning | Where |
|---|---|---|
| $f(u,v)$; $\mathcal D_n(u,v)$, $u_\pm$ | corner summand; diamond kernel and its half-angles | 3.1 |
| $w(x)$, $B(x)$ | $\cot(\pi x/2)$; cotangent with both poles removed | (9) |
| $x=r/m$, $s=m-r$, $\alpha$ | row variables ($1\le r<m$) | 3.1 |
| $T_{n,r}$, $V_n$, $D_{m,r}$, $\mathcal H_m$ | cotangent row sum, smooth part, digamma row, aggregate | (11)–(12) |
| $F_r$, $P_r$ | signed row entry, positive sum | 3.1 |
| $L_n$, $d_r$, $c_r$, $y_r$, $H_k$ | square reference, weights, cosecants, midpoints, harmonic numbers | 3.2 |
| $\ell$, $\sigma$, $t$, $h_{\sigma,\ell}$, $\Delta_n$, $M$ | offset, orientation, row position, local limit, defect sum, offset cutoff | 3.2 |
| $I_1,I_2,I_B$; $C_H,C_B,\beta_H,\beta_B$ | endpoint-regular integrals; constants of Prop. 3.2 | 3.3 |
| $e_r,u_r,S_e,S_u$; $d_0,q_0$; $F,J,R,v$ | endpoint sequences; Taylor constants; singular decomposition | 3.3 |
| $M_m$, $C_K$, $C_M$, $W$, $I(t)$, $F_B,G_B$ | logarithmic mean, constants, smooth-part functions | 3.3 |

**Section 4.1.** $m=n+1$, $L=\log n$, $\bar L=1+L$, $H_n=\sum_{j\le n}j^{-1}$.

| Symbol | Meaning | Where |
|---|---|---|
| $x,y,\rho,c_e,c_d,a,u,z,p,q,P,d_+$ | phase quantities ($a=c_ec_d$, $u=1-a$) | comparison:8–13 |
| $I(C,D,e)$, $J(v,s,e)$, $g(C,D;t)$, $R,E,Z$ | cancellation functional, its root form and remainders | (29)–(31) |
| $\mathcal C$, $C_0$, $\Phi$, $f$, $f''$, $J_0$ | reciprocal pair, profile, cusp atom | (32)–(33) |
| $H(w)$, $H_0$; $\mathfrak k,\mathfrak k_0$, $c_s$ | finite part and its maximum; series constants | (34)–(35) |
| $C_-(v),C_+(v)$, $\eta_\pm(v)$, $A(v)$, $\mathcal B(v)$, $\mathcal V(L,v)$ | row coefficients and profile | (37) |
| $U_0,B_0,D_0$; $M_\infty,b_{\rm full},E_\infty,C_\infty$ | completed model | (38) |
| $b_*,B,d_*,v_*,g_0,\mathfrak j,t_0$; $C_*,b_c$; $E_c$ | constants of Lemma 4.3; central term | (40)–(42) |
| $\mathfrak a_p,\mathfrak b_q,c_k,K$ | series for the certified $\kappa$ input | (48) |
| $b$, $B_\beta$, $I_4$, $F(v,a)$, $\tau$, $K(k)$ | Lemma 4.4 | (50)–(51) |

**Section 4.3.** Uses $a=c_ec_d$ and the phases of 4.1.

| Symbol | Meaning | Where |
|---|---|---|
| $\bar\rho$; $a_{\bar\rho}$, $U_{\bar\rho},V_{\bar\rho},W_{\bar\rho}$, $B_n(\bar\rho)$ | radius bound and floor ingredients | Lemma 4.6 |
| $\delta_n(\bar\rho)$; $p_\pi$, $\eta_{\bar\rho}$, $F_{\rm near},F_{\rm small},F_h,F_w$ | finite and tail floors | (70)–(71) |
| $\mathfrak d$, $Q_v,Q_h$, $Q$; $V_\pm$ | pair defect, projections, a projection value | (28), proof |
| $(\bar m,\bar n)$, $\theta_c$, $b=l\pi/\bar m$, $l$ | physical/periodic meshes, centre distance, physical row | proof |
| $i$, $q$, $w$; $\ell$ | endpoint distance, offsets, effective angle; arc length | proof |
| $A(u,v)$, $A_*$, $W$; $A_g$ | pair numerator, its floor, cosine span; correlated numerator | proof |
| $[b_-,b_+]$, $z_0$, $w_b$, $A(b)$, $f_b$, $c$, $\mathcal T_c$ | cosine band construction | (73) |
| $I$, $R$, $B_n^\sharp$ | band integrals; $\bar\rho=1/2$ bound | (73), proof |

**Section 5.** Uses $S_n$, $H_{rs}$, $\Gamma^-$, $\Delta_{JK}$ of Section 4.

| Symbol | Meaning | Where |
|---|---|---|
| $F=\max_\sigma f_\sigma$; $\omega_a,\omega_b$, $M$ | signed sums; frequencies; derivative bound | Lemma 5.1 |
| $R=[a_0,a_1]\times[b_0,b_1]$, $W_z$, $I_R$, $I_a,I_b$ | leaf rectangle, vertex uppers, bilinear interpolation | (88) |
| $L_\ell$, $c_{\ell,ij}$, $B_i^n$, $(s,t)$ | cardinals, Bernstein coefficients and basis | (89) |
| $L_c$, $w_*$, $D_R$ | validated lower endpoint; vertex weight; coefficient sum | 5.1 |
| $\mathcal T$, $(a,b)$, $\mu=n/(n+1)$, $f_\varepsilon$, $\varepsilon_{rs}$ | phase triangle, coordinates, ratio, signed sums | 5.2 |
| $q_R$, $V_R$, $\theta_R$; $M_*$, $E$, $V_E$ | leaf bound; true norm; quarter grid | (90)–(92) |
| $\delta_R$, $r_R$, $p_\pm$ | floor, certified radius, $\pi$ bracket | 5.2 |
| $U,V$, $W_x,W_y,W_{xy}$, $u',v'$, $q$, $c$, $g$; $A,B$ | corner witness; inward phases | 5.2 |

## 5. Verification recipe

`notation_scan.py` needs only python3 (standard library) and, for (c) against
a baseline, `git`. Copy it anywhere and run from the repository root:

```bash
python3 notation_scan.py --repo . --out /tmp/notation-out \
  [--paper-synctex PAPER.synctex.gz --companion-synctex COMPANION.synctex.gz] \
  [--baseline-rev c6e195fa5211d4504fd2638f3c7686368e28daee --rename-map renames.json] \
  [--free names.txt] [--symbol 'Q'] [--paper-dir DIR --companion-dir DIR]
```

- (a) `definitions-{paper,companion}.tsv`: every candidate definition site
  (base symbol, full token, unit, file, line, page, equation, right side);
  `symbols-*.tsv`: occurrences per unit and numbered equations per symbol;
  `numbered-*.tsv`: equations per full token.
- (b) `flags-*.txt`: tokens with more than one definition site in one unit,
  and base letters with several defined tokens in one unit.
- (c) block check: current paper against current companion (statements and
  numbered displays); with `--baseline-rev` and `--rename-map`, the baseline
  blocks after the declared renames must equal the current blocks of **both**
  texts. A rename map is a JSON list of `{"from": "B_n(t)", "to":
  "\\mathcal N_n(t)", "files": ["comparison-unified.tex"]}` (add `"regex":
  true` for a regular expression). Exit status 0 means every block check
  passed.
- (d) `summary.txt`; `--free` reports token, base-symbol and raw-text counts
  of proposed names in both texts.
- Page columns need a SyncTeX build: add `-synctex=1` to the existing
  pdflatex/latexmk command with a scratch output directory.

**Baseline on the head sources [E]:**

```text
paper: 3035 lines, 1817 math regions, 7337 symbol occurrences, 113 base symbols, 367 candidate definition sites; 18 (unit, token) pairs with >1 definition site; 60 (unit, base) pairs with >1 defined token; 61 base symbols defined in >1 unit; 92 numbered equations
companion: 10593 lines, 5832 math regions, 18991 symbol occurrences, 125 base symbols, 578 candidate definition sites; 67 (unit, token) pairs with >1 definition site; 89 (unit, base) pairs with >1 defined token; 68 base symbols defined in >1 unit; 92 numbered equations
PASS: current paper vs current companion: 13 statements, 90 numbered display blocks
PASS: numbered blocks equal baseline c6e195fa5211 after 0 declared renames (both texts)
```

Of the 18 paper flags, four join two different meanings in one unit: $\delta$ and $b$ in 4.1, $b$ in 4.2, $A$ in 4.3. The others are case splits or restatements of one object (for example $r$ in 3.2, where the case $r=n$ of $d_r$ is caught, $c$ in the two cases of the proof of Lemma 4.1, and $Q_0$, $s_L$, $s_R$, $q_\pm$ in 4.2). The 67 companion flags are in `flags-companion.txt`. The scanner's "base symbols defined in >1 unit" is a statistic of the heuristic, not the register count of §1.

**Self-test [E].** In a scratch copy, `B_n(t)` and `k_{Nx}` were renamed in
both texts. With the matching rename map both tests passed (exit 0). Without
the map, (c) failed and named exactly the changed blocks in both texts:
`uc:constants` (52), `uc:relative-comparison` (58), `uc:pole-error` (61),
`ul:near-base` (75) and the statement `uc:finite-bounds` (Proposition 4.5).
With the renames applied only in the companion, the current-versus-current
test failed on the same blocks.

**After renaming, Codex should check:** (b) shows no new
(unit, token) pair beyond the baseline flags; `--free` returns token count 0 for
any further new names before use; (c) passes with the full rename map; the
register rows of the renamed symbols reduce to one meaning per subsection; and
`check_correspondence.py` passes, or fails only in the ways §4.3 predicts until
AC decides the baseline question.

## Provenance

Scripts and outputs (scratch, not in the repository) under
`/tmp/claude-0/-home-user-padua-research/8833296e-cd9e-51d7-9205-e1ddfbc5960f/scratchpad/audit3/n-code/`:
- `notation_scan.py` — recipe script (a)–(d), `--free`, `--rename-map`;
- `make_register.py`, `loc.py`, `q.py` — register generation with needle
  checks, paper-to-companion line map, equation lookup;
- `make_constants.py`, `blocks_touched.py`, `where.py`, `eqcheck.py` —
  reuse search, numbered blocks per rename, grep with unit and page, equation
  number check against the auxiliary file;
- `synctex/{paper,companion}/main.synctex.gz` and `run.sh` — SyncTeX rebuild
  (48 and 162 pages) from the head sources;
- `out-baseline/` — baseline (a)–(d) and `free-check.tsv`; `out/` —
  register and block tables; `selftest/` — rename self-test copies and map;
  `proposed-names.txt` — the 75 checked names.
- Reference build used for page cross-checks: `audit3/build/` (page index,
  auxiliary files, pdftotext).
