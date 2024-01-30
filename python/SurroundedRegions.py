class Solution:
    def solve(self, board) -> None:
        rows = len(board)
        cols = len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        
        # change all "O"s to other any other letter recursively
        def capture(r, c):
            if (r < 0 or c < 0 or r == rows or c == cols or board[r][c] != "O"):
                return 
            board[r][c] = "N"

            for dr, dc in directions:
                capture(r + dr, c + dc)
        
        for r in range(rows):
            for c in range(cols):
                if (board[r][c] == "O" and (r in [0, rows - 1] or c in [0, cols - 1])):
                    capture(r, c)
        
        # change all "O"s to "X"
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        # change temporary letter to "O"
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "N":
                    board[r][c] = "O"
