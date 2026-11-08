# Section 4 onset-512 revision: developer response and preflight

Authored 2026-11-08 by the assigned Codex mathematical developer,
requested Sol xhigh; actual serving metadata is unexposed. Rules were
read at `b45e29fa1fe3dbfa2517ff8043e5d9c440870530`; the manuscript
edit was released by root after the notation checkpoint
`f77b6683d7601b68bae9793d7213683682bc7ecc`. This records a developer
candidate and dispositions, not an audit acceptance or publication freeze.

## Ownership and release

The edit scope was exactly these four sources:

| Source relative to this topic | SHA-256 at developer release |
|---|---|
| `paper/sections/comparison-unified.tex` | `1e106c9eaa046d7d01f4f6d1065bd7d8d5d65e4b62883930389aa389266a8294` |
| `paper/sections/localization-unified.tex` | `66d672b9e16eb611b15379f66e7db1475fde12a784cb1801174e7863c5e85e0e` |
| `companion-paper/sections/comparison-unified.tex` | `2b4db9743a2dd36380b18e22d569098432c1f3349f4dc19c88c1458b59a00f50` |
| `companion-paper/sections/localization-unified.tex` | `9dd80433aa61a646c0de59377b951106004e3a5d20bc74cf5dbeac5e29758c21` |

Root received these hashes and the release before this record was written.
The developer made no subsequent TeX edit. Root will fix the inherited
Abel-kernel overfull display before the final source freeze; that later
candidate must have its own identity and build record. This authored
response was separately requested by root after the TeX release.

The five top-level sections are preserved. The front-matter/Sections 1--3
writer and the certification writer own their files. This developer did
not edit their sources, frozen E01--E15 theory, engines, old reviews,
Git state, shared logs or historical PDF outputs.

## Mathematical content and source map

The mathematical inputs are the independently reviewed
[J01 gates](../theory/J01-onset512-gates.md) and
[J02 elementary enclosure](../theory/J02-elementary-constant-enclosure.md),
with their preregistered tiny exact-rational checker and receipt in
[`code/onset512_analytic/`](../code/onset512_analytic/). The manuscript
rewrite does not replace the all-n proofs by the audit's planning numbers.

| Manuscript interface | Result and source |
|---|---|
| `uc:finite-bounds` | A master comparison theorem: uniform absolute error, global signed norm, one-sided actual-origin lower bound, and the radius-one relative estimate. The old phase-dependent allowances remain proof intermediates. |
| `uc:absolute-gate`, `uc:absolute-gate-formula` | J01's single gate with the tangent condition, its persistence, and real-n monotonicity. `ul:outer-exclusion` is its n>=512, rho>=1 instance with gap 1/2. The proof also supplies the exact n=192, rho1=pi/2 base comparison needed by certificates. |
| `uc:relative-gate`, `ul:radial-quadratic`, `ul:wide-polynomial`, `uc:relative-gate-bounds` | J01's radius-one polynomial, exact quadratic optimization, decreasing unrestricted maximum and half-radius value, and vertex control for every real n>=512. The fixed positive-simplex optimizer argument proves the half-radius transfer. |
| `ul:selected-pairs`, `ul:finite-floors`, `ul:uniform-floor` | Original finite floor tiers are unchanged. The tail uses the fixed half-radius middle band, its increasing rational lower bound and its base at n=295; the other two classes already exceed 1/20 from n=64. |
| `ul:corner-lemma`, `ul:squared-peano`, `ul:corner256` | The existing corner-256 contract: both closed pi/4 squares, descent (A^2+B^2)/30. The axis proof now explicitly uses the general central-root estimate. |
| `ul:tail-location` | A numbered analytic localization theorem for every integer n>=512, proved by the two gates, uniform noncorner floor, corner descent, parity and compactness. |
| `uc:coarse-input`, `uc:kappa-series`, `uc:scalar-constants`, `ul:log-series` | J02's K=3 endpoint-cancelled series, analytic tail, rational pi/log/gamma/all-zeta bracket constructions and consequences. Only kappa>9/10, Cstar<1.8516, j>23/250, t0<221/500 and Cinfinity<9/4 are consumed. |

The radius-one signed outer theorem E14-wide-signed-outer remains a
premise of the relative row telescope. Its annular application is not a
premise. The uniform absolute error retains E08's correlated 3H/n
saving. The scalar maximum including its cusp, general central-root
bound, one-sided actual-origin bound and squared Peano argument remain.

The near relative column, its J_N/k_N/U_N symbols, the 3/8 central
specialization and quadratic B_beta lower bound, radius-dependent tail
floor statements, annular seams, outer geometry and separate u-dependent
far-192 derivation were removed from the manuscript chain. The historical
theory and audit records remain intact. Phase-dependent absolute
allowance definitions remain inside the proof because their correlations
are needed for the uniform bound.

The certification writer owns the moved `ul:far192` corollary in
Section 5. Its contract remains n>=192, rho>=pi/2, S<Lambda_c-3/100;
it cites `uc:absolute-gate`. The corner-256 label stays in Section 4.
The finite evaluator trust route, certificate data, I25 outcome and
final finite proposition are outside this four-file scope.

## Developer dispositions: paper and C2A

The following are implementation descriptions for root's response-03.
They do not declare the independent audit findings closed.

| Finding | Developer disposition in these sources |
|---|---|
| P-03 | Replaced the inherited Arb evaluation paragraph by the K3 series, exact rational constructions and analytic tail. Removed the unused upper kappa/H0 bounds and the trusted computational-input sentence in localization. Introduction/G01 edits belong to their writers. |
| P-04 | Added a region roadmap, the organizing identity lambda-Lambda_c=(S-S0)-Delta, numbered scalar corollaries, corner lemma and tail theorem, plus `fig:phase-regions`. Results are cited by their statement labels in the assembly. |
| P-09 / C3-03 | Deleted the entire obsolete outer-geometry argument, including its incorrect stated reason. Neither that reason nor the regional geometry is a premise of the new gate. |
| P-10(a) | Added physical/periodic phase-shift definitions, the effective-angle formula and the mesh-discrepancy bound to the paper's first center class. |
| P-10(b) | Added the singular-sample reconstruction using L+log(pi/m)=log pi-epsilon_n. |
| P-10(c) | Kept the circle layer-cake proof by centered-arc intersections; merged its duplicated companion summary. |
| P-10(d) | Added the sentence that the absolute finite-error proof at the origin uses none of the model-loss constants, so the origin identity creates no circular dependency. |
| P-11 | Removed the old multi-case completion recaps and obsolete audit/trust narration from the edited localization chain. This is not a claim of a complete paper-wide prose pass. |
| P-15 | Not fully implemented: old vertical-rule array styling remains. See the explicit remaining items below. |
| C2A-01 | Explained the completed row-integral model and added the exact b_full=2D0+(1/pi) integral coefficient identity before asserting the coefficient. The endpoint-reference completion points to its proof. |
| C2A-02 | Derived the phase row identity from angle addition and the divided-difference kernel, then derived both fractional pole offsets. The phase-zero toolkit remains in Section 3, coordinated with its writer. |
| C2A-03 | Repaired the broken weighted-C paragraph, factored the reciprocal increment correctly, and merged its duplicated estimate. |
| C2A-04 | Added h'(0)=pi/2-3/2>0 to the sine-comparison reasoning. |
| C2A-05 | Defined N_L/N_R before their first envelope use. Their deliberately coarse bounds remain sufficient; the expanded proof gives the pole decomposition. |
| C2A-06 | Stated evenness and pi-periodicity in separation and the integrable central-log convention at coincident channels. |
| C2A-07 | Supplied the new elementary bracket construction and retained/expanded the consumed derivative, coefficient and endpoint steps. Some optional one-line expansions from the original long list are still matters for the final pedagogical reading; this record does not assert that every suggested extra line was inserted. |
| C2A-08 | Restricted the cotangent sum explicitly to ordinary rows r not in A6, and identified its coarse coefficient bound. |
| C2A-09 | Merged repeated derivative, layer-cake, weighted-C and near/wide proof passages. Further stylistic compression is possible; exact preservation of every original prose sentence is no longer a goal. |
| C2A-10 | Preserved checkpoint aliases and corrected residual accidental substitutions: H<=H0, the root-convolution weight, row coefficients C_-/C_+, a local scalar summation index and a local sinc-profile symbol. |
| C2A-11 | Added the phase-region diagram and worked n=512 gate column. The optional additional cancellation/profile/row-sample figures were not adopted in this scope. |
| C2A-12 | Formal-block agreement was checked anew, as described below; old numbering identities are not claimed after restructuring. |

## Developer dispositions: C2B

| Finding | Developer disposition |
|---|---|
| M1 | Gave f_j=4a/(w^2-z^2), its signed reference sum, the absolute-sum identity, the signed finite row sum, positive-sample factorization and endpoint error. The paper is concise; the companion expands the subtraction. |
| M2 | Stated residual=2w sum E and the product-increment inputs that produce the three displayed coefficients. |
| M3(a) | Derived the L-coefficient sup/variation from the folded maxima and the monotone cotangent remainder. |
| M3(b) | Defined the pole numerators before use; the scalar maximum supplies their bounds. |
| M3(c) | Added an explicit central supremum bound using the R bound, the coefficient motion and t|log t|<=1/e. |
| M3(d) | Added source bounds for both hole envelopes. The entropy branch and s>v branch are treated separately before combining their R bounds; the false universal bound |R|<=p(-log sin e) is not asserted. |
| M3(e) | Displayed the normalized central-row pole estimate, bounded each row by L+6 and then summed the two rows. |
| M3(f) | Identified omitted exact-collision references, the per-reference Xi bound and the at-most-two count. |
| M3(g) | Defined temporary C_j/E_j with positive index ranges before the cutoff recurrence. |
| M4 | Used the checkpoint aliases, kept phase allowance definitions local to the proof, removed near-only symbols, and added the companion re-entry table. No comprehensive new one-page notation inventory was inserted; remaining local overloading is for the final pedagogical audit to assess. |
| m1 | Defined the separated upper bound rather than claiming it equals the actual termwise maximum. |
| m2 | Gave the sharper nu<=n/2+1/pi reason for the sinc argument range. |
| m3 | Stated the tail j>=3 guard where the reciprocal inequality is used. |
| m4 | Described 160 as a convenient common onset, without claiming it is earliest. |
| m5 | Explained why the closest row has no positive sample on rho<=1. |
| m6 | Defined S_disp at its first use in the origin calculation. |
| m7 | Made b=xi+|s|=rho/pi explicit. |
| m8 | Gave the cosine-weight/w estimate for the (1,-y) chart and the simpler estimate for the other charts. |
| m9 | Linked the global norm passage to the phase symmetries/reflection reduction. |
| m10 | Added the S<v case in the parameter-integral estimate. |
| m11 | Stated the 1/(nm) normalization for the finite charges. |
| m12 | Removed the repeated near/wide pole-table proof and merged several repeated summary/proof passages. Residual recurrence repetition e2 is explicitly still listed below. |
| e1--e4 | Not falsely closed. See the exact remaining items below. |
| n1 | Section 5 diagram belongs to the certification writer; this scope adds a separate Section 4 phase-region diagram. |
| n2 | The closed-domain passage remains in the complete expressions; the new gates explicitly include their seams and endpoint limits. |
| n3 | The new matched formal-core check replaces the old comparison identity check at this changed scope. |

## Developer dispositions: C3

| Finding | Developer disposition / boundary |
|---|---|
| C3-01 | Section 5 trust boundary belongs to the certification writer/root; the constant-enclosure computational premise is removed from this scope. |
| C3-02 | Added the four-output re-entry table and worked n=512 gate bounds in the companion; the common constants remain defined together. |
| C3-03 | Removed the obsolete outer-geometry proof, as above. |
| C3-04 | Removed the old artificial 1/8 split and coefficient tuple; derived the new J01 tuple explicitly and proved its all-real-n transfer. |
| C3-05 | Showed the positive common C grouping before band endpoint substitutions, including the fixed tail band. |
| C3-06 | Stated the fixed half-radius hypothesis inclusion rather than assuming radius monotonicity. |
| C3-07 | Corrected the endpoint identity to sum over sigma and explained the factorized weights/parity. |
| C3-08 | Used the general central-root bound for E_c(h,0)<1/4, with explicit rational bounds on p and a; retained E_c(0,h)<=0. |
| C3-09 | Made the strict cosine interval and equivalent upper/lower endpoint parity conditions explicit. |
| C3-10 | Displayed the normalized selected-pair count; companion folding/multiplicity explanations remain. |
| C3-11 | Distinguished mesh-index distance from phase radius. |
| C3-12--14 | Native vocabulary, tiny n=2 certificate and Section 5 diagram belong to the certification writer. |
| C3-15 | Added the explicit derivative criterion and the curvature/optimizer monotonicity argument. |
| C3-16 | Removed the radius-dependent tail-floor statement whose lower bounds could be negative near its start. |
| C3-17 | Removed the old outer-gate arithmetic; the corner proof still states its coarse pi bounds. |
| C3-18 | The checkpoint phase notation is preserved and the comparison/projection objects are identified. A final notation reading may still improve local reminders. |
| C3-19--20 | Replaced repeated completion summaries by one numbered tail theorem and one proof covering closed seams/ties. |
| C3-21 | The referenced outer-geometry application was removed with its whole block. |

## Exact remaining editorial items

These are not reported as closed. Line numbers below describe the
developer-release hashes and will shift under root's final edits.

- **C2B-e1:** paper comparison line 860 and companion line 2224 still
  read endpoint heights `$|D|\cot e,C\cot e$`; the intended second
  magnitude is `$|C|\cot e$`. The surrounding proof already treats
  general coefficient signs, so this is an editorial magnitude notation
  repair, not a new variation constant.
- **C2B-e2:** companion comparison line 2025 still repeats the cutoff
  recurrence immediately after its expanded derivation: “The h_j,g_j
  recurrences therefore show that increasing…”. Delete that repeated
  sentence in the editorial pass; keep the derived recurrence once.
- **C2B-e3:** companion comparison line 2656 still gives the coarser
  displacement bound `40a/(9*pi^2*m)`. The preceding sharper
  sum bound `sum z^-2<=3/(8*pi^2)` would give
  `10a/(3*pi^2*m)`. The displayed value follows from the weaker valid
  `sum z^-2<=1/(2*pi^2)`; the source should say which bound is used,
  or print the sharper intermediate. The final `18a/n` allowance is
  unchanged and remains a valid upper bound.
- **C2B-e4:** paper comparison line 806 and companion line 2089 still
  say “including ell_0”; explicitly identify it as `sinc y`, the
  r=0 signed sine contribution. The displayed sinc term is already
  present in the reference definition.
- **P-15:** old `array` displays still have vertical rules, including
  paper comparison lines 927, 1284, 1378 and the base table near 1528,
  with their companion counterparts. Booktabs-style presentation is
  not implemented by this candidate.
- **Inherited Abel display:** final preflight logs have one overfull
  box of 30.2171 pt at paper comparison line 180 and companion line
  343. Root explicitly reserved the repair. The long new relative-base
  display was split during development; it is no longer the reported
  overfull box.

The mathematical auditor should also assess whether the local notation
reminders and remaining companion prose meet the intended teaching
standard. The preceding dispositions are not self-approval of that
editorial judgment.

## Structural checks and preflight build scope

A standard-library source scan was executed on the four release files:

- Comparison: **7 paired formal statements and 47 paired numbered
  display environments**, byte-identical between paper and companion.
- Localization: **3 paired formal statements and 11 paired numbered
  display environments**, byte-identical between paper and companion.
- The label lists and heading lists agree in each pair; proof
  environments balance. A scan across the paper section files found
  no missing `ref`/`eqref` targets.

This was a structural comparison, not a mathematical proof or the final
re-baselined correspondence acceptance. The latter belongs to root.

The two full current manuscripts were built as developer **preflights**
using pdfTeX 3.141592653-2.6-1.40.26, TeX Live 2025/dev/Debian and
latexmk 4.86. Both builds used the existing pinned publisher-template
directory read-only and wrote only to fresh per-agent directories:

```
TEXINPUTS=/workspace/padua_research/local-output/padua-argmax-bridge-20261105/paper/template//: \
BSTINPUTS=/workspace/padua_research/local-output/padua-argmax-bridge-20261105/paper/template//: \
latexmk -norc -pdf -interaction=nonstopmode -halt-on-error -file-line-error \
  -outdir=/tmp/padua512-editor-paper main.tex
```

The working directory was the topic's `paper/`; the companion command
used its `companion-paper/` working directory and
`-outdir=/tmp/padua512-editor-companion-paper`. Stdout/stderr were
captured in `/tmp/padua512-editor-paper.build.txt` and
`/tmp/padua512-editor-companion-paper.build.txt`. Both final invocations
completed with exit 0. Final `.log` scans found no undefined references,
undefined citations or multiply-defined labels. The one inherited
overfull display is recorded above.

| Preflight artifact | Pages | Bytes | SHA-256 |
|---|---:|---:|---|
| `/tmp/padua512-editor-paper/main.pdf` | 50 | 705101 | `072f51e866d462b11f6c6a899d1d50e5b59763b7f67c3f0f0187a29c9f0af94d` |
| `/tmp/padua512-editor-companion-paper/main.pdf` | 147 | 1161961 | `cb3a3b817ab2e234731c45349d4d66dd18efc22a887f5dc09f8384bd3345c734` |

The sources outside this developer's four files were being integrated by
their owners. These numbers identify the observed preflight artifacts;
they are not a final integrated page count, final-source build claim,
43-page commitment or publication artifact. The old PDFs and build
directories were not overwritten. No generated PDF or large build log
is proposed for Git.

The first manual paper build lacked the required template path and
stopped with `sn-jnl.cls not found`; a following latexmk invocation
reported its cached failure. After supplying `TEXINPUTS/BSTINPUTS`, a
forced `latexmk -g` rebuild succeeded, followed by the successful final
invocation above. A preceding temporary edit helper also had a working-
directory path error and made no file change. These were development
preflight errors, not failed mathematical gates, native runs or
certificate attempts. The only mathematical base computation remains
the separately preregistered J01/J02 exact-rational check.

## Handoff boundary

The four TeX hashes above are the developer's review candidate. Root
owns final integration, the Abel formatting fix, the I25-dependent
Section 5 trust update, final builds and the distinct mathematical
review. This record does not claim those later steps occurred. No
further TeX edit or Git-state operation was performed when writing it.


## Root integration — 2026-11-08

The root integration splits the inherited Abel display, repairs C2B-e1's
absolute coefficient, identifies ell_0 as sinc(y) (e4), deletes the repeated
companion cutoff sentence (e2), and explicitly uses the weaker valid
reciprocal-square bound in the existing displacement estimate (e3). Array
column rules are removed for P-15. A duplicated “Thus / The preceding”
transition is merged. Two residual alias mistakes are corrected: the
finite-part counterterm is H(w), and the local tangent profile is T_c,
separate from the global model-loss coefficient. No numerical constant,
finite predicate or gate threshold changes in these corrections.

The front data statement is also corrected to identify the actual source
repository and mark the certificate deposit/DOI as future, rather than
claiming every essential certificate is in Git. AI, funding and contribution
paragraphs remain byte-identical to the input. The integrated paired-source
check passes 19 formal statements, 85 numbered display environments and116
labels. The distinct mathematical review accepts the current Section4 and
Section5 sources; final build/layout and Sol max presentation review follow.
The developer-release/preflight identities above remain historical.
