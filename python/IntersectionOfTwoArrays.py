from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        hashmap = {}
        for n in nums1:
            hashmap[n] = 1
        
        for n in nums2:
            ''' 
            all the values in nums1 are in hashmap with value 1, when we find the value,
            when we find the value, that is in the hashmap and nums2, we decrease it, so it can never be 1 again
            '''
            if n in hashmap and hashmap[n] == 1:
                result.append(n)
                hashmap[n] = hashmap[n] - 1
        
        return result