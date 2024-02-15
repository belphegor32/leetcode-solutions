from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # deals with condition that every next side should be >= than the previous
        nums.sort()

        total = 0
        maxTotal = -1

        for i in nums:
            # all sides combined should be longer than the longest side alone
            if total > i:
                maxTotal = total + i
            total += i

        
        return maxTotal