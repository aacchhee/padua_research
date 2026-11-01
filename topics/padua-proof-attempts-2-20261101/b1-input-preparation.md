# B1 input preparation — no B1 mathematics started

Prepared by Codex, requested `gpt-6.1-sol xhigh`, on 2026-11-01. Runtime-resolved model metadata beyond that designation is unexposed. Rules and input head actually read: `3062f77f5ead1d888fa319a7c3a20371d4f305f7`.

This is a reading and source-pinning record only. The parent authorized preparation while A4(a) is active; B3 must stop before the parent explicitly starts B1. **No B1 timebox, mathematical development, candidate generation, proof attempt, code development, mathematical computation or rerun has started.** Administrative file hashing below is input identification only. A5 mathematics stopped at its original 15:19 UTC ceiling; its sources and evidence were not changed for this task. Only this new file is owned/written here. No Git, handoff, ID allocation, shared registry or upstream-file mutation was performed.

## Authoritative statement and definitions to retain

The current programme `OPEN_TARGETS.md`, B1, is authoritative. Its statement is unchanged by the main-input updates between the previously read rules/input commit `842dfaaeff524b4db4141d314afff6ad4a5b7721` and the input head above. Those updates add part 1 status/context and the MZ campaign registration; they do not close B1.

Use the source notation, without silently changing formal rational functions into sampled vectors:

- `Pi_t` is the bivariate total-degree polynomial space. `pi_t = ell_1 ... ell_t`, with one affine linear pole factor per degree; `V_t = Pi_t / pi_t`.
- On `M` specified nodes with positive discrete weights, `W_t = V_t orthogonal-difference V_(t-1)`. The inner product and its real/complex convention must be fixed for the chosen class. The code library uses `sum_i w_i conj(f_i) g_i`.
- `P_(W_s)` is the orthogonal projector for that discrete inner product.
- `C_t = span{(W_(t-1) + W_t + x W_t + y W_t) / ell_(t+1)}` and `R_t = (I - P_(W_t) - P_(W_(t-1))) C_t`.
- The OPEN target is `W_(t+1) = {r in R_t : r perpendicular W_(t-2)}` for general-position poles and `t >= 2`. Its stated consequence is orthogonality to all `W_0,...,W_(t-3)` for every vector in that constrained remainder.

The complete current hypothesis list, including the audit/response clarification, is:

1. Every `ell_s`, `s <= t+1`, is nonzero at every sampled node.
2. Evaluation on the nodes is injective through `V_(t+1)`; dimensions are full, including `dim W_s = s+1` through the required degree. The source explicitly requires enough nodes, `M >= dim Pi_(t+1)`.
3. Fix a finite admissible ceiling `T`: `2 <= t <= T` and `dim Pi_(T+1) <= M`. A finite node set does not supply an unlimited-degree assertion.
4. Choose and state one pole class from the source, rather than importing all classes at once.
5. Specify the class's real/complex parameter coordinates. Here “general position” means outside a proper algebraic subset of that class's pole-parameter space, to be identified in a later proof. The exception set and its properness remain proof obligations. A generic joint-data statement must not silently replace the source's pole-class statement.

`response-02.md`, row B4.6, and `audit-03-support/targets-review.md`, row B4.6, accept this as an OPEN target template. Neither record proves the recurrence. B1 remains OPEN; PD-N040 is a scoped MEASURED implementation failure, not a rejection of this target.

## Pole-class dictionary from the existing inputs

The following is a transcription of the source definitions, not a choice of class or a new family. The library writes `ell(x,y) = a*x + b*y - c`; each conjugate pair occupies two successive degrees. Its line factory requires an even final degree, although intermediate degree blocks include odd indices. Its taper is `epsilon_j = exp(-sigma*(sqrt(m)-sqrt(j)))`, with the endpoint convention fixed in `taper`; far-first and near-first orderings differ.

| Existing name | Source definition / convention | Scope caution for the later attempt |
| --- | --- | --- |
| `Ppt` | Conjugate pairs of `x + i*y - zeta_j`, with `zeta_j = (1+i) + epsilon_j*exp(i*pi/4)` | Specify the real parameter coordinates and Hermitian convention; do not inherit the real-line proof sketch unchanged. |
| `Pbhh` | Conjugate pairs `x = 1 +/- i*epsilon_j` and `y = 1 +/- i*epsilon_j`, interleaved by edge | Fix the order and how a finite odd prefix is interpreted. |
| `Ldiag` | Real parallel lines `(x+y-2)/sqrt(2) = epsilon_k` | Parallel lines are a specified class, not general-position lines in the unrestricted line space. |
| `Pdiag` | Conjugate diagonal pairs `(x+y-2)/sqrt(2) = +/- i*epsilon_j` | Present in the authoritative B1 class list and library, but not in the actual `window_exact.py` class dictionary. |
| Generic real lines | `cos(theta_k)*x + sin(theta_k)*y - c_k`; stored diagnostic samples use `abs(c_k)` between 1.6 and 2.5 | The sampling recipe and sampled coefficients do not define or prove the requisite algebraic exceptional set. |
| `Mpt`, supplementary diagnostic | Initial constant factors `ell=1` (“lines at infinity”), then point-pole pairs | Appears in the exact-block diagnostic in place of `Pdiag`; it is not one of the authoritative B1 classes listed there. |
| `P`, control | All factors `ell=1`, polynomial blocks | A control, not evidence for a general finite-line rational class. |

No pole class has been selected or specialized in this preparation.

## Recorded predecessors, obstructions and input hazards

Closest full entry: **IDEA-192**, aliases `IDEA?programme-ideas-claude-03`, `gen1-draft-3`, bivariate ORFs, pencil-pair IEP, windowed rational Lanczos, three-block window, and “project two, constrain one.” Read its complete candidate record, programme registry/disposition table and complete **PD-N040** record. The canonical disposition rejects the tested windowed solver mechanism at its stated scope; it does not prove that the rational-function family or B1 is false.

The part 1 `attempts/T-B1-optional.md` stopped at a particular closure obstacle: transferring orthogonality by division by the new real nonvanishing pole would require membership of the divided test function in an older nested rational space. Its formal rational-function divisibility argument does not supply that closure. The attempt explicitly distinguishes a failed route from a finite-node counterexample and warns that accidental sampled relations are a different issue. That existing obstacle is retained; it was not re-proved or extended here.

The adversarial source's top-form/gauge sketch is conditional on generic ranks. It introduces `U_(t+1)=Pi_(t+1)/pi_t`, a top-form map to homogeneous forms, an asserted generic bijection from `W_t` to the degree-`t` forms, the gauge kernel, and a skew form. Its parity conclusions depend on the unproved generic-rank assertions. Generation of `ell_(t+1) W_(t+1)` from a small window does not by itself identify the kernel of the later `W_(t-2)` constraint. No rank assertion or parity claim from that sketch is promoted into a local proof here.

The decisive source corrects an older ambiguity: the dimension of a complement inside `C_t` is different from the rank of a projection remainder. Projecting off three old blocks is not interchangeable with projecting off two and then imposing an orthogonality constraint. The programme negative record labels its finite evidence MEASURED. Despite “EXACT blocks” in the diagnostic filename/docstring, `window_exact.py` constructs those blocks with double-precision QR, uses SVD thresholds (`1e-10` relative and `1e-8` absolute in the indicated decisions), and reports floating residuals. `orf2d.py` also documents enforced block dimensions in the recurrence after floating rank decisions fail. None of these files is an exact-arithmetic proof certificate.

Two literal source/coverage details require care before using the measured summaries:

- `topics/programme-ideas-20261031/checks/code/decisive/gen1-3/window_exact.py:37` (dictionary continued on line 38) actually tests generic real lines, `Ppt`, `Pbhh`, `Ldiag`, `Mpt`, and the polynomial control. `OPEN_TARGETS.md:49` names `Pdiag` instead of `Mpt`; the library implements `Pdiag` at `orf2d.py:130`. Coverage of one must not be reported as coverage of the other.
- The literal `Pbhh`, `t=9` row at `topics/programme-ideas-20261031/checks/code/decisive/gen1-3/window_exact.out:33` says “need 11”; **B(proj2,con1) has rem 19, constraint rank 8, kept 11**, consistent with that dimension, while the alternative **A(proj3,con1) has rem 19, constraint rank 7, kept 12**. Do not conflate that alternative with B1's project-two/constrain-one target. An initial preparatory message misread a truncated display as attributing kept 12 to B; the untruncated literal read corrected that error before this file was finalized, and the parent was explicitly notified. There is no B1-target mismatch in that stored row. These are floating diagnostic data, **not an exact or general-position counterexample**. No rerun or adjudication was performed here.

Other boundaries retained from PD-N040: rotation-based IEPs, selective/partial reorthogonalization, pole-cancelled candidate forms, untested placements/orderings and higher degrees are outside that negative's tested scope. They are not proposed as new routes here. Numerical stability or instability of an implementation does not decide B1's exact subspace identity.

## Preparatory registry and source scan

This adds no novelty-bearing mechanism, claim or candidate. It is a preparation refresh of the previously recorded complete relaxed gate, not permission to skip the gate when B1 actually starts. Scanned the complete current registry heading list; searched identifiers, aliases and mechanism synonyms across `state`, `PROOF_STATUS.md`, `ID_CROSSWALK.md`, `tracks`, the programme and bivariate-Lanczos topics, the part 1/part 2 topics, and `literature`. Terms included `rational window`, `nested pole`, `one-linear-pole`, `top form`, `gauge`, `project two`, `constrain one`, `pencil pair`, `Ppt`, `Pbhh`, `Ldiag`, `Pdiag`, and the provisional/final programme aliases.

Read the relevant programme candidate and obstruction/disposition tables in full, the common recorded obstruction tables, the complete new MZ registration/obstruction/disposition addition, and the full shortlisted rational candidate/negative/attempt/source records. Compared registry/OPEN_TARGETS changes since `842dfaa` read-only: the rational candidate and PD-N040 scope are unchanged. The new MZ records concern signed-weight/aliasing arguments, not a proof of this rational-window identity. Bivariate polynomial-window stability, gauge or fixed-start records returned by the synonym scan are contextual neighbours, not inherited rational recurrence results. No new shortlist mechanism or separation claim is introduced.

Consulted `literature/INDEX.md` by mechanism/source-name searches before source-specific attribution checks. Existing references to Bultheel et al.'s univariate ORF book, Van Buggenhout et al., BHH and the other papers remain coverage-qualified source reports in the programme records. No new web search, primary-paper inspection, priority claim, author contact or third-party fulltext/PDF ingestion was performed. The historical generator pointer `checks/state/gen1-draft-3.md` is absent from the current repository; the complete current candidate record and retained scientific sources above were read instead. This is not a claim to have read that missing file.

## Source-prescribed next step — reserved for the later authorized start

Part 1's explicit next step is: express the lower-block leakage of the projected candidate space through the top-form functional, then prove that restriction to `W_(t-2)` detects every leakage direction for a precisely stated pole class. A generic-rank assertion needs a structural proof or an exact nonzero polynomial witness, with the finite-sampling hypotheses stated. The current user request allows, alternatively, a general-position counterexample. This preparation does not choose the class, construct that functional, derive a rank condition, propose a witness or run a test.

After B3 stops, the parent must explicitly start B1. The later developer should first refresh current inputs and the full relaxed gate, then record the actual B1 start, its approximately two-hour ceiling and kill criteria in its own attempt record before mathematics or runs. B1 remains OPEN. Part 2 Claude audit remains PENDING. This preparation has no new theorem, negative-result or candidate ID and requires no allocation.

## Exact input pins

The following table is administrative provenance. Paths are repository-relative, all blobs are from the input head `3062f77f5ead1d888fa319a7c3a20371d4f305f7`, and each working file was compared to that blob before recording. No source module was imported or executed.

| Path | Git blob | Bytes | SHA256 |
| --- | --- | ---: | --- |
| `AGENTS.md` | `07cd8c8920fabccc16dce4a63fe853a2f3a26f3d` | 3572 | `c44a76f138fce01f02c06753b22fbc83fd5c1ee701785d49ba17cef5f8eee05b` |
| `agents/WORKFLOW.md` | `cca18dccfbc9c56754920d2905919e6bb69498e9` | 25921 | `3ac67448c6d0bd98c057262d60a01cf46fd0ae9df2643e4d8f20ef163f998d5e` |
| `agents/codex/CODEX.md` | `16a4ecfea89acd5b1d9cd09c9213094bce144caf` | 4969 | `28ca2976171a34860e2bf8d24292af6b92bee34ce22ba1e497891b366533083b` |
| `state/IDEAS.md` | `a3fd0aa42e7f90c64d012f410d2c0c95671718e7` | 170639 | `4a7f365d0932048d4e861a817e758077f9c715c936d2191b1c2a5da63d14d0bb` |
| `PROOF_STATUS.md` | `095a29706f03b5f6dac42e725c915c3ebc3802fe` | 112158 | `641d1aac027dd53f11dad22f327c694eb0ee880e4c355a4cc5eb736d6188231b` |
| `ID_CROSSWALK.md` | `327ec7fcb42bfc9f29dc327d2a813e52d267b08e` | 263250 | `73da371370b82b19452cf2aa6ae9daf90d212d744527c6f4f550133dcb846988` |
| `literature/INDEX.md` | `b6fad245a44916d958b0d810653522a1036c5281` | 268372 | `3cd4a057587459b117e555f1cae615e9985b770206c9b96d199a7161cc1a975e` |
| `topics/programme-ideas-20261031/OPEN_TARGETS.md` | `98f83956714b002e229cd9ad9b3c9072f19c4591` | 19652 | `c181d688edc8927b23e273f2a5f6542e950652b9bd892e5a96c89d2e3e199157` |
| `topics/padua-proof-attempts-20261101/attempts/T-B1-optional.md` | `3b90563c75d258b388aa5b39c6ddc68c89803da3` | 3229 | `8caa5f79534c9ae3381dd9d91a70dc6168ec409722c658c446f477af60c502e7` |
| `topics/programme-ideas-20261031/ideas/candidates.md` | `7d17cbf648921701c2e3bd9d1ae4d3eb7b461367` | 126236 | `2658ac851dcb2d5f3da0212c0ec827f377e15d4170e6718995a20b9d70311a99` |
| `topics/programme-ideas-20261031/theory/programme-ideas-claude-N02-windowed-rational-lanczos-instability.md` | `601b7d4be7d9ac272f231b0b49f7570a172f671c` | 5860 | `3c96bff3b0827f343932f22b3c629fd7e367a7d19a0d16ccae0ed339d0ccd8ed` |
| `topics/programme-ideas-20261031/checks/decisive-gen1-3.md` | `363e03e2c7a9af8cce4d9c23c558a79cfb699eef` | 30028 | `3e950d1b47b8ec87ffd9ebeed91f8fd27f22f4716d23507918f98dd86eb7825e` |
| `topics/programme-ideas-20261031/checks/adversarial-gen1-3.md` | `9a8dfd4caf930a6805b043432847f3f5725efaa5` | 32289 | `33e335c9ebb2b7a0d7951b07973654dc68ba323a0412b5d4e6a251b83fefa277` |
| `topics/programme-ideas-20261031/checks/code/decisive/gen1-3/window_exact.py` | `eaf15138f41bdfe3cbbf4a1f64d6ecf0d0827ea1` | 4546 | `abf066a0fe35355703586ad02701e3f3cfd55690e16a1f3da5b6749d292524c0` |
| `topics/programme-ideas-20261031/checks/code/decisive/gen1-3/window_exact.out` | `e7b47cc6875fe7b018bc7131dde5eb0010305e2d` | 15138 | `8354313abf496f9d62550daade12d5b148ff653b20ad1266c4e48d62cbc6a1e4` |
| `topics/programme-ideas-20261031/checks/code/decisive/gen1-3/orf2d.py` | `d21e6779f568282c7e9438a883ba12b8bb4d815a` | 19958 | `9e2197347a9125cc9f75178021c59d835bc3c85b7b63ef47d5e0213dc2287525` |
| `topics/programme-ideas-20261031/checks/code/adv/gen1-3/window_test.py` | `374f711b05fda5d8905769613bbf8d25491f92ed` | 9507 | `9f3d0a48d120647add35fa85eb4d6abf2f7b7f9128dad5962a2233679e351bf8` |
| `topics/programme-ideas-20261031/checks/code/adv/gen1-3/window_complex.py` | `118350bda2e409d8ad386021e261fdb554852aaa` | 3674 | `7fef756ca25e9a762b912929756668ab0eb5944d2d9f24a5487bac0a888f6619` |
| `topics/programme-ideas-20261031/response-02.md` | `f0b56384cca330fc6dad8c676da833801624abc4` | 6418 | `7da78e0fc01e408edcfcb2b2bf9cf4ba89af4efb0064fa86570da5306322a473` |
| `topics/programme-ideas-20261031/audit-02.md` | `d6d9de504749a1ff5d66b2173e35d0357aa7d3f1` | 18821 | `bde7f59ec66d1467541835b7a08d869ecd720ffa81a2e5a99e7f6ba258ffd60d` |
| `topics/programme-ideas-20261031/audit-03-support/targets-review.md` | `4f58c253339cb8225db6aaf1957bfedc28e36084` | 9397 | `032fefa89bab04dc6c4f75e5f3e90a6d0c6282d14a48690df12104151ac2a7ec` |
| `topics/padua-proof-attempts-2-20261101/handoffs/01-work.md` | `a42012daac90924d5dc34fc035a804e49a1babd2` | 5931 | `50bdc0f27aee5b62378d56f337f5a33ff7c98579266446edc50c79e682a76cb5` |
| `topics/padua-proof-attempts-2-20261101/plan.md` | `e6de67f0c9413daefc1b6071df3541146183d146` | 3966 | `1b5e05fb0f2a95000f64710a18ea29a206de11a643dff7340431f7e5e6587d31` |
| `topics/padua-proof-attempts-2-20261101/inputs-review.md` | `30f42de3a85cde0266cd7fbe22825e50508d5178` | 14557 | `64b064c47c5a93f8baf879066d818025f0f03cb4e3c5a5c6fe19a6413674b355` |

The user request was read from the supplied local attachment (not copied into Git): 9720 bytes, SHA256 `cc02c039c98fc7ec3e4fcb1f17b5bceeeca3431ec0b44c7af7341746573aeb8a`. Its B1 paragraph and ordered-target instruction agree with the parent's preparation-only scope.

Administrative completion: all 24 listed working files matched their pinned Git blobs when this table was written. No mathematical source code was executed. The preparation is complete and B1 remains unstarted.
