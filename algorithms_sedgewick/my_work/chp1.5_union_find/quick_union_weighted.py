"""
Quick-Union improved
=====================

-> Improvement 1: weighting        ===> no item is to far from the root
============================

Weighted quick-union.
・Modify quick-union to avoid tall trees.
・Keep track of size of each tree (number of objects).
・Balance by linking root of smaller tree to root of larger tree. <- reasonable alternatives: union by height or "rank"



i        0   1   2   3   4   5   6   7   8   9
id[i]    0   1   2   3   4   5   6   7   8   9 ==>

id[i]    6   2   6   4   4   6   6   2   4   4

<- union(4, 3) 3 -> 4 (root of 4 is 4)
<- union(3, 8) 8 -> 4 (8 is in the smaller tree, make 8 point to root of 3 <- weighting)
<- union(6, 5) 5 -> 6 (equal size trees)
<- union(9, 4) 9 -> 4 (9 is in the smaller tree, make 9 point to root of 4 <- weighting)
<- union(2, 1) 1 -> 2 (equal size trees)
<- union(5, 0) 0 -> 6 (5 is in the bigger tree, so 0 goes below, make 0 point to root of 5 <- weighting)
<- union(7, 2) 7 -> 2 (2 is in the bigger tree, so 7 goes below)
<- union(6, 1) 1 -> 6  (equal size trees)
<- union(7, 3) 3 -> 4 (7 in in the bigger tree, so 3 goes below, make 3's root point to 7's root)


Proposition. Depth of any node x is at most lg N <- lg = base-2 logarithm. (E.g. N = 10, depth(x) = 3 ≤ lg N)

Cost model. Number of array accesses (for read or write):

algorithm  initialize union connected
---------------------------------------
quick-find      N       N       1
quick-union     N      N^t      N
weighted QU     N    lg N^†    lg N

Q. Stop at guaranteed acceptable performance? A. No, easy to improve further.

-> Improvement 2: path compression
===================================
QU with path compression: After computing the root of p, set the id of each examined node to point to that root.

-> Two-pass implementation: add second loop to root() to set the id[] of each examined node to the root.

-> Simpler one-pass variant: Make every other node in path point to its grandparent (thereby halving path length).


Weighted quick union (with path compression): makes it possible to solve problems that could not otherwise be addressed.
============================================

algorithm                     worst-case time
---------------------------------------------
quick-find                      M       N
quick-union                     M       N
weighted QU                     N + M  log N
QU + path compression           N + M log N
weighted QU + path compression  N + M lg* N             M union-find operations on a set of N objects
"""


class QuickUnionWeighted:
    def __init__(self, n):
        self.n = n
        self._id = list(range(n))
        # extra array sz[i] to count number of objects in the tree rooted at i.
        self._sz = [1] * n

    # set id of each object to itself (it's own root) (N array accesses)
    def initialize(self, n):
        for i in range(len(n)):
            self._id[i] = i

    # check if p and q have same root (depth of p and q array accesses)
    def connected(self, p, q):
        return self.root(p) == self.root(q)

    # chase parent pointers until reach root (depth of i array accesses)
    def root(self, i):
        while i != self._id[i]:
            # to flatted the tree:
            # Make every other node in path point to its grandparent
            self._id[i] = self._id[self._id[i]]
            i = self._id[i]
        return i

    # Modify quick-union to:
    # ・Link root of smaller tree to root of larger tree.
    # ・Update the sz[] array.
    # (takes constant time, given roots)
    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)

        if i == j:
            return
        if self._sz[i] < self._sz[j]:
            self._id[i] = j
            self._sz[j] += self._sz[i]
        else:
            self._id[j] = i
            self._sz[i] += self._sz[j]


qf = QuickUnionWeighted(10)
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




