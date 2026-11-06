"""Fresh pinned C11 build, accepted builder closure policy, two row captures."""
import hashlib,pathlib
HERE=pathlib.Path(__file__).resolve().parent
ROOT=HERE.parents[3];CODE=HERE.parent
RAW=ROOT/'local-output/argmax-bridge-20261105/post-audit-D01/far'
BUILDER=CODE/'phase_checker/build_snapshot_r9.py'
def identity(p):
 p=pathlib.Path(p).resolve();b=p.read_bytes();return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def build():
 point=CODE/'cheap_rows_C11/point.cpp';partial=CODE/'cheap_rows_C11/partial.cpp'
 original=point.read_text();before={str(p):identity(p) for p in [point,partial,BUILDER]}
 generated=original.replace('#include "partial.cpp"','#include "'+str(partial)+'"\nstatic std::vector<B>* d01_capture=nullptr;')
 a='total=total+absolute(finiteF(n,r,k,af,bf));stats.retained++;'
 b='total=total+absolute(finiteF(n,r,k,af,bf));if(d01_capture)(*d01_capture)[r]=(*d01_capture)[r]+absolute(finiteF(n,r,k,af,bf));stats.retained++;'
 assert generated.count(a)==1;generated=generated.replace(a,b)
 a='total=total+row;';b='total=total+row;if(d01_capture)(*d01_capture)[r]=row;'
 assert generated.count(a)==1;generated=generated.replace(a,b)
 (RAW/'point_rows.cpp').write_text(generated)
 (RAW/'native.cpp').write_bytes((HERE/'native.cpp').read_bytes())
 text=BUILDER.read_text().replace("LOCAL=ROOT/'local-output/argmax-bridge-20261105/phase-r9'",'LOCAL=pathlib.Path('+repr(str(RAW))+')')
 text=text.replace('source_path=pathlib.Path(__file__).with_name(KERNEL_SOURCES[kernel_variant])','source_path=pathlib.Path('+repr(str(RAW/'native.cpp'))+')')
 text=text.replace("include=['-I'+str(INC)]","include=['-I'+str(INC),'-I'+"+repr(str(RAW))+']')
 ns={'__file__':str(BUILDER)};exec(compile(text,str(BUILDER),'exec'),ns)
 binary,manifest=ns['build']()
 assert before=={str(p):identity(p) for p in [point,partial,BUILDER]}
 manifest.update(frozen_inputs=list(before.values()),instrumentation=identity(RAW/'point_rows.cpp'),driver=identity(HERE/'run.py'),build_driver=identity(__file__))
 return binary,manifest,ns
