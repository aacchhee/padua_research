"""Normalize PR21 table presentation and root RESULTS link locations."""
import argparse
from pathlib import Path
import re
import subprocess

ap = argparse.ArgumentParser()
ap.add_argument('--repo', type=Path, default=Path('.'))
ap.add_argument('--base', default='65b24972954a6e13e950a489ef9ecb0397601328')
a = ap.parse_args()
r = a.repo.resolve()
p = r/'literature/INDEX.md'
out = []
for line in p.read_text().splitlines():
    m = re.match(r'^\| LIT-(\d{3})(?!\d)',line)
    if m and 482<=int(m[1])<=512:
        cells = line[1:-1].strip().split(' | ')
        assert len(cells)==7
        line = '| '+' | '.join(re.sub(r'(?<!\\)\|',r'\\|',c) for c in cells)+' |'
    out.append(line)
p.write_text('\n'.join(out)+'\n')
p = r/'literature/CORPUS.md'
before = subprocess.check_output(['git','-C',str(r),'show',a.base+':literature/CORPUS.md'],text=True)
keys = set(re.findall(r'^\| ([a-z][a-z0-9-]+) \|',before,re.M))
marker = '## padua-literature-20261103 — source coverage registration'
s = p.read_text()
keep = []
new = []
for line in s.splitlines():
    if line==marker or line in ['| Key | Citation | DOI / URL | Availability | Reading coverage | Record | Gaps |','|---|---|---|---|---|---|---|'] and marker in s and s.index(marker)<s.index(line):
        continue
    m = re.match(r'^\| ([a-z][a-z0-9-]+) \|',line)
    if m and m[1] not in keys:
        cells = line[1:-1].strip().split(' | ')
        assert len(cells)==7
        new.append('| '+' | '.join(re.sub(r'(?<!\\)\|',r'\\|',c) for c in cells)+' |')
    else:
        keep.append(line)
header = marker+'\n\n| Key | Citation | DOI / URL | Availability | Reading coverage | Record | Gaps |\n|---|---|---|---|---|---|---|\n'
assert new
p.write_text('\n'.join(keep).rstrip()+'\n\n'+header+'\n'.join(new)+'\n')
p = r/'RESULTS.md'
head,section = p.read_text().split('## padua-literature-20261103\n',1)
p.write_text(head+'## padua-literature-20261103\n'+section.replace('(../topics/','(topics/'))
