import sys, os, subprocess, json
sys.argv=[sys.argv[0], sys.argv[1]]
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'adv.py')).read().split('# 1 restore')[0])
repo, m, pay, g = mkrepo('r2')
(repo/'X/demo').mkdir(parents=True); (repo/'X/demo/cold-storage-export-receipt.json').write_text('{}'); g('add','-A'); g('commit','-qm','t')
(repo/'X/demo/cold-storage-export-receipt.json').unlink()
rc,out=cli(repo,'export','demo','--dest',repo/'X'); rec('R1 export receipt at tracked(absent) path -> refuse before payload', rc!=0 and not (repo/'X/demo/topics').exists(), out)
(repo/'Y').mkdir(); (repo/'Y/demo').write_text('tracked file'); g('add','-A'); g('commit','-qm','t2')
rc,out=cli(repo,'export','demo','--dest',repo/'Y'); rec('R2 export dir == tracked file -> refuse', rc!=0 and (repo/'Y/demo').read_text()=='tracked file', out)
# git worktree (.git file) as source root itself: linked worktree source
wt = BASE/'wt-linked'; subprocess.run(['git','-C',str(repo),'worktree','add','-q',str(wt)],check=True)
rc,out=cli(wt,'verify','demo'); rc2,out2=cli(wt,'restore','demo','--dest',BASE/'wtdest'); rc3,out3=cli(wt,'clean','demo','--dest',BASE/'wtdest')
rec('R3 linked-worktree source (.git file at own root) operates', rc==0 and rc2==0 and rc3==0, out3)
