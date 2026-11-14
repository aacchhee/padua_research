import subprocess
exec(open('size7.py').read().split("main=inv")[0])
head=inv('HEAD')
for ref in ['f4e8d8d','656c15b','5f0e8e4','d340d2e','8b1a6b5','ff92191^']:
    o=inv(ref)
    shrink=sum(o[p][1]-s for p,(b,s) in head.items() if p in o and s<o[p][1])
    deleted=sum(s for p,(b,s) in o.items() if p not in head)
    print(ref,'total',sum(s for _,s in o.values()),'shrink',shrink,'deleted',deleted,'sum',shrink+deleted)
