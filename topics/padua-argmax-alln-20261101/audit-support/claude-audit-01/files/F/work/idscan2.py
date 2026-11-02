import subprocess, re, sys, json
repo='/home/user/padua_research'
def git(*a): return subprocess.run(['git','-C',repo]+list(a),capture_output=True,text=True).stdout
# range-aware: "PD-T206–225", "PD-T206–PD-T225", "PD-T206-225", "PD-T 206"
tok=re.compile(r'(PD-T|PD-N|IDEA-|LIT-|IDEA|LIT)\s?(\d{3,4})(?:\s*[–-]\s*(?:PD-T|PD-N|IDEA-|LIT-|IDEA|LIT)?\s?(\d{3,4}))?')
thr={'PD-T':206,'PD-N':78,'IDEA':316,'LIT':460}
for ref in sys.argv[1:]:
    files=git('ls-tree','-r','--name-only',ref).split('\n')
    hits={}
    mx={'PD-T':0,'PD-N':0,'IDEA':0,'LIT':0}
    for f in files:
        if not (f.endswith('.md') or f.endswith('.json')): continue
        if f.startswith('topics/padua-argmax-alln-20261101/') : continue
        txt=git('show',f'{ref}:{f}')
        for m in tok.finditer(txt):
            ns=m.group(1).rstrip('-'); a=int(m.group(2)); b=int(m.group(3)) if m.group(3) else a
            if ns=='LIT' and (a>=1000 or b>=1000): continue
            if b<a: b=a
            hi=b
            if hi>mx[ns]: mx[ns]=hi
            if hi>=thr[ns]:
                hits.setdefault(f,set()).add(m.group(0))
    print('==',ref,'max(excluding this topic):',mx)
    for f,s in sorted(hits.items()):
        print('  ',f, sorted(s)[:12])
