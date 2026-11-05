import sys,subprocess
REC={'md','py','sh','tex','bib','svg','gitignore'}
def run(rev):
    out=subprocess.run(['git','-C','/home/claude/padua_research','ls-tree','-r','-l',rev],capture_output=True,text=True,check=True).stdout
    tot=0;byext={};T='topics/padua-lebesgue-followups-20261103/'
    topic=0
    for line in out.splitlines():
        meta,path=line.split('\t',1);size=int(meta.split()[3])
        name=path.rsplit('/',1)[-1];ext=name.rsplit('.',1)[-1].lower() if '.' in name else ''
        if ext in REC: continue
        tot+=size;byext[ext]=byext.get(ext,0)+size
        if path.startswith(T): topic+=size
    return tot,byext,topic
for rev in(sys.argv[1:]):
    t,b,tp=run(rev);print(rev[:7],'total',t,'MB',round(t/1e6,3),'MiB',round(t/2**20,3),'topic',tp)
    print('  ',sorted(b.items(),key=lambda x:-x[1])[:12])
    print('   excl json-manifests? total-json',t-b.get('json',0))
