# Claude readiness-01 reservation refresh: scan every ALLOCATIONS.md and ID_CROSSWALK.md range on each
# checked head for overlap with PR31's PD-T522-553 / IDEA-608-615 / LIT-633-635, and max used IDs in registries.
import subprocess,re,collections
br={'main':'origin/main','PR27':'origin/codex/padua-argmax-bridge-20261105','PR33':'origin/codex/padua-3d-20261106','PR31':'origin/codex/padua-mz-sharp-constants-20261106'}
ours={'PD-T':(522,553),'IDEA':(608,615),'LIT':(633,635)}
pat=re.compile(r'(PD-T|PD-N|IDEA|LIT)-?(\d{3,4})\s*[–-]\s*(?:(?:PD-T|PD-N|IDEA|LIT)-?)?(\d{3,4})')
for name,b in br.items():
    files=subprocess.run(['git','ls-tree','-r','--name-only',b],capture_output=True,text=True).stdout.split()
    mx=collections.defaultdict(int); over=[]
    for f in files:
        if not (f.endswith('ALLOCATIONS.md') or f=='ID_CROSSWALK.md') or 'padua-mz-sharp-constants' in f: continue
        txt=subprocess.run(['git','show',f'{b}:{f}'],capture_output=True,text=True).stdout
        for ns,a,c in pat.findall(txt):
            a,c=int(a),int(c)
            if c<a or c-a>400: continue
            mx[ns]=max(mx[ns],c)
            if ns in ours and a<=ours[ns][1] and c>=ours[ns][0] and f!='ID_CROSSWALK.md': over.append((f,ns,a,c))
    used=collections.defaultdict(int)
    for f in ['PROOF_STATUS.md','state/IDEAS.md','literature/INDEX.md']:
        txt=subprocess.run(['git','show',f'{b}:{f}'],capture_output=True,text=True).stdout
        for ns,n in re.findall(r'\b(PD-T|PD-N|IDEA|LIT)-?(\d{3})\b',txt): used[ns]=max(used[ns],int(n))
    print(name,b,'ledger-max(excl ours):',dict(mx),'used-max:',dict(used),'OVERLAPS:',over)
