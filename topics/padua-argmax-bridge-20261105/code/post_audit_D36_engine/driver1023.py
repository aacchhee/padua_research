"""The sole prospective D36 pilot: exact n1023, no queue or other case."""
import sys

def main():
 if sys.argv[1:]!=['--run-once']:raise SystemExit('Only reviewed --run-once fixed n1023 pilot is supported')
 import engine
 engine.main(['--mode','produce','--n','1023','--output','local-output/argmax-bridge-20261105/post-audit-D36/pilot1023','--run-once'])
if __name__=='__main__':main()
