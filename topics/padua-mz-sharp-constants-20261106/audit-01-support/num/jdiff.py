import json, sys, math
def walk(a,b,path,out):
    if isinstance(a,dict) and isinstance(b,dict):
        for k in sorted(set(a)|set(b)):
            if k not in a: out['only_committed'].append(path+'/'+k); continue
            if k not in b: out['only_new'].append(path+'/'+k); continue
            walk(a[k],b[k],path+'/'+str(k),out)
    elif isinstance(a,list) and isinstance(b,list):
        if len(a)!=len(b): out['len'].append((path,len(a),len(b)))
        for i,(x,y) in enumerate(zip(a,b)): walk(x,y,path+f'[{i}]',out)
    elif isinstance(a,bool) or isinstance(b,bool) or not (isinstance(a,(int,float)) and isinstance(b,(int,float))):
        if a!=b: out['neq'].append((path,a,b))
        else: out['eq']+=1
    else:
        d=abs(a-b); r=d/max(abs(a),abs(b)) if max(abs(a),abs(b))>0 else 0
        out['num'].append((path,a,b,d,r))
new=json.load(open(sys.argv[1])); old=json.load(open(sys.argv[2]))
out=dict(only_committed=[],only_new=[],len=[],neq=[],num=[],eq=0)
walk(new,old,'',out)
ign=lambda p: any(s in p.lower() for s in ('second','time','elapsed','environment','python','numpy','scipy','platform','output','command','wall','cpu','host','date','argv'))
num=[x for x in out['num'] if not ign(x[0])]; numi=[x for x in out['num'] if ign(x[0])]
print('numeric fields compared:',len(num),' identical:',sum(1 for x in num if x[3]==0))
if num:
    ma=max(num,key=lambda x:x[3]); mr=max(num,key=lambda x:x[4])
    print('max abs diff %.3e at %s'%(ma[3],ma[0])); print('max rel diff %.3e at %s'%(mr[4],mr[0]))
print('timing/env numeric fields ignored:',len(numi))
print('non-numeric equal:',out['eq'])
print('non-numeric differing (%d):'%len(out['neq']))
for p,a,b in out['neq']:
    sa,sb=str(a),str(b)
    print('  ',p,'| new:',sa[:100],'| committed:',sb[:100])
for k in ('only_committed','only_new','len'):
    if out[k]: print(k,out[k][:20])
