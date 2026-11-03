import subprocess, re, sys, json
repo='/home/user/padua_research'
def git(*a): return subprocess.run(['git','-C',repo]+list(a),capture_output=True,text=True).stdout
refs=sys.argv[1:]
pat={'PD-T':re.compile(r'PD-T(\d{3})'),'PD-N':re.compile(r'PD-N(\d{3})'),'IDEA':re.compile(r'IDEA-(\d{3})'),'LIT':re.compile(r'LIT-(\d{3,4})')}
# range patterns like PD-T206–225 or PD-T206–PD-T225
rng=re.compile(r'(PD-T|PD-N|IDEA-?|LIT-?)\s?(\d{3,4})\s*[–-]\s*(?:PD-T|PD-N|IDEA-?|LIT-?)?\s?(\d{3,4})')
out={}
for ref in refs:
    files=[f for f in git('ls-tree','-r','--name-only',ref).split('\n') if f.endswith('.md') or f.endswith('.json')]
    targets=[f for f in files if f in ('PROOF_STATUS.md','state/IDEAS.md','literature/INDEX.md','ID_CROSSWALK.md','RESULTS.md') or f.endswith('ALLOCATIONS.md')]
    res={}
    for f in targets:
        txt=git('show',f'{ref}:{f}')
        m={}
        for k,p in pat.items():
            vals=[int(x) for x in p.findall(txt)]
            if k=='LIT': vals=[v for v in vals if v<1000]
            m[k]=max(vals) if vals else None
        res[f]=m
    out[ref]=res
print(json.dumps(out,indent=1))
