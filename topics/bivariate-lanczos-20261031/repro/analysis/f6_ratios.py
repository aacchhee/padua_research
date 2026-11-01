import re,sys,math
for log in sys.argv[1:]:
    print("##",log.split('/')[-1])
    for line in open(log):
        m=re.match(r"(Padua n=\d+ (?:N=M=\d+|randW)|random M=\d+ n=\d+ N=\d+|sanity15) (\S+)\s+(.*)$",line.strip())
        if not m: continue
        v={}
        for t in m[3].split("  "):
            mm=re.match(r"([\w-]+):H([\d.e+-]+)/Q([\d.e+-]+)",t.strip())
            if mm: v[mm[1]]=float(mm[2])
        g=v['givens-scheme']
        print(f"{m[1]:28s} {m[2]:7s} G/HL={g/v['hl']:5.1f} ({math.log10(g/v['hl']):.2f} dig)  G/CGS2={g/v['cgs2']:5.1f}  G/HH={g/v['hh']:5.1f}  HL/HH={v['hl']/v['hh']:4.1f}  BJ/HL={v['bj']/v['hl']:4.1f}  largest/scheme={v['givens-largest']/g:.1e}")
