from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        def count(gl):
            if gl < 0:
                return 0
            
            res = 0
            l = 0
            total = 0
            for r in range(len(nums)):
                total += nums[r]

                # if current window sum is more than goal, decrease it
                while total > gl:
                    total -= nums[l]
                    l += 1

                # add window size, because it will equal to number of subarays ending at the last index of cur window
                res += (r - l + 1)

            return res
        
        # number of subarrays will equal to numbers we computed with our algorigthm minus numbers of arrays with the goal that is less by one
        return count(goal) - count(goal - 1)