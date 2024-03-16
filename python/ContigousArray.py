from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefixes = {}
        zeros = 0
        ones = 0
        res = 0

        for i, n in enumerate(nums):
            # get count of 0s and 1s
            if n == 0:
                zeros += 1
            elif n == 1:
                ones += 1

            # map current difference to index
            if zeros - ones not in prefixes:
                prefixes[zeros - ones] = i
            
            # if zeros == ones, then the window starts at the begging and we can just assign res to len of the window
            if zeros == ones:
                res = zeros + ones
            # else if we need to check if current diff is in prefixes, and remove this prefix, so we get equal ammount of 1s and 0s
            elif zeros - ones in prefixes:
                index = prefixes[zeros - ones]
                res = max(res, i - index)
        
        return res