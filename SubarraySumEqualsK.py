from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # make a count dict to keep a track of prefix sums
        count = defaultdict(int)
        # base case in the dict for prefix sum = 0
        count[0] = 1
        res = 0 
        cur = 0

        for n in nums: 
            cur += n
            # find the diffrence to search for how many arrays can we use to satisfy the sum k that we look for
            dif = cur - k

            # search and add the number of arrays with prefix sum dif
            res += count[dif]
            # increment the prefix sum dict value at key cur, since we just understood, that it satisfies the value we search for
            count[cur] += 1
        
        return res