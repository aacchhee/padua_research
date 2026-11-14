"""OPERATIONAL FIXTURE ONLY. Never a mathematical or scientific checker."""
from fractions import Fraction
def exact_hex(value): return Fraction.from_float(float.fromhex(value))
def rational(value): return Fraction(value)
def verify_essential(receipt, identity):
    assert receipt['fixture'] == 'NO_SCIENCE'
    return {'fixture': 'NO_SCIENCE'}
