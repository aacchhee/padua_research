# Primary-source recheck for response-01, F1 and N1

Date: 2026-11-05. Reader: Codex bounded mathematical developer.
Rules/input head: `9ec2a54c5b6af56514feaf11c9fc329f19a88820`.
Requested model allocation: gpt-6.1-sol xhigh; exact backend metadata
is not exposed. This is developer source verification, not an independent
audit or an expansion of the original literature campaign.

## Access and gate

Read AGENTS.md, agents/WORKFLOW.md, agents/codex/CODEX.md,
handoffs/03-response.md, audit-01 F1/N1, gate.md and literature.md.
Read the INDEX's introductory provenance caveat and searched its existing
NN/MOP/FHV rows before opening primary PDFs. The existing complete gate
is inherited only as a recorded prior gate; this worker did not repeat its
full IDEAS reading or open a new candidate. Scope: correct the interpretation
of known exact algebra and split existing substantive statements. No novelty
claim or new mechanism is proposed.

The managed executor reports enforced restricted networking and omits
arxiv.org from its allowed hosts. No shell PDF retrieval was attempted
by this worker; the earlier shell 403 is an earlier session's receipt.
The available `mcp__codex_apps__search_service_web_run` service successfully
returned primary PDF text for all three requested sources. Direct versioned
URLs were used for the final locator checks. No paper copies, browser
screenshots or extracted third-party text were written into the repository.

## FHV 2015: checked induction and exact divisor layers

Source: Filipuk–Haneczok–Van Assche,
[arXiv:1406.0364v2](https://arxiv.org/pdf/1406.0364v2),
23 January 2015, 22 pages. Page locators below are printed arXiv pages,
not Numerical Algorithms journal pagination.

Read §3.1's compatibility equations, axis data, Theorem 3.1 and full
induction, pp. 16–18; read §3.3 equations (3.11)–(3.15), Theorem 3.3
and its complete induction, pp. 20–21. The r=2 source notation is
(a,b,c,d)=(our a_1,a_2,b_1,b_2); source d is not our difference d_nu.

Faithful paraphrase: assuming coefficients through layer k, the lower
coefficients on layer k+1 follow from (3.7)–(3.8), using differences at
k-1 as denominators and at k as numerators. The remaining diagonal
coefficients follow from a two-equation system, (3.9)–(3.10), with a
difference at k as determinant. The general-r proof uses the same
degrees: (3.14) divides at k-1, and (3.15) divides at k. Both proofs use
marginal coefficients on the axes.

Local consequence, independently proved in
[PD-T?nn-mop-iep-codex-04](theory/marginal-reconstruction.md): stopping
at target layer N-1 uses only differences through N-2. The source's
global nonzero assumption need only hold at the divisors actually used
in this finite application. Its theorem statement is not itself being
quoted as an all-input finite-triangle theorem.

Coverage gaps: this round did not recheck §2's step-line conversions,
their initial-parameter issue, example computations, or Maple code.
No FHV implementation was executed.

## Van Assche 2011: compatibility theorem

Source: Van Assche,
[arXiv:1104.3778v1](https://arxiv.org/pdf/1104.3778v1),
22 pages. Read Theorem 3.1, (3.1)–(3.4), and its proof ending after
(3.5), printed pp. 9–10; also rechecked the surrounding normality
definition and determinant identity (2.12), printed pp. 2–3 and 9.

The theorem assumes normality of all indices and gives the two diagonal
compatibility equations and the two lower-coefficient ratio equations.
Its proof compares the two transports to the same opposite corner.
The local proof in PD-T?nn-mop-iep-codex-04 instead uses polynomial
identities and proves that every needed square lies within degree N.
Neither a global Riemann–Hilbert construction nor its invertibility
outside that finite domain is imported.

Coverage gaps: no complete recheck of the earlier Riemann–Hilbert
construction, general-r proof, later examples or cited dependencies.
The PDF shows the arXiv v1 identifier and 2011 submission but also a
different internal compilation date; the versioned URL is the source
identity, and no file hash or journal pagination is claimed.

## Kozhan–Vaktnäs: finite-domain hypotheses and CC algorithm

Source: Kozhan–Vaktnäs,
[arXiv:2407.13946v2](https://arxiv.org/pdf/2407.13946v2),
19 November 2025, 31 pages. Checked §2.2 finite-functional sizes,
printed p. 5; Definition 2.8 and the rectangle immediately preceding it,
p. 8; Lemma 2.18(b) and its proof, p. 11; §3.2 Theorem 3.6,
its proof and Remarks 3.7–3.8, pp. 16–17.

The source defines perfectness on 0<=nu_j<=N_j, with N_j determined
by the marginal finite functional. Its CC algorithm orders coefficients
by total degree and computes differences only where both successor
directions are available. Remark 3.7 invokes Lemma 2.18(b) to guarantee
nonzero differences there. That lemma makes opposite-corner normality
equivalent to a nonzero difference when the three other indices are normal.

The local common-support rank argument in PD-T?nn-mop-iep-codex-04
checks why this perfect-rectangle hypothesis is not met when both
positive measures have exactly N common nodes. This comparison does not
claim the algorithm fails on the normal triangular subdomain.

Coverage gaps: Theorem 3.19 and its inverse characterization were not
rechecked in this response. No journal-version text or code was checked.
The earlier reading ledger's other coverage remains attributed to its
original reader.

## Additional primary check for the F3 baseline

At the orchestrator's request, checked
[arXiv:2608.25758v1](https://arxiv.org/pdf/2608.25758v1), §5.1,
Examples 5.1–5.2, printed p. 20. Both examples use N support points
i=0,...,N-1. The weights are

    Kravchuk: binom(N-1,i) p_j^i (1-p_j)^(N-1-i),
              p_1=0.4, p_2=0.5;
    Hahn: ((beta_j+1)_i/i!)
          *((gamma+1)_(N-1-i)/(N-1-i)!),
          beta_1=1, beta_2=1.5, gamma=1.

Here (a)_i is the rising factorial. The last Hahn factor is N-i when
gamma=1. This verifies input convention only. No paper experiment, plot,
implementation, or stability conclusion was reproduced by this worker.

## Disposition and residual coverage limits

F1 is confirmed: the exact reconstruction ends before a terminal zero
difference could become a divisor. The separate written proof reconstructs
(A), (B1), (B2), handles axes and N=1, and proves the layer induction.
The terminal equality remains a necessary final boundary condition.

N1 is resolved only for the listed primary locators. ADY 2020, ADV 2016,
ADV 2015, the Toda paper, Kozhan–Vaktnäs Theorem 3.19 and other earlier
literature reports were not newly rechecked. This developer check does
not retroactively turn audit-01 into a primary-source audit. It supplies
inspectable versioned links and explicit coverage for the required
Claude re-audit. Floating-point stability and partially normal regions
remain outside the mathematical result.
