#!/usr/bin/env python3
"""Apply audited PR21 source-record proposals, without Git or ID allocation.

Default is a no-write plan. Pass --write after the orchestrator approves the map.
The supplied proposal remains immutable; only explicit named targets are changed.
"""
import argparse, hashlib, json, re
from pathlib import Path

P = 'topics/padua-literature-20261103/'
ID = re.compile(r'LIT\?padua-literature-claude-\d{2}(?!\d)')
ap = argparse.ArgumentParser(description=__doc__)
ap.add_argument('--repo', type=Path, required=True)
ap.add_argument('--map', type=Path, required=True)
ap.add_argument('--write', action='store_true')
ap.add_argument('--receipt', type=Path)
a = ap.parse_args(); root = a.repo.resolve()
raw_map = json.loads(a.map.read_text()); mapping = raw_map.get('mapping', raw_map)
assert isinstance(mapping, dict) and all(isinstance(v, str) and re.fullmatch(r'LIT-\d{3}', v) for v in mapping.values()), 'Expected token -> final-ID dictionary'
proposal = (root/P/'proposed-record-changes.md').read_text()
old = {}; work = {}; ops = []; skipped = []
def read(path):
    if path not in work:
        q = root/path; assert q.resolve().is_relative_to(root), path
        old[path] = work[path] = q.read_text()
    return work[path]
def settext(path, body, label):
    read(path); work[path] = body; ops.append({'target':path, 'operation':label})
def mapped(text):
    text = re.sub(r'LIT-\?\?\? \((LIT\?padua-literature-claude-\d{2})\)', r'\1', text)
    def sub(m):
        token=m.group(); assert token in mapping, 'Unmapped '+token
        if re.search(r'LIT-\d{3} \($', text[:m.start()]): return token
        if re.match(r'[–…-]\d{2}\b', text[m.end():]): return token  # historical provisional range, not a numeric final-ID offset
        return mapping[token]+' ('+token+')'
    return ID.sub(sub, text)
def replace(path, before, after, label):
    body = read(path); count = body.count(before)
    if count != 1:
        raise RuntimeError(f'{label}: {path}: expected one literal match, got {count}')
    settext(path, body.replace(before, mapped(after), 1), label)
def append(path, text, label):
    body=read(path); text=mapped(text).strip()
    if text in body:
        skipped.append({'target':path,'operation':label,'reason':'already present'}); return
    settext(path, body.rstrip()+'\n\n'+text+'\n', label)
def table_cells(row):
    return row.strip()[1:-1].strip().split(' | ')
def rows(path, key):
    return [line for line in read(path).splitlines() if line.startswith('| '+key+' |')]
def edit_corpus(key, edits, label):
    path='literature/CORPUS.md'; found=rows(path,key); assert len(found)==1,(key,len(found))
    before=found[0]; cells=table_cells(before)
    assert len(cells)==7,(key,len(cells))
    for i,how,text in edits:
        if how=='append':
            if text not in cells[i]:cells[i]+=' · '+text
        elif how=='replace':
            source,dest=text; assert source in cells[i],(key,i,source);cells[i]=cells[i].replace(source,dest,1)
        else:cells[i]=text
    settext(path,read(path).replace(before,'| '+' | '.join(cells)+' |',1),label)
def add_corpus(row, label):
    cells=table_cells(row); assert len(cells)==7,(label,len(cells));key=cells[0]
    found=rows('literature/CORPUS.md',key)
    if found:
        # An existing-key row is coverage, never a second canonical corpus key.
        assert len(found)==1,(key,len(found))
        edits=[(3,'append',cells[3]),(4,'append',cells[4])]
        if cells[5] not in table_cells(found[0])[5]:edits.append((5,'append',cells[5]))
        edit_corpus(key,edits,label+' (existing-key coverage)')
    else:
        append('literature/CORPUS.md',row,label)

def subsection(path, ident, fields, label):
    body=read(path)
    pat=r'(?m)^### '+re.escape(ident)+r'\b[^\n]*\n(?:(?!^##? |^### ).|\n)*'
    m=re.search(pat,body); assert m,(path,ident)
    section=m.group()
    for name,value in fields.items():
        pat2=r'(?m)^- '+re.escape(name)+r':[^\n]*$'
        assert len(re.findall(pat2,section))==1,(path,ident,name)
        section=re.sub(pat2,lambda _: '- '+name+': '+mapped(value),section,count=1)
    settext(path,body[:m.start()]+section+body[m.end():],label)

def addendum_link(key, label):
    path='literature/records/'+key+'.md'; add=P+'addenda/'+key+'.addendum.md'
    assert (root/add).exists(),add
    append(path,'## '+label+'\n\nCampaign primary-reading addendum: [statement-level coverage, locators and limits](../../'+add+'). Reader/model and source version are recorded there. This is literature attribution, not a local proof or an independent auditor source-page check. Audit-02 and audit-03 retain the explicit developer-only verification qualifications where applicable.',label)

# Literal Old/New targets, keyed by immutable proposal line numbers.
def targets(line):
    if line==47:return ['literature/lattice-unisolvence/records/demarchi-2022.md']
    if line==72:return ['topics/padua-proof-attempts-2-20261101/attempts/T-A2.md','topics/padua-proof-attempts-2-20261101/theory/proof-attempts-2-codex-03-corner-log-coefficient.md','topics/padua-proof-attempts-2-20261101/theory/proof-attempts-2-codex-04-corner-product-comparison.md']
    if 94<=line<=178 or 375<=line<=419 or 542<=line<=948:return ['literature/INDEX.md']
    if 214<=line<=256 or line in (442,453,464):return ['literature/CORPUS.md']
    if line in (296,308):return ['literature/records/faghih-et-al-2025.md']
    if line in (328,340):return ['literature/records/faghih-vanbarel-vandebril-2026.md']
    return {1047:['topics/padua-mz-2d-20261101/literature.md'],1058:['literature/lattice-unisolvence/records/xu-1996.md'],1069:['literature/lattice-unisolvence/records/padua-2006.md'],1080:['literature/records/mz2d-caliari-demarchi-vianello-2007.md'],1112:[]}[line]
pairs=list(re.finditer(r'(?m)^Old[^\n]*\n(?:\s*\n)*```[^\n]*\n(.*?)\n```\s*\nNew:\s*\n```[^\n]*\n(.*?)\n```',proposal,re.S))
assert len(pairs)==60,len(pairs)
for m in pairs:
    line=proposal[:m.start()].count('\n')+1
    ts=targets(line)
    if not ts:
        skipped.append({'proposal_line':line,'reason':'Optional merged-report paragraph explicitly conditional on AC wanting that annotation; P2 comparison carries the update.'});continue
    for path in ts:replace(path,m.group(1),m.group(2),'literal proposal line '+str(line))

# Every other fenced block needed for new statement rows and coverage addenda.
fences={proposal[:m.start()].count('\n')+1:m.group(1) for m in re.finditer(r'(?m)^```[^\n]*\n(.*?)\n```',proposal,re.S)}
index_rows=[]
for line in [12,192,430,964,1098,1126]:
    index_rows.extend(x for x in fences[line].splitlines() if re.match(r'^\| (?:LIT\?|LIT-\?\?\?)',x))
newrows=[]; reused=[]
for row in index_rows:
    token=ID.search(row).group(); fid=mapping[token]
    canonical=re.compile(r'^\| '+re.escape(fid)+r'(?:\b|[ (])',re.M)
    if canonical.search(read('literature/INDEX.md')):
        reused.append('- **'+fid+' / '+token+' — reused-statement coverage:** '+mapped(row))
    else:
        newrows.append(mapped(row))
# Append whole standalone tables; do not disturb accepted ordering or other topics.
if newrows:
    append('literature/INDEX.md','### padua-literature-20261103 — final new source statements\n\n| LIT ID | Claim type / keywords | Published statement and hypotheses | Source key | Page / theorem | Record | Reading coverage |\n|---|---|---|---|---|---|---|\n'+'\n'.join(newrows),'new statement table')
if reused:
    # Rows remain verbatim in coverage bullets rather than duplicated canonical IDs.
    body=read('literature/INDEX.md');text='### padua-literature-20261103 — reused-statement coverage\n\n'+'\n'.join(reused)
    settext('literature/INDEX.md',body.rstrip()+'\n\n'+text+'\n','reuse coverage, no duplicate canonical row')
for line in [25,1035,1102]:append('literature/INDEX.md','### padua-literature-20261103 — source coverage addendum (proposal line '+str(line)+')\n\n'+fences[line],'source coverage append '+str(line))

for line in [33,272,475,1003,1132]:
    for row in fences[line].splitlines():
        if row.startswith('| '):add_corpus(row,'corpus proposal line '+str(line))
# Pass2 has an explicit new source record and availability append, but omits a new
# corpus row. This metadata-only row repeats the audited citation/coverage.
if not rows('literature/CORPUS.md','mastroianni-russo-2000'):
    add_corpus('| mastroianni-russo-2000 | G. Mastroianni, M. G. Russo, Weighted Marcinkiewicz inequalities and boundedness of the Lagrange operator, in Mathematical Analysis and Applications, Hadronic Press (2000) 149–182 | no DOI; AC-supplied typeset copy | have (AC local copy, 2026-11-05) | copy pp. 1–3 and 16–28 selected text; pp. 22–23 page images (developer reading) | [record](records/mastroianni-russo-2000.md) | book-page mapping inferred; proofs not fully checked; audit02 developer-only visual-verification limit retained |','pass2 metadata-only missing corpus key')

# Explicit record edits using the audited replacement INDEX rows.
def final_index_row(ident):
    found=[x for x in read('literature/INDEX.md').splitlines() if re.match(r'^\| '+re.escape(ident)+r'(?:\b|[ (])',x)];assert len(found)==1,(ident,len(found));return table_cells(found[0])
for ident,key in [('LIT-119','faghih-et-al-2025'),('LIT-117','faghih-vanbarel-vandebril-2026'),('LIT-118','faghih-vanbarel-vandebril-2026')]:
    cs=final_index_row(ident);assert len(cs)==7,(ident,len(cs))
    subsection('literature/records/'+key+'.md',ident,{'Verification':'VERIFIED-fulltext for the stated items, developer source reading; no inherited proof status. Independent source-verification limits remain as recorded in audit02/03.','Statement in faithful paraphrase':cs[2],'Page / theorem / equation':cs[4]},'update existing '+ident+' record fields')
append('literature/records/faghih-et-al-2025.md',fences[322],'faghih history line')
append('literature/records/faghih-vanbarel-vandebril-2026.md',fences[354],'MOP history line')
addendum_link('faghih-vanbarel-vandebril-2026','2026-11-03 P4 primary-reading addendum')
addendum_link('faghih-et-al-2025','2026-11-03 P4 corrected reading addendum')
addendum_link('filipuk-haneczok-vanassche-2015','2026-11-03 P4 coverage addendum')

# P2: correct current summary paragraphs, retaining existing PR22/additive notes.
svz='literature/records/mz2d-sommariva-vianello-zanovello-2008.md'
body=read(svz);pat=r'(?m)^\*\*Preprint-specific discrepancy:\*\*.*?(?=\n\n|\Z)';mm=re.search(pat,body,re.S);assert mm,'SVZ discrepancy paragraph'
new='**Misprint in preprint and journal:** eq. (25) prints 1/((n+2)(n+3)) in the author preprint and in the published version (journal p. 417, checked on the page image by the developer 2026-11-03). Normalization requires 1/((n+1)(n+2)) = 1/(m(m+1)). The authors\' Table 1 (p. 421) is reproduced only with the correct normalization, so the misprint is typographical. No erratum was found (search not exhaustive). Independent journal-image verification is not claimed; see audit02/03.'
settext(svz,body[:mm.start()]+new+body[mm.end():],'SVZ audited discrepancy correction')
body=read(svz).replace('PDF p. 12 explicitly allows negative weights.','PDF p. 12 explicitly allows negative weights (journal p. 421, developer reading).');settext(svz,body,'SVZ journal locator')
# Literal prose corrections quoted in the LIT294 addendum are fully scoped.
kn='literature/records/mz-prior-art-2026-additions.md';add=(root/P/'addenda/mz-prior-art-2026-additions.addendum.md').read_text()
quoted=re.findall(r'- Old(?: citation)?: "([^"]+)"\.?\s*(?:\n- )?New: "([^"]+)"',add)
assert len(quoted)==3,len(quoted)
for i,(before,after) in enumerate(quoted):replace(kn,before,after,'LIT294 addendum correction '+str(i+1))
for key,label in [('mz2d-sommariva-vianello-zanovello-2008','2026-11-03 journal-body reading'),('mz-prior-art-2026-additions','2026-11-03 primary arXiv re-reading and journal access'),('mz-don-gottlieb-1994','2026-11-03 journal-version comparison'),('dencker-erb-2017','2026-11-03 journal/arXiv comparison'),('mz-an-wu-2022','2026-11-03 primary-reading addendum')]:
    text=(root/P/('addenda/'+key+'.addendum.md')).read_text()
    append('literature/records/'+key+'.md','## '+label+' — padua-literature-20261103\n\n'+text,label)
# Dencker old coverage line may have a bullet prefix; narrow literal phrase only.
de='literature/records/dencker-erb-2017.md';body=read(de);needle='Reading coverage: supplied secondary account only; original fulltext NOT inspected.'
if needle in body:settext(de,body.replace(needle,'Reading coverage: 2026-10-31 supplied secondary account; 2026-11-03 journal §§2.1–2.3 read (see dated section).',1),'Dencker current header coverage')
else:skipped.append({'target':de,'reason':'Exact obsolete generic coverage phrase absent; original detailed coverage and new dated section retained.'})

# P3 explicitly permits separate topic-owned addenda linked from source records.
p3keys=['simonova-tichy-2025','zhu-nakatsukasa-2026','hokanson-2020','brubeck-nakatsukasa-trefethen-2021','liu-narayan-2023','greenbaum-1989','paige-1980-lanczos','paige-2010-augmented','meurant-strakos-2006','sinha-2026','chen-2026']
for key in p3keys:addendum_link(key,'Addendum — padua-literature-20261103 (P3, 2026-11-03)')
for key in ['xu-tams-1994-operator','xu-tams-1994-blockjacobi','dunkl-xu-2014']:addendum_link(key,'2026-11-03 P3 supplement primary-reading addendum')
append('literature/records/austin-et-al-2021.md','## 2026-11-03 P3 attribution note\n\nHokanson arXiv 2009.10803v1, reference [2] (p. 11), cites A. P. Austin, M. Krishnamoorthy, S. Leyffer, S. Mrenna, J. Müller, H. Schulz, Multivariate rational approximation (2019), arXiv:1912.02272v1, and credits multivariate V+A to its Subsec. 3.2 (pp. 4–5). This bibliographic evidence links the arXiv number to the CPC paper; the arXiv metadata page itself was not verified.','Austin bibliographic note')
append('literature/records/zhu-nakatsukasa-2026.md','2026-11-03 (P3): the sentence IS in arXiv v2, Remark 5.1 item 5, p. 20 (pdf.js text read); finding F9\'s "not found" is withdrawn for v2. The old annotation stays as history.','ZN dated historical resolution')

# CORPUS coverage appends, always preserving pre-existing cell text.
coverage={
'greenbaum-1989':'P3 2026-11-03: AC copy 1-s2.0-0024379589902851-main.pdf read, pp. 13–14, 20–24, 30, 43–44, 50–51, 60–62 (Theorems 1, 1′)',
'paige-1980-lanczos':'P3 2026-11-03: AC copy 1-s2.0-0024379580901676-main.pdf read, pp. 237–239, 241, 245–246, 248, 250',
'simonova-tichy-2025':'P3 2026-11-03: arXiv v1 PDF (pdf.js) pp. 1–5, 10–20, 23–26',
'zhu-nakatsukasa-2026':'P3 2026-11-03: arXiv v2 PDF (pdf.js) pp. 1–8, 10–11, 13–15, 18–25; v2 has no appendix (Alg. 4 p. 8, Alg. 5 p. 20); IMA version not read',
'hokanson-2020':'P3 2026-11-03: arXiv v1 PDF pp. 1–7, 11–12',
'brubeck-nakatsukasa-trefethen-2021':'P3 2026-11-03: arXiv v1 PDF pp. 1, 3–5, 8–9',
'liu-narayan-2023':'P3 2026-11-03: arXiv v2 PDF pp. 1–2, 4–6, 9–13, 19, 21–22',
'paige-2010-augmented':'P3 2026-11-03: author PDF pp. 2347–2358 (statements)',
'meurant-strakos-2006':'P3 2026-11-03: author PDF pp. 505–506, 510–512',
'sinha-2026':'P3 2026-11-03: arXiv v1 PDF pp. 1, 27, 37–39, 42, 45, 49 (statements)',
'chen-2026':'P3 2026-11-03: arXiv v2 (18 Oct 2026) PDF pp. 1, 10–11, 14–16, 20–22 (statements); v1 numbering superseded'}
for key,text in coverage.items():edit_corpus(key,[(4,'append',text)],'P3 reading coverage '+key)
for key,txt in [('greenbaum-1989','have (AC local copy, 2026-11-03)'),('paige-1980-lanczos','have (AC local copy)')]:edit_corpus(key,[(3,'append',txt)],'P3 availability '+key)
edit_corpus('paige-1980-lanczos',[(6,'replace',('Whole source; pending-reference. Online pass: Whole source (scan).','Theorems 4.2–4.3 (pp. 252–253) and pp. 242–244 unread (P3 2026-11-03).'))],'Paige scoped gaps')
edit_corpus('hokanson-2020',[(3,'replace',('supplied account; fulltext pending','open (arXiv)'))],'Hokanson availability')
edit_corpus('chen-2026',[(1,'append','(v2 18 Oct 2026)')],'Chen version citation')
pass2_records={
'mastroianni-russo-2000':'literature/records/mastroianni-russo-2000.md',
'kolomoitsev-lomako-prestin-2018':'literature/records/kolomoitsev-lomako-prestin-2018.md',
'xu-1996':'literature/lattice-unisolvence/records/xu-1996.md',
'mz2d-caliari-demarchi-vianello-2007':'literature/records/mz2d-caliari-demarchi-vianello-2007.md',
'padua-2006':'literature/lattice-unisolvence/records/padua-2006.md'}
for key,recordpath in pass2_records.items():
    if not rows('literature/CORPUS.md',key):
        # The proposal calls for availability appends but these canonical record
        # keys have no CORPUS row. Supply metadata and a pointer, no new theorem.
        title=read(recordpath).splitlines()[0].lstrip('# ')
        if ' — ' in title:title=title.split(' — ',1)[1]
        recordlink=recordpath.removeprefix('literature/')
        add_corpus('| '+key+' | '+title+' | exact citation and DOI in linked record | have (AC local copy, 2026-11-05) | 2026-11-05 journal-version coverage and locators in the campaign addendum; developer-verified source checks | [record]('+recordlink+') | independent journal/page-image verification limits retained in audit02/03 |','Pass2 metadata-only corpus-key completion '+key)
    edit_corpus(key,[(3,'append','have (AC local copy, 2026-11-05)'),(4,'append','Pass2 2026-11-05: supplied-copy reading; exact coverage/locators and remaining limits in topics/padua-literature-20261103/addenda/journal-versions-2026-11-05.addendum.md and the source record')],'Pass2 availability '+key)

# Historical cross-topic files get only dated annotations, never replacement of
# their scientific statuses or proof bodies (except the audited Xu range line).
lit='topics/padua-mz-2d-20261101/literature.md'
append(lit,'## 2026-11-03 source-reading update — padua-literature-20261103\n\nLIT-427: the journal body (p. 417) prints the same (n+2)(n+3) denominator; the misprint is in both versions. See literature/records/mz2d-sommariva-vianello-zanovello-2008.md. LIT-014: journal body compared 2026-11-03, identical to arXiv v2 on inspected items. These are developer source readings with audit02/03 verification limits; no PD status changes.','merged 2D literature dated note')
append('topics/padua-mz-2d-20261101/report.md','## 2026-11-03 source-reading update — padua-literature-20261103\n\nSVZ and Dencker–Erb journal bodies were read 2026-11-03; KLP from arXiv v1. Xu1996, KL2021 and ASV published bodies remained unread by that P2 reader at that pass. The later pass2 journal-version addendum records the subsequent supplied-copy checks and their developer-only audit qualification. No scientific status changes.','merged 2D report source note')
append('topics/mz-prior-art-20261101/comparison.md','## 2026-11-03 source-reading update — padua-literature-20261103\n\nForward citations: Wu, Appl. Math. Lett. 182 (2026) 110033 read in full 2026-11-03: abstract MZ ⇒ Galerkin stability, no CC constants; verdict unchanged. König–Nielsen: parameter restriction confirmed from arXiv pp. 3,15; journal body inaccessible (unlicensed). Don–Gottlieb: journal version compared, identical on items used. These dated notes do not change the original comparison verdicts or proof statuses.','merged 1D comparison dated note')

# Audited provenance remains developer-specific even when INDEX says VERIFIED.
append('literature/INDEX.md','### padua-literature-20261103 — audit acceptance boundary\n\nThe source-reading and VERIFIED labels above identify the credited developer\'s reading at the stated locators. Audit02/03 accepted these bounded literature records; inaccessible journal/image/NTNU/Crossref checks remain developer-verified only as specified there. No independent auditor image inspection, exhaustive priority certification, local source-theorem proof or manuscript/submission readiness is inferred.','bounded source-verification qualification')

changed={p:b for p,b in work.items() if b!=old[p]}
receipt={'proposal_git_blob':hashlib.sha1(b'blob '+str(len(proposal.encode())).encode()+b'\0'+proposal.encode()).hexdigest(),'mode':'write' if a.write else 'dry-run','literal_blocks':len(pairs),'operations':ops,'skipped':skipped,'changed':[{'path':p,'before_sha256':hashlib.sha256(old[p].encode()).hexdigest(),'after_sha256':hashlib.sha256(b.encode()).hexdigest()} for p,b in sorted(changed.items())],'new_index_rows':len(newrows),'reused_coverage_rows':len(reused)}
if a.receipt:a.receipt.write_text(json.dumps(receipt,indent=2)+'\n')
if a.write:
    for p,b in changed.items():(root/p).write_text(b)
print(json.dumps({'mode':receipt['mode'],'changed_files':len(changed),'literal_blocks':len(pairs),'new_index_rows':len(newrows),'reused_coverage_rows':len(reused),'skipped':skipped},indent=2))
