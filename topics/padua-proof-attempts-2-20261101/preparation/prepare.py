"""Approved mechanical PR12 registration. No scientific execution; no Git mutation.

Run from the repository root after publishing reservation103ee71; controlled
shared outputs are rebuilt from pinned baselines for reproducibility. Baseline
shared inputs are pinned at merged main67bd07c; developer proof files stay in
place with a final-ID metadata line and their original provisional aliases.
"""
import hashlib, json, re, subprocess
from pathlib import Path

R=Path(__file__).resolve().parents[3]
T='topics/padua-proof-attempts-2-20261101/'
P=R/T/'preparation'
BASE='67bd07c0867d8d49eb104942237d7f51a7d9f77d'
RESPONSE='e1581b3d697610be5eb647c594e7d66fcbc61352'
MARK='## Second proof campaign — PR12 final registration'
def git(*a):return subprocess.check_output(['git',*a],cwd=R)
def old(path):return git('show',BASE+':'+path).decode()
def read(path):return (R/path).read_text()
def write(path,s):(R/path).write_text(s)
def cell(s):return re.sub(r'\s+',' ',s).strip().replace('|','\\|')
def append(path,s):
    if path.startswith(('state/','literature/')):s=s.replace(']('+T,'](../'+T)
    write(path,read(path).rstrip()+'\n\n'+s.strip()+'\n')

paths=sorted((R/T/'theory').glob('*.md'))
assert len(paths)==44
mapping={};records={};by_number={}
for kind,start in [('T',156),('N',72)]:
    selected=[p for p in paths if ('-N' in p.name)==(kind=='N')]
    for offset,p in enumerate(selected):
        text=p.read_text();local=text.splitlines()[0].split(' — ')[0].removeprefix('# ')
        number=re.search(r'codex-([N]?\d+)-',p.name)[1]
        final=f'PD-{kind}{start+offset:03}'
        mapping[local]=final;by_number[number]=final
        records[local]={'final':final,'path':str(p.relative_to(R)),'title':text.splitlines()[0].split(' — ',1)[1],
                        'status':'OPEN' if number in ['61','62','65'] else 'PROVED','local_number':number}
assert len([v for v in mapping.values() if v.startswith('PD-T')])==42
def canonical_source(n):
    if n in ['01','02','03','04']:return 'PD-T098 (A2 split; full A3 remains OPEN)'
    if n in ['07','11','17','42','52','70','71','72','73','74','75','76','77']:return 'PD-T099 (finite global or exact edge/central-scope split; full-square all-n statement remains OPEN)'
    if n in ['90','91','92','93']:return 'PD-N040 / OPEN_TARGETS B1 (structural class split; measured implementation instability retained)'
    if n in ['80','N01','N02']:return 'PD-N039 / OPEN_TARGETS B3 (computed-section extension or separate supporting route obstruction; original scope retained)'
    if n=='62':return 'PD-T099 and PD-T100 (OPEN degree-eight global obligation, without a completeness claim)'
    return 'PD-T100 / OPEN_TARGETS A5 (exact finite case, supporting result or separately OPEN obligation; source measurement retained)'

def ids(*numbers):return ', '.join(by_number[str(n)] for n in numbers)
def translate(s):
    for a,b in sorted(mapping.items(),key=lambda kv:-len(kv[0])):s=s.replace(a,b)
    # Short '-NN' references in the authored addenda only, never Old text.
    s=re.sub(r'(?<=[\s`,(/])-(\d{2})(?!\d|[./]\d)',lambda m:by_number.get(m[1],m[0]),s)
    return s

# Register the existing candidates, including their scoped failed/deferred
# variants. These are historical attempts, not new mechanisms or priority claims.
C=[
('a2-product','Prescribed sheared product-U route','deferred','T-A2.md','Source product route deferred after positive comparison; resume only with a proved cross-term advantage.','01,02,03,04'),
('a2-positive','Positive corner Cauchy rewrite','retained','T-A2.md','Exact endpoint-aware rewrite; a failed kernel identity would kill this rewrite only.','04'),
('a2-square','Same-mesh square and bounded deformation','retained','T-A2.md','Endpoint-weight and pointwise deformation proof; a bound growing with n would kill this comparison.','04'),
('a2-coarse','Coarse mean-value estimate near adjacent endpoints','abandoned','T-A2.md','The bound was too large; replaced by exact subtraction, not a negative theorem about A2.','04'),
('a5-n3','Complete cubic sign-arrangement certification','retained','T-A5.md','All active masks and physical boundary cases; any uncovered stratum blocks certification.','05,06,07'),
('n4-01','Quartic finite elimination retaining singular points','retained','T-A5-n4.md','Singular Hessians/common-gradient isolated real zeros are retained; costly expression-domain resultants were an abandoned implementation subroute.','08'),
('n4-02','Simultaneous spatial sign enumeration','retained','T-A5-n4.md','Full tree, all compatible signs, strict root predicates and boundaries; unresolved cases block a count.','09,10,11'),
('n5-generic','Exact node cones and generic spatial certificate','retained','T-A5-n5.md','Exact positive node gap and radial bounds replace exponential node-near sign work; no unproved genericity.','15,16,17,18,19'),
('n6-field','Principal exact tensor field for degree six','retained','T-A5-n6.md','Verified ring conversion and real embedding; ambiguous embedding kills the implementation.','40'),
('n6-cover','Complete degree-six spatial and boundary coverage','retained','T-A5-n6.md','Every mask/root/boundary gets a rigorous disposition; independent exact checker and regeneration completed.','41,42'),
('n7-field','Degree-seven formal field and complete certification','retained','T-A5-n7.md','Exact principal embedding plus complete count/global predicates; no floating rank/sign threshold.','50,51,52'),
('n7-roots','Tensor tower norms with Arb proposals and exact Sturm checks','retained','T-A5-n7.md','End-to-end native-norm pipeline and uncached per-endpoint root-count implementations stopped for cost; no isolated native-norm timing is claimed. Tensor resultants/cached exact Sturm retained. Arb proposals have no independent proof authority.','51,52'),
('n8-field','Degree-eight exact tensor field','retained','T-A5-n8.md','Exact field support is proved independently of count completeness.','60'),
('n8-cover','Degree-eight complete interior/boundary continuation','deferred','T-A5-n8.md','Includes the operational continuation/Candidate4 variants. Capped and deadline-interrupted runs are not passes. Resume only with corner arithmetic/atomic boundary persistence repaired and full checker time.','61,62,65'),
('n8-gradient','Universal compatible-gradient leaf','retained','T-A5-n8.md','Every ambiguous derivative enters the enclosure; a zero-containing bound never discards the leaf.','53'),
('n8-reflect','Exact x-reflection witness construction','retained','T-A5-n8.md','Identity and conditional transport are proved; a reflected proposal never supplies completeness by itself.','63,64'),
('n8-witness','Axis handling and standalone interior witness fallback','retained','T-A5-n8.md','Forty-four disjoint strict interior witnesses verified; standalone fallback has no upper-count or global claim.','64'),
('a4-edges','All-edge kernel and complementary-grid defect','retained','T-A4a.md','Polynomial removable limits and the exact singular correction retained. The unspecified endpoint quotient was corrected before use, not a refutation.','70,71'),
('a4-g','Positive central-grid limit and gap-constant series','retained','T-A4a.md','All-parity complementary ordinates replace a literal midpoint-only route; integral/series bounds, not the fit, supply g.','72,73'),
('a4-envelope','Uniform phase/gain/defect assembly for the central envelope','retained','T-A4a.md','Coarse O(log n) control alone gives only phase localization; signed pairing supplies vanishing gain. Global runner-up identification and full-square extensions stay deferred/OPEN.','74,75,76,77'),
('b3-c1','Literal common shrinking full-residual cluster','REJECTED: failed','T-B3.md','Uniform pivots and full-residual hypotheses obstruct this route only; compressed-cluster surrogates and other counts are outside scope.','80,N02'),
('b3-c2','Minimal positive computed-section screen','equivalent: consolidated into C3','T-B3.md','Positive moment/pivot screen retained inside C3; no separate failed-mechanism or negative theorem.','N01'),
('b3-c3','Small positive fourth atom and shrinking isolated-node box','retained','T-B3.md','Exact fixed-n,p family defeats the specified count at square-root boundary gap; other F/reference-existence claims stay open.','N01'),
('b1-detector','Next-pole top-form leakage detector','retained','T-B1.md','Positive exterior pole ratio proves detection. Prior unproved older-space closure and surjectivity alone are not premises; no theorem is rejected.','90'),
('b1-rank','Coalescent projective witness and pole-only minors','retained','T-B1.md','Nonzero polynomial for every fixed admissible sample, without generic-node substitution. Source infinity-gauge sketch is not a proof premise. The small exact fallback was not executed because structural proof sufficed.','91,92'),
('b1-taper','Literal source taper and finite real-exponential exceptions','retained','T-B1.md','Both fixed orders, both source normalizations, finite exceptional set; stored parameters and stability are not certified.','93'),
]
assert len(C)==26
ideas=[]
for i,(alias,title,disposition,attempt,outcome,numbers) in enumerate(C,286):
    local='IDEA?proof-attempts-2-codex-'+alias;final=f'IDEA-{i:03}'
    mapping[local]=final
    ideas.append({'local':local,'final':final,'title':title,'disposition':disposition,'attempt':T+'attempts/'+attempt,'outcome':outcome,'records':[by_number[n] for n in numbers.split(',')]})
assert {i['final'] for i in ideas}=={f'IDEA-{i:03}' for i in range(286,312)}
catalog='# Registered historical candidates and route memory\n\nFinal registration after Claude audit-01 and response-01. These are the existing attempted mechanisms and scoped subroutes, not newly generated ideas or priority claims. Detailed hypotheses, closest predecessors, gate searches, tests, pre-run kill criteria and actual evidence remain in the linked attempts. Existing candidate aliases n4-01/02 and B3-C1/C2/C3 are preserved.\n'
for row in ideas:
    catalog+=f'''\n## {row['final']} — {row['title']}

Aliases: `{row['local']}`; original candidate/route labels in [{Path(row['attempt']).name}](../attempts/{Path(row['attempt']).name}).

- Question, mechanism and hypotheses: the exact scope recorded in that attempt; no broader class is introduced here.
- Closest entries and separation: the attempt's recorded predecessor/gate and scoped distinction; this is proof completion or an implementation variant, without a novelty claim.
- Cheapest test, prewritten kill criterion and actual outcome: {row['outcome']}
- Disposition: **{row['disposition']}**. Failed/abandoned subroutes above do not reject a parent theorem.
- Canonical records: {', '.join(row['records'])}; [accepted audit](../audit-01.md), [response](../response-01.md).
'''
# Rebuild only explicitly owned shared outputs from the integration baselines.
for path in ['PROOF_STATUS.md','ID_CROSSWALK.md','state/IDEAS.md','literature/INDEX.md','state/CURRENT.md','PAPER_MAP.md','topics/README.md','RESULTS.md']:
    write(path,old(path))
write('topics/padua-batch-20261031/ALLOCATIONS.md',git('show','103ee71:topics/padua-batch-20261031/ALLOCATIONS.md').decode())
for path in ['attempts/T-A5-n4.md','attempts/T-B3.md']:
    write(T+path,git('show',RESPONSE+':'+T+path).decode())

write(T+'preparation/ideas-registration.md',catalog)
mapdoc={'reservation_commit':'103ee71e101265ca4133c7ffea8c0e48fa840109','base':BASE,'scientific_candidate':'4265bb94f987ce77d89cd5e15a8c435cbd1411d0','response':RESPONSE,'mapping':mapping,'records':records,'ideas':[{k:r[k] for k in ['local','final','title','disposition','attempt','records']} for r in ideas],'permanent_gaps':{'PD-T':'198–205','PD-N':'074–077','IDEA':'312–315','LIT':'no range'}}
(P/'final-id-map.json').write_text(json.dumps(mapdoc,indent=1)+'\n')

# Add metadata only: preserve provisional heading/text and every proof byte.
for local,row in records.items():
    path=row['path'];text=git('show',RESPONSE+':'+path).decode();first,rest=text.split('\n',1)
    write(path,first+f"\n\nFinal ID: **{row['final']}**. Provisional ID `{local}` is retained as an alias. Registered after accepted Claude audit-01 and response-01; historical pending-audit notes below are superseded.\n\nCanonical Split from (registration): {canonical_source(row['local_number'])}.\n"+rest)

# Apply exactly the approved literal blocks, translating authored additions only.
proposals=re.findall(r'Target: `([^`]+)`\s+Pinned commit: `([a-f0-9]{40})`\s+Old:\s+```text\n(.*?)\n```\s+New:\s+```text\n(.*?)\n```',read(T+'proposed-record-changes.md'),re.S)
assert len(proposals)==10
targets={};applied=[]
for target,pin,o,n in proposals:
    if not o:
        assert target not in git('ls-tree','-r','--name-only',BASE).decode().splitlines();targets[target]=translate(n)+'\n'
    else:
        s=targets.get(target,old(target));assert s.count(o)==1
        if n.startswith(o):new=o+translate(n[len(o):])
        elif n.endswith(o):new=translate(n[:-len(o)])+o
        else:raise AssertionError('Old not retained contiguously')
        targets[target]=s.replace(o,new,1)
    applied.append({'target':target,'pin':pin,'old_sha256':hashlib.sha256(o.encode()).hexdigest()})

PG='topics/programme-ideas-20261031/'
sources={
'04-padua-corner-expansion':ids('01','02','03','04'),
'05-padua-corner-argmax':ids('07','11','17','42','52','62','70','71','72','73','74','75','76','77'),
'06-padua-lebesgue-maxima-counts':ids('05','06','08','09','10','15','16','18','19','40','41','50','51','53','60','61','62','63','64','65'),
'N01-symmetrised-product-inertia-count':ids('N01','N02','80'),
'N02-windowed-rational-lanczos-instability':ids('90','91','92','93')}
for suffix,split in sources.items():
    path=PG+'theory/programme-ideas-claude-'+suffix+'.md';s=targets.get(path,old(path))
    match=re.search(r'^Split into: (.*)$',s,re.M);assert match
    previous=match[1]
    replacement='Split into: '+('' if previous=='none.' else previous.rstrip('.')+'; ')+split+' (PR12, exact scoped splits; original status/history retained).'
    s=s[:match.start()]+replacement+s[match.end():]
    if suffix.startswith('N02'):
        s+='\n\nDated structural split, 2026-11-01: '+split+' prove the constrained-window identity for exterior real diagonal poles under their fixed-sample/finite-degree hypotheses. The historical “not proved” observation for all five classes is superseded only in that class. This record remains MEASURED for its tested implementation instability; no stability claim follows.\n'
    targets[path]=s
path=PG+'OPEN_TARGETS.md';s=targets[path]
for line in s.splitlines():
    if line.startswith('A2/A3') or ('A2/A3 asymptotics' in line):
        s=s.replace(line,line.replace('A2/A3 asymptotics','Full A3 asymptotics (A2 closed in '+ids('01','02','03')+')'),1)
        s+='\nHistorical introduction before PR12: «'+line+'»\n'
targets[path]=s
for path,s in targets.items():write(path,s)

# All new registry rows use final identifiers, with links to exact durable scope.
audit=f'[{"Claude audit-01"}]({T}audit-01.md); [response-01]({T}response-01.md)'
rows=[MARK,'','| ID / alias | Statement and scope | Status | Evidence | Disposition / reason | Depends on | Record | Audit |','|---|---|---|---|---|---|---|---|']
for local,r in records.items():
    dep='Exact dependencies and assumptions in the linked record; accepted earlier results retain their IDs'
    ev='Written proof and recorded exact evidence/checks' if r['status']=='PROVED' else 'Target retained OPEN; supporting results do not discharge completeness/global obligations'
    disp='Retained at exact audited scope; no novelty claim' if r['status']=='PROVED' else 'OPEN, not rejected; deadline failures are not passes'
    rows.append(f"| {r['final']} ({local}) | {cell(r['title'])} | {r['status']} | {ev} | {disp} | {dep} | [record]({r['path']}) | {audit} |")
append('PROOF_STATUS.md','\n'.join(rows))

# Qualify the existing source rows in place; leave every unrelated row exact.
existing_updates={'PD-T098':f'A2 is closed by {ids("01","02","03")} with support{ids("04")}; full A3 remains OPEN.',
 'PD-T099':f'Finite n3–7 globals {ids("07","11","17","42","52")} and central-edge splits {ids("70","71","72","73","74","75","76","77")} are PROVED; full-square all-n target remains OPEN.',
 'PD-T100':f'MEASURED search status retained; separate n3–7 count proofs {ids("06","10","16","41","51")}; degree-eight lower{ids("64")} PROVED, exact{ids("61","62","65")} OPEN.',
 'PD-N039':f'Separate computed-section extension {ids("N01")} PROVED; distinct route failure{ids("N02")} supported by{ids("80")}; original symmetric-pair scope preserved.',
 'PD-N040':f'Structural exterior-class splits {ids("90","91","92","93")} PROVED; numerical implementation failures remain MEASURED at their original scope.'}
s=read('PROOF_STATUS.md')
for id,note in existing_updates.items():
    lines=s.splitlines();hits=[i for i,l in enumerate(lines) if re.match(r'^\| '+id+r'(?: |\()',l)];assert len(hits)==1
    i=hits[0];line=lines[i]
    if id=='PD-T098':line=line.replace('A2/A3 remain OPEN','A2 closed; full A3 remains OPEN')
    line=line.rstrip().removesuffix('|').rstrip()+'; PR12 dated split: '+note+' |'
    lines[i]=line;s='\n'.join(lines)+'\n'
write('PROOF_STATUS.md',s)

cross=[MARK,'','| Provisional / original | Final ID | Owner | Record | Audit / disposition |','|---|---|---|---|---|']
for local,r in records.items():cross.append(f"| {local} | {r['final']} | codex/padua-proof-attempts-2-20261101 | [record]({r['path']}) | {audit}; {r['status']} |")
for r in ideas:cross.append(f"| {r['local']} | {r['final']} | codex/padua-proof-attempts-2-20261101 | [candidate]({T}preparation/ideas-registration.md) | {r['disposition']}; original attempt alias retained |")
cross+=['',f'Original-to-split: PD-T098 → {ids("01","02","03","04")}; PD-T099 → {sources["05-padua-corner-argmax"]}; PD-T100 → {sources["06-padua-lebesgue-maxima-counts"]}; PD-N039 → {sources["N01-symmetrised-product-inertia-count"]}; PD-N040 → {sources["N02-windowed-rational-lanczos-instability"]}. Full A3 and all-n A4 stay OPEN; PD-T100 stays MEASURED. Permanent unused gaps PD-T198–205, PD-N074–077, IDEA-312–315. No LIT range.']
append('ID_CROSSWALK.md','\n'.join(cross))

s=read('state/IDEAS.md')
notes={'IDEA-206':f'PR12: A2 {ids("01","02","03")} closes the b-term; certified n3–7 counts/globals and central-edge {ids("70","71","72","73","74","75","76","77")} are separate PROVED splits. Degree-eight lower{ids("64")} PROVED, exact counts/global OPEN; full A3/all-n A4 remain OPEN; PD-T100 stays MEASURED.',
'IDEA-192':f'PR12 structural pointers {ids("90","91","92","93")} prove only the exterior real Ldiag class; original tested implementation failure and instability remain valid.',
'IDEA-198':f'PR12 {ids("N01")} proves specified S(α) REJECTED: refuted in genuine computed sections at fixed n1,p1/10. Other F/reference-existence questions remain OPEN; {ids("N02")} rejects only the literal C1 cluster route.',
'IDEA-048':'PR12 primary LIT-388 Table3 reading supersedes pending only for the stated n3–8 counts and scoped candidate corrections; unrelated geometry/open-problem claims remain qualified.'}
for id,note in notes.items():
    lines=s.splitlines();hits=[i for i,l in enumerate(lines) if re.match(r'^\| '+id+r'(?: |;|\()',l)];assert len(hits)==1
    i=hits[0];lines[i]=lines[i].rstrip().removesuffix('|').rstrip()+' Historical wording retained; dated '+note+' |';s='\n'.join(lines)+'\n'
write('state/IDEAS.md',s)
idea_rows=[MARK,'','| Idea / aliases | Mechanism and closest record | Disposition and durable evidence |','|---|---|---|']
for r in ideas:idea_rows.append(f"| {r['final']}; {r['local']} | {r['title']}; {', '.join(r['records'])} | {r['disposition']}; [candidate]({T}preparation/ideas-registration.md), [attempt]({r['attempt']}) |")
idea_rows+=['','### PR12 obstruction and disposition addenda','','| Record | Exact obstruction and affected candidate | Status / scope |','|---|---|---|',f'| [{ids("N01")}]({records["PD-N?proof-attempts-2-codex-01"]["path"]}) | Specified symmetrised-product S(α) fails in positive n1,p1/10,M4 computed sections; IDEA-308 supplies counterfamily | PROVED; specified count REJECTED: refuted; other F/reference existence not rejected |',f'| [{ids("N02")}]({records["PD-N?proof-attempts-2-codex-02"]["path"]}) | IDEA-306 literal common shrinking full-residual cluster fails with fixed N and uniform positive pivots, by {ids("80")} | PROVED scoped mechanism failure; not a theorem against other B3 routes |']
append('state/IDEAS.md','\n'.join(idea_rows))

append('literature/INDEX.md',MARK+f'''

- **LIT-379 — 2026-11-01 reading addendum:** this topic read the full arXiv2009.07114v1 text before method use: Theorem2.1 (global leading term/upper context only), Lemmas3.5(3.20),3.6(3.29), (4.5)–(4.6). Page numbers are per developer reading; Claude confirmed content through page-less text. The local explicit A2 proof is separate. [Coverage]({T}attempts/T-A2.md), [audit]({T}audit-01.md). Historical secondary row and earlier MZ addendum preserved.
- **LIT-388 — 2026-11-01 primary-reading addendum:** arXiv2605.23299v1 §3.3 Table3 reports n3–8 interior7,13,14,23,27,38 and total15,27,25,39,42,56. Certified n6/n7 give scoped candidate corrections25/41 and33/50; n8 lower≥44 contradicts interior38 only, without a replacement exact total. No accepted erratum/author contact. [Readings]({T}outputs/a5_n7_literature-comparison.md), [n8 scope]({T}outputs/a5_n8_literature-lower-bound-comparison.md). UNVERIFIED/pending is superseded only for these inspected count statements; unrelated geometric assertions remain qualified.
- **LIT-312 — 2026-11-01 bounded-reading addendum:** Bos et al.2006 author preprint, definitions and Theorem3 sum/integral estimates, global O(log²n) background only. No full-paper read or load-bearing local A2 theorem is claimed. [Coverage]({T}attempts/T-A2.md). Preserve prior source addenda and version gaps.
''')

summary=f'''The second proof campaign is accepted by Claude audit-01 with minor findings disposed in response-01. A2 {ids('01','02','03','04')} proves the requested b-term with remainder≤68. A5 closed counts15,27,25,41,50 for n3–7 and separate corner-only globals are PROVED; degree-eight lower{ids('64')} proves≥44interior, while exact{ids('61','62','65')} remain OPEN. A4 central-edge {ids('70','71','72','73','74','75','76','77')} proves the positive gap envelope, not full-square/global-runner-up identification. B3 {ids('N01')} refutes only specified S(α) on genuine positive sections; {ids('N02')} is a scoped route failure. B1 {ids('90','91','92','93')} proves the exterior real diagonal class/taper, not stability or every stored parameter. Remaining frontier: full A3, all-n full-square A4, exact n8, other B1 classes/parameters/stability. Completed proof/audit/preparation tasks are historical after merge. [Report]({T}report.md), [results](results/padua-proof-attempts-2-20261101.md). Only AC merges.'''
append('state/CURRENT.md',MARK+'\n\n'+summary.replace(']('+T,'](../'+T).replace('](results/','](../results/'))
append('PAPER_MAP.md',MARK+'\n\n| Brief | Support | Remaining gaps | Readiness |\n|---|---|---|---|\n| [Second proof campaign]('+T+'report.md) | PD-T156–197, PD-N072–073 at their exact statuses | Full A3, degree-eight completeness/global, full-square A4, other B1 classes and stability OPEN | Claude audit-01 accepted; minor response complete; PR12 follows merged PR15; no manuscript or novelty claim |')
append('topics/README.md',MARK+'\n\n[padua-proof-attempts-2-20261101](padua-proof-attempts-2-20261101/LOG.md): accepted second proof campaign; PD-T156–197, PD-N072–073, IDEA-286–311. Proved and OPEN scopes are separate. Claude audit-01 accepted, minor response complete, PR12 prepared after merged PR15. Only AC merges.')

# Supersede this topic's generic preparation sentence in the repository-results
# proposal now that AC authorized actual application. Other sections untouched.
result_path='results/padua-proof-attempts-2-20261101.md'
s=read(result_path).replace('Stage PR (preparation within topic-only scope)','Stage PR (prepared for AC review)').replace('remains unready for merge until preparation is complete','is prepared after merged PR15; only AC merges')
s+='\nFinal registration: PD-T156–197; PD-N072–073; IDEA-286–311. [Exact ID map](../'+T+'preparation/final-id-map.json). Reservation gaps PD-T198–205, PD-N074–077, IDEA-312–315 remain permanent.\n'
write(result_path,s)
append('RESULTS.md','## padua-proof-attempts-2-20261101\n\n'+s.removeprefix('# padua-proof-attempts-2-20261101 — second proof campaign\n').replace('](../topics/','](topics/'))
append('topics/padua-batch-20261031/ALLOCATIONS.md',f'''## PR12 assignments after reservation publication

Priority: published103ee71e101265ca4133c7ffea8c0e48fa840109 before assignment. Assigned PD-T156–197 (42), PD-N072–073 (2), IDEA-286–311 (26). Permanent unused headroom PD-T198–205, PD-N074–077, IDEA-312–315. No LIT assignment/range; source IDs312/379/388 reused. [Map](../padua-proof-attempts-2-20261101/preparation/final-id-map.json). All earlier reservations and gaps, especially merged PR15's, remain unchanged. PR15 is merged as67bd07c; PR12 follows on that base. Only AC merges.''')

# Add final candidate aliases to the explicit pre-existing attempt labels.
for path,note in [('attempts/T-A5-n4.md','Final registration: original n4-01 → IDEA-291; n4-02 → IDEA-292. Historical pre-run labels and dispositions retained.'),('attempts/T-B3.md','Final registration: original B3-C1 → IDEA-306 (REJECTED: failed); C2 → IDEA-307 (consolidated into C3); C3 → IDEA-308 (retained counterexample). Proved negatives PD-N072/073 remain scoped.')]:
    append(T+path,note)
receipt={'purpose':'mechanical final registration only; no science execution','base':BASE,'reservation':'103ee71e101265ca4133c7ffea8c0e48fa840109','theory_records':44,'idea_records':26,'literal_blocks':applied,'shared_paths':sorted(set(targets)|{'PROOF_STATUS.md','ID_CROSSWALK.md','state/IDEAS.md','literature/INDEX.md','state/CURRENT.md','PAPER_MAP.md','topics/README.md','RESULTS.md','topics/padua-batch-20261031/ALLOCATIONS.md'}),'proof_body_changes':0,'frozen_code_or_evidence_changes':0}
(P/'prepare-receipt.json').write_text(json.dumps(receipt,indent=1)+'\n')
print(json.dumps({'theory_records':44,'idea_records':26,'literal_blocks':10,'shared_files':len(receipt['shared_paths'])}))
