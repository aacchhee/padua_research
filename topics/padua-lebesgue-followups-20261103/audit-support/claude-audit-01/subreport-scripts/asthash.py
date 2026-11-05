import ast,hashlib,copy,sys
p='/home/claude/padua_research/topics/padua-proof-attempts-2-20261101/code/a5_checker_n8.py'
m=ast.parse(open(p,'rb').read());cls=next(n for n in m.body if isinstance(n,ast.ClassDef) and n.name=='Verifier')
b=next(n for n in cls.body if isinstance(n,ast.FunctionDef) and n.name=='boundaries')
print(sys.version.split()[0],'boundaries',hashlib.sha256(ast.dump(b,include_attributes=False).encode()).hexdigest())
run=next(n for n in cls.body if isinstance(n,ast.FunctionDef) and n.name=='run')
start=next(i for i,n in enumerate(run.body) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='summary' for t in n.targets))
tgt=ast.dump(ast.parse('allow_partial or complete',mode='eval').body,include_attributes=False)
stop=next(i for i,n in enumerate(run.body[start:],start) if isinstance(n,ast.Expr) and isinstance(n.value,ast.Call) and isinstance(n.value.func,ast.Name) and n.value.func.id=='require' and n.value.args and ast.dump(n.value.args[0],include_attributes=False)==tgt)
body=copy.deepcopy(run.body[start:stop+1])
print('summary',hashlib.sha256(ast.dump(ast.Module(body=body,type_ignores=[]),include_attributes=False).encode()).hexdigest())
