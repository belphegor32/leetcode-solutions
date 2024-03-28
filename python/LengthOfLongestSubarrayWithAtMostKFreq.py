from typing import List

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        res = 0

        count = {}
        l = 0
        r = 0

        while r < len(nums):
            if nums[r] in count:
                count[nums[r]] += 1
            else:
                count[nums[r]] = 1

            # if the element we just increased in hashmap is more than k, we need to remove the element we increased from the left side
            while count[nums[r]] > k:
                count[nums[l]] -= 1
                l += 1

            # the result will be the size of the window
            res = max(res, (r - l) + 1)
            r += 1

        return res 