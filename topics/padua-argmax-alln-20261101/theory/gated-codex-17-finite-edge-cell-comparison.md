# PD-T?argmax-alln-gated-codex-17 — Strict whole-cell edge comparisons at n=7 and n=12

ID kind: PD-T.
Aliases: direction3 round1 finite E-C; centreward vertical-edge cells;
whole-source Bernstein bound versus target-center lower bound.
Split from: none; finite instances of the retained E-C candidate.
Split into: none. All-degree E-C and PD-T099 remain OPEN.

## Statement

Use the even-checkerboard Padua cardinals of PD-T101 and write
lambda_n(x,y)=sum_B|L_B(x,y)|. For n in {7,12}, m=n+1, j in {0,n}, put

\[
 A_j=\{k\in\mathbb Z:2\le k\le m-2,\quad j+k\text{ odd}\},
 \qquad
 E_{jk}=\sup_{k-1\le t\le k+1}
       \lambda_n(\cos(j\pi/n),\cos(t\pi/m)).
\]

For every k,k' in A_j such that k'-k is +2 or -2 and
|k'-m/2|<|k-m/2|, one has

\[
 E_{jk}<\lambda_n(\cos(j\pi/n),\cos(k'\pi/m))\le E_{jk'}.
                                                        \tag{1}
\]

Thus all ten eligible directed whole-cell E-C comparisons at these two
degrees are strict. No exact value of either supremum is asserted.

## Definitions and assumptions

The nodes are (cos(a*pi/n),cos(b*pi/m)), 0<=a<=n,0<=b<=m, a+b even,
with weights 2 eps_a eta_b/(nm), endpoint factors eps,eta=1/2. The
corrected coefficient kernel has h_p h_q for p+q<=n, h_0=1,h_r=2 for
r>0, except the coefficient of the (n,0) mode is 1.
The physical edge is x=+1 when j=0 and x=-1 when j=n; this distinction
also applies at even n. Each source closed cell lies entirely within
0<t<m because 2<=k<=m-2.

Mathematical predicates use Python integer/Fraction arithmetic and
outward intervals scaled by S=2^192. Soundness assumes the specified
cardinal formula, the existing proved outward constructor rules, and
correct execution of the pinned small checker. Floating trigonometry,
optimizers, sign stability and local-maxima enumeration are not premises.

## Status by part

Overall status: **PROVED**, computer assisted in the stated finite scope.
The written reduction, full certificate, development replay and distinct
actual producer/checker replay are complete. Claude audit-01 ACCEPTED the mathematics at its stated scope (record fixes pending); this status does not approve the rest of the campaign.

| Mathematical part | Status | Evidence / limits |
|---|---|---|
| Strict comparison (1) for all eligible n=7,12 directed pairs | PROVED | Ten complete two-leaf source covers and strict target-center bounds, separately replayed |

Candidate disposition: retained finite E-C variant of original
IDEA03/Claude03. The stronger E-P translation has a separate exact
counterexample in gated-codex-N02; its failure does not contradict (1).
No novelty, priority or external 1-D theorem claim is made.

## Depends on

- PD-T101: the all-degree corrected-kernel cardinal formula and node
  conventions. Its local proof dependency file is
  `topics/padua-proof-attempts-20261101/theory/proof-attempts-codex-01-padua-corner.md`,
  SHA-256 `ea59aa077a4d021fc69354383f69340f21d17d87d3a28c6ecaaf302cc763612c`.
- PD-T?argmax-alln-codex-03, including its general-constructor enclosure
  proof: rational Machin/Taylor cosine enclosures, corrected cardinal
  coefficient enclosures, exact rational Bernstein transforms and
  outward de Casteljau subdivision. The univariate sufficient reduction
  needed here is written below.

No global-maximum theorem at these degrees, asymptotic bound, fitted
constant, E-P inequality or original rhombus ordering is assumed.

## Proof

Restrict every cardinal to the exact physical edge, giving degree<=n
univariate polynomials P_B(y). The pinned constructor encloses each power
coefficient by an integer interval at scale S. Edge substitution uses
only sums and exact signs, so these enclosures remain valid.

For source center k let a be the lower rigorous cosine enclosure at
(k+1)*pi/m and b the upper enclosure at (k-1)*pi/m, both divided by S.
Cosine decreases on [0,pi], so the entire source closed cell maps into
[a,b]. Bounding that slightly enlarged physical interval suffices.

After the affine substitution y=a+(b-a)z, 0<=z<=1, the exact Bernstein
coefficient of y^i at degree-n index r is

\[
 \sum_{h=0}^{\min(i,r)}
  {i\choose h}a^{i-h}(b-a)^h
       \frac{{r\choose h}}{{n\choose h}}.                \tag{2}
\]

This follows by expanding y^i and using
z^h=sum_(r=h)^n [binom(r,h)/binom(n,h)]B_r^n(z).
Applying the exact rational weights (2) to the enclosing power
coefficients, with floor/ceiling at the final integer grid, encloses
every Bernstein coefficient c_(B,r). The nonnegative Bernstein basis
sums to one. Consequently, on any such interval,

\[
 \sum_B|P_B(y)|\le
 \max_{0\le r\le n}\sum_B|c_{B,r}|
 \le S^{-1}\max_r\sum_B\max(|\ell_{B,r}|,|u_{B,r}|).     \tag{3}
\]

Outward de Casteljau at 1/2 preserves these coefficient enclosures on
both closed children. The certificate supplies the two binary leaf
paths 0 and 1 for every source, so their physical intervals cover [a,b],
including endpoints and split boundary. There is no assumption on the
cardinal signs or the number/positions of extrema.

At y'=cos(k'*pi/m), rigorous cosine intervals and outward Horner
evaluation give enclosing intervals for each P_B(y'). Summing their
absolute-value lower bounds produces T_-<=lambda_n(x,y'). This remains
valid when an interval contains zero. The center belongs to the target
closed cell. The checker reconstructs the initial enclosing source intervals (the root boxes of the subdivision trees), all Bernstein
coefficients, the complete prefix cover and T_- from pinned sources.
For every leaf it checks the strict integer inequality U<T_-*S, where U
is the scaled bound in (3). Hence the maximum over source leaves is
strictly below the target-center value, proving (1).

The exhaustive finite directed-pair list is:

| n | edge index j | directed center pairs k -> k' |
|---:|---:|---|
| 7 | 7 | 2 -> 4, 6 -> 4 |
| 12 | 0 | 3 -> 5, 5 -> 7, 9 -> 7, 11 -> 9 |
| 12 | 12 | 3 -> 5, 5 -> 7, 9 -> 7, 11 -> 9 |

At n=7,j=0 the eligible centers have equal distance from m/2, leaving
no directed comparison. The checker reconstructs this full finite list
from the defining integer conditions; it does not trust a producer-supplied
subset. All twenty source leaves and ten strict inequalities passed
development and distinct-agent replays. These computations establish
every finite premise of the reduction. This proves the statement. ∎

## Checks and essential evidence

Input administrative checkpoint:
`3aebb299a4154dac822974b7245a9d243f21374e`; rules unchanged from
`aa1883f2fd9a837bb931ce804cb4b210c7475886`; scientific base
`7d308b10d946b607ae0690454f6c0103690775a4`. The pre-execution contract and
written reduction are `gated/d3/r01-contract.md` and `gated/d3/r01-finite.md`.

| Source | SHA-256 |
|---|---|
| `code/gated/d3_edge_common.py` | `fd3b278f167999def5a8f43ddd83da258e5ce2452a76082d9256dcde93d01b92` |
| `code/gated/d3_edge_generate.py` | `b0c2b98851dd8721bc876686fd388c62085938ff24d97308a132a7f14e9e3145` |
| `code/gated/d3_edge_check.py` | `5f43f69a427c415542848f8ae9e337c69b3a5b8f822e78db38e095a0a2c9a358` |
| `code/part3/finite_general.py` | `b20b7f88ddfc0bbc92e68096063ef626664028c2a379c34d16dc9f84e17aa74a` |
| `code/part3/finite_bernstein.py` | `a3133c6c22a365380f6c2ab14f6d31f60153d0df902b325cfcfbeeccc1bed74f` |
| `code/part3/finite_n2_exact.py` | `a5f00e6039d6ec76660cac90fb5720e0d6721348ed34c9e62775e1125d3e87c2` |

The complete certificate `outputs/gated/d3_edge_certificate.json` is
13561 bytes, SHA-256
`0d660fc70e9db06624d6f8bd82371602c9f6d540b01124824e264624de0385b7`.
The development checker receipt `outputs/gated/d3_edge_check.json` is
9696 bytes, SHA-256
`7fd1ca1b8c94ea1f1f2e699de1b9aa2a70f4e749d7fcf1dc34291bb376fe2f05`.
It records accepted=true and seventeen malformed-input rejections.
The smallest strict scaled margin divided by S is approximately
.008105212862571 at n=12,k=5->7, on both actual vertical edges.
This decimal is descriptive; the certificate records the exact integer.

The executed commands from the repository root were:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-argmax-alln-20261101/code/gated/d3_edge_generate.py --output topics/padua-argmax-alln-20261101/outputs/gated/d3_edge_certificate.json --ep-output topics/padua-argmax-alln-20261101/outputs/gated/d3_ep_screen.json > topics/padua-argmax-alln-20261101/outputs/gated/d3_edge_generate.out
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-argmax-alln-20261101/code/gated/d3_edge_check.py topics/padua-argmax-alln-20261101/outputs/gated/d3_edge_certificate.json --output topics/padua-argmax-alln-20261101/outputs/gated/d3_edge_check.json --controls > topics/padua-argmax-alln-20261101/outputs/gated/d3_edge_check.out
```

The producer took 4.749713391 CPU seconds; development replay took
6.095775444 CPU seconds. Exact arithmetic controls include the existing
n=2 rational constructor comparison and nontrivial constant/affine
univariate Bernstein transforms. The checker rejects missing/wrong
comparisons, a nonedge index, malformed/incomplete/duplicate source
partitions, forged bounds/targets, source changes, false complete flags
and producer self-approval. It also mandates and verifies the designated
E-P witness, rejects duplicate witnesses and tests missing, nonpositive
or unregistered-phase witness inputs. Those E-P conclusions live in N02.

The distinct gpt-6-astra xhigh agent actually executed both the frozen
producer and checker, including all seventeen controls. The orchestrator
reported PASS on 2026-11-02: all ten E-C comparisons/twenty leaves/eight
E-P witnesses match exactly apart from timing metadata; the separate
float E-P output is byte-identical. The independent record and receipts
are linked from `gated/checks/d3-r01.md`. This is an actual different-agent
execution, not merely source inspection. Both executions share the
outward arithmetic implementation, which remains an explicit trusted
dependency; no separately implemented arithmetic kernel is claimed.
The independent receipt `outputs/gated/check_d3_r01_receipt.json` is
10932 bytes, SHA-256
`d77ee6d68926d3b19eaf663a6837a5fbcc9d9115fec0db36f26076cd37bf539b`.

## Sources

Accepted local corrected-kernel and certificate-soundness proofs only.
No external literature, priority claim or transferred 1-D argument.

## Scope and open items

Only the ten strict whole-cell inequalities at n=7 and n=12 are proved.
This does not establish all-n E-C, an exact formula for cell suprema,
any other degree, corner dominance or an effective all-degree threshold.
The E-P translation is refuted separately, so it cannot serve as the
unqualified all-cell pointwise comparison mechanism. A future all-n
E-C route still requires a distinct analytic comparison handling the
maximizing phases. No further scan or later round was executed here.

At initial publication the required Claude topic audit remained PENDING, including this finite
computer proof. The orchestrator controls the checkpoint/commit and the
essential-evidence disposition; all listed code and small certificate/
receipt artifacts are available in the shared workspace for that step.
No cold-storage-only dependency or invented storage locator is used.

## History

2026-11-02, Codex assigned gpt-6.1-sol xhigh, runtime metadata not
independently exposed: registered and executed the bounded D3 round-1
finite reduction at the supplied administrative checkpoint, with no Git
or shared-record operation. The final checker was strengthened before
independent replay to require the designated E-P witness and reject
duplicates/malformed witness records and nonedge indices. The certificate
was regenerated under the final pinned source hashes; mathematical
interval rows did not change. After the orchestrator confirmed the
distinct actual replay PASS, this separate finite statement was recorded
as PROVED. No all-degree target or older result status was upgraded.


### Documentation correction — 2026-11-02

N8: the original phrase “interval roots” meant the initial source intervals at the roots of the binary subdivision trees, not roots of a polynomial or interval root isolation. Only that wording is clarified.

Current review scope (F3): [Claude audit-01](../audit-01.md) ACCEPTED the mathematics exactly as stated; its record/protocol findings and the protocol check of this response remain pending. Supplementary independent checks are complete and do not replace that Claude audit. No proof status, statement, checker predicate or certificate changes. Earlier publication-time review wording is preserved here as history:

> Required Claude audit is
> **PENDING**

The original closing sentence began “The required Claude topic audit remains PENDING, including this finite”; it is now explicitly labeled as the publication checkpoint and superseded by the current review correction.
