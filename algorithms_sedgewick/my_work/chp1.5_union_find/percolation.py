"""
Percolation (Union-find application)
====================================
A model for many physical systems:
・N-by-N grid of sites.
・Each site is open with probability p (or blocked with probability 1 – p).
・System percolates iff top and bottom are connected by open sites (find a way to go bottom->top through white squares).

Percolation phase transition  --> only solution to find the threshold: through simulation
-----------------------------
When N is large, theory guarantees a sharp threshold p*.
・p > p*: almost certainly percolates.
・p < p*: almost certainly does not percolate.


Monte Carlo simulation   -> Dynamic connectivity solution to estimate percolation threshold
======================
・Initialize N-by-N whole grid to be blocked.
・Declare random sites open until top connected to bottom.
・Vacancy percentage estimates p*.

sites: full open site (connected to top); empty open site (not connected to top); blocked site

Q. How to check whether an N-by-N system percolates?
・Create an object for each site and name them 0 to N^2– 1.
・Sites are in same component if connected by open sites.
・Percolates iff any site on bottom row is connected to site on top row

Problem -> too slow: using just quick union find, we get quadratic brute-force algorithm: N^2 calls to connected()

Solution: Clever trick. Introduce 2 virtual sites (and connections to top and bottom).
・Percolates iff virtual top site is connected to virtual bottom site.
Dynamic connectivity solution to estimate percolation threshold <- efficient algorithm: only 1 call to connected()
"""