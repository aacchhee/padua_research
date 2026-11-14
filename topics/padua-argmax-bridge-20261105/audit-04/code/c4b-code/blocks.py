import re,sys
T='/home/user/padua_research/topics/padua-argmax-bridge-20261105/'
P=open(T+'paper/sections/comparison-unified.tex').read()
C=open(T+'companion-paper/sections/comparison-unified.tex').read()
envs=['lemma','theorem','proposition','corollary','definition','remark','equation','align','gather','multline']
def blocks(s):
    out=[]
    for m in re.finditer(r'\\begin\{(lemma|theorem|proposition|corollary|definition|remark|equation|align|gather|multline)\}(.*?)\\end\{\1\}',s,re.S):
        out.append((m.group(1),m.group(0),m.start()))
    return out
bp=blocks(P); bc=blocks(C)
print(len(bp),len(bc))
lines_c=[C.count('\n',0,b[2])+1 for b in bc]
for i,(a,b) in enumerate(zip(bp,bc)):
    same=a[1]==b[1]
    lab=re.findall(r'\\label\{([^}]*)\}',b[1])
    if lines_c[i]<=2100:
        print(i,b[0],lines_c[i],lab,'SAME' if same else 'DIFF')
# labels and refs in companion range
rng=C.split('\n')[:2050]
txt='\n'.join(rng)
print(sorted(set(re.findall(r'\\(?:eq)?ref\{([^}]*)\}',txt))))
