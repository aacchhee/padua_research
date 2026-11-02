# PD-N?argmax-alln-gated-codex-02 — Common-phase centreward edge translation fails

ID kind: PD-N.
Aliases: direction3 round1 E-P obstruction; n12 k5-to7 common phase
minus-one-half; pointwise edge translation counterexample.
Split from: the separately formulated E-P candidate in fallback-03 and
attempts/P3-P5-and-pairing.md. Split into: none. E-C compares whole-cell
suprema and remains a different OPEN all-degree candidate.

## Statement

For the even-checkerboard degree-12 Padua Lebesgue function,

\[
 \lambda_{12}(1,\cos(9\pi/26))-\lambda_{12}(1,0)
                                      >39/1000>0.       \tag{1}
\]

This contradicts the E-P inequality for the eligible centreward pair
k=5 to k'=7 on the vertical edge with physical first index j=0,
at the same cell phase u=-1/2. It does not contradict a comparison
between the two whole-cell suprema, and makes no assertion about other
edge pairings or the original ambiguous rhombus-order proposal.

## Definitions and negative-result scope

E-P has n>=2,m=n+1, physical first-edge index j in {0,n}, and
complementary integer centers k,k' in [2,m-2] with j+k,j+k' odd.
It requires k'-k in {-2,2}, |k'-m/2|<|k-m/2|, and asks

lambda_n(cos(j*pi/n),cos((k+u)*pi/m))
 <=lambda_n(cos(j*pi/n),cos((k'+u)*pi/m))

for every u in the source cell [-1,1]. The attempted mechanism is this
fixed-phase translation, intended as a sufficient route to whole-cell
E-C. The negative statement is confined to its explicit degree-12
pair and phase. All arithmetic in the certificate implication is exact
rational/outward integer interval arithmetic; float samples are not a
proof premise.

## Status by part

Overall status: **PROVED**, with the exact interval certificate, written
finite reduction, developer checker, and distinct actual producer/checker
execution completed at the declared scope. Codex configured gpt-6-astra
xhigh independently reconstructed the evidence, checked all eight exact
E-P witnesses, and passed the complete 17-case malformed-input controls.
Its broader run also verified the separately stated ten E-C comparisons
and twenty complete source leaves. Required Claude audit remains pending.

| Mathematical part | Status | Evidence / limit |
|---|---|---|
| Exact inequality (1) and E-P counterexample | PROVED | Positive integer witness, correct enclosure reduction and distinct executed replay/controls |

Candidate disposition: E-P **REJECTED: refuted** at the stated degree,
edge pair and common phase. E-C remains retained and OPEN outside its
separately certified finite comparisons. No negative conclusion about
whole-cell E-C is inferred.

## Depends on

PD-T101/185 corrected Padua cardinal polynomial identity; the general
outward constructor enclosure proof in
argmax-alln-codex-03-finite-certificate-correctness.md. New witness
construction/evidence: code/gated/d3_edge_common.py,
code/gated/d3_edge_check.py and outputs/gated/d3_edge_certificate.json.
The exact finite reduction and arithmetic assumptions are written below;
they require no external literature theorem.

## Proof reduction and exact witness

For n=12,m=13,j=0, both 5 and 7 are eligible complementary centers,
and |7-13/2|=1/2<3/2=|5-13/2|. The common phase u=-1/2 gives
the source mesh ordinate 9/2 and target 13/2, hence angles 9pi/26
and pi/2. Both are inside their respective closed cells, including the
source's required domain. The physical first coordinate is exactly 1,
and the target second coordinate is exactly 0.

Restrict every exact corrected cardinal polynomial to x=1, obtaining
univariate polynomials P_B(y). The existing constructor encloses every
coefficient at the common integer scale S=2^192. Rigorous rational
Machin/Taylor cosine enclosures contain cos(9pi/26) and cos(pi/2).
Outward Horner evaluation therefore encloses each P_B at each actual
point. If a polynomial interval is [l/S,h/S], its absolute value lies
between 0 (when the interval straddles zero) or min(|l|,|h|)/S and
max(|l|,|h|)/S. Summing these bounds encloses lambda at the point.
No sign assumption or avoidance of a cardinal zero is required.

The selected exact witness in the certificate is
`(n,j,source,target,phase)=(12,0,5,7,-1/2)`. It supplies the source
lower numerator

L_s=30470195454344039486544373764520686437665106855823873746908

and target upper numerator

U_t=30223024111189925342428840247143247502305683243932294679697.

Both denominators are S=2^192, and their exact difference is

G=247171343154114144115533517377438935359423611891579067211.

Thus the point-value difference is at least G/S. Direct integer
comparison gives 1000*G>39*2^192, proving (1). The stronger approximate
value .0393766667442563 is interpretation only, not part of the proof.

The checker reconstructs the exact corrected polynomial intervals and
the cosine intervals from source, verifies the pair, registered phase
and cell/domain conditions, reconstructs the witness dictionary and
tests its integer reversal. It also checks the shared interval arithmetic
controls and the certificate's source identities. An actual distinct
execution is required; reading the developer receipt is not a rerun.

## Evidence and commands

Developer certificate: `outputs/gated/d3_edge_certificate.json`, SHA-256
`0d660fc70e9db06624d6f8bd82371602c9f6d540b01124824e264624de0385b7`.
Checker source: `code/gated/d3_edge_check.py`, SHA-256
`5f43f69a427c415542848f8ae9e337c69b3a5b8f822e78db38e095a0a2c9a358`.
The certificate embeds its full constructor/common/producer/checker
source manifest and the preregistration identity. The finite worker's
complete source/command/output receipt is in gated/d3/r01-finite.md.

The developer commands were registered there; the independent checker
actually executed its own producer and checker runs and verified the
same finite data, as recorded in the independent receipt:

`python topics/padua-argmax-alln-20261101/code/gated/d3_edge_generate.py --output topics/padua-argmax-alln-20261101/outputs/gated/d3_edge_certificate.json --ep-output topics/padua-argmax-alln-20261101/outputs/gated/d3_ep_screen.json`

`python topics/padua-argmax-alln-20261101/code/gated/d3_edge_check.py topics/padua-argmax-alln-20261101/outputs/gated/d3_edge_certificate.json --output topics/padua-argmax-alln-20261101/outputs/gated/d3_edge_check.json --controls`

The producer is not self-approving; its certificate records
producer_accepted=false. The independent proof/evidence assessment and
compact execution receipt are recorded in
[direction3 round1 independent check](../gated/checks/d3-r01.md), including
its exact commands, source identities, comparison fields and controls.
The [compact execution receipt](../outputs/gated/check_d3_r01_receipt.json)
is 10932 bytes, SHA-256
`d77ee6d68926d3b19eaf663a6837a5fbcc9d9115fec0db36f26076cd37bf539b`.
It independently verifies the exact positive integer
1000G-39*2^192=2364375474033594325937729872339945131431749557481721208056.
The separate actual execution, rather than developer self-approval,
closes the finite certification obligation. The checker shares the
inspected outward arithmetic; an independently implemented arithmetic
kernel is not claimed.

## Scope and history

2026-11-02, Codex assigned gpt-6.1-sol xhigh; runtime metadata not
independently exposed. Current administrative/source head
`3aebb299a4154dac822974b7245a9d243f21374e`; unchanged rule reference
`aa1883f2fd9a837bb931ce804cb4b210c7475886`. The full prior candidate /
obstruction gate and refreshed E-C/E-P comparison are recorded in
gated/d3/r01-edge-analysis.md. This exact witness arose within the
predeclared n7,12 nine-phase test; no expanded phase or degree search
was executed by the math worker.

History: initial publication was CONDITIONAL while the distinct executed
replay/controls were pending. The stated obligation is now closed by the
Astra xhigh independent execution and mathematical assessment; the exact
witness and frozen mathematical source code are unchanged. Required
Claude audit remains pending.

The original E-P and E-C statements, earlier measured E-C support and
other pairing failures remain intact. This record rejects only the
specified pointwise translation mechanism;
it gives no negative result about all-degree corner dominance,
horizontal envelopes, whole-cell E-C or alternative phase maps.
