import sys

"""
Dynamic connectivity
====================

Given a set of N objects.
・Union command: connect two objects.
・Find/connected query: is there a path connecting the two objects?

Connectivity example: Q. Is there a path connecting p and q ? A. Yes

-> Modeling the objects:
When programming, convenient to name objects 0 to N –1.
・Use integers as array index.
・Suppress details not relevant to union-find.

-> Modeling the connections:
We assume "is connected to" is an equivalence relation:
・Reflexive: p is connected to p.
・Symmetric: if p is connected to q, then q is connected to p.
・Transitive: if p is connected to q and q is connected to r, then p is connected to r.

-> Connected components: Maximal set of objects that are mutually connected.

Implementing the operations
===========================
-> Find query: Check if two objects are in the same component.
-> Union command: Replace components containing two objects with their union.

Union-find data type (API)
==========================
Goal: Design efficient data structure for union-find.
・Number of objects N can be huge.
・Number of operations M can be huge.
・Find queries and union commands may be intermixed.
"""


class UnionFind:
    def __init__(self, n):
        self.n = n


# add connection between p and q
def union(p, q):
    pass


# are p and q in the same component?
def connected(p, q):
    pass


# component identifier for p (0 to N – 1)
def find(p):
    pass


# number of components
def count():
    pass

# Dynamic-connectivity client
# ・Read in number of objects N from standard input.
# ・Repeat:
#   – read in pair of integers from standard input
#   – if they are not yet connected, connect them and print out pair


def client():
    n = int(input("Enter number of objects: "))
    # initialize union-find data structure with N objects (0 to N – 1)
    uf = UnionFind(n)

    while not input() is None:
        p = int(input())
        q = int(input())

        if not uf.connected(p, q):
            uf.union(p, q)
            print("{} {}".format(p, q))


