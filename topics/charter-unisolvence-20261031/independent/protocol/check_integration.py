"""Read-only checks of canonical theory transformations against actual Git blobs."""
import hashlib,json,pathlib,re,subprocess
ROOT=pathlib.Path(__file__).resolve().parents[4]
TOP=ROOT/'topics/charter-unisolvence-20261031'
def sha(b): return hashlib.sha256(b).hexdigest()
mp=json.loads((TOP/'final-id-map.json').read_text())
checks=[]
for row in json.loads((TOP/'integration-impact.json').read_text()):
    old=subprocess.check_output(['git','show',row['source_commit']+':'+row['old_path']],cwd=ROOT)
    new=(ROOT/row['new_path']).read_bytes()
    expected=old.decode()
    for a in sorted(mp,key=len,reverse=True): expected=expected.replace(a,mp[a])
    for edit in row.get('editorial_replacements', []):
        expected=expected.replace(edit['old'],edit['new'])
    checks.append(dict(path=row['new_path'],source_commit=row['source_commit'],source_blob_sha256=sha(old),source_hash_matches=sha(old)==row['before_sha256'],final_hash_matches=sha(new)==row['after_sha256'],exact_documented_transform=expected.encode()==new))
files=[p for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.parts and '__pycache__' not in p.parts]
links=[]
for directory in ['tracks','literature','state']:
    for p in (ROOT/directory).rglob('*.md'):
        for target in re.findall(r'\]\(([^)]+)\)',p.read_text()):
            if '://' in target or target.startswith('#'): continue
            if not (p.parent/target.split('#')[0]).exists(): links.append(dict(file=str(p.relative_to(ROOT)),target=target))
result=dict(head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),theory_checks=checks,all_source_transforms_pass=all(all(row[k] for k in ['source_hash_matches','final_hash_matches','exact_documented_transform']) for row in checks),non_git_non_cache_total_bytes=sum(p.stat().st_size for p in files),largest_file_bytes=max(p.stat().st_size for p in files),pdf_zip_html_paths=[str(p.relative_to(ROOT)) for p in files if p.suffix.lower() in ['.pdf','.zip','.html']],missing_canonical_markdown_links=links,rules_or_github_diff=subprocess.check_output(['git','diff','d36722823441dc40c6e19d69a174459348dd309c','--','AGENTS.md','agents','.github'],cwd=ROOT,text=True))
print(json.dumps(result,indent=2))
