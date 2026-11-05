# Gate: nearest-neighbour MOP IEP and the bivariate pair

Rules/input head: `320fe07f5231ac7e72a4da45e64a38e5ff381b4a`.
Literature campaign input: `d669363` (pinned Git objects, not a branch merge).
Reader: Codex bounded gate developer, gpt-6.1-sol xhigh as dispatched;
exact backend runtime metadata is not exposed. Date: 2026-11-05.
This is a novelty/attribution assessment, not a new theorem or an audit.

## Decision

**Reduces to known exact MOP constructions, with a finite common-support
boundary qualification.** Nearest-neighbour (NN) compatibility and its
inverse/boundary-data formulations are established literature. They do not
identify the NN problem with the Van Barel–Chesnokov bivariate commuting-pair
IEP. A new stable path updating method has not been specified or established.
Stop the proposed new-method campaign at this gate; preserve the exact
finite clarification and scoped failed division rule as background/negative
records. This does not close the broader stability or updating questions.

The reason for stopping is the known exact reduction and failure of the
suggested commuting-pair identification. It is **not** an assertion that C4
has proved comparable floating-point stability or cost. No such comparison
was performed or found in the sources read. A floating-point comparison of
C3 with C4 would require a distinct, fully specified C3 algorithm first.

## Registry scan and provenance

- Read AGENTS.md, agents/WORKFLOW.md, agents/codex/CODEX.md and the full open
  handoff `handoffs/01-work.md` at the input head.
- Read all 889 lines of `state/IDEAS.md` in bounded raw chunks: 1–100,
  101–200, 201–300, 301–410, 411–515, 516–625, 626–720, 721–795,
  796–889. Re-read 660–690 to repair the single truncated output in
  626–720. Thus every obstruction/disposition table, including its scope
  and resumption conditions, was read in full.
- Scanned every `literature/INDEX.md` LIT row by identifier, source key and
  statement prefix, in bounded chunks over all 518 lines; repaired the
  truncated third chunk at 362–409. This was a source/summary scan, **not** a
  claim to have read all full row statements or all source papers. Read the
  full targeted rows LIT-117/118/119, 346–348 and 420, and the relevant
  Van Barel–Chesnokov record/rows. The INDEX flags many imported assertions
  as secondary and UNVERIFIED; those flags were not silently upgraded.
- Read PROOF_STATUS.md rows PD-T029–080, and the full PD-T057 theory file
  `tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-301-truncated-favard-sections.md`.
  Read the complete shortlisted predecessor entries/aliases in IDEAS and
  the linked baseline inventory, especially seed 014, 035 and 041.
- Searched `state`, `tracks`, `topics`, `literature` Markdown for
  `nearest.neigh`, `multiple orthogonal`, `MOP`, `Angelesco`, `Nikishin`,
  `Jacobi ... tree`, `Hermite.Pad`, `multiple Toda`; inspected mechanism
  context for commuting multiplication, compatibility, step-line, block
  Krylov and IEP. This includes theory and negative-result homes under
  `tracks`, not just title matches. No repository-wide theorem of
  impossibility for every possible NN formulation was inferred.
- Read at `d669363`: `topics/padua-literature-20261103/p4-memo.md`,
  `literature/records/filipuk-haneczok-vanassche-2015.md`,
  `topics/padua-literature-20261103/addenda/faghih-vanbarel-vandebril-2026.addendum.md`,
  `topics/padua-literature-20261103/notes/faghih-sinum-2026-assessment.md`,
  `literature/records/vanbarel-vanbuggenhout-vandebril-2023.md`.
  These are other readers' records; their primary-reading coverage is
  distinguished from this reader's primary checks in [literature.md](literature.md).

## Closest entries and applicable obstructions

| Entry | Relevant content | Consequence for this task |
|---|---|---|
| IDEA-031 (F5/rank 6) | NN MOP coefficients computable through univariate/step-line methods and FHV; stability source-reported open; finite-support limits | Exact computability is already registered background. |
| IDEA-117 = IDEA?bivariate-lanczos-claude-041, F5/R3 | NN IEP; misleading alias “bivariate discrete MOPs”; deferred to an AC request/Leuven coordination | This task resumes that entry. It does not create a second NN idea under a new name. No contact was made. |
| IDEA-090 = seed 014 | MOP conditioning through block-Krylov angles; separate univariate problem | Conditioning remains outside the present exact reduction. |
| IDEA-111 = seed 035 | Humet vector-weight/generalised implicit-Q context; unpublished proof gaps | Cannot import a uniqueness theorem for a proposed new coupled update. |
| IDEA-193 | Toda/qd on bivariate block Jacobi pairs judged equivalent to measure modification | Do not rebrand known transformations as a new mechanism. The one-variable MOP Toda literature supplies additional, different prior art. |
| IDEA-034; IDEA-085/172; PD-T057/076 | Moment/flat-extension background; one-operator versus genuinely graded two-operator distinctions | Their hypotheses matter. PD-T076 concerns reproduction of bivariate graded spaces, not impossibility of univariate MOP block Krylov methods. |

The full obstruction/disposition tables also warn against transferring
positivity to arbitrary fields, claiming all-index normality at finite
support, or replacing exact sections by arbitrary compressions. None is a
blanket ban on MOP algorithms. PD-T057 describes symmetric bivariate
sections of a scalar moment functional: the commutator may survive in the
last block. Its converse does not automatically provide a positive
representing measure. It must not be simplified to “all truncated pairs
commute.”

## Dictionary and mismatch

The two MOP measures act on **one polynomial variable**. For
\(\nu=(n,m)\), \(P_\nu\) is monic of degree \(n+m\), with two sets of
orthogonality constraints. Both NN recurrences multiply by the same scalar
variable \(z\). The two directions change how many constraints are imposed
against each measure. They are not multiplication by two coordinates.

In the bivariate finite IEP, one positive measure on nodes \((x_l,y_l)\)
gives two diagonal operators \(X,Y\), the **same** orthogonal basis change
\(Q\), and \(H_x=Q^*XQ, H_y=Q^*YQ\). On the full node space the pair
commutes. Its total-degree polynomial blocks have sizes \(1,2,3,\ldots\).
In contrast, the triangular collection of MOP indices is redundant as a
collection of polynomials in \(z\): through degree \(d\) it contains
\((d+1)(d+2)/2\) indexed polynomials in a space of dimension \(d+1\).
Its triangle is not a bivariate graded basis.

The faithful NN object is a site-dependent transfer system. With a suitable
state, \(\Psi_{\nu+e_i}(z)=R_i(\nu;z)\Psi_\nu(z)\), and compatibility is

\[
R_2(\nu+e_1;z)R_1(\nu;z)
=R_1(\nu+e_2;z)R_2(\nu;z).
\]

The factors are at different sites. This is discrete flatness, not the
same-site equation \([R_1(\nu;z),R_2(\nu;z)]=0\). It is established in
Van Assche 2011 §3 and in FHV §3.3; the Hermite–Padé literature proves
converses as well. Flatness can be represented by commuting covariant
shift operators on lattice-valued states where the necessary transports
are invertible. Their domain, site shifts and parameter \(z\) remain part
of the construction; this gives no bivariate positive-measure IEP.

For common finite nodes the natural spectral input is one
\(D=\operatorname{diag}(x_l)\) and two weight vectors. Different path
bases, when nonsingular, give different representations of this same
operator; their changes of basis intertwine these representations.
Biorthogonal similarities are not the single unitary similarity of the
bivariate pair. Neither the existence of such intertwiners nor the
trivial pair \((D,D)\) supplies the proposed faithful two-coordinate
dictionary.

ADY's tree construction unfolds distinct monotone paths into distinct
vertices, even when they project to the same multi-index. It produces one
Jacobi operator on that enlarged tree, under stronger assumptions; it does
not supply two commuting matrices on the original N-node space. Likewise,
the 2D discrete Schrödinger and Toda constructions concern index-space
operators or spectral deformations of one-variable MOPs. Their word “2D”
does not turn \(z\) into two polynomial variables.

## Correcting C4 and the finite boundary

FHV §2 propagates a **family** of shifted step-lines in both directions.
Two fixed shifted lines do not enumerate the whole lattice. The main
step-line also leaves an ambiguity in the second measure; its actual
first moment fixes the additional initial parameter. Therefore the
handoff's literal two-lines recipe needs correction before it is a
baseline. The simpler exact comparator is: compute the two marginal
univariate Jacobi recurrences, then use FHV §3.1/Thm 3.3 on a regular
region. Alternatively use the complete recursive shift construction with
the required boundary data. These are known algebraic conversions.

Their division hypotheses cannot be extended unchanged through a shared
finite-support terminal layer. On N common nodes, each normal total-degree
N polynomial equals \(F(z)=\prod_l(z-x_l)\). Thus two normal successors
of a degree N−1 index coincide and their NN diagonal coefficients agree.
The divisor \(b_{\nu,2}-b_{\nu,1}\) is then zero. This is a failure of a
specified unmodified propagation rule, not a failure of the finite moment
systems, nor a counterexample to FHV under its hypotheses. See
[finite formulation](theory/finite-moment-formulation.md) and
[terminal division record](theory/terminal-division-obstruction.md).

Kozhan–Vaktnäs, arXiv:2407.13946v2 / JCAM 2026, is especially relevant:
§3.2 extends the compatibility algorithm to finite perfect systems, and
§3.8 gives a Favard-type characterization with initial/final boundary
zeros. This rules out claiming that finite-support NN inverse theory is
absent. Its Definition 2.8 requires normality on the whole rectangle
\(0\le\nu_j\le N_j\). Two measures on the same N nodes cannot satisfy
that condition: the mixed moment rank is at most N while the rectangle
contains \((N,N)\). Consequently that theorem is not a direct all-input
solution of our common-support triangle. Local normality and terminal
treatment still have to be stated; the elementary finite formulation does
that without claiming novelty.

## Candidate disposition and resumption test

| Candidate | Gate disposition | Exact separation required before further work |
|---|---|---|
| C1 finite exact data | Equivalent/background, with an explicit common-support domain qualification | A new result must go beyond defining moment systems/known NN relations; changing finite notation does not suffice. |
| C2 NN as the bivariate commuting pair | Proposed literal identification fails; preserve the scoped mismatch | Supply a common space, two operators, basis/weight conditions and a faithful dictionary. Site-shifted flatness alone fails this test. No impossibility of every artificial embedding is claimed. |
| C3 path-wise node updating | Deferred, rather than declared impossible or algorithmically equivalent | Specify a coupled representation, every maintained weight/biorthogonality/compatibility/boundary invariant, update and breakdown rules, then prove a cost or stability advantage over a corrected known baseline. A single-path step-line update is already prior art. |
| C4 exact baseline | Known after correction; literal two-lines/all-divisors version is insufficient | Full finite coefficients must be produced with the actual marginal/boundary data. Comparable floating-point stability and cost remain unproved, not assumed. |

No distinct C3 mechanism survives this gate in a form that can be tested.
Further stability or path updating work requires a new, explicitly scoped
question; the source authors' future-work lists are motivation, not an
absence-of-prior-art theorem. No message to the Leuven group was sent.

## Coverage limits

The search was bounded, not exhaustive. Primary reading includes the
mandatory Van Assche, FHV and ADY foundations and selected later inverse,
Toda and finite-support results; exact pages and gaps are in
[literature.md](literature.md). The Leuven 2026 numerical statements here
come from the pinned campaign readers' assessments, not a fresh run or
fresh primary read by this gate worker. Follow-up tree spectral papers
were inspected only at the abstract/introduction level. No conclusion of
global novelty, optimal complexity, stability equivalence, or impossibility
of stable NN updating is justified by this coverage.
