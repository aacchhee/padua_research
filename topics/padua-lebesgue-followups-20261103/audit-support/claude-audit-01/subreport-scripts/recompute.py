import sys,json,hashlib,gzip,copy
R='/home/claude/padua_research';T=R+'/topics/padua-lebesgue-followups-20261103'
sys.path.insert(0,T+'/code')
import t1_compose as tc
from t1_payload import canonical,proof_payload,unique
E=T+'/evidence/'
def L(n):
    raw=open(E+n,'rb').read();return raw,json.loads(raw)
sha=lambda b:hashlib.sha256(b).hexdigest()
arch=json.loads(gzip.decompress(open('/home/claude/audit/subreports/t1work/arch/a5_n8_interior_candidate.json.gz','rb').read()),object_pairs_hook=unique)
A='a3b4f278a322338fb65f60922b4251265288148e1a09fd22882215004e81c324'
proof,removed=proof_payload(arch);cp=canonical(proof)
print('archive proof payload bytes',len(cp),'sha',sha(cp),'excluded',sorted(removed),'excl_sha',sha(canonical(removed)))
fi=[]
for n in('t1-reference-interior-check.json','t1-independent-reference-interior-check.json'):
    raw,d=L(n);f=tc.interior_receipt(d,arch,A,'0345e62ef9bb88fa11640e135d211648611c9536b85fec528d694e94ef57a69f');fi.append(f)
    print(n,sha(raw),'facts_sha',sha(canonical(f)),'roots',f['verified_interior_maxima_enclosures'],'patterns',f['verified_patterns'],'seconds',d.get('seconds'),'leaves',d.get('verified_leaves'),'breakpoints',f['verified_direction_breakpoints'],'disp',f['dispositions'])
print('interior facts equal',canonical(fi[0])==canonical(fi[1]))
fb=[]
for n in('t1-boundary-check.json','t1-independent-boundary-check.json'):
    raw,d=L(n);f=tc.boundary_receipt(d,'adfe1107a326d17cfdd083a2ef9b8ab7ce0aeaa6b906f7a825c53a4fa1da6f08',A,'844b27cf5294cf8494d63707f9862db5a7165fea00e29f8bdd6a6145523457f2');fb.append(f)
    print(n,sha(raw),'facts_sha',sha(canonical(f)),{k:f[k] for k in('verified_edge_maxima_enclosures','verified_corner_maxima','verified_edge_patterns','corner_active_patterns')},'edge_disp',f.get('edge_dispositions'),'seconds',d.get('seconds'))
print('boundary facts equal',canonical(fb[0])==canonical(fb[1]))
cs=[]
for n in('t1-final-composition.json','t1-independent-final-composition.json'):
    raw,d=L(n);d2=copy.deepcopy(d);del d2['inputs']['archived_interior']['path'];cs.append(d2);print(n,sha(raw),len(raw),'retained_sha',sha(canonical(d2)))
print('composition retained equal',canonical(cs[0])==canonical(cs[1]))
