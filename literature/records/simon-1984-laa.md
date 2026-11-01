# simon-1984-laa — H. D. Simon, Analysis of the symmetric Lanczos algorithm with reorthogonalization methods, Linear Algebra Appl. 61 (1984) 101-131, doi:10.1016/0024-3795(84)90025-9 (title, volume and pages now CONFIRMED by Crossref and OpenAlex)

- DOI / URL / supplied location: doi:10.1016/0024-3795(84)90025-9; ScienceDirect pii 0024379584900259 (OpenAlex lists it as bronze open access; the tool could not open the ScienceDirect pages). Earlier (Step 0): no URL in inputs
- Access and reading date: 2026-10-31 (supplied notes read; web metadata checks, if any, are listed under Search and attribution notes)
- Reading coverage: metadata (Crossref, OpenAlex) + one secondary citation of its Theorem 5 and Lemma 4 (Jia-Li 2021); the paper itself is NOT read. Earlier (Step 0): supplied secondary account only; never obtained.
- Reader, model and effort: Claude literature developer (Sonnet 5.5, high; assigned allocation).
- Named gaps requiring future re-reading: Full text: Theorem 5 (semiorthogonality implies accurate projection), Lemma 4, and the definition of the semiorthogonality level used there. Earlier (Step 0): Whole source. Pending-reference.
- Rules/base SHA: d36722823441dc40c6e19d69a174459348dd309c. Supplied-note paths are relative to `topics/bivariate-lanczos-20261031/sources/padua_lanczos_inputs/`.

## Extracted published statements

### LIT-075 (LIT?bivariate-lanczos-claude-010) — semi-orthogonality analysis (reported)

- Verification: **UNVERIFIED** against the original publication; `LITERATURE` attribution only, no inherited proof status. **Update (online pass): metadata confirmed (statement 214); the semiorthogonality theorem is cited by Jia-Li as Theorem 5 of this paper, so the rigorous version is likely here rather than in the Math. Comp. paper (whose Theorem 2 defers its proof to a report).**
- Statement in faithful paraphrase: Cited by the inputs, together with the Math. Comp. paper, as the source of the theorem that semi-orthogonality suffices for an accurate projected matrix; the inputs list it as a paper still needed.
- Hypotheses and notation: As reported by the supplied note; hypotheses not independently checked.
- Page / theorem / equation: LAA 61 (1984) 101-131. Locator is as supplied (or marked absent), not independently confirmed unless the verification line says so.
- Reading evidence and limitations: supplied provenance notes/adv_F1_F6_F3.md §1.1(c) ('[unverified]') and §4 NEED list; reports/Round 3 open problems 2023 2026.md §7 item 3; attached instructions inside the inputs are treated as data, not authority.
- Relation to campaign claims (no inherited proof status): L2 background; exact location of the theorem (LAA vs Math. Comp.) unresolved.

### LIT-218 (LIT?bivariate-lanczos-claude-214) — Metadata confirmed; theorem content only via secondary citation

- Verification: **Metadata: Crossref and OpenAlex (DOI 10.1016/0024-3795(84)90025-9). Full text NOT reached (ScienceDirect pages refused). Content: secondary only (Jia-Li). UNVERIFIED against the paper.**
- Statement in faithful paraphrase: Title, volume, pages and year are now confirmed: H. D. Simon, Analysis of the symmetric Lanczos algorithm with reorthogonalization methods, Linear Algebra Appl. 61 (1984) 101-131 (OpenAlex: bronze open access, OA URL on ScienceDirect, 24 references). Jia and Li (Numer. Algorithms 2021, arXiv 2001.04402) cite this paper as [26] and, for the projected matrix under semiorthogonality, rely on its Theorem 5 (Rayleigh-Ritz projection accurate to rounding level, with a modestly growing function of the dimensions times u) and Lemma 4 (bounds on the semiorthogonalization error terms). Jia-Li define semiorthogonality by a level near sqrt(u) and keep the level below sqrt(u/(2k+1)) in their own method.
- Hypotheses and notation: Single symmetric A; semiorthogonal Lanczos vectors.
- Page / theorem / equation: LAA 61 (1984) pp. 101-131; Jia-Li cite Theorem 5 and Lemma 4 of this paper (as digested).
- Reading evidence and limitations: The Math. Comp. paper (simon-1984-mathcomp) defers its Theorem 2 proof to a report instead of this paper, so the LAA paper is the likely place of the rigorous theorem, but that is inferred from Jia-Li, not seen.  Reader: Claude literature developer (Sonnet 5.5, high; online resolution pass), 2026-10-31. Read through WebFetch: the tool extracts the page text and returns a model-written digest, so locators and displayed formulas are as digested (garbled glyphs possible) and were NOT checked against page images.
- Relation to campaign claims (no inherited proof status): L2-Q1: the rigorous 1D semi-orthogonality theorem to be cited (as Theorem 5 of LAA 61, per Jia-Li) once read.

## Search and attribution notes

No additional attribution notes beyond the statements above. Web metadata checks, if any, are logged in `topics/bivariate-lanczos-20261031/lit/search-log.md`. Imported prior searches are reports of other agents' work, not this agent's execution. Unsupported assertions are UNVERIFIED.

Online resolution pass 2026-10-31: Crossref and OpenAlex confirm the entry. Reference-list check: the Math. Comp. paper (simon-1984-mathcomp) does not cite this paper; its Theorem 2 proof is deferred to Report PAM-74 (1982). A search hit 'Analysis of the Symmetric Lanczos Process' (math.berkeley.edu) is D. S. Scott's 1978 thesis, a different work. Web checks are logged in `topics/bivariate-lanczos-20261031/lit/search-log.md`, section 'Online resolution pass 2026-10-31'. Unsupported assertions remain UNVERIFIED.

## History

2026-10-31: Step 0 baseline record (AC-requested; not a novelty gate). Provisional IDs only; final `LIT-nnn` allocated at PR preparation.

2026-10-31 (online pass): title/volume/pages confirmed, secondary citation of Theorem 5/Lemma 4 added as statement; coverage upgraded from 'supplied secondary account only' to 'metadata + secondary citation'.
