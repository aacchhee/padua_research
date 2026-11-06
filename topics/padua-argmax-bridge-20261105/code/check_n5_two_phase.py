#!/usr/bin/env python3
"""Targeted independent N5-04 diagnostics; no author-code imports.

Finite triangular cosine sums provide the polynomial oracle. Small-degree
physical cardinal sums separately check the periodic half normalization.
These are measured diagnostics, not proof premises or phase certificates.
"""
import hashlib
import json
import pathlib
import platform
import time
from fractions import Fraction as F
import mpmath as mp

ROOT=pathlib.Path(__file__).resolve().parents[3]
TOPIC=ROOT/'topics/padua-argmax-bridge-20261105'
PINS={
 'theory/N5-two-phase-defect.md':'de47e7d806f6c4d5107148516c7bec6686ba27c60b1d872572564ec94b7e0646',
 'code/n5_two_phase_defect.py':'fd1402000f2bd0b06477396270ea797237b70d2f4295d09246d03468ef77dc63',
 'evidence/n5-two-phase-defect.json':'76ee7b68c3e0ec553765dba71ba97f2ea3598164c331a67f794be1d74a5aa0f8'}


def identity(path):
 raw=path.read_bytes()
 return {'path':str(path),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}


def cosines(u,n):
 return [mp.cos(i*u) for i in range(n+1)]


def primitive(n,u,v):
 """Corrected triangular polynomial, with an accumulated second-index sum."""
 cu=cosines(u,n);cv=cosines(v,n)
 prefix=[];total=mp.mpf(0)
 for j in range(n+1):
  total+=(1 if j==0 else 2)*cv[j];prefix.append(total)
 return mp.fsum((1 if i==0 else 2)*cu[i]*prefix[n-i] for i in range(n+1))-cu[n]


def selected_case(n,J,q,ast,bst,branch=None):
 a,b=mp.mpf(ast),mp.mpf(bst);m=n+1;phi=(q*mp.pi+b)/m
 assert J in (0,n) and (J+q)%2==1 and 0<q<m
 assert abs(a)+abs(b)<=mp.mpf('.5') and (a>=0 if J==0 else a<=0)
 gamma=min(phi,mp.pi-phi);distance=min(q,m-q)
 pairs=[];rowcounts=[]
 if distance<=4:
  category='near';top=q>m/2;eta=distance%2 if top else 1-distance%2
  for ell in range(n+1):
   if F(3*n,8)<=ell<=F(n,2):
    pairs.append((n-ell if top else ell,ell+eta))
  floor=mp.mpf(1)/1728;numfloor=mp.mpf(1)/8
  assert len(pairs)>=F(n,16)
 else:
  assert gamma>4*mp.pi/n
  category=branch or ('small' if gamma<=mp.pi/6 else 'middle')
  assert (gamma<=mp.pi/6+mp.mpf('1e-80') if category=='small' else gamma>=mp.pi/6-mp.mpf('1e-80'))
  for k in range(1,m):
   bp=(k if phi<=mp.pi/2 else m-k)*mp.pi/m
   if not (mp.pi/3<=bp<=mp.pi/2 if category=='small' else mp.pi/12<=bp<=mp.pi/6):continue
   center=bp if category=='small' else gamma
   width=gamma if category=='small' else bp
   row=[(r,k) for r in range(2*n) if (r+k-J)%2==0 and
        center-width/2<=(r*mp.pi+a)/n<=center+width/2]
   assert len(row)>=(n*gamma/(4*mp.pi) if category=='small' else mp.mpf(n)/48)
   pairs.extend(row);rowcounts.append(len(row))
  assert len(rowcounts)>=(mp.mpf(m)/12 if category=='small' else mp.mpf(m)/16)
  floor=7/(1536*mp.pi) if category=='small' else mp.mpf(7)/12288
  numfloor=mp.mpf(7)/32
 total=mp.mpf(0);maxerror=mp.mpf(0);minnum=mp.inf
 for r,k in pairs:
  assert (r+k-J)%2==0 and 0<k<m and 0<=r<2*n
  u=(r*mp.pi+a)/n;values=[];denominators=[]
  for sign in (-1,1):
   v=phi+sign*k*mp.pi/m
   denominator=mp.cos(u)-mp.cos(v)
   numerator=(mp.cos(a)+mp.cos(b))*(1+mp.cos(v))/2-mp.sin(a)*mp.sin(u)/2+mp.sin(b)*mp.sin(v)/2
   half=(-1)**r*primitive(n,u,v)/2
   assert numerator>=numfloor-mp.mpf('1e-80') and abs(denominator)>mp.mpf('1e-70')
   maxerror=max(maxerror,abs(half-numerator/denominator));minnum=min(minnum,numerator)
   values.append(half);denominators.append(denominator)
  assert denominators[0]*denominators[1]<0 and values[0]*values[1]<0
  total+=(abs(values[0])+abs(values[1])-abs(sum(values)))/(n*m)
 assert maxerror<mp.mpf('1e-75') and total>=floor>mp.mpf(1)/2048
 return {'n':n,'J':J,'q':q,'alpha':ast,'beta':bst,'branch':category,
         'pairs':len(pairs),'subset_defect':mp.nstr(total,30),'floor':mp.nstr(floor,30),
         'minimum_numerator':mp.nstr(minnum,20),'max_identity_error':mp.nstr(maxerror,12)}


def normalization_case(n,J,q,ast,bst):
 a,b=mp.mpf(ast),mp.mpf(bst);m=n+1;N=n*m
 theta=(J*mp.pi+a)/n;phi=(q*mp.pi+b)/m
 board={(r,s):primitive(n,(r*mp.pi+a)/n,(s*mp.pi+b)/m)
        for r in range(2*n) for s in range(2*m) if (r+s)%2}
 S=mp.fsum(abs(v) for v in board.values())/(2*N)
 Qperiodic=mp.mpf(0);orbit=mp.mpf(0)
 for (r,s),v in board.items():
  partner=board[r,(2*q-s)%(2*m)];rr=(2*J-r)%(2*n)
  Qperiodic+=abs(v)+abs(partner)-abs(v+partner)
  orbit+=abs(v+partner+board[rr,s]+board[rr,(2*q-s)%(2*m)])
 Qperiodic/=4*N;orbit/=8*N
 Qhalf=mp.mpf(0)
 for k in range(m+1):
  weight=(mp.mpf('.5') if k in (0,m) else mp.mpf(1))/N
  for r in range(2*n):
   if (r+k-J)%2:continue
   u=(r*mp.pi+a)/n
   hp=(-1)**r*primitive(n,u,phi+k*mp.pi/m)/2
   hm=(-1)**r*primitive(n,u,phi-k*mp.pi/m)/2
   Qhalf+=weight*(abs(hp)+abs(hm)-abs(hp+hm))
 # Direct individual cardinal values from the corrected orthogonal kernel.
 ct=cosines(theta,n);cp=cosines(phi,n);actual=mp.mpf(0)
 for j in range(n+1):
  cj=cosines(j*mp.pi/n,n)
  for k in range(m+1):
   if (j+k)%2:continue
   ck=cosines(k*mp.pi/m,n)
   cardinal=mp.mpf(0)
   for i in range(n+1):
    for h in range(n+1-i):
     coef=(1 if i==0 else 2)*(1 if h==0 else 2)-int((i,h)==(n,0))
     cardinal+=coef*ct[i]*cj[i]*cp[h]*ck[h]
   weight=mp.mpf(2)/N*(mp.mpf('.5') if j in (0,n) else 1)*(mp.mpf('.5') if k in (0,m) else 1)
   actual+=weight*abs(cardinal)
 error=max(abs(Qhalf-Qperiodic),abs(actual-orbit))
 assert error<mp.mpf('1e-75') and S-actual>=Qperiodic-mp.mpf('1e-75')
 if q in (0,m):assert abs(S-actual)<mp.mpf('1e-75')
 return {'n':n,'J':J,'q':q,'alpha':ast,'beta':bst,'actual_lambda':mp.nstr(actual,30),
         'primitive':mp.nstr(S,30),'projection':mp.nstr(Qperiodic,30),'max_identity_error':mp.nstr(error,12)}


def main():
 before=[identity(TOPIC/p) for p in PINS]
 assert all(row['sha256']==PINS[str(pathlib.Path(row['path']).relative_to(TOPIC))] for row in before)
 start=time.process_time();mp.mp.dps=90
 assert F(15,16)*F(2,5)-F(1,4)==F(1,8)
 assert F(15,32)-F(1,4)==F(7,32)
 assert F(65,128)<F(9,8)
 assert F(1,1728)>F(1,2048) and F(7,6144)>F(1,2048) and F(7,12288)>F(1,2048)
 assert F(7,576)+F(112,225)==F(66087,129600)<1
 cases=[(64,0,1,'.5','0'),(64,64,63,'-.25','.25'),
        (65,65,4,'-.25','-.25'),(65,65,62,'-.25','.25'),
        (64,0,5,'.25','-.25'),(65,65,6,'-.25','.25'),
        (65,0,11,'.25','-.25'),(65,0,11,'.25','.25'),
        (65,0,55,'.25','-.25'),(65,0,55,'.25','.25'),
        (65,65,32,'-.5','0')]
 rows=[selected_case(*case) for case in cases]
 rows += [selected_case(65,0,11,'.25','0',branch) for branch in ('small','middle')]
 norms=[normalization_case(*case) for case in [(4,0,1,'.25','-.25'),(5,5,2,'-.25','.25'),(4,0,5,'0','0')]]
 assert before==[identity(TOPIC/p) for p in PINS]
 report={'scope':'MEASURED targeted independent diagnostics; analytic review separate',
         'input_rules_sha':'121ae257a71564025ddc2da8f53d19478f5d7dd4','sources':before,
         'script':identity(pathlib.Path(__file__).resolve()),
         'command':'python topics/padua-argmax-bridge-20261105/code/check_n5_two_phase.py',
         'python':platform.python_version(),'mpmath':mp.__version__,'decimal_digits':90,
         'tolerance':'1e-75 for polynomial comparisons; diagnostics only',
         'selected_cases':rows,'normalization_cases':norms,'exact_rational_checks':True,
         'passed':True,'cpu_seconds':time.process_time()-start,
         'limitations':'No author imports, full108-case rerun, phase certificate or primitive maximum claim'}
 path=TOPIC/'evidence/independent-n5-two-phase.json';path.write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps({'passed':True,'selected_cases':len(rows),'normalization_cases':len(norms),
                   'cpu_seconds':report['cpu_seconds']}))


if __name__=='__main__':main()
