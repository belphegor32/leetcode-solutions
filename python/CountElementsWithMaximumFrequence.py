from typing import List

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # just use a hashmap
        count = {}
        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
        
        maxFreq = 0
        for k in count:
            maxFreq = max(maxFreq, count[k])
        res = 0
        for c in count:
            if count[c] == maxFreq:
                res += maxFreq
        
        return res