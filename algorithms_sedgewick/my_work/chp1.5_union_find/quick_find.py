"""
Quick-find [eager approach]
===========================
-> Data structure.
・Integer array id[] of length N.
・Interpretation: p and q are connected iff they have the same id.

-> Find: Check if p and q have the same id: id[1] = 1, id[6] = 0 => 6 and 1 are not connected

entry   0 1 2 3 4 5 6 7 8 9         {0, 5, 6}, {1, 2, 7}, {3, 4, 8, 9} are connected
id[]    0 1 1 8 8 0 0 1 8 8

-> Union: To merge components containing p and q, change all entries whose id equals id[p] to id[q].

        0 1 2 3 4 5 6 7 8 9         after union of 6 and 1 => need to change entries the same component as 6: {0, 5, 6}
id[]    1 1 1 8 8 1 1 1 8 8         problem: when huge no. of values, many entries to change


Quick-find is too slow - for huge problems
======================
Cost model. Number of array accesses (for read or write).

algorithm    initialize union connected
---------------------------------------   (order of growth of number of array accesses)
quick-find      N        N     1

Union is too expensive. It takes N^2 (quadratic) array accesses to process a sequence of N union commands on N objects.
Worst case: all entries, except id[q] are changed from id[p] to id[q].
"""


class QuickFind:
    def __init__(self, n):
        self.n = n
        self._id = list(range(n))

    # set id of each object to itself (its own root) (N array accesses)
    def initialize(self, n):
        for i in range(n):
            self._id[i] = i

    # check whether p and q are in the same component (2 array accesses)
    def connected(self, p, q):
        return self._id[p] == self._id[q]

    # change all entries with id[p] to id[q] (at most 2N + 2 array accesses)
    def union(self, p, q):
        pid = self._id[p]
        qid = self._id[q]

        for i in range(0, len(self._id)):
            if self._id[i] == pid:
                self._id[i] = qid

qf = QuickFind(10)
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

