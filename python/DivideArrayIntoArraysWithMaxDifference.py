from typing import List
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []
        l = 0

        # if after sorting the last elem - first elem is greater than k, then the whole list is impossible to divide
        while l < len(nums):
            if nums[l+2] - nums[l] > k:
                return []
            res.append(nums[l:l + 3])
            l += 3
        
        return res