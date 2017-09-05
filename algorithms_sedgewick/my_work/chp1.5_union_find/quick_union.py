"""
Quick-union [lazy approach] - avoid doing work until we have to
==========================

Data structure.
・Integer array id[] of length N.
・Interpretation: id[i] is parent of i.

Root of i is id[id[id[...id[i]...]]].   <- keep going until it doesn’t change (algorithm ensures no cycles)

i        0   1   2   3   4   5   6   7   8   9         <- root of 3 is 9: 3 -> 4 ->  9
id[i]    0   1   9   4   9   6   6   7   8   9

Find: Check if p and q have the same root.             <- root of 3 is 9, root of 5 is 6 => 3 and 5 are not connected

Union: To merge components containing p and q, set the id of p's root to the id of q's root.

i        0   1   2   3   4   5   6   7   8   9
id[i]    0   1   9   4   9   6   6   7   8   6         <- to union(3, 5), only one value changes
                                                          3's root becomes child of 5's root

Quick-union is also too slow
=============================

Quick-find vs. Quick-Union
==============================

Cost model. Number of array accesses (for read or write):

algorithm   initialize union connected
--------------------------------------
quick-find      N       N     1
quick-union     N      N^t    N     <- worst case       (N^t, t includes cost of finding roots)


Quick-find defect.
・Union too expensive (N array accesses).
・Trees are flat, but too expensive to keep them flat.

Quick-union defect.
・Trees can get tall.
・Find too expensive (could be N array accesses).
"""


class QuickUnion:
    def __init__(self, n):
        self.n = n
        self._id = list(range(n))

    # set id of each object to itself (N array accesses)
    def initialize(self, n):
        for i in range(n):
            self._id[i] = i

    # chase parent pointers until reach root (depth of i array accesses)
    def root(self, i):
        while i != self._id[i]:
            i = self._id[i]
        return i

    # check if p and q have same root (depth of p and q array accesses)
    def connected(self, p, q):
        return self.root(p) == self.root(q)

    # change root of p to point to root of q (depth of p and q array accesses)
    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)

        self._id[i] = j


qf = QuickUnion(10)
qf.union(4, 3)
qf.union(3, 8)
# change 1st to match 2nd
qf.union(6, 5)
qf.union(9, 4)
qf.union(2, 1)
print(qf.connected(8, 9))
print(qf.connected(5, 0))
qf.union(5, 0)
qf.union(7, 2)
qf.union(6, 1)