import re,subprocess,json,sys
T='topics/padua-proof-attempts-2-20261101'
txt=subprocess.check_output(['git','show',f'4265bb9:{T}/proposed-record-changes.md'],text=True)
pat=re.compile(r"Target: `([^`]+)`\s+Pinned commit: `([0-9a-f]+)`\s+Old:\s+```text\n(.*?)```\s+New:\s+```text\n(.*?)```",re.S)
out=[]
for i,(path,pin,old,new) in enumerate(pat.findall(txt),1):
    def src(c):
        r=subprocess.run(['git','show',f'{c}:{path}'],capture_output=True,text=True); return r.stdout if r.returncode==0 else None
    s=src(pin); m=src('28aaa20861d08074b77efc74eaef75cdcb36234d'); h=src('HEAD')
    o=old.rstrip('\n')
    rec=dict(i=i,path=path,pin=pin[:7],old_len=len(o),
      at_pin=None if s is None else s.count(o) if o else ('absent-ok' if s is None else 'exists'),
      at_main=None if m is None else m.count(o),
      at_head=None if h is None else h.count(o),
      old_in_new=(o in new), new_minus_old=len(new)-len(o))
    if not o: rec['at_pin']='file absent' if s is None else 'FILE EXISTS'
    out.append(rec)
for r in out: print(r)
