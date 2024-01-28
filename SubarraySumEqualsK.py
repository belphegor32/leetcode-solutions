from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        res = 0 
        cur = 0

        for n in nums:
            cur += n
            dif = cur - k

            res += count[dif]
            count[cur] += 1
        
        return res