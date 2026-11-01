# PD-T?proof-attempts-2-codex-06 — Degree-three Padua strict-local-maxima count

ID kind: PD-T.
Aliases: A5 n=3; 15 total / 7 interior / 6 edge / 2 corner; exact all-sign cubic certificate.
Split from: `PD-T?programme-ideas-claude-06`, A5's n=3 case, preserving the original n=3,…,8 statement and all other cases.
Split into: none; A4(d) global-value corollary is separate result07.

## Statement

For the even-checkerboard Padua nodes

Pad_3={(cos(jπ/3),cos(kπ/4)):0≤j≤3,0≤k≤4,j+k even},

let L_b be their unique total-degree≤3 polynomial cardinals and λ_3=Σ_b|L_b|. The intended certified statement is that λ_3 has exactly15 strict relative local maxima on [−1,1]²:7 interior,6 open edge,2 non-node corner. The non-node corners are(−1,−1),(−1,1).

## Definitions

Cardinalindices b=0,…,9 are lexicographic(j,k) with j+k even. A mask m has sign+1 at b iff its bth bit is1. Interior means both physical coordinates in(−1,1); edge excludescorners. Strictness is relative to the closed square. No floatingseed is identified with an exact root.

## Assumptions

Exactly the boardabove, exact polynomial arithmetic overQ(sqrt2), Fraction interval arithmetic, and the independentlyverified certificate predicates in `../code/a5_schema.md`. Trusted implementationdependencies are Pythoninteger/Fractionarithmetic and SymPy exact algebra (including the producer's exact root isolation and checker’s independentlyimplemented supplied-partition Sturm verification). No old certifier arithmetic is trusted.

## Status by part

Overall status: **OPEN — final certificate and independent execution pending**.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| exact count15 with statedlocation split | OPEN | complete final producer/checker/independent execution must finish before promotion |
| supporting finite reduction | Separate PROVED result05 | not itself a count |

No prefix pilot or preliminary whole interior run supplies a proof status upgrade. Required Claude audit of Part 2 remainspending.

## Depends on

- `PD-T?proof-attempts-2-codex-05`: cubic finite reduction and exact regular-crease / crossing exclusions.
- `PD-T?proof-attempts-codex-03 (audit pending)`: existing exact strictness / uniqueness at the two edge representativesx=1,y=±1/sqrt3. Dateddependency note 2026-11-01: part1 Claude audit at 95279b833bca5967fcf47c1b71a56ff622185b4e acceptedthisproof; response 7b8884a2f98518784ff3698dd2f3f9c49c9cdd62 disposedminor findings withoutchangingits mathematical proof / code. The task’s literaldependency spelling isretained. Part1 trace isnotsearchcoverage.

Cardinals are independently reconstructed by an exact10×10 monomialVandermondeinverse. Thus no old kernel evaluator or numerical normalization is inherited.

## Checks

Frozen final developer producer command (from repositoryroot):

```text
PYTHONDONTWRITEBYTECODE=1 python -B topics/padua-proof-attempts-2-20261101/code/a5_producer.py --output topics/padua-proof-attempts-2-20261101/outputs/a5_n3_certificate.json.gz --unresolved /tmp/a5-n3-final-unresolved.json > topics/padua-proof-attempts-2-20261101/outputs/a5_n3_producer.json 2> /tmp/a5-n3-final.log
```

Producer modules: `a5_producer.py`, `a5_arithmetic.py`, `a5_boundary.py`, `a5_global.py`. Separateindependent checker: `a5_checker.py`; adversecertificatecontrols: `a5_checker_adversarial.py`. No checker imports the producer or calls a root search/root isolation routine. It verifies supplied partitions and dispositions.

Frozen hashes and actualrunprogress are recorded in `../attempts/T-A5.md`; finalessential artifact receipt, finalchecker outputs and independentexecutor outputs will be inserted after completion. Large-development intermediates are in/tmp only and are notproofdependencies. No coldstorage is needed if the singlecompressed final certificate staysbelow1MB.

### Runs needed

Finish developer full producer; independentlyverify the certificate; actual separate subagentproducer+checker rerun; update this record onlyafter all succeed. The measured source counts are referencecomparisononly.

## Sources

Authoritative programme `OPEN_TARGETS.md` A5, THEORY-06 and frozen t3sources at 9bd14a6d2c4da69139a10107d8a787f2be0c5c9e. Measuredsource value n=3 is15total/7interior; the new certificate is independentofthatnumber. Literature/INDEX was readbefore anypapercomparison; no certified n=6,7,8count or publishedcorrection is assertedhere.

## Proof or evidence

The following is the proof reduction whose finite predicates the pending final checker must discharge.

1. Construct the exact cardinals from the Vandermondeinverse; matrixmultiplication verifiesinterpolation and reproducing constants. Eachsigned polynomial has degree≤3.
2. Enumerate all 1024 masks. If one gradient component isidentically zero, the signed polynomial cannot have a strictinteriormaximum. Otherwise verify exact common gcd divisions, nonzeroresidualprojection resultants, and the complete supplied Sturm root partitions of their squarefree QQ norms.
3. For eachresidual pattern, verify EVERY Cartesian pair of projected root intervals. Eachvaliddisposition either excludes the stationarypoint from the open square, excludes∇P=0, excludes sign consistency, excludes a negative definiteHessian, identifies an exactregularcrease / crossing root uniquely, or rigorouslycertifies exactlyone strict maximum with strict cardinal signs. Krawczyk existence uses exact rational preconditioners andoutward Fraction intervals; the injectivity bound applies to the entire box beingdiscarded. Rootboxes are pairwisedisjoint and root IDscomplete.
4. On all four edges enumerate EVERY canonicalmask of non-identically zero restricted cardinals. Cover ALL real roots of the normof the tangent derivative by independentlyverified Sturm partitions. Eachroot gets an exactexclusion or a strict tangential maximum with the actualonesided fullmask and strictly negative inward derivative. Identicallyzeroedge cardinals are handled by exact factor identity, never atolerance sign. For n=3 the onlysuchcardinal isL_6 onx=1, with quotient(2y²+1)/3>0.
5. At x=1 the twocertified edgeintervals mapexactly to y=±1/sqrt3 because their tangent derivatives are nonzero multiplesof1−3y² andtheirintervals haveoppositefixedsigns. Theirlocal strictness / uniqueness is reusedfrom part1 theorem03; the newboundary certificate corroborates theirphysicalnormal descent and incorporates them into complete global coverage. The old disc Hessianproof isnotredone.
6. At the four corners, exact cardinal values distinguish the twonode corners(1,±1), which cannot bestrict maxima sinceλ≥1, fromthe twonon-node corners. For every active pattern at each non-node corner, both inward derivatives are strictly negative, provingstrictness. Allarbitrary nearbyedge/interiorpoints were alreadycovered by steps2–4, so noold (D)/(E) neighbourhooddiscard remainsin the proof.
7. By result05 everystrict local maximum appears in one of these types and cannot lie in an excludedcandidate. Conversely eachacceptedroot/corner satisfies a rigorous strictness predicate. Thus complete verified root ID lists with7interior,6edge and2corner entries establish exactly15.

Everyneighbourhood discarded around a root is coveredby its ownverified injectivity / concavity region; all other consistent patterns are stillchecked. Exactcreaseidentification is a polynomial identity plus a uniquenessbound on the whole pair box, replacingthe old1e−10 convention. No discardedbox is justified byan unconstrainedNewton iterate or a first accepted-pattern early return.

## Scope

Only n=3. Cases n=4,…,8 remainOPEN untiltheir owncertificates exist. The theoremcertifiesstrictlocal maxima, not global argmax by itself; nonstrictplateaus andvalue comparisons require separate result07. Part1's(D)/(E) obligations are dischargedfor this new degree-three procedure throughdirectphysicalboundarycoverage, not byasserting the old floating handlers correct.

## Open items

Finalfinite verification andindependent execution, then required Claude audit. Extendthecount targetto n=4 with a separate quartic reduction thatdoesnotdiscardHessian-singular maxima bythe cubic lemma.

## History

2026-11-01, Codex `/root/a5_develop`, allocated gpt-6.1-sol xhigh. Writtenwhilethe frozen exact final producer and actualindependent producer run. Resultstatus deliberatelyOPENuntil the essentialfinite evidence andindependent checker outputs exist. The originalprogrammeclaim n=3,…,8 isnot silentlynarrowed; this file splitsits n=3 case.
