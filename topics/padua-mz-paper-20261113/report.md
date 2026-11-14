# MZ-CC and MZ-SP: topic report for AC

Branch `claude/padua-mz-paper-20261113`, draft PR #35, base `b5388c2`, head `a0206a8` at the time of writing (2026-11-14). Written by Claude Sonnet 5.5 (documentation developer) from the topic records. Day-to-day history is in the [LOG](LOG.md); nothing here is an audit statement. **The Codex audit of both papers is pending.** Nothing is submitted.

## 1. What was done

AC split the 2026-11-05 draft into two papers (2026-11-13) and chose venues. The orchestrator integrated the PR #31 results (PD-T522–T548) and the literature of PR #21, rewrote both introductions around exact constants, ran notation and literature scope passes, and ran two internal referee rounds per paper (mathematics Opus 5.5 xhigh: no CRITICAL or MAJOR finding in either paper, both certificates rerun bit-identically; exposition Opus 5.5 high). Both papers are complete internal drafts with frozen statement numbering (checked against the compiled `.aux` on 2026-11-14: 52 and 56 labels, no mismatch). Fresh builds are clean; hashes are in the [manuscript record](../mz-constants/directions/M7/manuscript-record.md). The scope tables are in the two READMEs ([MZ-CC](../../tracks/mz-constants/paper/README.md), [MZ-SP](../../tracks/mz-constants/paper-sp/README.md)).

## 2. The two papers

| | MZ-CC | MZ-SP |
|---|---|---|
| Title | *Marcinkiewicz–Zygmund constants of Clenshaw–Curtis quadrature beyond half-exactness* | *Marcinkiewicz–Zygmund constants of signed Padua rules beyond half-exactness* |
| Venue (AC) | SIAM J. Numer. Anal. (fallback Math. Comp.) | J. Approx. Theory (fallback Adv. Comput. Math.) |
| Class, pages | `siamart251216` (SIAM macros from public copies; replace by the official download), 32 pp. | `elsarticle` preprint, 12 pt, A4, 50 pp. |
| Order | first on arXiv | second; cites MZ-CC for three CC inputs |

**MZ-CC, main results (all PROVED at the stated scope).** For n < N all eigenvalues of G_{N,n} lie in (0, min{1+ρ, 5/3}] (the 5/3 is uniform in N and not claimed sharp), while λ₊(N,N) > 2. At n = N−1 and n = N: (log N)²λ₋ → π⁴/8 through all integers N (closes PD-T020), so interpolation from CC-weighted data to L² has norm (2√2/π² + o(1)) log N. λ₊(N,N−1) → Λ_edge ∈ [1, 3/2], the squared norm of an explicit endpoint operator, with Λ_edge ≥ 1.0044369 **computer-assisted and one-sided**. Consequences: 1−η_N = λ₋ for N ≥ 57, (log N)²(1−η_N) → π⁴/8, κ₂/(log N)² → 8Λ_edge/π⁴. Explicit strong constants at every fixed ratio below one, and a hyperinterpolation factor (1+√(5/3))√2. Open: the decimal value of Λ_edge, usable rates, identification of the operator. PD-T531 is omitted; Table 1 and the J-Galerkin proxy are MEASURED.

**MZ-SP, main results (all PROVED at the stated scope).** The first-coordinate marginal of any exact rule on the Padua points is twice the CC rule, which bounds the extremes by the CC ones. For every fixed τ ∈ (1/2, 1) the extreme eigenvalues diverge (sharp threshold, all integers m, by signed weight asymptotics and carriers). At n = m−1, λ^P_±/log m → c_±, the extremes of the spectrum of an explicit compact elliptic-integral operator B; c₋ = −‖B‖ is simple and 0 < c₊ < ‖B‖. A **computer-assisted** enclosure puts ‖B‖ in [0.0131, 0.478] and fixes no digit; analytic lower bounds ‖B‖ ≥ 0.02964, c₊ ≥ 0.01278. The direct signed coefficient operator has C→L² norm below 30 uniformly. Computer-assisted: certified spectral brackets at m = 10…80, and negative trial quotients at m = 1101, 1240, 1600 (no first crossing; trial quotients are not eigenvalue brackets). Open: decimals of c_±, first sign change, effective onsets, sharp norm of H_{m,n}.

## 3. New provisional claims (two records, flagged for the audit)

- **PD-T?mz-paper-claude-01** ([record](theory/cc-defect-condition-corollary.md); checks [1](check-cc-defect-corollary.md), [2](check-new-corollaries-02.md), PASS with corrections applied). (a) 1−η_N = λ₋(N,N−1) for every N ≥ 57 and (log N)²(1−η_N) → π⁴/8; (b) κ₂(G_N)/(log N)² → 8Λ_edge/π⁴, the numerical interval inheriting the computer-assisted PD-T547; (c) hyperinterpolation factor with B = min{1+ρ, 5/3}; (d) ‖𝓘_N‖ = λ₋(N,N)^{−1/2}, ‖𝓘_N‖/log N → 2√2/π². All are short consequences of PD-T017/019/022/025/526/527/530/546/547. Appears in MZ-CC as Lem 4.2 (N ≥ 57 part), Cor 4.7, Cor 6.1, eq. (8.3).
- **PD-T?mz-paper-claude-02** ([record](theory/sp-corner-norm-lower.md); check PASS). ‖B‖ = −c₋ ≥ c_new ≈ 0.0296418 and c₊ ≥ 0.0127789 (analytic, from PD-T533/379 with PD-T536/540). Appears in MZ-SP as Cor 6.10.

Other items for the audit, from the responses: the PD-T523 proof-route change (MZ-CC Prop 4.5 via Lem A.1(c)); Lemma 2.4 (Schur test, unregistered); the statement of PD-T529 weakened; PD-T539 weakened (MZ-SP Prop 6.6); the explicit bound (2+C_P)E_k(f) in MZ-SP Rem 7.2 and "η < 0.83" in Prop 8.1 (arithmetic not stated in any record); tighter constants inside the PD-T534 proof. Final IDs for the two provisional claims are to be reserved at PR preparation by the WORKFLOW procedure; none was reserved here.

## 4. Declined strengthenings (candidates, not in the papers)

- **MZ-CC, 23/15 (referee F2).** Observation: β_N ≤ 8/15 for N ≥ 3 (maximum at N = 4) and λ₊(2,1) = 1, hence sup_N λ₊(N,N−1) ≤ 23/15, and with min{1+ρ, 1+β_N} for N ≤ 8 even 95/63. It would improve 1/3 to 7/15 in Cor 6.1, the hyperinterpolation factor to 1+√(23/15) < 2.2385, and the ratio threshold to (1+√(8/15))/2. Declined as unregistered; needs a theory record and an independent check before use.
- **MZ-SP, Θ(log m) at fixed ratio (referee B6).** Claim: |λ^P_±(m,⌊τm⌋)| ≍ log m for every fixed τ ∈ (1/2, 1). Sketch: carriers of Prop 5.6 with a+b small have degree below τm, which gives the lower bound; the upper bound |λ^P_±(m,n)| ≤ 120 log R + 4096 for n < m follows from Thm 6.1 by restriction. Declined as unregistered. The related question (does λ^P_±(m,⌊τm⌋)/log m converge, presumably to the extremes of an analogous operator on {a+b ≤ τ}?) could then join Section 9.

Also declined, available if you want shorter or different text: shortening Appendix A.2 Step 1 of MZ-SP (about 0.8 page) and demoting its Prop 5.8 (about 0.4 page); moving a prior-ingredients passage of MZ-CC §1 to §8; a Halmos/HLP citation for ‖V‖ = 2/π (no verified pinpoint on file).

## 5. Open questions for AC

**Order.** arXiv MZ-CC first, then MZ-SP (your 2026-11-13 decision). Then put the MZ-CC arXiv identifier into MZ-SP's `refs.bib` (`MZ-CC` entry) and check the `MZ-SP` entry of MZ-CC's `refs.bib` (companion citation).

**Placeholders only you can fill** (agents did not touch them): authors, affiliations and `\thanks`, keywords and MSC (MZ-CC: 65D32, 41A17, 41A10, 65F35, suggested additions 41A05, 42C05; MZ-SP: 47B38, 65G20 added, please confirm), funding, CRediT, AI declaration, ORCID, `\date`, commit hash and Zenodo DOI in both availability statements (and "DOI to be added" after MZ-SP Prop 8.2). Confirm that `github.com/aacchhee/padua_research` is public, or give only the DOI. Before arXiv: remove the `% IDs:` and `% Source:` TeX comments (they are public and three in MZ-CC and one in MZ-SP carry provisional IDs); replace SIAM's class copies by the official macros.

**Unread sources that the referees wanted cited** (not cited, not in the bib; read them if you want the sentences they support):
- Caliari–De Marchi–Vianello 2005 (origin of the Padua points): [10.1016/j.amc.2004.07.001](https://doi.org/10.1016/j.amc.2004.07.001), [free PDF](https://profs.scienze.univr.it/caliari/pdf/CDMV05.pdf).
- Sloan 1995 (hyperinterpolation): [10.1006/jath.1995.1119](https://doi.org/10.1006/jath.1995.1119).
- Bos–De Marchi–Vianello–Xu 2007: [arXiv:math/0604604](https://arxiv.org/abs/math/0604604); DOI to verify (probably 10.1007/s00211-007-0112-z).
- Caliari–De Marchi–Vianello 2008: [10.1016/j.cam.2007.10.027](https://doi.org/10.1016/j.cam.2007.10.027).
- Padua2DM software paper: [preprint](https://profs.scienze.univr.it/caliari/pdf/preCDMSV09.pdf).
- Erb 2016 (source of KLP's L^p inequalities): [arXiv:1503.00895](https://arxiv.org/abs/1503.00895).
- An–Ran–Wu survey (LIT-387; do not cite as saying the signed case is open or closed): [10.25430/pupj-DRNA-2025-1-11](https://doi.org/10.25430/pupj-DRNA-2025-1-11).
- ASV 2027 published PDF (in your papers folder; equations (7)–(8) already confirmed): which rule is their Padua rule and the page locator; if it is Q^P_m, drop the "If that rule is…" conditional in MZ-SP §8.1 ([10.1016/j.matcom.2026.10.001](https://doi.org/10.1016/j.matcom.2026.10.001)).
- Classical, optional: Szegő Thm 8.1.1, [DLMF 18.11](https://dlmf.nist.gov/18.11), [DLMF 10.9](https://dlmf.nist.gov/10.9) (Mehler–Heine, Laplace and Poisson integrals); Reed–Simon IV §XIII.12 (Jentzsch/Krein–Rutman); Bhatia, *Matrix Analysis*, X.1.
- MZ-CC, optional: Nevai 1984 Thm 6 page image ([10.1090/S0002-9947-1984-0732113-4](https://doi.org/10.1090/S0002-9947-1984-0732113-4)); König–Nielsen journal body ([10.1515/form.1994.6.183](https://doi.org/10.1515/form.1994.6.183)); Feldheim 1937 expansion ([10.24033/bsmf.1260](https://doi.org/10.24033/bsmf.1260)), no longer needed after the rewording.

**Checked in your papers folder (2026-11-14).** None of the unread sources above is in `Downloads\padua\papers`. The orchestrator extracted the first page of every PDF there (48 files, plus a thesis it did not open); two scanned JAT files were identified as Xu's "Mean convergence … I/II". So the list above still needs fetching.

**DOI and bibliographic checks** (the sandbox could not reach Crossref): BCDMVX06 [10.1016/j.jat.2006.03.008](https://doi.org/10.1016/j.jat.2006.03.008) is now confirmed from the DOI printed on the journal PDF in your folder. For Xu96 [10.1006/jath.1996.0102](https://doi.org/10.1006/jath.1996.0102), the journal PDF in your folder prints "article no. 0102" in JAT 87; this is consistent with the DOI, which is still not resolver-checked; LIT-056 DOI 10.1137/120869845 came from a web search and is not yet in its LIT record; confirm "252 (2027)" for the ASV entry (LIT-045, which should also note that (7) and (8) are the same in the published PDF and arXiv v1); the editor, series and Kluwer imprint of LIT-052 are unverified.

**Not done.** Companions (BRIEF §5 item 3) wait for the audit and the freeze. Since this report was drafted, the orchestrator has filled the MZ-SP part of [literature-mz-paper.md](literature-mz-paper.md) from the exposition referee's per-citation check, and fixed the duplicated phrase in MZ-SP's proof of Prop 8.1. The ASV published equation numbering is confirmed (see the LOG); whether ASV's Padua rule is the interpolatory rule is still open.

## 6. Zenodo deposit file list

This lists every data or code file named in the two availability statements, with repository path and SHA-256 computed on 2026-11-14 at head `a0206a8` (all tracked in Git unless said otherwise). Paths in the papers are relative to the repository root. The statements promise a README in the archive; none exists yet. **Run-time dependencies** are not named in the papers but are needed to re-run: group B needs the directory `topics/mz-constants/sources/padua_mz_inputs/code/` (pinned by the SHA256SUMS.txt below), group F needs `g1_spectral.py`, and `mz2d_independent_check.py` reads `topics/padua-mz-2d-20261101/definitions.md`. The simplest faithful deposit is the tagged repository snapshot (`git archive` of the commit AC fixes) plus the items of section 6.2, which are not in Git.

### 6.1 Files in Git (groups A–F)

**A. MZ-CC, Prop 5.3 / Appendix C (Λ_edge ≥ 1.0044369), all in Git**

| Repository path | Bytes | SHA-256 |
|---|---:|---|
| `topics/padua-mz-sharp-constants-20261106/code/interval_dyadic.py` | 6575 | `8a90618d19ffd8f8efde50bc9002b0b0e26f62d243b4086c674cedcf657945fc` |
| `topics/padua-mz-sharp-constants-20261106/code/P4_rayleigh.py` | 4091 | `7bcf4032590cf07c12943ecd5b9bf1f3cef18f32240d884acba60ad5047947eb` |
| `topics/padua-mz-sharp-constants-20261106/code/P4_check_grouped.py` | 3083 | `63d53b6686e0a5259cab30bbb233d9ad8ad566283ae3f257bfb4411e455f4163` |
| `topics/padua-mz-sharp-constants-20261106/evidence/P4-trial-J512.json` | 12578 | `a472d397b6a802d7bfe9c06bdb25d2f572d18134726b8dad9f695772f0956da8` |
| `topics/padua-mz-sharp-constants-20261106/evidence/P4-trial-preparation.json` | 1081 | `613600248bad0c2a8567cb868842cb438769677ff24d216dcdf5c54d85047b0c` |
| `topics/padua-mz-sharp-constants-20261106/evidence/P4-rayleigh.json` | 2098 | `a4807c3b928e8f169f6f999f2284c82991fe7535e13d6001d67fd3bb36edfe07` |
| `topics/padua-mz-sharp-constants-20261106/evidence/P4-grouped-check.json` | 2108 | `a28033319547df6edcd8260af149ab485050d7212642c73ee3b8819ffa55323a` |
| `topics/padua-mz-sharp-constants-20261106/evidence/check-P4-independent.json` | 2067 | `28bb283a2cc3ca65153fd3afbb4a4b0473a7f3f6e96075a52d91a27d8c471a8e` |

**B. MZ-CC, Table 1 (MEASURED), code in Git**

| Repository path | Bytes | SHA-256 |
|---|---:|---|
| `tracks/mz-constants/code/reproduce.py` | 6216 | `fe88a16d2ac08df96dc5e18a224ac1b0d46d5cec4310cc86fff0f7fda1aa44ac` |
| `topics/mz-constants/sources/padua_mz_inputs/SHA256SUMS.txt` | 1958 | `c12ee67df3efc0a17791930da47332e6f7e8532f2006938a3608a6fd93ada19b` |
| `tracks/mz-constants/evidence/reproduction-manifest.json` | 2084 | `f07b2502444313da2e2180412e5a4c244a6e750e96973a25a090d914fff80be5` |

**C. MZ-SP, Prop 8.1 (certified brackets m = 10…80), all in Git**

| Repository path | Bytes | SHA-256 |
|---|---:|---|
| `topics/padua-mz-2d-frontier-20261105/code/cert_native.py` | 7857 | `6651de795706c0e2aa2689a58b9dd928835e2dbe9de0740b237b377d68b095ae` |
| `topics/padua-mz-2d-frontier-20261105/code/cert_pencil.c` | 4046 | `95993b761794306b41b67f6e7741fd9cd38817c08e5ec218c2f21fb08846d51e` |
| `topics/padua-mz-2d-frontier-20261105/code/independent_cert.py` | 7349 | `28228bf2fe412d13c9a581e907aed56385a914b3e51227126b110a9c6b4348cc` |
| `tracks/mz-constants/code/mz2d_exact.py` | 6421 | `5d1f005e2307d3a26badc9c1a44ce313dc9126625a49fba5d59430c151cf9c70` |
| `tracks/mz-constants/code/mz2d_independent_check.py` | 7617 | `5e455d747dc5dca84c883ed900095ff4a2bb40767f4ebcb3261d7d583df7bdfc` |
| `topics/padua-mz-2d-frontier-20261105/evidence/cert-m10.json` | 7082 | `c7310fbf90c46ee4b9c04f2ffb9ad1a0cc11c9e7e4a3dc4c6fc499b019da167a` |
| `topics/padua-mz-2d-frontier-20261105/evidence/cert-m20.json` | 7300 | `9c5392c3f34b54bd7666720baf38ed9fa8a6cf86fdc30ed640d8a8b9d2d860c3` |
| `topics/padua-mz-2d-frontier-20261105/evidence/cert-m30.json` | 7492 | `12cdeec967cac91497f80f13d9b7c12a3ce6a5d3d518c1b5335a39cc640344c9` |
| `topics/padua-mz-2d-frontier-20261105/evidence/cert-m40.json` | 7695 | `5cacc62a24b817c82cb448fad7d3eb53ca1b598b15f915255b3c2cb2ee4fcf36` |
| `topics/padua-mz-2d-frontier-20261105/evidence/cert-m60.json` | 8109 | `d853b8f24c52317c9e36904c0d344a2306e636ca67789f095d85ea6fdb2234a6` |
| `topics/padua-mz-2d-frontier-20261105/evidence/cert-m80.json` | 8545 | `c65655d77bc2ca85fa1eeb574beed1396a08a1a3acda0dee303f9e3283ac9ddd` |
| `topics/padua-mz-2d-frontier-20261105/evidence/independent-cert-m10.json` | 3850 | `91525efb9dc4da880e4f63fdfc7784553607780430d142c85e441edff7b0b370` |
| `topics/padua-mz-2d-frontier-20261105/evidence/independent-cert-m20.json` | 4059 | `992f82d553a2310195ad3543874d97584c7d54d1e655863d051b5c3d4dac3137` |
| `topics/padua-mz-2d-frontier-20261105/evidence/independent-cert-m30.json` | 4260 | `c69afa7dacb0712d8f120fb37459a6e62baf15dff83c3230e6d2ac8b3bbf16c3` |
| `topics/padua-mz-2d-frontier-20261105/evidence/independent-cert-m40.json` | 4467 | `603124a88c8ca9f22534f4e46c7f553ef8d66d79e7563831911dd99319c3c0f3` |
| `topics/padua-mz-2d-frontier-20261105/evidence/independent-cert-m60.json` | 4878 | `931f2c632943af1bd5d0772d3d7218f8883d08504c7c7bb2e949d616f4dcae23` |
| `topics/padua-mz-2d-frontier-20261105/evidence/independent-cert-m80.json` | 5300 | `7b57e74e0e3e919a79262067427e35afa97a637d5d39e0cc17620c93e99cd5fe` |

**D. MZ-SP, Prop 8.2 (witnesses m = 1101, 1240, 1600): code and receipts in Git**

| Repository path | Bytes | SHA-256 |
|---|---:|---|
| `topics/padua-mz-cleanup-20261105/code/rigorous_witness.py` | 10144 | `11f7cabcfb3c431a26224eb0d8df49db5d7de65c4685f979a9037d835a1cd498` |
| `topics/padua-mz-cleanup-20261105/code/independent_witness.py` | 7796 | `60c1e6db62fbd1c422fae2fa29476afad2796aa503a1225d7f507745fa08361f` |
| `topics/padua-mz-cleanup-20261105/evidence/witness-producer-m1101.json` | 2881 | `f5c3a58be6f875bcf77baf3e7a29c5c6e9d790304fc1a4121ae0f838ecfdb9cf` |
| `topics/padua-mz-cleanup-20261105/evidence/witness-producer-m1240.json` | 2880 | `a7bf9037d5282aecd6eadaf1bf5eeebc15368c509c12f5b780aafb50c6c6ad67` |
| `topics/padua-mz-cleanup-20261105/evidence/witness-producer-m1600.json` | 2881 | `87b74b1ba8b7ecaa8f79a93b26bcc92115a446aee5cf9d7536bf8c49539d5a4a` |
| `topics/padua-mz-cleanup-20261105/evidence/witness-independent-m1101.json` | 1594 | `7b0b36fa7c3f6ef1603fe98345f4355c31c6b06671234d86c1ec8664d4ea8a74` |
| `topics/padua-mz-cleanup-20261105/evidence/witness-independent-m1240.json` | 1582 | `0b4f58ba0c209fecb4ba4300f9c1fec90e321253aad753fde03aa44297c42b5f` |
| `topics/padua-mz-cleanup-20261105/evidence/witness-independent-m1600.json` | 1593 | `6b28a7514b41537bb027ae2301188e21f86b6ef0c9cd6e9c106592f8edce6912` |
| `topics/padua-mz-cleanup-20261105/evidence/witness-payload-identities.json` | 2403 | `2f280ff98ad2d230ad0e1d1a7865c8531e16895f41854b3d2f2fcbb1e5c1051b` |

**E. MZ-SP, Props 6.8 and 6.9 (‖B‖ enclosure), all in Git**

| Repository path | Bytes | SHA-256 |
|---|---:|---|
| `topics/padua-mz-sharp-constants-20261106/code/P1_rectangle.py` | 5075 | `c65b45fc2d4748e21ae7540bb47824dbc033f0d22917e49ac68084b7c1652963` |
| `topics/padua-mz-sharp-constants-20261106/code/interval_dyadic.py` | 6575 | `8a90618d19ffd8f8efde50bc9002b0b0e26f62d243b4086c674cedcf657945fc` |
| `topics/padua-mz-sharp-constants-20261106/evidence/P1-rectangle-N16.json` | 1914 | `004ec6dc00a90eab136da195878cb54a5cae9ab1a05610f997cbaef8ab773402` |
| `topics/padua-mz-sharp-constants-20261106/evidence/P1-rectangle-N8.json` | 1906 | `e4565ee893dd93ac84988c3896364350bd72861d44dbdd831b9361df1aabdf06` |
| `topics/padua-mz-sharp-constants-20261106/evidence/check-P1-independent-N16.json` | 1922 | `6557a68428a6a31708485f4506808a0d9dff3eff156673991b30c83c053cc909` |

**F. MZ-SP, Section 8.3 (MEASURED), all in Git**

| Repository path | Bytes | SHA-256 |
|---|---:|---|
| `topics/padua-mz-sharp-constants-20261106/code/P2_modes.py` | 11009 | `8e15fe58b19a1ef1a2ff71da80d18de04349d90081e02a885bcbb38b143d1161` |
| `topics/padua-mz-sharp-constants-20261106/code/S4_padua_fit.py` | 4243 | `529ca7a310341e3a30c50446de1d605baf489e4654436fe5285b1553e309cb13` |
| `topics/padua-mz-sharp-constants-20261106/code/S3_corner_model.py` | 3568 | `dc4c5f0c4d935d065ea3409d234c2727890a3ddcb10cdaf59c397127bda03b20` |
| `topics/padua-mz-2d-frontier-20261105/code/g1_spectral.py` | 8335 | `f246b7a436fa9e6133153a87fd5af887d80f6fb0ab12dc2208fbd9ade223c241` |
| `topics/padua-mz-sharp-constants-20261106/evidence/P2-m1600.json` | 3096 | `2817536e8f96cd70dcbb2725f9e8e993cdd8ae543288b71d4e57e77622d4bb01` |
| `topics/padua-mz-sharp-constants-20261106/evidence/P2-m1601.json` | 3096 | `1f7cefad8a95008db9bac0ba11fef712f60a04658a9a3af0b147c59155c7932f` |
| `topics/padua-mz-sharp-constants-20261106/evidence/P2-m3000.json` | 3075 | `ca7c0aa3cdfe67b4b481c04ac2bf4bbcf30c90c166790d57061726882c7feccd` |
| `topics/padua-mz-sharp-constants-20261106/evidence/P2-m3001.json` | 3095 | `ab052bae9dd3e1e936ea4368c006e2793a20e57a62f4ab13eb4aa611de167039` |
| `topics/padua-mz-sharp-constants-20261106/evidence/P2-b2-calibration.json` | 3603 | `fa842ea6e511bdeaf8137554db3b9fc2a24e7a1ec308754e44c873dae2ff3bd1` |
| `topics/padua-mz-sharp-constants-20261106/evidence/S4-padua-fit.json` | 7633 | `16ffc8171928e17db1eb5d1b16d0547cd0f158b821670ab2e362985205c160f9` |
| `topics/padua-mz-sharp-constants-20261106/evidence/S3-corner-model.json` | 3125 | `aa402823720b009305497aca1c2ff84101ea75aee12f02a8f07e7e53c1143feb` |

### 6.2 Files not in Git (cold storage), and their delivery state

**Delivery state: none of these has been delivered.** AC's destination `Downloads\padua\cold_storage\padua-mz-cleanup-20261105\` is not reachable from the sandbox, there is no delivery receipt anywhere, and the staging directory `/tmp/mz-cleanup` of the earlier session does not exist in this session. Identities below are from [padua-mz-cleanup-20261105/COLD_STORAGE.md](../padua-mz-cleanup-20261105/COLD_STORAGE.md), its [cold-storage.json](../padua-mz-cleanup-20261105/cold-storage.json) and the committed [witness-payload-identities.json](../padua-mz-cleanup-20261105/evidence/witness-payload-identities.json), which agree. Before the deposit AC needs a copy of the package: archive `c1-package-39479ff.tar.gz` (159,265,962 bytes, SHA-256 `ac6a628153746729688851baa3aa50f41dc31509d9ce4058dc221fb0550982b1`, 71 members, source commit `39479ffca76052ea79f90c2e5e0c4bfc80bf1584`, with inventory `PACKAGE-INVENTORY.json`, 19,557 bytes, SHA-256 `21e49393aa139cafa87c166520fe7478ee767694ee056356ef080f53c254170c`), staged at `/tmp/mz-cleanup/transfer-stage/padua-mz-cleanup-20261105/` in that earlier session. If it is lost, the witnesses are regenerable only from the committed producer with the frozen commands of COLD_STORAGE.md, but byte-pinned replay needs these exact files.

MZ-SP Prop 8.2 (PD-T376), referenced by the availability statement and by "archived with the deposit":

| Package path (inside the archive, under `checkpoint-39479ff/`) | Bytes | SHA-256 (container) | Decompressed JSON SHA-256 (bytes) |
|---|---:|---|---|
| `cert-m1101/witness.json.gz` (exact integer coefficients C_ab) | 4,196,078 | `22913a3271c0cd826ff062a1f880c3539ef937b0141820dab381b53181662813` | `71bcbc676272a19765c2e859c9116856ae7b5e2680eee332d042f4a3cf62e19e` (9,956,905) |
| `cert-m1240/witness.json.gz` | 5,365,436 | `1a9faac5677ac4dde63749a6acac38d95ee88a5082445e6ba6b59cc297d35e4e` | `899c680efe9fdd6ea013ce28e906bb273fbcc10633ee949df0fc47403abd9b3d` (12,801,774) |
| `cert-m1600/witness.json.gz` | 8,692,559 | `16d89f2c8600364aac3962c4164f0e0875c4fa866fc61269fd6f849e8f1fdad6` | `6bcf531c197b828cd67e1e3518a5404c6aa9bffeb456a9d26ee1b7ee96b1ec0f` (20,861,351) |

| Package path | Bytes | SHA-256 |
|---|---:|---|
| `cert-m1101/exact-norm.txt` (exact rational ‖p‖²) | 2,904 | `f651dff771fd67b5b3a9afb89e8f8c01c9b7a842a93cbe3b7658b04e69270f14` |
| `cert-m1240/exact-norm.txt` | 3,298 | `a9895473f6a97a3bca7a4b20144326a118f85d74157e00a32291eb11241f7daf` |
| `cert-m1600/exact-norm.txt` | 4,200 | `d6b405a856e735ac4df1d9db0295fbc093af66ee620d29c52ef553d6c1d3f6fa` |

The gzip container hashes depend on the zlib build; the decompressed hashes do not. The same package holds the positive controls m = 60 and m = 400 (witness gz `9a1bb58c…66e9` and `b433ab66…094d`, exact norms `04e78a32…6c4` and `6dc2c74a…0c2f`), which neither paper cites, and the producer and independent receipts.

MZ-CC Table 1 output (PD-T026, MEASURED). `tracks/mz-constants/evidence/reproduction.json` (29,202 bytes, SHA-256 `b85b06fa9b3317d6ce84f9d354626b74edad4e8f9885341ecad39166d4fd6d40`) left the branch head on 2026-11-02; it is the Git blob at `2b52b432fe59c9a50aef9deebe5152c5d6874465` (`git show 2b52b432fe59:tracks/mz-constants/evidence/reproduction.json`, checked 2026-11-14 to give this hash), AC cold storage PENDING ([COLD_STORAGE.md](../../tracks/mz-constants/COLD_STORAGE.md)). It regenerates in about 1.3 s: `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python tracks/mz-constants/code/reproduce.py --suite all --max-N 1280 --output <out>.json`; the numbers are deterministic, the JSON bytes carry timestamps.

MZ-SP §8.3 (P2 and S4 measurements). The calibration and summary files are committed (group F). The optional raw P2 and S4 outputs are **not retained** ([padua-mz-sharp-constants-20261106/COLD_STORAGE.md](../padua-mz-sharp-constants-20261106/COLD_STORAGE.md)); no delivery is promised and none is needed by a proof. The m = 1600 float vector of PR23 (10,246,528 bytes, SHA-256 `a23cb0e6e241993e5458474c64f153c965e8dc5047c2f1dfe08c7bc293e0a338`) was `/tmp` scratch and is uncertified; it is not referenced by either paper.

Not found: any manifest recording an actual delivery to AC's cold storage for the above (all manifests say PENDING), and any archive README for the deposit.
