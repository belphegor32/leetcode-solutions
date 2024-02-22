from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # since we are skipping first and last value, if the len of nums is 0, then we will skip the only value, so we wont rob any houses
        if len(nums) == 1:
            return nums[0]
            
        maxRob = 0
        def robI(arr):
            rob1 = 0
            rob2 = 0
            # rob1 is the max computed right before rob2, rob2 will check houses that go after rob1, and it will also store the maximum which we can rob
            for i in arr:
                temp = max(rob1 + i, rob2)
                rob1 = rob2
                rob2 = temp
            
            return rob2
        
        # since the houses are arranged in a circle, we cant rob last and first house together, even if they give us the max, since they are adjacent
        maxRob = max(robI(nums[1:]), robI(nums[:-1]))

        return maxRob