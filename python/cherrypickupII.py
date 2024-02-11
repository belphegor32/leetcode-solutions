from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [-1, 0, 1]
        cache = {}

        def dfs(r, c1, c2):
            if (r, c1, c2) in cache:
                return cache[(r, c1, c2)]
            if c1 == c2 or min(c1, c2) < 0 or max(c1, c2) == cols:
                return 0
            if r == rows - 1:
                return grid[r][c1] + grid[r][c2]

            res = 0

            # check all 9 possible cases
            for c1_delta in directions:
                for c2_delta in directions:
                    res = max(res, dfs(r + 1, c1 + c1_delta, c2 + c2_delta))

            cache[(r, c1, c2)] = res + grid[r][c1] + grid[r][c2]

            return cache[(r, c1, c2)]
        
        return dfs(0, 0, cols - 1)