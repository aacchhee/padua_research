#!/usr/bin/env python3
"""One-box outward draft calibration, deliberately no cover or acceptance."""
import ctypes
import json
from pathlib import Path
import platform
import subprocess
import time
from n3_native_receipt import identity

ROOT=Path(__file__).resolve().parents[3]
TOPIC=Path(__file__).resolve().parents[1]
OUT=ROOT/'local-output/argmax-bridge-20261105/N3'

def main():
    source=TOPIC/'code/n3_outward.c';include=OUT/'runtime/extracted/usr/include'
    binary=OUT/'n3_outward.so'
    command=['cc','-O3','-std=c11','-Wall','-Wextra','-Wpedantic','-I'+str(include),'-shared','-fPIC',str(source),
             '/lib/x86_64-linux-gnu/libmpfr.so.6','-lm','-o',str(binary)]
    subprocess.run(command,check=True)
    lib=ctypes.CDLL(str(binary));pointer=ctypes.POINTER(ctypes.c_double)
    lib.n3_constants.argtypes=[ctypes.c_int,pointer]
    lib.n3_box.argtypes=[ctypes.c_int,*([ctypes.c_double]*6),ctypes.c_int,pointer]
    lib.n3_mpfr_version.restype=ctypes.c_char_p
    values=(ctypes.c_double*6)();start=time.process_time();lib.n3_constants(33,values)
    constants=list(values[:4]);constant_cpu=time.process_time()-start
    start=time.process_time();status=lib.n3_box(33,.01,.02,.01,.02,constants[2],0.,0,values)
    box_cpu=time.process_time()-start
    assert status==0 and constants[0]<constants[1] and constants[2]<constants[3]
    record={'status':'MEASURED one-box draft calibration; no cover, independent replay or acceptance',
            'command':'python topics/padua-argmax-bridge-20261105/code/n3_outward_calibration.py',
            'compile_command':command,'python':platform.python_version(),'mpfr':lib.n3_mpfr_version().decode(),
            'sources':[identity(p) for p in [source,TOPIC/'code/n3_outward_interval.h',Path(__file__).resolve(),
                                           binary,include/'mpfr.h',OUT/'runtime/libmpfr-dev.deb']],
            'n':33,'pi_interval':constants[:2],'corner_interval':constants[2:],
            'constant_cpu_seconds':constant_cpu,'box':[.01,.02,.01,.02],
            'S_upper':values[0],'corner_upper':values[1],'defect_lower':values[2],
            'box_cpu_seconds':box_cpu,'producer_accepted':False,
            'limits':['One arbitrary box; no measured complete-cover cost or throughput law.',
                      'Candidate arithmetic and nonsmooth specification await separate audit/checker.']}
    (TOPIC/'evidence/n3-outward-calibration.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'constant_cpu_seconds':constant_cpu,'box_cpu_seconds':box_cpu,'status':record['status']}))

if __name__=='__main__':main()
