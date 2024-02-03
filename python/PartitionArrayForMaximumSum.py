from typing import List
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        # use caching to reduce computation of recursive calls the result of which we already now
        cache = {}

        def rec(i):
            if i >= len(arr):
                return 0
            if i in cache:
                return cache[i]
            
            max_elem = 0
            res = 0

            # we got from i to min of length of arr and i + k, since i + k might be out of bounds, the we just go until the end of arr
            for j in range(i, min(len(arr), i + k)):
                max_elem = max(max_elem, arr[j])
                window_size = j - i + 1
                # we sum up the sum of elements of current window plus the next window, which we get by recursive call, then compare it win cur res
                res = max(res, max_elem * window_size + rec(j + 1))
            
            cache[i] = res
            return res

        return rec(0)

# circular array solution from editorial
class Solution2:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0] * k
        dp[0] = arr[0]

        for i in range(1, len(arr)):
            cur_max = 0
            max_at_cur_index = 0
            for j in range(i, i - k, - 1):
                if j < 0:
                    break
                cur_max = max(cur_max, arr[j])
                window_size = i - j + 1
                cur_sum = cur_max * window_size
                if j > 0:
                    sub_sum = dp[(j - 1) % k]
                else:
                    sub_sum = dp[-1]
                max_at_cur_index = max(max_at_cur_index, cur_sum + sub_sum)

            dp[i % k] = max_at_cur_index
        
        return dp[(len(arr) - 1) % k]