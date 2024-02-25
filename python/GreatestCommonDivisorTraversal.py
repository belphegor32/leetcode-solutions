from typing import List

class UnionFind:
    def __init__(self, number):
        self.parent = [i for i in range(number)]
        self.rank = [1] * number
        self.count = number

    # find the parent of the current child we are looking at, if its already a parent of itself, we just return
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        # find both parents of x and y
        par_x, par_y = self.find(x), self.find(y)
        # if parents were already the same, we dont do anything
        if par_x == par_y:
            return 

        # if parents are different, we merge the child with the lower rank parent to the higher rank parent
        if self.rank[par_x] < self.rank[par_y]:
            self.parent[par_x] = par_y
            self.rank[par_y] += self.rank[par_x]
        else:
            self.parent[par_y] = par_x
            self.rank[par_x] += self.rank[par_y]

        # decreace the number of groups by 1, since we merged 2 groups together
        self.count -= 1

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        uf = UnionFind(len(nums))

        # map index -> factor
        factor_index = {}
        for i, n in enumerate(nums):
            f = 2
            # we want to iterate until sqrt(n), f * f <= n deals with by 1 offset issues
            while f * f <= n:
                if n % f == 0:
                    if f in factor_index:
                        # if we have seen the factor, we just union it with the same factor in map
                        uf.union(i, factor_index[f])
                    else:
                        # if we have not seen this factor yet, we add it to the map
                        factor_index[f] = i
                    while n % f == 0:
                        n //= f
                f += 1
            # if there are still factors left after our while loop (n != 1), then we get them too
            if n > 1:
                if n in factor_index:
                    uf.union(i, factor_index[n])
                else:
                    factor_index[n] = i
        
        return uf.count == 1
