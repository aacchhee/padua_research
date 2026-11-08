# Notation-only checkpoint receipt

Rules/input: `b45e29fa1fe3dbfa2517ff8043e5d9c440870530`.
Developer: delegated Codex notation worker, requested gpt-6.1-sol medium.
Actual serving-model identity and reasoning-effort setting are not independently
exposed by this runtime. No novelty-bearing work: the novelty gate does not
apply to symbol aliases with unchanged mathematical meanings.

Authority: handoff 29 dated AC addendum, item 2, authorizes coordinated
paper-wide renames and rename-aware checking now; final rebaseline follows
onset-512 restructuring. The root coordinator additionally accepted
`\mathsf{a}` for the phase amplitude and `\varepsilon_L` for the companion's
local vector-motion displacement after free-token checks.

## Applied register and exact scope

Both manuscripts use the proposed register in audit-03/n-notation.md §4.3:
model loss `T -> \mathfrak{T}`; scalar `j,j_* -> \mathfrak{j},\mathfrak{j}_*`;
scalar series constants `k,k_0 -> \mathfrak{k},\mathfrak{k}_0`;
mesh ratio `k=n/m -> \mu`; logarithmic majorant `H -> \bar{L}`;
row coefficients `C(v),D(v) -> C_-(v),C_+(v)`; row profile
`\mathcal H(L,v) -> \mathcal V(L,v)`; scalar convolution `W -> \mathcal{W}`;
pole norm `B_n(t) -> \mathcal{N}_n(t)`; radial coefficients
`\ell_1,\ell_2,d_1,d_2 -> \ell_x,\ell_y,d_x,d_y`,
`e,f,g -> \mathfrak{e},\mathfrak{f},\mathfrak{g}`, `P(rho) -> \mathfrak{p}(rho)`;
model constants `d_0,v_0 -> d_*,v_*`; outer majorants
`a_0,w_0,p_0,P_0 -> \bar{a},\bar{w},\bar{p},\bar{P}`;
band endpoints `a_0,b_0 -> b_-,b_+`, `C -> A(0)`, `A_0 -> A(b_-)`,
`E_n -> B_n^\sharp` (including indices 64 and 160), `D_b -> w_b`;
selected-pair meshes `M,L -> \bar{m},\bar{n}`, center angle
`\gamma -> \theta_c`, outer slope `\gamma_b -> \lambda_b`;
selected radius `r -> \bar{\rho}` (including radius-indexed families),
endpoint distance `s -> i` after its declaration, retaining the distinct
periodic indices `(r,s)` in the projection formulas;
outer gate `G,K,A -> \mathcal{G},\mathcal{K},\mathcal{A}`;
entropy majorant `C -> C_\Gamma`; corner loss `q_0 -> q_h`;
main cutoff/logarithm `epsilon,ell -> \hat{\varepsilon},\hat{\ell}`;
local hole cutoff/logarithm `epsilon,ell -> \varepsilon_h,\ell_h`;
coefficient displacement `\varepsilon -> \varepsilon_d`;
folded separation `epsilon=min(t,pi-t) -> e_t`;
cancellation difference `f -> \tilde g`; scalar second derivative `g -> f''`;
origin variation bound `V -> V_F`; corner diamond kernel `D_n -> \mathcal{D}_n`,
half-angles `S,T -> u_+,u_-`; endpoint weight `\epsilon_j -> \varepsilon_j`;
optional corner row `\alpha -> \alpha_r`.

The phase amplitude is `a=c_e c_d -> \mathsf{a}` in comparison and localization,
including explanatory mathematics. Bare `a=2/pi` in the corner expansion,
the companion's generic BV-cell endpoint `a`, the four-real-number pairing
example `a,b,c,d`, and certification rectangle/coordinate variables remain
unchanged. `\chi` was rejected: its existing nonnegative test-function role
has 3 companion tokens. Before amplitude renaming `\mathsf{a}` had zero token,
base and raw-text occurrences in both manuscripts. The local displacement
`\varepsilon_L=pi/(2m)` had zero full-token/raw-text occurrences in both;
its base family `\varepsilon` already existed. It is distinct from the main
cutoff `3pi/(2m)` and from the hole cutoff `h/2`.

Companion-only §4.2 aliases applied: introductory remainder `R_n -> \mathcal R_n`;
corrected kernel `R_n -> \widetilde K_n` throughout preliminaries;
hat function `\psi_B -> \mathsf{h}_B`; diamond inverse indices `A,B -> i_1,i_2`;
positive/negative row totals `P,Q -> P_+,P_-`; odd indicator
`e -> \boldsymbol1_{n\text{ odd}}`; local cosines `c,c_i -> \mathsf{c},\mathsf{c}_i`;
reciprocal-square sums `S,S_o -> \zeta(2),\zeta_{\rm odd}(2)`;
quadrature cell error `E_j -> \mathsf{E}_j`; local corner logarithm and constant
`L,c_v -> \mathsf{L}_m,\mathsf{c}_v`; entropy slope
`\kappa -> c_\Gamma`; finite-product odd size/cutoff/root/unit
`N,M,\zeta,w -> \mathsf{K},\mathsf{k},\mathsf{u},\mathsf{w}`;
trapezoid amplitude `M_* -> \mathsf{M}_e` and supports `I_1,I_2 -> \Omega_1,\Omega_2`;
curvature bound `K -> M`; root `D_* -> \mathsf{D}_*`;
concavity function/constant `H(g),d -> \mathsf{A}(g),\mathsf{d}`.
Decorative macros use braces so adjacent factors remain separate TeX tokens.

## Checks actually executed

Command from repository root:

```sh
python3 topics/padua-argmax-bridge-20261105/audit-03/code/n/notation_scan.py --repo . --out /tmp/notation-candidate --baseline-rev b45e29fa1fe3dbfa2517ff8043e5d9c440870530 --rename-map topics/padua-argmax-bridge-20261105/notation-rename-map.json
```

PASS: current paper vs current companion: 13 statements, 90 numbered display blocks.
PASS: numbered blocks equal baseline b45e29fa1fe3 after 118 declared renames (both texts).
The compact JSON map contains contextual literal substitutions in execution
order, scoped by section filename; it is specifically the scanner's checked
block contract, not a source-wide search-and-replace program. Context avoids
changing index `j`, scalar `k_0` versus index `k`, `H(w)` versus `H=1+L`, etc.
The mathematical alias register above also covers the unnumbered explanations.

Separate full-source checks passed on all 14 TeX files: identical sequences
of all non-math bytes; identical label/ref/eqref commands; identical math-region
counts and source line counts. Consequently all AI, funding, ORCID and author
contribution paragraphs are byte-identical (both main.tex files are entirely
unchanged). Full source SHA-256 identities below pin the reviewed candidate.
No equations, hypotheses, proofs, headings, declarations, bibliography or
reference text have been added, removed or rewritten.

Baseline scan: paper 18 duplicate-definition flags, companion 67.
Candidate scan: paper 19, companion 67. The heuristic flag set is not invariant
under symbol typography: two inherited paper flags s_L,s_R disappear and
three inherited local roles e,r,c are detected more fully. Specifically candidate
flags e at comparison 1260/1318 and r at 1147/1297 are existing different local
roles; candidate c at localization 216/230 is the existing choices 5/4 and 2.
No new mathematical meaning was assigned to an existing symbol. These scoped
local roles remain explicit; heuristic counts are not a collision proof.

The frozen `companion-paper/check_correspondence.py` was run and failed as
expected at `Original changed: .../paper/sections/certification-unified.tex`.
Its byte-freeze baseline has deliberately not been edited. Fresh builds used the explicit new directories recorded below; existing PDFs/freeze commits were not touched.

## Deferred to the content phase

Notation tables and explanatory register introductions must follow this pure
checkpoint. The remaining optional upright exponential/imaginary-unit glyph
normalization in companion-only derivations is cosmetic and deferred; the
corner diamond definition and its step-two geometric sum already use upright
glyphs. The finite-product coefficient c_N follows the new size as
c_{\mathsf K}. Global micro-aliases such as D_a and delta_a remain named
allowance/operator labels; they do not redefine the reserved scalar a.
No manuscript content rewrite or final baseline update is included.

## Candidate source identities

`path | baseline SHA-256 | candidate SHA-256`

`companion-paper/main.tex` | `2c3350b722030df1f5dddd3baa9d14986fe8825a468e54de1926530b4f8dafd0` | `2c3350b722030df1f5dddd3baa9d14986fe8825a468e54de1926530b4f8dafd0`

`companion-paper/sections/certification-unified.tex` | `a9d9874f58b8507eab7976e9a24b551b5b31285d688e9f725e5210fa279c4b09` | `baf8ed09237ffbffabc5a3f3d8d5f9d1bfea8024b6138153f952b8c2cab52415`

`companion-paper/sections/comparison-unified.tex` | `6fa8e0b26852d43047fc0127451df14ff598eefd853727566ca13516d356a092` | `eb9c8682283a34eb0d168611b94d341cf2b8ef20551ec302cb4ceb3f9be664ec`

`companion-paper/sections/corner-unified.tex` | `6d68c3f8038c822599689cbf34a1db35e243acd8aa2dd1d25fd222ea6f11ad3b` | `560598e6b808cedf34bfe92b644ca7cff87fd1b1112694e31133ddaf96af5419`

`companion-paper/sections/introduction.tex` | `8f3174fec71637c8c8c5a91188ddc2148722efbfc39d079d69bb18f79a6bad1a` | `dd747eac7ff9e35b3296ed2504cbb2f0ae66a67f91d2ea3b3993ae1c3c34f2d1`

`companion-paper/sections/localization-unified.tex` | `600c06cca07cd8647a33205714e32720067f498485c90d0dabba58104948dc41` | `660dcebce3ded15c12d6141f96a04c8692d455f74b68606dc669dd78a970ed45`

`companion-paper/sections/preliminaries.tex` | `0667719e8c5f0872a91b183b7fa95727716697329b0b0e89c3da4f2ad5d0be54` | `c51a82f89eec44852754a98ec0035dad4dabae3cd05e5ce2afc37e9074ac4aff`

`paper/main.tex` | `013789e91d291ae6763dcd8aa0caac8e35d18e26c394a16c074e3d37c7da66c9` | `013789e91d291ae6763dcd8aa0caac8e35d18e26c394a16c074e3d37c7da66c9`

`paper/sections/certification-unified.tex` | `80c4e3e764e559d596d38ae5ee40702fd3ce9ba54ea1dbe43eb5c234d6ee6eea` | `8733693e3fab90153cca2a1ff7b252c92f07c74136772f5426cdecfeb93953e1`

`paper/sections/comparison-unified.tex` | `be20756e98358fbd483135adddf545128640ae3e4c90f763ba427283a0a250ce` | `76adc270f3aec57ecc0f7a12b34dfd341ee7c1d60733845920b2afde6c693995`

`paper/sections/corner-unified.tex` | `c74e94d3aa15d446d49c425705e241475cd00cbded7728d76576f5efdbf73bf6` | `268dfb5e8cc1e610a1c920b1c400aca8fb9431543528e3d63fed59466dcbfed8`

`paper/sections/introduction.tex` | `c8c9c35ba0577a6a17b0089b8413277024d03c1a904aa582f7967d082db1ba78` | `c8c9c35ba0577a6a17b0089b8413277024d03c1a904aa582f7967d082db1ba78`

`paper/sections/localization-unified.tex` | `180efdc2bc10d00d9a5f6aa47befe538023b2c349db853a5481042b7a7cfe361` | `b49489ffb4a21260bc77c24e3071e8573e615f24724bc4301d6db87591a85da1`

`paper/sections/preliminaries.tex` | `f5cd4b1dc6ab98e31a1a51a5ef91a7d1336d531fe06bdf0026992cff45ec920b` | `0b90966321274a55809c63dc51272efdd6566019309ecd9d15f978dde662a033`

Aggregate source-set SHA-256 (sorted relative path, NUL, candidate hex, newline): `248285ab65da6300f5aa483f2d90049937e95e1513c941285bf9362c22368147`.


## Root-requested grouping correction and fresh builds

The root review caught that replacing an unbraced one-token macro argument
by a decorated symbol requires an outer group. Corrected both source trees:
`\frac ML -> \frac{\bar{m}}{\bar{n}}`,
`\frac a3 -> \frac{\mathsf{a}}{3}`,
`\frac am -> \frac{\mathsf{a}}{m}`,
`\sqrt a -> \sqrt{\mathsf{a}}`, and the analogous companion finite-product
size fractions, inverse-amplitude fractions, and indicator fractions.
Introduced decorated exponent/subscript arguments are grouped, including
`\mathsf{w}^{\mathsf{K}}`, `\sum_{k=1}^{\mathsf{k}}`, and
`\int_{\hat{\varepsilon}}`. A dedicated fixed-argument scan found no
remaining unbraced decorated argument in frac/tfrac/dfrac/sqrt or in a
superscript/subscript. Ordinary sin/cos/log/cot/tan arguments were inspected:
they accept an expression sequence and retain the intended decorated symbol.
No operatorname text was renamed. The companion's generic Bernstein
polynomial T and derivative-order j were restored in its local paragraph;
these are distinct from the model constants.

The first companion compile caught the indicator-fraction grouping case;
it was corrected before the successful converged rebuild. This source
correction is included in the candidate identities above. Both completed
build logs have zero TeX errors, undefined references/citations,
multiply-defined labels, warnings, or overfull boxes. Underfull diagnostics
remain and do not signal clipping. Template files were copied from the
existing output directories only after verifying their pinned SHA-256 hashes;
the new build scripts verified them again and performed no retrieval.

Build commands (from repository root):

```sh
PADUA_PAPER_OUTPUT_DIR=/workspace/padua_research/local-output/padua-argmax-bridge-20261105/notation-paper-20261108 bash topics/padua-argmax-bridge-20261105/paper/build.sh
PADUA_COMPANION_OUTPUT_DIR=/workspace/padua_research/local-output/padua-argmax-bridge-20261105/notation-companion-20261108 bash topics/padua-argmax-bridge-20261105/companion-paper/build.sh
```

`local-output/padua-argmax-bridge-20261105/notation-paper-20261108/main.pdf`: 646715 bytes; SHA-256 `53c02839ce22fd375d945bd6546b2465f94a16c8ebdf384e2efa197b5b532a0d`.

`local-output/padua-argmax-bridge-20261105/notation-paper-20261108/main.log`: 40314 bytes; SHA-256 `3e9f1f498e7f86761ba06551e55a5422084960679266b44b9890aec5b7914613`.

`local-output/padua-argmax-bridge-20261105/notation-companion-20261108/main.pdf`: 1166321 bytes; SHA-256 `5f64703fbfc5d29b1885ef2f1c653cecdb6e10b9d3bb3cb66124b5e809c71900`.

`local-output/padua-argmax-bridge-20261105/notation-companion-20261108/main.log`: 50173 bytes; SHA-256 `4f305c2d2e3fe5c8dead8327e9055aac224d958c0b2e48116fab301768212195`.

