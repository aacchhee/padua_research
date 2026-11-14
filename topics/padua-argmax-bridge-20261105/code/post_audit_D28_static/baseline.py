"""Strict pinned D21 baseline parsing and exact fresh-vs-old diagnostics.
No native work, imported endpoint evaluation, or old value enters new math.
"""
from fractions import Fraction as F
import math
import checker as C

FILES={
 'receipt':'evidence/d21-static6912.json',
 'final':'evidence/d21-static6912-final-accounting.json',
 'observation':'evidence/d21-static6912-primary-observation.json',
}
D21_FREEZE_SHA='c25384c68de1691de2342d1d012c3f0d08e99458dfffa3652dfe36befed607bc'
WIDTH=F(1,50000)

def binary(s):
 if not isinstance(s,str):raise ValueError('hex string required')
 x=float.fromhex(s)
 if not math.isfinite(x) or x.hex()!=s:raise ValueError('canonical finite binary64 endpoint required')
 return F.from_float(x)

def load(R,required):
 topic=R.ROOT/'topics/padua-argmax-bridge-20261105'
 docs={name:R.strict_json(topic/path,16384) for name,path in FILES.items()}
 old,final,observation=(docs[k] for k in ('receipt','final','observation'))
 if final.get('complete') is not True or final.get('first_failure') is not None or final.get('result')!='EXACT_STATIC_COVER_ACCEPTED_PENDING_INDEPENDENT_REPLAY':raise ValueError('D21 final accounting incomplete')
 if type(observation.get('observed_exit_code')) is not int or observation.get('observed_exit_code')!=0 or observation.get('final_accounting_complete') is not True:raise ValueError('D21 root actual exit observation absent')
 artifacts=observation.get('artifacts')
 if not isinstance(artifacts,list) or len(artifacts)!=2:raise ValueError('D21 observation artifact identities')
 for name in ('receipt','final'):
  ident=R.identity(topic/FILES[name]);matches=[row for row in artifacts if row.get('path')==str((topic/FILES[name]).relative_to(R.ROOT))]
  if len(matches)!=1 or any(matches[0].get(k)!=ident[k] for k in ('bytes','sha256')):raise ValueError('D21 observed artifact differs')
 if old.get('format')!='D21-static-allrow-v1' or type(old.get('n')) is not int or old['n']!=6912 or old.get('freeze',{}).get('sha256')!=D21_FREEZE_SHA or old.get('certificate',{}).get('sha256')!=C.TREE_SHA:raise ValueError('D21 source/tree/degree identity')
 if old.get('columns')!=['api','a','b','lower_hex','upper_hex','radius_hex','counts','CPU'] or old.get('count_columns')!=['retained','direct','blocks','maxdirect','maxblocks','ordinary']:raise ValueError('D21 row schema')
 rows={}
 if not isinstance(old.get('rows'),list) or len(old['rows'])!=41:raise ValueError('D21 all41 rows required')
 for row in old['rows']:
  if not isinstance(row,list) or len(row)!=8:raise ValueError('D21 row shape')
  api,a,b,lo,hi,rad,counters,cost=row
  if api!='S' or not isinstance(a,str) or not isinstance(b,str):raise ValueError('D21 API/rational key')
  key=F(a),F(b)
  if (str(key[0]),str(key[1]))!=(a,b) or C.canonical(*key)!=key or key in rows:raise ValueError('D21 duplicate/noncanonical key')
  lower,upper,radius=map(binary,(lo,hi,rad))
  if not 0<=lower<=upper or radius<0 or len(counters)!=6 or any(type(x) is not int or x<0 for x in counters):raise ValueError('D21 endpoints/counters')
  if not isinstance(cost,(int,float)) or isinstance(cost,bool) or not math.isfinite(cost) or cost<0:raise ValueError('D21 CPU')
  rows[key]={'lower':lower,'upper':upper,'radius':radius,'counts':counters}
 if set(rows)!=set(required):raise ValueError('D21 key closure differs from supplied tree')
 return rows,{k:R.identity(topic/path) for k,path in FILES.items()}

def compare(key,raw,old):
 if raw['api']!='S' or raw['n']!=6912 or tuple(map(F,raw['key']))!=key:raise ValueError('fresh comparison identity')
 native=raw['native']
 if native['returncode']!=0 or native['counts']!=old['counts']:raise ValueError('fresh/old per-point counters differ')
 lo,hi,radius=map(binary,native['raw_hex'])
 if not 0<=lo<=hi or radius<0:raise ValueError('fresh endpoints')
 if max(lo,old['lower'])>min(hi,old['upper']):raise ValueError('fresh/old disjoint enclosures')
 width=hi-lo;gap=hi-old['lower']
 if width>WIDTH:raise ValueError('fresh outward endpoint width exceeds2e-5')
 if gap>WIDTH:raise ValueError('fresh upper minus D21 lower exceeds2e-5')
 return width,old['upper']-old['lower'],gap
