from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        l = 0
        r = 0
        cur_prod = 1

        # use sliding window to track if current subarray is greater than k
        while r < len(nums):
            # increase current product
            cur_prod = cur_prod * nums[r]
            
            # if current product is greater than k, we remove values from the left until the product is less than k
            while l <= r and cur_prod >= k:
                cur_prod = cur_prod // nums[l]
                l += 1


            # the number of subarrays in current window will be equal to the length of the window
            res += (r - l) + 1
            r += 1

        return res