exec(open('size7.py').read().split("main=inv")[0])
head=inv('HEAD'); o=inv('8b1a6b5'); f=inv('f4e8d8d')
for p,(b,s) in head.items():
    if p in o and s!=o[p][1]: print('vs8b1a',p,o[p][1],'->',s)
# max-size since f4e8d8d along first-parent commits
import subprocess
revs=subprocess.check_output(['git','-C',R,'rev-list','--first-parent','f4e8d8d..HEAD'],text=True).split()
mx={}
for r in revs+['f4e8d8d']:
    for p,(b,s) in inv(r).items():
        if p.startswith('topics/padua-argmax-bridge'): mx[p]=max(mx.get(p,0),s)
cur={p:s for p,(b,s) in head.items() if p.startswith('topics/padua-argmax-bridge')}
print('sum shrink since f4e8d8d (max over first-parent)',sum(mx[p]-cur.get(p,0) for p in mx))
