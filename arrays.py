import numpy as np
import sympy as sym
import argparse

parser = argparse.ArgumentParser(
    description="Fa el producte (·) entre dos matrius"
)
parser.add_argument("-a", help="Matriu `a`", required=True)
parser.add_argument("-b", help="Matriu `b`", required=True)
args = parser.parse_args()

a = []
for token in args.a.split(";"):
    a.append([])
    for nmbr in token.split(" "):
        a[-1] += [sym.sympify(nmbr)]
b = []
for token in args.b.split(";"):
    b.append([])
    for nmbr in token.split(" "):
        b[-1] += [sym.sympify(nmbr)]

print("a = {}".format(a))
print("b = {}".format(b))
print("a·b =\n",np.dot(a,b))