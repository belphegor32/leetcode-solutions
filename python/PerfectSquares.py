class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)

        dp[0] = 0

        # we check every possible target and square, then compute the minimum at the current pos in dp
        for targ in range(1, n + 1):
            for s in range(1, targ + 1):
                if targ - (s**2) < 0:
                    break
                dp[targ] = min(dp[targ], 1 + dp[targ - s**2])
        
        return dp[-1]