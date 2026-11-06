import os
O = '/tmp/claude-0/-home-user-padua-research/8d35f915-ba92-5bfd-81d7-431865a9781c/scratchpad/audit/num'
os.chdir(O)
t = open('tables.md').read()
cc, rest = t.split('@@PADUA'); pad, rest = rest.split('@@BK\n'); bk, bkx = rest.split('@@BKX')
runlog = open('runlog.txt').read().replace(O, '$OUT')
rows = []
for l in runlog.strip().split('\n'):
    if l == 'DONE':
        continue
    name, rc, wall, cmd = l.split(' ', 3)
    rows.append(f"| {name} | `{cmd[4:]}` | {rc[3:]} | {float(wall[5:]):.2f} |")
jd = open('jdiff.txt').read().replace(O, '$OUT')
tmpl = open(os.path.join(O, 'src', 'report_template.md')).read()
rep = tmpl.replace('@@O@@', O).replace('@@ROWS@@', '\n'.join(rows)).replace('@@JD@@', jd.strip()) \
    .replace('@@CC@@', cc.strip()).replace('@@PAD@@', pad.strip()).replace('@@BKT@@', bk.strip()).replace('@@BKX@@', bkx.strip())
open('report.md', 'w').write(rep)
print(len(rep))
