# LIT?padua-3d-20261106-codex-T9-r06-03 — Chkifa, New bounds on Leja and R-Leja Lebesgue constants

Alias: T9-R06-LIT-CH. Extracted statements04/05/06 below and this source03 have full provisional local IDs; none is a global allocation.

- DOI / URL: primary author paper https://arxiv.org/pdf/1503.01731 . Title: *New bounds on the Lebesgue constants of Leja sequences on the unit disc and on R-Leja sequences*. Accessible PDF header arXiv v2, 16 May 2015; internal manuscript date November 19, 2021 was preserved without reconciling the mismatch.
- Access and reading date: 2026-11-06, available WEB connector; primary PDF and screenshot inspected.
- Reading coverage: introduction pp1–4, disk-sequence definition and explicit binary formula pp5–6, R-Leja definition/recursion pp13–14, Theorem3.2 and its displayed statement p15, difference-operator equation(4.4), Lemma4.2 proof, Corollary4.3(4.8) pp17–19, references p21. Not complete full text.
- Reader, model and effort: Codex T9 round06 worker; runtime model identity unavailable.
- Named gaps: complete proof of Theorem3.2 not independently reconstructed; all prior-paper proofs not read. The source's cited Cohen–Chkifa chapter was not retrieved in full.

## Extracted published statements

### LIT?padua-3d-20261106-codex-T9-r06-04 — all-prefix difference-operator bound

Alias: T9-R06-LIT-CH-D.

- Statement: R-Leja points are the real projections of a disk Leja sequence in its order, with repeated real points omitted. A real recursive version is r0=1,r1=-1,r2=0 and r_(2j-1)=sqrt((r_j+1)/2), r_(2j)=-r_(2j-1), j>=2 (3.5). Corollary4.3 states D0=1 and D_k<=2^sigma1(k)2^m for 2^m<=k<2^(m+1), equation(4.8), for the norm of the difference of interpolation operators at consecutive prefixes.
- Hypotheses: the specified R-Leja sequence and every integer prefix, not just completed dyadic Lobatto grids. Index k means the newly added point r_k; I_k has k+1 points.
- Local consequence: D_k<=(k+1)^2. This is the precise imported premise used in new `t9-r06-explicit-rleja.md`.
- Evidence/limits: source definition, displayed equation and Corollary proof checked. The proof invokes its Lemma4.2 and earlier hierarchical-sampling Lemma7, so the literature dependency remains explicit.

### LIT?padua-3d-20261106-codex-T9-r06-05 — every-prefix quadratic Lebesgue bound

Alias: T9-R06-LIT-CH-L.

- Statement: introductory equation(1.11), following Theorem3.2, gives a bound <=6sqrt(5) k 2^sigma1(l) at k-point R-Leja prefixes between dyadic Lobatto sizes; dyadic prefixes are separately bounded by the classical Lobatto logarithmic estimate(3.8). Thus all k-point prefixes satisfy <=6sqrt(5)k^2. This is stronger than a bound along dyadic prefixes alone.
- Campaign relation: the old conditional one-dimensional prefix hypothesis can be met using this later verified primary source. The new direct Delta transfer is sharper in constant than substituting differences of these prefix bounds.

### LIT?padua-3d-20261106-codex-T9-r06-06 — earlier multivariate cubic-in-point-count bound

Alias: T9-R06-LIT-CH-PRIOR.

- Statement: the introduction explicitly attributes a cubic Lebesgue bound in the number of multivariate interpolation points to Cohen–Chkifa, *On the Stability of Polynomial Interpolation Using Hierarchical Sampling*, reference[7], formula(25).
- Relation: this kills any 'first explicit minimal 3D polynomial bound' priority claim for our lower-set specialization. The reported order O(N^3) is prior art. Exact constants of formula(25) were not imported without the chapter's full text.

## 2013 intended primary and search limits

Chkifa's 2013 JAT paper is *On the Lebesgue constant of Leja sequences for the complex unit disk and of their real projection*, JAT166 (2013),176–200, DOI10.1016/j.jat.2012.11.005, primary ScienceDirect article S0021904512002067. Its metadata and abstract were inspected, verifying subject and citation. The rendered mathematics was missing, and full text was unavailable. We therefore do not claim the exact quadratic bound above follows from the 2013 paper on the basis of its abstract. The independently accessible later author paper supplies the required every-prefix premise and exposes the stronger multivariate prior art. No upload is necessary for the authorized fallback proof.

## History

2026-11-06: exact difference/prefix hypotheses verified from later primary source; priority claim gate-killed before final theorem status.
