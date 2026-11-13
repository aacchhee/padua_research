import importlib.util, sys, os, json
from pathlib import Path
import numpy as np
B=Path(sys.argv[1]); src=B/'src/topics/padua-3d-20261106/code/t9_maxima.py'
out=B/'out'; out.mkdir(exist_ok=True)
_save=np.save
np.save=lambda p,a,*k,**kw:_save(str(out/Path(p).name),a,*k,**kw)
sys.path.insert(0,str(src.parent))
spec=importlib.util.spec_from_file_location('t9_maxima',src); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
m.TOP=out/'top'; (m.TOP/'evidence').mkdir(parents=True,exist_ok=True)
m.main()
