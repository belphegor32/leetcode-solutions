from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visit = set()
        # directions = [[1, 0], [-1, 0], [0, 1], [0, 1]]

        def dfs(i, r, c):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= rows or c >= cols or word[i] != board[r][c] or (r, c) in visit):
                return False
            
            visit.add((r, c))

            # we check all 4 possible directions and if any of 4 directions have the needed letter we set res = True
            res = (dfs(i + 1, r + 1, c) or
                   dfs(i + 1, r - 1, c) or 
                   dfs(i + 1, r, c + 1) or
                   dfs(i + 1, r, c - 1))

            visit.remove((r, c))
            return res
        
        # check every possible starting possition
        for r in range(rows):
            for c in range(cols):
                if dfs(0, r, c):
                    return True

        return False