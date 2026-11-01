"""Response-01 (audit-01 A8): identify the exact input bytes the campaign agents read.

Run from the repository root:  python topics/programme-ideas-20261031/sources/campaign-inputs/provenance.py /home/claude/inputs
For every file of the orchestrator's input mirror except third-party PDFs (papers/), saved web pages (web/) and
AC's private notes (padua/, recorded separately in the cold-storage manifest), it records size, SHA-256, the git
blob id, and the commits of this repository (any branch) that introduce or remove that exact blob with the path.
A non-empty hit list proves the bytes are retrievable from the public repository history.
"""
import hashlib, json, os, subprocess, sys
root = sys.argv[1]
def git(*a):
    return subprocess.run(('git',) + a, capture_output=True, text=True).stdout
rows = []
for dp, dn, fn in os.walk(root):
    for f in fn:
        p = os.path.join(dp, f); rel = os.path.relpath(p, root)
        if rel.split(os.sep)[0] in ('papers', 'web', 'padua'):
            continue
        blob = git('hash-object', p).strip()
        hits, cur = [], None
        for line in git('log', '--all', '--format=C %H %cI', '--name-only', '--find-object=' + blob).splitlines():
            if line.startswith('C '):
                cur = line.split()[1:3]
            elif line.strip() and cur:
                hits.append({'commit': cur[0], 'date': cur[1], 'path': line.strip()})
        rows.append({'snapshot': rel, 'bytes': os.path.getsize(p),
                     'sha256': hashlib.sha256(open(p, 'rb').read()).hexdigest(),
                     'git_blob': blob, 'repo_history': hits})
rows.sort(key=lambda r: r['snapshot'])
print(json.dumps({'mirror_root': root, 'files': len(rows),
                  'retrievable_from_repo': sum(1 for r in rows if r['repo_history']),
                  'rows': rows}, indent=1, ensure_ascii=False))
