import subprocess, hashlib, ast, sys, json
R='/home/claude/padua_research'
DEV='5b2e36710144d5ab8dd1b8ee9dc2e8b0f1e13033'
C='topics/padua-lebesgue-followups-20261103/code/'
items=[
 ('t1_check.py','59ebc4f5ede28a769f1726a5422ab08d859ee3a9','0345e62ef9bb88fa11640e135d211648611c9536b85fec528d694e94ef57a69f','13fdfa85a4bcaa76e5e5b6ba3d3ede9d80e3ae006f20855f14fa82b581f5859a',2215),
 ('t1_produce.py','cd78c69852b8500d0e16e5fe26f7ee9bc09ecc3f','1ac5cbb83302d12006f35f042954fd6c76881e263ed6de065ca22c5302a77664','b52cdec4daf0b67c1dcee2fb0ea7242740b7c4c2987654aa9a02c4a72ba515bc',2659),
 ('t1_memo.py','90a84a680e1eeb695fbd8a56efef4181c5a884d9','d910cb5857a0c09288330925ca833f820690ef76553d8e66402c3e5e352b7e35','0e433e088236a44e5fe711aff532f8200703172497f6606bc8c68922e5371f2e',1084),
 ('t1_memo_controls.py','f26724d64e853dd87ca213a62ae6e6c04a45b195','e5c146fd8a85fecf642c98cd0c92c62d2594c3d2a65846a197fe0757f853b098','ac4c1364ea632136ce57ab22d518bf913ba2ab7c54cc41b1dd6c0f025ceb8c0f',3461),
 ('t1_corner_certificate_controls.py','6e7d5cb5cdb9924d5b5e64ade3f93a2358d91f1d','cf237404ee914a8d14255638506ace31d626aa42ca77f76934427faac361738d','9b0f7d4be27121b7893a3855a5c8a4f590e3e1f2f11925bd2073fc6fb1d1b8bf',2346),
 ('t1_corner_crossvalidate.py','c3f42881537b47e7e11f3e38ca25fb206a445e47','291ce1a3683cba42f0811c2d378840b5bc3ff6bdd034805d2504cf9d010d6948','f1a9c73fe3070c51b09800c321368210b8efb79bd0699a575f2d7c51373a18c0',1649),
 ('t1_boundary.py','011b8c4174bf1506479021f306c65da71f173e1e','7753e4ba8bc440133a46e6f5325e8b5531f20e5a20d8d0aa6778a32bacbdb7f0','a70e25326e513e65554c197c62d3fe684d45f6e54aa72e2e6df68bc5a25510bb',None),
]
def git(*a): return subprocess.run(['git','-C',R,*a],capture_output=True,check=True).stdout
ok=True
for name,blob,oldsha,newsha,nbytes in items:
    old=git('cat-file','blob',blob)
    cur=git('show',f'{DEV}:{C}{name}')
    head=open(f'{R}/{C}{name}','rb').read()
    so=hashlib.sha256(old).hexdigest(); sc=hashlib.sha256(cur).hexdigest()
    # diff lines
    ol=old.splitlines(keepends=True); cl=cur.splitlines(keepends=True)
    import difflib
    d=[l for l in difflib.unified_diff([x.decode() for x in ol],[x.decode() for x in cl],n=0) if not l.startswith(('---','+++','@@'))]
    removed=[l for l in d if l.startswith('-')]
    added=[l[1:] for l in d if l.startswith('+')]
    # attempt removal: remove exactly the added lines (contiguous block)
    curs=cur.decode(); addblock=''.join(added)
    idx=curs.find(addblock)
    restored=(curs[:idx]+curs[idx+len(addblock):]).encode() if idx>=0 and curs.count(addblock)==1 else None
    bytes_eq = restored==old
    try:
        astold=ast.dump(ast.parse(old)); astrest=ast.dump(ast.parse(restored)) if restored else None
        # AST of current with guard If stmt removed
        tc=ast.parse(cur); body=[s for s in tc.body if not (isinstance(s,ast.If) and isinstance(s.test,ast.UnaryOp) and isinstance(s.test.op,ast.Not) and getattr(s.test.operand,'id',None)=='__debug__')]
        tc.body=body; ast_eq=ast.dump(tc)==astold
    except Exception as e: ast_eq=repr(e)
    r=dict(name=name,blob=blob,old_sha_ok=so==oldsha,old_len=len(old),old_len_ok=(nbytes is None or len(old)==nbytes),cur_sha_at_dev=sc,cur_sha_ok=sc==newsha,head_equals_dev=head==cur,
           removed_lines=len(removed),added=added,restore_bytes_equal=bytes_eq,ast_equal_after_removing_guard_If=ast_eq)
    print(json.dumps(r))
    ok &= r['old_sha_ok'] and r['cur_sha_ok'] and bytes_eq and ast_eq is True and len(removed)==0
print('ALL_OK',ok)
