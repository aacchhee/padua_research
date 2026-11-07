# One argument instead of an atlas

AC requested Sol max audit and an approximately twofold reduction of the
88-page draft. This revision keeps the Springer class, fonts and layout.
It changes the proof organization, rather than hiding the old appendices
in a supplement. The complete earlier source remains at commit
`a948b24c3faeba1e475ce64f4c7fc9d4123d42a5`; its local PDF is preserved at
`local-output/padua-argmax-bridge-20261105/paper/original-88-pages/main.pdf`.
Canonical theory and prior computational evidence are unchanged.

The organizing identity is
`lambda_n - Lambda_c = (S_n - S_n(0)) - Delta_n`.
The corner calculation supplies the normalization. A completed model
estimates the change of the envelope; the selected-pair defect bounds and
corner interpolation argument handle equality. The finite certificates
use the same positivity/interpolation reasoning.

| Earlier organization | Unified treatment |
| --- | --- |
| Corner formula, separate asymptotic explanation and 12-page supporting appendix | One corner chapter: exact rows, one quadrature lemma, one aggregate calculation and half-step cancellation |
| Independently developed pole, row, scalar and central-model appendices | One comparison argument: a single completed model and one fixed-cutoff error telescope |
| Multiple absolute, origin, near and wide theorem families | Outputs of the same comparison, with shared constants and a contribution table |
| Separate generic root integral and paired-root application | One cancellation estimate and its paired consequence |
| Distinct finite and tail floor presentations | One selected-pair lemma with the finite/tail parameters required by the actual checker |
| Repeated all-degree and sharp-expansion statements | Each main theorem stated once in the introduction; later sections give its proof |
| Small-degree exact cases followed by different certificate implementations | One Bernstein implication for 2–40, with fresh common-route 2–16 witnesses and the accepted same-scheme 17–40 witnesses; degree1 has an explicit formula |
| Several certificate norm/corner arguments and long receipt histories | One positive interpolation lemma; exact proof predicates retained, operational histories in reproducibility records |

The proof keeps both near and wide error columns because the near margin
at degree320 does not tolerate the wider allowance. It also keeps the
analytic far192 and corner256 implications used by the retained hybrid
certificates, both norm witnesses, all closed guards and endpoint/parity
normalizations. The audit identified that the old draft did not give the
finite41–63 defect derivation explicitly; the unified selected-pair lemma
fills that exposition obligation from the existing D29/C02 proofs.

The global comparison retains its separately certified limiting-constant
input. The corner expansion is still analytic and independent of the
global maximizer argument. No theorem scope is narrowed to save space,
and no new high-degree numerical campaign is used.

The complete root build is46pages, down from88:42pages removed, about48%
shorter. The measured artifact and separate Sol max verdict are recorded
in BUILD.md and consolidation-audit.md. Several routine
estimates are deliberately concise, but a compressed step must remain
checkable; size reduction is not a reason to replace a proof by an
internal identifier.

At AC's subsequent request, Section 5 was expanded from three to five
pages with the intermediate interpolation, norm, guard and corner-descent
derivations. The current complete draft is 48 pages. This restores useful
proof detail within the unified certificate presentation; the rest of the
mathematical source and the journal layout are unchanged. The focused
review is recorded in section5-expansion-review.md.
