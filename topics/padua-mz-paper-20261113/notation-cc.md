# Notation register and clash audit: MZ-CC manuscript

Source: `tracks/mz-constants/paper/manuscript.tex`, working tree = commit 767f5d7 (child of 604e667; the only difference
is the "Data and code availability" paragraph, l.1443-1459, +10 lines). Line numbers below are for the current file:
identical to 604e667 for l.<1443; for 604e667 subtract 10 from every number >=1453 (appendices).
No manuscript edits made. Sections (siamart numbering): 1 Intro l.66; 2 Prelim l.308; 3 Upper l.446; 4 Endpoint min l.649 (4.1 sharp constant l.862);
5 Edge max l.1017; 6 Consequences l.1114; 7 Fixed ratio l.1160; 8 Hyper l.1286; 9 Numerics l.1394; App A l.1462; App B l.1788; App C l.2031.
Severity: **H** harmful = same section/proof/appendix or same lemma-level statement; **M** moderate = adjacent sections or
a global symbol reused locally; **T** tolerable = separate local scopes.

## 1. Register

### Global (main text)
| Symbol | Meaning | Defined | Scope |
|---|---|---|---|
| N, n | node index (N+1 nodes); polynomial degree (Pi_n) | 94, 100 | global |
| theta_j, x_j | node angle j*pi/N; x_j=cos theta_j | 94 | global (theta_j also reused as generic angle) |
| w_j, ell_j | CC weight; cardinal polynomial in Pi_N | 96-98, (eq:weights) 321 | global |
| Q_N, Q | CC rule; generic rule | 96; 68 | global |
| mu; mu_k | measure (68, 1334); Chebyshev moments of dx (311) | 68; 311 | global; two meanings, differ by index |
| G, G_{N,n}, G_N | Gram matrix; G_N=G_{N,N-1} | 69, 100, 1116 | global |
| lambda_pm(N,n) | extreme Gram eigenvalues | 101-107 | global |
| lamin, lamax | macros lambda_min/max of a generic matrix | 18-19, used 73 | local to (eq:eta) |
| eta, eta_N | MZ defect ‖I-G‖_2; eta_N for n=N-1 | 72; 45, 163 | global |
| d_N | max algebraic degree of exactness | 111 | global |
| rho_{N,n}, rho | (max{2n/N-1,0})^2 | 123; 498; 541 | global |
| Lambda_edge | squared norm of endpoint operator | 1052 | global |
| kappa_2 | 2-norm condition number | 167 (never defined) | global |
| calI_N | interpolation operator at N+1 nodes | 218; redefined 965, 1468 | global (3 definitions) |
| T_k, U_k | Chebyshev 1st/2nd kind | 310; 729, 773 | global |
| gamma_j | half-weights 1/2,1,..,1,1/2 | 320 | global |
| M, R, D | Chebyshev mass; discrete mass; defect D=2(M-R) | 336-342 | global (index range 0..n or 0..N-1) |
| E | diag(2,1,...,1) | 375 (used 596, 623) | Sec 2-3 |
| m_j | weight floor 1+min(j,N-j) | 417 | Sec 2, used 689-719 |
| S_N(theta) | bracket of eq:weights, w_j=2 S_N(theta_j)/N | 429 (reused 1843-1846) | Sec 2 lemma proof, App B |
| Y, Z | reflected / transition matrices, R=M-Y+Z | 557-566 | Sec 3, App B (M_N,R_N,Y_N,Z_N 1793) |
| beta_N, u_N | excess bound; even integer N or N+1 | 603; 586 | local to Thm five-thirds |
| H_s | harmonic number | 651 | global |
| h_N, K_N | 2H_{N+1}-1; cardinal constant | 653-654 | global (K_N in 143, 1124) |
| S_N | sum_{j<=N} 1/(2j-1) | 734 | Sec 4 (Lemma U-exact); Sec 8 (Prop counterexample 1303-1316) |
| q_N | upper bound of lambda_-(N,N-1) | 741 | local |
| V (Volterra) | (Vf)(x)=int_0^x f | 881 | Sec 4.1, 920, App A 1560, 1700 |
| J, k_0, alpha_J, sigma_N, tau_N | floor(N/2); ceil(L^2); 2H_J/pi+1; constants | 933-936 | Thm sharp-min, App A |
| Phi_k, calE | signed-remainder kernel and operator | 992-993 | Sec 4.1 and App A |
| sf M, sf D, omega_j | model mass; model energy; weights 2[(-1)^j+pi j Si(pi j)] | 1029-1034 | Sec 5, App B/C |
| calV_0, zeta_j, chi_j | span of zeta_j; 2[cos(pi j s)-(-1)^j]; its cosine transform | 1036-1040 | Sec 5, App B/C |
| p_{N,j} | ell_j-2(-1)^j ell_0 in Pi_{N-1} | 1058 | Sec 5, App B |
| C_0, C_* | 2(1+pi)^2; 3C_0^2(1+2/pi) | 170, 1170-1171 | global (C_* in 171) |
| V (mass), B, B_{N,n}, calL_n, E_k(f) | total mass; upper Gram constant; its CC value; hyperinterpolant; best approximation | 1333-1345, 1370 | Sec 8 (calL_n, E_k(f) already in 173-174) |

### Local, main text
| Symbol | Meaning | Defined | Scope |
|---|---|---|---|
| A (=2M-R), A_rho | sign matrices (A=A_{rho=1}) | 464; 499 | Thm 3.1 / 3.2 proofs |
| delta, d, r, s | N-n; i-j|; 2N-s; i+j | 502-503, 466, 366 | Sec 2-3 proofs |
| b_i, m_i, k_i | row-sum vector (1/2,1,..); least integer >=N of parity i; m_i-1 | 381-383 | Lemma floor |
| A_{jk}, B_{jk}, u_j, D_0, E_j | (1+|j-k|)^-1; weighted A; m_j^{-1/2}; 2(pi+1); cells | 694; 688; 686 | Thm cardinal proof |
| c_k | 2 at k=0,N else 1 (=1/gamma_k) | 673; 1465 | Thm cardinal, App A |
| M_0, p_N, B(th), A(th), C(th), K, E, I, J, L | floor((N-1)/2); witness; sine/cosine sums; floor(1/sin th); [N^{-1/2},1/4]; integrals; log N | 774-831 | Thm harmonic proof |
| a_k, u_k | nodal amplitude (-1)^k u_k; nodal data | 868 | Sec 4.1 (l.867-871), App A |
| F_m, K(t), eps, nu, t_j, q, z_j, H(t,j), R, S | Fejer; filter; 1-n/N; |sin t|+1/N; j*pi/N; p(cos t); weighted data; kernel; row/col constants | 1180-1235 | Thm 7.1 proof |
| A_theta, rho_theta, eta_theta, theta | strong lower bound; (2theta-1)_+^2; max{1-A,rho}; degree ratio | 1262-1266; 169-171 | Cor strong; Cor intro (2) |
| c_i, p_a, P_i, d | Q(fP_i); sum a_i P_i; basis; dim Pi_n | 1335, 1349-1350 | Prop hyper |
| m, k | An-Wu point count; reproduction degree in E_k | 114, 1291, 1299; 1341-1345 | Sec 1, 8 |

### Appendices
| Symbol | Meaning | Defined | Scope |
|---|---|---|---|
| L, theta_k, d_k, c_k | log N; k*pi/N; min(k,N-k); endpoint factors | 1464-1465 | App A |
| u, a_k, ‖u‖_w, ‖g‖_h, g_k, g^flat_k | nodal data; (-1)^k u_k; sqrt(sum w|u|^2); harmonic norm; k a_k/N, k a_{N-k}/N | 1468-1473, 1602-1603 | App A |
| sinc, delta=2^j, I_j, calJ_j, calK(t,k), Psi_k | normalized sinc; dyadic scales; kernel k Phi_k(t) | 1477, 1496-1502, 1533 | proof of signed remainder |
| H_0, f, F, S_m, Z | step f=g_m; F=int f; S_m=sum_{k<=m} g_k/k; step version of S_m | 1558-1560 | proof of discrete primitive |
| S(t), S^flat, P_u, Y_u, e(z), ell | partial sums; polynomial model; pole part; cot(z/2)-2/z; floor(N/L) | 1604-1607, 1596-1597, 1629, 1601, 1680, 1733 | Lemma endpoint-rep, Prop trial, finite bound |
| a, b (support), delta, I_delta, C_f | 0<a<b<1; small param; N^delta..N^{1-delta}; constant | 1678, 1701-1702, 1700 | proof of Prop trial |
| sinc_1, a_j=pi j, xi, varrho_{N,j} | sin z/z; pi j; N theta; exact factor | 1790-1792, 1815 | App B |
| calV, sf Y, sf Z, z(v), G(s) | form domain; Laplace/transition forms; kernel; even extension | 1879-1884, 1892 | App B |
| a_i, a, e_N, o_N, g_N^pm, E^e_N, E^o_N, Lambda^* | coefficients; maximizer coefficients; even/odd profiles; Laplace profiles; subsequential limit | 1928, 1962-1969, 2005-2011, 1959 | App B |
| s_j, Cin, calH, I(a), K(a), C_{ij}, D, C, q(u), J | (-1)^j; model Gram; D=diag(omega)+4ss^T; C=(C_ij); quotient; J=512 | 2035-2087 | App C |

## 2. Clash list

Format: symbol | meanings with lines | class | minimal rename (checked against the register; new letters are unused anywhere in the file:
vartheta, varpi, Gamma, Xi, Omega, Theta, Upsilon, W, X, calA/calB/calC, sf Q, k^*, N_e, sigma_pm, hat f).

### Harmful (H)
| # | Symbol | Occurrences | Proposal |
|---|---|---|---|
| H1 | theta | ratio theta in Cor intro (2) 169-170 and Cor strong 1262-1278 (also A_theta, rho_theta, eta_theta); angle theta=pi t/N, theta=xi/N in Methods 185, 190, and theta_j 94, 1022, all of Secs 2-5. Same Section 1: 169-170 vs 185, 190 | rename ratio to vartheta (so A_vartheta, rho_vartheta, eta_vartheta); ~12 lines |
| H2 | a (Prop sharp-trial proof) | support endpoints 0<a<b<1 and exponents N^a, N^b, N^-a (1678-1680, 1688, 1700) vs a_k=(-1)^k u_k (1468, 1681) in the same proof | support (sigma_-,sigma_+); N^{sigma_-}, N^{sigma_+} |
| H3 | a in App B/C | a_j=pi j (1792, 1826, 1866-1869, 2035, 2067) vs Chebyshev coefficients a_i (1928) and maximizer vector a=a^(N) (1962-2013) in the same appendix; also bare a=a_i, b=a_j, "integer multiple" (2051-2067) | a_j -> varpi_j (and a,b -> varpi_i, varpi_j in App C); a_i, a stay |
| H4 | K (Sec 4) | K_N (654) vs K=floor(1/sin theta) (794-802) in the same section; 571 reads "M-R, H and K" (stale names, see H5) | K -> nu_theta (floor(1/sin theta)) |
| H5 | H, K at l.571 | "every entry of M-R, H and K vanishes": H, K are undefined leftovers; should be Y and Z (also H_s l.651, H(t,j) 1218 would be a further clash) | change to "M-R, Y and Z" |
| H6 | S_N | S_N(theta) weight bracket (429-438, reused 1843-1846 with theta_j) vs S_N=sum_{j<=N}1/(2j-1) (734-758, S_8, S_57, S_58, S_512 at 753-755, 1303-1316): same symbol with and without argument in two lemma-level statements; also S_m (1560-1578) in App A | bracket -> W_N(theta) (w_j=2 gamma_j W_N(theta_j)/N; ~6 lines); S_N odd sum stays |
| H7 | D / sf D | defect D=2(M-R) (340-343, 449-637, entrywise >=0); model energy sf D(g)=|ghat(0)|^2+... (1034, 1046, 1053, 1071, 1095, 1105, App B 1854-1950, App C) which is the limit of N^2 Q_N(p^2)=a^T R a (the R-form, not the D-form); App C matrix D=diag(omega)+4ss^T (2084); D_0 (688). Reader will pair sf D with D | sf D -> sf Q (energy; ~40 occurrences); App C D -> sf Q_J; D_0 -> C_c |
| H8 | A, B, C in Sec 4 | A_{jk}, B_{jk} (694-719) in Thm cardinal; A(theta), B(theta), C(theta) (783-811) in the immediately following Thm harmonic proof; both fill the same section | harmonic sums -> calA, calB, calC (~12 lines) |
| H9 | m | m_i (382-395, Lemma floor: least integer >=N with parity of i) vs m_j=1+min(j,N-j) (417, 442, 689-719) in the next lemma, same section | m_i -> N_i (k_i=N_i-1) |
| H10 | a_k (Sec 3 vs 4.1) | Chebyshev coefficients a_i (472, 498-515, 552, 596) vs nodal amplitude a_k=(-1)^k u_k (868, 1468, App A passim): adjacent sections | rename nodal amplitude to tilde u_k (~20 lines in App A) or accept and say so at 868; Sec 3 vectors stay |

### Moderate (M)
| # | Symbol | Occurrences | Proposal |
|---|---|---|---|
| M1 | E | diag(2,1,..) 375, 596, 623; cells E_j 686, 689; interval E=[N^-1/2,1/4] 825-842; calE 993, 1004+; E^e_N, E^o_N 2005-2011; E_k(f) 174, 1292, 1345 | cells E_j -> Omega_j; interval -> Xi; E^{e,o}_N -> Theta^{e,o}_N; keep diag E, calE, E_k(f) |
| M2 | V | Volterra V 881-920, 1015, 1560, 1700; mass V 1292, 1333-1367, 1385-1386; form domain calV 1879-1892, core calV_0 1036-1096 | mass V -> |mu| (CC: |mu|=2) |
| M3 | B | B in Prop hyper (1336-1344), B_{N,n} (1370-1378, 123-125 as bound), B(theta) 783, B_{jk} 694-706 | hyper constant -> overline lambda, overline lambda_{N,n} (after H8 only B_{jk} remains) |
| M4 | J | J integral 831; J=floor(N/2) 933-953, 1002; model truncation J (1044-1048, 1067, 2071, 2087 J=512); calJ_j 1497 | integrals I,J -> X_1,X_2 (also frees I vs identity I); model truncation J -> sf J |
| M5 | ell | ell_j cardinal 98, 354, 670-688, 1058-1060, 1802-1803, 1926 vs ell=floor(N/L) in App A 1601-1603, 1642-1657, 1680, 1733-1737, 1773 | ell=floor(N/L) -> k^* (pairs with k_0; k_i in Lemma floor 383 is a different, Sec 2 local) |
| M6 | d | d_N ADE 111, 1375; d_k=min(k,N-k) 1465, 1591, 1621-1622, 1737, 1756, 1778 (d_N would be min(N,0)); d=|i-j| 466-510; d(t,s) 1178-1215; d=dim Pi_n 1335 | d_N -> d^ex_N (two lines); others local |
| M7 | Y, Z, S (App A vs Sec 3/App B) | Y_u(t), Y_{u^l}(t), Y_{u^r}(t) 1596-1661, Z step function 1560-1563, vs matrices Y, Z 557-566, 1793, forms sf Y, sf Z 1881-1949 | Y_u -> Upsilon_u; step Z -> bar S |
| M8 | p_N | witness p_N 776-849 (Thm harmonic); trial interpolant p_N 912-927, 1685+; maximizer p_N 1963-1968; p_{N,j} 1058; p_a 1350 | witness -> p^H_N |
| M9 | R, S (constants) | R,S Schur bounds 708-711; R,S rowH/colH 1231, 1235-1243 vs matrix R 339-340, cutoff R 1490-1498, 2057-2071, S_N, S(t) | Gamma_r, Gamma_c in both places |
| M10 | c | c_k endpoint factor 673, 1465 (=1/gamma_k, reciprocal of 320); c_i=Q(fP_i), vector c 1349-1355; absolute c>0 665 | drop c_k, write gamma_k^{-1}; c_i -> hat f_i |
| M11 | t | t=2n/N-1 (498-516) vs t=N theta/pi (679-692, 867-871, App A) vs circle angle t, t_j=j pi/N (1178-1253; t_j=theta_j, but elsewhere node k has t=k) vs integration variable in App C | Thm 3.2: eliminate t (sqrt rho); Thm 7.1: t,t_j -> theta, theta_j |
| M12 | rho vs varrho | rho_{N,n}, rho 123-125, 498-541, rho_theta 1265 vs varrho_{N,j}(xi) 1815-1831: near-identical glyphs | varrho_{N,j} -> varphi_{N,j} (rename dummy phi 1631-1635) |
| M13 | M, C (misc) | M_0 774-809; Mastroianni-Totik constant M 278-283; sf M 1029+; C_{ij}, C=(C_ij) 2039-2086 (model Gram of sf M); C(theta) 785; C_f 1700; generic C 1872-1873; C^1, C^2; C_l 285 | C_{ij} -> sf M_{ij}; C(theta) via H8; rest tolerable |
| M14 | K (other) | K(t) filter 1191-1218; calK(t,k) 1533-1549; K(a) 2055-2076 (+ K_N, K=...) | rename App C K(a) -> calK_0(a) optional; K(t) tolerable after H4 |
| M15 | mu | measure 68, 1334, 1357 vs mu_k moments 311-338 | tolerable (index distinguishes) |

### Tolerable (T)
| # | Symbol | Occurrences |
|---|---|---|
| T1 | eta | generic eta 72, eta_N 163, eta_theta 1266, An-Wu eta=3/4 1289-1297 |
| T2 | F | Fejer F_m 1186-1205; F=Vf 890-900, 1560, 1700; F(x) 1849 and 2108 |
| T3 | e | Euler number 1309; e(z) 1629; e_N 1967; e^{...} exponentials |
| T4 | alpha | alpha=pi/2 in Lemma Volterra proof 890-901; alpha_J 934, 1002; alpha=1/2 (Jacobi) 249 |
| T5 | delta | Kronecker 349, 1043; N-n 502; 2^j 1496; small parameter 1701; Cor |
| T6 | gamma | gamma_j 320, 1926; Euler gamma 2119 |
| T7 | zeta | zeta_j 1037; Riemann zeta(3/2) 1577 |
| T8 | h | h_N 653; sum index h 391, 1187, 1491; h_k 1481; h 1908 |
| T9 | n, k, T | n=ceil(2t) 1542, n<16 2088 vs degree n; k reproduction degree vs index; T cutoff (1002, 1747, 1983) vs T_k |
| T10 | q, g, G, z, P, p | q_N 741 / q(t) 1180 / q(u) 2083 / q upper limit 359; g_k vs g in L^2(0,1); G(s) 1892; z=pi k/N 1741 vs e(z); P_i 69, P_u 1607; polynomial p vs exponent p=2 (245-267) |
| T11 | L, lambda | L=log N vs L^2 space (950-955); lambda_pm vs lamin/lamax (73) |
| T13 | u | u_N=N or N+1 and even integer u 586-594 (Sec 3, proposal N_e); nodal data u_k 141, 965, App A; coefficient vector u 1044-1048, 2071; u=1-i/N 1934 |
| T12 | nu, Delta_N | nu(t)=|sin t|+1/N (1180) is N*Delta_N(cos t) from 226: duplicated notation, no clash |

### Status of the plan's table (review-plan-cc.md (e))
Resolved in current text: S_N(theta) vs S_N (still H6, same name), eps=2/L^2 (no longer present; epsilon has one meaning 1180),
L_N, K=ceil(L^2) (now k_0), A_J (now alpha_J), t scale in App B (now xi), c_0=c_N=1/2 (all uses are 2), lambda_min/max in text (only (eq:eta)).
Still open: S, E, V, A, B, C, D, K, H, F, theta, J, a, d, m, R, plus new: Y_u/Z in App A (M7), p_N (M8), ell (M5), varrho (M12).

## 3. Symbols used before definition
| Symbol | Use | Definition | Remark |
|---|---|---|---|
| kappa_2 | 167, 1131, 1145 | none | standard condition number; add "(2-norm condition number)" |
| u_k, nodal data | 141-142 (Thm intro-min), 223 | 965 (Cor), 1457-1459 (App A) | state "u_k=p(x_k)" |
| calL_n, E_k(f), k | 173-174 (Cor intro (3)) | 1338, 1345 | add inline definition or pointer |
| K_N, Lambda_edge | 143-144; 42, 151 | 654; 1052 | explicit pointers (eq:KN, eq:Lambda-edge): acceptable |
| rho | 484-485 (proof of Thm 3.1) | 498 (Thm ratio-upper); rho_{N,n} 123 | forward to the next theorem; says "see Theorem" at 482 |
| calV (form domain) | 1096 (closure of calV_0 only) | 1879 | no forward use of calV itself |
| calI_N | 218 | redefined 965, 1468 | consistent, three definitions |
| theta=pi t/N, t | 185 | no definition of t in Section 1 | methods paragraph; fine |
| Y, Z | 1089-1095 (Sec 5) | 557-566 (Sec 3) | backward |
| H, K (stale) | 571 | none | defect (H5) |

## 4. Counts
- Register: 34 global rows + 11 local-main rows + 10 appendix rows = 55 rows, about 190 distinct symbols/variants (rows bundle related symbols).
- Clashes: 10 harmful (H1-H10, of which H5 is a stale-name defect), 15 moderate (M1-M15), 13 tolerable (T1-T13): 38 entries, covering about 55 distinct letters.
- Forward uses: 3 real (kappa_2, u_k, calL_n/E_k(f)), 1 stale (H,K at 571), 4 acceptable.
- Free symbols used in proposals (all unused in the file): vartheta, varpi, Gamma_r/c, Xi, Omega, Theta, Upsilon, W, X_1/X_2, calA/B/C, sf Q, sf J, k^*, N_e (for u_N), sigma_pm, hat f, d^ex.
- Proposal conflicts checked: each new symbol appears once in the allocation; Gamma (not used for E), W only for the bracket, Xi only for the interval.
