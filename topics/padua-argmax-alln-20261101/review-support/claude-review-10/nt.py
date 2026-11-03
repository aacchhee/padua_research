import importlib.util, os, sys, shutil, argparse, pathlib, subprocess, json, hashlib
spec = importlib.util.spec_from_file_location('cs', '/home/user/padua_research/tools/cold_storage.py'); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
mode = sys.argv[1]
if mode == 'nt': os.name = 'nt'
elif mode == 'nofollow': delattr(os, 'O_NOFOLLOW')
sys.argv = ['cold_storage.py', *sys.argv[2:]]; m.main()
