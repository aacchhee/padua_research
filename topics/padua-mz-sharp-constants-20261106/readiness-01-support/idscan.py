import re,collections,subprocess,sys
def scan(text,kind):
    c=collections.Counter(); occ=collections.defaultdict(list)
    for i,l in enumerate(text.splitlines(),1):
        if kind=='IDEA':
            m=re.match(r'^###\s+(IDEA-\d+)\b',l)
            if m: c[('h',m.group(1))]+=1; occ[('h',m.group(1))].append(i)
            m=re.match(r'^\|\s*(IDEA-\d+)\b',l)
            if m: c[('r',m.group(1))]+=1; occ[('r',m.group(1))].append(i)
        else:
            m=re.match(r'^\|\s*(LIT-\d+)\b',l)
            if m: c[m.group(1)]+=1; occ[m.group(1)].append(i)
    return c,occ
for f,k in [('state/IDEAS.md','IDEA'),('literature/INDEX.md','LIT')]:
    new,occ=scan(open(f).read(),k)
    old,_=scan(subprocess.run(['git','show','origin/main:'+f],capture_output=True,text=True).stdout,k)
    dn={x:v for x,v in new.items() if v>1}; do={x:v for x,v in old.items() if v>1}
    print(f,'dups now',len(dn),'dups on main',len(do),'new dups:',{x:(v,occ[x]) for x,v in dn.items() if do.get(x)!=v})
    for t in (['IDEA-608','IDEA-609','IDEA-610','IDEA-611'] if k=='IDEA' else ['LIT-633']):
        print('  ',t,{x:(v,occ[x]) for x,v in new.items() if (x[1] if isinstance(x,tuple) else x)==t})
