from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        def dfs(i):
            if i >= len(nums):
                return []
            if i in cache:
                return cache[i]
            
            res = [nums[i]]
            # if the next value in nums is divisble by cur value in res, we call a recursive call on the index of this value
            for j in range(i + 1, len(nums)):
                if nums[j] % nums[i] == 0:
                    temp = [nums[i]] + dfs(j)
                    if len(temp) > len(res):
                        res = temp

            cache[i] = res
            return res
        
        # we sort the input, because if the value is larger we only need to check if its divisible by a smaller value in the list
        nums.sort()
        cache = {}
        res = []
        
        # starting possition can be any, so we need to check every possible starting position for out answer
        for i in range(len(nums)):
            tmp = dfs(i)
            if len(tmp) > len(res):
                res = tmp
    
        return res